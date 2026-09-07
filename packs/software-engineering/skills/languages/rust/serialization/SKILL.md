---
name: rust-serialization
description: "Use when Rust code involves serde, nullability, defaults, enums, unknown fields, or wire compatibility."
---

# Rust Serialization

Use this specialist with the global `$tdd` skill for implementation and `$code-review` for review. It owns only Rust-specific decisions for this concern.

## Rules

- Use the repository's serde conventions and explicit wire types; define missing, null, default, enum, unknown-field, and version behavior.
- Validate external data before constructing trusted domain values and avoid lossy coercions.
- Review compatibility before changing a public serialized representation.

