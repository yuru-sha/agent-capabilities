---
name: change-review
description: Use when reviewing a branch, pull request, implementation, or work-in-progress across language, database, or OpenAPI boundaries; composes the existing code-review skill with focused evidence checks.
---

# Change review adapter

Use the global `$code-review` skill for the fixed-point process and its separate
Standards/Spec reports. This skill supplies the cross-cutting coverage lens;
it is not a second diff-review workflow.

## Compose the review

1. Identify the primary language, database, and API contract in the diff.
2. Load only the matching adapter skills and the relevant agent role.
3. Keep Standards, Spec, security, database, and test findings distinguishable.
4. Cite the changed file/hunk and the repository rule, contract, or measured
   evidence that supports each finding.

## Coverage

- Boundary behavior: validation, errors, cancellation, cleanup, timeouts, and
  authorization.
- Compatibility: public API, serialized data, migrations, generated artifacts,
  and mixed-version behavior.
- Operations: logs, metrics/traces, configuration, resource limits, and
  recoverability.
- Tests: public seams, independent expected values, failure paths, and
  deterministic fixtures.

## Findings

Report missing requirements, wrong behavior, scope creep, and evidence limits
separately. Treat a green formatter, linter, or unit test command as tooling
evidence only; it does not prove semantic or security correctness.

