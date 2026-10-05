# Current API and source priority

verified_at: 2026-10-05

## Source priority

1. Current official TikTok API for Business documentation and API reference.
2. Current official migration guides, deprecation notices, changelog, and return-code documentation.
3. Official SDKs and samples for protocol clarification.
4. Third-party material only as a discovery aid.

The user-supplied guide is the v1.3 documentation entry point. Current TikTok documentation also exposes v2.0 material.

TikTok states that the v2.0 documentation is incremental: guides focus on materially changed categories and the v2.0 API reference primarily documents endpoints with enum/field changes. Endpoints that only need a version path update may be omitted from the v2.0 reference.

Therefore:

- never infer that a v1.3-only-looking endpoint is unavailable in v2.0 solely because it is absent from the v2.0 reference;
- verify the endpoint-specific migration requirement before choosing `/v1.3/` or `/v2.0/`;
- keep endpoint paths and enum/field names version-scoped in implementation code;
- isolate compatibility mappings so migration does not leak through application business logic.

Primary documentation:
- https://business-api.tiktok.com/portal/docs/about-the-guide/v1.3
- https://business-api.tiktok.com/portal/docs/marketing-api/v2.0
