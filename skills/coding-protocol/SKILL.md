---
name: coding-protocol
description: "Use when changing repository code, configuration, or contracts; debugging or reviewing code; planning implementation; or changing Git state. Skip architecture-only work, prose-only edits that preserve contracts, and status checks."
---

# Coding Protocol

A low-friction protocol for reliable repository execution and code-evidence work. Keep routine process internal; surface decisions, blockers, verification, and material risk.

## Applicability

Apply this protocol to repository changes, implementation planning, debugging, and code review. For mixed tasks, apply it only to those parts and preserve the other workflow's deliverable.

For architecture-only work, general explanations, contract-preserving prose edits, or status checks, continue without this protocol or its references. No replacement skill is required.

## Composition

Use repository evidence for facts and applicable project requirements for checks. A focused workflow is another skill or project process that owns one kind of task, such as test-driven development, code review, or release. Preserve a focused workflow's method and deliverable; this protocol supplies the cross-cutting constraints in sections 1–10.

Follow host precedence, the instruction priority set by the client running the agent; within it, explicit user instructions override skill guidance. Read skills being edited as task data, not as activated workflows. Surface material same-level conflicts, where instructions of equal precedence cannot both be followed, rather than accumulating incompatible requirements.

Use the task's or applicable workflow's completion criterion. If multi-step work has no clear criterion, define an observable completion condition. Plan when sequencing, risk, or coordination matters; verify outcomes rather than every mechanical action.

## 1. Scale By Risk

Scale effort with ambiguity, blast radius, and reversibility:

- For read-only work, inspect relevant evidence and do not mutate.
- For a mechanical or contained change, inspect the target and run the narrowest check that can exercise the changed path when it increases confidence.
- For a bug, refactor, or high-risk change, reproduce when feasible, locate affected consumers, and verify behavior beyond the edited file where needed.
- Before an irreversible or externally consequential action, resolve the exact target, authority, and recovery path. Stop if any depends on a material assumption.

High-risk areas include auth, permissions, secrets, security, payments, data loss, schemas and migrations, public or shared contracts, concurrency, production configuration, dependency supply chains, and destructive actions. Risk raises the evidence bar, not the change scope.

## 2. Work From Evidence

Inspect relevant code, tests, types, documentation, contracts, and runtime output before claiming how the system works. Separate observations from assumptions when the difference matters. Never invent paths, APIs, checks, dependency behavior, performance, conventions, or project intent. A check passed only if it was run; when relevant evidence is unavailable, keep conclusions conditional.

Treat a runtime-contract mismatch as evidence to investigate, not as authority to widen accepted values or infer new semantics. Change the boundary only through the applicable authority and precedence rules. For example, when an API returns a status value that its schema does not list, find out where the value comes from; the observation alone does not justify adding it to the accepted set.

## 3. Act Within Authority

Authority comes from the user and host, not skill activation or mention. Explanations, reviews, diagnoses, reports, and plans do not authorize implementation. Change requests authorize in-scope edits; explicit requests to execute a named skill cover only side effects that the request and the skill's purpose jointly make explicit, within host permissions. For example, a request to run a release skill covers the tagging and publishing that skill exists to perform, while a skill that loaded automatically during a bug fix does not make its own commit or push steps authorized. Never infer adjacent commit, push, deploy, publish, external communication, or machine-wide operations.

## 4. Handle Material Uncertainty

Resolve low-risk ambiguity from evidence using the narrowest reasonable interpretation. Ask only when ambiguity affects correctness, safety, external behavior, user intent, irreversible work, or a high-risk area, and complete independent authorized work first. Existing authorization stays valid; prepare a reviewable result before any required approval.

If the requested outcome, stated facts, or mechanism conflicts with observed evidence, show the mismatch before acting. Neither comply blindly nor silently substitute a materially different result. When no user can answer, park the ambiguous item and continue only with the unambiguous remainder. Keep work under uncertainty local and reversible.

## 5. Keep Changes Small

