---
name: sqlite-vacuum-maintenance
description: "Use when SQLite VACUUM, auto_vacuum, ANALYZE, free pages, page size, or maintenance scheduling is involved."
---

# SQLite Vacuum and Maintenance

Use with `sqlite-performance`, `sqlite-wal-checkpoint`, and
`sqlite-integrity-recovery`.

## Check

- Choose ordinary `VACUUM`, `VACUUM INTO`, incremental auto-vacuum, or no rebuild based on file size, fragmentation, journal mode, and downtime.
- Account for temporary disk space, write locks, transaction boundaries, page-size constraints, and interruption/recovery.
- Run `ANALYZE` or maintain statistics where query plans depend on them; verify with representative plans.
- Measure file size, free pages, write cost, and query behavior before and after maintenance.
- Do not schedule a full rebuild as a generic fix for a workload or indexing problem that evidence does not show.

