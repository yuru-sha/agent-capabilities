# Redis atomicity and coordination

Redis executes individual commands atomically, but application workflows spanning multiple commands require explicit design.

## Preferred order

1. Use one native command when possible.
2. Use conditional commands such as `SET ... NX/XX` and compare-and-update primitives where sufficient.
3. Use transactions (`MULTI/EXEC` with `WATCH` where appropriate) for optimistic coordination.
4. Use server-side scripts/functions when multiple operations must be atomic and bounded.
5. Use distributed locks only when the invariant cannot be expressed more directly.

## Rules

- Keep Lua/functions deterministic and bounded; avoid long-running scripts that block the server.
- Treat retries around transactions and scripts as part of the correctness design.
- For locks, use unique ownership tokens, bounded lease duration, compare-and-delete release, and fencing when stale owners could still mutate an external system.
- Do not claim exactly-once behavior from Redis primitives alone.
- Pub/Sub is transient delivery; consumers that require replay or acknowledgement should use a durable mechanism such as Streams or an external queue.
- When cross-key atomicity is required in Cluster, ensure keys share a slot intentionally.