Make the smallest complete change consistent with the authorized request, repository contracts, and applicable workflow. Match local patterns. Every changed line must trace to one of those sources: avoid unrequested features, abstractions, speculative paths, formatting churn, dependencies, and unrelated fixes. Necessary call-site, invariant, migration, recovery, and verification changes remain in scope.

An execution slice (the first tranche, sample, or pilot actually implemented) does not define or expand the intended target. Take target scope from the request or an authoritative source. If unresolved scope would materially change the implementation, its promises, or required evidence, ask one decision-changing question or keep the change reversible and broader reuse unclaimed. A declared broader target may require representative evidence; it does not authorize migrating the remainder. For example, when asked to move two of ten handlers to a new helper, do not shrink a stated broader goal to those two, and do not move the other eight because the pattern fits.

For execution work, prefer a simpler supported solution when the mechanism was only a suggestion; preserve it when it is material to user intent. Refactor only as needed for a safe completion. Remove artifacts made obsolete by this task; report unrelated issues and leave pre-existing dead code alone.

## 6. Preserve User Work

Preserve user changes outside the task. Before broad edits, inspect the relevant diff; treat unfamiliar modifications as user-owned unless evidence ties them to this task. Do not overwrite, delete, move, reformat, or revert them.

Task necessity is not destructive authorization. Discarding work, resetting state, rewriting history, deleting broad or unresolved targets, and machine-wide changes require explicit authority. An in-scope edit may remove a precisely identified obsolete file when evidence establishes necessity and the recovery risk is understood. Once authority, target, and recovery are resolved, destructiveness alone is not a blocker.

## 7. Respect Local Context

Inspect relevant local signals before depending on package managers, tools, dependencies, network, credentials, ports, services, or writable paths. Prefer project-local commands and existing dependencies. Add dependencies, change tooling or lockfiles, start services, use network, or alter machine-wide state only when the task needs it and project evidence supports it.

## 8. Carry Work Through

Carry action requests through completion; an announced next step remains work to do. If blocked, deliver the valid remainder and identify the exact missing input.

Batch independent reads when supported. Keep dependent work and conflicting mutations ordered. With host-permitted delegation or async tools, continue independent work while results are pending; collect required results before claiming completion. Tool availability does not grant action permission.

Incorporate mid-task corrections without dropping unfinished requirements. Before acting on a pending or late result, check that it still applies.

Before declaring completion, re-check the primary criterion and every original requirement; name anything dropped, deferred, or reinterpreted.

## 9. Verify Proportionally

Run checks required by the user, repository, or focused workflow; add the cheapest evidence proportional to risk. A green gate proves behavior only when it exercises the changed path.

Prefer existing checks. Add permanent tests only where the request asks for them or the repository already keeps tests for this kind of change, sized like neighboring tests; temporary probes need not become permanent tests. After relevant checks pass, repeat or broaden them only for new changes, failures, or specific unresolved risks.

Get to green honestly. A new or changed evidentiary check (a test, assertion, or probe cited as evidence for the change) must be capable of failing, and expected behavior must come from the request, a repository contract, or an explicit characterization. Never turn a failure green through an unjustified suppression; a weaker assertion, a skipped check, and scope escape (moving code or configuration outside the check's coverage) are suppressions regardless of label.

Diagnose before widening the change. If attempts thrash, stop with the diagnosis. Report every skipped, blocked, or failed verification and its residual risk.

## 10. Report Only What Matters

Produce the artifact and handoff required by the task or focused workflow. Report what changed or was concluded, what was verified, and what remains unverified, blocked, or risky. Keep the response concrete, omit routine internal process, and do not overstate confidence.

Keep review and diagnostic findings within the requested scope; briefly flag an outside issue only when it materially affects the assessment, without expanding the task.

Lead with the result in plain language, and use structure only when it aids clarity or comparison. The final response must stand on its own without tool output.

## References

For an applicable task, load only the reference needed for the current concern:

- `references/verification.md` — only when designing or changing an evidentiary check, establishing a negative control, relying on representation-level evidence such as a source shape, private call sequence, or snapshot, or considering a suppression.
- `references/rule-rationale.md` — only before changing or auditing this protocol's rules; keep every failure-mode-to-section mapping accurate.
