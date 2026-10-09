---
name: rust-refactoring
description: "Use when Rust code involves types, traits, macros, generics, public APIs, or generated code."
---

# Rust Refactoring

Use this specialist with pstack's TDD workflow for implementation and pstack's review workflow for review. It owns only Rust-specific decisions for this concern.

## Rules

- Prefer small types and explicit ownership; add a trait, macro, or generic abstraction only for a second real implementation or seam.
- Preserve public APIs and feature behavior and keep generated code separate from hand-written adapters.
- Use the repository's formatter and lints as gates, not as a reason to broaden the change.

