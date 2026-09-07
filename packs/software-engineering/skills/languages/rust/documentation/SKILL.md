---
name: rust-documentation
description: "Use when Rust code involves rustdoc, CLI help, examples, or toolchain support."
---

# Rust Documentation

Use this specialist with the global `$tdd` skill for implementation and `$code-review` for review. It owns only Rust-specific decisions for this concern.

## Rules

- Keep rustdoc, CLI help, configuration examples, serialized/API examples, and supported toolchain behavior aligned.
- Document safety invariants and compatibility boundaries where callers must rely on them.
- Prefer examples that compile or run through existing repository checks.

