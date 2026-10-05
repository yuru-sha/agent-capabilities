# Reporting

Define the analytical question before exporting data.

## Report plan

Record:
- product: Search / Display Auction / Display Guaranteed;
- account;
- reporting level (campaign, ad group, ad, keyword, targeting, placement, etc.);
- date range and timezone;
- metrics and conversions;
- attribution/conversion definition;
- breakdown/dimensions;
- filters;
- output format;
- report generation time.

## Performance reports

Search Ads performance reports can be configured by hierarchy, fields, and aggregation period. Current LINE Ads documentation also distinguishes performance reports from Custom Reports (beta): performance reports reflect delivered-user attributes, while custom reports use configured targeting attributes.

For historical extraction, respect product retention limits. LINEヤフー announced that Search Ads performance report/data retrieval is limited to the 11 years preceding extraction.

## Comparability

When comparing periods across the 2026 LINE/Yahoo unification:
- keep product/account identifiers;
- preserve old product/placement names in raw data;
- map names only in a derived normalization layer;
- note discontinued placements and metric-definition changes;
- do not fill missing historical dimensions with zero.

For large downloads, stream/process incrementally where practical and retain the original export plus report-definition metadata.

Primary sources:
- https://www.lycbiz.com/jp/column/ly-ads/technique/performance_report/
- https://www.lycbiz.com/jp/manual/line-ads/other_003/
- https://www.lycbiz.com/jp/news/yahoo-ads/20250116/
