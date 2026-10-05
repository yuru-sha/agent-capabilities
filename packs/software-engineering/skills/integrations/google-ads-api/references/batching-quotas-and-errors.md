# Batching, quotas, and errors

## BatchJobService

Use `BatchJobService` for large asynchronous collections of supported mutate operations when reducing synchronous request count, using temporary IDs, or delegating transient retries is useful.

Official overview:
https://developers.google.com/google-ads/api/docs/batch-processing/overview

Batch jobs use partial-failure-style execution for supported operations: successful operations are not generally rolled back because another operation fails. Some operations that require atomic behavior are not supported in batch jobs; verify the current list before use.

Do not assume BatchJobService is automatically faster. Choose it for operational fit, not as a universal performance optimization.

## Important verified limits

Official quotas:
https://developers.google.com/google-ads/api/docs/best-practices/quotas

As verified on 2026-10-05:
- standard mutate requests allow up to 10,000 mutate operations per request;
- Google Ads client libraries configure a 64 MB maximum gRPC response size;
- daily API-operation allowance depends on developer-token access level;
- individual services can impose stricter per-request or per-second limits.

The mutation best-practices documentation also describes larger special-case limits for some operation families and BatchJobService request/job sizing. Re-check current limits before implementing chunk sizes.

Never bake quota values into business logic without a versioned/configurable boundary.

## Error structure

Google Ads API errors include structured `GoogleAdsFailure` and `GoogleAdsError` details. Capture:
- error code;
- human-readable message;
- field/path location;
- trigger/details when present;
- request ID;
- customer and operation index context.

Official error guide:
https://developers.google.com/google-ads/api/docs/get-started/handle-errors

## Retry policy

Retry only failures that are transient according to the current documentation, such as selected resource-exhaustion/rate-limit or transport failures.

Use bounded exponential backoff with jitter. Respect server guidance when present.

Do not blindly retry:
- authentication/authorization failures;
- invalid fields or enums;
- policy/validation errors;
- quota configuration problems that require access changes;
- deterministic resource conflicts.

## Concurrent modification

Concurrent writes to the same campaign/account/resource family can produce concurrent-modification failures. Serialize conflicting mutations or use a partitioning key that prevents overlapping writers.

## Ambiguous outcomes

A timeout or transport failure after sending a mutation does not prove the server rejected it.

Before retrying an ambiguous create/update:
1. query for the intended resulting state using stable external keys, names, labels, or resource relationships;
2. determine whether the prior write committed;
3. retry only the missing delta.

Design create flows with idempotent reconciliation where the API does not provide a native idempotency key.

## Partial failure diagnostics

When partial failure is enabled:
- correlate each error with its operation index;
- distinguish failed operations from successful results;
- retain enough input metadata to replay only safe failures;
- do not replay successful siblings.

## Request sizing

Chunk by both operation count and payload/response size. Large GAQL responses should reduce selected fields, narrow the query, or use streaming rather than relying on maximum message limits.
