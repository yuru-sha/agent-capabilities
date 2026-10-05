---
name: python3-type-checking
description: "Use when reviewing Python 3 type hints, mypy or pyright configuration, Any usage, Optional narrowing, Protocols, or typed boundaries."
---

# Python 3 Type Checking

Use with `python3-data-modeling` or `python3-serialization` when the typed
boundary also has a runtime representation, and with the repository's actual
mypy, pyright, or type-check command. Static typing does not validate runtime
values.

## Check

- Treat `Any` as a deliberate escape hatch: prevent unrestricted `Any` at input, output, and public API boundaries and trace its propagation into downstream code.
- Review `cast`, `# type: ignore`, `type: ignore[code]`, and untyped definitions for a specific, documented reason and a narrowing plan.
- Narrow `Optional`/`None`, unions, containers, and exceptions explicitly; use `Protocol`, `TypedDict`, dataclasses, or generics where they express the contract.
- Keep strictness settings, stubs, plugins, generated types, and Python-version targets consistent with CI.
- Pair static checks with malformed-runtime tests; a green type checker is not proof that JSON, config, or database values are valid.
