# Conditional XiaoZhi protocol integration

Only load this reference when the project actually uses the XiaoZhi ESP32 ecosystem. XiaoZhi protocol behavior depends on the selected repository revision, server deployment and transport. **Do not treat these notes as a normative universal spec.**

Primary implementation-derived protocol reference: https://github.com/78/xiaozhi-esp32/blob/main/docs/websocket.md
Implementation/release/license source: https://github.com/78/xiaozhi-esp32
Motivating integration example: https://github.com/m5stack/StackChan

Before implementing:
1. Pin and inspect the precise upstream commit, `LICENSE`, component/model licenses, selected transport (WebSocket vs alternatives), server compatibility and deployed auth/provisioning behavior. Review current source if documentation differs; document uncertain fields rather than guessing.
2. For documented WebSocket flows, evaluate the `hello` exchange, protocol version, supported features, audio format, session IDs and binary payload variant. Illustrative repository documentation includes authorization/device/client identification headers and Opus audio parameters; these are **version-dependent**, not fixed project defaults.
3. Define format/channel/sample-rate/frame-duration negotiation and validate server responses. Do not assume every XiaoZhi server implements all optional features or binary protocol versions.
4. Use scoped, revocable credentials and verify device binding server-side. A MAC-like Device-Id header is not proof of possession; do not expose production tokens, device IDs or audio recordings in logs.
5. Separate control JSON events from binary audio, handle message size/version validation, turn interruption, end-of-speech and duplicated/stale messages; confirm event names against the pinned source implementation.
6. Run contract tests against the **actual** target server and HIL audio tests. Track protocol drift, upstream license compliance and deployment terms at each version upgrade.

When authoritative docs, licensing or server behavior cannot be confirmed, stop at an integration checklist and explicitly mark implementation details unverified.
