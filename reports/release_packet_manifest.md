# Release Packet Manifest

Generated: `2026-04-20`
Prepared by: `Jason`
Status: `ready for instructor confirmation / not ready for student release`

## Purpose

This manifest defines the exact files to use for the instructor release gate. It
keeps the next step clear: ask for policy confirmation first, then generate
student-facing feedback only after the instructor reply is recorded.

## Recommended Instructor Packet

Send or paste these first:

| File | Purpose | Include by default? |
| --- | --- | --- |
| `reports/instructor_email_draft.md` | Email body Jason can send or adapt. | yes |
| `reports/instructor_policy_confirmation_packet.md` | Detailed policy questions and current TA treatment. | yes |
| `reports/hw5_instructor_report.md` | HW5 summary, category averages, common deductions, policy issues. | yes |
| `reports/hw6_master_audit_report.md` | HW6 dual-score summary, category averages, common deductions, and workbook status. | yes |
| `reports/hw6_code_audit_report.md` | HW6(code) category averages and code deduction patterns. | yes |
| `reports/hw6_figure_audit_report.md` | HW6(圖) category averages and figure deduction patterns. | yes |

Keep these available but do not send unless requested:

| File or folder | Purpose | Reason not default |
| --- | --- | --- |
| `grading/hw5/scores.csv` | HW5 score rows. | contains student-level grading data |
| `grading/hw6/code_scores.csv` | HW6(code) score rows. | contains student-level grading data |
| `grading/hw6/figure_scores.csv` | HW6(圖) score rows. | contains student-level grading data |
| `grading/hw6/combined_summary.csv` | HW6 dual-score summary used for workbook write-back. | contains student-level grading data |
| `grading/hw5/deduction_log.csv` | HW5 deduction evidence. | detailed audit evidence |
| `grading/hw6/code_deduction_log.csv` | HW6(code) deduction evidence. | detailed audit evidence |
| `grading/hw6/figure_deduction_log.csv` | HW6(圖) deduction evidence. | detailed audit evidence |
| `grading/hw5/student_notes/` | HW5 per-student audit notes. | student-level detail |
| `grading/hw6/feedback/` | HW6 per-student dual-score audit notes. | student-level detail |

Do not send:

| Path pattern | Reason |
| --- | --- |
| `submissions/*/raw/` | raw private submissions |
| `submissions/*/renamed/` | renamed private submissions |
| `submissions/*/extracted/` | extracted private submissions |
| `course_materials/*/raw/` | bulky or source course files |
| `course_materials/*/renamed/` | local working copies of bulky materials |

## Current Release Gate Status

| Gate | Status | Evidence |
| --- | --- | --- |
| HW5 scores complete | done | `grading/hw5/scores.csv` has 21 rows |
| HW6 dual scores complete | done | `grading/hw6/code_scores.csv` and `grading/hw6/figure_scores.csv` each have 21 rows |
| HW5 validation | passed | `python3 scripts/validate_grading_records.py --homework hw5` |
| HW6 dual validation | passed | `python3 scripts/validate_hw6_dual_grading.py` |
| HW6 workbook write-back | done | `reports/hw6_workbook_writeback_report.md` |
| Instructor policy confirmation | pending | `reports/release_decision_log.md` |
| Late policy applied | pending | no late penalty applied yet |
| Student-facing feedback generated | blocked | wait for instructor confirmation |
| LMS import ready | blocked | wait for instructor confirmation and final feedback generation |

## Pre-Send Checklist

- [ ] Read `reports/instructor_email_draft.md`.
- [ ] Confirm recipient and course context.
- [ ] Decide whether to paste the policy packet into the email or attach it.
- [ ] Attach only summary/policy files unless the instructor asks for detailed student evidence.
- [ ] Do not attach raw submissions or extracted archives.
- [ ] After sending, write a dated note in `reports/release_decision_log.md`.

## After Instructor Reply

1. Record the reply in `reports/release_decision_log.md`.
2. If policy is unchanged, mark pending decisions as approved and freeze score CSVs.
3. If policy changes, adjust only affected rows listed in `reports/instructor_policy_confirmation_packet.md`.
4. Re-run validation:

```bash
python3 scripts/validate_grading_records.py --homework hw5
python3 scripts/validate_hw6_dual_grading.py
python3 scripts/build_hw6_dual_reports.py
```

5. Generate feedback only after policy confirmation:

```bash
python3 scripts/generate_student_feedback.py --homework hw5 --apply
# HW6 dual-score feedback already lives under grading/hw6/feedback/.
```

6. Commit the final release state before importing to LMS.
