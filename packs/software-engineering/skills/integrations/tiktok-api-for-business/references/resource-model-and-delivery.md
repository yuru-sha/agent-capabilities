# Resource model and delivery

## Core hierarchy

For manual advertising, model the common ownership chain explicitly:

Advertiser -> Campaign -> Ad Group -> Ad

Do not assume every workflow maps identically to that shape. Upgraded Smart+ has dedicated campaign/ad-group operations and compatibility behavior.

## Plan resources first

For each requested operation mark resources as:

- create
- reuse
- update
- copy
- enable/disable
- not_required

Resolve dependencies before mutation.

## Campaign and ad-group concerns

Verify current endpoint-specific support for:

- objective / campaign type;
- Manual vs Upgraded Smart+;
- budget strategy and budget ownership;
- placements and automatic search placement;
- targeting and Smart Targeting;
- optimization/conversion event;
- bidding and bid limits;
- attribution settings;
- schedule and timezone;
- catalog/product dependencies;
- app/web destination;
- operation status.

## Lifecycle safety

- Prefer inactive/disabled creation when the API supports it and activation was not explicitly requested.
- Do not infer delivery from operation status alone.
- Diagnose parent status, review state, account status, schedule, budget, targeting, creative readiness, identity authorization, and billing/funding constraints.
- Treat deprecated Legacy Smart+ and deprecated ad formats as migration work, not as preferred implementation paths.
- Re-read affected objects after writes.
