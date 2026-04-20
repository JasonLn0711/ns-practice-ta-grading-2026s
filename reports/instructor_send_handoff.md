# Instructor Send Handoff

Generated: `2026-04-20`
Prepared by: `Jason`
Status: `ready except recipient address`

## Purpose

This handoff is the next operational step after grading and packet generation.
The grading records are complete, but release is intentionally blocked until the
instructor confirms policy and late-policy handling.

## Current State

- HW5 grading records are complete and validated.
- HW6 has independent `HW6(code)` and `HW6(圖)` score records.
- The HW6 workbook write-back exists only as a separate ignored copy; the
  original workbook remains untouched.
- The sanitized instructor packet is ready at
  `release_packets/instructor_confirmation_2026-04-20/`.
- The syllabus confirms lecturer name `吳育德` but does not expose a reliable
  email address in the inspected local text.

## Immediate Next Action

1. Confirm the instructor recipient address from E3, a prior course email, or
   the instructor directly.
2. Open `reports/instructor_confirmation_outbox.md`.
3. Replace the recipient TODO with the confirmed address.
4. Paste the subject and body into the mail client.
5. Attach only the sanitized files from
   `release_packets/instructor_confirmation_2026-04-20/`, or paste the policy
   packet inline.
6. Confirm no raw submissions, extracted archives, per-student notes, score CSVs,
   or workbook binaries are attached by default.
7. Send the email.
8. Record the send event in `reports/release_decision_log.md`.
9. Wait for the instructor reply before changing scores or releasing feedback.

## Default Files To Attach

- `instructor_policy_confirmation_packet.md`
- `hw5_instructor_report.md`
- `hw6_instructor_report.md`
- `hw6_master_audit_report.md`

## Do Not Attach By Default

- `submissions/*/raw/`
- `submissions/*/renamed/`
- `submissions/*/extracted/`
- `course_materials/*/raw/`
- `course_materials/*/renamed/`
- `grading/*/feedback/`
- `grading/*/student_notes/`
- `grading/*/*scores.csv`
- `grading/*/*deduction*.csv`

## Send Event Entry

After sending, paste and complete this entry in
`reports/release_decision_log.md`:

```text
Date sent:
Recipient:
Subject: BEBN20024 HW5/HW6 grading completed - policy confirmation needed before release
Files sent or pasted:
- release_packets/instructor_confirmation_2026-04-20/instructor_policy_confirmation_packet.md
- release_packets/instructor_confirmation_2026-04-20/hw5_instructor_report.md
- release_packets/instructor_confirmation_2026-04-20/hw6_instructor_report.md
- release_packets/instructor_confirmation_2026-04-20/hw6_master_audit_report.md
Pending decisions: HW5-D1 through HW5-D5, HW6-D1 through HW6-D5
Notes: Waiting for instructor policy confirmation before student-facing release or LMS import.
```

## Release Boundary

Do not generate final student-facing feedback, import the workbook, or mark the
release gate ready until:

- instructor recipient and send event are recorded;
- all instructor policy decisions are resolved;
- late policy is either applied or explicitly marked not applicable;
- `python3 scripts/check_release_gate.py --write` reports no blockers.
