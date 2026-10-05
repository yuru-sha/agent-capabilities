# Instance, AMI, and bootstrap

Select instance families from CPU, memory, network, storage, architecture, accelerator, and burst requirements rather than generic size labels.

Pin or control AMI lineage. Define patch/update ownership and how new AMIs are promoted.

Keep user data/bootstrap idempotent and bounded. Do not fetch unpinned code or credentials during boot.

Prefer immutable replacement for fleet changes. Validate application health after boot instead of treating EC2 running state as readiness.
