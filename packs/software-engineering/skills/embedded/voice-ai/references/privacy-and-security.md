# Audio privacy, authorization and operational limits

- Determine whether recording is always-on, wake-triggered or push-to-talk; disclose capture and cloud transmission, offer an accessible mute control and respect microphone permissions.
- Minimize retention of raw audio, transcriptions, speaker identifiers and conversation history. State storage region, retention and deletion policy from actual product requirements.
- Require TLS/certificate validation, device identity and scoped credentials for remote ASR/LLM/TTS. Use authorized device-to-user bindings before executing tool/actuator commands.
- Avoid sending tokens in URLs, persisting secrets in firmware or dumping raw audio/text into debug logs; redact IDs and sensitive transcripts.
- Treat transcribed speech and returned model text as untrusted instructions. Apply explicit allowlists, confirmation and physical safety checks to privileged operations.
- Monitor stage latency, VAD/wake rates, ASR timeout, underrun/overrun, task CPU/stack, codec buffer queue depth, reconnect count and user-visible failures without recording conversation content unnecessarily.
- Verify third-party voice cloning/voice assets, models and components for license and consent before shipping.
