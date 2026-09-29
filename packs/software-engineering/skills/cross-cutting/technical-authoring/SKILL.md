---
name: technical-authoring
description: "Use when designing or writing technical books, explanations, tutorials, how-to guides, procedures, runbooks, troubleshooting guides, references, architecture or design documents, or migration guides."
---

# Technical authoring

Design technical documents around the reader's outcome, and ground technical claims in evidence. Use the installed `technical-writing` skill for Diátaxis mode selection and prose style. This skill adds technical-document structures, source grounding, executable-content checks, and operational safety. Language, database, API, and infrastructure specialists own domain-specific behavior. Do not replace generic project planning, research, review, or orchestration workflows.

## Select the document form

Honor an explicit request. Otherwise infer the reader's outcome. Do not ask for a formal label when the intent is clear.

| Reader's outcome | Document form |
|---|---|
| Build understanding across dependent concepts | Technical book or long-form explanation |
| Learn a technical task through a working result | Tutorial |
| Complete a specific task | How-to guide |
| Execute a defined operation safely and repeatably | Procedure |
| Act during live operations | Runbook |
| Diagnose and resolve a symptom | Troubleshooting guide |
| Retrieve exact technical facts | Reference |
| Understand system structure, constraints, or decisions | Architecture or design document |
| Move between versions or system states | Migration guide |

Use the matching Diátaxis mode from `technical-writing` for tutorials, how-to guides, references, and explanations. Procedure, runbook, troubleshooting, architecture, and migration forms add technical constraints that the four-mode distinction does not specify.

## Ground technical claims

Establish the intended reader, assumed knowledge, goal, and required starting state. State relevant versions, permissions, environment, configuration, and existing system state before dependent instructions. Preserve project terminology and introduce domain terms before relying on them.

For repository-based documents, inspect the implementation, configuration, specification, or other authoritative source that defines the behavior. Do not invent commands, APIs, configuration keys, defaults, version behavior, compatibility, errors, or rationale. Distinguish established behavior from inference. Mark unresolved facts when they affect correctness or safe execution.

## Add technical structure by document form

### Technical book or long-form explanation

Order chapters by concept dependency. Make prerequisites and assumed knowledge explicit. Explain the mental model before relying on implementation details. Connect each concept to a minimal example and, where useful, a practical case and its limits. Keep examples consistent when later chapters depend on earlier code. Reconnect details to the larger model instead of repeating definitions.

### Tutorial

For tutorials with executable steps, state the required tool and dependency versions and the starting project state. Check that each milestone can be reached from the preceding steps. Keep sample code consistent across steps, and distinguish teaching simplifications from production guidance. Show only expected output that has been checked against the stated environment.

### Procedure

Include relevant scope, permissions, impact, prerequisites, pre-checks, actions, verification, failure handling, rollback, and completion criteria. For each consequential action, state the operation, expected state, and observable check. Put data-loss, interruption, irreversible-change, backup, and rollback-limit warnings before the action they constrain.

### Runbook

Put the trigger, applicability, severity, and immediate safety checks where an operator can find them quickly. Use explicit decision branches tied to observable state. Separate diagnosis from remediation. State expected observations, recovery checks, stop conditions, escalation criteria, and evidence to collect.

### Troubleshooting guide

Start with observable symptoms. Choose checks that distinguish likely cause categories, and state what each result implies and which check follows. Gather low-risk evidence before remediation unless urgency and evidence justify a riskier action. Give recovery verification and escalation conditions for each relevant path.

### Reference

Document the technical contract within scope: names, syntax, parameter types, defaults, constraints, results, errors, side effects, and compatibility. Include only fields that apply. Verify each fact against its authoritative source and identify the applicable version when behavior changes by version.

### Architecture or design document

Record the system context, goals and non-goals, constraints, boundaries, component responsibilities, interfaces, data or control flow, dependencies, failure and trust boundaries, operational concerns, tradeoffs, and limitations that matter. Distinguish current behavior from a proposal. State decision rationale and rejected alternatives only when project evidence supports them.

### Migration guide

Name the source and target states and supported versions. State compatibility constraints, prerequisites, risks, backup and recovery preparation, known downtime, and irreversible steps. Describe ordered state transitions with pre-checks and intermediate and final verification. Give rollback conditions and limits, breaking changes, and post-migration cleanup. Do not promise zero downtime or rollback without evidence.

## Verify executable content and protect operations

Treat examples and commands as part of the technical contract. Check syntax and behavior against the repository, specification, or authoritative versioned source when available. Include imports, dependencies, versions, and prior state needed to run an example. State expected output only when verified.

For every operational action, identify how the reader observes success and what to do if the check fails. Prefer concrete exit status, test result, response, service or database state, log evidence, generated artifact, UI state, or metric. Do not use vague completion claims when an observable criterion can be established.

Before a destructive or production-impacting operation, state the required authority, data-loss or interruption risk, backup or recovery preparation, and rollback limitations. Keep dangerous actions distinct from harmless checks. Do not recommend a destructive remediation before lower-risk diagnostics unless urgency and evidence justify it.

## Keep technical documents maintainable

Keep examples, paths, versions, and generated content aligned with their source of truth. Use cross-references when they prevent duplication without interrupting the reader's task. Record material assumptions and evidence gaps where maintainers can update them. Do not turn an unverified inference into a durable guarantee.
