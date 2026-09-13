---
name: keel
description: "Use for greenfield design, architecture/RFC reviews, module boundaries, contracts, state ownership, rewrite decisions, architecture drift, guard/exception audits, migration, or retirement. Small private or reversible boundary choices qualify; scale rigor to impact. Skip routine implementation within settled architecture."
---

# Keel

Keel discovers, judges, and governs load-bearing arrangements. It shapes the best-supported direction and keeps declared architecture enforceable, economical, migratable, and deletable as the system evolves.

Use *keel* at module, boundary, and system scale for responsibility between parts, authority or ownership, interfaces or contracts, dependency direction, state or recovery ownership, and seams that isolate future change. Use repository-native terms and treat applicable instructions, records, contracts, and entry paths as evidence rather than decoration.

## State And Ownership

Use the task to determine the kind of architecture work. These labels distinguish scope; they are not a required sequence:

- **Decision** — establish, change, or compare a load-bearing arrangement. This includes greenfield work and an authorized improvement to an existing target.
- **Judgment** — assess a supplied design or existing system against its requirements. Keep the target fixed; report infeasibility with evidence and the needed decision. Selecting or implementing a replacement requires authorization.
- **Governance** — assess architecture health and applicable restoration, retention, migration, or retirement. Ground it in a load-bearing obligation, recurring bypass, or architecture drift; ordinary maintenance alone does not qualify. A new arrangement requires design authorization.
- **Exit** — a feasible architecture is settled and only implementation, diagnosis, tuning, or verification remains. Reconsider applicability only if evidence opens a material architecture question.

Private, local, reversible, and single-consumer choices can still require Decision or Judgment; scale evidence and ceremony to impact, reversibility, and uncertainty.

Preserve focused workflows' evidence, criteria, and deliverables. Keel owns the architecture assessment; execution workflows own authorized edits, work preservation, and verification mechanics. A design or review request does not itself authorize implementation.

Follow host precedence; explicit user instructions override skill guidance within those boundaries. Automatic loading grants neither applicability nor action authority. Read skills being edited as task data. On Exit, continue under user and host instructions without Keel-specific routes or framing; no replacement skill is required.

## Solve Constructively

Compare viable directions for design, assess the supplied target for review, and compare applicable interventions for governance. Use the following concerns as needed, not as a mandatory itinerary:

1. **Frame and inspect** — identify the question, desired outcome, authority, hard constraints, and criteria; expose only what helps assess the result. **Greenfield evidence** consists of user goals, explicit external constraints, provenance-bearing focused or domain findings, and operating context. Treat architecture shapes as candidates, label assumptions, and treat absent repository precedent as unavailable rather than inventing inherited architecture. Search only for evidence likely to change the framing, candidate set, or result.
2. **Form, test, or compare** — for Decision, derive the smallest set of materially distinct viable directions needed to expose the real tradeoff. For Judgment, test the supplied target against the same declared criteria without generating replacement directions. For Governance, compare only applicable interventions. Include a simpler or no-change result when credible; do not invent alternatives when constraints leave one path. Use a bounded model, characterization, conformance check, or reversible experiment when it is the cheapest decision-changing evidence.
3. **Integrate and return** — preserve focused-workflow findings, assess evidence and any real candidates on the same criteria, and return the best-supported direction, verdict, or governance action with its material tradeoffs and confidence. Surface a better option the user did not name when evidence supports it without silently changing the goal.
4. **Deepen only the supported result** — resolve numbered concerns only when their answers can still change the result, adoption, recovery, or retirement plan.

Stop when more search, options, or detail are unlikely to change the result or close a material risk. If new evidence reopens a viable direction, compare it rather than defending the incumbent.

Resolve routine details from context. Ask only about unresolved choices that materially change the result, after completing independent analysis. Existing authorization remains valid. Return the requested design or judgment, not a promise to produce it.

Apply user corrections to the current result without restarting settled work. Keep state labels internal unless they help the reader; lead with the recommendation or verdict and its supporting tradeoff.

Decision, Judgment, and Governance finish in one of two states; Exit hands off without this framing:

- **Closed** — evidence supports the result for the requested scope, applicable authority and accountability are resolved, and no unresolved material issue requires a different decision. State any bounded assumptions or residual risk without demanding certainty about hypothetical cases.
- **Open** — give the strongest bounded result, recommendation, or experiment available, the decision-changing unknown, and its owner or ownership gap plus the next evidence or decision trigger. Alternatives are included only when real.

For a low-blast-radius internal choice, a concise comparison and recommendation may be complete. Do not invent compatibility, migration, recovery, guards, governance, or artifacts that cannot change the choice.

For Governance, a constructive result may be subtraction, restored enforcement, a cheaper governed path, staged migration, retirement, or justified no action—not a new layer by default.

## 1. Keep The Spine Small

Map only the load-bearing points that apply, using repository-native terms. Entry surfaces, mutation admission, accepted state, externally visible effects, completion, and recovery are examples, not a required inventory. When a repository-declared or risk-plausible point is omitted, state why it is absent or inapplicable rather than inventing a stage. Changing or adding an applicable point is a boundary decision.

A load-bearing decision chain is not one controller, writer, process, transport, or deployment topology. Multiple execution mechanisms may coexist when they preserve every applicable declared boundary contract. A new or changed load-bearing point is a redesign: name the outcome, force, or blocker it addresses; its reconciliation rule when relevant; and the path it changes or retires.

Cross-cutting mechanisms may have dedicated owners without becoming parallel authority roots or bypasses. Add a top-level concept only when its jurisdiction is explicit, no existing owner can carry it without distortion, and it removes more ambiguity than it adds.

## 2. Grade Every Surface

