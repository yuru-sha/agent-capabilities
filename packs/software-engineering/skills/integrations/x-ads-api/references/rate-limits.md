# Rate limits and concurrency

verified_at: 2026-10-03

Rate limits vary by endpoint family and scope. Do not implement one global
requests-per-second constant.

## Rate-limit scopes

At verification time, X documents user-token and Ads-account rate-limit headers.
When returned, distinguish:

User scope:

- `x-rate-limit-limit`;
- `x-rate-limit-remaining`;
- `x-rate-limit-reset`.

Ads-account scope:

- `x-account-rate-limit-limit`;
- `x-account-rate-limit-remaining`;
- `x-account-rate-limit-reset`.

Prefer account-level capacity for eligible account-scoped reads when the server
returns it, but do not assume those headers exist for every endpoint or write.

## Adaptive concurrency

Concurrency should respond to:

- remaining capacity;
- reset time;
- endpoint latency;
- async-job limits;
- downstream processing capacity.

Use bounded concurrency. Reduce or stop new work as capacity approaches zero.

## 429 handling

On rate-limit responses:

1. identify the applicable scope;
2. use the returned reset/retry information;
3. pause the affected scope rather than unrelated accounts when possible;
4. resume with bounded jitter to avoid a synchronized retry burst.

Do not retry immediately in a tight loop.

## Analytics

Current Analytics documentation has dedicated sync request limits and an
account-scoped maximum for concurrently processing async jobs. Re-check those
values before implementation and enforce both submission and polling budgets.

## Request reduction

Prefer supported API capabilities that reduce calls:

- multi-ID filters;
- larger but reasonable page sizes;
- reusable cached lookup/reference data;
- async reports for large historical ranges;
- avoiding repeated reads of immutable/static metadata inside loops.

Caching must still respect freshness and mutation visibility requirements.
