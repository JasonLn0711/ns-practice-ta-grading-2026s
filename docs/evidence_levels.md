# Evidence Levels

Evidence level controls the maximum score available in evidence-related rubric
items. It does not replace technical grading.

## Level A

Code + logs + result outputs + traceable configuration.

Use Level A when the submission includes enough information to connect the model,
training settings, and reported result. Evidence and auditability may receive full
credit.

## Level B

Code + final results + partial logs.

Use Level B when the main implementation is visible and a final result is shown,
but the path from configuration to output is incomplete. Evidence and
auditability is capped at `10 / 15`.

## Level C

Incomplete or weak evidence.

Use Level C when evidence is mostly claims, screenshots, incomplete output, or
files that do not clearly connect code to results. Evidence and auditability is
capped at `5 / 15`.

## Unsupported Claims

Unsupported claims cannot receive full evidence credit. If a result cannot be
verified from code, logs, outputs, or traceable configuration, apply
`CANNOT_VERIFY_RESULT` or the closest HW-specific deduction tag.