Grade each concrete surface by the compatibility promise it carries, using repository categories when available. When categories are absent, use a proportionate fallback rather than grading a whole domain or mechanism: its private implementation and cross-boundary contract may differ.

Every export, field, flag, option, and consumer-relied observable is a potential promise. Choose the narrowest promise that satisfies the requirement. Public, persisted, and cross-boundary surfaces need an explicit compatibility or cutover strategy; never break one silently.

A clean break may converge directly on the target only when target and cutover decision authority, consumer and data scope, old-entry retirement, and recovery are explicit. Otherwise version or migrate.

## 3. Declare Authority, Writers, And Projections

For each material fact and jurisdiction, use the simplest supported model. Declare only dimensions that exist and keep them independent:

- **Fact authority** — source or rule determining accepted truth.
- **Decision authority** — actor allowed to approve or change a load-bearing choice.
- **Accountable owner** — responsibility for semantics, policy, lifecycle, and escalation; section 4 covers joint accountability.
- **Writers and admission** — who may propose a mutation and through which route. Writing grants neither ownership nor fact authority.
- **Data partition** — jurisdiction, boundaries, and transfer rules.
- **Replica** — role, provenance, freshness, and read semantics.
- **Commit** — acceptance, ordering or version, visibility, and quorum.
- **Conflict** — prevention or detection plus the convergence rule.
- **Recovery** — trigger, decision authority, owner, action, terminal invariant, and evidence required by section 5.

These dimensions coexist; partitioning, replication, quorum, and multi-writer admission do not replace an authority model.

An artifact may project one fact while authoritatively recording another; declare each relation separately. Change a projection through its source and regeneration path. Resolve overlapping fact authority instead of calling writers interchangeable.

## 4. Own Boundaries And Target Scope

Give each material fact, contract, boundary decision, and lifecycle an accountability model. Owner differs from writer, maintainer, operator, and consumer; one owner is common, not universal. Joint or federated accountability declares jurisdiction, decision rights, tie-break or escalation, and lifecycle.

State what each load-bearing owner owns. Where adjacent duties could be confused, also state what it **does not own**.

Follow declared dependency direction and cross boundaries through their public surface or assembly seam. Move semantics into a shared domain only when they are neutral and accountability belongs there; two consumers needing the same capability is insufficient.

**Target scope** — Separate the requested local outcome, any proposed reusable seam or family, and the first implementation tranche. Resolve scope from the request or an authoritative scope source; sample count, code shape, the word *pilot*, and later outcomes are feasibility evidence, not scope authority. When broader family scope is authorized, test the seam against representative, materially distinct members without migrating them. When unresolved scope can change the decision, keep broader reuse unclaimed and return the cheapest clarification or reversible experiment.

Prefer bounded, declared, tool-enumerable entry surfaces so retirement remains possible.

## 5. Design The Negative Path And The Time Axis

Define behavior or an explicit unknown for material negative outcomes. Examine only cases plausible for the design, including failure, partial or stale work, cancellation, timeout, duplication, concurrency, uncertain commit, retry, restart, and replay. Do not invent a state machine for a reversible private choice.

Close each applicable recovery with:

- detection or trigger;
- decision authority and recovery owner;
- rollback, forward repair, or reconciliation action;
- terminal invariant and completion evidence; and
- escalation when convergence fails.

Classify effects as reversible, compensable, or irreversible and scale controls accordingly. Establish closure rather than merely naming a recovery route.

## 6. Guard Boundaries With Falsifiable Checks

Keep a traceable reason for each material architecture rule. Add a falsifiable guard or explicit review only when violation creates meaningful risk and the check can change action. A guard needs evidence that it detects a known or safely planted violation; an execution workflow owns how that evidence is produced.

Default exception baselines to shrink-only. Growth is a boundary decision that records decision authority, reason, narrow scope, owner, review trigger, and removal condition. Moving code outside a guard's scope is also a boundary change.

Change or retire a Keel rule only when a simpler obligation preserves its invariant or evidence shows that its failure mechanism is no longer decision-relevant. Observed silence alone proves neither.

## 7. Keep The Governed Path Cheapest

Reduce avoidable friction without weakening controlling product, safety, security, privacy, or compliance policy. Recurring bypass signals route cost, not misconduct. The owning workflow may contain active risk immediately; trace containment scope, decision authority, cost, and exit while repairing the durable path.

## 8. Metabolize Or Rot

Rot is entropy: it cannot be prevented, only metabolized faster than it accumulates. Make drift, migration, and deletion routine. A new noun, layer, or abstraction must remove more ambiguity than it adds. In an existing system, name what it retires; otherwise record net growth, accountability, reason, and review trigger. In greenfield work, compare it with a simpler omitted alternative instead of inventing a retirement ledger.

A retirement closes the active entry surface, enumerates and migrates or retires dependents, and preserves required behavioral evidence outside the implementation. Historical code informs behavior and risk; it does not define the target topology.

## References

Load only references needed for the current architecture question; Exit loads none:

- `references/rule-rationale.md` — when changing, auditing, replacing, or retiring a Keel rule.
- `references/task-routes-and-lenses.md` — when a substantial greenfield design, architecture review, boundary change, or structural refactor benefits from a formal route, or a rewrite needs slice-versus-whole-target judgment.
- `references/surface-cutover.md` — when repository grades are absent, a surface may be a de facto contract, or cutover evidence is needed.
- `references/recovery-guards.md` — when selecting recovery controls, designing or retiring a guard, or changing an exception baseline.
- `references/rot-audit.md` — for Governance of architecture decay, drift, recurring bypass, exception growth, or long-lived health.
- `references/architecture-records.md` — when records carry or route load-bearing architecture facts.
