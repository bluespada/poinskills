---
name: agents-creator
description: >-
  You must use this skill when the user wants to create, rewrite or audit an
  AGENTS.md for a repository. It fixes the house structure every project shares
  — a short paragraph preamble under the H1 then the four sections Command, Code Guideline,
  Workflow Guideline and Security Policy — with ATX headings, paragraph-then-bullets
  and no tables. Commands come from the real manifest and CI workflows, nested
  files extend the root instead of repeating it, and the CLAUDE.md import keeps
  Claude Code from shadowing the file.
---

# Agents Creator

## Shape
- The file is `AGENTS.md` at the repository root, and it keeps one shape in every project, because Codex, Copilot, Cursor and Claude Code all read this same file.
- Under the H1: one short paragraph (1-4 sentences) on what the project is, plus one line on what this file is for.
- Then exactly four H2 sections, always in this order: `## Command`, `## Code Guideline`, `## Workflow Guideline`, `## Security Policy`.
- Copy `assets/AGENTS.md` for the skeleton and keep those four names byte-identical everywhere.
- A concern that fits none of them becomes a bullet in the closest one, not a fifth section.

## Form
- ATX `#` headings only, never a setext underline.
- Short paragraph then bullets: at most one short paragraph directly after each heading for context, core rules always as bullets; no tables, no numbered lists.
- One command per bullet, copy-pasteable, naming the directory it runs in.
- Under 150 lines at the root; when it outgrows that, split it into nested files instead of truncating it.
- `references/house-structure.md` holds what belongs in each section, what to read before writing, and how each tool loads the file.

## Truth
- Take commands from the package manifest, the task runner and the CI workflows; a command that is not in the repository is a bug in the file.
- Take conventions from the linter, formatter and editor configs the project already runs.
- Never invent a rule, a version, a path or a security policy the repository does not evidence.
- An empty section is a finding: say the project has none and leave it at one bullet.
- Draft from what you read, show the draft, and let it be approved before it reaches the repository.

## Fit
- A nested `AGENTS.md` extends the root and never restates it; the nearest file wins a conflict.
- Where a `CLAUDE.md` exists, its first line is a bare `@AGENTS.md` import, never a sentence pointing at the file.
- Cut anything in `.cursor/rules/`, `.claude/rules/` or `.github/instructions/` that a bullet already states.

## Verify
- Confirm it loaded: `/memory` or `/context` under Claude Code, and a read-only `codex "Summarize the current instructions."` run under the session's normal approval policy. Never add flags that disable approvals, and never run write commands to verify loading.
- Re-read the file after writing and check the heading order, the line count, and that no table slipped in.
- Report the sections left empty and the commands you could not run, instead of filling them with generic advice.