# Motion safety and hardware tests

- Define safe startup/shutdown, power loss/brownout, watchdog reset and lost communication behavior for the exact mechanism. Do not assume setting PWM to zero stops all actuators safely.
- Provide emergency stop independent of cloud/network availability where the hazard assessment requires it; verify power isolation and brake behavior against device characteristics.
- Fault-injection matrix: invalid/out-of-range command, duplicate/stale command, jam/overcurrent, missing position feedback, power interruption, controller reboot, stalled task, queue overflow and competing clients.
- Test pure trajectory math and state logic on the host. HIL must validate calibrated limits, supply sag, thermal behavior, actual failsafe and stop latency under supervision.
- Log command ID, safety-relevant state transitions and error reason without leaking credentials; do not imply a software check replaces mechanical protection.

Reference: https://www.nist.gov/el/intelligent-systems-division-73500
