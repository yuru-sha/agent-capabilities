---
name: sqlite-integrity-recovery
description: "Use when SQLite corruption signals, integrity checks, recovery, repair, immutable reads, or atomic database replacement are involved."
---

# SQLite Integrity and Recovery

Use with `sqlite-backup-restore`, `sqlite-wal-checkpoint`, and
`sqlite-version-compatibility`.

## Check

- Use `PRAGMA integrity_check` or `quick_check` at the appropriate scope and treat their output as evidence, not a repair command.
- Preserve the original database and journal files before attempting recovery; make replacement atomic and reversible.
- Distinguish corruption, schema mismatch, unsupported features, locking, filesystem failure, and application-level inconsistency.
- Define read-only or immutable handling, user-visible failure behavior, telemetry, and escalation when recovery is incomplete.
- Verify the recovered database with integrity, schema, row-count/domain checks, and application-level reads before returning it to service.

