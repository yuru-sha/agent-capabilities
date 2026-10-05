# Writes, transactions, and concurrency

## Conditional writes

Use condition expressions for invariants such as create-if-absent, compare-and-set, optimistic version checks, ownership/state transitions, and uniqueness records.

Do not implement read-then-write checks without a conditional mutation when concurrent writers can race.

## Idempotency

Assume clients, workers, or upstream services can retry. Where duplicate effects matter, use an idempotency token, condition expression, deduplication record, or state-machine transition that makes repeated requests safe.

Do not blindly retry ambiguous write failures if the application cannot determine whether the original write committed.

## Transactions

Use `TransactWriteItems` or `TransactGetItems` for real multi-item atomicity requirements. Keep transactions small, deterministic, and conflict-aware.

Expect transaction conflicts under contention. Distinguish retryable conflicts/throttling from permanent validation or condition failures.

Transactions are regional. For global tables, do not assume a transaction is atomically observed across Regions.

## Batch operations

Batch APIs improve network efficiency but do not provide transactions. Handle unprocessed keys/items explicitly with bounded exponential backoff and jitter.

Preserve item-level error/accounting semantics so a partial batch retry does not duplicate unrelated side effects.
