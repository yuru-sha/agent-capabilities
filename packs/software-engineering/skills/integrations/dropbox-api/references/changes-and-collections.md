# Changes, cursors, pagination, and batching

verified_at: 2026-10-03

## list_folder cursor model

Use `/files/list_folder` for initial traversal and retain its cursor. Continue
with `/files/list_folder/continue` while `has_more` is true.

For incremental change tracking:

1. perform an initial scan or obtain the appropriate starting cursor;
2. persist the cursor only after the application has durably processed the corresponding page;
3. later call the continuation endpoint with that cursor;
4. process additions, modifications, moves/deletions as represented by current metadata/tombstone semantics;
5. persist the new cursor.

Treat cursors as opaque. Never parse or manufacture them.

## Processing guarantee

Choose an application-level delivery model deliberately:

- at-least-once processing is usually simpler: process page, commit local state,
  then persist cursor;
- exactly-once effects require idempotent local writes or deduplication and
  cannot be obtained merely from a Dropbox cursor.

Do not advance a cursor before durable local processing if losing changes would
be unacceptable.

## Collection pagination

Many sharing/team endpoints use cursor + continuation families independent of
`files/list_folder`. Follow each endpoint's own response shape and continue
until exhausted.

Do not assume:

- every endpoint uses `has_more`;
- all cursors share one type;
- page size defaults or maximums are stable.

## Sorting

Do not rely on undocumented server order. If the product requires a stable
presentation order, sort after collection using explicit keys. For very large
collections, use bounded-memory/external sorting or downstream storage rather
than accumulating all entries in memory.

## Batching

Prefer batch endpoints when they reduce API calls and preserve acceptable
failure semantics. A batch response can contain mixed per-item success and
failure; do not treat HTTP success as proof that every entry succeeded.
