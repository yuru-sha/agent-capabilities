---
name: rust-configuration
description: "Use when Rust code involves CLI, environment, files, defaults, or secret handling."
---

# Rust Configuration

Use this specialist with the global `$tdd` skill for implementation and `$code-review` for review. It owns only Rust-specific decisions for this concern.

## Rules

- Parse and validate configuration at startup or command entry with explicit CLI/environment/file precedence.
- Avoid hidden global mutable configuration and distinguish missing, empty, invalid, and default values.
- Keep secrets out of defaults, Debug output, logs, and test fixtures.

