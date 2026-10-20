# Sensors, cameras and audio peripherals

- Define sensor sampling interval, units, calibration, timestamp and validity state. Reject outliers where justified, and make disconnected/invalid data explicit.
- Camera: confirm clock, pixel format, frame size, DMA/PSRAM budget and ownership across capture/encode/display; bound queues and release framebuffers exactly once.
- Microphone/speaker: verify codec/I2S channel format, clocks, buffer size and latency. Prevent audio underflow/overflow and isolate capture/playback scheduling from UI.
- Separate driver ISR/DMA completion, acquisition and higher-level processing tasks; never retain a buffer beyond its owner contract.
- Treat user-visible camera/microphone activation and stored media as privacy-sensitive; prevent accidental capture/logging or stale UI indicators.
- Test unplug/replug, bus resets, missing frames, empty buffers, concurrent camera/display load and power interruptions.

References: https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/api-reference/peripherals/index.html ; https://github.com/espressif/esp32-camera
