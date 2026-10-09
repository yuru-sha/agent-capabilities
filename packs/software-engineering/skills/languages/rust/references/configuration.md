---
name: rust-configuration
description: "Use when Rust code involves CLI, environment, files, defaults, or secret handling."
---

# Rust Configuration

Use this specialist with the project's TDD workflow for implementation and the project's review workflow for review. It owns only Rust-specific decisions for this concern.

## Rules

- Parse and validate configuration at startup or command entry with explicit CLI/environment/file precedence.
- Avoid hidden global mutable configuration and distinguish missing, empty, invalid, and default values.
- Keep secrets out of defaults, Debug output, logs, and test fixtures.

