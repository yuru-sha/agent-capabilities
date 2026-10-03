# Pagination

verified_at: 2026-10-03

Pagination is part of correctness, not just performance. Never assume a single
response contains every matching resource.

## Cursor model

Many collection endpoints use:

- `count`;
- opaque `cursor`;
- `next_cursor`.

General loop:

1. request the first page;
2. process/store it incrementally;
3. read `next_cursor`;
4. stop when the current endpoint indicates termination;
5. otherwise pass the returned cursor unchanged.

Treat cursors as opaque tokens. Do not parse or synthesize them.

## Limits

The current generic pagination guide documents common defaults/maxima, but
endpoint-specific limits can differ. Verify the current endpoint before choosing
`count`.

Do not use a maximum page size automatically when:

- response payloads are large;
- latency/timeouts increase materially;
- downstream processing is slower than retrieval;
- rate-limit strategy favors smaller bounded pages.

## Duplicate and mutation safety

Datasets can change while traversing pages.

For workflows requiring stable processing:

- de-duplicate by stable resource ID;
- record processed IDs or checkpoints;
- avoid mutating the same collection concurrently with a pagination scan when
  that can change membership/order;
- restart safely if a cursor expires or becomes invalid according to current API
  semantics.

## Analytics is different

Do not force generic cursor pagination onto Analytics. Partition reporting using
the current entity-ID, date-range, segmentation, and async-job limits.

## Memory behavior

Process pages incrementally. Avoid concatenating all pages into one in-memory
array unless the bounded result size is known and small.
