#!/usr/bin/env python3
"""Build HW6 dual-score audit reports."""

from __future__ import annotations

import csv
from collections import Counter
from datetime import datetime, timezone, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HW6 = ROOT / "grading" / "hw6"
REPORTS = ROOT / "reports"
NOW = datetime.now(timezone(timedelta(hours=8))).isoformat(timespec="seconds")


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def number(value: str) -> float:
    try:
        return float(value)
    except ValueError:
        return 0.0


def average(rows: list[dict[str, str]], field: str) -> float:
    return sum(number(row[field]) for row in rows) / len(rows) if rows else 0.0


def yes(value: str) -> bool:
    return value.strip().lower() in {"yes", "y", "true", "1"}


def tags(rows: list[dict[str, str]], field: str) -> Counter[str]:
    counts: Counter[str] = Counter()
    for row in rows:
        for tag in row.get(field, "").replace(";", ",").split(","):
            tag = tag.strip()
            if tag:
                counts[tag] += 1
    return counts


def distribution(rows: list[dict[str, str]], fields: list[str]) -> str:
    lines = ["| Category | Average |", "| --- | ---: |"]
    for field in fields:
        lines.append(f"| `{field}` | {average(rows, field):.2f} |")
    return "\n".join(lines)


def tag_table(counts: Counter[str]) -> str:
    if not counts:
        return "- none"
    return "\n".join(f"- `{tag}`: {count}" for tag, count in sorted(counts.items()))


def evidence_table(rows: list[dict[str, str]]) -> str:
    counts = Counter(row["evidence_level"] for row in rows)
    lines = ["| Evidence level | Count |", "| --- | ---: |"]
    for level in ["A", "B", "C", "D"]:
        lines.append(f"| `{level}` | {counts.get(level, 0)} |")
    return "\n".join(lines)


