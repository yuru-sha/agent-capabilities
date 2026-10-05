---
name: typescript-type-design
description: "Use when designing or reviewing TypeScript types, public interfaces, generics, unions, narrowing, or strictness boundaries."
---

# TypeScript Type Design

Use with `typescript-runtime-validation` when values come from outside the
type system. Types document and constrain code; they do not validate runtime
input.

## Rules

- Prefer precise domain types, discriminated unions, `unknown` at untrusted boundaries, and narrowing over broad `any` or assertions.
- Keep generic constraints, variance, optionality, `null`/`undefined`, and readonly behavior intentional in public types.
- Model impossible states out of the type space without making normal callers fight the type system.
- Check declaration output and consumer ergonomics for exported types; avoid leaking internal implementation types.
- Use the repository's strict compiler settings and type tests; do not weaken them to make an invalid design compile.

