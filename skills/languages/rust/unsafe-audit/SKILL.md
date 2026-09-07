---
name: rust-unsafe-audit
description: "Use when Rust changes unsafe blocks, raw pointers, FFI wrappers, transmute, manual allocation, or safe abstractions over unsafe code."
---

# Rust Unsafe Audit

Use with `rust-ffi-abi`, `$code-review`, and the repository's sanitizer or Miri
workflow when available.

## Check

- Require a local safety invariant for every `unsafe` block; review it against all callers, lifetimes, aliasing, initialization, alignment, and thread-safety assumptions.
- Minimize the unsafe region and keep unchecked operations behind a small safe abstraction with tests for boundary cases.
- Audit raw pointer provenance, ownership/freeing, integer casts, layout, uninitialized memory, `Send`/`Sync`, and panic cleanup.
- Prefer safe standard-library or crate APIs when they express the invariant without unsafe code.
- Run the strongest existing checks and state what Miri, sanitizer, target, or concurrency coverage was unavailable.

