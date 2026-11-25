---
name: skills-creator
description: >-
  You must use this skill when the user wants to author or audit an Agent Skill:
  drafting a SKILL.md, repairing a description that fails to trigger, or
  deciding whether a body has outgrown its token budget. It applies the house
  rules — a mandate-first description inside 80-120 tokens and a body inside
  350-600 tokens under one H1 with bullet-only sections — then proves each
  rule by running the bundled token validator instead of estimating by eye.
---

# Skills Creator

## Rules this skill enforces
- `name` is kebab-case, at most 64 characters, and identical to the parent directory name.
- `description` is required, at most 1024 characters, and free of angle brackets, which break clients that render descriptions as markup.
- Non-spec frontmatter keys warn rather than fail, so client extensions such as `disable-model-invocation` pass.

## The description
- Opens with the literal mandate `You must use this skill`, then the conditional, then the goals; a mandate with no `when` clause fails.
- Holds 80-120 tokens. The floor bites: three goals plus a near-miss clause measures 65 tokens on `o200k_base`, so one sentence will not clear it.
- Stays under 8 comma-separated segments, since more reads as a keyword list and invites false triggers.
- Describes user intent, not implementation, and is deliberately pushy, because under-triggering is the failure mode.

## The body
- Opens with one H1 title and then `##` sections: nothing above the H1, nothing deeper than H3.
- Holds 350-600 tokens including fenced code; the whole body loads on activation.
- Bullets only — ordered steps, bare paragraphs, and tables are errors; the reader is an agent.
- Carries what the agent could not infer alone: project conventions, non-obvious gotchas, the exact command.
- Point at bundled files by skill-root-relative path, and say when to read each one.

## Workflow
- Draft to the rules, then validate rather than estimate, and re-run until the exit code is 0.
- Re-run the client's resource discovery after writing; skill lists are cached at startup, so a new skill is invisible until the session reloads.
- Judge trigger quality with ~20 labelled should- and should-not-trigger queries, not by reading the wording.

## Running the validator
- `uv run scripts/validate_skill.py <skill-dir>`, run from this skill's directory; `<skill-dir>` holds the `SKILL.md` under test.
- Exit 0 clean, 1 errors, 2 warnings, 3 usage error; `--strict` folds warnings into errors for CI.
- Widen with `--desc-tokens MIN:MAX` or `--body-tokens MIN:MAX` when a skill needs the room.
- First run pulls `tiktoken` and `pyyaml` into the `uv` cache; no install step.

## What it does not catch
- A clean-parsing description that triggers on the wrong prompts; that needs eval queries, not a validator.
- Internal links, orphaned files, and reference-file token bloat; use `skill-validator check --strict` for those.
- Whether the content earns its place — the novelty question no static check answers.