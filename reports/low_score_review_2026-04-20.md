# Low-Score Review Report - 2026-04-20

Reviewed at: `2026-04-20T22:17:58+08:00`

## Scope

- Reviewed every recorded score below 60 across `HW5`, `HW6(圖)`, and `HW6(code)`.
- `HW5`: no score below 60 was found.
- Original HW6 below-60 score records reviewed: 9.
- Records still below 60 after review: 8.
- Records adjusted above 60 after review: 1.
- Linked non-low score correction: `514660010` `HW6(code)` changed from `77` to `100` because the same missed graph evidence invalidated the prior code graph-to-code deduction.

## Review Decisions

| Student ID | Name | Score | Original | Reviewed | Decision | Reason |
| --- | --- | --- | ---: | ---: | --- | --- |
| `113304030` | 鄭丞言 | `HW6(圖)` | 26 | 26 | `keep_below_60` | Only intermediate feature maps were found. No computational graph artifact and no learned-filter plot were auditable, so Figure-1 and Figure-2 remain zero under the official figure rubric. |
| `214952033` | 陳奕樺 | `HW6(code)` | 49 | 49 | `keep_below_60` | Notebook shows a CNN with only one hidden fully connected layer before output, no computational graph, and Adam rather than explicit mini-batch stochastic gradient with momentum. High accuracy does not override missing architecture, graph-to-code, or momentum evidence. |
| `214952033` | 陳奕樺 | `HW6(圖)` | 53 | 53 | `keep_below_60` | Learned filters and feature maps are present, but no computational graph artifact is present; graph evidence is a required 40-point figure category. |
| `314261002` | 洪至寬 | `HW6(圖)` | 53 | 53 | `keep_below_60` | Filters and feature maps are present. The notebook references image1.png as CNN structure, but the referenced image is not recoverable in the submission bundle, so graph credit is not auditable. |
| `314264001` | 陳耘加 | `HW6(圖)` | 53 | 53 | `keep_below_60` | Filters and feature maps are present, but no computational graph artifact was found. Missing graph evidence keeps Figure-1 at zero and caps figure auditability. |
| `314264019` | 游乙倢 | `HW6(圖)` | 53 | 53 | `keep_below_60` | Filters and feature maps are present, but no computational graph artifact was found. Missing graph evidence keeps Figure-1 at zero and caps figure auditability. |
| `314264023` | 蔡宜勳 | `HW6(圖)` | 53 | 53 | `keep_below_60` | Filters and feature maps are present, but no computational graph artifact was found. Missing graph evidence keeps Figure-1 at zero and caps figure auditability. |
| `314264029` | 方禹棠 | `HW6(圖)` | 52 | 52 | `keep_below_60` | The graph and visuals are traceable but describe a dense MLP, not the required CNN workflow. The visualized weights are not learned convolution filters, and dense activations are not CNN intermediate feature maps. |
| `514660010` | 林煜樺 | `HW6(圖)` | 53 | 100 | `adjust_above_60` | Review found the embedded CNN computational graph in notebook markdown with source-code variable names, forward/backward relations, and momentum context. Filters, input digit, and feature maps were already present. |

## Adjustment Made

- `514660010 林煜樺` `HW6(圖)`: `53 -> 100`.
- Linked correction: `514660010 林煜樺` `HW6(code)`: `77 -> 100` because the prior `CODE_GRAPH_NOTATION_MISMATCH` deduction depended on the same missed graph evidence.
- Superseded deduction rows for `514660010` were removed from canonical HW6 deduction logs so validation and reports match the corrected current score state.
- Detailed before/after fields are stored in `grading/hw6/score_adjustment_log_2026-04-20.csv`.

## Files Written

- `grading/low_score_reviews_2026-04-20.csv`
- `grading/low_score_reviews_2026-04-20/`
- `grading/hw6/score_adjustment_log_2026-04-20.csv`

## Policy Notes

- A graph or figure mentioned by filename but not recoverable in the submitted bundle was treated as not auditable.
- High accuracy did not override missing architecture, graph-to-code, or momentum evidence.
- Dense-network visualizations were not treated as CNN learned filters or CNN feature maps.
