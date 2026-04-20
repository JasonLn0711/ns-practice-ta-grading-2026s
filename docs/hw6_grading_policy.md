# HW6 Dual-Score Grading Policy

HW6 is graded as two independent scores:

- `HW6(code)`: 100 points
- `HW6(圖)`: 100 points

Do not average or merge these scores inside the grading workspace. The workbook
write-back fills `HW6(圖)` and `HW6(code)` separately.

## Operating Rules

- Grade requirement fulfillment, not effort.
- Grade correctness, not confidence.
- Grade evidence, not claims.
- No full credit for a missing or unverifiable required item.
- No deduction without a written reason.
- Every non-full score must trace to a rubric item and deduction tag.
- Accuracy does not compensate for missing graph, architecture, filter, or
  feature-map evidence.
- Code and figure are independent: a strong code submission can still receive a
  low figure score, and a strong figure submission can still receive a low code
  score.
- Graph/code mismatch is deducted twice: code loses graph-consistency credit,
  and figure loses graph/code-consistency credit.
- Suspicious copying is a manual-review flag, not an automatic guilt finding.

## Edge Cases

| Edge case | Policy |
| --- | --- |
| Broken file structure | Grade any readable evidence; record missing/unreadable files. |
| Cleared notebook outputs | Code can receive implementation credit, but result/evidence credit is capped unless logs or other outputs are present. |
| Claimed accuracy without traceable run | Result quality maxes at the claim-only cap in the code rubric. |
| Graph visible but not alignable to code | Deduct code graph-consistency and figure graph consistency. |
| Filters or feature maps unlabeled | Award only partial visualization/explainability credit. |
| Multiple versions submitted | Use the latest clearly submitted version unless instructor says otherwise; record which file was graded. |
| Missing figure but code exists | Grade code independently; figure categories for missing deliverables receive zero or low partial credit. |
| Missing code but figure exists | Grade figure independently; code categories requiring implementation evidence receive zero or low partial credit. |
| Late submission | TODO: instructor confirmation before applying penalties. |
| Partial work with high-quality reasoning | Award only rubric-supported partial credit; do not give presentation/effort credit outside the rubric. |
| Ambiguous workbook name match | Do not guess; leave workbook cells unchanged and record in `unmatched_students.csv`. |
| No reliable workbook match | Do not guess; leave workbook cells unchanged and record in `unmatched_students.csv`. |

## Workbook Release Rule

The original workbook must not be overwritten. The write-back script writes only
to a copied output workbook and only touches the `HW6(圖)` and `HW6(code)` cells
on the `HW成績` sheet.
