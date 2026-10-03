# Collection traversal: pagination and sorting

verified_at: 2026-10-03

Pagination and ordering are correctness concerns. Do not assume a single
response is complete or that collection order is stable.

## Cursor pagination

Many collection endpoints use:

- `count`;
- opaque `cursor`;
- `next_cursor`.

General traversal:

1. request the first page with an endpoint-appropriate count;
2. process/store it incrementally;
3. read `next_cursor`;
4. stop when the endpoint indicates termination;
5. otherwise pass the returned cursor unchanged.

Treat cursors as opaque. Do not parse, synthesize, or persist assumptions about
their internal structure.

The generic pagination documentation has common defaults/maxima, but endpoint
limits can differ. Verify the current endpoint before choosing page size.

## Stable processing

Collections can change while pages are being traversed.

When correctness matters:

- de-duplicate by stable resource ID;
- keep a checkpoint or processed-ID set when resumability is required;
- avoid mutating collection membership concurrently with a scan when practical;
- define recovery behavior for expired/invalid cursors;
- do not assume page boundaries remain stable across retries.

Process pages incrementally rather than concatenating the entire collection in
memory.

## Sorting

Do not assume a universal `sort` parameter or default order.

Before relying on server-side sorting, verify from the current endpoint:

- whether sorting is supported;
- allowed fields;
- ascending/descending syntax;
- default order;
- whether ordering is guaranteed/stable;
- interaction with cursor pagination.

Do not copy sort parameters from another endpoint or an old SDK.

## Sorting with pagination

If deterministic traversal is required:

- prefer documented stable server-side ordering;
- use a stable tie-breaker when the endpoint supports it;
- de-duplicate by resource ID;
- account for resources created/updated during traversal.

Client-side sorting after pagination does not make the original traversal
stable.

## Client-side and external sorting

Client-side sorting is appropriate only when the complete bounded dataset has
intentionally been retrieved.

For large collections, use persistent/external sorting rather than loading all
items into memory solely to sort them.

For reporting "top N" results, retrieve the complete intended report scope
first, compute the metric consistently, then sort in the reporting layer unless
the current Analytics endpoint explicitly provides the required ordering.

## Analytics exception

Analytics does not use the generic collection cursor model. Partition reports by
the current entity-ID, time-range, segmentation, and async-job limits.
