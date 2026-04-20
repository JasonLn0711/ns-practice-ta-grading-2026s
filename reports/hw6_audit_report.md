# HW6 Audit Report

Generated: 2026-04-20T20:09:51

## Overview

- Number of submissions graded: 21
- Average score: 89.43
- Manual reviews: 0

## Distribution By Category

| Category | Average |
| --- | ---: |
| completeness_score | 9.19 |
| architecture_score | 14.05 |
| graph_score | 9.24 |
| training_score | 19.52 |
| result_score | 9.95 |
| visualization_score | 14.38 |
| evidence_score | 13.10 |

## Common Deduction Reasons

- ACCURACY_BELOW_TARGET: 1
- CODE_INCOMPLETE: 9
- COMPUTATIONAL_GRAPH_MISSING: 14
- FEATURE_MAP_MISSING: 1
- FILTER_PLOT_MISSING: 2
- MISSING_REQUIRED_FILE: 9
- MOMENTUM_NOT_IMPLEMENTED: 1

## Manual Reviews

- none recorded

## Policy Issues Needing Instructor Decision

- Confirm accepted computational graph formats: separate image/PDF, rendered notebook output, markdown diagram, text-only source cell, or code comments.
- Confirm the hidden-layer interpretation: current grading treats the requirement as three hidden fully connected layers total after convolution/pooling, because HW6 asks for two more hidden layers.
- Confirm whether external frameworks such as PyTorch should receive full credit when architecture, momentum, graph, result, and visualization evidence are present.
- Confirm that dense non-CNN submissions should not receive full architecture/filter/feature-map credit even if they reach the accuracy target.
- Confirm late-policy handling before importing final grades into the LMS.

## Audit Sources

- `grading/hw6/scores.csv`
- `grading/hw6/deduction_log.csv`
- `grading/hw6/evidence.csv`
