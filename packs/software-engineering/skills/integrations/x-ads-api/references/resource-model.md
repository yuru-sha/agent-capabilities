# Resource model, advertising types, scheduling, and lifecycle

verified_at: 2026-10-03

## Resolve dependencies from the advertising type

Never begin with a fixed Campaign -> Line Item -> Media -> Ad template. Determine
what is being promoted and the current objective/product/placement first, then
consult the current Campaign Management and Creatives references.

Represent the plan explicitly:

```yaml
campaign:
  mode: create | reuse | not_required
line_item:
  mode: create | reuse | not_required
media:
  mode: upload | reuse | not_required
creative:
  mode: create | reuse | not_required
association:
  mode: create | reuse | not_required
```

If the user supplies a compatible Campaign, Line Item, media key, Post/Card, or
creative ID, prefer reuse after validation.

## Current advertising families to recognize

The current official documentation describes these major families. They are a
classification aid, not a frozen enum list; re-check objective, product type,
placement, and required endpoints before implementation.

| Family | Dependency notes |
|---|---|
| Promoted Post ads | Usually campaign + line item + promotable Post; media/card is conditional on the Post creative |
| Follower / Promoted Account campaigns | Campaign + line item; account promotion semantics differ from ordinary promoted posts |
| Video / promoted video | Post-based video ads can use uploaded media; pre-roll/in-stream is a separate flow |
| In-stream / pre-roll (`VIDEO_VIEWS_PREROLL`) | Official guide states it does not use Promoted Posts or Cards; upload `amplify_video`, add to Media Library, associate media creative with line item, configure pre-roll CTA as applicable |
| Mobile App Promotion | Resolve app, objective/product, card/Post and conversion dependencies from current docs |
| Lead Gen Ads | Lead form + card with `LEAD_FORM` destination plus the normal campaign/line-item promotion relationship required by the current product |
| Dynamic Product Ads | Resolve Catalog/product-set/feed dependencies from Catalog Management before campaign/creative creation |
| X Audience Platform media creatives | Resolve supported account-media/media-creative and placement requirements before association |

Promoted Trends are documented as unavailable through the Ads API.

## Hierarchy and reuse

At verification time the official hierarchy states:

- Ads accounts are the top-level container.
- Funding instruments belong to accounts; campaigns use a funding source.
- Campaigns define budget and schedule.
- Line items (ad groups) live under campaigns and define targeting/bidding and
  the creative association.
- account media, Media Library objects, cards, and audiences are account-scoped
  assets that can often be reused.
- each line item needs at least one eligible creative association to run.

Validate compatibility instead of recreating resources.

## Scheduling

Capture these fields from the user intent:

- start datetime;
- optional end datetime;
- source timezone;
- whether the intent is indefinite/no end;
- Campaign schedule;
- Line Item schedule if the current endpoint supports or constrains it.

Preserve the original timezone in the plan. Convert only for API transmission
according to the current endpoint rules. The general Timezones documentation
states returned datetime values are UTC, but analytics DAY boundaries are based
on the Ads account timezone.

Do not infer parent/child date constraints. Before a create/update, confirm the
current Campaign and Line Item parameter tables. Treat end time as optional only
when the current endpoint permits it.

State phases to reason about:

- pre-start: configured but outside the delivery window;
- active period: inside schedule, subject to all other eligibility;
- post-end: schedule has elapsed even if a configured entity status still looks
  enabled.

## Lifecycle and minimum mutation scope

Read the current endpoint enum before writing. Current examples use
`entity_status=PAUSED` and `entity_status=ACTIVE` for Campaign/Line Item
operations, while deletion is a separate DELETE operation. Do not invent
`ENDED` or `ARCHIVED` enum values without confirming them.

For Campaign and Line Item intents support the concepts:

- create;
- activate;
- pause;
- resume;
- end by schedule where supported;
- delete only when the current endpoint supports the requested destructive
  behavior.

Promoted-object and creative lifecycle differs by type. Verify whether the
current resource is toggled, deleted, disassociated, approval-gated, or
processing-gated.

Always choose the smallest mutation scope. To stop one promoted object, do not
pause its campaign if the object or line-item association can be safely stopped
without affecting siblings.

## Configured state vs effective delivery

Never report "delivering" from one status field. Diagnose a conceptual
eligibility chain such as:

```text
campaign eligible
AND line item eligible
AND schedule active
AND promoted object/association enabled
AND creative/media available
AND creative approved where approval applies
AND targeting valid
AND funding available
AND current product/placement constraints satisfied
```

This is a Skill diagnostic model, not a claim that X exposes one
`effective_delivery` field. When delivery is unexpectedly stopped, inspect the
whole relevant hierarchy and current API errors/approval/processing states.
