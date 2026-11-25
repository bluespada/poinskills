---
name: decision-log
description: >-
  You must use this skill when the user wants to record why a decision was made
  or to add an entry to the project decision log. It writes one
  specs/decisions/DNN-decisions.md per decision, carrying PRD frontmatter without
  the tasks field and a body of plain headings and bullets, so the reasoning
  behind a later ADR can still be traced. It records decisions rather than
  synthesising an ADR, and it syncs the referred artifacts in the same work when
  a live user request changes direction.
---

# Decision Log

## Locate the artifact
- One file per decision: `specs/decisions/DNN-decisions.md`, with `DNN` zero-padded from the next free number.
- Scan `specs/decisions/` for the highest existing number rather than assuming `D01`.
- Frontmatter is the PRD's minus `tasks`: `name`, `description`, `status`, `authored`, `createdAt`, `updatedAt`.
- Copy `assets/decision-template.md` as the skeleton, and read `references/decision-rules.md` for the field rules.

## Write the entry
- The body is deliberately raw: `#` headings and bullets, shaped however makes the reasoning readable.
- Lead with the decision in one line, then the reasoning, then what the decision rules out.
- Record the alternatives that were rejected and why; that is what a later reader comes looking for.
- Link the artifacts the decision affects, and state plainly that this record is not an ADR.
- Append. Never rewrite an earlier entry to match a later decision, except when a live user request
  changes direction: then update the affected entry and its artifacts in the same work.

## Status
- `draft` while the reasoning is still being gathered, `pending` once written and awaiting a decision, `complete` once settled, `canceled` if the decision was dropped.
- Never mark an entry `complete` while the reasoning is thin; say what is still missing.

## Difference from an ADR
- This log is the raw trail: what was decided and why, including the parts that never reached a formal record.
- An ADR is the synthesised architectural record and is produced by its own process.
- Never copy an ADR into the log or a log entry into an ADR; reference across them instead.

## Finish
- Report each file written, its number, and any decision it depends on that is still `draft`.
- Ask before editing a file that already exists.