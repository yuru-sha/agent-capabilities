---
name: line-yahoo-ads
description: Use when planning, trafficking, reviewing, launching, or reporting LINE Yahoo Ads across Search Ads, Display Ads (Auction), and Display Ads (Guaranteed) in the LINE Yahoo advertising management tools.
---

# LINE Yahoo Ads

Use this Skill to turn an advertising request into a safe, current trafficking and reporting plan for LINEヤフー広告.

## Core invariants

- Official LINEヤフー for Business service pages, manuals, product notices, media sheets, and submission guidelines are authoritative.
- Treat Search Ads, Display Ads (Auction), and Display Ads (Guaranteed) as different products. Do not reuse a hierarchy, creative rule, targeting option, buying model, or report schema without verification.
- Prefer current LINEヤフー広告 terminology. Preserve legacy names (Yahoo!広告, LINE広告) only to locate still-relevant documentation or historical data.
- Resolve account, objective, destination, budget, schedule, targeting, creative, tracking, review status, and reporting requirements before enabling delivery.
- Create or edit the minimum required objects. Keep delivery paused/off until explicit launch intent and review readiness are confirmed.
- Never infer that "saved" means "eligible to deliver"; confirm review, status, dates, budget/funding, and all parent/child states.
- Do not silently change budget, bid, dates, targeting, URL, tracking parameters, or creative to make validation pass.
- Preserve historical reporting definitions and note product/UI migrations when comparing time periods.
- Treat bulk sheets, CSV exports, downloaded reports, and customer/audience data as potentially sensitive.

## Freshness gate

The bundled references were verified against official LINEヤフー for Business material on `2026-10-05`.

Re-check official material before execution when:
- 30 days have passed;
- the management UI or product naming changed;
- a field, objective, targeting option, creative specification, report column, or buying rule differs;
- an old Yahoo!広告 / LINE広告 manual is the only available source;
- the operation concerns a reservation/guaranteed product, special placement, or time-limited sales sheet.

Read [references/current-platform.md](references/current-platform.md) first.

## Workflow

1. Identify Search / Display Auction / Display Guaranteed and the intended account.
2. Pass the freshness gate and confirm current product/UI boundaries.
3. Resolve trafficking inputs using the matching product reference.
4. Validate destination, creative, targeting, budget/bid, schedule, tracking, and review requirements.
5. Prefer paused/inactive creation where the UI allows it; verify the saved state.
6. Before launch, run the preflight in [references/trafficking-safety.md](references/trafficking-safety.md).
7. For results, define reporting level, period, timezone, attribution/conversion interpretation, dimensions, and export format before downloading.
8. Verify output completeness and retain enough metadata to reproduce the report.

## Reference map

- [current-platform.md](references/current-platform.md): current product naming, source priority, migrations, freshness.
- [search-ads.md](references/search-ads.md): Search Ads trafficking model and checks.
- [display-auction.md](references/display-auction.md): Display Ads (Auction) trafficking model and checks.
- [display-guaranteed.md](references/display-guaranteed.md): Display Ads (Guaranteed) planning, ordering, trafficking, and product-specific cautions.
- [reporting.md](references/reporting.md): performance/custom reports, report design, exports, historical comparability.
- [trafficking-safety.md](references/trafficking-safety.md): review, activation, bulk operations, validation, rollback, and audit rules.
