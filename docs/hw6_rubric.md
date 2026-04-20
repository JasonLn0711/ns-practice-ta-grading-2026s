# HW6 Rubric

Total score: `100`.

HW6 asks students to replace a fully connected layer with two more hidden layers,
draw a computational graph similar to slide 48, use that notation in code, train
with mini-batch stochastic gradient with momentum, reach at least `98%` MNIST
test accuracy, and plot learned filters plus intermediate feature maps.

## Grading Discipline Gates

- No score without evidence: every non-empty score row must cite a submission
  path, evidence level, grader, timestamp, and per-student note.
- No deduction without a written reason: any non-full category score or penalty
  requires a deduction tag and reason in `deduction_summary` or
  `grading/hw6/deduction_log.csv`.
- No full credit for missing or unverifiable requirements: claims without code,
  graph, output, logs, or visualization evidence cannot receive full points.
- Accuracy does not override missing architecture/graph/visualization evidence:
  reaching `98%` only supports result quality.
- Suspicious duplication is not a guilt decision: use
  `POSSIBLE_COPYING_MANUAL_REVIEW` and create a manual review note.

## Category Breakdown

| Category | Points |
| --- | ---: |
| Submission completeness | 10 |
| Architecture modification correctness | 15 |
| Computational graph correctness | 15 |
| Training method correctness | 20 |
| Result quality | 10 |
| Visualization requirements | 15 |
| Evidence and auditability | 15 |

## Submission Completeness: 10

| Item | Points | Full-credit evidence | Partial credit | Zero credit |
| --- | ---: | --- | --- | --- |
| Relevant submission exists | 1 | E3 map row and working file under `submissions/hw6/renamed/` or extracted folder | 0.5 if mapping is ambiguous | 0 if no relevant file |
| Code/notebook present | 3 | `.ipynb` or `.py` containing HW6 work | 1-2 if only code fragment/report exists | 0 if no code-like artifact |
| Computational graph artifact present | 2 | graph image/PDF/notebook output/report section | 1 if graph-like evidence is hard to locate | 0 if absent |
| Visualization artifacts present | 2 | learned filter and feature-map outputs or files | 1 if only one visualization is visible | 0 if both absent |
| Result/output artifact present | 1 | output/log/report section showing MNIST result | 0.5 if hard to locate | 0 if absent |
| Files are readable and traceable | 1 | files open and map to one student | 0.5 if partly readable | 0 if unreadable/unmapped |

Auto-checkable: file existence, suffixes, maps, archive readability.
Manual-review: whether embedded notebook output is enough graph/plot evidence.

## Architecture Modification Correctness: 15

| Item | Points | Full-credit evidence | Partial credit | Zero credit |
| --- | ---: | --- | --- | --- |
| Fully connected layer replacement | 5 | code visibly replaces the prior fully connected layer structure | 2-4 if model change is plausible but not clear | 0 if no replacement evidence |
| Two additional hidden layers | 6 | two additional hidden layers are implemented and used in forward/training path | 3-5 if layers exist but usage/dimensions are unclear | 0 if absent |
| Dimension and data-flow consistency | 4 | shapes/data flow are internally consistent and tied to MNIST/CNN workflow | 2-3 if mostly plausible but incomplete | 0 if flow cannot be verified |

Cap rules:

- If no code/notebook is present, this category maxes at `3`.
- If architecture is only described in prose/screenshot, this category maxes at `6`.

Auto-checkable: code/notebook presence.
Manual-review: all architecture correctness decisions.

## Computational Graph Correctness: 15

| Item | Points | Full-credit evidence | Partial credit | Zero credit |
| --- | ---: | --- | --- | --- |
| Graph is present and model-specific | 5 | graph file/output depicts the submitted model, not a generic diagram | 2-4 if graph exists but model link is weak | 0 if absent |
| Slide-48-style notation | 5 | graph is similar to required slide style and uses comparable notation | 2-4 if notation is partially aligned | 0 if notation is unrelated/missing |
| Code uses graph notation | 5 | variables/notation in code correspond to graph labels or are clearly mapped | 2-4 if mapping is partial | 0 if no code/graph alignment |

Cap rules:

- If the graph is missing, this category is `0`.
- If graph exists but cannot be tied to code, category maxes at `8`.

Auto-checkable: graph filenames and graph keywords.
Manual-review: graph correctness and notation alignment.

## Training Method Correctness: 20

