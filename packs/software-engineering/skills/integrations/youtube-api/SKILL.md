---
name: youtube-api
description: Use when researching, designing, implementing, reviewing, or maintaining YouTube integrations across Data API v3, video uploads, channels, playlists, comments, captions, Analytics, Reporting, and Live Streaming in any programming language.
---

# YouTube API

Use this Skill to translate YouTube product intent into current official API behavior without depending on a specific programming language or assuming remembered quota, scope, endpoint, metric, or upload behavior is still current.

## Non-negotiable principles

- Official Google/YouTube developer documentation is the source of truth.
- Treat YouTube Data API v3, YouTube Analytics API, YouTube Reporting API, and YouTube Live Streaming API as related but distinct API surfaces.
- Never assume remembered quota costs, limits, scopes, fields, metrics, dimensions, or live-state rules are current.
- Cross-reference official Google API client libraries and samples in multiple languages when useful, but extract protocol semantics rather than copying SDK architecture.
- Request the minimum OAuth scopes required by the operation.
- Use API keys only for operations that actually support unauthenticated/public-data access; use OAuth 2.0 for private data and mutations.
- Resolve the authenticated channel identity before channel-scoped mutations.
- Request only required resource parts/fields and avoid unnecessary collection scans.
- Stream media and report downloads; do not load large files entirely into memory.
- Prefer resumable video upload for large or failure-sensitive transfers.
- Treat quota exhaustion, rate limiting, authorization failure, validation failure, and transient server failure as different conditions.
- Do not retry ambiguous mutations blindly after a timeout; reconcile server state first.
- Preserve opaque IDs, page tokens, upload-session URLs, report IDs, and live resource IDs exactly.

## Freshness gate

The local references record `verified_at: 2026-10-03` and use a 30-day freshness threshold. Re-check official YouTube documentation before implementation when verification is older than 30 days.

Re-check even inside 30 days when:

- an endpoint, scope, quota bucket/cost, field, metric, dimension, report type, live-state transition, or error reason is unknown;
- a Google client library/sample disagrees with the REST reference;
- an unexpected 4xx suggests the contract changed;
- a quota or upload restriction materially affects architecture;
- a deprecated metric/dimension/resource is encountered.

Read [references/current-api.md](references/current-api.md) first.

## API selection workflow

1. Parse intent: public lookup, authenticated channel operation, upload/publishing, analytics, bulk reporting, or live streaming.
2. Pass the freshness gate and choose the API surface:
   - Data API v3 for videos, channels, playlists, search, comments, captions, subscriptions, thumbnails, and ordinary metadata mutations;
   - Analytics API for targeted, interactive metric queries;
   - Reporting API for scheduled bulk report generation and download;
   - Live Streaming API for broadcasts, streams, live chat, moderation, and related live resources.
3. Resolve credentials, scopes, and channel identity using [references/authentication-and-channels.md](references/authentication-and-channels.md).
4. Resolve endpoint/resource behavior using [references/data-api.md](references/data-api.md), [references/analytics.md](references/analytics.md), [references/reporting.md](references/reporting.md), or [references/live-streaming.md](references/live-streaming.md).
5. For uploads, use [references/video-upload.md](references/video-upload.md).
6. For collections and query construction, use [references/collections-and-querying.md](references/collections-and-querying.md).
7. For batches, multi-channel work, and local file correlation, use [references/batch-and-file-mapping.md](references/batch-and-file-mapping.md).
8. Apply quota, retry, and error rules from [references/resilience.md](references/resilience.md).
9. Use [references/workflows.md](references/workflows.md) for representative end-to-end recipes.
10. After a mutation, read back the resulting resource when correctness depends on final server state.

## Language-independent implementation guidance

Implement the wire contract idiomatically in the target language.

Official Google API client libraries and samples are useful for OAuth, resumable upload, pagination, request construction, media streaming, error decoding, and generated resource types. They are implementation references, not authority over newer REST documentation.

When the target language lacks a suitable client library:

- use a mature OAuth 2.0 implementation;
- implement REST requests directly from the current reference;
- stream upload/download bodies;
- preserve `part`, `fields`, filters, page tokens, and opaque IDs exactly;
- represent method-specific error reasons explicitly;
- make cancellation/timeouts and bounded retries first-class;
- keep YouTube-specific transport/resource rules separate from application/domain adapters.

## Mutation safety

- Never log access tokens, refresh tokens, client secrets, authorization codes, upload-session URLs, or private report URLs.
- Resolve the intended channel before upload/update/delete operations.
- Do not assume an authenticated Google account maps to only one YouTube channel.
- Do not broaden privacy, visibility, moderation, or audience settings unless requested.
- Treat deletion, moderation bans, playlist removals, and live transitions as state-changing operations that require explicit intent.
- Do not replay an upload finalization or other ambiguous write until the current server state is understood.
- For multi-channel batches, isolate credentials and result state per channel and per item.
- Verify scheduling and publication state after writes when timing matters.

## Reference map

- [current-api.md](references/current-api.md): source priority, freshness policy, current API families, and official-library research.
- [authentication-and-channels.md](references/authentication-and-channels.md): API keys, OAuth 2.0, scopes, channel identity, token handling, and multi-channel credentials.
- [data-api.md](references/data-api.md): Data API resources, endpoint families, `part`, fields, search, playlists, comments, captions, thumbnails, and subscriptions.
- [video-upload.md](references/video-upload.md): video insert, resumable upload, streaming, metadata, publication, thumbnail/caption follow-up, and upload verification.
- [collections-and-querying.md](references/collections-and-querying.md): pagination, filtering, sorting, partial responses, page tokens, and efficient lookup patterns.
- [analytics.md](references/analytics.md): Analytics API query model, metrics, dimensions, filters, sort, groups, and date semantics.
- [reporting.md](references/reporting.md): report types, jobs, report download, incremental ingestion, historical/backfill data, and large-file handling.
- [live-streaming.md](references/live-streaming.md): broadcasts, streams, binding, transitions, stream health, live chat, moderators, bans, and related live resources.
- [batch-and-file-mapping.md](references/batch-and-file-mapping.md): many-item/many-channel orchestration, deduplication, local filename/video mapping, and result normalization.
- [resilience.md](references/resilience.md): quota buckets, rate limits, error reasons, retries, ambiguous writes, concurrency, and observability.
- [workflows.md](references/workflows.md): representative lookup, publishing, analytics, reporting, and live workflows.
