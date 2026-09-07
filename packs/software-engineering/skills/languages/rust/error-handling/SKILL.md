---
name: rust-error-handling
description: "Use when Rust code involves Result, Option, error context, unwrap, or failure propagation."
---

# Rust Error handling

Use this specialist with the global `$tdd` skill for implementation and `$code-review` for review. It owns only Rust-specific decisions for this concern.

## Rules

- Use Result/Option and ? to preserve failure paths; add context at boundaries with the repository's existing error crate.
- Avoid unwrap/expect on untrusted or operational paths unless the invariant is local, explicit, and tested.
- Keep error types stable where callers match them and avoid a second error hierarchy.

