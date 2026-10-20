---
name: iot-ble
description: Use for BLE discovery, GATT, pairing, lifecycle and secure device communications.
---

# iot-ble

Inspect target stack, SDK version, peer roles and trust boundaries before suggesting APIs. This is a language-independent, protocol-specific skill.

## Reference routing
- [gatt-and-framing](references/gatt-and-framing.md)
- [lifecycle-and-security](references/lifecycle-and-security.md)

## Rules
- Load only the relevant references; confirm current official documentation and device constraints.
- Compose with Go, Dart/Flutter, ESP-IDF or other language skills for concrete implementation APIs.
- Keep transport guarantees separate from application authorization, message acknowledgement and physical safety.
- Do not duplicate generic HTTP/OpenAPI or language networking guidance.
