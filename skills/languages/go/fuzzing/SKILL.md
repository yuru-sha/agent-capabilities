---
name: go-fuzzing
description: "Use when Go parsers, decoders, protocol handlers, or serialization boundaries need fuzz tests or corpus-driven robustness checks."
---

# Go Fuzzing

Use the standard `testing.F` fuzzing model and compose with the global `$tdd`
skill. Keep the target narrow and its invariant explicit.

## Rules

- Fuzz the smallest public or package seam that can expose malformed input, panics, hangs, state corruption, or non-termination.
- Define properties independently of the implementation, such as round-trip validity, parser safety, or bounded resource use.
- Seed useful boundary cases, preserve minimized failing inputs, and make failures reproducible as ordinary tests.
- Bound input size and expensive work; do not turn fuzzing into an unbounded integration test.
- Reuse the repository's fuzz command and report runtime, corpus, and coverage limits honestly.

