---
name: go-struct-json-tags
description: "Use when generating or reviewing Go structs and json tags from JSON examples, JSON Schema, or API payloads."
---

# Go struct and JSON-tag generation

Use this specialist with the global `$tdd` skill for implementation work and `$code-review` for review work. It owns only this language-specific concern.

## Rules

- Identify the input contract, target package, Go version, naming policy, and whether output is generated or hand-maintained before emitting code.
- Create exported fields with deterministic `json:"..."` names; report invalid identifiers, collisions, reserved words, and ambiguous nested shapes instead of silently dropping data.
- Map nullable or optional values deliberately, use `omitempty` only when omission matches the wire contract, and avoid `any` when a concrete nested type or `json.RawMessage` preserves meaning.
- Choose number, time, array, map, and additionalProperties representations from the contract; use `json.Number` or a custom type when precision requires it.
- Keep generated output separate from hand-written methods, run gofmt, and make regeneration deterministic. Reuse an existing repository generator before adding a dependency.

