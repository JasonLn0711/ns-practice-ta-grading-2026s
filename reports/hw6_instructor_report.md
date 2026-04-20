# HW6 Instructor Report

Generated: `2026-04-20`

## Overview

HW6 is now reported as two independent official workbook scores:

- `HW6(code)`: implementation, graph-to-code consistency, training method, result quality, and evidence.
- `HW6(圖)`: computational graph, learned filters, intermediate feature maps, and figure evidence.

| Score | Graded rows | Average | Manual reviews |
| --- | ---: | ---: | ---: |
| HW6(code) | 21 | 88.38 | 0 |
| HW6(圖) | 21 | 78.38 | 0 |

Workbook write-back status:

- Rows updated in copied workbook: `21`
- Workbook rows left unchanged due to missing reliable HW6 evidence: `4`
- Unmatched graded students in workbook: `0`

## Category Averages

### HW6(code)

| Category | Average |
| --- | ---: |
| architecture_score | 23.38 |
| graph_code_alignment_score | 12.43 |
| training_method_score | 24.38 |
| result_score | 19.38 |
| evidence_score | 8.81 |

### HW6(圖)

| Category | Average |
| --- | ---: |
| graph_score | 24.14 |
| filters_score | 18.48 |
| feature_maps_score | 24.24 |
| figure_evidence_score | 11.52 |

## Common Deduction Reasons

### HW6(code)

- `CODE_GRAPH_NOTATION_MISMATCH`: 11
- `CODE_RESULT_BAND_BELOW_FULL`: 6
- `CODE_ARCH_REPLACEMENT_INCOMPLETE`: 4
- `CODE_ACCURACY_BELOW_TARGET`: 1
- `CODE_MOMENTUM_MISSING`: 1

### HW6(圖)

- `FIG_LABELING_INSUFFICIENT`: 11
- `FIG_GRAPH_MISSING`: 7
- `FIG_GRAPH_INCOMPLETE`: 3
- `FIG_FEATURE_MAPS_UNCLEAR`: 2
- `FIG_FILTERS_MISSING`: 1
- `FIG_FILTERS_UNCLEAR`: 1
- `FIG_GRAPH_CODE_MISMATCH`: 1

## Policy Issues Needing Instructor Decision

- Confirm accepted computational graph formats: separate image/PDF, rendered notebook output, markdown diagram, text-only source cell, or code comments.
- Confirm the hidden-layer interpretation: current grading treats the requirement as three hidden fully connected layers total after convolution/pooling, because HW6 asks for two more hidden layers.
- Confirm whether external frameworks such as PyTorch should receive full credit when architecture, momentum, graph, result, and visualization evidence are present.
- Confirm that dense non-CNN submissions should not receive full architecture/filter/feature-map credit even if they reach the accuracy target.
- Confirm late-policy handling before importing final grades into the LMS.

## Audit Sources

- `reports/hw6_master_audit_report.md`
- `reports/hw6_code_audit_report.md`
- `reports/hw6_figure_audit_report.md`
- `reports/hw6_workbook_writeback_report.md`
- `grading/hw6/code_scores.csv`
- `grading/hw6/figure_scores.csv`
- `grading/hw6/combined_summary.csv`
