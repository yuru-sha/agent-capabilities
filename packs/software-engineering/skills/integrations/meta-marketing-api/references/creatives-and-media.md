# Creatives and media

verified_at: 2026-10-03

## Separate layers

Distinguish:

1. source file or remote asset;
2. Ad Account image/video upload and processing;
3. Ad Creative specification;
4. Page/Instagram/WhatsApp identity;
5. Ad that references the Creative.

This prevents duplicate uploads and makes retries and reuse safer.

## Media reuse and upload

Prefer reusing compatible existing image hashes/video IDs when the user's intent
is to reuse the same asset.

For large media:

- stream from disk or object storage;
- avoid reading the whole file into memory;
- use current resumable/upload-session behavior where Meta requires or recommends it;
- persist upload/session identifiers when supported;
- poll processing state with bounded backoff;
- do not create delivery objects that depend on media before required processing completes.

## Creative specifications

Current creative payloads can involve story specs, link/video data, asset-feed
or dynamic structures, catalog/product data, call-to-action specs, and
placement-specific identity fields.

Never copy an old `object_story_spec` or `asset_feed_spec` shape blindly.
Verify current fields for the objective, destination, placement, Page,
Instagram account, and API version.

## Dynamic and automated creative

Dynamic creative, Advantage-family creative, catalog creative, flexible formats,
and placement customization evolve frequently. Resolve the current supported
creative object and constraints from official docs before implementation.

## Preview and review

Use current preview/rendering APIs where available before activation.

A technically valid creative can still be rejected, limited, or unable to
deliver due to policy, identity, destination, media processing, or account state.
