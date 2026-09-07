---
name: rust-msrv
description: "Use when Rust code, dependencies, language features, targets, or CI must support a declared minimum supported Rust version."
---

# Rust MSRV

Use with `$code-review`, `rust-features-workspaces`, and the repository's
toolchain/CI definition.

## Check

- Read the declared `rust-version`, toolchain files, CI matrix, target policy, and dependency MSRV constraints before changing code.
- Verify language/library features, Cargo behavior, build scripts, proc macros, and dependency versions against the declared minimum compiler.
- Test with the actual MSRV toolchain when available; a successful build on the newest local compiler is not MSRV evidence.
- Keep lockfile and resolver behavior compatible with the supported workflow and document unavoidable platform exceptions.
- Do not raise MSRV silently through a convenience API, dependency update, edition change, or generated code.

