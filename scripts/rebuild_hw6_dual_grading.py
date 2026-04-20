#!/usr/bin/env python3
"""Build HW6 dual-score grading records from audited HW6 evidence.

This script is intentionally explicit: the point allocations below are the
human grading decisions made under the dual HW6(code)/HW6(figure) rubrics.
Running it rewrites the dual-score CSVs, deduction logs, and per-student
feedback notes.
"""

from __future__ import annotations

import csv
from datetime import datetime, timezone, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HW6 = ROOT / "grading" / "hw6"
GRADER = "Jason"
NOW = datetime.now(timezone(timedelta(hours=8))).isoformat(timespec="seconds")

CODE_FIELDS = [
    "student_name",
    "student_id",
    "submission_path",
    "architecture_score",
    "graph_code_alignment_score",
    "training_method_score",
    "result_score",
    "evidence_score",
    "code_penalty",
    "hw6_code_score",
    "evidence_level",
    "manual_review_needed",
    "code_deduction_tags",
    "grader",
    "graded_at",
    "notes",
]

FIGURE_FIELDS = [
    "student_name",
    "student_id",
    "submission_path",
    "graph_score",
    "filters_score",
    "feature_maps_score",
    "figure_evidence_score",
    "figure_penalty",
    "hw6_figure_score",
    "evidence_level",
    "manual_review_needed",
    "figure_deduction_tags",
    "grader",
    "graded_at",
    "notes",
]

COMBINED_FIELDS = [
    "student_name",
    "student_id",
    "submission_path",
    "hw6_code_score",
    "hw6_figure_score",
    "evidence_level",
    "manual_review_needed",
    "code_deduction_summary",
    "figure_deduction_summary",
    "final_comment",
]

