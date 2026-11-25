# House Structure

## Why one shape
- Codex, Copilot, Cursor and Claude Code all read the same `AGENTS.md`, so a per-project layout costs that file its audience for no gain.
- The four sections are a contract: an agent can expect `## Command` to hold commands in any repository it opens.
- The file is guidance, not enforcement. Agents follow it because it is short and specific, and they stop reading it the moment it bloats.

## The four sections
- `## Command` — install, build, run, test, lint, typecheck. One copy-pasteable bullet each, with the working directory and any prerequisite: a service to start, an env file to copy.
- `## Code Guideline` — only rules the repository already enforces or demonstrably follows. Point at the enforcing command rather than restating the rule; "Prettier runs in `pnpm lint`" beats a paragraph on print width.
- After each H2, at most one short paragraph of context is allowed before the bullets; the rules themselves stay as bullets.
- `## Workflow Guideline` — how work is done: branch, commit, review, merge gate, and the actions that need a human first.
- `## Security Policy` — the credential rules, the files never to read, and the boundaries that need approval.
- Under the H1 — one short paragraph (1-4 sentences) on what the project is, plus one line on what the file is for. No history, no marketing, no restating the README.

## What to read before writing
- `package.json` scripts, `pyproject.toml`, `Makefile`, `justfile`, `Cargo.toml`, `go.mod`, `composer.json`, `Gemfile` — the real command surface.
- `.github/workflows/` and any other CI config — the merge gate is whatever CI runs.
- `.editorconfig`, `eslint`, `prettier`, `biome`, `ruff`, `rustfmt`, `.golangci.yml` — the style the repo enforces.
- `README.md` and `CONTRIBUTING.md` — for the human workflow, never copied wholesale.
- `CLAUDE.md`, `.cursor/rules/`, `.claude/rules/`, `.github/instructions/` — existing guidance, to merge rather than contradict.

## Budget and shape
- Under 150 lines at the root; past that, adherence falls off before any tool truncates.
- Codex stops adding instruction files at 32 KiB in total, `project_doc_max_bytes` in `config.toml`, and truncates without warning.
- Claude Code targets under 200 lines per file for the same reason: it loads at session start and competes with the conversation.
- Split by directory, not by topic. A nested `AGENTS.md` earns its place only when that subtree genuinely diverges.
- Do not add frontmatter. The spec makes it optional and it buys nothing when the path is already descriptive.

## How the tools load it
- Codex — global `~/.codex/AGENTS.override.md` then `AGENTS.md`; per directory `AGENTS.override.md`, `AGENTS.md`, then configured fallbacks. One file per directory, concatenated root to current directory, nearest last.
- Copilot — the nearest `AGENTS.md` in the tree wins; precedence is personal over repository over organization.
- Cursor — reads `AGENTS.md` at the root and nested, always applies `CLAUDE.md`, and keeps glob-scoped rules in `.cursor/rules/*.mdc`.
- Claude Code — reads `AGENTS.md` natively from v2.1.277, but only when no `CLAUDE.md`, `.claude/CLAUDE.md` or `CLAUDE.local.md` sits at or above the working directory. Set Project instructions to `claude-md-and-agents-md` in `/config` to read both.
- Aider needs `read: AGENTS.md` in `.aider.conf.yml`. Gemini CLI needs `{"context": {"fileName": "AGENTS.md"}}`.
- A `CLAUDE.md` whose first line is `@AGENTS.md` is the portable bridge. A sentence such as "see AGENTS.md" is not an import and loads nothing.

## Nested files
- Jurisdiction is the directory tree: a file governs its own folder and everything below it, never a sibling.
- Guidance accumulates, so a child extends its ancestors and never repeats a rule the root already states.
- The nearest file wins a conflict, and an instruction typed in chat beats every file.

## Anti-patterns
- A command nobody can run because it was guessed. Every bullet is copy-pasteable or it is a defect.
- A section padded with generic advice, such as "write clean code", to look complete.
- A paragraph that restates what the bullets already say, instead of adding context the bullets need.
- A table. The format is a flat list because a list survives every tool that loads it.
- Duplicating what a linter or CI already enforces, which drifts the moment that config changes.
- A file that outlives its commands. Update it in the same commit that changed the command.
- A fifth section, because the four are the contract.

## Verify
- Claude Code — `/memory` or `/context`, and look for the path under Memory files.
- Codex — `codex --ask-for-approval never "Summarize the current instructions."` and read back the merged result.
- Both — confirm the merged text is the sum you expect and nothing was cut at a cap.
- By hand — heading order, no table, every command still exists, every referenced path still resolves.

## Maintain
- Re-audit whenever a command, a linter or a directory layout changes. The audit reports drift, it does not rewrite the project.
- Record a convention once, in the file that owns it, and point at it from everywhere else.