# BullMQ delivery, retries, and idempotency

BullMQ jobs can be processed more than once because workers may crash, lose locks, stall, or retry failed work.

## Rules

- Make externally visible side effects idempotent.
- Persist an idempotency key or business operation ID when duplicate execution would be harmful.
- Use `attempts` and backoff intentionally; retries without backoff can amplify outages.
- Distinguish transient failures from permanent validation/business failures.
- Throw `Error` objects from processors so BullMQ failure handling behaves predictably.
- Ensure a retry can safely resume after partial progress.
- Treat timeouts and lost connections as potentially ambiguous outcomes if an external side effect may already have succeeded.

## Stalled jobs

A worker holds and renews a job lock. If renewal cannot happen, the job may be moved back to waiting and executed again or eventually fail after exceeding stalled limits. CPU-heavy work that blocks the Node.js event loop increases this risk.

Test:
- process crash after side effect but before completion acknowledgement;
- Redis disconnect/reconnect;
- worker restart;
- retry after partial external success.
