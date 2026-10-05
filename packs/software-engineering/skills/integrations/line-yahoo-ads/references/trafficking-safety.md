# Trafficking safety

## Preflight before enabling delivery

Confirm:
- correct account and product;
- campaign/ad group/ad or reservation identifiers;
- intended objective;
- dates and timezone;
- budget and bid values with units;
- targeting and placements;
- creative and destination URL;
- tracking parameters;
- review/approval state;
- payment/funding readiness;
- all required parent and child statuses.

Current LINE Ads guidance states that campaign, ad group, and ad statuses must all be enabled for delivery, subject to the configured start time.

## Mutation rules

- Prefer create-paused / save-first workflows when available.
- Separate creation from activation.
- After a bulk upload/import, inspect validation results and sample affected objects before enabling.
- Never retry a partially successful bulk operation blindly.
- Keep an audit record of source brief, operator, timestamp, changed object IDs, and material before/after values.
- For destructive or wide-scope edits, export the current configuration first when the tool supports it.

## Review failures

Classify a failure as:
- input validation;
- policy/review;
- account/billing;
- schedule/status;
- missing dependency/asset;
- product availability;
- UI/document drift.

Do not weaken targeting, alter creative claims, change landing pages, or increase spend to "fix" a failure without explicit approval.

Primary sources:
- https://www.lycbiz.com/jp/manual/line-ads/ad_006/
- https://www.lycbiz.com/jp/manual/line-ads/
