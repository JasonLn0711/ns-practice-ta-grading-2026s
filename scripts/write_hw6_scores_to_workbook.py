#!/usr/bin/env python3
"""Write HW6 dual scores into a copied course workbook.

Uses LibreOffice UNO so existing formatting, widths, formulas, and styles are
preserved as much as possible. The original workbook is never overwritten.
"""

from __future__ import annotations

import argparse
import csv
import subprocess
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path

import uno
from com.sun.star.beans import PropertyValue


ROOT = Path(__file__).resolve().parents[1]
HW6 = ROOT / "grading" / "hw6"
REPORTS = ROOT / "reports"
DEFAULT_INPUT = ROOT / "course_materials" / "hw6" / "raw" / "(114下)深度學習成績和分組.xlsx"
DEFAULT_OUTPUT = ROOT / "course_materials" / "hw6" / "renamed" / "(114下)深度學習成績和分組_hw6_scored.xlsx"
IGNORE_NAMES = {"程式碼乾淨/註解/用心程度", "基本分", "程式不動(有努力)", "交白卷/缺交"}
UNMATCHED_FIELDS = [
    "student_name",
    "student_id",
    "submission_path",
    "status",
    "reason",
    "workbook_sheet",
    "workbook_row",
    "action",
]
MANUAL_FIELDS = [
    "student_name",
    "student_id",
    "submission_path",
    "hw6_code_score",
    "hw6_figure_score",
    "manual_review_reason",
    "source",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Write HW6(code)/HW6(figure) scores to workbook copy.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--combined", type=Path, default=HW6 / "combined_summary.csv")
    parser.add_argument("--dry-run", action="store_true", help="Inspect and report without saving workbook.")
    parser.add_argument("--apply", action="store_true", help="Save workbook copy and write reports.")
    parser.add_argument("--port", type=int, default=2002)
    return parser.parse_args()


def prop(name: str, value: object) -> PropertyValue:
    item = PropertyValue()
    item.Name = name
    item.Value = value
    return item


def file_url(path: Path) -> str:
    return path.resolve().as_uri()


def read_combined(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def yes(value: str) -> bool:
    return value.strip().lower() in {"yes", "y", "true", "1"}


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


def used_names(sheet) -> dict[str, int]:
    names: dict[str, int] = {}
    row = 1  # zero-based row 1 is spreadsheet row 2.
    blank_run = 0
    while row < 500:
        value = str(sheet.getCellByPosition(0, row).String).strip()
        if not value:
            blank_run += 1
            if blank_run > 10:
                break
            row += 1
            continue
        blank_run = 0
        if value not in IGNORE_NAMES:
            names[value] = row
        row += 1
    return names


def write_csv(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_report(path: Path, lines: list[str]) -> None:
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

    combined = read_combined(args.combined)
    by_name: dict[str, dict[str, str]] = {}
    duplicate_names: set[str] = set()
    for row in combined:
        name = row["student_name"].strip()
        if name in by_name:
            duplicate_names.add(name)
        by_name[name] = row

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
        if sheet.getCellByPosition(12, 0).String != "HW6(圖)" or sheet.getCellByPosition(13, 0).String != "HW6(code)":
            raise RuntimeError("Expected HW6(圖) in M1 and HW6(code) in N1.")

        workbook_names = used_names(sheet)
        unmatched: list[dict[str, object]] = []
        manual: list[dict[str, object]] = []
        updated = 0

        for name in duplicate_names:
            row = by_name[name]
            unmatched.append({
                "student_name": name,
                "student_id": row.get("student_id", ""),
                "submission_path": row.get("submission_path", ""),
                "status": "ambiguous_grading_name",
                "reason": "Duplicate name in combined_summary.csv.",
                "workbook_sheet": "HW成績",
                "workbook_row": "",
                "action": "left workbook unchanged",
            })

        for name, row in by_name.items():
            if name in duplicate_names:
                continue
            if name not in workbook_names:
                unmatched.append({
                    "student_name": name,
                    "student_id": row.get("student_id", ""),
                    "submission_path": row.get("submission_path", ""),
                    "status": "graded_row_unmatched_in_workbook",
                    "reason": "No exact workbook name match.",
                    "workbook_sheet": "HW成績",
                    "workbook_row": "",
                    "action": "left workbook unchanged",
                })
                continue
            row_index = workbook_names[name]
            if not args.dry_run:
                sheet.getCellByPosition(12, row_index).Value = float(row["hw6_figure_score"])
                sheet.getCellByPosition(13, row_index).Value = float(row["hw6_code_score"])
            updated += 1
            if yes(row.get("manual_review_needed", "")):
                manual.append({
                    "student_name": name,
                    "student_id": row.get("student_id", ""),
                    "submission_path": row.get("submission_path", ""),
                    "hw6_code_score": row.get("hw6_code_score", ""),
                    "hw6_figure_score": row.get("hw6_figure_score", ""),
                    "manual_review_reason": "manual_review_needed=yes in combined_summary.csv",
                    "source": "grading/hw6/combined_summary.csv",
                })

        for name, row_index in workbook_names.items():
            if name not in by_name and name not in IGNORE_NAMES:
                unmatched.append({
                    "student_name": name,
                    "student_id": "",
                    "submission_path": "",
                    "status": "not_graded_due_to_missing_evidence",
                    "reason": "Workbook row has no reliable HW6 grading evidence row.",
                    "workbook_sheet": "HW成績",
                    "workbook_row": row_index + 1,
                    "action": "left HW6 cells unchanged",
                })

        now = datetime.now(timezone(timedelta(hours=8))).isoformat(timespec="seconds")
        report_lines = [
            "# HW6 Workbook Write-Back Report",
            "",
            f"Generated: `{now}`",
            "",
            "## Summary",
            "",
            f"- Workbook read: `{args.input}`",
            f"- Workbook written: `{args.output if args.apply else 'dry-run only'}`",
            f"- Rows updated: {updated}",
            f"- Graded successfully: {updated - len(manual)}",
            f"- Graded with manual review flag: {len(manual)}",
            f"- Not graded due to missing evidence: {sum(1 for row in unmatched if row['status'] == 'not_graded_due_to_missing_evidence')}",
            f"- Unmatched in workbook: {sum(1 for row in unmatched if row['status'] == 'graded_row_unmatched_in_workbook')}",
            "",
            "## Write-Back Columns",
            "",
            "- Sheet: `HW成績`",
            "- `HW6(圖)`: column `M`",
            "- `HW6(code)`: column `N`",
            "",
            "## Unmatched / Not-Graded Rows",
            "",
        ]
        if unmatched:
            report_lines += [f"- {row['student_name']}: {row['status']} ({row['reason']})" for row in unmatched]
        else:
            report_lines.append("- none")
        report_lines += ["", "## Manual Review Rows", ""]
        if manual:
            report_lines += [f"- {row['student_name']} `{row['student_id']}`: {row['manual_review_reason']}" for row in manual]
        else:
            report_lines.append("- none")

        print("\n".join(report_lines))

        if args.apply:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            document.storeAsURL(file_url(args.output), (prop("FilterName", "Calc MS Excel 2007 XML"),))
            write_csv(HW6 / "unmatched_students.csv", UNMATCHED_FIELDS, unmatched)
            write_csv(HW6 / "manual_review_students.csv", MANUAL_FIELDS, manual)
            write_report(REPORTS / "hw6_workbook_writeback_report.md", report_lines)
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
