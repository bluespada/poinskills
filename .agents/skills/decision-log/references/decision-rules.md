# Decision record rules

Field rules and the reasoning for `specs/decisions/DNN-decisions.md`. The body of a record is deliberately
unconstrained; the frontmatter is not.

## Purpose

A decision record is the raw trail: what was decided, when, and why — including the parts that never made it
into a formal record. It exists so that months later someone can trace *why* a given ADR exists, or why a
decision that never became an ADR was taken.

It is not an ADR. An ADR is the synthesised architectural record, revised when the user's direction
changes. A decision record is a note.

## Frontmatter

The PRD's fields, minus `tasks`, since a decision is not decomposed into work.

```yaml
---
name: Sessions over JWTs for the web app
description: Why the login flow uses server sessions.
status: complete
authored:
  - bluespada
createdAt: 2026-09-28T06:50:00Z
updatedAt: 2026-09-28T06:50:00Z
---
```

- `name` is the decision in title form, specific enough to distinguish it from a similar one.
- `description` is one line. The reasoning goes in the body, not here.
- `status` uses the shared vocabulary: `draft`, `pending`, `complete`, `canceled`.
- `authored` is appended to, never replaced. `createdAt` is written once, `updatedAt` moves on every write.
- Timestamps are ISO-8601 UTC.

## The body

Raw markdown: `#` headings and bullets. There is no required section list, on purpose — the record should be
as long as the reasoning needs and no longer. A shape that usually works:

```
## Decision

One line: what was decided.

## Why

- The constraints that forced it.
- The requirement or incident that made it necessary.

## Rejected

- Alternative: why it lost.
- Alternative: why it lost.

## Affects

- artifacts this decision touches, and where the record is referenced from

## Not an ADR

- Whether an ADR is warranted, and the ADR number if one exists.
```

- Lead with the decision. A reader scanning the log needs the verdict before the argument.
- Record rejected alternatives even when the reasons are thin. "Nobody liked it" is a reason worth keeping.
- Link what the decision affects, so the trail runs both ways.
- State whether an ADR follows. If one does, name it; if not, say why not.

## Rules

- **Append, never rewrite, except on confirmed user drift.** A reversal is a new record referencing the old one,
  not an edit to history. When a live user request changes direction, pause and name the affected record,
  then wait for explicit user confirmation before updating it; without confirmation, write the new direction
  as a separate draft and stop.
- **Sync the artifacts a record refers to only on confirmed user drift.** A live user request that contradicts the PRD,
  design, or task wins only after the user explicitly confirms the sync; the agent never rewrites PRD, design,
  or task files on its own. Describe the proposed sync and stop until the user approves.
- **One decision per file.** A file holding several decisions cannot be referenced, superseded, or dated
  coherently.
- **Do not copy an ADR in.** Link to it. Two copies of a synthesised record will disagree eventually.
- **No status inflation.** A record is `complete` when the reasoning is written down, not when the decision
  has been implemented.

## Allocating the number

- Scan `specs/decisions/` for the highest existing `DNN` and take the next one.
- Numbers are never reused, including for `canceled` records. A gap is a record that was removed, and
  reusing the number makes old references point at the wrong decision.
- The filename and the record's position in the sequence must agree; if they do not, report it rather than
  quietly renumbering.