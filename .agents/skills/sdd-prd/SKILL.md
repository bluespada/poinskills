---
name: sdd-prd
description: >-
  You must use this skill when the user asks for a PRD or product requirements
  document before implementation starts. It allocates the next specs/prd/ number
  and writes frontmatter carrying name description status and authored fields
  plus an empty tasks list. It keeps requirements atomic and marks every unknown
  as [NEEDS CLARIFICATION]. It does not create task files, and does not apply to
  bug fixes or one-line changes.
---

# SDD PRD

## Locate the artifact
- Path is `specs/prd/<NNN>-<slug>.md`, with `<NNN>` zero-padded from the next free number in `specs/prd/`.
- The same identifier names the spec everywhere: the PRD filename, the task group prefixes, and any branch.
- Ask before creating a branch, and ask before writing outside `specs/`.

## Frontmatter
- Emit exactly these keys in this order: `name`, `description`, `status`, `tasks`, `authored`, `createdAt`, `updatedAt`.
- `status` starts `draft`; the set is `draft`, `pending`, `complete`, `canceled`.
- `tasks` ships as an empty list — the plan step fills it with the task file paths it bootstraps.
- `authored` lists who worked on the artifact; append to it rather than replacing the list.
- `createdAt` is set once and never edited; `updatedAt` moves on every write. Both are ISO-8601 UTC.
- Read `references/prd-rules.md` for field semantics and the status lifecycle.

## Gather before writing
- Copy `assets/prd-template.md` as the skeleton and keep its section order.
- Read `references/prd-checklist.md` before declaring the PRD done, not while drafting.
- Ask the user when a requirement is unclear; eliciting requirements is this skill's job, inventing them is a defect.

## Write the body
- One `FR-NNN` per requirement, each independently referenceable and testable.
- Every requirement carries priority, status, and verification method — test, inspection, or analysis.
- Number non-functional requirements in their own series, each with a measurement window.
- Include cost, compliance, assumptions, out-of-scope, and dependencies only where they genuinely apply.
- Name every unknown as `[NEEDS CLARIFICATION: the specific question]` rather than picking a plausible reading.

## Hard rules
- No implementation detail: write "managed relational database", never the product name.
- No prose blobs — a requirement nobody can cite by ID is malformed.
- Success criteria must be objectively verifiable without knowing the implementation.
- Never write task files and never edit anything under `specs/tasks/`; that surface belongs to the later steps.

## Finish
- Walk `references/prd-checklist.md` and report every box left unchecked, with the reason.
- Report the path, the requirement count, and the open `[NEEDS CLARIFICATION]` count.
- Stop here: adversarial review and task bootstrapping belong to `sdd-plan`.