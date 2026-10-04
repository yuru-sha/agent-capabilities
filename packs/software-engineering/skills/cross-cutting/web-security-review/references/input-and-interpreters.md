# Input, interpreters, files, and server-side requests

## Validation model

Treat all external data as untrusted, including stored data and external-service responses. Validate against the application contract on the server side.

Review required versus absent versus empty values, type conversion failures, length/range/count/size limits, allow-listed enumerations and structured values, parameter pollution, normalization policy, unknown JSON properties, and validation before persistence or side effects.

Client-side validation improves UX but is not a security boundary. Sanitization and validation serve different purposes.

## SQL and query injection

Trace input into ORM escape hatches, raw SQL, dynamic identifiers, sort/order expressions, LIKE patterns, and filter DSLs.

Use parameter binding for data values. For identifiers or operators that cannot be bound, choose from server-defined allow lists. Validation does not replace parameterization.

Do not conclude SQL injection from a quote-triggered error alone. Confirm that controlled input can change query meaning or produce a comparably decisive effect.

## Command and argument injection

The preferred fix is to avoid invoking an external process when an in-process library can perform the operation.

If a subprocess is necessary:

- avoid shells;
- pass arguments separately;
- use fixed executable paths;
- constrain option-like arguments with allow lists or command-specific delimiters where supported;
- control environment, working directory, timeout, output size, and privilege.

\`shell=False\` reduces shell parsing but does not remove argument/option injection into the invoked program.

## Template injection

Distinguish template source from template data. User-controlled content must not become executable template source. Auto-escaping addresses output encoding, not server-side template injection.

Review dynamic template names, template context exposure, stored input rendered later, sandbox/resource limits if user-defined templates are an explicit product feature, and debug/error output.

## Path traversal and filesystem boundaries

Prefer opaque IDs or server-side mappings instead of accepting filesystem paths from users.

If paths are accepted, resolve them canonically and verify the resolved object remains under the intended base directory. Do not use string-prefix checks as a parent/child proof. Consider symlinks and archive-entry paths separately.

Review read, write, delete, template lookup, language/theme selection, archive extraction, and download handlers independently. OS/container permissions limit impact but do not fix traversal.

## File upload and delivery

Model the full lifecycle: receive, inspect, transform, name, store, serve, replace, and delete.

Do not trust browser \`accept\`, original filename, or client \`Content-Type\`. Generate server-side storage names. Allow only formats required by the feature, enforce byte and post-decode/decompression bounds, and separate untrusted storage from executable locations.

For images or transformable formats, distinguish parser verification from actually re-encoding into a known-safe representation. Treat archives as nested untrusted input.

When serving uploads, set intended content type and disposition. Avoid serving active content from the same trusted origin unless explicitly required and safely handled.

## SSRF

First ask whether arbitrary outbound URLs are a real requirement. A fixed destination or server-side resource identifier is safer than general URL fetching.

If arbitrary outbound requests are required, reason separately about scheme, hostname/port, IPv4/IPv6 and DNS, redirects, credentials/headers/body forwarded, timeout/response size, response data returned to the requester, and network egress policy.

Parsing a URL successfully does not make it safe. Network egress restrictions are a second boundary, not a substitute for application validation.

## XML and deserialization

For XML, review DTD/entity behavior, external-resource access, parser version/configuration, document size/depth, schema/value validation, and XPath construction. Schema validation is not an XXE control.

Do not deserialize untrusted bytes with object formats capable of code execution. Prefer simple data formats such as JSON plus explicit schema/value checks. For YAML, select a safe loader appropriate to the library. A signature only supports the trust model if key ownership and producer authorization are themselves sound.
