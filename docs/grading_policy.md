# Grading Policy

## Purpose

This workspace supports rigorous, quantitative, auditable grading for HW5 and HW6.
The goal is not to reward writing style or confidence; the goal is to record what
requirements were fulfilled, what evidence supports that judgment, and what
deductions were applied.

## Grading Philosophy

- Grade requirement fulfillment, not presentation flair.
- Grade correctness, not confidence.
- Grade evidence, not claims.
- Grade reproducibility and auditability, not vague impression.
- Separate objective checks from manual judgment.
- Every non-full score must have a written deduction reason.
- Every score must be traceable to rubric items.
- If something cannot be verified, do not award full credit for it.
- Suspicious duplication is a manual-review flag, not an accusation.
- Consistency across students is more important than custom exceptions.

## Auditability Requirements

For each graded submission, record:

- score breakdown by rubric category
- evidence level: `A`, `B`, or `C`
- deduction tags and short deduction notes
- unresolved ambiguity, if any
- manual-review flag, if needed
- grader name and grading timestamp

The score CSV is the grading ledger. Per-student notes explain the evidence and
deductions behind the row. Instructor reports summarize patterns without
requiring the instructor to inspect every file.

## What Counts As Evidence

Strong evidence includes:

- submitted code or notebook
- visible model/training implementation
- output logs or notebook outputs
- reported MNIST test accuracy with enough context to verify
- visible hyperparameter configuration
- computational graph, filter plots, or feature maps when required
- file mappings from original submission names to working names

Weak evidence includes screenshots without code, claims without outputs, unclear
notebook outputs, or files that cannot be connected to the required task.

## Missing Files

- If a required file is missing, apply the relevant deduction tag.
- If the missing file prevents verifying a core requirement, cap the related
  rubric category at partial credit.
- If no relevant submission exists, use the zero-score condition and mark manual
  review if policy confirmation is needed.

## Code That Does Not Run

- Do not automatically give zero if the intent and output are reviewable.
- Deduct from evidence/reproducibility and the affected technical category.
- If the failure is due to missing dependencies, broken paths, or hidden local
  files, record the failure and mark manual review when the grading impact is
  ambiguous.

## Partial Completion

Award credit for independently verifiable parts. Do not double-penalize one root
cause across every category. Example: if the code is present but lacks credible
accuracy evidence, deduct in result quality and evidence, but still award code
structure points that can be verified.

## Unsupported Claims

A claim such as "accuracy reached 98%" is not full evidence by itself. Full result
credit requires code and output/log evidence that make the claim reasonably
traceable. Unsupported claims should receive `CANNOT_VERIFY_RESULT` or the
closest relevant deduction tag.

## Manual Review

Set `manual_review_needed=yes` when:

- academic-integrity concern exists
- file corruption or late-policy ambiguity affects score
- a nonstandard framework or format creates fairness uncertainty
- a required result is close to a threshold and the rule is unclear
- the TA cannot determine whether evidence satisfies the assignment

Manual review notes should state observable facts only and avoid unsupported
accusations.

## Recording Deductions

Use standardized deduction tags from the HW-specific deduction dictionary. Each
deduction entry should include:

- tag
- affected rubric category
- point impact
- concise evidence-based reason
- whether instructor confirmation is needed

## Consistency Across Students

- Use the same rubric version for all students in a homework.
- Apply the same deduction range for the same defect.
- If an exception is approved, record it once and apply it consistently.
- Keep attendance notes separate from grading notes.
- Do not store student-sensitive grading details in random planning notes.
