---
name: rust-concurrency
description: "Use when Rust code involves async tasks, threads, Send/Sync, channels, locks, or cancellation."
---

# Rust Concurrency

Use this specialist with the global `$tdd` skill for implementation and `$code-review` for review. It owns only Rust-specific decisions for this concern.

## Rules

- Make Send/Sync bounds, ownership, lock scope, channel closure, and task lifetime explicit.
- Use the repository's async runtime and define cancellation and JoinHandle shutdown; do not spawn unowned work.
- Avoid blocking an async executor and test deadlock, cancellation, and error propagation paths.

