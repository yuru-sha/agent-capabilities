# Secret model, access, and caching

Name and tag secrets from stable workload/environment ownership.

Grant `GetSecretValue` only to intended workload roles and scope resource ARNs where practical.

Client-side caching can reduce API cost and latency. Define cache TTL/refresh behavior so rotation becomes visible without excessive calls.

Never print secret values in logs, plans, CI output, examples, or incident artifacts.
