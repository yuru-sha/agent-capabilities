# Backpressure and recovery

- Bound per-connection queues and message/reassembly memory. Separate telemetry that can be dropped/coalesced from commands needing ACK and durable reconciliation.
- Define heartbeat interval, timeout, stale connection cleanup and mobile sleep/wake behavior; reconnect using bounded jitter without storms.
- WebSocket does not ensure durable delivery or exactly-once command execution. Use command IDs, deduplication, explicit acknowledgements and observed-state reconciliation after ambiguous disconnect.
- Isolate slow receivers, serialize conflicting commands and cancel goroutines/tasks/subscriptions on shutdown.
- Measure redacted queue depth, reconnect counts, duplicate rejection and authorization failures.

Source: https://www.rfc-editor.org/rfc/rfc6455
