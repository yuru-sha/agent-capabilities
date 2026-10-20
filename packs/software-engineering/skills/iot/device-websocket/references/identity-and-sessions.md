# Identity, sessions and messages

- Distinguish authenticated user, registered physical device, gateway and connection session. Enforce user-to-device binding on every privileged command, not just during handshake.
- Use WSS, certificate validation, revocable scoped credentials; never use an arbitrary client-supplied device ID as authorization or leak tokens in logs/URLs.
- Define states: disconnected → authenticating → connected → degraded/reconnecting → stopped. Superseded sessions must not execute stale commands.
- Specify a versioned message envelope: type, command ID, session/epoch, timestamp/TTL, payload size, correlation and validation.
- Define binary/JSON limits, max received frame/message size, heartbeat (protocol ping/pong vs app health) and secure server/browser origin handling.

Source: https://www.rfc-editor.org/rfc/rfc6455
