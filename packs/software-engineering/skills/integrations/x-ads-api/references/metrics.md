# Reporting metrics and dimensions

verified_at: 2026-10-03

Always verify metric/entity compatibility against the current official Metrics
and Segmentation documentation before querying.

## Current metric groups

At verification time the Analytics documentation includes these metric groups:

- `ENGAGEMENT`;
- `BILLING`;
- `VIDEO`;
- `WEB_CONVERSION`;
- `MOBILE_CONVERSION`;
- `LIFE_TIME_VALUE_MOBILE_CONVERSION`.

Do not assume every entity level, objective, product, or placement supports every
group.

## Common measurement concepts

Typical user intents map to metrics in these families:

- impressions;
- engagements;
- clicks and click subtypes;
- spend / billed charge;
- video starts/views/completions and related video engagement;
- web conversions;
- mobile conversions;
- lifetime-value mobile conversion metrics.

Use the exact current API field names from the official table at implementation
time.

## Derived metrics

For derived values such as CTR, CPC, CPM, engagement rate, or conversion rate:

1. identify the raw numerator and denominator exposed by the current API;
2. verify they are available for the same entity level, placement, time range,
   and segmentation;
3. calculate the derived value in the reporting layer;
4. document denominator-zero behavior explicitly.

Do not request a synthetic field from X merely because the UI displays it.

## Dimensions and segmentation

Segmentation availability is tied to asynchronous analytics and to current
entity/metric compatibility.

Before requesting segmentation:

- verify the requested dimension is supported;
- verify async reporting is required/allowed;
- verify the reduced segmented date-range limit;
- confirm whether the metric group is compatible with the segmentation;
- determine whether separate placement queries are required.

## Missing-value semantics

Preserve the distinction among:

- numeric `0`;
- JSON `null`;
- missing field;
- empty result/no row.

Normalize only after the API semantics are understood.

## Creative-level reporting

The current Analytics history documents `MEDIA_CREATIVE` support, while the
core Metrics and Segmentation table prominently documents
`ACCOUNT`, `FUNDING_INSTRUMENT`, `CAMPAIGN`, `LINE_ITEM`, and
`PROMOTED_TWEET`.

Therefore a request such as "Creative-level CTR" must trigger a current
entity-level check before constructing the query. Do not silently substitute
`PROMOTED_TWEET` or another entity level.
