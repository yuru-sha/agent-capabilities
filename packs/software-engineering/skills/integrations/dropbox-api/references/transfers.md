# File transfers

verified_at: 2026-10-03

## Transfer selection

Use the current endpoint limits from the HTTP reference. As a design rule:

- use simple upload when the payload comfortably fits the endpoint's current limit and retry requirements;
- use upload sessions for large, chunked, resumable, or retry-sensitive uploads;
- stream downloads to the consumer or a temporary file.

Never make the implementation depend on a remembered size threshold. Verify it.

## Upload sessions

The protocol is:

1. start an upload session;
2. append one or more chunks with the exact committed offset;
3. finish the session with the final cursor and commit info.

Implementation requirements:

- read chunks from a stream/file instead of buffering the full object;
- track the session ID and committed offset as opaque server state;
- on offset disagreement, reconcile with the server response instead of blindly advancing;
- bound chunk size and memory use;
- bound retries;
- persist resumable state only if the product actually supports cross-process resume;
- avoid concurrent appends to one session unless the current documented mode explicitly supports the intended behavior;
- use batch-finish APIs when many completed sessions can be committed together and the current API supports it.

## Ambiguous upload failure

After a timeout or connection loss, do not assume the final write failed. For
non-idempotent or session-finishing operations, inspect server state or session
offset/metadata before retrying.

## Downloads

Preferred pattern:

1. open destination stream or temporary file;
2. stream response bytes;
3. verify expected length where available;
4. verify Dropbox content_hash when appropriate and implemented correctly;
5. fsync/close as required by the host;
6. atomically replace/rename the final local destination when local durability matters.

A failed download should not leave a partially written file at the final path.

## Integrity

Dropbox `content_hash` is Dropbox-specific; do not substitute a normal
single-pass SHA-256 over the entire file and call it equivalent. Implement the
published Dropbox content-hash algorithm exactly when validation is required.

## Backpressure and cancellation

The target language implementation should support:

- streaming backpressure;
- cancellation/timeouts;
- bounded buffers;
- explicit cleanup of partial temporary files or abandoned local resources.
