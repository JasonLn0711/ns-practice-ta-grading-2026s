# Final Release Gate Report

Generated: `2026-04-20T21:43:38+08:00`
Release ready: `no`

## Summary

- Passed checks: `9`
- Blocking checks: `4`
- Failed checks: `0`

## Checks

| Check | Status | Detail |
| --- | --- | --- |
| Required release files | `pass` | 19 files present |
| Compile scripts | `pass` | ok |
| Validate HW5 grading records | `pass` | Homework: hw5<br>Score rows: 21<br>Evidence rows: 21<br>Deduction rows: 39<br>Validation passed. |
| Validate HW6 dual grading records | `pass` | HW6 dual grading validation passed.<br>Code rows: 21<br>Figure rows: 21<br>Combined rows: 21<br>Code deductions: 32<br>Figure deductions: 26<br>Manual review rows: 0 |
| Git whitespace check | `pass` | ok |
| HW6 workbook copy | `pass` | output workbook exists and is ignored |
| Instructor packet | `pass` | 5 files present and ignored |
| Instructor recipient | `blocked` | recipient email not confirmed in outbox |
| Tracked private artifacts | `pass` | no tracked raw/renamed/extracted files |
| Git status | `pass` | working tree clean |
| Instructor decisions | `blocked` | 10 pending decisions |
| Confirmation email send event | `blocked` | no completed send event recorded |
| Late policy | `blocked` | late policy pending |

## Current Release Decision

Do not release grades yet. Resolve all `blocked` and `fail` checks first.

## Next Action

- If the instructor recipient is still blocked, confirm the address from E3, a prior course email, or the instructor directly.
- Once the recipient is confirmed, send `reports/instructor_confirmation_outbox.md` with only the sanitized packet files.
- After the instructor replies, use `reports/post_instructor_reply_runbook.md`.
- Re-run this script after recording the reply and applying any policy changes.
