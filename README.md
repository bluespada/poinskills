# poinskills

[![skills.sh](https://skills.sh/b/bluespada/poinskills)](https://skills.sh/bluespada/poinskills)

Personal collection of agent skills. Each skill lives under `.agents/skills/<name>/SKILL.md` so the `skills` CLI discovers it automatically.

## Skills

- `agents-creator` - create, rewrite, or audit an `AGENTS.md` with the house structure every project shares.
- `clean-room-reimplementation` - reimplement a product's observable behavior from scratch with lawful acquisition and clean-room records.
- `codereview` - review code and pull requests with small diffs, fast first response, and evidence-grounded checks.
- `codesweep` - sweep a codebase for bugs across files with no diff, map each issue as structure or local.
- `decision-log` - record why a decision was made in `specs/decisions/`.
- `design-doc` - write design docs and tokens in the `DESIGN.md` format.
- `frontend-taste` - recommend 2-3 named visual directions before building any UI.
- `git-commit` - split diffs into atomic Conventional Commits with sign-off, never push.
- `how-to-basic` - ground operators in a new system with assumptions, base rules, patterns, and provenance.
- `research` - run disciplined open-source research with corroboration and inline citations.
- `sdd-plan` - turn a PRD into a wired task graph under `specs/tasks/`.
- `sdd-prd` - write an atomic product requirements document with unknowns marked.
- `sdd-tasks` - maintain task files and keep the dependency graph valid.
- `sdd-team` - orchestrate multiple agents or people as a team from shared specs with re-anchoring and gated review.
- `skills-creator` - author or audit an Agent Skill against the house rules.
- `spec-conventions` - document what belongs in `specs/` and which numbers and statuses to use.
- `teach-me` - teach a concept in small honest steps with an optional quiz.
- `unit-test-discipline` - write unit tests with a red-to-green gate and fixed coverage obligations.
- `unslop` - remove AI writing tells and give prose a human voice.

## Install

Requires Node.js 22.20 or later.

```bash
# list what this repo ships
npx skills add bluespada/poinskills -l

# install one skill globally
npx skills add bluespada/poinskills --skill agents-creator -g -y

# install everything globally
npx skills add bluespada/poinskills --all -g -y
```

Project-local installs drop `-g`; they land in the current project's agent directories instead.

## Layout

```
.agents/skills/<name>/SKILL.md
.agents/skills/<name>/assets/...
.agents/skills/<name>/references/...
.agents/skills/<name>/scripts/...
```

## License

MIT, see `LICENSE`.
