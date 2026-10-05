# Scaling, retention, and backpressure

## Stream mode and scaling

Choose stream capacity mode from traffic predictability, control requirements, and cost. In provisioned mode, shard count is part of the capacity contract; in on-demand modes, still design partition keys to avoid concentrated hot keys.

When resharding, expect consumer topology changes and allow the consumer library to discover child shards safely.

## Retention

Use retention long enough to cover the longest credible downstream outage plus replay/recovery needs. Longer retention improves recovery flexibility but changes cost and operational replay volume.

Do not use retention as a permanent archive. Send durable analytical or compliance copies to an appropriate storage system when required.

## Backpressure

Track iterator age/consumer lag and downstream saturation. When downstream systems slow:

- limit consumer concurrency;
- reduce batch size if sink latency/limits require it;
- use bounded retries with jitter;
- pause or shed non-critical derived work where the application contract allows;
- scale the sink before scaling consumers blindly.

A faster consumer that overwhelms its sink increases retry traffic and can worsen lag.

## Poison records

Define a strategy for records that repeatedly fail: bounded retries, failure destination/quarantine storage, alerting, operator inspection, and safe replay after correction. Never allow one malformed record to block a shard indefinitely without an explicit policy.
