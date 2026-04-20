# Remote Setup

This standalone TA grading repo is local-only by default.

Do not push student IDs, grades, grading notes, or reports to a public remote.
If a remote is needed later, create a private repository first and confirm access
with the instructor or course owner.

## Future Private Remote Commands

```bash
git remote add origin <private-remote-url>
git remote -v
git push -u origin main
```

Before pushing:

- confirm the remote is private
- confirm raw submissions and bulky course binaries are still ignored
- confirm the score CSVs, student maps, and grading notes are intended to be
  versioned in that private repo
- run `git status --short --ignored`
- run `git diff --check`
