---
name: rust-features-workspaces
description: "Use when Rust workspace members, Cargo features, resolver behavior, optional dependencies, build scripts, or all-features builds change."
---

# Rust Features and Workspaces

Use with `rust-msrv`, `rust-api-compatibility`, and the repository's workspace
commands.

## Check

- Trace feature definitions, optional dependencies, workspace inheritance, resolver version, and feature unification across every member.
- Check default-feature leakage, feature names exposed to consumers, mutually exclusive combinations, and target-specific dependencies.
- Verify package-local, workspace, `--all-features`, `--no-default-features`, and representative target builds.
- Keep build scripts and generated code deterministic across feature combinations.
- Avoid adding a feature when a crate boundary or ordinary configuration expresses the dependency more clearly.

