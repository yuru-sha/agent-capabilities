# Lifecycle, versioning, and retention

Use lifecycle rules to transition or delete objects according to age, storage class, versions, prefixes, or other supported conditions.

Versioning and retention solve different problems. Versioning preserves replaced/deleted generations; retention policies and object holds prevent deletion until policy conditions are satisfied.

Treat retention-policy locking as an irreversible governance action.

Define restore/recovery procedures for accidental overwrite/delete and test them before relying on versioning as backup.

Choose storage class from access frequency and retrieval economics, and avoid aggressive transitions that conflict with actual usage patterns.
