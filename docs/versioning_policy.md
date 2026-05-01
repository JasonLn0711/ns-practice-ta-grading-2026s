# Versioning Policy

This repository is private and auditable. It versions the records needed to
explain grading decisions while keeping bulky or high-exposure artifacts out of
Git.

## Versioned

- grading policies, rubrics, evidence levels, and deduction dictionaries
- assignment requirement notes
- scripts and templates
- score sheets, evidence sheets, and deduction logs
- per-student grading notes and manual review notes
- submission mapping CSVs
- audit reports and instructor reports
- migration reports and path mappings

## Not Versioned

- raw LMS/E3 exports
- renamed working copies of student submissions
- extracted submission archives
- bulky course-material binaries
- workbook binaries and scored workbook copies
- cache files and temporary build artifacts

## Rationale

Versioning scores, notes, maps, and reports supports auditability: every score
can be traced to evidence, rubric categories, and written deduction reasons.
Ignoring raw submissions and bulky binaries reduces accidental exposure and
keeps Git history reviewable.

## License And Access

See `../LICENSE`. This repository is an all-rights-reserved private grading
workspace. The license does not relicense student submissions, course materials,
workbook data, or institutional records. Do not publish or push this repository
unless the remote is confirmed private and authorized for course grading use.

## Operational Rule

Before committing, run:

```bash
git status --short --ignored
git ls-files | rg 'submissions/.*/(raw|renamed|extracted)|course_materials/.*/(raw|renamed)'
```

The second command should show only allowed `.gitkeep` files. If a raw
submission or bulky binary appears, stop and fix `.gitignore` before committing.
