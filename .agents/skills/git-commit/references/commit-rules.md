# Commit rules

Conventional Commits with strict subject, type, and body rules, plus change-linkage rules via traceability lines.

The gate, the never-push rule, the atomic-split procedure, and the do-not-verify rule live in SKILL.md and are not repeated here.

## Subject line

```
type(scope): description
```

- `type` is required and comes from the closed set below. An unknown type is a rejection, not a variant.
- `scope` is optional and names the module, package, or area. Never a file path, never a ticket number.
- `description` is lowercase, imperative, and has no trailing period. "add password reset endpoint", not "Added password reset endpoint.".
- Keep the whole subject within 72 characters so it survives `git log --oneline`.

## Types

- `feat` — a new feature for the user.
- `fix` — a bug fix for the user.
- `docs` — documentation only.
- `style` — formatting, whitespace, missing semicolons. No behaviour change.
- `refactor` — a change that neither fixes a bug nor adds a feature.
- `perf` — a change that improves performance.
- `test` — adding or correcting tests.
- `chore` — maintenance: dependencies, config, build, template syncs.
- `ci` — pipeline and automation changes.
- `revert` — reverting a previous commit.

## Body

- One paragraph per `-m` flag. Git inserts the blank lines for you, so never hand-write `\n\n`.
- The body explains **why**. The diff already says what changed; if the reason is obvious from the diff, omit the body rather than padding it.
- Wrap body paragraphs at roughly 72 characters.

## Traceability lines

Add these as trailing paragraphs when the change closes work tracked under `specs/tasks/`. They are the link between a commit and the spec tree, and they are what makes the commit reviewable against intent.

- `Task:` the task `name` values this commit closes.
- `Requirements:` the `FR-NNN` ids the task satisfies. Read them from the task's `content`, which opens with a `Satisfies:` line.
- `ADR:` the ADR number, when the change implements an architecturally significant decision.

```
git commit -s -m "feat(auth): add password reset endpoint" \
  -m "Task: Reset form" \
  -m "Requirements: FR-002"
```

Omit the lines entirely when no spec tree exists. Do not invent task names or requirement ids to fill them, and do not reference a task the commit does not actually close.

## Breaking changes

- Append `!` after the type or scope: `feat(api)!: drop v1 auth header`.
- Add a `BREAKING CHANGE:` paragraph explaining what breaks and what to do instead.

## Reverts

- Subject: `revert: <the original subject line>`.
- Body: the original commit hash and a one-line reason. Git's own `Revert "<subject>"` form is also acceptable and is what `git revert` produces.

## Anti-patterns

- `update files`, `fix bug`, `wip`, `changes`, `misc` — say nothing, so they are rejected.
- Bundling unrelated work into one commit; split it.
- Past tense, a capital first letter, or a trailing period in the subject.
- A scope that is a filename or a ticket number.
- A body that restates the subject instead of explaining the reason.
- Adding the traceability lines when the change does not close the task; the link is a claim.
- Committing generated files, lockfiles changed as a side effect, or secrets.

## Worked examples

```
feat(auth): add password reset endpoint
fix(ui): resolve button alignment on mobile
docs(readme): update installation instructions
chore(template): merge template changes
test(parser): cover empty input
refactor(client): extract retry policy
revert: feat(auth): add password reset endpoint
feat(api)!: require v2 authentication header
```