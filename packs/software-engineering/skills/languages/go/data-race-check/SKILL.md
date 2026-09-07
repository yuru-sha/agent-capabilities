---
name: go-data-race-check
description: "Use when checking Go code for data races, unsafe shared state, goroutine interleavings, or race-detector coverage."
---

# Go data-race check

Use this specialist with the global `$tdd` skill for implementation work and `$code-review` for review work. It owns only this language-specific concern.

## Rules

- Run the repository's race-enabled command, typically `go test -race` or `go run -race`, at the smallest relevant scope first.
- Review maps, slices, pointers, captured variables, goroutine ownership, channel closure, atomics, and lock scope; compile success does not prove race freedom.
- Exercise conflicting interleavings with deterministic coordination or bounded repetition; do not use sleeps as the primary proof.
- Treat a clean race run as evidence for executed paths only and report unexecuted paths, unavailable tools, and performance impact separately.

