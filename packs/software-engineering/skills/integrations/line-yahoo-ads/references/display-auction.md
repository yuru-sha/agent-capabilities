# Display Ads (Auction) trafficking

Display Ads (Auction) is the unified auction-based display offering across LINE, Yahoo! JAPAN, and related inventory.

## Core hierarchy

Treat the common operational structure as:

Account -> Campaign -> Ad Group -> Ad

Current LINE Ads manuals describe:
- campaign: objective, delivery period, optional campaign budget;
- ad group: targeting, placements, optimization/bidding, daily budget;
- ad: parent campaign/ad group, format/media, title/description, destination URL, status.

## Resolve before entry

- objective and conversion/optimization event;
- campaign dates and budget ownership;
- audience/demographic/location/placement targeting;
- automatic vs selected placements;
- bid strategy and bid/target values;
- daily budget;
- image/video/app/product-feed assets;
- destination and tracking;
- review/policy requirements;
- initial status.

## Current-platform caution

Some indexed manuals still carry the "LINE広告" title even though the product has been unified into LINEヤフー広告. Use them for behavior only after checking current product notices and the actual management UI.

Do not hard-code placement lists from an old manual. For example, LINE VOOM advertising delivery ended with the service on 2026-09-30, while historical performance remains reportable.

Primary sources:
- https://www.lycbiz.com/jp/service/ly-ads/displayads-auc/
- https://www.lycbiz.com/jp/manual/line-ads/ad_001/
- https://www.lycbiz.com/jp/manual/line-ads/ad_002/
- https://www.lycbiz.com/jp/manual/line-ads/ad_005/
