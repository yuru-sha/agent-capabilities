# Current Meta Marketing API reference

verified_at: 2026-10-03
freshness_threshold_days: 30
verified_current_graph_api_version: v26.0
verified_current_marketing_api_version: v26.0

## Authority and revalidation

Use sources in this order:

1. Current Meta Marketing API and Graph API reference pages.
2. Graph API / Marketing API changelog and out-of-cycle changes.
3. Current permissions/features documentation and App Dashboard requirements.
4. Current official Business SDKs and official samples.
5. Meta developer blog posts as release context.
6. Community implementations only as corroborating evidence.

At verification time, Meta documentation lists Graph API v26.0 and Marketing API
v26.0 as released on 2026-07-29. Do not hard-code that assumption beyond the
freshness window.

Marketing API compatibility can change through versioned releases and
out-of-cycle changes. Before implementation, inspect both the version changelog
and out-of-cycle notices that apply to the requested endpoint family.

## Transport and versioning

Typical base URL:

`https://graph.facebook.com/v{VERSION}`

Version every production request explicitly unless current official guidance for
the specific flow says otherwise. Do not rely on an unversioned default.

Treat these as independently changeable contracts:

- fields and edges;
- objective/optimization/billing enums;
- placement and targeting schema;
- creative specifications;
- permissions/features and App Review requirements;
- Insights fields, breakdowns, action attribution, and retention;
- deprecated fields and removal dates.

## 2026 access-tier terminology

Meta renamed "Ads Management Standard Access" to "Marketing API Access Tier" in
2026. The underlying concern is broader Marketing API capacity/eligibility, not
the `ads_management` permission itself.

At verification time, Meta's developer update described Limited Access and Full
Access labels and published current qualification requirements in App Dashboard.
Treat the dashboard and current feature reference as authoritative because
thresholds and eligibility rules can change independently of API code.

## Current-v26 change risk

The v26 changelog removed several delivery-estimate fields for v26+ and announced
cross-version application later in 2026. This is why old response fields must not
be treated as stable just because older SDKs or examples still contain them.

## Official implementation research

Use official Business SDKs in multiple languages to understand Graph edge/request
composition, token placement, paging cursors, batch requests, media upload
behavior, async Insights jobs, and error-object parsing.

Do not copy SDK version defaults, generated field enums, retry policy, or object
models without checking current reference pages. Generated SDKs can lag newly
introduced or removed fields.
