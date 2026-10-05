# Security Cache And Operations

Prefer Origin Access Control for private S3 origins where supported. Treat signed URLs or cookies as time-bounded bearer authorization. Prefer versioned asset names for immutable content and use invalidations for exceptional mutable-path purge needs. Monitor cache hit ratio, origin latency/errors, and 4xx/5xx.
