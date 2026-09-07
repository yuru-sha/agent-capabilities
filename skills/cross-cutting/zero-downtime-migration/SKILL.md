---
name: zero-downtime-migration
description: "Use when a schema, API, data, or configuration migration must run while old and new application versions coexist without avoidable downtime."
---

# Zero-Downtime Migration

Compose with the matching database migration, locking, compatibility, and
OpenAPI versioning skills. The expand/backfill/contract pattern is a default,
not a guarantee that every operation is online.

## Check

- Design an expand phase compatible with old and new readers/writers, a bounded/idempotent backfill, and a contract phase after the old path is retired.
- Measure DDL locks, transaction duration, write amplification, replication/backup impact, and connection-pool behavior before production rollout.
- Make retries, checkpoints, throttling, pause/resume, observability, and operator abort behavior explicit.
- Test mixed-version traffic, partial backfill, duplicate/replayed work, deploy rollback, and data-loss scenarios.
- Confirm that the database, API, generated clients, events, and operational runbooks share the same compatibility window.

