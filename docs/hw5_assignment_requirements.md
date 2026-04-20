# HW5 Assignment Requirements

## Source Basis

This summary uses only the provided HW5 assignment file and related course
materials currently recorded in this workspace.

Primary visible source:

- `course_materials/hw5/renamed/hw5_course_homework05-assignment-spec.pdf`

Supporting context:

- `course_materials/hw5/renamed/hw5_course_homework04-context-spec.pdf`
- `course_materials/hw5/renamed/hw5_reference_05-development-configuration.ipynb`
- `course_materials/hw5/mnist-verification.md`

## Required Deliverables

HW5 requires students to modify Homework 4 by adding the configuration function
from `05_development.ipynb`.

The configuration workflow must determine:

- number of hidden nodes for each hidden layer
- learning rate
- batch size
- epoch count

The submitted work must provide evidence that MNIST test accuracy reaches at
least `98%`.

## Evidence Expected For Grading

The grading workspace should look for:

- code or notebook derived from the HW4 workflow
- visible configuration function or equivalent configuration workflow
- explicit hyperparameter choices
- MNIST test accuracy output
- enough code/output context to decide whether the result is traceable

## TODO: Instructor Confirmation

- accepted submission format: notebook, Python script, PDF report, screenshots,
  or a combination
- whether graders must rerun code or only inspect submitted evidence
- whether a fixed random seed is required
- whether external libraries beyond lecture code are allowed
- whether HW4 plots or other HW4 deliverables still carry points in HW5
