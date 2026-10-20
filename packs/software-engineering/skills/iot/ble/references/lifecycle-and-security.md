# Connection state and trust

State machine: idle → scanning → connecting → discovering → ready → disconnecting → idle; timeout/disconnect may enter bounded-backoff reconnection, and cancellation/permission-denial should be terminal until user action.
- Serialize GATT operations as required by the platform and use connection-generation tokens to ignore stale callbacks.
- Cancel scans, subscriptions and pending operations on teardown; handle radio-off, background suspension and disconnected-during-write.
- Pairing/bonding does not authorize sensitive application commands. Evaluate encryption, MITM protection, device capabilities, key storage and revocation against threat model.
- Avoid identifier spoofing, leaking secrets or unbounded auto-connect loops. Require explicit access checks for device-control commands.
- Test reconnect storms, multiple central clients, revoked access, interrupted pairing and stale session events.

Sources: https://developer.android.com/develop/connectivity/bluetooth/permissions ; https://developer.apple.com/documentation/corebluetooth
