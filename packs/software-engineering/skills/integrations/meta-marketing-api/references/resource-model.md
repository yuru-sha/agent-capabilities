# Resource model and dependency planning

verified_at: 2026-10-03

## Core hierarchy

The common delivery hierarchy is:

`Business -> Ad Account -> Campaign -> Ad Set -> Ad -> Ad Creative`

Supporting dependencies frequently sit outside that chain:

- Page / Instagram / WhatsApp identity;
- image/video assets;
- Pixel/Dataset and conversion events;
- Custom/Lookalike Audiences;
- catalogs and product sets;
- lead forms;
- app, domain, destination URL, deep link, or promoted object.

Do not model the API as only a nested CRUD tree.

## Explicit resource plan

Before mutation, classify each resource as `create`, `reuse`, `upload`,
`update`, or `not_required`. Capture existing IDs and dependency reasons.

Never create a replacement merely because creation is easier than compatibility checks.

## Compatibility checks

Validate parent/child compatibility for:

- objective and buying type;
- budget strategy;
- optimization goal and billing event;
- bid strategy;
- promoted object / conversion location;
- targeting and placement;
- creative format;
- Page/Instagram identity;
- attribution setting;
- catalog/product-set use.

## Effective delivery

Configured status is not delivery truth. Diagnose at least:

- Ad Account status/funding;
- Campaign status and schedule;
- Ad Set status, schedule, budget, bid, targeting, audience, optimization;
- Ad status;
- Creative processing/review/policy state;
- identity validity;
- account/business/app restrictions;
- learning/delivery state and current product constraints.

Expose configured status and delivery diagnostics separately.

## Reconciliation

For automation, persist stable correlation identifiers or deterministic names
where appropriate. After uncertain writes, reconcile by reading existing
resources before retrying creation.
