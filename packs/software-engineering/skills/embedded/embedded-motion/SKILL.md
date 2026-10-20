---
name: embedded-motion
description: Use for safe servo and robotic actuator control, calibration, motion limits, feedback, scheduling, watchdogs and fail-safe testing.
---

# Embedded motion

Establish physical hardware model, power rail, emergency-stop behavior, position/velocity limits and whether movement can harm people or equipment before implementing commands.

## References

- [Calibration and safe commands](references/controls-and-limits.md)
- [Fault handling and HIL verification](references/failsafe-and-tests.md)

## Boundaries

- This Skill owns actuator-specific hazards, not generic ESP-IDF PWM wiring, BLE transport or LVGL rendering.
- Never prescribe numeric motion limits without device datasheet and validated mechanical calibration.
- Require authorized, supervised hardware tests before moving physical devices.
