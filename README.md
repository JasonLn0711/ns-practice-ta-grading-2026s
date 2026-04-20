# NS Practice TA Grading 2026 Spring

Private, auditable workspace for Jason's TA grading work.

## Purpose

This workspace keeps TA grading simple:

- preserve raw files
- rename working copies consistently
- separate objective checks from manual grading
- keep rubrics, policies, feedback tags, and exceptions in one place
- reduce repeated work for `HW5` and `HW6`

## What Goes Where

| Need | Location |
| --- | --- |
| Raw files exactly as received | `submissions/<hw>/raw/` |
| Renamed working copies | `submissions/<hw>/renamed/` |
| Extracted archives or notebooks | `submissions/<hw>/extracted/` |
| Course/reference materials | `course_materials/<hw>/` |
| Score sheet | `grading/<hw>/scores.csv` |
| Short feedback files | `grading/<hw>/feedback/` |
| Private review notes / exceptions | `grading/<hw>/review_notes/` |
| Rubrics and policies | `docs/` |
| Reusable feedback forms | `templates/` |
| Repeatable helper commands | `scripts/` |
| TA attendance and weekly work logs | `ta_notes/` |

## Current Imported Course Materials

The current HW5-related batch came from `~/Downloads/TA-deep-learning/` and is stored under `course_materials/hw5/`.

- `Homework 5 .pdf` appears to be the HW5 assignment specification.
- `Homework 4 .pdf` appears to be prerequisite/context because HW5 asks students to modify HW4 code.
- `05_Training of Multi-Layer Neural Network.pdf` appears to be Lecture 5 reference slides.
- `01_perceptron_classifier.ipynb` through `06_drop_out.ipynb` are Lecture 5 reference notebooks.
- `linearly_separable.txt`, `circles.txt`, and `non_linearly_separable.txt` are small lecture datasets.
- `data/mnist/*.gz` are verified MNIST IDX gzip files for training/test data.

The current HW6-related batch came from `~/Downloads/TA-deep-learning/` and is stored under `course_materials/hw6/`.

- `Homework 6 .pdf` is stored under `course_materials/hw6/` as the HW6 assignment spec.
- `06_Convolutional Neural Network_final.pdf` appears to be Lecture 6 CNN slides.
- `01_CNN_MNIST_batch.ipynb` and `02_CNN_MNIST_momentum.ipynb` are Lecture 6 CNN MNIST reference notebooks.

The raw files are copied locally and ignored by Git. The original Downloads files were not modified.

## Privacy / Git Boundary

The scaffold, rubrics, scripts, policy docs, templates, and course-material rename maps are safe to version.

The following are local/private by default and ignored by Git:

- raw files
- renamed working copies
- extracted archives
- `submissions/<hw>/rename_map.csv`
- `submissions/<hw>/student_file_map.csv`
- feedback files
- review notes
- `grading/<hw>/scores.csv`
- `course_materials/<hw>/raw/`
- `course_materials/<hw>/renamed/`

## Naming Rule

For manually organized student submissions:

```text
hw5_<studentID>_<name>_<originalShortName>.<ext>
hw6_<studentID>_<name>_<originalShortName>.<ext>
```

If student identity cannot be inferred:

```text
hw5_unknown_<index>_<originalShortName>.<ext>
hw6_unknown_<index>_<originalShortName>.<ext>
```

For E3 ZIP exports, the import script uses a privacy-preserving working pattern:

```text
hw5_<studentID>_<sequence>_<originalShortName>.<ext>
hw6_<studentID>_<sequence>_<originalShortName>.<ext>
```

For course/reference material, use:

```text
hw5_course_<short-description>.<ext>
hw6_course_<short-description>.<ext>
hw5_reference_<short-description>.<ext>
hw6_reference_<short-description>.<ext>
```

Every submission rename should be recorded in `submissions/<hw>/rename_map.csv`.
Every course-material rename should be recorded in `course_materials/<hw>/rename_map.csv`.

For E3 ZIP exports, also keep a private identity map:

```text
submissions/<hw>/student_file_map.csv
```

This maps each submitted file to the inferred student ID and should not be committed.

## Grading Workflow

1. Put files in `submissions/<hw>/raw/`.
2. Run the rename script in dry-run mode:

```bash
python3 scripts/rename_submissions.py --homework hw5
```

3. If the plan looks right, apply it:

```bash
python3 scripts/rename_submissions.py --homework hw5 --apply
```

4. Unpack archives only when needed:

```bash
python3 scripts/unpack_archives.py --homework hw5
python3 scripts/unpack_archives.py --homework hw5 --apply
```

5. For E3 ZIP exports, import and rename submitted files:

```bash
python3 scripts/import_e3_submissions.py --homework hw5 --archive /path/to/e3.zip --e3-pdf /path/to/e3.pdf
python3 scripts/import_e3_submissions.py --homework hw5 --archive /path/to/e3.zip --e3-pdf /path/to/e3.pdf --snapshot-date 20260420 --apply
```

6. Run objective required-file checks:

```bash
python3 scripts/check_required_files.py --homework hw5 --submission-dir submissions/hw5/extracted/<student-folder>
```

7. Grade with the rubric, then fill `grading/<hw>/scores.csv`.
8. Use feedback tags first, then add short personalized notes only where useful.
9. Log exceptions or ambiguous cases once in `grading/<hw>/review_notes/`.
10. Before releasing scores, run:

```bash
python3 scripts/summarize_scores.py --homework hw5
```

## Manual Judgment

Scripts can check file presence, naming, extraction, and score summaries.

Humans must judge:

- whether the implementation actually meets the assignment
- whether reported accuracy is reproducible
- whether hyperparameter tuning is reasonable
- whether plots/graphs match the requested model
- whether partial credit is fair
- whether suspicious similarity needs escalation

## Before Releasing Scores

- Confirm the rubric version is final.
- Confirm any late policy with the instructor.
- Review all `manual_review_needed=yes` rows.
- Check that no student received a custom standard.
- Ensure every major deduction has a feedback tag or note.
- Do not publish raw review notes unless intended.
