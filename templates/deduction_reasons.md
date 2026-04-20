# Deduction Reasons

Use this structure when writing non-full-score reasons.

```text
Tag: <STANDARD_DEDUCTION_TAG>
Category: <rubric category>
Points deducted: <number>
Evidence reviewed: <file/path/output>
Reason: <observable fact, not speculation>
Manual review needed: yes/no
Instructor confirmation needed: yes/no
```

## Examples

```text
Tag: CANNOT_VERIFY_RESULT
Category: Result quality
Points deducted: 8
Evidence reviewed: submitted notebook output cells
Reason: Accuracy is claimed, but no test output or log connects the value to the submitted code.
Manual review needed: no
Instructor confirmation needed: no
```

```text
Tag: POSSIBLE_COPYING_MANUAL_REVIEW
Category: Manual review
Points deducted: 0
Evidence reviewed: notebook code cells 4-12
Reason: Similarity requires instructor review; no academic-integrity conclusion made by TA.
Manual review needed: yes
Instructor confirmation needed: yes
```
