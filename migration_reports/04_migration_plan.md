# Migration Plan

## Strategy

1. Copy `/home/jnclaw/every_on_git_jnclaw/planning-everything-track/ns-practice-ta-grading-2026s` to `/home/jnclaw/every_on_git_jnclaw/ns-practice-ta-grading-2026s` including `.git` and ignored local files.
2. Verify file counts, SHA-256 digests, Git history, and ignored-file policy.
3. Rename the old nested directory to a timestamped local backup.
4. Create small compatibility stubs at the old path.
5. Rewrite only high-confidence parent Markdown references.
6. Commit standalone repo changes and parent compatibility changes separately.

## File Classification

- Move/copy directly: docs, scripts, templates, reports, README files.
- Copy first, verify later: raw submissions, renamed binaries, extracted
  archives, bulky course materials.
- Leave stub or redirect note: old root README and common rubric paths.
- Leave in place for now: timestamped backup until Jason confirms cleanup.
- Ignore/exclude from version control: raw, renamed, extracted, caches, bulky
  course binary folders.
- Manual review required: ambiguous prose mentions and code-block path mentions.

## Non-Destructive Rule

The scripts never delete the source by default. The old repo is renamed only
after the sibling copy passes verification.
