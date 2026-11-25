# Conventions rules

What belongs in `specs/SPECS.md`, and what does not. This file is the reasoning behind the skill; the
document itself is the deliverable.

## What this document is for

`specs/SPECS.md` answers the questions every other artifact assumes an answer to: where does a file go, what
is it called, what fields does it carry, what does a status mean, and what does an abbreviation stand for.
Without it, those answers live only in the skills, and a skill is invisible to anyone reading the repository.

It carries no frontmatter and no status of its own. It is a living reference: current, not versioned by
lifecycle. If it needs an "updated" marker, put the date in the section that changed.

## Directory layout

Record the layout as it actually is, not as it should be. The tree belongs here so a reader can see the
whole shape in one place.

```
specs/
├── SPECS.md                 conventions and glossary (this document)
├── DESIGNS.md               central design document
├── designs/                 per-context design documents
├── prd/                     one PRD per spec
├── tasks/                   task files, one per phase or wave
└── decisions/               one decision record per decision
```

## Numbering and naming

- Spec numbers: `<NNN>-<slug>`, zero-padded three digits, allocated from the highest existing number.
- The directory name, the PRD filename, and any branch share the number and slug.
- Task files: `<TNN>-<group-slug>.yml`, one per phase or wave.
- Decision records: `<DNN>-decisions.md`, one decision per file.
- Design documents: `<context>-designs.md`, named for the context, not for a spec number, because a design
  can outlive or span specs.

## Frontmatter rules

| Artifact | Fields |
|---|---|
| PRD | name, description, status, tasks, authored, createdAt, updatedAt |
| Task file | name, description, content, status, dependsOn, goals, authored, createdAt, updatedAt |
| Decision record | name, description, status, authored, createdAt, updatedAt |
| Design doc | none |
| SPECS.md | none |

- Timestamps are ISO-8601 UTC. `createdAt` is written once; `updatedAt` moves on every write.
- `authored` is appended to, never replaced.

## Status vocabulary

The same four values are used everywhere a status exists, so a reader does not have to relearn them:

- `draft` — written, not settled. Still moving.
- `pending` — settled, awaiting or undergoing work.
- `complete` — done and verified against its own criteria.
- `canceled` — will not be done. Record why.

For a decision record, `complete` means the decision is settled, not that the code exists. For a task,
`complete` means every goal holds.

## Glossary

One line per term, for terms that actually appear in the specs.

| Term | Meaning |
|---|---|
| FR | Functional requirement, in a PRD |
| NFR | Non-functional requirement, in a PRD |
| PRD | Product requirements document — what and why, no implementation |
| ADR | Architecture decision record — the synthesised architectural record |
| DNN | A decision record number under `specs/decisions/` |
| TNN | A task group number under `specs/tasks/` |
| goal | The finish condition of a task; all goals holding means `complete` |
| hotspot | A file only one task may write, such as a route table or registry |

## What does not belong here

- Requirements, designs, or decisions themselves — link to them.
- General programming glossary terms that never appear in the specs.
- Conventions the project has not actually adopted. List those as open questions instead.
- Restated skill instructions. The skill says how to write; this document says what was decided.