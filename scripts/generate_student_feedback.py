#!/usr/bin/env python3
"""Generate student feedback Markdown files from scores.csv.

Default mode is dry-run. Use --apply to write files under grading/<hw>/feedback.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate student feedback files.")
    parser.add_argument("--homework", choices=["hw5", "hw6"], required=True)
    parser.add_argument("--scores", type=Path)
    parser.add_argument("--template", type=Path, default=ROOT / "templates" / "student_feedback.md")
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--apply", action="store_true", help="Write feedback files.")
    return parser.parse_args()


def score_breakdown(row: dict[str, str]) -> str:
    skip = {
        "student_id",
        "student_name",
        "hw_id",
        "submission_path",
        "evidence_level",
        "manual_review_needed",
        "deduction_summary",
        "grader",
        "graded_at",
    }
    lines = []
    for key, value in row.items():
        if key.endswith("_score") and key not in skip:
            lines.append(f"- {key}: {value}")
    return "\n".join(lines) or "- No scores recorded."


def render(template: str, row: dict[str, str]) -> str:
    values = {
        "student_id": row.get("student_id", ""),
        "hw_id": row.get("hw_id", ""),
        "total_score": row.get("total_score", ""),
        "evidence_level": row.get("evidence_level", ""),
        "manual_review_needed": row.get("manual_review_needed", ""),
        "score_breakdown": score_breakdown(row),
        "deduction_summary": row.get("deduction_summary", "") or "No deductions recorded.",
        "feedback_body": "See score breakdown and deduction summary.",
        "reproducibility_note": "Evidence level records how reproducible the submitted result was.",
    }
    for key, value in values.items():
        template = template.replace("{" + key + "}", value)
    return template


def main() -> int:
    args = parse_args()
    scores_path = args.scores or ROOT / "grading" / args.homework / "scores.csv"
    output_dir = args.output_dir or ROOT / "grading" / args.homework / "feedback"

    if not scores_path.exists():
        print(f"Scores file does not exist: {scores_path}")
        return 1
    if not args.template.exists():
        print(f"Template does not exist: {args.template}")
        return 1

    template = args.template.read_text(encoding="utf-8")
    with scores_path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    for row in rows:
        student_id = row.get("student_id", "unknown") or "unknown"
        target = output_dir / f"{student_id}_{args.homework}_feedback.md"
        print(f"{'write' if args.apply else 'would write'}: {target}")
        if args.apply:
            output_dir.mkdir(parents=True, exist_ok=True)
            target.write_text(render(template, row), encoding="utf-8")

    if not args.apply:
        print("Dry-run only. Re-run with --apply to write feedback files.")
    print(f"Summary: rows={len(rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
