---
name: sqlite-backup-restore
description: "Use when SQLite database backup, restore, online backup, VACUUM INTO, file copying, or disaster recovery is involved."
---

# SQLite Backup and Restore

Use with `sqlite-wal-checkpoint`, `sqlite-integrity-recovery`, and
`sqlite-version-compatibility`.

## Check

- Choose an online backup, `VACUUM INTO`, or controlled file copy based on journal mode, active writers, size, and recovery needs.
- Preserve a transactionally consistent snapshot and define behavior for concurrent readers/writers, busy timeouts, and interrupted copies.
- Protect backup files, permissions, paths, and encryption assumptions; do not confuse a copied file with a verified backup.
- Restore into an isolated path, run integrity checks, verify schema/data and application reads, then define atomic replacement and rollback.
- Test disk-full, locked, partial, and older/newer runtime scenarios relevant to the deployment.

