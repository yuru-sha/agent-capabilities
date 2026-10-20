# Servo motion, calibration and validation

- Read datasheet and wiring to identify servo/controller type, supported pulse/frequency, gear ratio, mechanical stops, current and thermal limits.
- Define calibrated soft limits inside verified hard stops, neutral/safe home position, velocity/acceleration limits and maximum command rate.
- Validate every command (including remote UI/network commands) at the actuator boundary: authorization, finite numeric values, units, ranges, freshness/TTL and conflict handling.
- Schedule motion off ISR/UI callbacks, use a single actuator owner and bounded command queue. Deduplicate repeated commands and avoid unsafe replay after reconnection.
- If homing requires motion, verify sensors, obstruction detection and an explicit authorized procedure; do not drive blindly into a hard stop.
- Treat sensor feedback as potentially stale or faulty, with clear closed/open-loop fallback and documented physical safety response.
