# Advertising types and dependency resolution

verified_at: 2026-10-03

This matrix is a decision aid. It is not a frozen product catalog. Re-check the
current Campaign Management, Creatives, Catalog, and Lead Generation references
before implementation.

| Advertising family | Campaign | Line item | Targeting | Media / creative dependency | Association notes |
|---|---|---|---|---|---|
| Promoted Post | normally required | normally required | line-item scoped | Post required; media/card conditional | create/reuse promoted-post association |
| Follower / Promoted Account | required | required | product-specific | account-promotion creative semantics | do not model as ordinary promoted post |
| Image/video Post ad | required | required | line-item scoped | Post plus uploaded/reused media as applicable | promoted-post relationship usually applies |
| In-stream / pre-roll | required | required | product-specific | `amplify_video` media + Media Library/media creative | current guide says no Promoted Post/Card dependency |
| Mobile App Promotion | required | required | product-specific | resolve current app/card/Post requirements | validate app and conversion dependencies |
| Lead Gen | required | required | product-specific | lead form plus currently supported card/creative path | resolve promotion association after form/card setup |
| Dynamic Product Ads | required | required | product-specific | catalog + product set/feed + supported creative | catalog eligibility is an upstream dependency |
| X Audience Platform media creative | product-dependent | product-dependent | placement-specific | account media/media creative | verify placement/product support |

## Resolution algorithm

For every advertising request:

1. identify objective and advertising family;
2. identify required product/placement;
3. query current documentation for required parent resources;
4. map each resource to `create`, `reuse`, `upload`, or `not_required`;
5. validate supplied IDs against account ownership and compatibility;
6. create only missing dependencies;
7. create the narrowest required association.

## Reuse checks

Before reusing a resource, validate:

- same Ads account or supported cross-account semantics;
- parent/child compatibility;
- objective/product compatibility;
- schedule compatibility;
- targeting compatibility;
- creative/media processing and approval state;
- deleted/archived state;
- current API visibility.

Do not recreate an asset because it is easier than checking reuse.

## Unknown advertising type

If the user asks for an advertising type not present here:

- treat it as unknown, not unsupported;
- re-check official docs immediately;
- resolve its current dependency graph;
- update the local reference if appropriate;
- do not map it to the "closest" known type by guesswork.
