# Connectivity, auth, and configuration

Place databases in private subnets unless a documented exceptional requirement exists.

Review security groups, DNS endpoints, TLS verification, IAM database authentication where supported, secret rotation, and KMS access together.

Treat parameter/option group changes as operational changes; know which settings are dynamic and which require reboot.

Use Secrets Manager or approved secret delivery rather than embedding DB passwords in source or images.
