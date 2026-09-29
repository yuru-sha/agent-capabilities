---
name: technical-authoring
description: "Use when designing or writing technical books, explanations, tutorials, how-to guides, procedures, runbooks, troubleshooting guides, references, architecture or design documents, or migration guides."
---

# Technical authoring

Design the document around the reader's task. Use this skill for document structure, technical evidence, executable examples, verification, and operational safety. Use the installed `technical-writing` skill for sentence-level style and mode conventions. Use oh-my-pstack's generic writing workflow where applicable. Use language, database, API, and infrastructure specialists for domain behavior. Do not take over planning, research, review, or orchestration workflows.

## Choose the document type

Honor an explicit type. Otherwise infer it from the reader's outcome. Do not ask the reader to name a category when the request makes the outcome clear.

| Reader's outcome | Document type | Optimize for |
|---|---|---|
| Build understanding progressively | Technical book or long-form explanation | Concept order and a durable mental model |
| Learn through a guided successful build | Tutorial | A working result at meaningful milestones |
| Complete a specific task | How-to guide | The shortest reliable path to the goal |
| Execute a defined operation | Procedure | Safe, repeatable steps and completion criteria |
| Act during live operations | Runbook | Fast scanning, observable state, and clear decisions |
| Find a cause and resolve a symptom | Troubleshooting guide | Evidence-driven diagnosis and recovery |
| Look up exact behavior or options | Reference | Precise, complete retrieval |
| Understand system structure or a decision | Architecture or design document | Boundaries, rationale, constraints, and tradeoffs |
| Move between versions or system states | Migration guide | A verified, recoverable state transition |

Keep one primary document type. Include another type's material only when the reader needs it; otherwise link to a separate document rather than mixing modes.

## Establish the reader contract

Before choosing sections, establish:

- **Audience:** who will use the document, their technical level, and knowledge it assumes.
- **Purpose:** what the reader should understand, build, operate, diagnose, retrieve, decide, or migrate.
- **Starting state:** the versions, permissions, environment, configuration, and existing system state the instructions require.
- **Evidence:** what source supports each material technical claim and what observation proves an action worked.

State prerequisites before the steps that depend on them. Use the project's established terminology. Introduce unfamiliar terms before relying on them. Do not invent commands, APIs, configuration, version behavior, compatibility, errors, or rationale. Inspect the implementation or authoritative source when available. Label an inference or unresolved fact, and identify evidence gaps that affect safe use.

## Shape the document for its type

### Technical book or long-form explanation

Build from prerequisites through concepts and their dependencies. Define learning outcomes and a concept order before writing chapters. Introduce foundational concepts before dependent ones; mark any assumed knowledge explicitly. For each major concept, explain the idea, show a minimal example, then connect it to a practical case and relevant limits. Keep examples consistent when they build on earlier chapters. Separate the mental model from implementation details. End a chapter with a concise recap and a bridge only when it prepares the next concept. Use exercises or checks when they test a real learning objective. Avoid repeated definitions, unexplained code, heading-heavy fragments, and length without new understanding.

### Tutorial

Name the result the reader will build. State prerequisites and the starting state. Guide one coherent path to a working outcome. Break the path into steps that produce visible results; state expected observations at meaningful milestones. Keep optional branches out of the primary path. Explain only what the reader needs at that point. Finish with the complete result, what the reader accomplished, and a useful next destination.

### How-to guide

Name the task in the title. State the prerequisites, then give the minimum reliable steps for the stated goal. Put verification after the action. Include only caveats that change the choice or outcome. Link to an explanation for background instead of turning the guide into a tutorial.

### Procedure

Include the sections the operation needs: purpose, scope, prerequisites, permissions, impact, pre-checks, steps, verification, failure handling, rollback, and completion criteria. For each consequential step, state the action, exact command or operation, expected result, and verification. Give a concrete failure path. Surface service interruption, data-loss risk, irreversible effects, backup requirements, production impact, and rollback limits before the relevant action. Do not replace specific checks with "verify that it works."

### Runbook

Put the trigger, applicability, severity, and immediate safety checks near the top. Make current-state checks, decision branches, actions, expected observations, recovery verification, rollback, escalation conditions, and evidence to collect easy to scan. Separate diagnostic checks from changes that remediate the issue. State when to stop and escalate. Do not bury urgent actions in background explanation.

### Troubleshooting guide

Organize by observable symptom. Use checks that distinguish likely cause categories and make the next branch explicit. Prefer low-risk diagnostics before remediation. For each branch, state the evidence, what it implies, the next check or action, and how to verify recovery. Keep diagnosis separate from remediation. Include escalation when evidence does not narrow the cause or a safe fix is unknown.

### Reference documentation

Organize entries to match the API, command, configuration, or other subject so readers can predict where facts live. Use searchable headings and consistent fields. Document applicable names, purpose, syntax, parameters and types, defaults, constraints, results, errors, side effects, examples, and compatibility. Be concise, factual, and complete within the stated scope. Generate from the authoritative source when the project supports it.

### Architecture or design document

Capture the context, goals and non-goals, constraints, boundaries, components and responsibilities, interfaces, data and control flow, dependencies, failure and trust boundaries, operational concerns, tradeoffs, limitations, and decisions that matter. Distinguish current behavior from proposed design and explain why a decision exists only when evidence supports the rationale. Identify rejected alternatives only when the decision record or source material establishes them.

### Migration guide

Name the source and target states and supported versions. State compatibility constraints, prerequisites, risks, backup and recovery preparation, downtime requirements, pre-checks, ordered migration steps, intermediate and final verification, rollback strategy, breaking changes, irreversible steps, and post-migration cleanup. Make each state transition explicit. Do not promise zero downtime or rollback where evidence does not support the claim.

## Make executable content verifiable and safe

Treat every example and command as part of the contract. Verify syntax against the repository, specification, or authoritative versioned source when available. Include required imports, dependencies, versions, and prior state. State expected output when it helps detect failure. Use the smallest example that teaches the point. Mark simplifications and distinguish them from production guidance.

For every executable step, ask how the reader can observe success. Prefer a concrete exit status, test result, response, service state, database state, log, artifact, UI state, or metric. State what to do when the check fails. Do not present an unverified command or expected output as fact.

Before destructive or production-impacting actions, state the risk, required authority, backup or recovery preparation, and rollback limits. Isolate dangerous actions rather than hiding them in a large command block. Do not recommend a destructive fix before gathering lower-risk evidence unless urgency and evidence justify it.

## Keep the document maintainable

Keep each section aligned with the selected reader outcome. Use cross-references only when they reduce duplication without making the reader lose the task. Prefer one clear explanation and one relevant example over repeated caveats or abstraction. Keep examples, paths, versions, and generated material aligned with their source of truth. Record unresolved assumptions where maintainers can find them; do not turn guesses into durable claims.
