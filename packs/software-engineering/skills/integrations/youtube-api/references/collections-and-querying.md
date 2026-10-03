# Collections, filtering, sorting, and partial responses

verified_at: 2026-10-03

## Pagination

Data/Live collection methods commonly use opaque `pageToken` values with fields such as `nextPageToken` and optional `prevPageToken`.

Rules:

- treat tokens as opaque;
- preserve all query parameters that define the collection when continuing;
- stop as soon as enough results are collected;
- do not restart a full scan merely because one page is empty;
- handle expired/invalid page tokens as contract/state errors rather than infinite retries.

Analytics uses its own row pagination model; Reporting job/report listing has its own collection semantics. Do not assume one pagination mechanism across all API families.

## Filters

Prefer narrow resource filters:

- exact video/channel/playlist IDs where known;
- authenticated-owner filters such as `mine` where supported;
- playlist/channel-specific traversal instead of global search.

Verify mutually exclusive filter combinations in the method reference.

## Sorting

Only rely on server sorting explicitly documented by the method.

For Analytics, `sort` is part of the query model and descending order is commonly expressed with a leading `-`.

For API methods without documented ordering, sort application-side if the product requires a stable order.

## Partial responses

Use:

- `part` to select YouTube resource sections as required by the method;
- `fields`/partial-response syntax where supported to avoid transferring unused fields.

Do not omit a required `part` merely because `fields` asks for a nested field.

## Search versus list

Search is expensive enough to deserve intentional use and has its own quota bucket/default allocation policy.

Prefer exact list methods and upload-playlist traversal when IDs/channel context are known.

A common efficient pattern is:

1. use `search.list` only to discover candidate IDs;
2. collect IDs;
3. call resource-specific `*.list` methods for detailed fields.

## Deduplication during traversal

When pages can be refreshed/retried or the underlying collection changes concurrently, deduplicate by stable YouTube resource ID rather than display title.
