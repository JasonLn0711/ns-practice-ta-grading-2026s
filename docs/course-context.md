# Course Context

## Identity

- Course: `BEBN20024` Deep Learning / PyTorch, 2026 Spring.
- Lecturer: Prof. Wu Yude.
- Jason's role: teaching assistant and class attendee.
- Current grading mission: `HW5(1)` and `HW6(2) 畫圖 + code`.

## File Inspection Summary

Source inspected: `/home/jnclaw/Downloads/TA-deep-learning/`

| File or folder | Type | Likely meaning | Naming issue |
| --- | --- | --- | --- |
| `Homework 5 .pdf` | PDF, 1 page | HW5 assignment specification | Space before `.pdf`; generic title |
| `Homework 4 .pdf` | PDF, 1 page | HW4 assignment specification; prerequisite/context because HW5 asks students to modify HW4 code | Space before `.pdf`; generic title |
| `Homework 6 .pdf` | PDF, 2 pages | HW6 assignment specification | Space before `.pdf`; generic title |
| `05_Training of Multi-Layer Neural Network.pdf` | PDF slides, 79 pages | Lecture 5 reference slides for multi-layer neural networks and backpropagation | Spaces and title-case mixed with underscore prefix |
| `06_Convolutional Neural Network_final.pdf` | PDF slides, 73 pages | Lecture 6 reference slides for CNN, computational graph, filters, and feature maps | Spaces and title-case mixed with underscore prefix |
| `Lecture 5_Multi_layer neural network_Backprop.rar` | RAR archive | Lecture 5 notebooks and small data files | Spaces, mixed underscores, long descriptive name |
| `Lecture 5_Multi_layer neural network_Backprop/` | extracted folder | Extracted version of Lecture 5 archive | Existing extracted folder outside workspace |
| `Lecture 6_CNN_MINST/` | extracted folder | Lecture 6 CNN notebook folder | `MINST` appears to be a typo for `MNIST`; existing extracted folder outside workspace |
| `01_CNN_MNIST_batch.ipynb` | Jupyter notebook, 29 code cells | Lecture 6 reference notebook for CNN MNIST mini-batch workflow | Uppercase acronym style; copied under HW6 reference naming |
| `02_CNN_MNIST_momentum.ipynb` | Jupyter notebook, 26 code cells | Lecture 6 reference notebook for CNN MNIST with momentum | Uppercase acronym style; copied under HW6 reference naming |
| `data.rar` | RAR archive | Shared datasets, including MNIST and CIFAR-10 | Generic name; large archive |
| `data/` | extracted folder | Extracted dataset folder | Existing extracted folder outside workspace |
| `Lecture 3_4_Single-layer neural network.rar` | RAR archive | Earlier lecture reference material, likely HW4 context | Not directly HW5 unless rubric needs HW4 comparison |
| `Lecture 3_4_Single-layer neural network/` | extracted folder | Extracted earlier lecture archive | Not directly copied into HW5 workspace |
| `data/mnist/*.gz` | gzip IDX files | MNIST training/test image and label files for HW5/HW6-style accuracy checks | Canonical MNIST names; copied into an HW5 `mnist/` subgroup |

## HW5 Course-Material Placement

The explicit HW5-related attachments are now copied under:

- `course_materials/hw5/raw/`
- `course_materials/hw5/renamed/`

They are intentionally not stored under `submissions/hw5/`, because they are course/reference files rather than student submissions.

The mapping is tracked in `course_materials/hw5/rename_map.csv`.

The MNIST files are verified in `course_materials/hw5/mnist-verification.md`.

## HW6 Course-Material Placement

The explicit HW6-related attachments are now copied under:

- `course_materials/hw6/raw/`
- `course_materials/hw6/renamed/`

They are intentionally not stored under `submissions/hw6/`, because they are
course/reference files rather than student submissions.

The mapping is tracked in `course_materials/hw6/rename_map.csv`.

## E3 Submission Export Placement

E3 submission-page PDFs and ZIP exports belong in `submissions/<hw>/raw/`.

The flattened renamed working files belong in `submissions/<hw>/renamed/`.

For actual student submissions, keep these maps private and ignored by Git:

- `submissions/<hw>/rename_map.csv`
- `submissions/<hw>/student_file_map.csv`

The `student_file_map.csv` table is the answer to the operational question:
yes, each homework should have a private mapping table from submitted file names
to student IDs.

HW6 assignment/reference material is stored under `course_materials/hw6/`;
student-submission exports are stored separately under `submissions/hw6/`.

As of 2026-04-20, HW5/HW6 E3 ZIP/PDF exports have been imported locally.
The identity-bearing submission maps and renamed/extracted student files are
private workspace files and are ignored by Git.

## HW5 Assignment Facts Visible From Current Files

From `Homework 5 .pdf`:

- Modify Homework 4 code.
- Add the `configuration` function from `05_development.ipynb`.
- Determine hyperparameters:
  - number of hidden nodes for each hidden layer
  - learning rate
  - batch size
  - epoch
- Target: MNIST test accuracy at least `98%`.
- Deadline shown in the file: `2026/03/23 3:30pm`.

## HW6 Assignment Facts Visible From Current Files

From `Homework 6 .pdf`:

- Replace a fully connected layer with two more hidden layers.
- Draw the computational graph similar to slide 48 and use its notations in code.
- Use mini-batch stochastic gradient with momentum.
- Target: MNIST test accuracy at least `98%`.
- Plot learned filters and intermediate feature maps for an arbitrary input digit.
- Deadline shown in the file: `2026/03/30 3:30pm`.

## Current Naming Pattern

Imported course/reference material uses:

```text
hw5_course_<short-description>.<ext>
hw6_course_<short-description>.<ext>
hw5_reference_<short-description>.<ext>
hw6_reference_<short-description>.<ext>
```

Student submissions should use:

```text
hw5_<studentID>_<name>_<originalShortName>.<ext>
hw6_<studentID>_<name>_<originalShortName>.<ext>
```

If identity cannot be inferred:

```text
hw5_unknown_<index>_<originalShortName>.<ext>
hw6_unknown_<index>_<originalShortName>.<ext>
```

For E3 ZIP exports, use the import script's generated pattern:

```text
hw5_<studentID>_<sequence>_<originalShortName>.<ext>
hw6_<studentID>_<sequence>_<originalShortName>.<ext>
```

## Privacy Boundary

- Do not copy student names, IDs, grades, or review notes into random planning notes.
- Keep raw files, extracted archives, feedback, review notes, and score sheets local/private by default.
- If a policy decision matters later, summarize the decision without exposing unnecessary student details.
