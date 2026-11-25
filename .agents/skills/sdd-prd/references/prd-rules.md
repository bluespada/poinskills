# PRD rules

Atomic, traceable requirements: each requirement is an independent artifact with priority / status / verification method. The cloud, cost, and compliance sections are conditional so the skill works on any software project.

## Frontmatter and status

The PRD is a markdown file at `specs/prd/<NNN>-<slug>.md` whose YAML frontmatter is machine-read by the
later steps. Key order is fixed; the DAG resolver and the task bootstrap both depend on it.

```yaml
name: Login flow
description: One-line summary of what this PRD covers.
status: draft
tasks: []
authored:
  - bluespada
createdAt: 2026-09-28T06:20:00Z
updatedAt: 2026-09-28T06:20:00Z
```

- `name` is human-readable and is the referent other artifacts cite; `description` is one line.
- `tasks` stays an empty list until the plan step bootstraps the task files, then holds their paths.
- `authored` is a list of contributors; append, never replace, or the history is lost.
- `createdAt` is written once. `updatedAt` moves on every write, including the plan step's back-fill.
- Both timestamps are ISO-8601 UTC with a trailing `Z`.

Status lifecycle: `draft` -> `pending` -> `complete`, with `canceled` reachable from any state.

- `draft` means the requirements are still moving; the plan step may proceed but should say so.
- `pending` means the requirements are settled and awaiting or undergoing work.
- `complete` means every requirement has been verified per its stated verification method.
- `canceled` means the feature will not be built; record why, since the task files are now orphaned.

## Atomicity

A requirement is an artifact, not a sentence. Each one must be independently referenceable, independently
verifiable, and independently assignable to a test.

- One capability per requirement. If the sentence contains "and", it is usually two requirements.
- Stable ID: `FR-001` for functional, `NFR-001` for non-functional. Never renumber; retire instead.
- Each requirement carries three attributes: priority (High / Medium / Low), status (Draft / Approved /
  Implemented / Verified), and verification method (Test / Inspection / Analysis).
- The verification method is a promise about how it will be proven later. "Test" is only honest if a test
  can be written without knowing the implementation.

Bad — a prose blob:

```
The system should handle user logins securely with proper authentication mechanisms.
```

Good — atomic and traceable:

```
**FR-001**: The system MUST provide identity and access management with multi-factor
authentication for administrative operations.
Priority: High | Status: Approved | Verification: Test
Trace: -> ADR-0042 -> tests/security/test_mfa.py -> DEF-1234
```

## Traceability

The trace chain is the point of the format. Each link must be fillable:

```
PRD requirement (FR-NNN) -> task (`specs/tasks/*.yml`) -> goal -> test case -> defect
```

- A requirement with no task covering it is unplanned work; the plan step reports the gap.
- A requirement reached by no goal is untestable as written.
- A task with no requirement is either scope creep or a missing requirement; say which.
- A test case with no requirement is a test nobody asked for.
- Propagate requirement changes forward through the chain rather than editing the PRD in isolation.

## Requirement numbering

- Functional and non-functional series stay separate so a reader can see the shape of the system.
- Section order is fixed by the template; it encodes the review order.
- Where a requirement implies a measurable target, put the target and the measurement window in the
  requirement itself: "p95 latency under 100ms measured over a 30-day rolling window", not "fast".

## The clarification marker

`[NEEDS CLARIFICATION: <the specific question>]` replaces a guess. It is a signal to the reviewer, not a
failure of the author.

- Name the question concretely: `[NEEDS CLARIFICATION: auth method - email/password, SSO, or OAuth?]`.
- Never resolve the marker yourself by picking the most plausible option.
- The marker count is reported when the PRD is handed off; a PRD full of markers is a legitimate output
  that shows exactly which decisions are outstanding.

## Anti-patterns

- **Monolithic PRDs** are the named anti-pattern: requirements buried in prose without atomic traceability.
- **Retroactive test design** is forbidden: test cases trace to requirements from day one.
- **Vibe-based approval**: every gate has measurable exit criteria, so success criteria must be checkable.
- **Orphaned change sets**: no requirement without a downstream plan and task link.

## Conditional sections

Include only when they carry real content. An empty Cost Constraints section is worse than no section.

- **Cost constraints**: applies when the project spends money at runtime or per-unit.
- **Compliance**: applies under SOC 2, HIPAA, PCI-DSS, GDPR, or an internal security standard. Name the
  framework, the data residency requirement, and the retention period.
- **SLOs**: applies to anything that runs as a service.
- **Out of scope**: pays for itself whenever a reviewer might otherwise assume the work is included.