DEDUCTION_FIELDS = [
    "student_name",
    "student_id",
    "score_type",
    "deduction_tag",
    "category",
    "points_deducted",
    "evidence_path",
    "note",
    "manual_review_needed",
    "grader",
    "recorded_at",
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

START = "<!-- HW6_DUAL_SCORE_START -->"
END = "<!-- HW6_DUAL_SCORE_END -->"

RESULT_SCORE_CORRECTIONS = {
    "113350014": (19, "CODE_RESULT_BAND_BELOW_FULL", "98.30-98.49", "Verified accuracy is in the 98.30-98.49% band, so result earns 19/20."),
    "314261001": (19, "CODE_RESULT_BAND_BELOW_FULL", "98.30-98.49", "Verified accuracy is in the 98.30-98.49% band, so result earns 19/20."),
    "314261002": (15, "CODE_ACCURACY_BELOW_TARGET", "97.60-97.79", "Retained test accuracy is 97.62%, below the 98% target and in the 97.60-97.79% band."),
    "314261024": (18, "CODE_RESULT_BAND_BELOW_FULL", "98.10-98.29", "Verified accuracy is in the 98.10-98.29% band, so result earns 18/20."),
    "314264001": (19, "CODE_RESULT_BAND_BELOW_FULL", "98.30-98.49", "Verified accuracy is in the 98.30-98.49% band, so result earns 19/20."),
    "314264013": (19, "CODE_RESULT_BAND_BELOW_FULL", "98.30-98.49", "Verified accuracy is in the 98.30-98.49% band, so result earns 19/20."),
    "314351005": (18, "CODE_RESULT_BAND_BELOW_FULL", "98.10-98.29", "Verified accuracy is in the 98.10-98.29% band, so result earns 18/20."),
}


def row(
    student_id: str,
    student_name: str,
    submission_path: str,
    code: tuple[int, int, int, int, int],
    figure: tuple[int, int, int, int],
    code_level: str,
    figure_level: str,
    code_tags: str,
    figure_tags: str,
    code_note: str,
    figure_note: str,
    code_deductions: list[tuple[str, str, int, str]],
    figure_deductions: list[tuple[str, str, int, str]],
) -> dict[str, object]:
    return {
        "student_id": student_id,
        "student_name": student_name,
        "submission_path": submission_path,
        "code": code,
        "figure": figure,
        "code_level": code_level,
        "figure_level": figure_level,
        "code_tags": code_tags,
        "figure_tags": figure_tags,
        "code_note": code_note,
        "figure_note": figure_note,
        "code_deductions": code_deductions,
        "figure_deductions": figure_deductions,
    }


ROWS = [
    row("111550109", "黃琮仁", "submissions/hw6/renamed", (25, 20, 25, 20, 10), (40, 20, 25, 15), "A", "A", "", "", "Complete code evidence: architecture, graph-aligned implementation, momentum training, 98%+ result, and retained outputs.", "Complete figure evidence: graph, learned filters, feature maps, and traceable labels.", [], []),
    row("112654017", "蕭景升", "submissions/hw6/renamed", (25, 20, 25, 20, 10), (40, 20, 25, 15), "A", "A", "", "", "Momentum is implemented through beta/m variables even though the literal word momentum is absent; result and code are traceable.", "PDF graph, filters, and feature maps are complete and auditable.", [], []),
    row("113304030", "鄭丞言", "submissions/hw6/renamed/hw6_113304030_01_hw6.ipynb", (25, 0, 25, 20, 7), (0, 0, 22, 4), "B", "C", "CODE_GRAPH_NOTATION_MISMATCH", "FIG_GRAPH_MISSING;FIG_FILTERS_MISSING;FIG_FEATURE_MAPS_UNCLEAR;FIG_LABELING_INSUFFICIENT", "Strong code/result evidence, but no computational graph artifact exists, so graph-consistent implementation receives zero and Level B code evidence applies.", "Feature maps are present, but the computational graph and learned-filter plot are missing; figure evidence is weak.", [("CODE_GRAPH_NOTATION_MISMATCH", "graph_code_alignment_score", 20, "No computational graph artifact was found, so code/graph notation alignment cannot be verified."), ("CODE_GRAPH_NOTATION_MISMATCH", "evidence_score", 3, "Missing graph prevents full code/graph/result traceability.")], [("FIG_GRAPH_MISSING", "graph_score", 40, "No computational graph artifact was found."), ("FIG_FILTERS_MISSING", "filters_score", 20, "No learned-filter plot tied to trained filters was found."), ("FIG_FEATURE_MAPS_UNCLEAR", "feature_maps_score", 3, "Feature maps are present but not enough to compensate for missing graph/filter figure evidence."), ("FIG_LABELING_INSUFFICIENT", "figure_evidence_score", 11, "Only partial feature-map figure evidence is auditable.")]),
    row("113350014", "凃宏諭", "submissions/hw6/renamed", (25, 20, 25, 20, 10), (40, 20, 25, 15), "A", "A", "", "", "Complete code evidence with graph-matching notation and momentum updates.", "Complete graph/PDF and visualization evidence.", [], []),
    row("214952033", "陳奕樺", "submissions/hw6/renamed/hw6_214952033_01_hw6.ipynb", (10, 0, 12, 20, 7), (0, 20, 25, 8), "B", "B", "CODE_ARCH_REPLACEMENT_INCOMPLETE;CODE_GRAPH_NOTATION_MISMATCH;CODE_MOMENTUM_MISSING", "FIG_GRAPH_MISSING;FIG_LABELING_INSUFFICIENT", "Code has result, filters, and maps, but architecture lacks the required added hidden layers, graph is missing, and Adam is used instead of explicit momentum.", "Filters and feature maps are present, but the computational graph is missing.", [("CODE_ARCH_REPLACEMENT_INCOMPLETE", "architecture_score", 15, "Submitted model has one hidden fully connected layer plus output rather than two added hidden layers."), ("CODE_GRAPH_NOTATION_MISMATCH", "graph_code_alignment_score", 20, "No computational graph artifact was found."), ("CODE_MOMENTUM_MISSING", "training_method_score", 13, "Training uses Adam rather than mini-batch stochastic gradient with historical momentum accumulation."), ("CODE_GRAPH_NOTATION_MISMATCH", "evidence_score", 3, "Missing graph and missing required momentum evidence cap code auditability.")], [("FIG_GRAPH_MISSING", "graph_score", 40, "No computational graph artifact was found."), ("FIG_LABELING_INSUFFICIENT", "figure_evidence_score", 7, "Figures are partially auditable but graph traceability is absent.")]),
    row("314261001", "沈恩佑", "submissions/hw6/renamed", (25, 20, 25, 20, 10), (40, 20, 25, 15), "A", "A", "", "", "Complete W-style architecture, graph alignment, momentum updates, and target-reaching result.", "Complete PDF graph, learned filters, and y1/y2/y3 feature-map evidence.", [], []),
    row("314261002", "洪至寬", "submissions/hw6/renamed/hw6_314261002_01_hw6.ipynb", (25, 0, 25, 18, 7), (0, 20, 25, 8), "B", "B", "CODE_GRAPH_NOTATION_MISMATCH;CODE_ACCURACY_BELOW_TARGET", "FIG_GRAPH_MISSING;FIG_LABELING_INSUFFICIENT", "Architecture and momentum are strong, but no graph artifact exists and retained test accuracy is 97.62%.", "Filters and feature maps are present, but computational graph evidence is missing.", [("CODE_GRAPH_NOTATION_MISMATCH", "graph_code_alignment_score", 20, "No computational graph artifact was found."), ("CODE_ACCURACY_BELOW_TARGET", "result_score", 2, "Retained test accuracy is 97.62%, below the 98% target."), ("CODE_GRAPH_NOTATION_MISMATCH", "evidence_score", 3, "Missing graph prevents full code/graph/result traceability.")], [("FIG_GRAPH_MISSING", "graph_score", 40, "No computational graph artifact was found."), ("FIG_LABELING_INSUFFICIENT", "figure_evidence_score", 7, "Visualization evidence is present, but graph traceability is absent.")]),
    row("314261024", "李昀昇", "submissions/hw6/renamed", (25, 20, 25, 20, 10), (40, 20, 25, 15), "A", "A", "", "", "Complete notebook markdown graph, matching code, momentum updates, and 98%+ result.", "Complete graph, learned filters, and feature maps.", [], []),
    row("314264001", "陳耘加", "submissions/hw6/renamed/hw6_314264001_01_hw6-314264001.ipynb", (25, 0, 25, 20, 7), (0, 20, 25, 8), "B", "B", "CODE_GRAPH_NOTATION_MISMATCH", "FIG_GRAPH_MISSING;FIG_LABELING_INSUFFICIENT", "Code is strong and target-reaching, but graph-consistent implementation cannot be verified because graph evidence is missing.", "Filters and feature maps are present, but no graph artifact exists.", [("CODE_GRAPH_NOTATION_MISMATCH", "graph_code_alignment_score", 20, "No computational graph artifact was found."), ("CODE_GRAPH_NOTATION_MISMATCH", "evidence_score", 3, "Missing graph caps code auditability.")], [("FIG_GRAPH_MISSING", "graph_score", 40, "No computational graph artifact was found."), ("FIG_LABELING_INSUFFICIENT", "figure_evidence_score", 7, "Visualization evidence is present, but graph traceability is absent.")]),
    row("314264009", "張庭榮", "submissions/hw6/renamed", (25, 20, 25, 20, 10), (40, 20, 25, 15), "A", "A", "", "", "Complete PyTorch CNN, Graphviz graph, SGD momentum, 99.09% result, filters, and maps.", "Complete generated graph and visualization evidence.", [], []),
    row("314264011", "許浩哲", "submissions/hw6/renamed", (22, 20, 25, 20, 10), (40, 20, 25, 15), "A", "A", "CODE_ARCH_REPLACEMENT_INCOMPLETE", "", "Code and graph show two hidden fully connected layers total; current rubric expects two additional hidden layers.", "Figure deliverables are complete and consistent with the submitted code.", [("CODE_ARCH_REPLACEMENT_INCOMPLETE", "architecture_score", 3, "Architecture shows two hidden fully connected layers total instead of two additional hidden layers under current rubric interpretation.")], []),
    row("314264012", "游晟彬", "submissions/hw6/renamed", (25, 20, 25, 20, 10), (40, 20, 25, 15), "A", "A", "", "", "Complete generated graph, PyTorch CNN, SGD momentum, result, filters, and maps.", "Complete generated graph and visualization evidence.", [], []),
    row("314264013", "張達瑋", "submissions/hw6/renamed", (25, 20, 25, 20, 10), (40, 20, 25, 15), "A", "A", "", "", "Complete PDF graph, matching code, momentum updates, and target-reaching accuracy.", "Complete PDF graph, learned filters, and feature maps.", [], []),
    row("314264019", "游乙倢", "submissions/hw6/renamed/hw6_314264019_01_hw6.ipynb", (25, 0, 25, 20, 7), (0, 20, 25, 8), "B", "B", "CODE_GRAPH_NOTATION_MISMATCH", "FIG_GRAPH_MISSING;FIG_LABELING_INSUFFICIENT", "Code is strong and target-reaching, but graph-consistent implementation cannot be verified because graph evidence is missing.", "Filters and feature maps are present, but no graph artifact exists.", [("CODE_GRAPH_NOTATION_MISMATCH", "graph_code_alignment_score", 20, "No computational graph artifact was found."), ("CODE_GRAPH_NOTATION_MISMATCH", "evidence_score", 3, "Missing graph caps code auditability.")], [("FIG_GRAPH_MISSING", "graph_score", 40, "No computational graph artifact was found."), ("FIG_LABELING_INSUFFICIENT", "figure_evidence_score", 7, "Visualization evidence is present, but graph traceability is absent.")]),
    row("314264023", "蔡宜勳", "submissions/hw6/renamed/hw6_314264023_01_hw06.ipynb", (25, 0, 25, 20, 7), (0, 20, 25, 8), "B", "B", "CODE_GRAPH_NOTATION_MISMATCH", "FIG_GRAPH_MISSING;FIG_LABELING_INSUFFICIENT", "Code is strong and target-reaching, but graph-consistent implementation cannot be verified because graph evidence is missing.", "Filters and feature maps are present, but no graph artifact exists.", [("CODE_GRAPH_NOTATION_MISMATCH", "graph_code_alignment_score", 20, "No computational graph artifact was found."), ("CODE_GRAPH_NOTATION_MISMATCH", "evidence_score", 3, "Missing graph caps code auditability.")], [("FIG_GRAPH_MISSING", "graph_score", 40, "No computational graph artifact was found."), ("FIG_LABELING_INSUFFICIENT", "figure_evidence_score", 7, "Visualization evidence is present, but graph traceability is absent.")]),
    row("314264024", "王靖崴", "submissions/hw6/renamed/hw6_314264024_01_hw6.ipynb", (25, 17, 25, 20, 10), (30, 20, 25, 10), "A", "B", "CODE_GRAPH_NOTATION_MISMATCH", "FIG_GRAPH_INCOMPLETE;FIG_LABELING_INSUFFICIENT", "Code is complete and graph notation is aligned, but graph evidence is text-only in an unexecuted source cell.", "Text-only graph notation is model-specific, but not a rendered slide-style graph artifact.", [("CODE_GRAPH_NOTATION_MISMATCH", "graph_code_alignment_score", 3, "Graph notation is text-only source, so implementation/graph consistency is less independently auditable.")], [("FIG_GRAPH_INCOMPLETE", "graph_score", 10, "Graph evidence is text-only source rather than a rendered slide-style graph artifact."), ("FIG_LABELING_INSUFFICIENT", "figure_evidence_score", 5, "Text-only graph format caps figure explainability.")]),
    row("314264029", "方禹棠", "submissions/hw6/renamed/hw6_314264029_01_hw6.ipynb", (12, 14, 25, 20, 9), (22, 8, 12, 10), "A", "A", "CODE_ARCH_REPLACEMENT_INCOMPLETE;CODE_GRAPH_NOTATION_MISMATCH", "FIG_GRAPH_INCOMPLETE;FIG_FILTERS_UNCLEAR;FIG_FEATURE_MAPS_UNCLEAR;FIG_LABELING_INSUFFICIENT", "Submission has strong dense-network evidence, but it does not implement the required CNN convolution/pooling workflow.", "Graph and visual outputs are traceable but correspond to a dense model, not CNN filters/feature maps.", [("CODE_ARCH_REPLACEMENT_INCOMPLETE", "architecture_score", 13, "Code implements a dense 4-layer MNIST network rather than the required CNN architecture."), ("CODE_GRAPH_NOTATION_MISMATCH", "graph_code_alignment_score", 6, "Graph/code are aligned to a dense model, not the required CNN workflow."), ("CODE_GRAPH_NOTATION_MISMATCH", "evidence_score", 1, "Evidence is traceable but tied to the wrong architecture.")], [("FIG_GRAPH_INCOMPLETE", "graph_score", 18, "Graph describes the submitted dense model rather than the required CNN workflow."), ("FIG_FILTERS_UNCLEAR", "filters_score", 12, "Dense weights are visualized, not learned convolution filters."), ("FIG_FEATURE_MAPS_UNCLEAR", "feature_maps_score", 13, "Dense-layer responses are visualized, not CNN intermediate feature maps."), ("FIG_LABELING_INSUFFICIENT", "figure_evidence_score", 5, "Visuals are auditable but not tied to CNN deliverables.")]),
    row("314351005", "邱欣儀", "submissions/hw6/renamed", (25, 20, 25, 20, 10), (40, 20, 25, 15), "A", "A", "", "", "Complete PDF graph, matching code, momentum updates, result, filters, and maps.", "Complete graph and visualization evidence.", [], []),
    row("314351006", "陳叡儀", "submissions/hw6/renamed", (22, 12, 25, 20, 7), (25, 20, 25, 10), "B", "B", "CODE_ARCH_REPLACEMENT_INCOMPLETE;CODE_GRAPH_NOTATION_MISMATCH", "FIG_GRAPH_CODE_MISMATCH;FIG_LABELING_INSUFFICIENT", "Graph shows three hidden layers, but code uses two hidden fully connected layers before output.", "Graph is visible but does not fully match code hidden-layer count.", [("CODE_ARCH_REPLACEMENT_INCOMPLETE", "architecture_score", 3, "Notebook code implements two hidden fully connected layers while current rubric expects two additional hidden layers."), ("CODE_GRAPH_NOTATION_MISMATCH", "graph_code_alignment_score", 8, "Submitted graph and code disagree on hidden-layer count."), ("CODE_GRAPH_NOTATION_MISMATCH", "evidence_score", 3, "Graph/code mismatch caps code auditability.")], [("FIG_GRAPH_CODE_MISMATCH", "graph_score", 15, "Graph shows a different hidden-layer count from the submitted code."), ("FIG_LABELING_INSUFFICIENT", "figure_evidence_score", 5, "Graph/code mismatch caps figure explainability.")]),
    row("514660010", "林煜樺", "submissions/hw6/renamed/hw6_514660010_01_homework-6.ipynb", (25, 0, 25, 20, 7), (0, 20, 25, 8), "B", "B", "CODE_GRAPH_NOTATION_MISMATCH", "FIG_GRAPH_MISSING;FIG_LABELING_INSUFFICIENT", "Code is strong and target-reaching, but graph-consistent implementation cannot be verified because graph evidence is missing.", "Filters and feature maps are present, but no graph artifact exists.", [("CODE_GRAPH_NOTATION_MISMATCH", "graph_code_alignment_score", 20, "No computational graph artifact was found."), ("CODE_GRAPH_NOTATION_MISMATCH", "evidence_score", 3, "Missing graph caps code auditability.")], [("FIG_GRAPH_MISSING", "graph_score", 40, "No computational graph artifact was found."), ("FIG_LABELING_INSUFFICIENT", "figure_evidence_score", 7, "Visualization evidence is present, but graph traceability is absent.")]),
    row("514661019", "蔡宇量", "submissions/hw6/renamed/hw6_514661019_01_homework-6-514661019.ipynb", (25, 18, 25, 20, 10), (30, 20, 25, 10), "A", "B", "CODE_GRAPH_NOTATION_MISMATCH", "FIG_GRAPH_INCOMPLETE;FIG_LABELING_INSUFFICIENT", "Code is complete and graph notation is aligned, but graph evidence appears only as source comments.", "Source-comment graph notation is model-specific, but not a rendered slide-style graph artifact.", [("CODE_GRAPH_NOTATION_MISMATCH", "graph_code_alignment_score", 2, "Graph notation is source comments only, so implementation/graph consistency is less independently auditable.")], [("FIG_GRAPH_INCOMPLETE", "graph_score", 10, "Graph evidence appears as source comments rather than a rendered slide-style graph artifact."), ("FIG_LABELING_INSUFFICIENT", "figure_evidence_score", 5, "Source-comment graph format caps figure explainability.")]),
]


def total(values: tuple[int, ...]) -> int:
    return sum(values)


def combined_level(code_level: str, figure_level: str) -> str:
    order = {"A": 0, "B": 1, "C": 2, "D": 3}
    return max([code_level, figure_level], key=lambda value: order[value])


def write_csv(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def safe_name(name: object) -> str:
    return str(name).replace("/", "-").replace("\\", "-").replace(" ", "")


def append_tag(existing: str, tag: str) -> str:
    parts = [part for part in existing.split(";") if part]
    if tag not in parts:
        parts.append(tag)
    return ";".join(parts)


def apply_result_score_correction(item: dict[str, object]) -> None:
    correction = RESULT_SCORE_CORRECTIONS.get(str(item["student_id"]))
    if correction is None:
        return
    score, tag, band, note = correction
    code = item["code"]
    item["code"] = (code[0], code[1], code[2], score, code[4])
    item["code_tags"] = append_tag(str(item["code_tags"]), tag)
    item["code_note"] = f"{item['code_note']} Result band correction: {note}"
    deductions = [
        deduction
        for deduction in item["code_deductions"]
        if not (deduction[1] == "result_score" and deduction[0] in {"CODE_ACCURACY_BELOW_TARGET", "CODE_RESULT_BAND_BELOW_FULL"})
    ]
    deductions.append((tag, "result_score", 20 - score, f"Accuracy band {band} earns {score}/20. {note}"))
    item["code_deductions"] = deductions


def update_note(item: dict[str, object]) -> None:
    note_path = HW6 / "feedback" / f"{item['student_id']}_{safe_name(item['student_name'])}.md"
    code = item["code"]
    figure = item["figure"]
    code_total = total(code)
    figure_total = total(figure)
    combined = combined_level(item["code_level"], item["figure_level"])
    missing_evidence = []
    if item["code_tags"]:
        missing_evidence.append(f"Code deductions: {item['code_tags']}")
    if item["figure_tags"]:
        missing_evidence.append(f"Figure deductions: {item['figure_tags']}")
    if not missing_evidence:
        missing_evidence.append("None recorded.")
    section = f"""
# HW6 Feedback - {item['student_name']}

Student ID: `{item['student_id']}`
Submission path: `{item['submission_path']}`
Generated: `{NOW}`
Grader: `{GRADER}`

## Final Independent Scores

- HW6(code): `{code_total}` / 100
- HW6(figure): `{figure_total}` / 100
- Evidence level: `{combined}`
- Manual review needed: `no`

## HW6(code) Breakdown

| Category | Score | Max | Evidence note |
| --- | ---: | ---: | --- |
| Code-1. 架構修改正確性 | {code[0]} | 25 | {item['code_note']} |
| Graph-to-code consistency | {code[1]} | 20 | {item['code_note']} |
| Code-3. 訓練法正確性 | {code[2]} | 25 | {item['code_note']} |
| Code-4. 結果達成度 | {code[3]} | 20 | {item['code_note']} |
| Code-5. 證據與可稽核性 | {code[4]} | 10 | Code evidence level `{item['code_level']}` |

Code deduction tags: `{item['code_tags'] or 'none'}`

## HW6(figure) Breakdown

| Category | Score | Max | Evidence note |
| --- | ---: | ---: | --- |
| Figure-1. Computational graph 正確性與完整性 | {figure[0]} | 40 | {item['figure_note']} |
| Figure-2. learned filters 視覺化 | {figure[1]} | 20 | {item['figure_note']} |
| Figure-3. intermediate feature maps 視覺化 | {figure[2]} | 25 | {item['figure_note']} |
| Figure-4. 圖像證據與可稽核性 | {figure[3]} | 15 | Figure evidence level `{item['figure_level']}` |

Figure deduction tags: `{item['figure_tags'] or 'none'}`

## Evidence Observed

- Code evidence level: `{item['code_level']}`
- Figure evidence level: `{item['figure_level']}`
- Code note: {item['code_note']}
- Figure note: {item['figure_note']}

## Missing Evidence

{chr(10).join(f"- {line}" for line in missing_evidence)}

## Student-Facing Explanation

HW6 is reported as two independent scores. Code credit reflects implementation,
graph/code alignment, training method, result quality, and auditability. Figure
credit reflects the computational graph, learned filters, intermediate feature
maps, and figure auditability.

## TA / Instructor Audit Explanation

{item['code_note']} {item['figure_note']} Every non-full category above is
represented in `grading/hw6/code_deduction_log.csv` or
`grading/hw6/figure_deduction_log.csv`.
""".strip()
    note_path.parent.mkdir(parents=True, exist_ok=True)
    note_path.write_text(section + "\n", encoding="utf-8")


def main() -> int:
    code_rows: list[dict[str, object]] = []
    figure_rows: list[dict[str, object]] = []
    combined_rows: list[dict[str, object]] = []
    code_deductions: list[dict[str, object]] = []
    figure_deductions: list[dict[str, object]] = []

    for item in ROWS:
        apply_result_score_correction(item)
        code = item["code"]
        figure = item["figure"]
        code_total = total(code)
        figure_total = total(figure)
        code_rows.append({
            "student_name": item["student_name"],
            "student_id": item["student_id"],
            "submission_path": item["submission_path"],
            "architecture_score": code[0],
            "graph_code_alignment_score": code[1],
            "training_method_score": code[2],
            "result_score": code[3],
            "evidence_score": code[4],
            "code_penalty": 0,
            "hw6_code_score": code_total,
            "evidence_level": item["code_level"],
            "manual_review_needed": "no",
            "code_deduction_tags": item["code_tags"],
            "grader": GRADER,
            "graded_at": NOW,
            "notes": item["code_note"],
        })
        figure_rows.append({
            "student_name": item["student_name"],
            "student_id": item["student_id"],
            "submission_path": item["submission_path"],
            "graph_score": figure[0],
            "filters_score": figure[1],
            "feature_maps_score": figure[2],
            "figure_evidence_score": figure[3],
            "figure_penalty": 0,
            "hw6_figure_score": figure_total,
            "evidence_level": item["figure_level"],
            "manual_review_needed": "no",
            "figure_deduction_tags": item["figure_tags"],
            "grader": GRADER,
            "graded_at": NOW,
            "notes": item["figure_note"],
        })
        combined_rows.append({
            "student_name": item["student_name"],
            "student_id": item["student_id"],
            "submission_path": item["submission_path"],
            "hw6_code_score": code_total,
            "hw6_figure_score": figure_total,
            "evidence_level": combined_level(item["code_level"], item["figure_level"]),
            "manual_review_needed": "no",
            "code_deduction_summary": item["code_tags"],
            "figure_deduction_summary": item["figure_tags"],
            "final_comment": f"Code: {item['code_note']} Figure: {item['figure_note']}",
        })
        for tag, category, points, note in item["code_deductions"]:
            code_deductions.append({
                "student_name": item["student_name"],
                "student_id": item["student_id"],
                "score_type": "code",
                "deduction_tag": tag,
                "category": category,
                "points_deducted": points,
                "evidence_path": item["submission_path"],
                "note": note,
                "manual_review_needed": "no",
                "grader": GRADER,
                "recorded_at": NOW,
            })
        for tag, category, points, note in item["figure_deductions"]:
            figure_deductions.append({
                "student_name": item["student_name"],
                "student_id": item["student_id"],
                "score_type": "figure",
                "deduction_tag": tag,
                "category": category,
                "points_deducted": points,
                "evidence_path": item["submission_path"],
                "note": note,
                "manual_review_needed": "no",
                "grader": GRADER,
                "recorded_at": NOW,
            })
        update_note(item)

    write_csv(HW6 / "code_scores.csv", CODE_FIELDS, code_rows)
    write_csv(HW6 / "figure_scores.csv", FIGURE_FIELDS, figure_rows)
    write_csv(HW6 / "combined_summary.csv", COMBINED_FIELDS, combined_rows)
    write_csv(HW6 / "code_deduction_log.csv", DEDUCTION_FIELDS, code_deductions)
    write_csv(HW6 / "figure_deduction_log.csv", DEDUCTION_FIELDS, figure_deductions)
    write_csv(HW6 / "manual_review_students.csv", MANUAL_FIELDS, [])
    write_csv(HW6 / "unmatched_students.csv", UNMATCHED_FIELDS, [])

    print(f"HW6 dual grading rows: {len(ROWS)}")
    print(f"Code deductions: {len(code_deductions)}")
    print(f"Figure deductions: {len(figure_deductions)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
