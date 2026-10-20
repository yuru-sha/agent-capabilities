---
name: iot-esp-now
description: Use for ESP-NOW peer/channel management, secure framing, command reliability and Wi-Fi coexistence.
---

# iot-esp-now

Inspect target stack, SDK version, peer roles and trust boundaries before suggesting APIs. This is a language-independent, protocol-specific skill.

## Reference routing
- [peers-and-payloads](references/peers-and-payloads.md)
- [delivery-security-and-tests](references/delivery-security-and-tests.md)

## Rules
- Load only the relevant references; confirm current official documentation and device constraints.
- Compose with Go, Dart/Flutter, ESP-IDF or other language skills for concrete implementation APIs.
- Keep transport guarantees separate from application authorization, message acknowledgement and physical safety.
- Do not duplicate generic HTTP/OpenAPI or language networking guidance.
