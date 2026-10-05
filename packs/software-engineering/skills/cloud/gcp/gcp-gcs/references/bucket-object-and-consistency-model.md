# Bucket, object, and consistency model

Choose bucket location from latency, residency, availability, service integration, and cost requirements before data is written.

Object names form a flat namespace even when they contain slash-like prefixes. Do not rely on filesystem rename, locking, or atomic directory operations.

Use generation numbers to identify immutable object versions and metageneration for metadata state.

Design metadata, content type, cache control, checksums, and custom metadata deliberately.

Treat object replacement as a new object generation. Consumers that require immutable references should record generation-qualified identity.
