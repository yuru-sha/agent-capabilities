# Representative workflows

verified_at: 2026-10-03

These recipes are examples, not scope limits.

## Resolve video URL from local filename

1. Read the application's persistent local-file -> channel -> video-ID mapping.
2. If exactly one mapping matches, return a URL derived from the stored video ID.
3. If multiple mappings match, narrow by channel/credential/time or return ambiguity.
4. If mapping is absent, inspect local asset metadata/history.
5. Only as fallback, retrieve/search candidate YouTube videos for the intended channel.
6. Compare title/known description markers/upload time/channel and other available metadata.
7. Never silently choose among multiple plausible candidates.

See [batch-and-file-mapping.md](batch-and-file-mapping.md).

## Upload one video to a specified channel

1. Resolve credential profile -> authenticated channel ID.
2. Confirm it equals the requested target channel.
3. Validate upload metadata/privacy/scheduling fields.
4. Create a resumable upload session.
5. Stream the video with bounded memory and resume on documented transient failures.
6. Persist returned video ID and local-file mapping.
7. Read the video back when privacy/schedule/metadata correctness matters.
8. Run thumbnail/caption/playlist follow-up steps independently.

## Upload many videos to many channels

1. Normalize all source files and targets into independent work items.
2. Resolve credentials/scopes/channel ID for every target before transferring bytes.
3. Check prior completion/ambiguous state for deduplication.
4. Queue items with bounded global and per-credential/channel concurrency.
5. Start/resume uploads independently.
6. Persist success immediately per item.
7. Retry only retryable item failures.
8. Return a per-item result summary without rolling back unrelated successes.

## Search videos then fetch details

1. Use `search.list` only when discovery semantics are required.
2. Collect candidate video IDs.
3. Use `videos.list` for the exact resource parts needed.
4. Stop when sufficient results are available.

## List a channel's uploaded videos

1. Resolve the channel.
2. Get its uploads playlist ID from the channel resource.
3. Traverse `playlistItems.list`.
4. Fetch detailed video fields only when needed.

## Query top videos by Analytics metric

1. Resolve authorized channel/content-owner scope.
2. Choose date range.
3. Verify metric/dimension compatibility.
4. Query Analytics with `dimensions=video`, desired metric(s), and sort.
5. Join video IDs to Data API metadata only if human-readable video fields are needed.

## Ingest bulk Reporting data

1. Discover available report types.
2. Create/reuse the desired reporting job.
3. List generated reports.
4. Skip report IDs already ingested unless a backfill/replacement requires reconciliation.
5. Stream each report download.
6. Atomically mark the report/time range ingested.
7. Replace prior period data when the API provides a backfill report.

## Create and start a live broadcast

1. Create the broadcast with explicit schedule/privacy.
2. Create or reuse a compatible live stream.
3. Bind broadcast to stream.
4. Configure encoder from the stream ingestion settings.
5. Wait for/verify active stream health/status.
6. Transition to testing when desired/supported.
7. Transition to live only with explicit intent.
8. Monitor state and complete/end according to current rules.

## Moderate live chat

1. Resolve broadcast/live chat identity.
2. Retrieve messages with the documented continuation/polling behavior.
3. Identify the exact target user/message.
4. Apply the narrowest supported moderation action.
5. Verify resulting state when security/community correctness matters.
