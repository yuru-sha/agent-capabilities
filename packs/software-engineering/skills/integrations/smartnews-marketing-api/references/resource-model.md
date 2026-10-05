# Resource model

The primary delivery hierarchy is:

Ad Account
→ Campaign
→ Ad Group
→ Ad

Media files, custom audiences, pixels, targeting option dictionaries, catalogs,
and product sets are supporting resources.

## Planning rule

For every requested operation, mark resources as one of:

- create
- reuse
- update
- delete
- read/report
- not required

Resolve IDs and ownership before mutation.

## Parent/child concurrency rule

SmartNews rejects certain simultaneous writes with `409 Conflict`.

Do not concurrently create/update/delete:

- multiple children sharing the same parent;
- a parent and one of its children;
- related Campaign / AdGroup / Ad objects whose operations overlap before the prior response completes.

Use a per-parent serialization key or dependency queue. Parallelism is still
reasonable across independent parent branches when the API contract permits it.

## Safe lifecycle behavior

- Read current state before destructive or expensive mutations.
- Avoid deleting/recreating an object when PATCH can satisfy the intent.
- After a mutation, fetch the resource again before dependent work.
- If a write times out after transmission, reconcile by reading before retrying.
