# Bootstrap rules

How the plan step turns a reviewed PRD into the first version of the task graph. It writes drafts; it does
not attempt a finished task list, because the user is expected to edit the YAML by hand or hand it back to
an agent afterwards.

## File grouping

- One file per phase or wave: `specs/tasks/<TNN>-<group-slug>.yml`, with `<TNN>` zero-padded (`T01`).
- Group slugs are kebab-case and describe the phase, not the feature.
- Task names must be unique across every file under `specs/tasks/`, because `dependsOn` resolves against
  them. Collisions make the graph ambiguous.
- Keep a file small enough to review in one sitting. When a group grows past roughly eight tasks, split it
  along its own dependency seam rather than by habit.

## Task schema

A file is a YAML sequence. Each entry is a mapping with exactly these keys, in this order:

```yaml
- name: Login endpoint
  description: One-line summary.
  content: |
    The work specification, written so another agent can execute it without
    re-reading the PRD.
  status: draft
  dependsOn: []
  goals:
    - Condition that means the task is finished.
  authored:
    - pi
  createdAt: 2026-09-28T06:20:00Z
  updatedAt: 2026-09-28T06:20:00Z
```

- `name` is the graph node identifier as well as the display title.
- `description` is one line; `content` carries the detail. Do not merge them.
- `status` is `draft` for everything bootstrapped. `draft`, `pending`, `complete`, `canceled` is the set.
- `dependsOn` defaults to an empty list; only add an edge that genuinely exists.
- `goals` is a list of conditions, not a restatement of the description.
- `authored` lists the authoring agent and any human who shaped the task.
- Timestamps are ISO-8601 UTC; both are set to the bootstrap time.

## Goals

A goal is the finish flag for its task: the condition whose truth means the task is done. Meeting every goal
in the list is what makes the task finished — a partially met list is not finished, it is in progress.

- `goals` is a plain string list. No nested objects, no per-goal status, no priority. The only signal is
  whether the condition holds.
- Phrase it so a command, a test, or an observable behavior settles it without judgement.
- Derive it from the requirement the task satisfies, and keep the requirement's wording for anything
  measurable, so the target and the measurement window survive into the task.
- Prefer two sharp goals over one covering several conditions with "and" — the conjunction hides which
  half is met.
- A goal nobody can check is a description, not a goal. Move it to `content`.
- A task with an empty `goals` list cannot be finished, only abandoned.

## Dependency graph

`dependsOn` entries are task `name` values, or a path to a task file meaning "every task in that file".
The second form is how whole phases are ordered.

- Add an edge only for a real ordering constraint: shared interface, required artifact, migration order.
- Prefer a shallow graph. A wide wave of independent tasks is safer than a deep chain.
- Reject cycles outright; a cycle means two tasks each need the other's output, which is one task.
- Reject dangling references; a `dependsOn` naming a task that does not exist is a broken graph.
- Give hotspot files — routing tables, registries, config, schemas — an explicit single owner task, and
  make the other tasks depend on it rather than writing alongside it.
- Since `dependsOn` resolves by name, renaming a task silently breaks every edge into it. Report a rename
  as a graph change, and prefer rewriting the graph over patching one reference.

## Task size

- A task is the smallest unit that can be verified on its own.
- Keep the historical ceiling of roughly eight hours of work. A larger task cannot be verified mid-flight
  and hides its own risk.
- Decomposition also protects accuracy: agents are reliable on single-issue work and degrade sharply on
  multi-file changes, so a task spanning unrelated modules is a defect at bootstrap time.
- Name the files or interfaces each task owns, in `content`, so two parallel tasks cannot collide.

## Traceability

The task schema has no requirement field, so the link is carried in `content` and in the PRD's `tasks`
list. Keep it explicit anyway.

- Open `content` with the requirement ids the task satisfies.
- When a requirement has no covering task, say so in the findings rather than inventing a task for it.
- When a task traces to no requirement, mark it suspected scope creep instead of deleting it silently.

## After bootstrapping

- Back-fill the PRD's `tasks` list with the emitted file paths, then move the PRD's `updatedAt`.
- Report the number of files, the task count, the dependency order, and the parallel-safe set.
- Stop. Maintaining the graph is a separate step, and the user reviews it first.