# Pagination, rate limits, errors, and retries

verified_at: 2026-10-03

## Cursor pagination

Many collection GET endpoints support `count`, `cursor`, and
`next_cursor`.

Algorithm:

1. Request the first page with an allowed count.
2. Process that page before fetching the next one.
3. If `next_cursor` is null, stop.
4. Otherwise pass the cursor opaquely on the next request.
5. De-duplicate by stable resource ID if the consuming workflow cannot tolerate
   changes between pages.

The current pagination guide says most endpoints use a default count of 200 and
a maximum of 1000. Verify per endpoint. Analytics does not use this generic
pagination model; partition analytics by time/entity/job limits instead.

## Rate limits

Read the current Rate Limiting documentation and response headers for every
endpoint family. Do not assume one global rate.

At verification time, X documents both user-token and ad-account rate-limit
scopes. Prefer account-level headers when they are returned:

- user scope: `x-rate-limit-limit`, `x-rate-limit-remaining`,
  `x-rate-limit-reset`;
- ad-account scope: `x-account-rate-limit-limit`,
  `x-account-rate-limit-remaining`, `x-account-rate-limit-reset`.

Account-level limits are documented for eligible GET endpoints and are not a
general write-limit contract. Current rate-limit tables also distinguish
categories and endpoints, so do not use one concurrency budget for all calls.

At minimum:

- observe remaining/reset headers when provided;
- prefer the ad-account limit when the response includes it;
- stop increasing concurrency when remaining capacity is low;
- wait until reset for hard rate-limit responses;
- use bounded exponential backoff with jitter for eligible transient failures;
- cap concurrency separately for account-scoped async jobs and high-volume
  collection reads;
- use high-count reads and multi-entity filters where the current endpoint
  supports them rather than repeatedly fetching the same data.

Current Analytics documentation states synchronous analytics is user-level 250
requests per 15 minutes and asynchronous analytics allows 100 concurrently
processing jobs per account. Re-check these values before relying on them.

## Error classes

Distinguish:

- authentication/signature errors;
- authorization/account access;
- invalid/expired resource IDs;
- validation/enum/schema errors;
- funding/budget constraints;
- rate limiting;
- media format or processing errors;
- async job processing failures;
- transient server/network errors.

The official API returns structured `errors[].code` values for many failures,
but HTTP status remains authoritative when a structured body is unavailable.

## Retry policy

Usually retryable after appropriate delay:

- explicit rate-limit responses after reset;
- selected 5xx/transient network failures for idempotent reads;
- polling when an async job or media object is still processing.

Usually non-retryable without changing the request or authorization:

- invalid parameter / unsupported enum;
- permission/account access failure;
- not-found for the intended resource;
- invalid media/category;
- funding constraints;
- rejected/failed async job after terminal state.

For POST/PUT/DELETE, never assume a transport error means no mutation occurred.
Before retrying a non-idempotent or destructive operation, read back the
resource or use an available idempotency/deduplication mechanism documented by
the current API.

## Polling

For media processing and async analytics:

- use an explicit terminal-state set from the current reference;
- back off between polls rather than tight-looping;
- honor any server-provided retry hints;
- impose an overall deadline and maximum attempts;
- persist identifiers required to resume polling;
- on terminal failure, surface the server-provided failure details rather than
  re-submitting the whole workflow blindly.
