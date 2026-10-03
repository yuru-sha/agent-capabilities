# Rate limits, errors, retries, and polling

verified_at: 2026-10-03

Operational failures must be classified before retrying. Rate-limit scope,
mutation ambiguity, async processing, and validation freshness are all part of
the same recovery decision.

## Rate-limit scopes

At verification time X documents user-token and Ads-account rate-limit headers.

User scope:

- `x-rate-limit-limit`;
- `x-rate-limit-remaining`;
- `x-rate-limit-reset`.

Ads-account scope:

- `x-account-rate-limit-limit`;
- `x-account-rate-limit-remaining`;
- `x-account-rate-limit-reset`.

Prefer account-level capacity for eligible account-scoped reads when returned,
but do not assume those headers exist for every endpoint or write.

Rate-limit values vary by endpoint/category. Do not implement one global rate.

## Adaptive concurrency

Bound concurrency according to:

- remaining/reset capacity;
- endpoint latency;
- async-job limits;
- downstream processing capacity.

Reduce or stop new work when capacity approaches zero. On a rate-limit response,
pause the affected scope until reset and add bounded jitter before resuming.

Current Analytics documentation has dedicated sync request limits and an
account-level maximum for concurrently processing async jobs. Re-check current
values before relying on them.

## Error classes

Distinguish at least:

- authentication/signature;
- authorization/account access;
- resource ownership/not-found;
- validation/schema/enum;
- targeting incompatibility;
- schedule/timezone;
- currency/budget/funding;
- rate limit;
- media upload/processing;
- creative approval/review;
- async analytics job;
- transient network/server;
- non-idempotent/destructive write with unknown outcome.

Use both HTTP status and the current structured error payload when available.
Preserve documented error code/message, affected parameter, request/correlation
ID, and retry/reset metadata. Do not log credentials or OAuth headers.

## Retryability

Usually retryable with bounds:

- rate limits after reset;
- selected network/5xx failures for idempotent reads;
- non-terminal media/report processing states.

Usually not retryable without changing request/state:

- invalid parameters or enums;
- permission/account-access failures;
- unsupported advertising/product combinations;
- invalid media format/category;
- funding/budget constraints;
- terminal media-processing failure;
- terminal async-report failure.

## Ambiguous writes

For POST/PUT/DELETE timeout or connection loss:

1. do not assume the mutation failed;
2. read back the resource/association;
3. determine whether the intended state already exists;
4. retry only when current semantics make it safe.

Do not blindly retry resource creation, association creation, or destructive
operations.

## Validation errors as freshness signals

Unexpected 4xx validation failures can indicate stale local knowledge.

Re-open current official documentation when failures suggest:

- changed required parameters;
- removed/changed enums;
- changed resource relationships;
- changed media requirements;
- changed metric/dimension compatibility.

Update local references only after confirming the current contract.

## Polling

For media processing and async Analytics:

- use the current documented terminal states;
- back off between polls;
- honor server retry hints when present;
- impose an overall deadline and maximum attempts;
- persist IDs needed to resume polling;
- surface terminal failure details rather than resubmitting the whole workflow.

## Request reduction

Prefer supported mechanisms that reduce request volume:

- multi-ID filters;
- reasonable larger pages;
- reusable cached lookup/reference data within freshness bounds;
- async reporting for large historical ranges;
- avoiding repeated reads of static metadata inside loops.
