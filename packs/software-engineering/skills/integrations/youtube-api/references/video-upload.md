# Video upload and publishing

verified_at: 2026-10-03

## Endpoint and authorization

Use the current `videos.insert` upload endpoint and verify the accepted OAuth scopes and upload quota behavior before implementation.

Google currently documents a dedicated Video Uploads quota bucket for `videos.insert`; do not hard-code current daily allocations into application correctness.

## Resumable upload

Prefer resumable upload for large files, unstable networks, long-running transfers, or any workflow where restarting from byte zero is expensive.

Protocol shape:

1. initiate a resumable session with metadata and the required `part`;
2. capture the `Location` upload-session URL;
3. stream bytes with `PUT`, using the required content headers/ranges;
4. on interruption, query session status;
5. use the server's `Range`/status response to determine the next byte;
6. resume until the server returns the created video resource.

Treat the session URL as sensitive capability-like state and as opaque.

Official guidance currently calls out 500, 502, 503, and 504 as resumable-upload retry candidates and recommends exponential backoff; honor `Retry-After` when present.

## Memory and I/O

- Never read the entire video into memory for ordinary uploads.
- Stream from file/reader to the HTTP body.
- Use bounded chunks when chunked upload is needed.
- Make chunk size configurable and avoid an undocumented "optimal" constant.
- Support cancellation and deadlines.
- Persist resumable session state only when cross-process resume is a product requirement.

## Metadata and publication

Validate current fields before setting:

- title;
- description;
- tags;
- category;
- privacy status;
- publish/schedule timing;
- audience/made-for-kids flags where applicable;
- recording/location/language metadata when relevant.

Do not silently default privacy to public.

Scheduled publication has eligibility and field constraints; confirm the current `status` contract before relying on it.

## Post-upload operations

Thumbnail, caption, playlist insertion, comment settings, or other follow-up steps are separate API operations.

Model them as independent steps with their own retry/result state instead of treating "video bytes uploaded" as proof the entire publishing workflow completed.

## Upload verification

After success:

- persist the returned video ID;
- construct/store the canonical watch URL only from the returned ID;
- read the video back when metadata/privacy/scheduling correctness matters;
- record channel ID and credential context;
- persist local-file mapping when future reverse lookup is required.

If upload completion is ambiguous after a transport failure, do not automatically start a new upload. Query the resumable session or reconcile recent channel videos and local mapping before deciding whether a retry would create a duplicate.
