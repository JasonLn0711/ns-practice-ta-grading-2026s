# HW6(figure) Rubric

Total score: `100`.

HW6(figure) grades the computational graph and required visualizations. It does
not award code implementation credit except where figure/code consistency is
required by the assignment.

## Category Breakdown

| Category | Points |
| --- | ---: |
| Computational graph correctness and completeness | 40 |
| Learned filters visualization quality and correctness | 20 |
| Intermediate feature maps visualization quality and correctness | 25 |
| Figure evidence and explainability | 15 |

## Computational Graph Correctness and Completeness: 40

| Item | Points | Full credit | Partial credit | Zero credit |
| --- | ---: | --- | --- | --- |
| Architecture completeness | 10 | Graph shows the submitted HW6 architecture, including added hidden layers. | 5-9 for partial architecture. | 0 if absent/unrelated. |
| Notation correctness | 7 | Uses clear slide-48-style or equivalent notation. | 3-6 for partial notation. | 0 if notation missing/unusable. |
| Forward-flow correctness | 7 | Data/layer flow is correct and ordered. | 3-6 for minor omissions. | 0 if flow is wrong. |
| Backward/gradient expressiveness | 6 | Backprop/gradient relationships are represented or clearly implied. | 2-5 for weak/incomplete gradient relationship. | 0 if absent. |
| Slide-48-style logic | 4 | Graph is comparable to the requested slide style. | 1-3 for text-only or simplified format. | 0 if not comparable. |
| Consistency with code | 6 | Graph matches the submitted code architecture and notation. | 2-5 for partial mismatch. | 0 if graph contradicts code. |

Caps:

- No graph artifact: category score `0`.
- Text-only graph/comment notation: max `30`.
- Generic graph not tied to the student model: max `20`.
- Graph/code architecture mismatch: max `28`.

Manual-review triggers: reused graph, figure/code mismatch that changes score,
or graph not attributable to the student submission.

## Learned Filters Visualization: 20

| Item | Points | Full credit | Partial credit | Zero credit |
| --- | ---: | --- | --- | --- |
| Learned filters shown | 10 | Trained filters are visibly plotted. | 4-9 for incomplete/unclear plots. | 0 if absent. |
| Tied to trained model | 5 | Filters clearly come from the submitted trained model. | 2-4 if likely but weak. | 0 if generic/unrelated. |
| Filter layout readable | 3 | Figure is readable enough for audit. | 1-2 if cramped/unclear. | 0 if unreadable. |
| Labels/context | 2 | Figure or note identifies filter source/layer. | 1 if weak. | 0 if unlabeled. |

Caps:

- Generic image not tied to model: max `8`.
- Dense weights shown instead of convolution filters: max `8` unless instructor
  accepts dense non-CNN work.

## Intermediate Feature Maps Visualization: 25

| Item | Points | Full credit | Partial credit | Zero credit |
| --- | ---: | --- | --- | --- |
| Feature maps shown | 10 | Intermediate feature maps are visibly plotted. | 4-9 for incomplete plots. | 0 if absent. |
| Intermediate layer traceability | 6 | Maps correspond to intermediate layers. | 2-5 if layer source is weak. | 0 if not traceable. |
| Arbitrary input digit context | 4 | Input digit is visible or identified. | 1-3 if partial. | 0 if missing. |
| Model consistency | 3 | Maps come from the submitted trained model. | 1-2 if likely but weak. | 0 if unrelated. |
| Readability | 2 | Visualization is auditable. | 1 if hard to read. | 0 if unreadable. |

Caps:

- Dense activations shown instead of CNN feature maps: max `12` unless
  instructor accepts dense non-CNN work.
- No visible input digit or layer source: max `18`.

## Figure Evidence and Explainability: 15

| Item | Points | Full credit | Partial credit | Zero credit |
| --- | ---: | --- | --- | --- |
| File/source traceability | 4 | Figure files or notebook cells are traceable. | 1-3 for partial traceability. | 0 if disconnected. |
| Labels/titles sufficient | 4 | Graph, filters, and maps are labeled enough for audit. | 1-3 for weak labels. | 0 if unlabeled. |
| Figure/code alignment note | 3 | Alignment with code is clear from submission or TA note. | 1-2 for partial alignment. | 0 if no alignment. |
| Deduction traceability | 2 | Every lost point has a tag and reason. | 1 if incomplete. | 0 if missing. |
| Per-student note exists | 2 | Dual-score note records figure evidence and final score. | 1 if thin. | 0 if missing. |

Evidence caps are defined in `docs/hw6_evidence_levels.md`.
