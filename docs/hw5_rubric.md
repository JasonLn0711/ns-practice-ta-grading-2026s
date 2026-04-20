# HW5 Rubric

Total score: `100`.

HW5 asks students to modify HW4 by adding the configuration workflow from
`05_development.ipynb`, determine key hyperparameters, and provide evidence that
MNIST test accuracy reaches at least `98%`.

## Grading Discipline Gates

- No score without evidence: every non-empty score row must cite a submission
  path, evidence level, grader, timestamp, and per-student note.
- No deduction without a written reason: any non-full category score or penalty
  requires a deduction tag and reason in `deduction_summary` or
  `grading/hw5/deduction_log.csv`.
- No full credit for missing or unverifiable requirements: claims without code,
  output, logs, or traceable configuration cannot receive full points.
- Accuracy does not override missing development evidence: reaching `98%` does
  not give full requirement, technical, or evidence credit unless those items are
  separately supported.
- Suspicious duplication is not a guilt decision: use
  `POSSIBLE_COPYING_MANUAL_REVIEW` and create a manual review note.

## Category Breakdown

| Category | Points |
| --- | ---: |
| Submission completeness | 10 |
| Requirement fulfillment | 30 |
| Technical correctness | 30 |
| Result quality | 15 |
| Evidence and auditability | 15 |

## Submission Completeness: 10

| Item | Points | Full-credit evidence | Partial credit | Zero credit |
| --- | ---: | --- | --- | --- |
| Relevant submission exists | 2 | E3 map row and working file under `submissions/hw5/renamed/` or extracted folder | 1 if file exists but mapping is ambiguous | 0 if no relevant file |
| Code/notebook present | 3 | `.ipynb` or `.py` containing HW5 work | 1-2 if only report/screenshot or code fragment exists | 0 if no code-like artifact |
| Files are readable | 2 | file opens, archive extracts, notebook/script text can be inspected | 1 if partly readable | 0 if unreadable and no accepted replacement |
| Result/output artifact present | 2 | notebook output, log, screenshot, or report section showing MNIST test result | 1 if output is present but hard to locate | 0 if no result artifact |
| Student identity traceable | 1 | `student_file_map.csv` or `rename_map.csv` links file to student | 0.5 if identity is inferable but not mapped | 0 if identity cannot be tied to file |

Auto-checkable: file existence, suffixes, maps, archive readability.
Manual-review: whether screenshots/report fragments are acceptable.

## Requirement Fulfillment: 30

| Item | Points | Full-credit evidence | Partial credit | Zero credit |
| --- | ---: | --- | --- | --- |
| Configuration workflow/function | 10 | visible `configuration` function or equivalent workflow from/consistent with `05_development.ipynb`, used for HW5 | 5-8 if present but incomplete; max 5 if only mentioned | 0 if absent |
| Hidden nodes per hidden layer | 5 | explicit chosen hidden-node values for each hidden layer, in code/output/report | 2-4 if values are incomplete or hard to tie to model | 0 if missing |
| Learning rate | 5 | explicit learning-rate value and where it enters training | 2-4 if value exists but use is unclear | 0 if missing |
| Batch size | 5 | explicit batch-size value and batch construction/use | 2-4 if value exists but batching is unclear | 0 if missing |
| Epoch count | 5 | explicit epoch count and training loop/output showing use | 2-4 if value exists but loop/output is unclear | 0 if missing |

Cap rule: if no configuration workflow is shown, this category maxes at `15`
even if the final accuracy is high.

Auto-checkable: keywords for configuration, hidden, learning rate, batch, epoch.
Manual-review: whether an alternative workflow satisfies the assignment.

## Technical Correctness: 30

