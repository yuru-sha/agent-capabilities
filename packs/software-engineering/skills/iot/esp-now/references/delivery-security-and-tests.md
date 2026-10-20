# Delivery and safety

- Link-layer send success does not prove an application command ran. Add app-level ACK/correlation when needed.
- Design retries with bounded exponential backoff, duplicate suppression and stale-command expiry; do not re-run non-idempotent physical actions on duplicate delivery.
- Configure PMK/LMK protection as supported; provision/rotate secrets securely. Threat model spoofing, replay, jamming, firmware reset and peer removal.
- On lost control link, enter an explicitly safe physical state defined by device specifications.
- Test packet loss, duplicates, out-of-order delivery, channel mismatch, Wi-Fi reconnect, reboot, simultaneous transmitters and bounded queues using real hardware where needed.

Official: https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/api-reference/network/esp_now.html
