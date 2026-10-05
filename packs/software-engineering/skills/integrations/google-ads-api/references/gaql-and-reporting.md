# GAQL and reporting

## Query model

Google Ads Query Language (GAQL) is the primary query language for resource reads and performance reporting.

A query selects fields from one primary resource:

```text
SELECT
  campaign.id,
  campaign.name,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros
FROM campaign
WHERE segments.date BETWEEN '2026-09-01' AND '2026-09-30'
ORDER BY campaign.id
```

Do not assume every attribute, segment, and metric is compatible with every `FROM` resource. Validate fields against the versioned Google Ads Fields reference or Query Builder.

Official reporting overview:
https://developers.google.com/google-ads/api/docs/reporting/overview

## Search versus SearchStream

Use `GoogleAdsService.Search` when explicit pagination and page-by-page processing are useful.

Use `GoogleAdsService.SearchStream` when streaming the result set over one response is operationally simpler and response sizing is safe.

Do not load arbitrarily large reports into memory. Process rows incrementally, write checkpoints where appropriate, and bound downstream buffers.

## Pagination and result completeness

For `Search`:
- follow returned page tokens until exhausted;
- preserve the exact GAQL and customer context across pages;
- do not parallelize page tokens unless the API contract explicitly permits it.

For streaming:
- handle stream interruption and decide whether restart-from-query is safe;
- avoid duplicate downstream effects by making result ingestion idempotent.

## Reporting contract

Before running a performance report, define:
- target customer(s);
- API version;
- primary `FROM` resource;
- attributes;
- metrics;
- segments/breakdowns;
- date range;
- account timezone;
- currency and micros conversion;
- conversion/action definitions;
- attribution interpretation where relevant;
- filters and sort;
- output schema and destination.

Persist enough metadata to reproduce the report.

## Time and money

Dates and daily segmentation follow Google Ads account/report semantics, not necessarily the executor's local timezone. Record the account timezone when daily boundaries matter.

Many monetary fields are expressed in micros. Preserve integer micros during computation where possible and convert for presentation only with an explicit currency.

## Multi-account reporting

Manager accounts do not imply that one arbitrary query returns every child account's report rows. Resolve accessible customers and query each intended customer according to the current API contract.

Bound concurrency to quota and service limits, and keep customer identity attached to every result row or output partition.

## Zero rows and segmentation

Adding segments can change row cardinality and metric interpretation. Zero-metric behavior and incompatible segmentation can also affect results. Treat a changed GAQL shape as a different report contract, not a cosmetic modification.
