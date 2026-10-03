# YouTube Analytics API

verified_at: 2026-10-03

Use Analytics for targeted, interactive queries over authorized channel/content-owner performance data.

## Query model

The core reports query is defined by:

- ids: channel or content-owner scope;
- startDate;
- endDate;
- metrics;
- optional dimensions;
- optional filters;
- optional sort;
- optional row pagination parameters;
- optional currency for supported monetary metrics.

Treat the valid combinations of metrics, dimensions, and filters as a schema that must be verified against the current report documentation.

## Metrics, dimensions, filters

- Metrics are measurements such as views or engagement/revenue measures.
- Dimensions group results, such as day, country, video, device, traffic source, or demographic categories.
- Filters restrict the dataset by supported dimension values.
- Sorting can use dimensions/metrics supported by the query; a leading `-` indicates descending order.

Do not invent a metric/dimension combination because each name exists independently.

## Example intent translation

Intent: "top videos by views for the last 30 days"

Conceptual query:

- ids: authenticated channel;
- dimensions: `video`;
- metrics: `views`;
- date range: last 30 complete/desired days;
- sort: `-views`;
- optional maxResults.

Resolve video IDs to titles with the Data API only if the output actually needs titles.

## Authorization

Analytics requires OAuth. Verify the current required YouTube/Analytics scopes for the chosen query, especially when monetary data is requested.

## Groups

Analytics groups can aggregate supported resource IDs. Use them when they materially simplify repeated analysis, but do not create persistent groups merely for one query if direct filters are sufficient.

## Date/data availability

Recent days may be incomplete or omitted depending on the report. Do not interpret absent recent rows as zero without checking the report semantics.

Preserve "no row", zero, null, and unavailable/deprecated metric states distinctly.

## Analytics versus Reporting

Choose Analytics when the caller needs ad-hoc, filtered, sorted, targeted answers.

Choose Reporting when the system needs recurring bulk datasets for storage/ETL/warehouse processing.
