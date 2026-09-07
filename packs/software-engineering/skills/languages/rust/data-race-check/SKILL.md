---
name: rust-data-race-check
description: "Use when checking Rust for data races, unsafe shared state, Send/Sync boundaries, or concurrent logic races."
---

# Rust data-race check

Use this specialist with the global `$tdd` skill for implementation work and `$code-review` for review work. It owns only this language-specific concern.

## Rules

- Use the compiler's Send/Sync and ownership diagnostics as one layer, then inspect unsafe code, interior mutability, FFI, atomics, and lock-free paths.
- Distinguish memory-race prevention from logical races such as stale state, lost updates, deadlocks, and cancellation ordering.
- Use existing Loom, Miri, sanitizer, stress, or model-test support when configured; do not add a tool just to produce a green badge.
- Record the schedule/model and paths exercised; a successful build alone is not a concurrency proof.

