---
name: go-testing
description: "Use when Go code involves tests, table-driven cases, subtests, race, fuzzing, or benchmarks."
---

# Go Testing

Use this specialist with the global `$tdd` skill for implementation and `$code-review` for review. It owns only Go-specific decisions for this concern.

## Rules

- Use table-driven cases with t.Run; parallel tests require isolated fixtures, ports, environment, and cleanup.
- Exercise HTTP seams with httptest and add -race, fuzz, or benchmark coverage only when the changed behavior warrants it.
- Keep expected values independent of the implementation and let the repository's existing test command define the gate.

