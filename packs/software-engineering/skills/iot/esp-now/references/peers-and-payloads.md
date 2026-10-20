# Peers, channels and payloads

Inspect ESP-IDF version/chip, supported ESP-NOW frame sizes, radio interface, Wi-Fi role, peer configuration and channel restrictions. Do not assume all ESP32 chips and protocol versions share limits.
- Configure peers only after confirming Wi-Fi initialization and current channel; account for station/AP coexistence and channel change.
- Define explicit versioned payloads with source, message ID, command, length, sequence/epoch, TTL and bounded parser validation.
- Send/receive callbacks may run in Wi-Fi task context: enqueue minimum data to bounded worker queues; avoid expensive work, blocked waits and direct actuator commands.
- Differentiate peer-level encryption support from unencrypted/broadcast traffic; do not assume peer MAC alone proves authorization.

Official: https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/api-reference/network/esp_now.html
