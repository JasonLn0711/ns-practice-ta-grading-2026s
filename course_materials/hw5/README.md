# HW5 Course Materials

This folder stores course/reference material for HW5 grading.

These are not student submissions.

## Folder Use

- `raw/`: copies with original filenames, preserved for traceability.
- `renamed/`: consistent working names for grading reference.
- `rename_map.csv`: auditable mapping from original names to working names.

## Current Materials

- HW5 assignment spec.
- HW4 assignment spec, because HW5 says to modify HW4 code.
- Lecture 5 slides.
- Lecture 5 notebooks:
  - perceptron classifier
  - neural-network classifier
  - batching
  - testing
  - development/configuration
  - dropout
- Small lecture datasets for separability examples.
- MNIST IDX gzip dataset files used by HW5:
  - 60,000 training images and labels.
  - 10,000 test images and labels.
  - See `mnist-verification.md` for header/checksum verification.

## Naming Rule

Course/reference files use:

```text
hw5_course_<artifact>.ext
hw5_reference_<artifact>.ext
```

Actual student submissions should stay under `submissions/hw5/`.
