---
name: rust-api-compatibility
description: "Use when changing a Rust crate's public API, semver behavior, feature flags, error types, serialization, or documented public contract."
---

# Rust API Compatibility

Use with `$code-review`, `rust-features-workspaces`, and the matching wire or
OpenAPI skill when the crate is a protocol client/server.

## Check

- Compare public modules, types, trait methods, bounds, visibility, constants, feature gates, and macro output across the supported versions.
- Treat changed defaults, error variants, trait implementations, serde representation, and feature combinations as compatibility surfaces.
- Check semver impact, deprecation path, changelog, migration examples, and downstream compile behavior rather than only local tests.
- Use the repository's compatibility checker or consumer fixture when available.
- Keep generated API and docs synchronized with the actual public surface.

