# Instructor Confirmation Send Checklist

Generated: `2026-04-20`
Prepared by: `Jason`
Status: `ready to send / not sent`

## Purpose

This checklist is the immediate next action before grade release. It turns the
release packet into a small, auditable send workflow: ask the instructor to
confirm policy, avoid exposing raw submissions, and record the reply before any
student-facing release.

## Send Objective

Ask the instructor to approve or revise the current HW5/HW6 grading policy.
Do not ask the instructor to regrade all students. Ask only for policy decisions
that could affect score release.

## Default Materials To Send

Use the local packet folder first:

```text
release_packets/instructor_confirmation_2026-04-20/
```

It contains copies of these approved summary/policy files:

| File | Use |
| --- | --- |
| `reports/instructor_email_draft.md` | outgoing email body |
| `reports/instructor_policy_confirmation_packet.md` | policy questions and current TA treatment |
| `reports/hw5_instructor_report.md` | HW5 summary for instructor review |
| `reports/hw6_instructor_report.md` | HW6 dual-score summary for instructor review |
| `reports/hw6_master_audit_report.md` | HW6 audit summary and workbook write-back status |

Keep these available only if the instructor asks for detailed evidence:

| File or folder | Use |
| --- | --- |
| `grading/hw5/scores.csv` | HW5 score rows |
| `grading/hw6/code_scores.csv` | HW6(code) score rows |
| `grading/hw6/figure_scores.csv` | HW6(圖) score rows |
| `grading/hw5/deduction_log.csv` | HW5 deduction evidence |
| `grading/hw6/code_deduction_log.csv` | HW6(code) deduction evidence |
| `grading/hw6/figure_deduction_log.csv` | HW6(圖) deduction evidence |
| `grading/hw5/student_notes/` | HW5 per-student audit notes |
| `grading/hw6/feedback/` | HW6 per-student audit notes |

Do not send raw/private artifacts unless the instructor explicitly requests them
through a secure channel:

| Path pattern | Reason |
| --- | --- |
| `submissions/*/raw/` | raw student submissions |
| `submissions/*/renamed/` | renamed student submissions |
| `submissions/*/extracted/` | extracted student submissions |
| `course_materials/*/raw/` | source course files and original workbook |
| `course_materials/*/renamed/` | local workbook/output copies |

## Pre-Send Steps

- [x] Confirm the instructor recipient address from E3, a prior course email, or
  the instructor directly. Gmail search found prior messages from `吳 (Wu)育德
  (Yu-Te) <ytwu@nycu.edu.tw>`, and the inspected E3 course announcement confirms
  the course lecturer context as `吳育德`.
- [x] Attempt Gmail connector draft creation. Result: blocked by
  `ACCESS_TOKEN_SCOPE_INSUFFICIENT`; no draft was created and no email was sent.
  Use Gmail web UI or another authorized mail client for the send step.
- [ ] Open `reports/instructor_confirmation_outbox.md`.
- [ ] If needed, compare it against `reports/instructor_email_draft.md`.
- [x] Confirm the recipient and course name.
- [ ] Paste the email body into the mail client.
- [ ] Attach files from `release_packets/instructor_confirmation_2026-04-20/`, or paste the policy packet inline.
- [ ] Verify the email includes these current summary numbers:
  - HW5: `21` graded rows, average `90.76`, manual reviews `0`
  - HW6(code): `21` graded rows, average `88.38`, manual reviews `0`
  - HW6(圖): `21` graded rows, average `78.38`, manual reviews `0`
  - HW6 workbook copy: `21` updated rows, `4` unchanged rows due missing reliable HW6 evidence
- [ ] Confirm the email asks for late-policy confirmation before release.
- [ ] Confirm no raw submissions, extracted archives, or workbook binaries are attached.
- [ ] Send the email.
- [ ] Record the send event in `reports/release_decision_log.md`.

## Send Event Log Template

Paste this into `reports/release_decision_log.md` after sending:

```text
Date sent:
Recipient:
Subject:
Files sent or pasted:
Pending decisions:
Notes:
```

## Instructor Reply Handling

### If The Instructor Approves Current Policy

1. Mark each pending decision in `reports/release_decision_log.md` as approved.
2. Record the instructor/source and date.
3. Re-run validation:

```bash
python3 scripts/validate_grading_records.py --homework hw5
python3 scripts/validate_hw6_dual_grading.py
python3 scripts/build_hw6_dual_reports.py
python3 -m py_compile scripts/*.py
```

4. Generate final HW5 student-facing feedback:

```bash
python3 scripts/generate_student_feedback.py --homework hw5 --apply
```

5. Keep HW6 feedback under `grading/hw6/feedback/`.
6. Commit the final release state.

### If The Instructor Changes Policy

1. Record the exact decision in `reports/release_decision_log.md`.
2. Adjust only the affected rows listed in
   `reports/instructor_policy_confirmation_packet.md`.
3. For every changed score, update:
   - score CSV row
   - deduction log or adjustment note
   - per-student grading note
   - relevant report summary
4. Re-run validation before release.
5. Commit the policy-adjusted release state separately.

### If The Instructor Requests Detailed Evidence

Send the smallest sufficient evidence set. Prefer score CSVs and deduction logs
before per-student notes. Avoid raw submissions unless the instructor explicitly
asks for them and the channel is appropriate.

## Release Blockers Still Open

- Instructor policy confirmation is pending.
- Late policy is pending.
- Instructor recipient email is not recorded in this repo.
- Student-facing release should not happen until the instructor reply is logged.
- Any policy change must be traceable in score rows, deduction notes, and commit history.
