# Rotation, versions, and recovery

Understand version IDs and staging labels such as current/previous when implementing rotation and rollback.

Rotation must coordinate credential creation, resource update, validation, and stage promotion. Make each step idempotent where retries are possible.

Test application behavior during rotation overlap and stale-cache windows.

Define recovery when rotation fails halfway or when the newly promoted credential is unusable.
