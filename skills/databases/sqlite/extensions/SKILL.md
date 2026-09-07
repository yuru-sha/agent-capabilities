---
name: sqlite-extensions
description: "Use when SQLite JSON, FTS5, virtual tables, custom extensions, tokenizers, loadable modules, or compile-time capabilities are involved."
---

# SQLite Extensions

Use with `sqlite-version-compatibility`, `security-review`, and the relevant
indexing/serialization skills.

## Check

- Verify extension availability, compile options, wrapper registration, platform packaging, and behavior on the minimum runtime.
- Treat virtual-table, FTS, tokenizer, JSON, and loadable-extension inputs as trust boundaries; constrain paths and untrusted query syntax.
- Define indexing, transaction, update, delete, rebuild, and migration semantics for the extension.
- Provide a safe fallback or fail clearly when a required capability is absent.
- Test malformed input, tokenizer behavior, escaping, ranking/query semantics, backup/restore, and schema upgrades.
