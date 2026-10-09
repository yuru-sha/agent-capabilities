---
name: go-serialization
description: "Use when Go code involves JSON, wire types, nullability, numbers, dates, or compatibility."
---

# Go Serialization

Use this specialist with the project's TDD workflow for implementation and the project's review workflow for review. It owns only Go-specific decisions for this concern.

## Rules

- Use explicit encoding/json wire types and distinguish absent, null, zero, empty, time, number, and enum values when the contract does.
- Reject ambiguous or oversized external payloads before domain logic.
- Keep serialized forms stable and review migrations when a public representation changes.

