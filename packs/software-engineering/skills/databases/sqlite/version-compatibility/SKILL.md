---
name: sqlite-version-compatibility
description: "Use when SQLite runtime versions, compile options, PRAGMAs, schema migrations, or platform-specific feature support change."
---

# SQLite Version Compatibility

Use with `sqlite-migrations`, `sqlite-extensions`, and the application's
supported runtime matrix.

## Check

- Identify the SQLite library version, compile options, wrapper behavior, platform packaging, and minimum supported runtime.
- Gate migrations and features with capability detection where version or compile-time support varies; do not infer support from a developer machine.
- Check PRAGMA defaults, journal behavior, type/affinity semantics, generated columns, JSON/FTS features, and locking differences.
- Test existing databases created by older versions and application startup against newer or missing capabilities.
- Document fallback, migration failure, downgrade, and rollback behavior for each supported environment.

