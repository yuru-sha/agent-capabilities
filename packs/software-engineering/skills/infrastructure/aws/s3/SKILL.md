---
name: s3
description: "Use when designing, implementing, reviewing, operating, or troubleshooting Amazon S3 buckets, objects, multipart transfers, versioning, lifecycle, replication, Object Lock, access points, public access controls, or event integrations."
---

# Amazon S3

Use this skill for S3 object storage semantics, transfer, lifecycle, protection, and access.

## Reference routing

- `objects-transfers-and-concurrency` → `references/objects-transfers-and-concurrency.md`
- `lifecycle-versioning-and-replication` → `references/lifecycle-versioning-and-replication.md`
- `security-events-and-operations` → `references/security-events-and-operations.md`

## Rules

- Treat bucket Region, object identity, versioning, lifecycle, and retention as explicit data-lifecycle choices.
- Prefer multipart upload for large objects and abort incomplete multipart uploads through lifecycle/cleanup policy.
- Use conditional requests/version IDs when concurrent overwrite/delete correctness matters.
- Enable Block Public Access unless public access is an intentional requirement.
- Treat replication as asynchronous and design recovery around versioning and destination ownership.
- Treat Object Lock/retention as governance controls with potentially irreversible consequences.
- Treat `references/` as detailed guidance, not independently selectable skills.
