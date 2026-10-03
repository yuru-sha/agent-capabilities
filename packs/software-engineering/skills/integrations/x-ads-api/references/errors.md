# Error handling

verified_at: 2026-10-03

Error handling must distinguish whether a request was rejected, partially
processed, accepted asynchronously, or completed with a later processing
failure.

## Error classes

Classify at least:

- authentication/signature;
- authorization/account access;
- invalid resource or ownership;
- validation/schema/enum;
- targeting incompatibility;
- schedule/timezone;
- currency/budget/funding;
- rate limit;
- media upload/processing;
- creative approval/review;
- async analytics job;
- transient network/server;
- destructive or non-idempotent write with unknown outcome.

## HTTP and structured errors

Use both HTTP status and the current structured error payload when available.

Do not assume every failure returns the same JSON schema. Preserve:

- HTTP status;
- documented error code;
- human-readable message;
- parameter/field information when present;
- request/correlation ID when returned;
- retry/reset metadata.

Never log credential-bearing request data.

## Retryability

Retry only after classifying the failure.

Typically retryable with bounds:

- rate limit after reset;
- selected transport failures for idempotent reads;
- selected transient 5xx responses;
- non-terminal media/report processing states.

Typically not retryable without changing state/request:

- invalid enum or parameter;
- permission failure;
- unsupported advertising type/product combination;
- invalid media format/category;
- funding/budget constraint;
- terminal media-processing failure;
- terminal async-report failure.

## Ambiguous writes

For POST/PUT/DELETE timeouts or connection loss:

1. do not assume failure;
2. read back the target resource/association;
3. determine whether the intended mutation already occurred;
4. retry only when current API semantics make that safe.

This is especially important for resource creation, association creation, and
destructive operations.

## Validation errors as freshness signals

An unexpected 4xx validation failure can indicate stale local knowledge.

If a documented request previously expected to be valid fails because of:

- unknown/removed enum;
- changed required parameter;
- changed resource relationship;
- media requirement change;
- metric/dimension incompatibility;

re-open the current official endpoint documentation before modifying code.

## User-facing diagnostics

Report:

- which resource/action failed;
- whether anything was mutated;
- whether retry is safe;
- what prerequisite is missing or invalid;
- whether the failure suggests documentation revalidation.

Avoid collapsing all API errors into "X Ads request failed".
