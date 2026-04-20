#!/usr/bin/env python3
"""Validate grading records before scores are released.

This script enforces process rules. It does not decide grades.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

MAX_POINTS = {
    "hw5": {
        "completeness_score": 10,
        "requirement_score": 30,
        "technical_score": 30,
        "result_score": 15,
        "evidence_score": 15,
    },
    "hw6": {
        "completeness_score": 10,
        "architecture_score": 15,
        "graph_score": 15,
        "training_score": 20,
        "result_score": 10,
        "visualization_score": 15,
        "evidence_score": 15,
    },
}

EVIDENCE_CAPS = {"A": 15, "B": 10, "C": 5}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate auditable grading records.")
    parser.add_argument("--homework", choices=["hw5", "hw6"], required=True)
    return parser.parse_args()


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def num(value: str) -> float | None:
    if value is None or value == "":
        return None
    try:
        return float(value)
    except ValueError:
        return None


def yes(value: str) -> bool:
    return value.strip().lower() in {"yes", "y", "true", "1"}


def split_tags(text: str) -> set[str]:
    return {tag.strip() for tag in text.replace(";", ",").split(",") if tag.strip()}


def has_deduction_log(student_id: str, logs: list[dict[str, str]]) -> bool:
    return any(row.get("student_id") == student_id and row.get("note", "").strip() for row in logs)


def validate_log_rows(logs: list[dict[str, str]], errors: list[str]) -> None:
    required = ["student_id", "deduction_tag", "category", "points_deducted", "evidence_path", "note"]
    for index, row in enumerate(logs, start=2):
        for field in required:
            if not row.get(field, "").strip():
                errors.append(f"deduction_log.csv:{index}: missing {field}")
        points = num(row.get("points_deducted", ""))
        if points is None:
            errors.append(f"deduction_log.csv:{index}: points_deducted is not numeric")
        if row.get("deduction_tag") == "POSSIBLE_COPYING_MANUAL_REVIEW" and not yes(
            row.get("manual_review_needed", "")
        ):
            errors.append(f"deduction_log.csv:{index}: plagiarism/similarity tag must set manual_review_needed=yes")


def validate_score_row(
    homework: str,
    row: dict[str, str],
    line_no: int,
    evidence_ids: set[str],
    logs: list[dict[str, str]],
    errors: list[str],
) -> None:
    student_id = row.get("student_id", "").strip()
    prefix = f"scores.csv:{line_no}:{student_id or 'unknown'}"
    if not student_id:
        errors.append(f"{prefix}: missing student_id")
        return

    for field in ["submission_path", "evidence_level", "grader", "graded_at", "total_score"]:
        if not row.get(field, "").strip():
            errors.append(f"{prefix}: missing {field}")

    note_path = ROOT / "grading" / homework / "student_notes" / f"{student_id}.md"
    if not note_path.exists():
        errors.append(f"{prefix}: missing per-student note {note_path.relative_to(ROOT)}")

    if student_id not in evidence_ids:
        errors.append(f"{prefix}: missing matching row in grading/{homework}/evidence.csv")

    evidence_level = row.get("evidence_level", "").strip().upper()
    evidence_score = num(row.get("evidence_score", ""))
    if evidence_level not in EVIDENCE_CAPS:
        errors.append(f"{prefix}: evidence_level must be A, B, or C")
    elif evidence_score is not None and evidence_score > EVIDENCE_CAPS[evidence_level]:
        errors.append(
            f"{prefix}: evidence_score {evidence_score:g} exceeds Level {evidence_level} cap {EVIDENCE_CAPS[evidence_level]}"
        )

    deduction_tags = split_tags(row.get("deduction_summary", ""))
    log_has_reason = has_deduction_log(student_id, logs)
    needs_reason = False
    for field, max_score in MAX_POINTS[homework].items():
        value = num(row.get(field, ""))
        if value is None:
            errors.append(f"{prefix}: {field} is missing or non-numeric")
            continue
        if value < max_score:
            needs_reason = True

    penalty = num(row.get("penalty_score", ""))
    if penalty is not None and penalty != 0:
        needs_reason = True

    if needs_reason and not deduction_tags and not log_has_reason:
        errors.append(f"{prefix}: non-full score or penalty needs deduction_summary or deduction_log reason")

    all_tags = set(deduction_tags)
    all_tags.update(row.get("deduction_tag", "") for row in logs if row.get("student_id") == student_id)
    if "POSSIBLE_COPYING_MANUAL_REVIEW" in all_tags and not yes(row.get("manual_review_needed", "")):
        errors.append(f"{prefix}: possible-copying tag requires manual_review_needed=yes")


def main() -> int:
    args = parse_args()
    scores_path = ROOT / "grading" / args.homework / "scores.csv"
    evidence_path = ROOT / "grading" / args.homework / "evidence.csv"
    log_path = ROOT / "grading" / args.homework / "deduction_log.csv"

    scores = read_csv(scores_path)
    evidence = read_csv(evidence_path)
    logs = read_csv(log_path)
    evidence_ids = {row.get("student_id", "").strip() for row in evidence if row.get("student_id", "").strip()}

    errors: list[str] = []
    validate_log_rows(logs, errors)
    for line_no, row in enumerate(scores, start=2):
        validate_score_row(args.homework, row, line_no, evidence_ids, logs, errors)

    print(f"Homework: {args.homework}")
    print(f"Score rows: {len(scores)}")
    print(f"Evidence rows: {len(evidence)}")
    print(f"Deduction rows: {len(logs)}")

    if errors:
        print("\nValidation errors:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
