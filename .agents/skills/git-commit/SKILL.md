---
name: git-commit
description: >-
  You must use this skill when the user asks to commit, stage, or sign off
  changes in a git repository. It reads the diff and splits the change into
  atomic commits, writes Conventional Commits subjects with traceability
  lines, and always passes -s -m. It commits when the user
  explicitly asks for the commit. It never pushes,
  rebases, or amends. It never reads or sets user.name or user.email: when -s
  fails it tells the user to set their own project identity.
---

# Git Commit

## The loop
- Read `git status --short` and `git diff --stat` first. They size the job and suggest the first group; the full diff waits until you need it for one group.
- Name the subject, then stage and commit that group. Never hold the whole tree in a plan before the first `git add`: a perfect split that lands late is a commit someone else takes.
- If a group's boundaries are unclear, read the diff for those files only. The whole-tree diff is a last resort, not a first step.
- One logical change per commit. Split independent changes; keep changes that touch the same lines together.
- Stage only the paths one commit owns, one commit at a time; never `git add -A` on a tree with unrelated edits.
- Subject is `type(scope): description`, lowercase imperative, no trailing period, under 72 characters.
- Types, body, and traceability lines: read `references/commit-rules.md`.
- Every commit is `git commit -s -m "..."`, one extra `-m` per paragraph. Never `--no-verify`, never a bare editor commit.

## The gates
- Commit only on an explicit instruction in this session. "Looks good", "continue", "we're done" are not instructions.
- Never push, force-push, push tags, or open a change request, even when asked; say it is out of scope.
- Never rebase, amend, or rewrite history, and never commit onto a branch the user did not name.
- Never commit secrets, credentials, or generated artifacts.
- Never read or set the identity: no `git config`, no `.git/config`, no `-c user.name=...`, no `GIT_AUTHOR_*`. Let `-s` fail.
- On a sign-off failure, report the error verbatim, give the user the two `git config` commands to run, then stop. Read `references/signoff-failure.md`.
- Do not verify: no test run, no lint, no build before committing; whether the change works is the user's gate.

## Finish
- Report the subject, files, and hash of every commit made.
- On failure, report the error verbatim and the command the user must run.