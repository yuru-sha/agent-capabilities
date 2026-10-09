---
name: rust-dependencies
description: "Use when Rust code involves Cargo.toml, Cargo.lock, toolchains, features, or dependency security."
---

# Rust Dependencies

Use this specialist with the project's TDD workflow for implementation and the project's review workflow for review. It owns only Rust-specific decisions for this concern.

## Rules

- Preserve Cargo.toml, Cargo.lock, and the pinned toolchain; add a crate only for a concrete capability.
- Use the repository's existing audit, deny, license, and feature checks and inspect transitive changes.
- Do not mix a broad dependency update with an unrelated feature.

