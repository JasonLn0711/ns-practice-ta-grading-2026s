#!/usr/bin/env python3
"""Summarize a homework score CSV."""

from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Summarize grading scores.")
    parser.add_argument("--homework", choices=["hw5", "hw6"], default="hw5")
    parser.add_argument("--scores", type=Path)
    return parser.parse_args()


def to_float(value: str) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def yes(value: str) -> bool:
    return value.strip().lower() in {"yes", "y", "true", "1"}


def main() -> int:
    args = parse_args()
    scores_path = args.scores or ROOT / "grading" / args.homework / "scores.csv"

    if not scores_path.exists():
        print(f"Scores file does not exist: {scores_path}")
        return 1

    with scores_path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    if not rows:
        print(f"No score rows yet: {scores_path}")
        return 0

    totals = [to_float(row.get("total_score", "")) for row in rows]
    manual_rows = [row for row in rows if yes(row.get("manual_review_needed", ""))]
    tags = Counter(row.get("feedback_tag", "").strip() or "untagged" for row in rows)

    print(f"Homework: {args.homework}")
    print(f"Rows: {len(rows)}")
    print(f"Average total: {sum(totals) / len(totals):.2f}")
    print(f"Min total: {min(totals):.2f}")
    print(f"Max total: {max(totals):.2f}")
    print(f"Manual review needed: {len(manual_rows)}")

    print("\nFeedback tags:")
    for tag, count in sorted(tags.items()):
        print(f"- {tag}: {count}")

    if manual_rows:
        print("\nManual review rows:")
        for row in manual_rows:
            student = row.get("student_id") or row.get("student_name") or row.get("submission_name")
            print(f"- {student}: {row.get('notes', '').strip()}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
