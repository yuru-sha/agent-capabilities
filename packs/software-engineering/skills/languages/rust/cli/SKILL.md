---
name: rust-cli
description: "Use when Rust code involves CLI parsing, streams, exit codes, signals, or command errors."
---

# Rust CLI

Use this specialist with the global `$tdd` skill for implementation and `$code-review` for review. It owns only Rust-specific decisions for this concern.

## Rules

- Reuse the existing clap or standard-library CLI layer and define stdin, stdout, stderr, exit codes, signals, and cancellation.
- Validate flags and configuration before side effects and render user-safe errors without leaking secrets.
- Do not add a CLI crate for a small command when existing code is sufficient.

