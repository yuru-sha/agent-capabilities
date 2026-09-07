---
name: typescript-runtime-validation
description: "Use when TypeScript consumes JSON, environment variables, headers, untyped JavaScript, DOM values, or other runtime data."
---

# TypeScript Runtime Validation

Use at every trust boundary where static types are erased. Compose with
`typescript-type-design`, `typescript-security`, and the applicable API skill.

## Rules

- Validate shape, requiredness, nullability, enums, ranges, and cross-field invariants before using external data.
- Prefer `unknown` plus a repository-approved parser or small explicit guard; do not treat `as`, non-null assertions, or `any` as validation.
- Keep validation and normalization behavior visible, deterministic, and consistent with the error contract.
- Preserve the distinction between absent, `null`, empty, and invalid values when the boundary requires it.
- Add malformed, partial, and unexpected-extra-field tests at the boundary rather than only testing typed happy paths.

