# YouTube Reporting API

verified_at: 2026-10-03

Use Reporting for scheduled bulk Analytics datasets.

## Core flow

1. `reportTypes.list` to discover report types available to the authorized channel/content owner.
2. `jobs.create` to schedule generation of the selected report type.
3. `jobs.reports.list` to enumerate generated report instances.
4. Read each report's `downloadUrl`.
5. Send an authorized GET and stream the report to storage/processing.
6. Persist report/job IDs and covered time ranges so ingestion is incremental and deduplicated.

Jobs are scheduled report generators, not immediate synchronous query requests.

## Download handling

Reports can be large.

- stream downloads;
- use gzip when current documentation supports it;
- process incrementally rather than building a whole CSV/string in memory;
- store checksum/size/report ID metadata when useful;
- make ingestion idempotent.

Treat download URLs as sensitive and short-lived/authorization-bound data; do not log them unnecessarily.

## Historical data

Current documentation describes historical report generation when a new job is created, including a bounded period before job creation. Verify the current retention/window rather than hard-coding it.

## Backfill data

A backfill report replaces previously delivered data for the same period.

When a new report covers the same `startTime`/`endTime` as an already-ingested report:

- identify it as replacement data;
- replace/reconcile the earlier dataset for that period;
- do not append both as if they were independent daily facts.

## Job lifecycle

Track:

- reportTypeId;
- job ID;
- create/expire state;
- last downloaded report;
- covered time range;
- ingestion status.

If a job stops generating reports or expires, inspect the current API state before recreating it.

## Authorization

Reporting requires OAuth and uses Analytics-related scopes. Monetary reports require the current monetary-read scope and access rights.

## Reporting versus Analytics

Reporting is optimized for recurring bulk extraction with predefined report schemas. Analytics is optimized for custom on-demand queries.
