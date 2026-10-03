# Account context: timezone and currency

verified_at: 2026-10-03

Timezone and currency are Ads-account semantics, not presentation details.
Resolve them early because they affect scheduling, reporting, budgets, bids,
spend, and reconciliation.

## Timezone

Track separately:

- the user's input timezone;
- the Ads account timezone;
- the API transport/response timezone semantics.

Never send a naive local datetime.

Before schedule writes:

1. parse the user's timezone-aware datetime;
2. verify the Ads account timezone where endpoint semantics depend on it;
3. check current Campaign/Line Item scheduling rules;
4. normalize only to the representation required by the endpoint;
5. retain the original timezone and normalized instant.

For Analytics, current DAY aggregation uses Ads-account timezone boundaries and
an exclusive end time. Resolve relative periods such as "yesterday" against the
account timezone unless the user explicitly requests another interpretation.

For DST-observing zones, explicitly handle nonexistent and repeated local times.
Prefer IANA timezone identifiers over persisted fixed offsets.

## Currency

Read the Ads account and funding context before constructing monetary writes.
Do not assume USD.

Before creating or changing budgets, bids, or other monetary values:

1. determine the Ads account currency;
2. verify the current funding instrument;
3. verify the endpoint's amount representation and unit;
4. use integer/decimal-safe arithmetic;
5. preserve the user's original amount/currency separately from the transmitted
   account-currency value.

Never infer whether an amount is in major or minor units from an example.

## Currency conversion

Do not silently convert currencies.

If user input differs from the Ads account currency, make the conversion policy
explicit and retain:

- source and target currency;
- FX source;
- rate and timestamp;
- rounding rule;
- converted amount.

The Ads API is not an FX-rate source.

## Reporting and reconciliation

For spend/billing output:

- keep account currency attached to monetary values;
- do not aggregate spend across accounts with different currencies unless an
  explicit normalization policy is applied;
- preserve raw API values for reconciliation.

For report periods, distinguish the account timezone used for aggregation from
the user's display timezone when they differ.
