# Resource and mutation model

## Resource model

Google Ads API exposes account, campaign, ad group, ad, asset, criterion, bidding, conversion, audience, budget, billing, recommendation, planning, and reporting resources through versioned services.

Do not reduce every campaign type to one fixed hierarchy. Resolve the dependency graph from the requested campaign/channel type and the current version reference.

Typical delivery dependencies can include:
- customer/account context;
- campaign budget;
- campaign;
- ad group or asset group;
- targeting/criteria;
- assets and asset links;
- ads;
- conversion goals and bidding configuration.

Some campaign types use different resource combinations.

## Mutation choices

Use resource-specific mutate methods when working within one resource family and the method contract is sufficient.

Use `GoogleAdsService.Mutate` when a single request benefits from mixed operation types or temporary resource IDs across related objects.

Official mutation overview:
https://developers.google.com/google-ads/api/docs/mutating/overview

## Update semantics

For updates:
- read the current resource when needed;
- set only intended fields;
- use the explicit update mask required by the service/client;
- never send broad masks merely to make an update succeed;
- do not silently overwrite user-managed fields.

For removals, verify whether removal is reversible and whether child/dependent resources remain queryable.

## Temporary IDs

Temporary resource IDs can connect dependent creates in one mutate request or batch job. Keep them unique within the request/job and map them back to returned real resource names.

Do not persist temporary IDs as durable identifiers.

## validate_only

Where a request exposes `validate_only`, use it for risky or structurally complex writes before execution. Validation does not prove policy approval, delivery eligibility, budget sufficiency, or future state.

## Partial failure

By default, a mutate request may fail atomically when any operation is invalid. Where supported, `partial_failure=true` allows independent valid operations to commit while failures are returned separately.

Use partial failure only when successful operations are safe without failed siblings.

Avoid it for tightly dependent operation sets unless the documented dependency semantics make partial execution acceptable. A failed parent referenced by temporary ID can cause dependent child operations to fail as well.

Official guidance:
https://developers.google.com/google-ads/api/docs/best-practices/partial-failures

## Delivery safety

For campaign/ad creation:
- create the minimum required resources;
- prefer paused state where supported;
- verify budget, bidding, targeting, schedules, URLs, tracking, creatives/assets, conversion goals, and policy/review readiness before enabling;
- confirm both object status and relevant parent status.

A successful mutate response does not mean the ad is approved or delivering.
