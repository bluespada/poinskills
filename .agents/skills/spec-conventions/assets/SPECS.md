# Specs

Conventions and glossary for the `specs/` tree. Living document — update in place, no status of its own.

## Directory layout

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

- Spec: `{{NNN}}-{{slug}}`, zero-padded, allocated from the highest existing number.
- A spec's PRD is `specs/prd/{{NNN}}-{{slug}}.md`; the number and slug match everywhere, including the branch.
- Task file: `specs/tasks/{{TNN}}-{{group-slug}}.yml`.
- Decision record: `specs/decisions/{{DNN}}-decisions.md`.
- Design document: `specs/designs/{{context}}-designs.md`, named for the context, not a spec number.

## Frontmatter rules

| Artifact | Fields |
|---|---|
| PRD | name, description, status, tasks, authored, createdAt, updatedAt |
| Task file | name, description, content, status, dependsOn, goals, authored, reviewer, createdAt, updatedAt |
| Decision record | name, description, status, authored, createdAt, updatedAt |
| Design doc | none |
| SPECS.md | none |

- Timestamps are ISO-8601 UTC. `createdAt` is written once, `updatedAt` moves on every write.
- `authored` is appended to, never replaced.

## Status vocabulary

- `draft` — written, not settled.
- `pending` — settled, awaiting or undergoing work.
- `in-review` — PR open with a reviewer assigned; owned by the reviewer gate.
- `complete` — done and verified against its own criteria plus reviewer LGTM.
- `canceled` — will not be done; the reason is recorded.

## Open conventions

- {{A convention still undecided, and what would settle it.}}

## Glossary

| Term | Meaning |
|---|---|
| FR | Functional requirement, in a PRD |
| NFR | Non-functional requirement, in a PRD |
| PRD | Product requirements document |
| ADR | Architecture decision record |
| DNN | A decision record number under `specs/decisions/` |
| TNN | A task group number under `specs/tasks/` |
| goal | A task's finish condition; all goals holding means `complete` |
| hotspot | A file only one task may write |