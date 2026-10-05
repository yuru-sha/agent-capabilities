# IAM, signed URLs, and security

Prefer uniform bucket-level access and IAM over object ACLs for new designs unless a specific compatibility requirement justifies ACLs.

Enable public access prevention where public serving is not required. Review bucket IAM, service-agent access, and cross-project identities explicitly.

Signed URLs are bearer capabilities. Scope method, object, expiration, and headers narrowly, and avoid exposing long-lived URLs in logs or analytics.

Use customer-managed encryption keys only when key ownership/rotation requirements justify the added dependency and IAM complexity.

Do not place credentials, signed URL secrets, or service-account keys in source, examples, build logs, or artifacts.
