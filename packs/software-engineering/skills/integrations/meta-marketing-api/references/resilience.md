# Rate limits, errors, retries, and observability

verified_at: 2026-10-03

## Marketing API rate limits

Marketing API limits are not one global requests-per-second number. At
verification time Meta documents Ads Management limits and Business Use Case
(BUC) usage metadata, including call count, CPU time, total time, and estimated
recovery information in response headers.

Current access-tier terminology changed in 2026. Do not copy historical
"Standard/Advanced Access" labels into product logic; inspect current Marketing
API Access Tier and rate-limit documentation.

## Read rate-limit headers

Capture current app/business-use-case usage headers without logging secrets. Use
them for adaptive concurrency, queue backpressure, alerting, estimated retry
timing, and per-account/use-case diagnostics.

Treat exact header names and fields as versioned documentation, not permanent constants.

## Error classification

Parse Meta's structured error object and preserve:

- HTTP status;
- error code and subcode;
- type/message for operator diagnostics;
- transient/retry indicators when exposed;
- request/trace identifiers when exposed.

Classify errors into authentication/permission, invalid schema/enum, resource or
ownership, policy/account restriction, rate limit, transient service,
media/async processing, and ambiguous transport failure.

Do not retry permanent validation or permission failures.

## Retry policy

Retry only operations that are safe or explicitly reconciled.

Good candidates include idempotent reads, polling/status reads, transient
failures with documented retryability, and upload chunks whose protocol safely
identifies them.

For mutations after timeout or connection loss:

1. assume the result is unknown;
2. read/reconcile using parent, correlation metadata, or external state;
3. retry only if no matching object/write exists.

Use exponential backoff with jitter and honor current retry/recovery guidance.

## Observability

Record API version, endpoint family, non-secret Ad Account ID, operation type,
duration, status/error code/subcode, rate-limit usage metadata, async job/report
ID, retry count, and correlation ID.

Redact access tokens, app secrets, customer data, hashes derived from personal
identifiers, and sensitive creative/form payloads as appropriate.
