# Timezone handling

verified_at: 2026-10-03

Timezone behavior affects scheduling, analytics boundaries, user-facing dates,
and reconciliation. Do not treat timezone as a formatting concern.

## Preserve three concepts separately

Track:

- the user's input timezone;
- the Ads account timezone;
- the API transport/response timezone semantics.

Do not overwrite the user's timezone merely because an endpoint transmits or
returns UTC-oriented timestamps.

## Scheduling

Before creating or updating Campaign/Line Item schedules:

1. parse user input as a timezone-aware datetime;
2. verify the Ads account timezone where endpoint semantics depend on it;
3. check current Campaign/Line Item parameter documentation;
4. convert only to the form required by the API;
5. retain the original timezone and normalized instant for auditing.

Never send a naive local datetime.

## Analytics

Current Analytics rules differ from generic resource timestamps.

For `DAY` granularity:

- day boundaries are based on the Ads account timezone;
- start/end must align to the required whole-hour/midnight boundaries;
- end time is exclusive.

Therefore "yesterday" must be resolved in the Ads account timezone unless the
user explicitly requests another reporting interpretation.

## User intent vs account timezone

If the user specifies a timezone different from the Ads account timezone:

- preserve the user's stated intent;
- normalize the exact instants correctly;
- verify whether the endpoint interprets timestamps as absolute instants or
  account-local boundaries;
- surface the effective account-local interval when it matters.

## DST and ambiguous local times

For zones with daylight-saving transitions:

- reject or explicitly resolve nonexistent local times;
- disambiguate repeated local times;
- prefer IANA timezone names over fixed offsets for persisted user intent.

## Reporting output

When presenting report periods, distinguish:

- account timezone used for API aggregation;
- user/requested timezone used for display.

Do not silently mix them.
