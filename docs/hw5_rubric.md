# HW5 Rubric

Total score: `100`.

HW5 asks students to modify HW4 by adding the configuration workflow from
`05_development.ipynb`, determine key hyperparameters, and provide evidence that
MNIST test accuracy reaches at least `98%`.

## Category Breakdown

| Category | Points |
| --- | ---: |
| Submission completeness | 10 |
| Requirement fulfillment | 30 |
| Technical correctness | 30 |
| Result quality | 15 |
| Evidence and auditability | 15 |

## Submission Completeness: 10

Full credit:

- relevant HW5 submission is present
- code or notebook is present
- output or result evidence is present
- submission can be mapped to one student

Partial credit:

- `7`: minor file organization problem but core files are present
- `4`: code present but output/result evidence is missing
- `2`: only screenshots/report fragments are present

Zero credit:

- no relevant HW5 submission
- file cannot be opened and no replacement is allowed

Auto-checkable: file existence, file type, archive readability, student map.

Manual-review needed: whether screenshots/report fragments count as enough
submission evidence.

## Requirement Fulfillment: 30

Full credit:

- configuration function or equivalent workflow is present
- hidden nodes for each hidden layer are explicitly determined
- learning rate is explicitly determined
- batch size is explicitly determined
- epoch count is explicitly determined

Suggested point split:

- configuration workflow: 10
- hidden-node setting: 5
- learning rate: 5
- batch size: 5
- epoch count: 5

Partial credit:

- award the relevant subpoints when the evidence is visible
- cap this category at `15` if the configuration workflow is claimed but not
  shown

Zero credit:

- no configuration or hyperparameter evidence is visible

Auto-checkable: keyword indicators for configuration, hidden nodes, learning
rate, batch size, epoch.

Manual-review needed: whether an alternative configuration workflow satisfies
the assignment intent.

## Technical Correctness: 30

Full credit:

- code appears to modify the HW4 model/training path
- configuration is actually connected to model/training behavior
- training and testing logic use MNIST train/test split correctly
- hyperparameter search/tuning is plausible, not only hard-coded output

Suggested point split:

- correct HW4 extension path: 8
- configuration connected to code: 8
- training/testing pipeline correctness: 8
- plausible hyperparameter search or tuning: 6

Partial credit:

- cap at `20` if code is structurally plausible but cannot be run or fully traced
- cap at `15` if the configuration exists but is not clearly used
- cap at `10` if code is mostly unrelated boilerplate with limited HW5-specific work

Zero credit:

- no relevant implementation
- implementation is unrelated to HW5

Auto-checkable: notebook/script presence and basic keyword evidence.

Manual-review needed: all correctness judgments.

## Result Quality: 15

Full credit:

- MNIST test accuracy is reported as at least `98%`
- the result is tied to the submitted code/configuration

Partial credit:

- `10`: accuracy is close to target but below `98%`
- `8`: result is reported but test/train distinction is unclear
- `5`: accuracy claim is present but weakly supported

Zero credit:

- no result evidence
- result is unrelated to MNIST test accuracy

Auto-checkable: visible accuracy/result indicators.

Manual-review needed: credibility of the result and whether a near-threshold
result deserves exception.

## Evidence and Auditability: 15

Full credit:

- Level A evidence: code + logs/outputs + result + traceable configuration
- deduction reasons can be tied to rubric items

Evidence caps:

- Level A: max `15`
- Level B: max `10`
- Level C: max `5`

Zero credit:

- no auditable evidence
- grader cannot connect score to submitted artifacts

Auto-checkable: evidence-level field exists in score CSV.

Manual-review needed: evidence level assignment.

## Standard Deduction Rules

- Missing code: apply `MISSING_REQUIRED_FILE`.
- Cannot verify the reported result: apply `CANNOT_VERIFY_RESULT`.
- Accuracy below `98%`: apply `ACCURACY_BELOW_TARGET`.
- No hyperparameter search/tuning evidence: apply
  `NO_HYPERPARAMETER_SEARCH_EVIDENCE`.
- Possible copying: apply `POSSIBLE_COPYING_MANUAL_REVIEW` and do not make an
  unsupported accusation.

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
