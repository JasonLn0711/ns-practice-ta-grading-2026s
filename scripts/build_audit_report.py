#!/usr/bin/env python3
"""Build audit and instructor reports from grading CSVs.

Default mode is dry-run. Use --apply to overwrite report Markdown files.
"""

from __future__ import annotations

import argparse
import csv
from collections import Counter
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build grading audit reports.")
    parser.add_argument("--homework", choices=["hw5", "hw6"], required=True)
    parser.add_argument("--apply", action="store_true", help="Write report files.")
    return parser.parse_args()


def read_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def number(value: str) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def yes(value: str) -> bool:
    return value.strip().lower() in {"yes", "y", "true", "1"}


def split_tags(text: str) -> list[str]:
    return [tag.strip() for tag in text.replace(";", ",").split(",") if tag.strip()]


def score_columns(rows: list[dict[str, str]]) -> list[str]:
    if not rows:
        return []
    return [key for key in rows[0] if key.endswith("_score") and key not in {"total_score", "penalty_score"}]


def average(rows: list[dict[str, str]], column: str) -> str:
    if not rows:
        return "TODO"
    return f"{sum(number(row.get(column, '')) for row in rows) / len(rows):.2f}"


def report_text(homework: str, scores: list[dict[str, str]], deductions: list[dict[str, str]], instructor: bool) -> str:
    title = "Instructor Report" if instructor else "Audit Report"
    totals = [number(row.get("total_score", "")) for row in scores]
    manual = [row for row in scores if yes(row.get("manual_review_needed", ""))]
    tags = Counter(row.get("deduction_tag", "") for row in deductions if row.get("deduction_tag"))
    if not tags:
        tags = Counter(tag for row in scores for tag in split_tags(row.get("deduction_summary", "")))

    lines = [
        f"# {homework.upper()} {title}",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        "",
        "## Overview",
        "",
        f"- Number of submissions graded: {len(scores)}",
        f"- Average score: {sum(totals) / len(totals):.2f}" if totals else "- Average score: TODO",
        f"- Manual reviews: {len(manual)}",
        "",
        "## Distribution By Category",
        "",
        "| Category | Average |",
        "| --- | ---: |",
    ]
    for column in score_columns(scores):
        lines.append(f"| {column} | {average(scores, column)} |")
    if not score_columns(scores):
        lines.append("| TODO | TODO |")

    lines += ["", "## Common Deduction Reasons", ""]
    if tags:
        for tag, count in sorted(tags.items()):
            lines.append(f"- {tag}: {count}")
    else:
        lines.append("- none recorded")

    lines += ["", "## Manual Reviews", ""]
    if manual:
        for row in manual:
            lines.append(f"- {row.get('student_id', 'unknown')}: {row.get('deduction_summary', '').strip()}")
    else:
        lines.append("- none recorded")

    lines += ["", "## Policy Issues Needing Instructor Decision", "", "- TODO"]
    if not instructor:
        lines += ["", "## Audit Sources", "", f"- `grading/{homework}/scores.csv`", f"- `grading/{homework}/deduction_log.csv`", f"- `grading/{homework}/evidence.csv`"]
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    scores = read_rows(ROOT / "grading" / args.homework / "scores.csv")
    deductions = read_rows(ROOT / "grading" / args.homework / "deduction_log.csv")
    audit = report_text(args.homework, scores, deductions, instructor=False)
    instructor = report_text(args.homework, scores, deductions, instructor=True)

    audit_path = ROOT / "reports" / f"{args.homework}_audit_report.md"
    instructor_path = ROOT / "reports" / f"{args.homework}_instructor_report.md"

    print(audit)
    if args.apply:
        audit_path.write_text(audit, encoding="utf-8")
        instructor_path.write_text(instructor, encoding="utf-8")
        print(f"Wrote: {audit_path}")
        print(f"Wrote: {instructor_path}")
    else:
        print("Dry-run only. Re-run with --apply to write report files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
