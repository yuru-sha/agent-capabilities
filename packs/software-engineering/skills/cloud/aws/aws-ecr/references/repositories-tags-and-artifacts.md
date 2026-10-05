# Repositories, tags, and artifacts

Define repository naming, ownership, encryption, tag mutability, and retention expectations.

Use image digests for immutable deployment identity. If human-readable release tags are used, ensure they map to a controlled immutable artifact.

Avoid reusing environment tags such as `prod` as the only deployment evidence.

Separate multi-architecture manifests and platform compatibility from application version semantics.
