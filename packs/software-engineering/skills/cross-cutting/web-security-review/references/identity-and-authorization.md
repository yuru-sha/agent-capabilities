# Identity, session, and authorization review

## Authentication

Review authentication as a collection of entry points, not only the login form:

- registration and account activation;
- login and logout;
- password change and reset;
- MFA/passkey enrollment and recovery;
- account recovery and identity changes;
- token/API-key issuance and revocation.

Check for account enumeration through response status, body, timing, email behavior, and reset flows. Keep externally visible responses appropriately generic while retaining useful internal audit detail.

Password storage should use a modern password-hashing scheme with per-password salt and tunable cost. Treat peppers, if used, as server-side secrets with rotation/operational implications. Review upgrade/rehash behavior when parameters change.

Rate limiting and lockout controls must consider online guessing without creating an easy denial-of-service primitive. Verify the reset/recovery path is not a weaker authentication channel than the primary login.

## Session lifecycle

Trace the complete lifecycle: creation, privilege change, renewal, expiration, logout, revocation, and reuse of copied credentials.

Review:

- cookie \`Secure\`, \`HttpOnly\`, and appropriate \`SameSite\` attributes;
- cookie scope (\`Domain\`, \`Path\`) and naming/prefix conventions where applicable;
- session identifier rotation across authentication or privilege elevation;
- idle and absolute lifetime semantics;
- server-side invalidation when immediate revocation is required;
- reauthentication for sensitive operations;
- session/token leakage into URLs, logs, error messages, analytics, or client storage.

A signed client-side session protects integrity, not secrecy. JWT does not eliminate session-lifecycle, revocation, leakage, authorization, or replay concerns.

## Authorization model

Describe each authorization rule using at least:

- subject (who acts);
- object/resource (what is targeted);
- action (what is attempted);
- relationship/tenant boundary;
- object/application state.

Prefer default deny. Express important policy server-side and keep it consistent across HTML, API, admin, alternate-version, and background-processing entry points.

## Object-level authorization

Test with at least two ordinary users where ownership or privacy exists. Change only the object identifier and verify the server does not rely on identifier secrecy.

Look for IDOR/BOLA patterns in read, update, delete, download, message, attachment, export, nested-resource, and batch endpoints.

When possible, include authorization predicates in the data-selection query so unauthorized objects are not loaded and filtered only afterward.

## Function-level authorization

Hiding a button or route link is not authorization. Directly request privileged routes and actions under lower privilege.

Check that newly added admin or privileged routes cannot omit the common authorization guard. Prefer shared enforcement plus tests that enumerate or cover the privileged route set.

Do not assume administrators may read every object. Model distinct administrative duties such as user management, moderation, support, audit, and security operations as separate capabilities where the product requires it.

## Client-controlled authoritative fields

Reject mass-assignment/over-posting of fields the server should own, including owner IDs, tenant IDs, roles, price, approval status, workflow state, quotas, or computed entitlements. Accept only explicitly writable properties and derive authoritative values server-side.

## Error behavior

Choose 403 versus 404 deliberately. Use consistent behavior where resource existence itself is sensitive. Do not rely on status codes alone; compare body, timing, and side effects for existence leaks.

## Regression matrix

Represent authorization expectations as a matrix across subject, role, tenant, object owner/relationship, object state, action, and entry point. Add negative tests for denied combinations and positive tests for permitted ones.
