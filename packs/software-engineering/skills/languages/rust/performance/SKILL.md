---
name: rust-performance
description: "Use when Rust code involves benchmarks, profiling, allocations, cloning, blocking, or contention."
---

# Rust Performance

Use this specialist with the global `$tdd` skill for implementation and `$code-review` for review. It owns only Rust-specific decisions for this concern.

## Rules

- Measure with the repository's benchmark or profiler before optimizing; inspect allocations, cloning, blocking, and lock contention.
- Prefer ownership and data structures that make the hot path simple over speculative unsafe code or custom pools.
- Record toolchain, workload, and command behind performance evidence.

