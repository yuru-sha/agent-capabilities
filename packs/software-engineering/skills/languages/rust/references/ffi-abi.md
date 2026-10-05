---
name: rust-ffi-abi
description: "Use when Rust crosses a C ABI, dynamic library, foreign callback, shared memory, or other FFI boundary."
---

# Rust FFI and ABI

Use with `rust-unsafe-audit`, `rust-api-compatibility`, and the target
platform's build/link instructions.

## Check

- Use explicit `#[repr(C)]` layout and FFI-safe types; do not expose Rust layout, references, trait objects, or unwinding assumptions across C ABI boundaries.
- Define ownership, allocation/freeing, nullability, string encoding, length/capacity, callback lifetime, and thread-affinity contracts.
- Prevent Rust panics from crossing the boundary and handle foreign errors without leaks or double frees.
- Check symbol names, calling conventions, link flags, generated headers, platform variants, and feature combinations.
- Exercise null, invalid length, repeated free, callback-after-drop, concurrent, and foreign-side error cases.

