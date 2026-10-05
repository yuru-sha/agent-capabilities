# Key policies, IAM, and grants

Every KMS key has a key policy. Review it separately from identity policies and service/resource policies.

Separate key administrators from principals allowed to encrypt/decrypt.

Use grants for bounded delegation, especially AWS service integrations, and understand retirement/revocation ownership.

Constrain permissions with encryption context, ViaService, caller account, resource aliases/tags, or other conditions when they correctly express the trust boundary.
