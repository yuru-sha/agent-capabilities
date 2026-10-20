---
name: embedded-peripherals
description: Use for MCU hardware abstraction, GPIO, I2C, SPI, UART, PWM, sensors, cameras and peripheral ownership, timing and fault recovery.
---

# Embedded peripherals

Inspect board revision, schematics, voltage/current ratings, pin mux, bus topology and firmware/HAL boundaries first. Load only matching references.

## References

- [HAL and bus ownership](references/hal-and-buses.md)
- [Sensors, camera and audio](references/sensors-and-media.md)
- [Resource and HIL test checklist](references/resource-and-testing.md)

## Boundaries

- This is a language-neutral hardware integration Skill; use `esp-idf` for Espressif APIs, `lvgl` for UI and `embedded-motion` for actuator safety.
- Never invent pinouts, safe voltage levels, timing constraints or calibration constants.
