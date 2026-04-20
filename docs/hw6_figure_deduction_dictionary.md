# HW6(圖) Deduction Dictionary

Use these tags in `grading/hw6/figure_scores.csv`, `grading/hw6/figure_deduction_log.csv`, and per-student feedback notes. Every non-full figure category must have a written reason tied to one or more tags.

| Tag | Precise description | Affected item / typical impact | Manual review | Required note format |
| --- | --- | --- | --- | --- |
| `FIG_GRAPH_MISSING` | Computational graph artifact is absent. | Figure-1, up to `40` points | no unless disputed | `Graph missing from <files reviewed>.` |
| `FIG_GRAPH_INCOMPLETE` | Graph exists but misses architecture, notation, forward flow, or backward relationship. | Figure-1, typically `3-25` points | if format policy is unclear | `Graph incomplete: <observable issue>; evidence: <file/cell>.` |
| `FIG_GRAPH_NOTATION_INCORRECT` | Graph notation is wrong, inconsistent, or unusable for code alignment. | Figure-1B, typically `3-10` points | if notation policy is unclear | `Graph notation issue: <observable issue>; evidence: <graph>.` |
| `FIG_GRAPH_CODE_MISMATCH` | Graph does not match the submitted code architecture, flow, or notation. | Figure-1 and cross-rule deduction | if mismatch changes score interpretation | `Graph/code mismatch: <observable mismatch>; evidence: <files>.` |
| `FIG_FILTERS_MISSING` | Learned filters are absent. | Figure-2, up to `20` points | no unless embedded output is disputed | `Filters missing from <files reviewed>.` |
| `FIG_FILTERS_UNCLEAR` | Filters are incomplete, unreadable, generic, unlabeled, or not recognizable as learned filters. | Figure-2A/B, typically `2-14` points | if figure source is ambiguous | `Filters unclear: <observable issue>; evidence: <file/cell>.` |
| `FIG_FILTERS_NOT_TRACEABLE` | Filters are visible but cannot be tied to the trained submitted model. | Figure-2C, typically `2-6` points | if source is ambiguous | `Filters not traceable: <observable issue>; evidence: <file/cell>.` |
| `FIG_FEATURE_MAPS_MISSING` | Intermediate feature maps are absent. | Figure-3, up to `25` points | no unless embedded output is disputed | `Feature maps missing from <files reviewed>.` |
| `FIG_FEATURE_MAPS_UNCLEAR` | Feature maps are incomplete, unlabeled, not tied to a layer/stage, or hard to interpret. | Figure-3, typically `2-15` points | if map source is ambiguous | `Feature maps unclear: <observable issue>; evidence: <file/cell>.` |
| `FIG_FEATURE_MAPS_NOT_TRACEABLE` | Feature maps are visible but cannot be tied to the input digit, layer, or submitted model. | Figure-3, typically `2-10` points | if traceability affects score materially | `Feature maps not traceable: <observable issue>; evidence: <file/cell>.` |
| `FIG_LABELING_INSUFFICIENT` | Titles, labels, captions, or context are insufficient for audit. | Figure-4A/B/C, typically `2-12` points | no | `Labeling insufficient: <observable issue>; evidence: <file/cell>.` |
| `FIG_NOT_AUDITABLE` | Figure evidence cannot be traced to submission/model, or another TA could not reconstruct the basis for scoring. | Figure-4, typically `5-15` points | yes if score impact is large | `Figure not auditable: <observable issue>; evidence: <file/path>.` |
| `FIG_POSSIBLE_COPYING_MANUAL_REVIEW` | Similarity or suspicious duplication requires instructor review. This tag records concern only; it is not an accusation. | Manual review; no automatic penalty | yes | `Manual review: similar figure in <students/files>; no accusation made.` |

Rubric point allocations are controlling; deduction ranges are guides for consistent written reasoning.
