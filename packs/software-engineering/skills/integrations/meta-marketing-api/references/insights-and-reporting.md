# Ads Insights and reporting

verified_at: 2026-10-03

## Translate intent into a report plan

For requests such as "yesterday by campaign", "spend by ad", "ROAS by placement",
or "weekly conversions by age/gender", derive and validate:

- Ad Account/object scope;
- `level` (account/campaign/adset/ad or current supported level);
- date range / date preset;
- account timezone;
- `time_increment`;
- fields;
- breakdowns and action breakdowns;
- attribution setting / action report time;
- filtering;
- sorting;
- pagination;
- synchronous vs asynchronous retrieval.

## Fields and actions

Do not assume all historical fields remain available or combinable. Verify the
current Insights field reference for delivery, click, cost, spend, action,
conversion-value, video, engagement, quality/ranking, and objective-specific metrics.

Preserve action type keys and attribution semantics. Do not flatten every
`actions` entry into one generic conversion count.

## Breakdowns

Breakdowns can multiply result cardinality dramatically and many combinations
are restricted. Validate current compatibility for age, gender, geography,
publisher/platform/placement/device, product, hourly/time, and other dimensions.

## Attribution and time semantics

Explicitly record:

- account timezone;
- date range;
- attribution windows/settings;
- impression-time vs conversion-time semantics where configurable;
- current data freshness and modeled/delayed conversion behavior.

This is required for correct comparison with Ads Manager exports.

## Async Insights

Prefer asynchronous reporting for large date ranges, many fields/breakdowns,
high-cardinality queries, exports, or recurring ETL.

General pattern:

`create async report -> store report_run_id -> poll -> fetch paginated result -> stream/process -> checkpoint`

Do not busy-wait. Use bounded polling with jitter and persist job IDs across restarts.

## Pagination and memory

Process result pages incrementally. Do not concatenate an unbounded Insights
export into one in-memory array unless the expected result size is provably small.

Preserve null, zero, missing, and unavailable values distinctly in raw ingestion.
Normalize only in an explicit analytics layer.
