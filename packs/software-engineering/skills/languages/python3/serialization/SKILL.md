---
name: python3-serialization
description: "Use when Python 3 code involves JSON, None, missing fields, datetimes, numbers, or wire compatibility."
---

# Python 3 Serialization

Use this specialist with the global `$tdd` skill for implementation and `$code-review` for review. It owns only Python 3-specific decisions for this concern.

## Rules

- Define missing, None, empty, default, numeric precision, datetime/timezone, enum, and unknown-field behavior for every wire format.
- Validate external JSON before domain use and avoid implicit coercions that change meaning.
- Review compatibility before changing a public serialized representation.

