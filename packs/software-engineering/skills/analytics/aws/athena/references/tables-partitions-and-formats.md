# Tables Partitions And Formats

Design Athena tables around S3 layout, partition pruning, file size, compression, and columnar formats such as Parquet or ORC. Use partition projection or catalog partitions where they reduce metadata overhead. Avoid many tiny files and unbounded partition scans.
