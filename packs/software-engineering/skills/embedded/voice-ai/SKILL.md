---
name: voice-ai
description: Use for embedded conversational audio pipelines, wake-word/VAD/ASR/LLM/TTS, real-time playback, voice-session lifecycle, privacy and optional XiaoZhi integration.
---

# Embedded voice AI

Start with the device's audio hardware, target SoC, SDK/model versions, capture/playback topology, server boundary and user consent. Keep the core pipeline platform-neutral.

## Reference routing
- [Capture, signal processing and codec pipeline](references/audio-pipeline.md)
- [Sessions, interruption and network resilience](references/session-and-streaming.md)
- [Privacy, security and observability](references/privacy-and-security.md)
- [Host and hardware test matrix](references/testing-and-performance.md)
- [Conditional XiaoZhi integration](references/xiaozhi-integration.md) — read only when the project actually uses XiaoZhi.

## Boundaries
- Compose with `esp-idf` / `embedded-peripherals` for ESP-SR, I2S and codec drivers, `device-websocket` for generic socket semantics, and language Skills for implementation APIs.
- Do not hardcode XiaoZhi message frames as a universal voice-agent protocol.
- Verify versions, licensing, hardware capabilities and authoritative documentation before recommending integration steps.
- Never start capture, transmit voice or actuate a device without appropriate authorization and consent.
