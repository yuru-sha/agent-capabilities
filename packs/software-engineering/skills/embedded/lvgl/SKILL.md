---
name: lvgl
description: Use when building or reviewing LVGL embedded interfaces, display/touch ports, event lifecycle, rendering buffers and UI task concurrency.
---

# LVGL

Identify LVGL major version, port (including esp_lvgl_port if used), SoC, display bus and UI task ownership. Use only the relevant references.

## References

- [Thread ownership and lifecycle](references/concurrency-and-lifecycle.md)
- [Display, touch and performance](references/display-and-performance.md)
- [Embedded UI verification](references/testing.md)

## Boundaries

- Do not apply browser DOM/React advice to LVGL.
- Compose with `esp-idf` and `embedded-cpp` for target-specific drivers and resource control; with `embedded-peripherals` for buses and sensors.
- Confirm LVGL and port versions against official documentation before using APIs. Rendering must not issue unsafe actuator commands directly.
