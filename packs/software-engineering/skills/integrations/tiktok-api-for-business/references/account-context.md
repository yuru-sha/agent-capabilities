# Account and business context

Resolve the execution context before writes.

Record at minimum:

- advertiser_id;
- Business Center / organization ownership when relevant;
- advertiser account status;
- account timezone;
- account currency and money-field units;
- connected TikTok identity / Spark Ads identity requirements;
- promoted app, website, catalog/store, pixel/event source, or lead asset as applicable;
- permission boundaries for the selected developer app and token.

## Time and money

Do not convert budgets or schedule timestamps until the endpoint-specific unit and timezone semantics are verified.

Keep:

- human-entered monetary values;
- API wire values;
- advertiser currency;
- conversion/rounding rules

as separate concepts.

When scheduling ads, derive times in the advertiser account's configured timezone unless the endpoint explicitly defines another basis.

## Identity

TikTok ad creation may depend on an authorized identity, including Spark Ads flows. Resolve identity type and permission before creating the ad rather than treating identity as a late creative detail.
