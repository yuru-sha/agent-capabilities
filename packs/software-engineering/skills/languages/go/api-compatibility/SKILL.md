---
name: go-api-compatibility
description: "Use when changing an exported Go package, public method, error contract, JSON or wire format, or versioned API."
---

# Go API Compatibility

Use with `$code-review`, `go-serialization`, `go-error-handling`, and the
relevant OpenAPI compatibility skills when the API crosses a process boundary.

## Check

- Compare exported identifiers, method sets, interfaces, constructors, zero-value behavior, and sentinel/wrapped errors.
- Treat serialized field names, omission, nullability, numeric representation, and unknown-field behavior as compatibility surfaces.
- Check source, binary, behavioral, and wire compatibility separately; a compiling consumer is not proof of wire compatibility.
- Preserve deprecated paths when required, document migration order, and avoid changing defaults or error timing silently.
- Use the repository's API compatibility tool or consumer fixtures if present, and record any untested consumer assumptions.

