---
name: rust-testing
description: "Use when Rust code involves tests, integration seams, async tests, property tests, fuzzing, or benchmarks."
---

# Rust Testing

Use this specialist with the global `$tdd` skill for implementation and `$code-review` for review. It owns only Rust-specific decisions for this concern.

## Rules

- Test public behavior through the repository's cargo test layout; use integration seams for externally visible contracts.
- Use the existing async, property, fuzz, or benchmark tools only when the behavior and repository already justify them.
- Keep async tests deterministic and make cancellation, ownership, and cleanup observable.

