# Delivery and lifecycle

## Campaigns

A campaign defines the business objective. Current documented objectives include
`TRAFFIC`, `SALES`, `AWARENESS`, and `APP_PROMOTION`, with regional
restrictions. Re-check supported objectives for the target ad account.

An ad account can currently hold up to 1,000 campaigns.

## Ad Groups

Ad Groups hold delivery controls such as schedule, bid/optimization settings,
targeting, and optional frequency controls. A campaign can currently hold up to
1,000 ad groups.

## Ads

Ads bind creative and destination configuration beneath an Ad Group. An Ad Group
can currently hold up to 100 ads.

## Money

Fields ending in `_micro` represent actual currency multiplied by 1,000,000.
Use integer arithmetic/decimal conversion. Never use binary floating-point for budget conversion.

Currency is configured at the ad-account level; do not infer it from locale.

## Scheduling and state

- Preserve the account timezone and API timestamp semantics.
- Validate start/end ordering and current-object state before updates.
- Prefer non-destructive updates.
- Do not infer effective delivery from one configured status field alone; inspect
  parent state, review/business errors, budget, schedule, and creative readiness.
