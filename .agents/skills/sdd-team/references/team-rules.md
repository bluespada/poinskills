# Team rules

Detail behind `SKILL.md` for branch, board, re-anchor, and conflict handling. Read this before the first claim.

## Branch and worktree

- Cut one branch per claimed task from current `main`. The form is `t/<issue-id>-<task-slug>`.
- Each task gets its own worktree, created with `git worktree add ../<repo>-<slug> -b t/<id>-<slug>`.
- Local databases, containers, and caches are shared even across worktrees, so name that shared state inside the task.
- Review happens on the task branch. `main` moves only through merged PRs.
- After the merge, remove the worktree with `git worktree remove ../<repo>-<slug>`.

## Board mapping

- One PRD becomes one Epic in GitLab, or one parent issue plus milestone in GitHub.
- Every task `name` keeps its identical title when it becomes a child issue.
- Goals turn into acceptance checkboxes in the issue body, one checkbox per entry.
- Ordering edges travel as blocked-by links. Prose like blocked by migration never counts as a link.
- Assignee comes from `authored`, and the reviewer field carries the reviewer. Backlog holds `draft` work.
- Ready means `pending`, the review column means `in-review`, and done means `complete`.

## Re-anchor protocol

- When claiming, read the PRD section and the task YAML and the newest decision entries. Then state the goal in one sentence.
- At PR time, re-read the same three sources. List what changed and what is unfinished and what went stale.
- Drift means pausing first. Name the old decision and the affected artifacts, then wait for explicit user confirmation.
- Sources sometimes disagree. Stop and sync the same day, with task YAML beating issue and issue beating chat.
- Hotspot files move under other owners, so refresh those reads on every re-anchor.

## Ownership and conflict

- A task has exactly one owner. A second agent may join as reviewer but never as co-writer on the same files.
- Each hotspot file answers to a single owning task. Everyone else depends on it and waits for its merge.
- Parallel-safe describes owned files and interfaces that do not overlap. Similar wording in two descriptions proves nothing.
- Conflicting edits resolve in favor of the hotspot owner, and the other task rebases after that merge lands.
- Scope never narrows silently through `content` or `goals` edits. Report the gap or ask for redirection first.

## Wording templates

- A claim reads as `I own <task name>, files <owned paths>, forbidden <hotspot paths>, sources read <PRD plus task plus decisions>`.
- A handoff reads as `Changed <what>, unfinished <what>, stale <what>, next <task or reviewer>`.
- A drift note reads as `Old decision <DNN>, new direction <one line>, affected <artifacts>, awaiting confirmation`.
- A review reads as `LGTM or request-changes, goals holding <n of m>, verifier <clean or findings>, proof <test plus log>`.
- A merge reads as `Closes #<issue>, Task <name>, Requirements <FR ids>, reviewer <name>`.

## Status transitions

- `draft` means written but unapproved. Only the graph owner can move it to `pending`.
- `pending` means approved and unclaimed. Claiming appends the owner and keeps the state.
- Open the PR and assign a reviewer, and the task becomes `in-review` by owner action.
- `complete` needs reviewer LGTM and a clean verifier run and every goal holding. The reviewer confirms it.
- Canceling needs a reason, plus a note on what turns unreachable downstream.
