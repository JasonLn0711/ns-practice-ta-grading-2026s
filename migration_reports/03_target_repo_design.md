# Target Repo Design

Source: `/home/jnclaw/every_on_git_jnclaw/planning-everything-track/ns-practice-ta-grading-2026s`

Target: `/home/jnclaw/every_on_git_jnclaw/ns-practice-ta-grading-2026s`

## Design Choice

The migration keeps the existing grading repo structure. It does not add root
`scores/`, `feedback/`, or `review_notes/` folders because `grading/hw5/` and
`grading/hw6/` already separate scores, feedback, review notes, evidence, and
deduction logs by homework.

## Canonical Areas

- `docs/`: grading policy, evidence levels, rubrics, assignment requirements.
- `grading/hw5/` and `grading/hw6/`: versioned scores, evidence, deduction logs,
  and per-student notes.
- `submissions/<hw>/`: raw, renamed, and extracted student submissions; bulky
  files remain ignored while mapping CSVs are versioned.
- `course_materials/<hw>/`: assignment/reference metadata is versioned; bulky
  raw/renamed course files remain ignored.
- `scripts/`: safe helpers for grading and migration.
- `migration_reports/`: migration inventory, mapping, link scan, and verification
  records.

## Privacy Boundary

The standalone repo is private. Audit metadata is versioned for traceability;
raw submissions and bulky course binaries stay out of Git to reduce exposure
risk.
