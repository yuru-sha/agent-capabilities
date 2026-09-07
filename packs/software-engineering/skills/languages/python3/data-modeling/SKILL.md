---
name: python3-data-modeling
description: "Use when choosing or reviewing Python 3 dataclasses, TypedDicts, Protocols, enums, immutable values, validation, or serialization models."
---

# Python 3 Data Modeling

Use with `python3-type-checking` and `python3-serialization` when the model is
typed or crosses a persistence/API boundary.

## Check

- Choose `dataclass`, `TypedDict`, `Protocol`, named tuple, enum, or a validation model based on runtime behavior and ownership, not fashion.
- Make mutability, equality, ordering, defaults, `None`, missing fields, and nested values explicit.
- Keep parsing and validation at the boundary; do not let partially initialized objects masquerade as valid domain values.
- Avoid mutable defaults, accidental shared state, and serialization behavior that depends on incidental field order.
- Test round trips, invalid input, backward-compatible missing fields, and unknown fields according to the contract.

