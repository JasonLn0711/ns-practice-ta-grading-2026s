# Grading Release Readiness Review

Generated: `2026-04-20`
Grader: `Jason`
Scope: `HW5` and `HW6`

## Current Status

Both homework grading passes are complete from the grading-record side.

| Homework / score | Score rows | Evidence rows | Average | Manual reviews | Status |
| --- | ---: | ---: | ---: | ---: | --- |
| HW5 | 21 | 21 | 90.76 | 0 | ready for instructor policy review |
| HW6(code) | 21 | 21 | 88.90 | 0 | workbook copy written |
| HW6(figure) | 21 | 21 | 78.38 | 0 | workbook copy written |

Validation commands passed:

- `python3 scripts/validate_grading_records.py --homework hw5`
- `python3 scripts/validate_grading_records.py --homework hw6`
- `python3 scripts/validate_hw6_dual_grading.py`
- `python3 -m py_compile scripts/*.py`

## Release Gate

Do not release grades until these checks are complete:

- [ ] Instructor confirms policy questions below or explicitly accepts current rubric interpretation.
- [ ] Late policy is applied, if needed.
- [ ] Score CSVs are reviewed for obvious import formatting issues.
- [ ] Student-facing feedback is generated only after policy questions are resolved.
- [ ] Final release commit is made after any instructor-requested adjustment.

## Instructor Questions

### HW5

1. Should grading be based only on submitted evidence, or should TAs rerun notebooks before release?
2. Should students who reached `98%` accuracy but showed weak hyperparameter-search evidence keep the current configuration/evidence deductions?
3. How strict should the course be for students who tune on, split, or partially evaluate the official MNIST test set?
4. Which evidence formats are accepted for grading: notebook outputs, scripts, PDF reports, screenshots, or combinations?
5. Is there any late policy adjustment to apply before LMS import?

Current HW5 policy used in grading:

- Submitted evidence was inspected; notebooks were not rerun.
- Accuracy alone did not override missing development/hyperparameter evidence.
- Test-pipeline ambiguity received `TEST_PIPELINE_UNCLEAR`, not an automatic zero or manual hold.
- No academic-integrity manual reviews were opened.

### HW6

1. What computational graph formats should receive full credit?
2. Does "replace the fully connected layer with 2 more hidden layers" mean three hidden fully connected layers total after convolution/pooling, or two hidden layers total?
3. Should PyTorch implementations receive full credit when they satisfy architecture, momentum, graph, result, and visualization evidence?
4. Should a dense non-CNN implementation receive only partial HW6 architecture/filter/feature-map credit even if it reaches `98%` accuracy?
5. Is there any late policy adjustment to apply before LMS import?

Current HW6 policy used in grading:

- HW6 is now represented by two independent 100-point scores:
  `HW6(code)` and `HW6(figure)`.
- Separate image/PDF graphs and rendered notebook graphs received full graph credit when aligned with code.
- Text-only graph notation or code comments received partial graph credit.
- Missing graph artifacts received zero graph credit.
- PyTorch submissions received full credit when they satisfied the same evidence requirements.
- Dense non-CNN work received result/training/evidence credit but not full CNN architecture/filter/feature-map credit.

## Potential Score-Adjustment Targets

Only adjust these if the instructor changes policy. Otherwise leave the current scores unchanged for consistency.

### HW5 Policy-Sensitive Patterns

| Pattern | Current treatment | Affected evidence |
| --- | --- | --- |
| Weak or missing hyperparameter-search evidence | `NO_HYPERPARAMETER_SEARCH_EVIDENCE` / evidence deductions | see `grading/hw5/deduction_log.csv` |
| Test-pipeline ambiguity or official test-set development | `TEST_PIPELINE_UNCLEAR` technical/evidence deductions | see `grading/hw5/deduction_log.csv` |
| Near-target accuracy below `98%` | proportional result deduction | see `ACCURACY_BELOW_TARGET` rows |

### HW6 Policy-Sensitive Students

| Student ID | Current issue | HW6(code) | HW6(figure) | Possible policy decision |
| --- | --- | ---: | ---: | --- |
| 314264011 | two hidden layers total; graph otherwise complete | 97 | 100 | add code architecture credit if instructor accepts two hidden layers total |
| 314351006 | graph/code hidden-layer mismatch | 86 | 80 | adjust only if instructor accepts code architecture and graph mismatch policy |
| 314264024 | text-only graph notation in notebook source | 97 | 85 | add figure graph/explainability credit if text-only graph format is accepted |
| 514661019 | graph notation in code comments only | 98 | 85 | add figure graph/explainability credit if source-comment graph format is accepted |
| 314264029 | dense non-CNN implementation | 80 | 52 | adjust only if instructor accepts non-CNN replacement for HW6 |

## Files To Review Before Release

- `reports/instructor_email_draft.md`
- `reports/release_packet_manifest.md`
- `reports/instructor_policy_confirmation_packet.md`
- `reports/release_decision_log.md`
- `reports/hw5_instructor_report.md`
- `reports/hw6_instructor_report.md`
- `reports/hw6_code_audit_report.md`
- `reports/hw6_figure_audit_report.md`
- `reports/hw6_master_audit_report.md`
- `reports/hw6_workbook_writeback_report.md`
- `grading/hw5/scores.csv`
- `grading/hw6/scores.csv`
- `grading/hw6/code_scores.csv`
- `grading/hw6/figure_scores.csv`
- `grading/hw6/combined_summary.csv`
- `grading/hw5/deduction_log.csv`
- `grading/hw6/deduction_log.csv`
- `grading/hw6/code_deduction_log.csv`
- `grading/hw6/figure_deduction_log.csv`

## Recommended Next Action

Use `reports/instructor_email_draft.md` as the outgoing message and
`reports/release_packet_manifest.md` as the attachment checklist. Send
`reports/instructor_policy_confirmation_packet.md` to the instructor, with the
two instructor reports available as supporting attachments. Record the reply in
`reports/release_decision_log.md`. If the instructor accepts the current policy,
freeze the score CSVs and generate student-facing feedback. If the instructor
changes policy, adjust only the targeted rows listed above and record the change
in a new commit.