def write(path: Path, text: str) -> None:
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def main() -> int:
    code_rows = read_csv(HW6 / "code_scores.csv")
    figure_rows = read_csv(HW6 / "figure_scores.csv")
    combined_rows = read_csv(HW6 / "combined_summary.csv")
    code_deductions = read_csv(HW6 / "code_deduction_log.csv")
    figure_deductions = read_csv(HW6 / "figure_deduction_log.csv")
    unmatched = read_csv(HW6 / "unmatched_students.csv") if (HW6 / "unmatched_students.csv").exists() else []
    manual = read_csv(HW6 / "manual_review_students.csv") if (HW6 / "manual_review_students.csv").exists() else []

    code_fields = [
        "architecture_score",
        "graph_code_alignment_score",
        "training_method_score",
        "result_score",
        "evidence_score",
    ]
    figure_fields = [
        "graph_score",
        "filters_score",
        "feature_maps_score",
        "figure_evidence_score",
    ]

    code_report = f"""# HW6(code) Audit Report

Generated: `{NOW}`

## Summary

- Total submissions represented in score file: {len(code_rows)}
- Submissions graded: {len(code_rows)}
- Complete Level A evidence rows: {sum(1 for row in code_rows if row['evidence_level'] == 'A')}
- Manual review rows: {sum(1 for row in code_rows if yes(row['manual_review_needed']))}
- Average HW6(code) score: {average(code_rows, 'hw6_code_score'):.2f}

## Evidence Levels

{evidence_table(code_rows)}

## Category Distribution

{distribution(code_rows, code_fields)}

## Common Code Deductions

{tag_table(tags(code_rows, 'code_deduction_tags'))}

## Suspicious Patterns

{("- none recorded" if not manual else "- see `grading/hw6/manual_review_students.csv`")}

## Unresolved Policy Issues

- Late submission handling remains TODO until instructor confirmation.
- Dense non-CNN submissions are not awarded full CNN architecture/filter/feature-map credit unless instructor policy changes.
- Text-only or source-comment computational graphs remain partial-credit figure evidence unless accepted by the instructor.

## Policy Notes

- Code score is independent from figure score.
- Missing graph evidence can reduce graph-consistent implementation even when code runs.
- Momentum requires historical accumulation, not just a claim or variable name.
- Accuracy at or above `98%` does not override missing architecture, momentum, or graph-to-code evidence.
"""

    figure_report = f"""# HW6(figure) Audit Report

Generated: `{NOW}`

## Summary

- Total submissions represented in score file: {len(figure_rows)}
- Submissions graded: {len(figure_rows)}
- Complete Level A evidence rows: {sum(1 for row in figure_rows if row['evidence_level'] == 'A')}
- Manual review rows: {sum(1 for row in figure_rows if yes(row['manual_review_needed']))}
- Average HW6(figure) score: {average(figure_rows, 'hw6_figure_score'):.2f}

## Evidence Levels

{evidence_table(figure_rows)}

## Category Distribution

{distribution(figure_rows, figure_fields)}

## Common Figure Deductions

{tag_table(tags(figure_rows, 'figure_deduction_tags'))}

## Suspicious Patterns

{("- none recorded" if not manual else "- see `grading/hw6/manual_review_students.csv`")}

## Unresolved Policy Issues

- Late submission handling remains TODO until instructor confirmation.
- Dense non-CNN submissions are not awarded full learned-filter/feature-map credit unless instructor policy changes.
- Text-only or source-comment computational graphs remain partial-credit figure evidence unless accepted by the instructor.

## Policy Notes

- Figure score is independent from code score.
- A missing graph can make the figure score low even if code and accuracy are strong.
- Filters and feature maps must be tied to the submitted model to receive full credit.
- Visual polish does not replace true learned filters, intermediate feature maps, notation, or code alignment.
"""

    master_report = f"""# HW6 Master Dual-Score Audit Report

Generated: `{NOW}`

## Summary

- Total submissions represented in dual-score files: {len(combined_rows)}
- Graded successfully: {sum(1 for row in combined_rows if not yes(row['manual_review_needed']))}
- Graded with manual review flag: {sum(1 for row in combined_rows if yes(row['manual_review_needed']))}
- Not graded due to missing evidence: {sum(1 for row in unmatched if row.get('status') == 'not_graded_due_to_missing_evidence')}
- Unmatched in workbook: {sum(1 for row in unmatched if row.get('status') == 'graded_row_unmatched_in_workbook')}
- Average HW6(code): {average(combined_rows, 'hw6_code_score'):.2f}
- Average HW6(figure): {average(combined_rows, 'hw6_figure_score'):.2f}

## Evidence Levels - Code

{evidence_table(code_rows)}

## Evidence Levels - Figure

{evidence_table(figure_rows)}

## Code Score Distribution

{distribution(code_rows, code_fields)}

## Figure Score Distribution

{distribution(figure_rows, figure_fields)}

## Most Common Code Deduction Reasons

{tag_table(tags(code_rows, 'code_deduction_tags'))}

## Most Common Figure Deduction Reasons

{tag_table(tags(figure_rows, 'figure_deduction_tags'))}

## Unresolved Policy Issues

- Late submission handling remains TODO until instructor confirmation.
- Text-only graph and source-comment graph formats remain policy-sensitive.
- Dense non-CNN submissions are not awarded full CNN filter/feature-map credit unless the instructor changes policy.

## Rubric Interpretation Notes For Future Consistency

- `HW6(code)` and `HW6(圖)` are independent 100-point scores.
- No score should be awarded without inspectable evidence.
- Every non-full category must have a deduction tag and written reason.
- Accuracy can earn result-band points only when it is credible and traceable to the submitted HW6 model.
- Figure credit requires graph/filter/feature-map evidence, not just attractive screenshots.

## Audit Sources

- `grading/hw6/code_scores.csv`
- `grading/hw6/figure_scores.csv`
- `grading/hw6/combined_summary.csv`
- `grading/hw6/code_deduction_log.csv`
- `grading/hw6/figure_deduction_log.csv`
- `grading/hw6/feedback/`
"""

    REPORTS.mkdir(parents=True, exist_ok=True)
    write(REPORTS / "hw6_code_audit_report.md", code_report)
    write(REPORTS / "hw6_figure_audit_report.md", figure_report)
    write(REPORTS / "hw6_master_audit_report.md", master_report)
    print("Wrote HW6 dual-score audit reports.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
