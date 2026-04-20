# HW6 Edge Case Policy

Use this policy when the submission does not fit the normal grading path. If a final policy is not supported by course files, leave a TODO and grade conservatively from available evidence.

| Edge case | Handling rule | Required record |
| --- | --- | --- |
| Submission exists but file structure is broken | Grade only inspectable files. Do not award full completeness/evidence credit if core artifacts cannot be located. | Note searched paths and missing files. |
| Notebook exists but outputs are cleared | Grade code normally where inspectable, but cap execution/result evidence unless logs or screenshots support the run. | Record `CODE_RESULT_NOT_VERIFIABLE` or evidence cap. |
| Claimed accuracy exists but no traceable run evidence | Do not award full result credit. Use Level C/D evidence unless another credible output supports the claim. | Record claim and missing evidence. |
| Graph is visually present but not usable for code alignment | Award only partial Figure-1 credit; deduct Code-2 if code cannot be mapped to the graph. | Record graph/code mismatch or notation issue. |
| Filters / feature maps are present but unlabeled | Award existence points if recognizable, but cap readability, traceability, and figure evidence items. | Record `FIG_LABELING_INSUFFICIENT` and relevant unclear/not-traceable tag. |
| Multiple submission versions | Use the official/latest E3 version if identifiable. If not reliable, mark manual review and avoid guessing. | Record chosen source or ambiguity. |
| Missing figure submission but code exists | Grade code from code evidence; figure missing categories receive zero or conservative partial credit only if figure evidence is embedded in code outputs. | Record missing figure evidence. |
| Missing code submission but figure exists | Grade figure from figure evidence; code missing categories receive zero or conservative partial credit only if code evidence is embedded elsewhere. | Record missing code evidence. |
| Late submission | TODO: instructor confirmation needed. Do not invent a penalty. | Record late flag only if visible. |
| Partial work with good reasoning | Award only requirement evidence that is actually present; reasoning alone cannot replace required code/figures/results. | Record partial-credit basis. |
| Ambiguous student-name matching in workbook | Do not write scores for ambiguous matches. | Add row to `grading/hw6/unmatched_students.csv`. |
| No reliable workbook match | Leave workbook cells unchanged. | Add row to `grading/hw6/unmatched_students.csv`. |

## TODO: Instructor Confirmation

- Late submission penalty, if any.
- Whether source-comment computational graphs can receive full graph credit.
- Whether dense non-CNN submissions can receive full learned-filter/feature-map credit.
- Whether TAs must rerun notebooks or can rely on retained outputs.

