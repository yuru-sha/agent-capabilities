# Sorting and stable ordering

verified_at: 2026-10-03

Do not assume a universal `sort` parameter, default ordering, or stable order
across X Ads API collection endpoints.

## Server-side sorting

Before relying on server-side ordering:

1. check the current endpoint reference for a supported sort parameter;
2. verify allowed fields;
3. verify ascending/descending syntax;
4. verify default order when sort is omitted;
5. verify whether the ordering is guaranteed or merely observed.

Do not send unsupported sort fields derived from another endpoint or an old SDK.

## Sorting with pagination

Ordering and pagination interact.

When a workflow requires deterministic traversal:

- prefer a documented stable server-side order;
- include a stable tie-breaker when the endpoint supports multiple sort keys;
- de-duplicate by resource ID;
- account for resources created/updated during traversal;
- do not assume cursor order remains equivalent to client-side sorting.

If stable server ordering is not documented, treat cross-page order as
potentially unstable.

## Client-side sorting

Client-side sorting is acceptable when:

- the complete bounded dataset has intentionally been retrieved;
- API ordering cannot satisfy the user requirement;
- memory/storage cost is acceptable.

For large datasets, prefer incremental/external sorting or persistent storage
rather than loading everything into memory solely to sort it.

## Reporting

Analytics ordering is a separate concern from resource-list ordering. Do not
assume metrics responses can use generic resource-list sort semantics.

For "top N" reporting:

1. retrieve the required complete report scope;
2. compute/derive the metric consistently;
3. sort in the reporting layer unless the current analytics endpoint explicitly
   supports the desired ordering;
4. define tie behavior.

Never compute "top N" from only the first paginated page unless the server
explicitly guarantees the requested ranking.
