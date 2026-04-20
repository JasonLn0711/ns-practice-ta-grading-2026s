# HW5 Rubric

## Purpose

Grade HW5 consistently and quickly while preserving fairness.

HW5 asks students to extend HW4 by adding a configuration workflow from `05_development.ipynb`, tune hyperparameters, and reach at least `98%` MNIST test accuracy.

## Required Submission Components

Visible from current assignment file:

- modified HW4 code or notebook
- configuration function / workflow
- chosen hidden-node setting for each hidden layer
- learning rate
- batch size
- epoch count
- MNIST test accuracy result

TODO instructor confirmation:

- expected submission format: notebook, `.py`, PDF report, screenshots, or all of these
- whether code execution is required during grading
- whether train/test loss plots are still required from HW4
- whether a fixed random seed is required
- whether students may use libraries beyond the lecture code

## Scoring Breakdown

Proposed `100` point structure until instructor confirms otherwise:

| Category | Points | What To Check |
| --- | ---: | --- |
| Completeness | 20 | Required files and stated hyperparameters are present |
| Correctness | 45 | Code implements the requested configuration/tuning workflow and reports valid MNIST test accuracy |
| Reproducibility | 15 | Results can be rerun or reasonably verified from submitted code/output |
| Clarity | 15 | The chosen configuration and result are easy to find and understand |
| Professional hygiene | 5 | File naming, organization, and no obvious broken paths or missing dependencies |

## Auto-Checkable Items

- submission file exists
- notebook or script exists
- readable archive if compressed
- filename can be mapped to one student
- visible mention of hidden nodes, learning rate, batch size, and epochs
- visible mention of MNIST test accuracy

## Manual-Review Items

- whether the configuration function is actually used
- whether the model and training loop match the assignment intent
- whether the `98%` accuracy claim is credible
- whether hyperparameter tuning is meaningful rather than hard-coded output
- whether code is understandable enough for grading

## Deduction Rules

- Missing submission or unreadable file: large deduction; mark manual review.
- Missing configuration/tuning workflow: deduct from correctness.
- Missing one hyperparameter report: deduct from completeness/clarity.
- Accuracy below `98%`: deduct from correctness, unless instructor grants exception.
- Result reported but not reproducible from code: deduct from reproducibility.
- Output is present but unclear: deduct from clarity.

## Zero-Score Conditions

Use only when clearly justified:

- no relevant submission
- file cannot be opened and no replacement is allowed
- submission is unrelated to HW5
- confirmed academic-integrity violation, after instructor decision

## Partial-Credit Guidelines

- Give credit for correct structure even if accuracy is below target.
- Give credit for a runnable implementation even if explanation is weak.
- Give credit for clear hyperparameter exploration even if final tuning is imperfect.
- Do not double-penalize the same root cause across every category.

## Edge Cases Requiring Instructor Confirmation

- code uses a deep-learning framework not covered by the assignment
- student submits only screenshots or only output without code
- accuracy slightly below `98%`
- late submission with no visible policy note
- corrupted archive after deadline
- suspected copied code

## Feedback Tags

- `missing-code`
- `missing-config`
- `missing-hyperparams`
- `accuracy-below-target`
- `not-reproducible`
- `unclear-result`
- `good-complete`
- `manual-review`
