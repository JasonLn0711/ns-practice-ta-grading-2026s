# HW6 Assignment Requirements

## Source Basis

This summary uses only the provided HW6 assignment file and related course
materials currently recorded in this workspace.

Primary visible source:

- `course_materials/hw6/renamed/hw6_course_homework06-assignment-spec.pdf`

Supporting context:

- `course_materials/hw6/renamed/hw6_course_lecture06-convolutional-neural-network.pdf`
- `course_materials/hw6/renamed/hw6_reference_01-cnn-mnist-batch.ipynb`
- `course_materials/hw6/renamed/hw6_reference_02-cnn-mnist-momentum.ipynb`

## Required Deliverables

HW6 requires students to:

- replace the fully connected layer with two more hidden layers
- draw a computational graph similar to slide 48
- use the notation in the graph to implement the code
- use mini-batch stochastic gradient with momentum
- train the model so MNIST test accuracy reaches at least `98%`
- plot learned filters
- plot intermediate feature maps for an arbitrary input digit

## Evidence Expected For Grading

The grading workspace should look for:

- code or notebook implementing the HW6 model
- visible architecture change from the prior fully connected layer structure
- computational graph evidence
- evidence that code notation corresponds to the graph
- momentum implementation, not just a comment mentioning momentum
- MNIST test accuracy output
- learned filter plot
- intermediate feature-map plot tied to an input digit

## TODO: Instructor Confirmation

- accepted computational graph format
- whether graph notation must exactly match slide 48
- accepted plot format: notebook output, image file, PDF, or screenshot
- whether graders must rerun code or only inspect submitted evidence
- whether external frameworks beyond lecture code are allowed
- how to score outputs generated from the wrong model or ambiguous code
