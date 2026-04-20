# Migration README

This repo was migrated out of
`/home/jnclaw/every_on_git_jnclaw/planning-everything-track/` into a standalone
private grading repo.

## Why Separate It

The planning repo is Jason's personal operating system. The grading repo has a
different privacy and audit boundary: student submissions, student IDs, scores,
deduction logs, and manual review notes should live in a purpose-built private
workspace.

## Canonical Location

Canonical grading repo:

`/home/jnclaw/every_on_git_jnclaw/ns-practice-ta-grading-2026s`

The old nested path is retained only as a compatibility stub for older planning
links.

## Link Handling

Migration scripts scan parent Markdown references before rewriting anything.
Only high-confidence references are rewritten. Ambiguous mentions and code-block
paths are reported for review.

## Stubs And Redirects

Compatibility stubs at the old path say that the canonical file moved and point
to the new standalone repo. They are intentionally small and contain no private
grading data.

## How To Verify

From the standalone repo:

```bash
python3 scripts/migration_verify.py \
  --parent /home/jnclaw/every_on_git_jnclaw/planning-everything-track \
  --target /home/jnclaw/every_on_git_jnclaw/ns-practice-ta-grading-2026s \
  --mapping migration_reports/path_mapping.csv \
  --output migration_reports/07_verification_report.md \
  --write
```

Also run the grading workflow checks:

```bash
python3 scripts/validate_grading_records.py --homework hw5
python3 scripts/validate_grading_records.py --homework hw6
```

## Manual Follow-Up

- Add a private remote only after confirming access and privacy settings.
- Review ambiguous Markdown references listed in
  `migration_reports/markdown_reference_index.csv`.
- Keep the timestamped backup until the migration has been reviewed.
