# Errors, retries, rate limits, and concurrency

verified_at: 2026-10-03

## Error classification

Handle both HTTP status and endpoint-specific tagged errors.

General policy:

- 400: request/contract problem; do not retry unchanged.
- 401: token invalid/expired/revoked, member suspended, or authorization problem;
  refresh only when the flow indicates an expired renewable token, otherwise
  re-authenticate or surface the authorization failure.
- 403: policy/permission/plan/restriction; inspect details, do not blind-retry.
- 409: endpoint-specific conflict; branch on the typed/tagged error.
- 429: rate limit or excessive parallel writes; honor Retry-After when present.
- 5xx: transient Dropbox-side failure may be retryable with bounded backoff.

Always confirm current endpoint-specific errors in the HTTP reference.

## Retry policy

Use bounded exponential backoff with jitter for retryable failures.

Priority:

1. Retry-After when present;
2. otherwise bounded exponential backoff + jitter;
3. global attempt/deadline budget;
4. cancellation support.

Do not retry malformed requests or permission failures unchanged.

## Namespace write concurrency

Dropbox documents 429 responses for both high request rate and too many
simultaneous writes to the same namespace.

Therefore:

- limit write concurrency per namespace;
- do not fix 429s merely by increasing worker count;
- consider a namespace-keyed queue/semaphore;
- use batch endpoints when appropriate;
- separate read concurrency from write concurrency if the workload allows it.

The exact safe concurrency is workload/service dependent; do not hard-code an
undocumented Dropbox limit.

## Ambiguous mutations

A transport timeout does not prove that a write failed.

For upload finish, move, copy, delete, sharing changes, and other non-idempotent
writes:

- do not immediately replay when duplication or conflict matters;
- read back metadata/state;
- reconcile by stable ID/revision/path and expected result;
- retry only when the current state proves it is safe.

## Endpoint errors

Prefer generated/tagged error variants from an official SDK or an equivalent
typed representation. If handling `error_summary`, Dropbox recommends prefix
matching rather than exact full-string matching because detail may be appended.

## Request IDs and observability

Record `X-Dropbox-Request-Id` with operation name, endpoint family, attempt,
latency, and status, but never log credentials or sensitive file content.

Track:

- 429 rate;
- retry counts and exhausted retries;
- namespace write queue depth;
- upload-session restarts/offset corrections;
- cursor lag/failures;
- 4xx categories;
- 5xx duration.

A high 429 rate should trigger workload/batching/concurrency review rather than
infinite retries.
