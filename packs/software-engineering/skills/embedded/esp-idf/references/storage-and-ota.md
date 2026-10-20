# Partitions, NVS and OTA

- Inspect partition CSV, flash size, bootloader/partition offsets and target capabilities. Confirm OTA slot count, app size, rollback states and data partition space before accepting an artifact.
- Version persisted NVS schemas and handle missing/corrupt entries gracefully. Avoid storing secrets in plaintext where device threat model requires encrypted NVS or flash encryption; use safe key provisioning.
- Define update staging, integrity/signature verification, anti-rollback policy where applicable, trial boot, self-test, mark-valid and automatic rollback; test loss of power mid-download and mid-boot.
- Preserve device identity, calibration and user data across updates. A full erase is destructive and must never be a default recovery suggestion.
- For secure boot, flash encryption and eFuse provisioning: verify release-mode implications and irreversible effects; require explicit operator authorization and physical recovery plan.
- Never embed production Wi-Fi passwords, cloud API tokens or private keys in firmware, logs, issue reports or fixtures.
- Verify rollback/recovery with a known-good image and a target matching production flash layout.

Primary docs: https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/api-reference/storage/partition.html ; https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/api-reference/storage/nvs_flash.html ; https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/api-reference/system/ota.html ; https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/security/flash-encryption.html
