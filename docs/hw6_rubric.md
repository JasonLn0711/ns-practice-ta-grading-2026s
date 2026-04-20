# HW6 Rubric

## Purpose

Grade HW6 consistently while separating objective evidence from manual judgment.

HW6 asks students to replace a fully connected layer with two more hidden layers, draw a computational graph, use mini-batch stochastic gradient with momentum, reach at least `98%` MNIST test accuracy, and plot learned filters / intermediate feature maps.

Current supporting course materials are stored in `course_materials/hw6/`:
the HW6 assignment spec, Lecture 6 CNN slides, and the CNN MNIST batch/momentum notebooks.

## Required Submission Components

Visible from current assignment file:

- computational graph similar to slide 48
- code using graph notation
- model with two additional hidden layers replacing the fully connected layer
- mini-batch stochastic gradient with momentum
- MNIST test accuracy result at least `98%`
- learned filters plot
- intermediate feature-map plot for an arbitrary input digit

TODO instructor confirmation:

- expected drawing format
- expected code format
- whether plots may be screenshots, notebook outputs, or separate image files
- whether code execution is required during grading
- whether exact slide-48 notation is mandatory or approximate notation is acceptable

## Scoring Breakdown

Proposed `100` point structure until instructor confirms otherwise:

| Category | Points | What To Check |
| --- | ---: | --- |
| Completeness | 20 | Graph, code, accuracy, filters, and feature maps are present |
| Correctness | 40 | Architecture, training method, and momentum update match the assignment |
| Reproducibility | 15 | Code/output can be reasonably rerun or verified |
| Clarity | 15 | Graph notation, code structure, and plots are understandable |
| Visualization quality | 10 | Learned filters and feature maps are legible and tied to the chosen input |

## Auto-Checkable Items

- submission file exists
- notebook or script exists
- graph image/PDF/notebook output exists
- filter plot exists
- feature-map plot exists
- visible mention of momentum
- visible mention of MNIST test accuracy

## Manual-Review Items

- whether the graph matches the implemented code
- whether two extra hidden layers were added correctly
- whether mini-batch SGD with momentum is implemented, not merely mentioned
- whether the `98%` accuracy claim is credible
- whether plots are meaningful, not decorative

## Deduction Rules

- Missing computational graph: deduct from completeness and clarity.
- Graph and code notation do not match: deduct from correctness/clarity.
- Missing momentum: deduct from correctness.
- Missing learned-filter or feature-map plot: deduct from completeness/visualization.
- Accuracy below `98%`: deduct from correctness, unless instructor grants exception.
- Non-runnable code with no output evidence: deduct from reproducibility.

## Zero-Score Conditions

Use only when clearly justified:

- no relevant submission
- file cannot be opened and no replacement is allowed
- submission is unrelated to HW6
- confirmed academic-integrity violation, after instructor decision

## Partial-Credit Guidelines

- Give graph credit separately from code credit.
- Give visualization credit separately from accuracy credit.
- Give implementation credit even if final accuracy misses the target.
- Do not double-penalize the same missing file in every category.

## Edge Cases Requiring Instructor Confirmation

- graph exists but does not use slide-48 notation
- code uses a high-level framework instead of lecture-style implementation
- plots are present but generated from the wrong model
- accuracy slightly below `98%`
- late submission with no visible policy note
- suspected copied code

## Feedback Tags

- `missing-graph`
- `missing-code`
- `missing-momentum`
- `missing-filter-plot`
- `missing-feature-map`
- `accuracy-below-target`
- `not-reproducible`
- `unclear-notation`
- `good-complete`
- `manual-review`
