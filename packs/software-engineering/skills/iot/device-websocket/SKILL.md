---
name: device-websocket
description: Use for Authenticated bidirectional IoT WebSocket sessions, heartbeats, flow control and recovery.
---

# device-websocket

Inspect target stack, SDK version, peer roles and trust boundaries before suggesting APIs. This is a language-independent, protocol-specific skill.

## Reference routing
- [identity-and-sessions](references/identity-and-sessions.md)
- [recovery-and-backpressure](references/recovery-and-backpressure.md)
- [fault-injection-and-threats](references/fault-injection-and-threats.md)

## Rules
- Load only the relevant references; confirm current official documentation and device constraints.
- Compose with Go, Dart/Flutter, ESP-IDF or other language skills for concrete implementation APIs.
- Keep transport guarantees separate from application authorization, message acknowledgement and physical safety.
- Do not duplicate generic HTTP/OpenAPI or language networking guidance.
