# Campaign delivery, targeting, and lifecycle

verified_at: 2026-10-03

## Campaign

Resolve current objective, buying type, special-ad-category requirements, budget
strategy, and status fields from the current Campaign reference.

Do not reuse legacy objective names without validation. Recent Marketing API
versions use newer outcome-oriented objective families for many campaign types.

## Ad Set

An Ad Set can combine:

- campaign ID;
- daily/lifetime budget when not campaign-budgeted;
- start/end schedule;
- billing event;
- optimization goal;
- bid strategy / bid amount where applicable;
- targeting;
- promoted object / conversion source;
- attribution settings;
- placements and automation settings;
- status.

Validate these as one coherent tuple. An enum can be individually valid but
invalid for the selected objective, promoted object, or placement.

## Ad

An Ad commonly associates an Ad Set with a Creative and lifecycle state. Avoid
creating duplicates after a timeout; first reconcile whether the intended
association already exists.

## Targeting and placements

Resolve current targeting IDs and schema from official search/reference APIs.
Do not hard-code IDs from display names.

Placement support depends on objective, optimization, creative format, identity,
destination, and current product availability across Meta surfaces. Do not
assume a historical publisher/platform-position matrix remains valid.

Automation and Advantage-family controls can change defaults and required
payload shape. Verify current automation fields before implementation.

## Safe creation pattern

Unless explicitly asked to launch immediately:

1. Create or reuse Campaign in PAUSED state.
2. Create or reuse Ad Set in PAUSED state.
3. Create or reuse/upload Creative assets.
4. Create or reuse Ad in PAUSED state.
5. Read back fields, preview, and delivery diagnostics.
6. Activate only the minimum intended layer.

## Scheduling and delivery state

Interpret schedules in the Ad Account timezone and current endpoint format.

Do not infer that a parent ACTIVE state means delivery is occurring. Verify
account status/funding, parent and child status, schedule, budget/bid, targeting,
audience, creative review/processing, identity, and current product constraints.

## Delivery estimates

Treat reach/delivery-estimate endpoints as advisory and version-sensitive. The
v26 changelog removed several delivery-estimate fields. Never make a required
workflow depend on an estimate field without current validation.

## Policy-sensitive categories

Special ad categories, regulated products, regional requirements, authorization,
disclaimers, and targeting restrictions can change independently of API schema.
Separate API acceptance, policy review, and actual delivery state.
