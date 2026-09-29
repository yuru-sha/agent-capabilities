---
name: rust-security
description: "Use when Rust code involves unsafe code, deserialization, paths, commands, TLS, secrets, or authorization."
---

# Rust Security

Use this specialist with oh-my-pstack's TDD workflow for implementation and oh-my-pstack's review workflow for review. It owns only Rust-specific decisions for this concern.

## Rules

- Review unsafe blocks, path and command handling, TLS, deserialization, secrets, input validation, and authorization boundaries.
- Keep credentials out of source, examples, logs, panic messages, and generated artifacts.
- Treat compiler safety as one layer; it does not prove protocol or business authorization.

