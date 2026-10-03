# Media upload and creative assets

verified_at: 2026-10-03

## Separate upload from account association

At verification time, the Creatives reference exposes account Media Library
resources at:

- `GET /12/accounts/:account_id/media_library`;
- `GET /12/accounts/:account_id/media_library/:media_key`;
- account association/create through `POST /12/accounts/:account_id/media_library`;
- update/delete on the media-key resource where documented.

The current Creatives reference also exposes Account Media reads/deletes for
supported creative types. Do not confuse raw upload, Media Library association,
Account Media, and line-item media-creative association: they are different
lifecycle steps.

## Bounded-memory implementation

Do not implement large uploads as:

```text
read whole file -> byte[] -> base64 copy -> multipart copy -> HTTP buffer
```

Prefer:

```text
filesystem/stream
  -> bounded buffer
  -> request body or upload chunk
  -> network
```

Use the target language's streaming request APIs, cancellation, connection
reuse, and bounded buffers. Avoid retaining successful chunks after the server
has acknowledged them.

## Chunked video uploads

The current Campaign Management guide explicitly describes chunked video upload
for promoted/in-stream video and the sequence:

```text
INIT
 -> APPEND chunk 0
 -> APPEND chunk 1
 -> ...
 -> FINALIZE
 -> STATUS polling
```

The guide requires `media_category=amplify_video` for pre-roll/in-stream
assets and says to continue only after STATUS reports successful processing.
Re-check the current media-upload documentation for host, parameters, maximum
size, chunk-size constraints, supported categories, and processing states before
implementation.

Do not assume that every image/GIF/video uses the same upload path or media
category.

## Retry and processing rules

- Retry only chunks or reads whose semantics are known to be safe.
- After a timeout on FINALIZE or another ambiguous write, query processing/state
  before reissuing the write.
- Honor server retry/rate-limit guidance.
- Poll STATUS with a bounded interval/backoff and an overall deadline.
- Distinguish transport failure from media-processing failure.
- Surface non-retryable format, duration, dimension, category, permission, and
  validation failures without blind retries.
- Verify the returned `media_key` is associated with the intended Ads account
  before creating a Card/Post/media-creative association.

For bulk asset workflows, process files incrementally and cap concurrent
uploads; avoid opening or buffering the entire batch at once.
