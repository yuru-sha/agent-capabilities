# Security, events, and operations

Prefer bucket policies/IAM/access points over ACL-heavy designs. Keep Block Public Access enabled unless public serving is explicitly required.

For SSE-KMS, review both S3 permissions and KMS key policy/grants.

Treat event notifications/EventBridge delivery as at-least-once style integration and make consumers idempotent.

Monitor access-denied patterns, replication failures, lifecycle effects, storage growth, incomplete multipart uploads, and public-access posture.
