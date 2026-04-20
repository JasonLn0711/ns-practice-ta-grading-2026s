#!/usr/bin/env python3
"""Summarize score CSVs for HW5/HW6."""

from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Summarize grading scores.")
    parser.add_argument("--homework", choices=["hw5", "hw6"], required=True)
    parser.add_argument("--scores", type=Path)
    return parser.parse_args()


def number(value: str) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def yes(value: str) -> bool:
    return value.strip().lower() in {"yes", "y", "true", "1"}


def split_tags(text: str) -> list[str]:
    return [tag.strip() for tag in text.replace(";", ",").split(",") if tag.strip()]


def main() -> int:
    args = parse_args()
    scores_path = args.scores or ROOT / "grading" / args.homework / "scores.csv"

    if not scores_path.exists():
        print(f"Scores file does not exist: {scores_path}")
        return 1

    with scores_path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    print(f"Homework: {args.homework}")
    print(f"Scores file: {scores_path}")
    print(f"Rows: {len(rows)}")

    if not rows:
        print("No graded rows yet.")
        return 0

    totals = [number(row.get("total_score", "")) for row in rows]
    manual = [row for row in rows if yes(row.get("manual_review_needed", ""))]
    evidence = Counter(row.get("evidence_level", "").strip() or "unset" for row in rows)
    deductions = Counter(tag for row in rows for tag in split_tags(row.get("deduction_summary", "")))

    print(f"Average total: {sum(totals) / len(totals):.2f}")
    print(f"Min total: {min(totals):.2f}")
    print(f"Max total: {max(totals):.2f}")
    print(f"Manual review needed: {len(manual)}")

    print("\nEvidence levels:")
    for level, count in sorted(evidence.items()):
        print(f"- {level}: {count}")

    print("\nDeduction tags:")
    if deductions:
        for tag, count in sorted(deductions.items()):
            print(f"- {tag}: {count}")
    else:
        print("- none recorded")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
