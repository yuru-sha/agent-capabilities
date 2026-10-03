# Scheduling, status, and delivery lifecycle

verified_at: 2026-10-03

## Scheduling inputs

Read [account-context.md](account-context.md) first for timezone semantics.

Capture:

- requested start datetime;
- requested end datetime or indefinite/no-end intent;
- Campaign schedule;
- Line Item schedule/constraints where currently supported.

Keep both the user's timezone-aware intent and the normalized instant required by
the current endpoint. Do not duplicate timezone-conversion rules here; account
timezone, Analytics day boundaries, DST, and display-timezone handling belong to
the account-context reference.

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
