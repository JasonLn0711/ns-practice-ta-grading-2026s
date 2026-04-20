#!/usr/bin/env python3
"""Validate HW6 dual-score grading records."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HW6 = ROOT / "grading" / "hw6"

CODE_FIELDS = [
    "student_name", "student_id", "submission_path", "architecture_score",
    "graph_code_alignment_score", "training_method_score",
    "result_score", "evidence_score",
    "code_penalty", "hw6_code_score", "evidence_level",
    "manual_review_needed", "code_deduction_tags", "grader", "graded_at",
    "notes",
]
FIGURE_FIELDS = [
    "student_name", "student_id", "submission_path", "graph_score",
    "filters_score", "feature_maps_score", "figure_evidence_score",
    "figure_penalty", "hw6_figure_score", "evidence_level",
    "manual_review_needed", "figure_deduction_tags", "grader", "graded_at",
    "notes",
]
COMBINED_FIELDS = [
    "student_name", "student_id", "submission_path", "hw6_code_score",
    "hw6_figure_score", "evidence_level", "manual_review_needed",
    "code_deduction_summary", "figure_deduction_summary", "final_comment",
]

CODE_MAX = {
    "architecture_score": 25,
    "graph_code_alignment_score": 20,
    "training_method_score": 25,
    "result_score": 20,
    "evidence_score": 10,
}
FIGURE_MAX = {
    "graph_score": 40,
    "filters_score": 20,
    "feature_maps_score": 25,
    "figure_evidence_score": 15,
}
CODE_EVIDENCE_CAP = {"A": 10, "B": 7, "C": 4, "D": 2}
FIGURE_EVIDENCE_CAP = {"A": 15, "B": 10, "C": 6, "D": 3}


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise SystemExit(f"Missing required file: {path}")
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def number(row: dict[str, str], field: str) -> int:
    try:
        return int(float(row[field]))
    except (KeyError, ValueError) as exc:
        raise SystemExit(f"Invalid numeric value for {field}: {row}") from exc


def check_fields(path: Path, expected: list[str]) -> None:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.reader(handle)
        header = next(reader, [])
    if header != expected:
        raise SystemExit(f"Bad header in {path}:\nexpected={expected}\nactual={header}")


def tag_set(text: str) -> set[str]:
    return {part.strip() for part in text.replace(";", ",").split(",") if part.strip()}


def yes(value: str) -> bool:
    return value.strip().lower() in {"yes", "y", "true", "1"}


def safe_name(name: str) -> str:
    return name.replace("/", "-").replace("\\", "-").replace(" ", "")


def main() -> int:
    check_fields(HW6 / "code_scores.csv", CODE_FIELDS)
    check_fields(HW6 / "figure_scores.csv", FIGURE_FIELDS)
    check_fields(HW6 / "combined_summary.csv", COMBINED_FIELDS)

    code_rows = read_csv(HW6 / "code_scores.csv")
    figure_rows = read_csv(HW6 / "figure_scores.csv")
    combined_rows = read_csv(HW6 / "combined_summary.csv")
    code_deductions = read_csv(HW6 / "code_deduction_log.csv")
    figure_deductions = read_csv(HW6 / "figure_deduction_log.csv")
    manual_rows = read_csv(HW6 / "manual_review_students.csv")

    errors: list[str] = []
    code_by_id = {row["student_id"]: row for row in code_rows}
    figure_by_id = {row["student_id"]: row for row in figure_rows}

    if len(code_by_id) != len(code_rows):
        errors.append("Duplicate student_id in code_scores.csv")
    if len(figure_by_id) != len(figure_rows):
        errors.append("Duplicate student_id in figure_scores.csv")
    if set(code_by_id) != set(figure_by_id):
        errors.append("Code and figure score files do not contain the same students")

    code_deduction_keys = {(row["student_id"], row["category"]) for row in code_deductions}
    figure_deduction_keys = {(row["student_id"], row["category"]) for row in figure_deductions}
    manual_ids = {row["student_id"] for row in manual_rows}

    for row in code_rows:
        sid = row["student_id"]
        subtotal = sum(number(row, field) for field in CODE_MAX) - number(row, "code_penalty")
        if subtotal != number(row, "hw6_code_score"):
            errors.append(f"{sid}: code total mismatch")
        level = row["evidence_level"]
        if level not in CODE_EVIDENCE_CAP:
            errors.append(f"{sid}: invalid code evidence level {level}")
        elif number(row, "evidence_score") > CODE_EVIDENCE_CAP[level]:
            errors.append(f"{sid}: code evidence score exceeds Level {level} cap")
        for field, max_score in CODE_MAX.items():
            value = number(row, field)
            if not 0 <= value <= max_score:
                errors.append(f"{sid}: {field} out of range")
            if value < max_score and (sid, field) not in code_deduction_keys:
                errors.append(f"{sid}: missing code deduction row for {field}")
        if number(row, "hw6_code_score") < 100 and not tag_set(row["code_deduction_tags"]):
            errors.append(f"{sid}: non-full code score without deduction tags")
        if number(row, "code_penalty") != 0 and (sid, "code_penalty") not in code_deduction_keys:
            errors.append(f"{sid}: code penalty without deduction row")
        if yes(row["manual_review_needed"]) and sid not in manual_ids:
            errors.append(f"{sid}: code manual review flag without manual_review_students row")
        note_path = HW6 / "feedback" / f"{sid}_{safe_name(row['student_name'])}.md"
        if not note_path.exists():
            errors.append(f"{sid}: missing feedback note")
        else:
            note_text = note_path.read_text(encoding="utf-8")
            for needle in ["Final Independent Scores", "HW6(code)", "HW6(figure)", "TA / Instructor Audit Explanation"]:
                if needle not in note_text:
                    errors.append(f"{sid}: feedback note missing {needle}")

    for row in figure_rows:
        sid = row["student_id"]
        subtotal = sum(number(row, field) for field in FIGURE_MAX) - number(row, "figure_penalty")
        if subtotal != number(row, "hw6_figure_score"):
            errors.append(f"{sid}: figure total mismatch")
        level = row["evidence_level"]
        if level not in FIGURE_EVIDENCE_CAP:
            errors.append(f"{sid}: invalid figure evidence level {level}")
        elif number(row, "figure_evidence_score") > FIGURE_EVIDENCE_CAP[level]:
            errors.append(f"{sid}: figure explainability exceeds Level {level} cap")
        for field, max_score in FIGURE_MAX.items():
            value = number(row, field)
            if not 0 <= value <= max_score:
                errors.append(f"{sid}: {field} out of range")
            if value < max_score and (sid, field) not in figure_deduction_keys:
                errors.append(f"{sid}: missing figure deduction row for {field}")
        if number(row, "hw6_figure_score") < 100 and not tag_set(row["figure_deduction_tags"]):
            errors.append(f"{sid}: non-full figure score without deduction tags")
        if number(row, "figure_penalty") != 0 and (sid, "figure_penalty") not in figure_deduction_keys:
            errors.append(f"{sid}: figure penalty without deduction row")
        if yes(row["manual_review_needed"]) and sid not in manual_ids:
            errors.append(f"{sid}: figure manual review flag without manual_review_students row")

    for row in combined_rows:
        sid = row["student_id"]
        if sid not in code_by_id or sid not in figure_by_id:
            errors.append(f"{sid}: combined row without code/figure row")
            continue
        if number(row, "hw6_code_score") != number(code_by_id[sid], "hw6_code_score"):
            errors.append(f"{sid}: combined code score mismatch")
        if number(row, "hw6_figure_score") != number(figure_by_id[sid], "hw6_figure_score"):
            errors.append(f"{sid}: combined figure score mismatch")

    if errors:
        print("HW6 dual grading validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("HW6 dual grading validation passed.")
    print(f"Code rows: {len(code_rows)}")
    print(f"Figure rows: {len(figure_rows)}")
    print(f"Combined rows: {len(combined_rows)}")
    print(f"Code deductions: {len(code_deductions)}")
    print(f"Figure deductions: {len(figure_deductions)}")
    print(f"Manual review rows: {len(manual_rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
