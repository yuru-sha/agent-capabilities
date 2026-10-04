# Browser, API, and cross-origin boundaries

## XSS and browser sinks

Trace browser-controlled and server-supplied values from source to the exact sink. Distinguish stored, reflected, and DOM-based paths, but review them using the same data-flow method.

Encode for the actual output context: HTML text, attribute, URL, JavaScript, CSS, or another interpreter. Prefer text APIs such as \`textContent\` for text. Avoid converting strings into HTML or JavaScript when not required.

Framework auto-escaping is useful until explicitly bypassed or until data reaches a different sink such as \`innerHTML\`, URL navigation, script construction, or a third-party widget. Sanitization is needed only when rich active markup is an explicit feature; configure it to the allowed feature set.

Treat CSP and Trusted Types as defense-in-depth, not replacements for safe data handling.

## CSRF

A cookie proves that the browser has a credential, not that the intended user initiated the request.

Review all state-changing operations, including unauthenticated forms that create security-relevant state. Do not change state with GET. Apply CSRF protection consistently to unsafe methods and ensure exceptions such as webhooks have their own authentication model.

Review token handling, \`SameSite\`, Origin/Referer/Fetch Metadata checks where used, and JavaScript/API behavior. Do not put CSRF tokens in URLs.

JSON and preflight are not automatic CSRF defenses. Client-side CSRF can arise when legitimate JavaScript is tricked into constructing an unintended state-changing request.

## Same-Origin Policy and CORS

CORS controls which origins may read a response; it is not authentication or authorization.

For credentialed CORS, use explicit allowed origins rather than reflecting arbitrary \`Origin\` values. Keep allowed methods/headers narrow, emit \`Vary: Origin\` when responses vary by origin, and reason about same-origin separately from same-site.

Do not rely on preflight as an authentication gate.

## Security headers

Review final responses at the deployment edge, not only framework defaults:

- CSP;
- clickjacking/frame controls;
- MIME sniffing controls;
- referrer policy;
- permissions policy where relevant;
- HSTS when HTTPS deployment is ready for it;
- caching behavior for sensitive responses;
- cookie attributes.

Headers are boundary-specific controls; they do not repair server-side authorization or injection flaws.

## API review

Treat APIs as directly callable HTTP interfaces regardless of what the UI exposes.

Check:

- object-level and function-level authorization;
- explicit response properties to avoid excessive data exposure;
- explicit writable properties to avoid mass assignment;
- method and \`Content-Type\` contracts;
- structured, non-sensitive error responses;
- pagination, collection limits, request size, and expensive-query bounds;
- automation/abuse resistance for valuable workflows;
- versioned and forgotten endpoints;
- external API responses as untrusted input.

Use API-security taxonomies as planning indexes, not substitutes for application-specific authorization and state analysis.

## Client-side trust boundaries

Review URL fragments/query strings, DOM data, \`postMessage\`, Web Storage, indexed state, service workers, browser extensions, and third-party scripts as separate trust boundaries.

For \`postMessage\`, validate sender origin and message schema separately. Browser storage is storage, not a source of truth or a safe place for long-lived secrets by default.

Frontend role checks and hidden controls are never sufficient authorization.

## WebSocket

Authentication at connection establishment is not enough. Review authorization after connection for channels/topics/objects and for each sensitive message/action. Also review message size, rate, schema validation, origin expectations, and session revocation behavior.
