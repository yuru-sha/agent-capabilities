# Batch operations and local file mapping

verified_at: 2026-10-03

This reference covers application orchestration around YouTube APIs. These are not separate YouTube endpoints.

## Many videos and many channels

Normalize requested work into items that bind:

- local file identity;
- intended YouTube channel ID;
- credential profile;
- requested metadata/settings;
- operation type;
- deduplication key;
- current result state.

Support at least:

- one file -> one channel;
- many files -> one channel;
- one file -> many channels;
- many files -> many channels.

Do not let one failed item erase successful item state.

## Concurrency

Do not maximize concurrency blindly.

Bound concurrency using:

- available upload bandwidth;
- open-file/memory limits;
- quota availability;
- per-credential/channel operational behavior;
- retry pressure;
- application cancellation/deadline constraints.

A practical implementation can use global and channel/credential-specific semaphores/queues without embedding undocumented YouTube concurrency limits.

## Result normalization

Useful application-level states include:

- SUCCESS;
- SKIPPED_ALREADY_COMPLETED;
- RETRYABLE_FAILED;
- PERMANENT_FAILED;
- AMBIGUOUS_NEEDS_RECONCILIATION.

Keep raw YouTube error reason/status alongside normalized state.

## Local filename -> YouTube URL

YouTube does not expose a reliable universal "original local filename -> video" reverse lookup.

For deterministic lookup, persist an application mapping at upload time:

- original filename/path identity;
- optional stable local asset ID;
- optional file size/hash/fingerprint;
- channel ID;
- credential profile ID;
- YouTube video ID;
- canonical/watch URL;
- upload timestamp;
- upload/publish status;
- optional resumable session state while in progress.

Use video ID as the authoritative YouTube identity.

## Lookup priority

For a filename-to-URL request:

1. query the persistent upload mapping;
2. narrow by intended channel when available;
3. if mapping is missing, use application metadata/fingerprint/history to find candidates;
4. only then query YouTube resources/search as a fallback;
5. compare title, description markers, upload time, channel, and other known metadata;
6. return ambiguity instead of guessing when multiple candidates remain.

A YouTube title is not a local filename identity.

## Fingerprints

A content hash can strengthen deduplication, but full hashing of very large videos can be expensive.

Prefer an existing stable asset ID or previously computed hash. Compute a new full hash only when the product requires content-level identity.

Do not treat filename + mtime alone as collision-proof.

## Idempotency

Before starting a new upload for a batch item:

- check persistent completion mapping;
- reconcile ambiguous prior attempts;
- verify whether retrying could create a duplicate;
- only then create a new resumable session.
