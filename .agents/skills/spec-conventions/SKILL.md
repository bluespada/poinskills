---
name: spec-conventions
description: >-
  You must use this skill when the user asks what belongs in a spec directory or
  which number and status value to use. It writes and maintains specs/SPECS.md,
  which holds the directory layout, the numbering and naming rules, the
  frontmatter rules, the status vocabulary and the glossary. It documents
  conventions rather than authoring artifacts, so it never writes a PRD or design
  doc or task file or decision record.
---

# Spec Conventions

## Locate the artifact
- Path is `specs/SPECS.md`, at the specs root, beside `specs/DESIGNS.md`.
- It carries no frontmatter: it is a living reference, not a status-tracked artifact.
- Copy `assets/SPECS.md` for its skeleton, and update it in place when a convention changes.
- Read `references/conventions-rules.md` for what each section is for and what does not belong in it.

## Sections it holds
- Directory layout: what lives where under `specs/`, shown as a tree.
- Numbering and naming: spec numbers, task group prefixes, decision numbers, and context-named design files.
- Frontmatter rules: a table of the fields each artifact carries, and which artifact omits which field.
- Status vocabulary: `draft`, `pending`, `in-review`, `complete`, `canceled`, and what each means per artifact type.
- Glossary: one line per term, limited to terms that actually appear in the specs.

## Keep it true
- Name the artifact or skill that owns each convention, so a reader can find the rule that acts on it.
- Record a mismatch as a finding rather than relaxing the rule to match the artifact that drifted.
- Treat the layout section as a description of the tree as it is, not as it was intended to be.
- Put the date beside a section only when that section changed, instead of dating the whole document.

## Rules
- Record only what is decided. An unsettled convention is listed as open, never guessed at.
- Keep the glossary free of general programming terms; a general glossary belongs elsewhere.
- Cite the source of a convention when it came from a decision record or an ADR.
- On user drift, update the artifact and the convention together in the same work; otherwise report the mismatch instead of quietly editing.
- Never invent a convention that no existing artifact follows without asking first.

## Finish
- Report the sections changed, and any convention the existing specs now contradict.
- Report any artifact whose frontmatter does not match the table, and any spec term the glossary does not define.