# Current YouTube APIs

verified_at: 2026-10-03
freshness_days: 30

## Source priority

Use sources in this order:

1. Official YouTube Data API v3 reference and guides:
   https://developers.google.com/youtube/v3
2. Official YouTube Analytics API reference:
   https://developers.google.com/youtube/analytics
3. Official YouTube Reporting API reference:
   https://developers.google.com/youtube/reporting
4. Official YouTube Live Streaming API reference:
   https://developers.google.com/youtube/v3/live
5. Official Google API client libraries and official samples.
6. Third-party material only when official material does not cover the question.

If a client library or sample conflicts with the current REST reference, follow the REST reference.

## API families

Keep these surfaces distinct:

- YouTube Data API v3: resource CRUD, search, metadata, comments, captions, playlists, uploads, thumbnails, subscriptions, and related ordinary channel/video operations.
- YouTube Analytics API: interactive queries over metrics/dimensions/filters/sort for authorized channel or content-owner data.
- YouTube Reporting API: scheduled bulk reports generated as downloadable files.
- YouTube Live Streaming API: broadcasts, streams, live chat, moderation, cuepoints, and live lifecycle operations.

Do not route an analytics intent through Data API statistics when the user requires Analytics dimensions/metrics, and do not use Analytics queries as a substitute for bulk Reporting jobs when the workload is designed for scheduled ingestion.

## Freshness rules

Re-verify after 30 days and sooner when:

- quota buckets, costs, daily allocations, or rate-limit behavior matter;
- a resource method or parameter differs from this Skill;
- an OAuth scope or authorization requirement changes;
- a metric/dimension/report type is deprecated or rejected;
- upload limits or resumable protocol behavior changes;
- live broadcast/stream states or transition prerequisites differ;
- a current official library exposes newer resource fields or methods.

Do not bake default quota allocations or upload limits into application correctness. Defaults and service policies can change.

## Official implementation research

Inspect official client libraries/samples across languages for protocol patterns such as:

- OAuth token refresh and installed/web application flows;
- resumable upload session creation and chunk resume;
- media streaming without whole-file buffering;
- generated request/resource types and `part` handling;
- page-token iteration;
- method-specific error decoding;
- Analytics query serialization;
- Reporting download streaming;
- live broadcast/stream polling and transitions.

Extract the protocol behavior, then implement it idiomatically in the target language.

## Verified official guide set

This Skill was checked against current official documentation for:

- Data API getting started and quota:
  https://developers.google.com/youtube/v3/getting-started
- Data API error catalog:
  https://developers.google.com/youtube/v3/docs/errors
- Resumable upload protocol:
  https://developers.google.com/youtube/v3/guides/using_resumable_upload_protocol
- Analytics API reports query:
  https://developers.google.com/youtube/analytics/reference/reports/query
- Reporting API REST reference:
  https://developers.google.com/youtube/reporting/v1/reference/rest
- Reporting bulk reports/backfill:
  https://developers.google.com/youtube/reporting/v1/reports
- Live Streaming API reference:
  https://developers.google.com/youtube/v3/live/docs
- Broadcast/stream implementation guide:
  https://developers.google.com/youtube/v3/live/guides/implementation/broadcasts-and-streams

Before implementing a concrete method, open its current reference and confirm scopes, parameters, `part`, request body, response fields, quota impact, and method-specific error reasons.
