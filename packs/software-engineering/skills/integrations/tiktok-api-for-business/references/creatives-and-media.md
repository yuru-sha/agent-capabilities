# Creatives and media

TikTok API for Business includes creative-asset operations for images, videos, music, playables, instant pages, calls to action, cards, stickers, interactive/premium add-ons, and related creative tooling.

## Rules

- Verify format, size, duration, aspect ratio, checksum/hash, and processing requirements from the current endpoint reference before upload.
- Reuse an existing compatible asset when it is clearly the intended asset.
- Stream large files from disk/network source instead of reading them fully into memory.
- Preserve cancellation and upload timeouts.
- After upload, poll or read processing state when the workflow requires server-side processing before ad creation.
- Do not assume upload success means the asset is immediately eligible for delivery.

## Spark Ads and identity

Spark Ads depend on identity/authorization behavior that differs from ordinary uploaded creative.

Resolve:

- identity type;
- authorization/permission;
- post/video reference;
- migration requirements for existing Spark Ads;
- ad-format compatibility

before creating the ad.

## Smart Creative

Treat Smart Creative and other automated creative features as distinct resource/endpoint families. Verify current availability and deprecation status before use.
