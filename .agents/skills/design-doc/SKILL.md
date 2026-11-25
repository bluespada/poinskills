---
name: design-doc
description: >-
  You must use this skill when the user asks for a design doc, design system,
  or visual identity before implementation starts, or when coding agents need
  the product's tokens written down. It writes specs/DESIGNS.md plus one
  specs/designs/{context}-designs.md per component, all in the DESIGN.md
  format: YAML front matter tokens with prose in the canonical section order.
  It validates every file by running the design.md linter. It writes no
  requirements, no tasks, and no architecture.
---

# Design Doc

## Locate the artifact
- The central file is `specs/DESIGNS.md`; a component that needs its own treatment gets `specs/designs/<context>-designs.md`, named for the context it covers.
- Every file is a standalone `DESIGN.md` document, not a chapter of one.
- Read `references/design-md-spec.md` before writing, and copy `assets/DESIGN.md` as the skeleton.

## Write the format
- The file is YAML front matter followed by a markdown body; the front matter opens and closes with a line containing exactly `---`.
- Front matter holds `name` plus any of `version`, `description`, `omitted`, `colors`, `typography`, `rounded`, `spacing`, `components`.
- Body sections use `##` headings and appear in this order: Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Do's and Don'ts.
- Omit a section rather than leaving it empty, and name it under `omitted` with a reason.
- Tokens are the normative values; the prose says why they exist and how to apply them.
- Reference a token as `{colors.primary}` instead of repeating its literal value.
- One optional `#` title is allowed and is not parsed as a section.

## Decide whether it is warranted
- A per-component file earns its place when that component has its own tokens or its own visual identity.
- A component with no visual identity is not a design-system document; do not invent tokens for it.
- For a small change, write it into `specs/DESIGNS.md` rather than creating a new file.

## Verify
- Run `npx @google/design.md lint <file>` on the central file and on every changed component file.
- Fix every error; report every warning you leave, naming the rule that raised it.
- Run `npx @google/design.md export --format dtcg <file>` when a consumer needs `tokens.json`.
- Report the files written, the sections omitted, and any finding you did not act on.

## Hard rules
- No engineering design-doc sections. Context, goals, and alternatives are not part of this format.
- Trade-offs and rejected alternatives belong in `specs/decisions/`, not here.
- Never restate a requirement; link the PRD instead.
- Ask before treating a design as approved.