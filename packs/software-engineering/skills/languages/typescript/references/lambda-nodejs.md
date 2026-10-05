# Node.js on AWS Lambda

Use this reference only when a Lambda function is implemented in Node.js/TypeScript. Compose it with the language-independent `lambda` Skill.

Align the configured Lambda runtime with local/CI Node.js versions, `package.json` engines, module format, handler path, architecture, and compiled output.

Use the repository's package manager and authoritative lockfile. Keep production dependencies deterministic and avoid silently relying on a runtime-provided SDK version when reproducibility requires a pinned package.

For AWS SDK for JavaScript v3, instantiate reusable clients outside the handler when safe and import only the required clients/commands.

Verify ESM/CommonJS behavior, source-map handling, handler resolution, and the actual deployment artifact layout. Package only runtime-required code and dependencies; exclude credentials and development-only material.

Run a packaging smoke test in addition to unit tests when module resolution, transpilation, native dependencies, or zip layout can fail independently of handler logic.
