# Reporting

TikTok Reporting API supports synchronous and asynchronous report workflows.

Use synchronous reporting for bounded queries that fit the current endpoint limits. Use asynchronous reporting for larger exports or workflows where the API recommends task creation and download.

## Resolve before querying

- advertiser(s);
- report type;
- data level;
- dimensions;
- metrics;
- date range and timezone semantics;
- attribution settings;
- filters;
- sorting;
- pagination;
- sync vs async mode;
- output/download format.

Do not assume arbitrary dimensions and metrics can be combined. Validate supported dimension/metric/filter combinations from the current report type reference.

## Async workflow

Model async reporting as:

create task -> poll task status -> download output -> persist/stream result -> cancel only when needed

Use bounded polling with backoff and cancellation. Stream downloaded results.

## Data latency

TikTok documents both real-time and offline reporting data. Real-time values can be adjusted later, while offline data is refreshed differently.

Do not treat a freshly queried value as immutable. Record retrieval time and report date window, and design reconciliation where downstream decisions require stable numbers.

TikTok explicitly notes that Reporting API data is intended for reporting; use a more appropriate API such as Automated Rules for automated-control use cases when available.
