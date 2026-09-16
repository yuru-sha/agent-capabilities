---
name: frontend-form-validation
description: "Use when building or reviewing cross-framework web forms involving semantic controls, input purpose or autocomplete, client and server validation, submission lifecycle, pending or error states, focus management, or progressive enhancement."
---

# Frontend Form Validation

Use with `frontend-web-quality` and the global `$tdd` skill. Compose
`typescript-dom-accessibility` or a framework specialist when those concerns
are independently in scope. Keep this Skill focused on the form contract
across browsers, renderers, and frameworks.

## Rules

- Start with a real `<form>`, native controls, labels, `name`, `id`,
  meaningful `type` and `inputmode`, and valid `autocomplete` tokens.
  Use `fieldset` and `legend` for related controls and native constraint
  validation before custom widgets or duplicated event handling.
- Treat client validation as immediate guidance, not the trust boundary.
  Validate untrusted values on the server, enforce authorization and business
  rules there, and map the server's field-level and form-level result back to
  the preserved user input.
- Make the submission lifecycle explicit: editing, client-invalid, submitting,
  pending, accepted, server-invalid, network-failed, and retry. Prevent
  duplicate submissions without making recovery or the current state
  invisible.
- Associate each error with its control, expose invalid and pending state to
  assistive technology, keep instructions concise, and move focus to the first
  actionable error or summary without destroying the user's context.
- Preserve a meaningful `action` and `method` and a usable server-handled
  path when JavaScript is absent or fails. Progressive enhancement may improve
  feedback and pending UI, but critical validation and submission must not
  depend only on client code.
- Keep form data, redirects, tokens, and rendered messages safe at their
  boundaries. Use the repository's existing schema or validation mechanism
  when one exists instead of introducing a second contract.

## Verify

Test the public form flow with keyboard and supported pointer or touch input.
Cover native constraints, valid submission, server field and form errors,
pending and duplicate-submit behavior, focus restoration, network failure and
retry, autocomplete purpose, and the no-JavaScript path when progressive
enhancement is required. Run the repository's existing type, lint, build,
accessibility, and browser checks; do not add a browser dependency solely to
apply this Skill.

## References

- [HTML Standard: Forms](https://html.spec.whatwg.org/multipage/forms.html)
- [WAI Forms Tutorial](https://www.w3.org/WAI/tutorials/forms/)
- [MDN: autocomplete](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete)
