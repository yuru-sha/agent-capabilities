# Collections and resilience

## Pagination and sorting

Never assume a list endpoint is complete in one response.

For each endpoint, verify the current pagination contract and:

- preserve server ordering when it is meaningful;
- use stable explicit sorting when supported and required;
- continue until the API signals completion;
- de-duplicate by resource ID when retries or page drift can overlap;
- bound memory for large collections.

## Rate limits

Treat rate limits as endpoint/app/account specific unless the current official documentation states a global rule.

- Inspect current documentation and response metadata/headers.
- Back off on documented throttling responses.
- Honor server-provided retry guidance when available.
- Add jitter to retry delays.
- Limit concurrent writes even when reads can be parallelized.

## Errors and return codes

Parse both HTTP status and TikTok's structured return code/message/request identifier when provided.

Classify failures into:

- authentication/authorization;
- validation/schema;
- business-state or policy/review;
- throttling;
- transient server/network;
- ambiguous write.

Retry only failures that are safe to retry.

For non-idempotent writes with an uncertain outcome, perform a reconciliation read/search before retrying.

## Polling

Use bounded backoff for async reports, media processing, copy tasks, or other asynchronous operations. Support cancellation and terminal failure states.

## Webhooks

Assume webhook delivery can be duplicated, delayed, or retried.

- verify signatures/authentication according to the current product docs;
- make handlers idempotent;
- persist event identity/checkpoints;
- acknowledge promptly;
- reconcile critical state with API reads.
