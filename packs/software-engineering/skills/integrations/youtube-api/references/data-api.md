# YouTube Data API v3

verified_at: 2026-10-03

Use the Data API for ordinary YouTube resources and mutations.

## Core resource families

Common resource families include:

- videos;
- channels;
- search;
- playlists;
- playlistItems;
- commentThreads and comments;
- captions;
- thumbnails;
- subscriptions;
- activities;
- channelSections;
- videoCategories;
- memberships/members where the authenticated channel and current API support them.

This list is an intent index, not a substitute for the current method reference.

## Resource parts

Many methods require or support `part`.

Treat `part` as part of the wire contract:

- request only the resource parts needed for the operation;
- for update/insert methods, include the parts that contain properties being written;
- do not assume omitted properties are preserved unless the method's update semantics say so;
- combine `part` with `fields`/partial response when useful to reduce payload.

## Efficient video/channel lookup

For a known video ID, prefer `videos.list` over `search.list`.

For a known channel ID, use `channels.list` with a specific filter rather than broad search.

For "all uploads from a channel", prefer the channel's uploads playlist and traverse `playlistItems.list` rather than repeatedly searching the global index.

Use `search.list` when actual search semantics are required, then follow returned IDs with the resource-specific list method when richer metadata is needed.

## Videos

Use current `videos` methods for:

- metadata/statistics/content details retrieval;
- upload/insert;
- metadata/status updates;
- deletion;
- ratings/report-abuse where supported.

Do not confuse basic Data API statistics with Analytics API metrics.

## Playlists

Keep playlist identity and playlist-item identity separate.

A playlist item is the membership/position of a video in a playlist; removing/reordering an item is not the same operation as deleting the underlying video.

## Comments and moderation

Distinguish:

- comment threads/top-level comments;
- individual comments/replies;
- retrieval;
- replies;
- moderation status changes;
- deletion.

Check whether comments are disabled and whether the authenticated channel owns or moderates the relevant resource before mutating.

## Captions and thumbnails

Caption tracks and thumbnails have media-transfer semantics distinct from ordinary JSON-only metadata updates. Verify current upload format, scopes, and method-specific restrictions.

## Search caveat

Search results are discovery candidates, not proof of local-file identity. If a product needs to resolve a local filename to a previously uploaded video, use persistent upload mapping first; see [batch-and-file-mapping.md](batch-and-file-mapping.md).
