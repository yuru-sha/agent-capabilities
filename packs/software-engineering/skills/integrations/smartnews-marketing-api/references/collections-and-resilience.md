# Collections and resilience

## Pagination

Marketing API v3 collection endpoints for Insights, Campaigns, AdGroups, and Ads
use `page_size` and `page`.

For JSON, start at page 1 and follow pagination metadata. For CSV Insights,
pagination metadata is absent; continue until no rows are returned.

## Rate limits

Current documented limits per developer app:

- 10 GET requests/second;
- 10 POST/PATCH/DELETE requests/second;
- 5 OAuth token requests/minute.

These limits may change. Implement behavior based on actual `429` responses.

## Retry policy

Retry transient `429`, `500`, and `503` responses with bounded exponential
backoff and jitter. Respect server retry metadata when present.

Do not automatically retry ambiguous non-idempotent writes after a connection
failure. Reconcile state first.

## Error classes

Handle 400, 401, 403, 404, 409, 410, 429, 500, and 503 distinctly. Error
payloads may expose a message, type, field validation detail, and `retriable`
signal. Capture diagnostics without leaking secrets or customer data.
