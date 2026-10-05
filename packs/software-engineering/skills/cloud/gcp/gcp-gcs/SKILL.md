---
name: gcp-gcs
description: "Use when designing, implementing, reviewing, operating, or troubleshooting Google Cloud Storage buckets, objects, uploads/downloads, signed URLs, lifecycle/storage classes, versioning, retention, object locks, IAM, or large-object transfer behavior."
---

# gcp-gcs

Use this skill for GCS-specific object storage semantics and operations.

## Reference routing

- `bucket-object-and-consistency-model` → `references/bucket-object-and-consistency-model.md`
- `uploads-downloads-and-concurrency` → `references/uploads-downloads-and-concurrency.md`
- `lifecycle-versioning-and-retention` → `references/lifecycle-versioning-and-retention.md`
- `iam-signed-urls-and-security` → `references/iam-signed-urls-and-security.md`

## Rules

- Treat bucket location, storage class, lifecycle, retention, and access policy as explicit data-lifecycle decisions.
- Use object generation/metageneration preconditions for race-safe conditional updates and deletes.
- Prefer resumable uploads for large or unreliable transfers and keep memory use bounded.
- Do not treat object names as directories with filesystem locking/rename semantics.
- Make versioning, soft-delete/retention/object-lock behavior explicit before destructive operations.
- Prefer IAM and public-access prevention over ACL-heavy legacy designs.
- Treat signed URLs as scoped, time-limited bearer capabilities.
- Treat `references/` as detailed guidance, not independently selectable skills.
