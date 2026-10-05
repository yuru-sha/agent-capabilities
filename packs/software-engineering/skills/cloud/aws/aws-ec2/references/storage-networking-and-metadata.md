# Storage, networking, and metadata

Choose EBS volume type, size, IOPS, throughput, encryption, snapshot, and delete-on-termination behavior explicitly.

Review ENI/subnet/security-group placement and private/public addressing with VPC topology.

Use IMDSv2 and constrain hop limits/access where containers or untrusted local processes could reach metadata.

Do not place long-lived AWS credentials on disk when an instance profile can provide short-lived credentials.
