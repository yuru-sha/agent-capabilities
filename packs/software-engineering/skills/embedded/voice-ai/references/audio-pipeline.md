# Capture → recognition → response → playback

- Draw the actual path: microphone/I2S codec → optional AEC/noise suppression/beamforming → wake word/VAD → capture segmentation → ASR → LLM/tools → TTS → audio decoder/resampler → speaker.
- Identify which stages run locally vs server-side. Wake word, VAD and ASR are distinct; ESP-SR capabilities vary by chip, model and selected component version.
- Document PCM bit depth, channels, sample rate, frame duration, endianness, Opus/PCM encoding and explicit resampling boundaries. Verify device/codec capabilities before assuming 16 kHz mono.
- Bound ring buffers and processing queues, control PSRAM/DMA ownership, plan I2S interrupts and avoid decoding/HTTP work in audio callbacks. Measure audio end-to-end latency per stage.
- Prevent speaker-to-mic feedback using suitable AEC and gain strategy where supported, including reference-channel alignment and tail latency.
- Handle VAD false starts, false rejects, quiet speech, ambient noise, wake-word false triggers and simultaneous playback/capture.
- Define what happens when LLM/tools are unavailable: no blocking of capture tasks, bounded fallback response, and no stale audio played after a new turn.
- Choose codecs based on transport bandwidth, compute budget, algorithmic delay and packet-loss concealment; use negotiated formats, not implicit assumptions.

Official: https://docs.espressif.com/projects/esp-sr/en/latest/esp32s3/audio_front_end/README.html ; https://github.com/espressif/esp-sr
