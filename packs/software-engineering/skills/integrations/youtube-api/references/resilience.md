# Quota, errors, retries, and observability

verified_at: 2026-10-03

## Quota model

The Data API uses quota and currently documents distinct default allocation concepts for:

- video uploads;
- search calls;
- a combined pool for other endpoints.

Treat current numeric allocations as service configuration, not stable constants.

All requests, including invalid requests, can consume quota. Therefore validate locally when possible and avoid speculative calls.

## Quota-aware design

- Prefer exact ID/list methods over search when possible.
- Traverse a channel's uploads playlist instead of repeatedly searching the global index.
- Cache stable public metadata when product freshness permits.
- Stop pagination once the application has enough results.
- Request only needed parts/fields.
- For batches, estimate operation mix before launching large runs.
- Surface quota exhaustion separately from rate limiting.

Do not repeatedly retry `quotaExceeded`; wait for quota recovery or request additional quota according to current YouTube policy.

## Error classification

Inspect both HTTP status and YouTube/Google error reason.

Examples in current official documentation include:

- `quotaExceeded`;
- `forbidden`;
- `incompatibleParameters`;
- `invalidFilters`;
- `invalidPageToken`;
- method-specific reasons such as upload, comment, playlist, caption, or live-state failures.

Do not key logic solely on human-readable error message text.

## Retry policy

Retry candidates commonly include:

- network interruption;
- connection reset/timeout where the operation is safely resumable;
- documented transient 5xx;
- documented rate-limit conditions, respecting `Retry-After`.

Use bounded exponential backoff with jitter.

Do not blindly retry:

- invalid parameters;
- insufficient permissions/scopes;
- not-found caused by a bad identifier;
- `quotaExceeded`;
- permanent upload validation errors;
- invalid live-state transitions.

## Ambiguous mutations

A timeout does not prove a mutation failed.

For uploads, comments, playlist writes, live transitions, deletes, or metadata updates:

- inspect resumable session/server state where available;
- read back the target resource;
- reconcile using stable IDs and expected state;
- retry only when duplication/state conflict is understood.

## Batch failure handling

Each item owns its own attempt count, last error, next retry time, and final state.

Do not retry an entire multi-channel batch because one item failed.

Bound retries globally and per item.

## Observability

Record non-secret operational fields such as:

- API family and method;
- channel ID;
- video/resource ID;
- quota/error reason;
- HTTP status;
- attempt number;
- latency;
- upload byte offset/progress;
- report job/report ID;
- live broadcast/stream ID and state.

Never log bearer tokens, refresh tokens, client secrets, resumable upload-session URLs, or private report download URLs.

Track quota exhaustion, rate-limit frequency, retry counts, duplicate-prevention events, upload resumptions, permanent failures, and ambiguous writes.
