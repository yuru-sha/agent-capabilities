# Scheduling, status, and delivery lifecycle

verified_at: 2026-10-03

## Scheduling inputs

Capture:

- requested start datetime;
- requested end datetime or indefinite/no-end intent;
- user timezone;
- Ads account timezone;
- Campaign schedule;
- Line Item schedule/constraints where currently supported.

Preserve the user's timezone in the plan even if the API requires normalized
timestamps.

## Time normalization

General X Ads API datetime responses are UTC-oriented, while Analytics DAY
boundaries use the Ads account timezone.

Do not apply one timezone rule to both campaign scheduling and reporting.

Before a write:

1. parse the user's timezone-aware datetime;
2. verify account timezone where relevant;
3. check current Campaign/Line Item scheduling parameter semantics;
4. normalize only to the form required by the endpoint;
5. retain the source timezone for user-facing output and auditing.

## Parent/child schedule relationships

Do not assume child schedules can extend outside parent schedules.

Before creating/updating a Line Item under a Campaign, verify current official
constraints for:

- child start before parent start;
- child end after parent end;
- omitted parent/child end;
- updates after delivery has begun;
- updates after the scheduled end.

## Lifecycle concepts

### Campaign

Support the intent concepts:

- create;
- activate;
- pause;
- resume;
- scheduled end;
- delete when currently supported and explicitly intended.

### Line Item

Apply the same intent model, but verify its own endpoint fields and restrictions.

### Promoted object / advertising association

Determine whether the current resource supports:

- active/paused configured state;
- delete/disassociate;
- immutable replacement;
- schedule-driven cessation.

Do not reuse Campaign status semantics blindly.

### Creative/media

Delivery can depend on:

- upload processing;
- availability;
- policy approval;
- review state;
- enabled/disabled association;
- supported product/placement.

Do not invent a universal Creative `ACTIVE` enum.

## Configured status vs effective delivery

Treat effective delivery as a diagnosis across the dependency graph:

```text
campaign configured and eligible
AND line item configured and eligible
AND current time is inside the valid schedule
AND advertising association is enabled
AND creative/media is available
AND required approval/review has passed
AND targeting is valid
AND funding/budget is usable
AND current product/placement constraints are satisfied
```

This is a diagnostic model, not an API field.

## Smallest-scope mutation

Examples:

- stop one promoted Post -> change/remove the narrowest relevant promoted
  association when supported;
- stop one ad group -> pause the Line Item rather than its Campaign;
- stop an entire initiative -> Campaign-level pause may be appropriate.

Before mutating a parent, enumerate the sibling resources that would also be
affected.

## Read-after-write verification

After status/schedule mutations:

1. re-read the changed resource;
2. confirm the configured state;
3. if the user's goal is delivery-related, inspect relevant parent/child and
   creative/media states;
4. distinguish "mutation succeeded" from "delivery is now effective".
