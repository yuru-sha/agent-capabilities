# Ad Account and Business context

verified_at: 2026-10-03

## Resolve context before building payloads

For every operation, establish:

- Business ID and ownership;
- Ad Account ID in `act_{id}` form when required;
- account status;
- timezone and timezone offset;
- currency;
- funding/billing readiness;
- spending limits where relevant;
- connected Page and Instagram account identity;
- Pixel/Dataset and conversion assets;
- catalogs/product sets when used;
- whether the account is subject to special-ad-category or regional constraints.

## Currency and budget semantics

Do not treat budget fields as human-readable decimal currency without checking
the current endpoint contract. Advertising budget/bid fields commonly use
integer API values in the account currency's minor unit or other endpoint-
specific integer semantics.

Keep a clear boundary:

`human money -> validated account currency -> API integer representation`

Never reuse a raw amount copied from an account with a different currency.

## Timezone

Use the Ad Account timezone as the default business/reporting context unless the
user explicitly asks for another display timezone.

Scheduling, day-level reporting, daily budgets, and UI/API comparisons can look
wrong when code silently uses UTC or the host timezone.

Persist timestamps as timezone-aware values and record the account timezone used
to construct or interpret each request.

## Connected identities

Creative creation may require a Facebook Page, Instagram account, WhatsApp
identity, or other surface-specific identity. Verify current placement-specific
requirements before constructing story, asset-feed, or identity specs.

Do not infer identity from a previously used ad when another Business, Page,
Instagram account, or WhatsApp asset was selected.
