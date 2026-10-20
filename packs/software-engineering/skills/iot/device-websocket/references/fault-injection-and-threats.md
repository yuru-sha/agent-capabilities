# Cross-layer failure test matrix

| Injected fault | Required check |
| --- | --- |
| BLE permission revoked or interrupted pairing | terminal/cancel behavior, no stale callbacks |
| BLE disconnect mid-chunk | bounded reassembly, no partial command execution |
| ESP-NOW drop/duplicate/reorder/channel change | retries, ACK/dedup and stale TTL rejection |
| WebSocket closes after command send | reconciliation by command ID, no repeat actuation |
| Multiple clients control one device | ACL, ordering and independent queue bounds |
| Token expires or device unbound | terminate authorization, reject next command |
| Slow peer / queue overflow | bounded memory and documented drop/disconnect policy |
| Device power loss/reboot | safe startup, authenticated resumption and key retention |

Use deterministic simulated transports and clocks for state-machine tests, then OS/device HIL tests for radio timing, hardware authorization and power failure. Threat boundaries include BLE pairing vs app authorization, ESP-NOW peer identity, device-to-cloud TLS, cross-user binding and command replay. Never treat network encryption as end-to-end actuator authorization.

Example: https://github.com/m5stack/StackChan
