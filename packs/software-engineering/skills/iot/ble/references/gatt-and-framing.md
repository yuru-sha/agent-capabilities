# Discovery, GATT and framing

Check central/peripheral roles, SDK, Bluetooth version, advertising filters and service/characteristic UUIDs. Prefer service discovery to identifying devices by potentially randomized MACs.
- Distinguish scanning, connecting, pairing/bonding, service discovery, notification subscription and app authorization.
- Request Android/iOS permissions at point of use, handle denial/revocation and background restrictions; stop scans on cancel.
- Define read/write/write-without-response/notify/indicate behavior. Negotiate MTU where available and compute actual ATT payload overhead; do not assume requested MTU is granted.
- Frame multi-chunk messages with version, length, ID, sequence, timeout, bounds, reassembly and integrity; cap memory and in-flight writes.
- Test short MTU, malformed attributes, missing services, duplicate notifications, chunk loss and rapid device switching.

Primary references: https://www.bluetooth.com/specifications/specs/ ; https://developer.android.com/develop/connectivity/bluetooth/ble/ble-overview ; https://developer.apple.com/documentation/corebluetooth
