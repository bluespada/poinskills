---
name: sdd-tasks
description: >-
  You must use this skill when task files exist under specs/tasks/ and need
  editing or status changes, or when the dependency graph must be validated. It
  owns the YAML task files after bootstrap: adding and removing tasks, fixing
  dependsOn so the graph resolves without cycles or dangling references, moving
  status between draft pending complete and canceled, and keeping the PRD tasks
  list in sync. It does not write the PRD or implementation code.
---

# SDD Tasks

## Locate the artifact
- Own `specs/tasks/*.yml` plus the PRD's `tasks` list, and change nothing else.
- Read the PRD that points at a task file before editing it, since each goal traces back to a requirement there.
- Ask before touching `specs/prd/`, and ask before committing.

## Read and write the format
- Read `references/tasks-rules.md` for the schema, the status lifecycle, and the DAG rules.
- Copy `assets/task-file.yml` when creating a file; it is a YAML sequence with one mapping per task.
- Keep the key order used in that template, and keep every key present even when a list is empty.
- Preserve `content` and `goals` unless the user asks for a change or a live request drifts from them; they carry the requirements this skill did not author.
- Move `updatedAt` on every write, leave `createdAt` alone, and append to `authored` rather than replacing it.

## Edit the graph
- Split a task when it cannot be verified on its own, and remove one only when the user confirms.
- Rewire `dependsOn` from real ordering constraints, then resolve the whole graph rather than checking the file you edited.
- Reject cycles and dangling references, and name the exact tasks involved when you find one.
- Keep every task name unique across all files, since `dependsOn` resolves against names.
- Ask which tasks the user intends to run in parallel, and name the files or interfaces each one owns before calling anything parallel-safe.

## Status
- `draft` means written but unapproved, `pending` means approved and not started, `complete` means its goals hold, `canceled` means it will not be done.
- Never mark a task `complete` without checking each goal; report the goal that failed instead.
- Ask before canceling a task, and say what the cancellation leaves unreachable downstream.

## Finish
- Run `uv run scripts/verify_specs.py specs/` rather than recollecting status by hand, and report its finished and unfinished lists verbatim.
- Report each file changed, the tasks added or removed, the status transitions, and the resolved dependency order.
- Report any goal that could not be checked, and any task whose requirement traceability is broken.
- Stop at the task files: implementation and commits are the user's call.