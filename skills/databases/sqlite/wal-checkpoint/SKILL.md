---
name: sqlite-wal-checkpoint
description: "Use when SQLite WAL mode, checkpointing, busy or locked errors, reader starvation, or database file handling changes."
---

# SQLite WAL and Checkpointing

Use with `sqlite-transactions`, `sqlite-backup-restore`, and
`sqlite-performance`.

## Check

- Understand WAL mode persistence, reader/writer concurrency, checkpoint mode, autocheckpoint thresholds, and the sidecar `-wal`/`-shm` files.
- Check for long-lived readers that starve checkpoints and unbounded WAL growth.
- Define busy timeout/retry behavior and distinguish transient contention from an actual transaction or file-lifecycle bug.
- Ensure backups, copies, cleanup, and process shutdown account for all journal files and active connections.
- Measure checkpoint latency, WAL size, write throughput, and read behavior with representative concurrent workloads.

