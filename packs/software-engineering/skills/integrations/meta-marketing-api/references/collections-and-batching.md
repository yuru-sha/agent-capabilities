# Collections, field selection, filtering, and batching

verified_at: 2026-10-03

## Cursor pagination

Graph API collections commonly return cursor-based paging metadata and
`next`/cursor information.

- Follow returned cursors/next links rather than synthesizing page numbers.
- Stop only when the response indicates there is no next page.
- Stream/process pages incrementally for large result sets.
- Persist checkpoints for long-running synchronization jobs.

## Field selection and expansion

Request only fields needed for the use case. Deep field expansion can create
large, slow, rate-limit-heavy responses.

Prefer a small number of purpose-built reads over one enormous nested expansion
when that improves retry isolation and observability.

## Filtering and sorting

Use server-side filtering/sorting only where the current edge/reference
documents it. Do not assume Graph API supports arbitrary SQL-like filters or
stable sort keys on every edge.

For deterministic synchronization, define an explicit ordering/checkpoint model
in the application even when the API's collection order is not guaranteed.

## Batch API

Graph API batch requests can reduce round trips but are not a transaction and
do not remove per-call validation, permission checks, or rate-limit accounting.

Use batch requests when calls are independent or explicit dependency semantics
are supported, payload size remains bounded, and per-item errors are handled separately.

Do not batch non-idempotent mutations merely to maximize throughput.

## Concurrency

Bound concurrency per app/account/use case. Adaptive concurrency should react to
current rate-limit headers and error responses rather than using one global
worker count.
