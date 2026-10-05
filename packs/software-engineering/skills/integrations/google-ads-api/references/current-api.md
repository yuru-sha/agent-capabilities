# Current Google Ads API

Verified: 2026-10-05.

## Source priority

Use these official sources in this order:

1. Google Ads API release notes: https://developers.google.com/google-ads/api/docs/release-notes
2. Versioned API reference: https://developers.google.com/google-ads/api/reference/rpc
3. Guides: https://developers.google.com/google-ads/api/docs/start
4. Fields/GAQL reference and Query Builder: https://developers.google.com/google-ads/api/fields/overview
5. Deprecations and sunset guidance linked from the release notes.

Do not treat blog posts, generated client code from an older dependency, examples pinned to older versions, or search snippets as stronger than the current official reference.

## Verified baseline

On 2026-10-05:
- the latest documented major line is Google Ads API v25;
- v25 was released on 2026-07-22;
- v25.2 was released on 2026-09-23;
- minor releases add fields/features without intentional breaking changes, while major versions may remove or structurally change resources, fields, services, and enums.

Always confirm the currently supported versions before implementation. Code, REST paths, generated clients, field metadata, and resource schemas must agree on the same API version.

## Version-sensitive areas

Re-check these before relying on memory:
- campaign types and channel subtypes;
- bidding strategy fields and goals;
- Performance Max, Demand Gen, App, Shopping, and asset automation features;
- conversion goals and lifecycle/customer acquisition schemas;
- ad and asset types;
- reporting fields, metrics, segments, and compatibility;
- planning and audience insight services;
- synthetic/AI-generated content declarations;
- YouTube/video upload integration exposed through Google Ads API;
- deprecated fields and sunset versions.

## Upgrade discipline

When upgrading:
1. read the release notes between the source and target versions;
2. identify removals, replacements, renamed fields, enum changes, and behavior changes;
3. regenerate or upgrade client libraries if used;
4. validate GAQL fields against the target version;
5. run `validate_only` or non-delivering test mutations where supported;
6. verify report parity and mutation results against representative accounts.

Do not mix examples from different major versions in one implementation.
