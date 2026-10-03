# Currency and money handling

verified_at: 2026-10-03

Currency is part of the Ads account contract. Treat it as a typed property, not
as a display suffix.

## Account currency first

Before creating or updating budget, bid, spend, or billing-related values:

1. read the target Ads account;
2. determine the current account currency and relevant funding instrument;
3. verify the endpoint's monetary unit/representation;
4. convert user input only when explicitly intended;
5. preserve the original user amount/currency separately from the transmitted
   account-currency amount.

Do not assume USD.

## Amount representation

Verify per current endpoint whether money is represented as:

- decimal major units;
- integer minor units;
- another documented unit/encoding.

Never infer the unit from a sample value.

Use integer/decimal-safe arithmetic. Do not use binary floating-point for
authoritative budget/bid/conversion calculations.

## Currency conversion

The X Ads API should not be treated as a generic FX service.

If the user's requested amount is in a different currency from the Ads account:

- identify the account currency;
- require an explicit conversion policy/source if conversion is needed;
- record the FX rate, source, timestamp, rounding rule, and resulting amount;
- do not silently convert.

## Funding and budget checks

Currency compatibility is only one delivery prerequisite. Also verify current:

- funding instrument availability;
- account/funding restrictions;
- campaign/line-item budget constraints;
- minimum/maximum bid or budget rules for the selected objective/product.

## Reporting

For spend/billing reports:

- preserve the account currency alongside values;
- do not combine monetary values from accounts with different currencies without
  an explicit normalization step;
- keep raw API monetary values available for reconciliation.

A cross-account "total spend" is invalid unless the currency treatment is
explicit.
