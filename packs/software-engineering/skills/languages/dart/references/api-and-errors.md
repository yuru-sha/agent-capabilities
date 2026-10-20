# HTTP APIs, errors and serialization

- Separate transport objects from validated domain models; encode/decode at explicit boundaries.
- Require timeouts, cancellation strategy, status-aware error handling and bounded retries with jitter only for retryable/idempotent operations.
- Distinguish errors safe for users from diagnostic details; redact tokens, device IDs where sensitive and response bodies containing personal data.
- Verify endpoint authentication/refresh policy and avoid leaking Bearer tokens in URL query parameters or logs.
- Handle Unicode, binary encodings, timestamp/timezone precision and compatibility with unknown JSON fields.
- For code generation, inspect generated files' ownership, regeneration commands and reproducible constraints before editing outputs.
- Test malformed/partial payloads, authorization expiration, offline mode, retries and ambiguous mutation outcomes.

Official: https://dart.dev/libraries/serialization/json ; https://dart.dev/tutorials/server/fetch-data
