#!/usr/bin/env python3
"""Write HW5 and HW6 dual scores into a copied course workbook.

The original workbook is never overwritten. This script uses LibreOffice UNO
instead of rewriting the XLSX package directly so cell formatting, widths, and
styles are preserved as much as practical.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import subprocess
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import uno
from com.sun.star.beans import PropertyValue


ROOT = Path(__file__).resolve().parents[1]
GRADING = ROOT / "grading"
REPORTS = ROOT / "reports"
DEFAULT_INPUT = ROOT / "course_materials" / "hw6" / "raw" / "(114下)深度學習成績和分組.xlsx"
DEFAULT_OUTPUT = ROOT / "course_materials" / "hw6" / "renamed" / "(114下)深度學習成績和分組_hw5_hw6_scored.xlsx"
DEFAULT_HW5 = GRADING / "hw5" / "scores.csv"
DEFAULT_HW6 = GRADING / "hw6" / "combined_summary.csv"
DEFAULT_UNMATCHED = GRADING / "hw5_hw6_workbook_unmatched_students.csv"
DEFAULT_REPORT = REPORTS / "hw5_hw6_workbook_writeback_report.md"
IGNORE_NAMES = {"程式碼乾淨/註解/用心程度", "基本分", "程式不動(有努力)", "交白卷/缺交"}
TARGET_HEADERS = {
    "HW5": "hw5",
    "HW6(圖)": "hw6_figure",
    "HW6(code)": "hw6_code",
}
UNMATCHED_FIELDS = [
    "student_name",
    "student_id",
    "homework",
    "status",
    "reason",
    "workbook_sheet",
    "workbook_row",
    "action",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Write HW5, HW6(圖), and HW6(code) scores to a workbook copy.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--hw5-scores", type=Path, default=DEFAULT_HW5)
    parser.add_argument("--hw6-summary", type=Path, default=DEFAULT_HW6)
    parser.add_argument("--unmatched", type=Path, default=DEFAULT_UNMATCHED)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--dry-run", action="store_true", help="Inspect and report without saving workbook.")
    parser.add_argument("--apply", action="store_true", help="Save workbook copy and write report/CSV metadata.")
    parser.add_argument("--port", type=int, default=2016)
    return parser.parse_args()


def prop(name: str, value: object) -> PropertyValue:
    item = PropertyValue()
    item.Name = name
    item.Value = value
    return item


def file_url(path: Path) -> str:
    return path.resolve().as_uri()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def numeric(value: str) -> float:
    text = value.strip()
    if not text:
        raise ValueError("missing numeric value")
    return float(text)


def start_office(port: int) -> subprocess.Popen[str]:
    command = [
        "libreoffice",
        "--headless",
        "--norestore",
        "--nodefault",
        "--nofirststartwizard",
        f"--accept=socket,host=127.0.0.1,port={port};urp;StarOffice.ComponentContext",
    ]
    return subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, text=True)


def connect(port: int):
    local_ctx = uno.getComponentContext()
    resolver = local_ctx.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", local_ctx)
    url = f"uno:socket,host=127.0.0.1,port={port};urp;StarOffice.ComponentContext"
    for _ in range(40):
        try:
            ctx = resolver.resolve(url)
            return ctx.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)
        except Exception:
            time.sleep(0.25)
    raise RuntimeError("Could not connect to LibreOffice UNO listener.")


def header_columns(sheet) -> dict[str, int]:
    found: dict[str, int] = {}
    for col in range(0, 80):
        header = str(sheet.getCellByPosition(col, 0).String).strip()
        if header in TARGET_HEADERS:
            found[TARGET_HEADERS[header]] = col
    missing = sorted(set(TARGET_HEADERS.values()) - set(found))
    if missing:
        raise RuntimeError(f"Missing expected workbook headers: {', '.join(missing)}")
    return found


def workbook_names(sheet) -> dict[str, int]:
    names: dict[str, int] = {}
    blank_run = 0
    row = 1
    while row < 500:
        name = str(sheet.getCellByPosition(0, row).String).strip()
        if not name:
            blank_run += 1
            if blank_run > 10:
                break
            row += 1
            continue
        blank_run = 0
        if name not in IGNORE_NAMES:
            names[name] = row
        row += 1
    return names


def score_maps(hw5_rows: list[dict[str, str]], hw6_rows: list[dict[str, str]]) -> tuple[dict[str, dict[str, str]], dict[str, dict[str, str]], set[str]]:
    duplicates: set[str] = set()
    hw5_by_name: dict[str, dict[str, str]] = {}
    hw6_by_name: dict[str, dict[str, str]] = {}
    for source, target in ((hw5_rows, hw5_by_name), (hw6_rows, hw6_by_name)):
        seen: set[str] = set()
        for row in source:
            name = row.get("student_name", "").strip()
            if not name:
                continue
            if name in seen:
                duplicates.add(name)
            seen.add(name)
            target[name] = row
    return hw5_by_name, hw6_by_name, duplicates


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=UNMATCHED_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_report(path: Path, lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    args = parse_args()
    if args.dry_run == args.apply:
        print("Choose exactly one of --dry-run or --apply.")
        return 2
    if not args.input.exists():
        print(f"Input workbook does not exist: {args.input}")
        return 1
    if args.output.resolve() == args.input.resolve():
        print("Refusing to overwrite the original workbook.")
        return 1

    hw5_rows = read_rows(args.hw5_scores)
    hw6_rows = read_rows(args.hw6_summary)
    hw5_by_name, hw6_by_name, duplicate_names = score_maps(hw5_rows, hw6_rows)
    input_hash_before = sha256(args.input)

    office = start_office(args.port)
    document = None
    try:
        desktop = connect(args.port)
        document = desktop.loadComponentFromURL(
            file_url(args.input),
            "_blank",
            0,
            (prop("Hidden", True), prop("ReadOnly", False)),
        )
        sheet = document.Sheets.getByName("HW成績")
        columns = header_columns(sheet)
        names = workbook_names(sheet)
        unmatched: list[dict[str, object]] = []

        counters = {
            "hw5_updated": 0,
            "hw6_updated": 0,
            "workbook_rows_seen": len(names),
            "duplicate_names": len(duplicate_names),
        }

        for name in duplicate_names:
            workbook_row = names.get(name)
            for homework in ("hw5", "hw6"):
                source = hw5_by_name if homework == "hw5" else hw6_by_name
                row = source.get(name, {})
                unmatched.append({
                    "student_name": name,
                    "student_id": row.get("student_id", ""),
                    "homework": homework,
                    "status": "ambiguous_grading_name",
                    "reason": "Duplicate student name in grading source.",
                    "workbook_sheet": "HW成績",
                    "workbook_row": workbook_row + 1 if workbook_row is not None else "",
                    "action": "left cells unchanged",
                })

        for name, row in hw5_by_name.items():
            if name in duplicate_names:
                continue
            if name not in names:
                unmatched.append({
                    "student_name": name,
                    "student_id": row.get("student_id", ""),
                    "homework": "hw5",
                    "status": "graded_row_unmatched_in_workbook",
                    "reason": "No exact workbook name match.",
                    "workbook_sheet": "HW成績",
                    "workbook_row": "",
                    "action": "left HW5 cell unchanged",
                })
                continue
            row_index = names[name]
            if not args.dry_run:
                sheet.getCellByPosition(columns["hw5"], row_index).Value = numeric(row["total_score"])
            counters["hw5_updated"] += 1

        for name, row in hw6_by_name.items():
            if name in duplicate_names:
                continue
            if name not in names:
                unmatched.append({
                    "student_name": name,
                    "student_id": row.get("student_id", ""),
                    "homework": "hw6",
                    "status": "graded_row_unmatched_in_workbook",
                    "reason": "No exact workbook name match.",
                    "workbook_sheet": "HW成績",
                    "workbook_row": "",
                    "action": "left HW6 cells unchanged",
                })
                continue
            row_index = names[name]
            if not args.dry_run:
                sheet.getCellByPosition(columns["hw6_figure"], row_index).Value = numeric(row["hw6_figure_score"])
                sheet.getCellByPosition(columns["hw6_code"], row_index).Value = numeric(row["hw6_code_score"])
            counters["hw6_updated"] += 1

        for name, row_index in names.items():
            if name not in hw5_by_name:
                unmatched.append({
                    "student_name": name,
                    "student_id": "",
                    "homework": "hw5",
                    "status": "not_graded_due_to_missing_evidence",
                    "reason": "Workbook row has no reliable HW5 grading row.",
                    "workbook_sheet": "HW成績",
                    "workbook_row": row_index + 1,
                    "action": "left HW5 cell unchanged",
                })
            if name not in hw6_by_name:
                unmatched.append({
                    "student_name": name,
                    "student_id": "",
                    "homework": "hw6",
                    "status": "not_graded_due_to_missing_evidence",
                    "reason": "Workbook row has no reliable HW6 grading row.",
                    "workbook_sheet": "HW成績",
                    "workbook_row": row_index + 1,
                    "action": "left HW6 cells unchanged",
                })

        now = datetime.now(timezone(timedelta(hours=8))).isoformat(timespec="seconds")
        output_display = args.output if args.apply else "dry-run only"
        report_lines = [
            "# HW5/HW6 Workbook Write-Back Report",
            "",
            f"Generated: `{now}`",
            "",
            "## Summary",
            "",
            f"- Workbook read: `{args.input}`",
            f"- Workbook written: `{output_display}`",
            f"- Original workbook SHA-256 before write: `{input_hash_before}`",
            f"- Workbook rows scanned: {counters['workbook_rows_seen']}",
            f"- HW5 rows updated: {counters['hw5_updated']}",
            f"- HW6 rows updated: {counters['hw6_updated']}",
            f"- Duplicate grading names skipped: {counters['duplicate_names']}",
            f"- Unmatched / not-graded records: {len(unmatched)}",
            "",
            "## Write-Back Columns",
            "",
            f"- Sheet: `HW成績`",
            f"- `HW5`: column `{columns['hw5'] + 1}`",
            f"- `HW6(圖)`: column `{columns['hw6_figure'] + 1}`",
            f"- `HW6(code)`: column `{columns['hw6_code'] + 1}`",
            "",
            "## Source Score Files",
            "",
            f"- HW5: `{args.hw5_scores}`",
            f"- HW6: `{args.hw6_summary}`",
            "",
            "## Unmatched / Not-Graded Rows",
            "",
        ]
        if unmatched:
            for row in unmatched:
                report_lines.append(f"- {row['student_name']} `{row['homework']}`: {row['status']} ({row['reason']})")
        else:
            report_lines.append("- none")

        print("\n".join(report_lines))

        if args.apply:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            document.storeAsURL(file_url(args.output), (prop("FilterName", "Calc MS Excel 2007 XML"),))
            input_hash_after = sha256(args.input)
            if input_hash_after != input_hash_before:
                raise RuntimeError("Original workbook hash changed; refusing to continue.")
            report_lines.insert(12, f"- Original workbook SHA-256 after write: `{input_hash_after}`")
            write_csv(args.unmatched, unmatched)
            write_report(args.report, report_lines)
    finally:
        if document is not None:
            document.close(True)
        office.terminate()
        try:
            office.wait(timeout=5)
        except subprocess.TimeoutExpired:
            office.kill()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
