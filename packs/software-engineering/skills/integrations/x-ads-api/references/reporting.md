# Analytics and reporting

verified_at: 2026-10-03

## Translate intent into a report plan

For requests such as "yesterday by campaign", "this line item for the last 30
days", or "CTR by creative", derive and validate:

- Ads account;
- entity level and entity IDs;
- date/time range;
- account timezone and requested display timezone;
- granularity;
- metric groups and concrete metrics;
- placement;
- optional segmentation/dimension;
- synchronous vs asynchronous retrieval;
- batching and storage/streaming strategy.

Do not request a metric or segmentation merely because it existed historically.

## Current analytics modes

At verification time the official Analytics documentation states:

| Property | Synchronous | Asynchronous |
|---|---|---|
| Endpoint | `GET /12/stats/accounts/:account_id` | `POST/GET /12/stats/jobs/accounts/:account_id` |
| Max range | 7 days | 90 days non-segmented; 45 days segmented |
| Segmentation | no | yes |
| Result | metrics in response | processing job, then downloadable gzip file |
| Intended use | real-time/interactive optimization | scheduled sync, backfill, larger reports |

A request accepts up to 20 entity IDs. Async job status can be checked for
multiple job IDs; the official guide shows up to 200 job IDs in a status query.

## Entity levels and metric groups

The current Metrics and Segmentation table documents metric groups for:

- `ACCOUNT`;
- `FUNDING_INSTRUMENT`;
- `CAMPAIGN`;
- `LINE_ITEM`;
- `PROMOTED_TWEET`.

The current Analytics version history also documents `MEDIA_CREATIVE` support.
Because availability can vary by endpoint/version, verify the current entity
enum before issuing a query.

Current metric groups include:

- `ENGAGEMENT`;
- `BILLING`;
- `VIDEO`;
- `WEB_CONVERSION`;
- `MOBILE_CONVERSION`;
- `LIFE_TIME_VALUE_MOBILE_CONVERSION`.

Representative exposed metrics include impressions, engagements, clicks and
engagement subtypes, billed charge/spend-related metrics, video-view metrics,
and conversion metrics. Use the current table to map the user's requested
derived value (for example CTR) to exposed numerator/denominator fields.

## Time and placement semantics

Current Analytics rules require whole-hour timestamps. For `DAY` granularity,
start/end must align with midnight in the Ads account timezone. End time is
exclusive.

Current placements documented for analytics include:

- `ALL_ON_TWITTER`;
- `SPOTLIGHT`;
- `TREND`.

Only one placement is accepted per request. If the desired report spans
placements, issue separate requests and combine intentionally.

## Large reports

Prefer async for long ranges, segmentation, historical backfills, or large
entity sets:

```text
create job
 -> store job id
 -> poll status
 -> SUCCESS
 -> stream/download .json.gz
 -> decompress incrementally
 -> parse/process incrementally
```

Do not load a large compressed file and its fully decompressed JSON into memory
at the same time. Stream to disk or pipe through decompression and an
incremental parser where practical.

Batch entity IDs and date ranges within current endpoint limits. Persist job
state so a process restart does not submit duplicate jobs unnecessarily.

## Null, zero, missing, and no data

Do not collapse these blindly:

- numeric zero;
- JSON `null`;
- missing field;
- empty result/no matching activity.

Follow the current response schema. The official Analytics FAQ currently notes
that UI zeroes may correspond to API nulls for non-serving periods, but that
does not justify converting every missing or null field to zero. Preserve raw
semantics and normalize only in a reporting layer with explicit rules.

Billing/spend metrics may continue to settle after an event; current docs say
spend is generally final within three days and can be processed for longer for
quality filtering.
