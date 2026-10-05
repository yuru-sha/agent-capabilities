# Uploads, downloads, and concurrency

Use resumable uploads for large objects or unreliable networks. Bound buffers and stream data rather than reading entire files into memory.

Use generation-match and metageneration-match preconditions for create-if-absent, compare-and-swap metadata, safe overwrite, and safe delete behavior.

Retry idempotent operations with bounded exponential backoff and jitter. For non-idempotent writes, use preconditions or resumable-session state to make retries safe.

Validate checksums where integrity matters.

For high-throughput transfer, tune parallelism against network, object count, API quotas, and downstream disk/memory limits rather than maximizing concurrency blindly.
