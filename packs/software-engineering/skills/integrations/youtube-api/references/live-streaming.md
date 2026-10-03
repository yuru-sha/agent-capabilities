# YouTube Live Streaming API

verified_at: 2026-10-03

## Resource model

Keep these concepts separate:

- `liveBroadcast`: the viewer-facing scheduled/live event and its YouTube video identity;
- `liveStream`: ingest/transmission configuration used by an encoder;
- binding: association between a broadcast and a stream;
- live chat and moderation resources: communication state associated with an active/upcoming broadcast.

Do not model "a live stream" as one object.

## Typical lifecycle

1. create/schedule a broadcast with title, scheduled start, privacy, and supported settings;
2. create or reuse a stream with current CDN/ingestion settings;
3. bind the broadcast to the stream;
4. configure encoder ingestion using the returned stream ingestion information;
5. monitor stream health/status;
6. transition the broadcast through valid states such as testing/live as appropriate;
7. complete/end according to current broadcast rules;
8. verify final status/archive behavior.

Before `liveBroadcasts.transition`, verify the current prerequisite stream state. Official guidance currently instructs callers to confirm the bound stream is active before transitioning to testing/live.

## Reuse

A stream resource may be reusable across broadcasts when current API rules allow it. Do not create a new stream for every broadcast by default.

Similarly, do not delete a reusable stream when completing one broadcast unless the product explicitly wants it removed.

## Live chat

Current Live API resource families include operations for:

- reading/posting live chat messages;
- deleting/moderating messages where supported;
- moderators;
- bans;
- polls/transitions where supported;
- Super Chat/event data where authorized and available.

Use the current method reference because chat capabilities and fields can change independently of broadcast APIs.

## Polling and streaming behavior

Do not busy-loop.

- honor polling intervals returned/documented by the relevant method;
- use bounded retries;
- stop polling when the broadcast/chat reaches terminal state;
- preserve continuation/page tokens as opaque values.

## Safety

- Do not transition a broadcast live without explicit intent.
- Do not ban users or delete chat messages based on an ambiguous identity.
- Preserve privacy and audience settings unless the request explicitly changes them.
- Confirm stream/broadcast ownership before mutation.
