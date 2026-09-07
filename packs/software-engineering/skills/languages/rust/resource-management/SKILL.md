---
name: rust-resource-management
description: "Use when Rust code involves RAII, Drop, guards, tasks, locks, transactions, or cleanup."
---

# Rust Resource management

Use this specialist with the global `$tdd` skill for implementation and `$code-review` for review. It owns only Rust-specific decisions for this concern.

## Rules

- Use RAII, Drop, and guard scope for files, sockets, locks, spans, transactions, and runtime handles.
- Define shutdown for spawned tasks and make cancellation release resources deterministically.
- Test error and cancellation paths rather than relying on process teardown.

