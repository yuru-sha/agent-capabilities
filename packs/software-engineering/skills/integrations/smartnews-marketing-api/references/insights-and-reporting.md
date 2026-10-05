# Insights and reporting

Use:

`GET /api/ma/v3/ad_accounts/{ad_account_id}/insights/{layer}`

for Campaign, AdGroup, or Ad reporting.

Resolve explicitly: layer, target IDs when needed, date/time range, fields,
metrics, breakdowns, page size/page, response format, and supported sorting/filtering.

The caller must explicitly request fields. Do not assume default metric sets.

## JSON and CSV

Insights v3 supports `application/json` and `text/csv`.

JSON includes pagination metadata. CSV does not expose the pagination summary.
For multi-page CSV export, set `remove_csv_header=true` after page 1 and
continue until an empty page is returned.

## Breakdown changes

As of September 2026, `target_ids` is optional for breakdown requests and the
general maximum-size restriction was removed; hourly breakdowns remain limited
to 5 IDs. Re-check this rule before implementing hourly reports.

## Large exports

Stream response bodies and incrementally parse/write rows.
