# Link Preservation Strategy

Canonical standalone repo: `/home/jnclaw/every_on_git_jnclaw/ns-practice-ta-grading-2026s`

## Stub Strategy

Create a small `README.md` at the old nested path and short stubs for legacy
rubric filenames. The stubs explain that the canonical grading workspace moved,
include the migration date, and point to the new sibling repo.

## Rewrite Strategy

Rewrite only high-confidence references in parent Markdown files. The current
scan found references in the project note and the 2026-04-20 daily note. Code
block references and ambiguous text are reported, not changed.

## Compatibility Rule

The parent planning repo remains usable even if an older note still points to
`ns-practice-ta-grading-2026s/`: the old path contains a redirect note, not
private grading data.