| Item | Points | Full-credit evidence | Partial credit | Zero credit |
| --- | ---: | --- | --- | --- |
| Mini-batch stochastic gradient training | 6 | code constructs/uses mini-batches in training | 3-5 if batching is likely but unclear | 0 if absent |
| Momentum implementation | 8 | update rule/state includes momentum, not just a comment | 4-7 if partially implemented or ambiguous | 0 if absent |
| Training loop tied to HW6 model | 4 | training loop updates the submitted HW6 architecture | 2-3 if connection is plausible but unclear | 0 if disconnected |
| Loss/update traceability | 2 | loss/update variables are inspectable and support training claim | 1 if weak | 0 if not traceable |

Cap rules:

- If momentum is only mentioned, training method maxes at `12`.
- If momentum is absent, training method maxes at `10`.
- If the training loop is disconnected from the HW6 model, maxes at `8`.

Auto-checkable: momentum and batch keyword indicators.
Manual-review: whether momentum is actually implemented.

## Result Quality: 10

| Item | Points | Full-credit evidence | Partial credit | Zero credit |
| --- | ---: | --- | --- | --- |
| Target accuracy reached | 6 | MNIST test accuracy is shown as `>=98%` in output/log/report | 4-5 for `97.0-97.99%`; 2-3 for lower but meaningful result; max 2 for unsupported claim | 0 if no result |
| Test result is distinguishable from training result | 2 | output clearly labels test/evaluation accuracy or uses test set | 1 if likely but not explicit | 0 if train/test distinction is absent |
| Result tied to submitted HW6 model | 2 | output is tied to the architecture/training code being graded | 1 if weakly tied | 0 if disconnected |

Cap rules:

- If result is a claim without output/log evidence, result quality maxes at `3`.
- If result is not from the HW6 architecture, result quality maxes at `4`.

Auto-checkable: visible accuracy/result indicators.
Manual-review: credibility and near-threshold cases.

## Visualization Requirements: 15

| Item | Points | Full-credit evidence | Partial credit | Zero credit |
| --- | ---: | --- | --- | --- |
| Learned filters plotted | 6 | filter plot appears as image/PDF/notebook output and is tied to trained model | 3-5 if plot exists but model link is weak | 0 if absent |
| Intermediate feature maps plotted | 6 | feature-map plot appears and is tied to an intermediate layer | 3-5 if plot exists but layer/model link is weak | 0 if absent |
| Arbitrary input digit context | 3 | chosen input digit is visible/described and connected to feature maps | 1-2 if input context is partial | 0 if missing |

Cap rules:

- If both required plot types are missing, visualization score is `0`.
- If plots are present but not tied to the implemented model, visualization maxes
  at `8`.

Auto-checkable: filter/feature-map filenames or keywords.
Manual-review: whether plots are meaningful and linked to the model.

## Evidence and Auditability: 15

| Item | Points | Full-credit evidence | Partial credit | Zero credit |
| --- | ---: | --- | --- | --- |
| Evidence level assigned correctly | 3 | `A`, `B`, or `C` recorded and consistent with `docs/evidence_levels.md` | 1-2 if level is recorded but needs clarification | 0 if missing |
| Code/result/graph/plot traceability | 4 | code, model, graph, plots, and result can be connected by file/cell/output references | 2-3 if partially traceable | 0 if disconnected |
| Logs/output/model evidence retained | 3 | logs, notebook outputs, screenshots, or report evidence support the score | 1-2 if weak or incomplete | 0 if no retained evidence |
| Deduction traceability | 3 | every lost point has a tag and written reason | 1-2 if reasons exist but are incomplete | 0 if deductions are unexplained |
| Per-student note quality | 2 | `grading/hw6/student_notes/<student_id>.md` records evidence, deductions, ambiguity, summary | 1 if note exists but is thin | 0 if missing |

Evidence caps:

- Level A: max `15`
- Level B: max `10`
- Level C: max `5`
- Missing evidence level: max `0`

## Required Deduction Tags

Use the closest tag from `docs/hw6_deduction_dictionary.md`. Common tags:

- `MISSING_REQUIRED_FILE`
- `CANNOT_VERIFY_RESULT`
- `ACCURACY_BELOW_TARGET`
- `COMPUTATIONAL_GRAPH_MISSING`
- `MOMENTUM_NOT_IMPLEMENTED`
- `FILTER_PLOT_MISSING`
- `FEATURE_MAP_MISSING`
- `CODE_INCOMPLETE`
- `TEST_PIPELINE_UNCLEAR`
- `POSSIBLE_COPYING_MANUAL_REVIEW`

## Zero-Score Conditions

Use only when clearly justified:

- no relevant submission
- file cannot be opened and no replacement is allowed
- submission is unrelated to HW6
- confirmed academic-integrity violation after instructor decision

## TODO: Instructor Confirmation

- whether graph notation must exactly match slide 48
- accepted graph/plot formats
- whether graders must rerun code
- exact late policy
- whether external frameworks are allowed
- how to handle accuracy slightly below `98%`