| Item | Points | Full-credit evidence | Partial credit | Zero credit |
| --- | ---: | --- | --- | --- |
| HW4 modification path | 8 | submitted code clearly modifies HW4-style model/training code | 4-6 if likely derived from HW4 but unclear | 0 if unrelated implementation |
| Configuration connected to training | 8 | chosen hyperparameters flow into model/training calls | 4-6 if partially connected; max 4 if only hard-coded output | 0 if configuration not used |
| MNIST train/test pipeline | 6 | code loads/uses MNIST train data for training and test data for evaluation | 3-5 if split is plausible but unclear | 0 if no valid MNIST test pipeline |
| Hyperparameter search or tuning behavior | 4 | evidence of comparing or deciding hyperparameters, not only final claim | 2-3 if one or two settings were tried | 0 if no tuning/development evidence |
| Code execution structure | 4 | code has enough imports, paths, and cell/order context to be rerun or inspected | 2-3 if minor path/dependency problems | 0 if code is not executable/inspectable |

Cap rules:

- If no code/notebook is present, this category maxes at `5`.
- If code cannot be inspected, this category maxes at `8`.
- If configuration is not connected to training, this category maxes at `15`.

Auto-checkable: code/notebook presence and basic keyword evidence.
Manual-review: all correctness decisions.

## Result Quality: 15

| Item | Points | Full-credit evidence | Partial credit | Zero credit |
| --- | ---: | --- | --- | --- |
| Target accuracy reached | 10 | MNIST test accuracy is shown as `>=98%` in output/log/report | 7-9 for `97.0-97.99%`; 4-6 for lower but meaningful result; max 3 for unsupported claim | 0 if no accuracy result |
| Test result is distinguishable from training result | 3 | output clearly labels test/evaluation accuracy or uses test set | 1-2 if likely but not explicit | 0 if train/test distinction is absent |
| Result tied to submitted configuration | 2 | result output is near the code/configuration that produced it or clearly referenced | 1 if weakly tied | 0 if result appears disconnected |

Cap rules:

- If result is a claim without output/log evidence, result quality maxes at `5`.
- If the result is not test accuracy, result quality maxes at `6`.

Auto-checkable: visible accuracy/result indicators.
Manual-review: credibility and near-threshold cases.

## Evidence and Auditability: 15

| Item | Points | Full-credit evidence | Partial credit | Zero credit |
| --- | ---: | --- | --- | --- |
| Evidence level assigned correctly | 3 | `A`, `B`, or `C` recorded and consistent with `docs/evidence_levels.md` | 1-2 if level is recorded but needs clarification | 0 if missing |
| Code/result traceability | 4 | code, configuration, and result can be connected by file/cell/output references | 2-3 if partially traceable | 0 if disconnected |
| Logs/output/configuration retained | 3 | logs, notebook outputs, screenshots, or report evidence support the score | 1-2 if weak or incomplete | 0 if no retained evidence |
| Deduction traceability | 3 | every lost point has a tag and written reason | 1-2 if reasons exist but are incomplete | 0 if deductions are unexplained |
| Per-student note quality | 2 | `grading/hw5/student_notes/<student_id>.md` records evidence, deductions, ambiguity, summary | 1 if note exists but is thin | 0 if missing |

Evidence caps:

- Level A: max `15`
- Level B: max `10`
- Level C: max `5`
- Missing evidence level: max `0`

## Required Deduction Tags

Use the closest tag from `docs/hw5_deduction_dictionary.md`. Common tags:

- `MISSING_REQUIRED_FILE`
- `CANNOT_VERIFY_RESULT`
- `ACCURACY_BELOW_TARGET`
- `NO_HYPERPARAMETER_SEARCH_EVIDENCE`
- `CODE_INCOMPLETE`
- `TEST_PIPELINE_UNCLEAR`
- `POSSIBLE_COPYING_MANUAL_REVIEW`

## Zero-Score Conditions

Use only when clearly justified:

- no relevant submission
- file cannot be opened and no replacement is allowed
- submission is unrelated to HW5
- confirmed academic-integrity violation after instructor decision

## TODO: Instructor Confirmation

- whether graders must rerun code
- exact late policy
- accepted non-notebook formats
- whether external libraries are allowed
- how to handle accuracy slightly below `98%`
