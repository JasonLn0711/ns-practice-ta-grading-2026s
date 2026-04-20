# HW6 Rubric

Total score: `100`.

HW6 asks students to replace a fully connected layer with two more hidden layers,
draw a computational graph similar to slide 48, use that notation in code, train
with mini-batch stochastic gradient with momentum, reach at least `98%` MNIST
test accuracy, and plot learned filters plus intermediate feature maps.

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

Full credit:

- relevant HW6 submission is present
- code or notebook is present
- computational graph evidence is present
- result evidence is present
- visualization evidence is present
- submission can be mapped to one student

Partial credit:

- `7`: one required artifact is hard to locate but likely present
- `4`: code present but graph or visualization evidence is missing
- `2`: only screenshots/report fragments are present

Zero credit:

- no relevant HW6 submission
- file cannot be opened and no replacement is allowed

Auto-checkable: file existence, file type, archive readability, student map.

Manual-review needed: whether embedded notebook output is enough for graph or
visualization evidence.

## Architecture Modification Correctness: 15

Full credit:

- the fully connected layer replacement is visible
- two additional hidden layers are implemented
- layer dimensions/flow are internally consistent

Partial credit:

- `10`: architecture is mostly correct but dimensions/flow are unclear
- `7`: extra layers exist but the replacement requirement is ambiguous
- `4`: code contains model changes but not the requested architecture

Zero credit:

- no architecture modification evidence

Auto-checkable: basic code/notebook presence.

Manual-review needed: all architecture correctness decisions.

## Computational Graph Correctness: 15

Full credit:

- computational graph is present
- graph is similar to the required slide-48 style
- notation used in the graph is reflected in the code

Partial credit:

- `10`: graph present but code-notation link is incomplete
- `7`: graph present but too vague to verify fully
- `4`: graph-like image exists but is not clearly the model graph

Zero credit:

- no computational graph evidence

Auto-checkable: graph-named files or graph keywords.

Manual-review needed: graph correctness and notation alignment.

## Training Method Correctness: 20

Full credit:

- mini-batch stochastic gradient training is implemented
- momentum is implemented in the update, not merely mentioned
- training loop is connected to the HW6 model

Suggested point split:

- mini-batch training: 7
- momentum update: 8
- integration with model/training loop: 5

Partial credit:

- cap at `12` if momentum is mentioned but implementation is unclear
- cap at `10` if mini-batch training is visible but momentum is absent
- cap at `8` if training loop is not connected to the submitted model

Zero credit:

- no relevant training implementation

Auto-checkable: momentum and batch keyword indicators.

Manual-review needed: whether momentum is actually implemented.

## Result Quality: 10

Full credit:

- MNIST test accuracy is reported as at least `98%`
- result is tied to the submitted HW6 model

Partial credit:

- `7`: accuracy is close to target but below `98%`
- `5`: result is reported but train/test distinction is unclear
- `3`: unsupported accuracy claim only

Zero credit:

- no result evidence
- result is unrelated to MNIST test accuracy

Auto-checkable: visible accuracy/result indicators.

Manual-review needed: credibility and near-threshold cases.

## Visualization Requirements: 15

Full credit:

- learned filters are plotted
- intermediate feature maps are plotted
- feature-map plot is tied to an arbitrary input digit

Suggested point split:

- learned filter plot: 7
- feature-map plot: 7
- chosen input digit context: 1

Partial credit:

- award visible subpoints independently
- cap at `8` if plots are present but not tied to the implemented model

Zero credit:

- no relevant visualization evidence

Auto-checkable: filter/feature-map filenames or keywords.

Manual-review needed: whether plots are meaningful and linked to the model.

## Evidence and Auditability: 15

Full credit:

- Level A evidence: code + logs/outputs + result + traceable model/training
  configuration
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

- Missing graph: apply `COMPUTATIONAL_GRAPH_MISSING`.
- Momentum absent or unsupported: apply `MOMENTUM_NOT_IMPLEMENTED`.
- Missing learned filters: apply `FILTER_PLOT_MISSING`.
- Missing feature maps: apply `FEATURE_MAP_MISSING`.
- Cannot verify reported result: apply `CANNOT_VERIFY_RESULT`.
- Possible copying: apply `POSSIBLE_COPYING_MANUAL_REVIEW` and do not make an
  unsupported accusation.

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
