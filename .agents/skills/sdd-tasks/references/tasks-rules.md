# Task rules

Schema, lifecycle, and graph rules for `specs/tasks/*.yml`.

## Schema

A file is a YAML sequence of task mappings, with exactly these keys in this order:

```yaml
- name: Login endpoint
  description: One-line summary.
  content: |
    Satisfies: FR-001

    The work specification.
  status: draft
  dependsOn: []
  goals:
    - Condition that means the task is finished.
  authored:
    - pi
  createdAt: 2026-09-28T06:20:00Z
  updatedAt: 2026-09-28T06:20:00Z
```

- `name` is both the display title and the graph node identifier, so it must be unique across every file.
- `description` is one line. `content` holds the detail. Keeping them separate is what makes a file
  scannable and still executable.
- `content` opens with the requirement ids the task satisfies, since the schema has no requirement field.
- `dependsOn` is a list, empty rather than absent when there are no dependencies.
- `goals` is a plain string list of checkable conditions. No nested objects, no per-goal status. The list
  is the finish flag in full: the task is `complete` only when every goal holds, and a partially met list
  means the task is still `pending` or `in-review`. An empty `goals` list means the task cannot be finished at all.
- `authored` is a list of contributors. Append; never replace, or the history is lost.
- There is no `reviewer` key on the task file: the reviewer lives on the tracker issue, and `in-review` plus LGTM are the process gate, not schema fields.
- `createdAt` is written once, `updatedAt` moves on every write. Both are ISO-8601 UTC with a trailing `Z`.

## Status lifecycle

```
draft -> pending -> in-review -> complete
   \        \          \            /
    \        \          \          /
     +-------------------------------+-----> canceled
```

- `draft` — written but unapproved. Bootstrapped tasks start here. The graph may still change.
- `pending` — approved and not started. Dependencies are being respected.
- `in-review` — PR open with a reviewer assigned. Set by the owner when the PR opens.
- `complete` — every goal holds plus reviewer LGTM plus a clean verifier run. All of them, not most. Not "the code is written".
- `canceled` — will not be done. Requires a reason, and a note on what it leaves unreachable.

Transitions that are never valid: `complete` back to `pending` (reopen as `draft` instead, so the review
happens again), and `canceled` to `complete` (a canceled task that gets done is a new task).

## Graph rules

`dependsOn` entries are task `name` values, or a path to a task file meaning "every task in that file".

- **No cycles.** A cycle means two tasks each need the other's output, which is one task mis-split.
- **No dangling references.** An edge naming a task that does not exist is a broken graph.
- **Resolve globally.** Editing one file can break another; validate the whole `specs/tasks/` set after
  any change to a name or an edge.
- **Name uniqueness is load-bearing.** Because edges resolve by name, a duplicate name silently merges two
  nodes. Treat a collision as a graph corruption, not a naming preference.
- **Renaming is a graph change.** Every inbound edge breaks. Report the rename with the list of edges it
  affects and rewire them in the same edit.
- **Shallow beats deep.** A wide wave of independent tasks is safer than a long chain, because a failure
  in the middle of a chain invalidates everything behind it.
- **Hotspots have one writer.** Routing tables, registries, config, schemas, and shared indexes get a
  single owning task; every other task depends on it rather than editing alongside it.
- **Parallel-safe is a claim about files, not about intent.** Two tasks are parallel-safe only when their
  owned files and interfaces do not overlap, however unrelated their descriptions read.
- Isolation for parallel work is a worktree per task. Worktrees do not isolate local databases,
  containers, or caches, so that shared state still needs explicit handling.

## Sizing

- Keep the roughly eight-hour ceiling for a task's scope. Estimate is no longer a field, so the ceiling
  applies to the work described in `content` rather than to a recorded number.
- A task that cannot be verified on its own is a candidate for splitting, not for a longer `content`.
- Decomposition also protects accuracy: agents are reliable on single-issue work and degrade sharply on
  multi-file changes, so a task spanning unrelated modules is a defect.

## Verifying

`scripts/verify_specs.py` reads the whole tree and reports finished against unfinished. Run it rather
than recollecting status by hand.

- `uv run scripts/verify_specs.py specs/` for the report; `--json` for machine-readable output.
- Exit codes: `0` everything finished and the graph clean, `1` unfinished work remains, `2` schema or graph errors.
- A task is finished when its `status` is `complete`. A PRD is finished when its `status` is `complete`
  and every task in its `tasks` list is complete.
- It also reports what status cannot express: duplicate task names, dangling `dependsOn` references,
  cycles, a `complete` task depending on an unfinished one, empty `goals`, a missing `Satisfies:` line,
  malformed timestamps, a PRD whose `tasks` list names a missing file, and task files no PRD lists.
- It does not evaluate whether a goal is actually met — goals are prose, so only a human or a separate
  check can settle them. A task can be `complete` and wrong.
- Without `uv`, run it with any Python 3.11+ that has PyYAML: `python3 scripts/verify_specs.py specs/`.
- Adding `chmod +x` lets the shebang run it directly as `./scripts/verify_specs.py specs/`.

## Editing discipline

- Add tasks when a requirement is uncovered, or when an existing task fails the verifiability test.
- Remove tasks only on explicit confirmation; deleting a task silently orphans whatever depended on it.
- Never edit `goals` unasked to make a check pass. A goal that cannot be met is a finding, not a wording
  problem — but once the user redirects, update the goal in the same work.
- Never edit `content` to narrow scope without saying so; that is how a task stops matching its
  requirement.
- Update the PRD's `tasks` list when files are added or removed, and move its `updatedAt` with it.