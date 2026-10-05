# Lifecycle, versioning, and replication

Versioning improves recovery from overwrite/delete but increases retained storage; define noncurrent-version lifecycle intentionally.

Lifecycle transitions/deletion are asynchronous policy actions. Avoid rules that remove rollback or compliance-critical data unexpectedly.

Replication requires versioning and is asynchronous. Define source/destination ownership, encryption/KMS permissions, delete-marker behavior, metrics, and failure handling.

Object Lock and legal holds are separate from ordinary versioning; test governance/compliance behavior before enabling irreversible retention.
