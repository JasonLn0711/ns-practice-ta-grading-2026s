# HW6(figure) Deduction Dictionary

Use these tags in `grading/hw6/figure_scores.csv`,
`grading/hw6/figure_deduction_log.csv`, student notes, and feedback.

| Tag | Description | Typical impact | Manual review | Required note format |
| --- | --- | ---: | --- | --- |
| `FIG_GRAPH_MISSING` | Computational graph artifact is absent. | 20-40 | no unless disputed | `Graph missing from <files reviewed>.` |
| `FIG_GRAPH_INCOMPLETE` | Graph exists but misses architecture, notation, forward flow, or backward relationship. | 3-25 | if format policy is unclear | `Graph incomplete: <observable issue>; evidence: <file/cell>.` |
| `FIG_GRAPH_CODE_MISMATCH` | Graph does not match submitted code. | 5-25 | if mismatch changes score interpretation | `Graph/code mismatch: <observable mismatch>; evidence: <files>.` |
| `FIG_FILTERS_MISSING` | Learned filters are absent. | 8-20 | no unless embedded output is disputed | `Filters missing from <files reviewed>.` |
| `FIG_FILTERS_UNCLEAR` | Filters are generic, unreadable, unlabeled, or not tied to the trained model. | 3-15 | if source is ambiguous | `Filters unclear: <observable issue>; evidence: <file/cell>.` |
| `FIG_FEATURE_MAPS_MISSING` | Intermediate feature maps are absent. | 10-25 | no unless embedded output is disputed | `Feature maps missing from <files reviewed>.` |
| `FIG_FEATURE_MAPS_UNCLEAR` | Feature maps are unlabeled, generic, or not tied to intermediate layers. | 3-15 | if source is ambiguous | `Feature maps unclear: <observable issue>; evidence: <file/cell>.` |
| `FIG_LABELING_INSUFFICIENT` | Figure labels/titles/context are insufficient for audit. | 2-12 | no | `Labeling insufficient: <observable issue>; evidence: <file/cell>.` |
| `FIG_NOT_AUDITABLE` | Figure evidence cannot be traced to the submission/model. | 5-30 | yes if score impact is large | `Figure not auditable: <observable issue>; evidence: <file/path>.` |
| `FIG_POSSIBLE_COPYING_MANUAL_REVIEW` | Figure similarity requires instructor review. | 0 pending decision | yes | `Manual review: similar figure in <students/files>; no accusation made.` |

Deduction ranges are guides. The rubric category caps are controlling.
