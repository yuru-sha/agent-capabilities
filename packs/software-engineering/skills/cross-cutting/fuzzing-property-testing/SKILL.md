---
name: fuzzing-property-testing
description: "Use when parsers, serializers, protocol boundaries, state machines, or complex invariants need fuzzing or property-based tests across languages."
---

# Fuzzing and Property Testing

Compose with the language-specific testing or fuzzing skill and the global
`$tdd` skill. This skill chooses the test shape; it does not replace a
language's runner.

## Rules

- Choose examples, properties, stateful models, or fuzzing based on the failure mode and the smallest public seam.
- Define an independent invariant or reference model; do not merely restate the implementation.
- Bound input size, execution time, state growth, and external effects so CI remains deterministic.
- Preserve seeds and minimized reproducers, make failures runnable as ordinary regression tests, and review shrinking for false simplification.
- Cover malformed, boundary, adversarial, and mixed-version inputs while keeping secrets and production data out of corpora.

