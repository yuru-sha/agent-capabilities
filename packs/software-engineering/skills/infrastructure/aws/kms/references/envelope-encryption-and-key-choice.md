# Envelope encryption and key choice

Use data keys/envelope encryption for application payloads. KMS protects the data-encryption key while the application/service encrypts bulk data locally.

Choose key type/spec/usage according to encrypt/decrypt, sign/verify, MAC, or asymmetric interoperability needs.

Customer-managed keys add policy, lifecycle, audit, and operational responsibility; use them when those controls are required rather than by reflex.

Keep plaintext data keys in memory only as long as required and never persist or log them.
