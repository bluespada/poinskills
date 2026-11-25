# ADR rules

The standard Nygard ADR format, delivered as a pull request through the same review workflow as code.

## When a decision earns an ADR

- The choice is hard or expensive to reverse.
- A reasonable engineer would ask "why not the obvious alternative?" later.
- The choice constrains other components, teams, or future work.
- The choice carries an accepted cost — performance, complexity, a vendor dependency.

A decision that fails all four belongs in a task's `content`, not in an ADR. An ADR with no plausible
alternative is a design note, not a decision record.

## Format

```
# ADR-NNN: <title>
**Status**: Proposed | Accepted | Rejected | Superseded
**Date**: YYYY-MM-DD
**Authors**: <name>
**Reviewers**: <names>

## Context
Forces at play - technical, organisational, project constraints. Three to five sentences, specific.

## Decision
Declarative verdict: "We will use X for Y because Z." One sentence. No hedging.

## Options Considered
1. Chosen option - two or three bullets on its tradeoffs
2. Runner-up - two or three bullets
3. Initial favourite, where different from the above

## Consequences
- Positive: ...
- Negative: ...
- Neutral: ...
- Follow-up ADRs required: links, where any

## Supersedes
"Supersedes ADR-001. Reason: ..." where applicable
```

## Lifecycle

```
Proposed -> review -> Accepted | Rejected
                         |
        a later decision -> new ADR -> old one marked Superseded, never deleted
```

## Rules

- **Revisable when the user drifts.** A live user request wins over an accepted ADR. Revise the ADR in
  place with a dated note, or supersede it with a new ADR that links back. Never block the request to
  protect the record.
- **Stored in version control** beside the code, in the project's ADR directory, numbered sequentially.
  Not in a wiki or a shared drive — an ADR outside the repo cannot be surfaced during review.
- **Delivered as a pull request**, the same toolchain as code, with the decision diff visible.
- **Consequences section is mandatory.** An ADR without consequences is useless; the positive and negative
  lists are what stop the decision being re-litigated.
- **No hedging.** "We will decide later" is not a decision — the ADR stays Proposed and is reported as an
  open decision rather than merged.

## Integration with review

- A change touching architecture should reference any ADR it implements or revises.
- When a live user request contradicts an accepted ADR, follow the request and revise or supersede the
  ADR as part of the same work. The drift note is one line: old direction -> new direction and why.
- Cite the ADR in the task `content`, in the PRD's dependencies, and in any change
  description that implements it.
- Ask before opening an ADR file or committing it, since it is a repository artifact like any other.