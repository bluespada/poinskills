---
name: sdd-team
description: >-
  You must use this skill when the user wants multiple agents or people to work as a team from shared specs or asks to split tasks and review them together. It orchestrates the existing SDD skills into one team loop with re-anchoring and gated review plus single ownership and branch isolation so drift stays visible before it spreads. It keeps specs as the source of truth while issues track ownership and status for the team. It never replaces sdd-tasks or codereview or git-commit or decision-log.
---

# SDD Team

## Re-anchor before every act
- Before writing code, re-read the PRD plus the task YAML plus the newest decision entries, then state the goal in one sentence.
- Every act names three anchors, the exact task name, your owner role, and the latest shared state you build on.
- When anchors disagree across PRD, task file, issue, or chat, stop and sync them the same day. YAML wins every dispute.
- Claim time, PR time, and any live request that changes direction each trigger a fresh re-anchor.

## Claim one task alone
- Append your name to `authored` to claim, and leave other owner entries untouched. One task keeps one owner.
- Cut branch `t/<issue-id>-<task-slug>` from current main with one worktree per task, so no two tasks share files.
- The branch, board, and conflict protocol live in `references/team-rules.md`, which you read before the first claim.
- Only `pending` tasks with resolved `dependsOn` and checkable goals may be claimed.
- Parallel work needs named files or interfaces per task first, and nothing counts as parallel-safe until ownership is written down.

## Respect the single writer
- Routing tables, registries, config, schemas, and shared indexes each belong to exactly one owning task.
- Depend on the owner task through `dependsOn` to reach shared files instead of editing alongside the owner.
- A task that cannot be verified alone gets split, while removal waits for explicit user confirmation.
- After graph edits, run `uv run scripts/verify_specs.py specs/` and report the finished and unfinished lists verbatim.

## Gate review before complete
- Reviews follow `codereview/SKILL.md` with one primary reviewer, and diffs stay under 200 lines with attention on logic.
- Every claim needs proof, meaning tests that fail without the patch plus execution logs plus static analysis output.
- No task turns `complete` without reviewer LGTM and a clean verifier run and every goal holding.
- Commits follow `git-commit/SKILL.md` on the task branch, adding a Task line and a Requirements line and a Closes line for the issue.

## Mirror specs to the tracker
- Each PRD becomes one Epic or parent issue, and each task `name` becomes one child issue while each `goals` entry becomes a checklist item.
- Edges travel as blocked-by links, `authored` travels as assignee, and the reviewer travels as reviewer.
- The four states `draft`, `pending`, `in-review`, and `complete` stay aligned on both YAML and board.
- Specs get written first and mirrored to issues second, then implementation reads from issues, and drift syncs back the same day.
