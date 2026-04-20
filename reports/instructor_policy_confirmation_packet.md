# Instructor Policy Confirmation Packet

Generated: `2026-04-20`
Prepared by: `Jason`
Scope: `HW5` and `HW6`

## Purpose

The HW5/HW6 grading records are complete under the current working rubric. Before
student-facing feedback or LMS score import, the instructor should confirm the
small set of policy decisions that can affect score release.

This packet is meant to be copy-pasteable for instructor review. It does not ask
the instructor to regrade every student; it asks for policy confirmation so any
score adjustment is targeted, consistent, and auditable.

## Current Status

| Homework | Graded rows | Average | Min | Max | Manual review holds |
| --- | ---: | ---: | ---: | ---: | ---: |
| HW5 | 21 | 90.76 | 63 | 100 | 0 |
| HW6 | 21 | 89.43 | 59 | 100 | 0 |

Validation already passed:

```bash
python3 scripts/validate_grading_records.py --homework hw5
python3 scripts/validate_grading_records.py --homework hw6
python3 -m py_compile scripts/*.py
```

## Current TA Grading Policy Used

- Scores are based on submitted evidence, not unsupported claims.
- Accuracy alone does not override missing development, architecture, graph, or visualization evidence.
- Missing or unverifiable required items do not receive full credit.
- Every non-full score has a written deduction reason.
- Per-student grading notes, evidence rows, deduction logs, and score rows are kept for audit.
- Suspicious copying would be marked for manual review rather than treated as automatic guilt; no manual review holds are currently recorded.

## Decisions Requested

### HW5

1. Should HW5 grading be based on submitted evidence only, or should TAs rerun notebooks before release?
   - Current TA treatment: submitted evidence was inspected; notebooks were not rerun.
   - Default if approved: keep current evidence-based scores.

2. Should a student who reaches `98%` accuracy but has weak or missing hyperparameter-search evidence receive full requirement/evidence credit?
   - Current TA treatment: no; accuracy does not erase missing development evidence.
   - Default if approved: keep `NO_HYPERPARAMETER_SEARCH_EVIDENCE` and `WEAK_AUDIT_EVIDENCE` deductions.

3. How strict should the course be when the official MNIST test set is tuned on, split, or partially used as validation data?
   - Current TA treatment: apply `TEST_PIPELINE_UNCLEAR` deductions, not automatic zero and not a release hold.
   - Default if approved: keep current technical/evidence deductions.

4. Which evidence formats are acceptable for HW5 full credit?
   - Possible formats: notebook outputs, code/script outputs, PDF report, screenshots, or combinations.
   - Current TA treatment: accepted retained notebook/script/report evidence when it was traceable.

5. Is any late-policy adjustment required before LMS import?
   - Current TA treatment: no late penalty has been applied in the score CSVs.

### HW6

1. What computational graph formats should receive full graph credit?
   - Current TA treatment: separate image/PDF graphs and rendered notebook graphs receive full graph credit when aligned with code; text-only source cells or code comments receive partial credit; missing graph artifacts receive zero graph credit.
   - Default if approved: keep current graph scores.

2. Does "replace the fully connected layer with 2 more hidden layers" mean three hidden fully connected layers total after convolution/pooling, or two hidden layers total?
   - Current TA treatment: three hidden fully connected layers total after convolution/pooling.
   - Default if approved: keep current architecture scores.

3. Should PyTorch implementations receive full credit when they satisfy architecture, momentum, graph, result, and visualization evidence?
   - Current TA treatment: yes.
   - Default if approved: keep current scores.

4. Should dense non-CNN submissions receive full HW6 architecture/filter/feature-map credit if they reach `98%` accuracy?
   - Current TA treatment: no; dense non-CNN work receives result/training/evidence credit where supported, but not full CNN architecture/filter/feature-map credit.
   - Default if approved: keep current architecture/visualization deductions.

5. Is any late-policy adjustment required before LMS import?
   - Current TA treatment: no late penalty has been applied in the score CSVs.

## Policy-Sensitive Rows

Adjust only these rows if the instructor changes policy. Otherwise leave the
current scores unchanged for consistency.

| Homework | Student ID | Current score | Policy-sensitive issue |
| --- | --- | ---: | --- |
| HW6 | 314264011 | 97 | two hidden layers total; graph otherwise complete |
| HW6 | 314351006 | 87 | graph/code hidden-layer mismatch |
| HW6 | 314264024 | 96 | text-only graph notation in notebook source |
| HW6 | 514661019 | 96 | graph notation in code comments only |
| HW6 | 314264029 | 83 | dense non-CNN implementation |
| HW5 | see deduction log | varies | weak/missing hyperparameter-search evidence |
| HW5 | see deduction log | varies | ambiguous MNIST test/development pipeline |

Detailed evidence is in:

- `grading/hw5/deduction_log.csv`
- `grading/hw6/deduction_log.csv`
- `grading/hw5/student_notes/`
- `grading/hw6/student_notes/`

## Recommended Instructor Reply Format

The fastest useful instructor reply would be:

```text
I approve the current TA grading policy for HW5/HW6 as described, with these changes:

HW5:
- rerun notebooks? yes/no
- weak hyperparameter-search evidence: keep deductions / adjust
- MNIST test-pipeline ambiguity: keep deductions / adjust
- accepted evidence formats:
- late policy:

HW6:
- accepted graph formats:
- hidden-layer interpretation:
- PyTorch accepted for full credit? yes/no
- dense non-CNN treatment:
- late policy:
```

## Release Workflow After Instructor Confirmation

1. Record the instructor decision in `reports/release_decision_log.md`.
2. If policy is unchanged, freeze the score CSVs.
3. If policy changes, adjust only affected rows and record the reason in the relevant student note and deduction log.
4. Re-run:

```bash
python3 scripts/validate_grading_records.py --homework hw5
python3 scripts/validate_grading_records.py --homework hw6
python3 scripts/summarize_scores.py --homework hw5
python3 scripts/summarize_scores.py --homework hw6
```

5. Generate student-facing feedback only after policy confirmation:

```bash
python3 scripts/generate_student_feedback.py --homework hw5 --apply
python3 scripts/generate_student_feedback.py --homework hw6 --apply
```

6. Commit the final release state in the private grading repo.
