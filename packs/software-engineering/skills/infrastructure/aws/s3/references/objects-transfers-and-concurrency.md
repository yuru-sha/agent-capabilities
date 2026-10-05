# Objects, transfers, and concurrency

S3 is object storage, not a POSIX filesystem. Avoid assumptions about append, directory locks, or atomic directory rename.

For large objects, stream data and use multipart upload with bounded parallelism, retry, checksum/integrity validation, and abort behavior.

Use ETag only with awareness of multipart/encryption semantics; prefer supported checksum features when end-to-end integrity matters.

Use conditional requests, version IDs, or application-level coordination for race-sensitive writes and deletes.
