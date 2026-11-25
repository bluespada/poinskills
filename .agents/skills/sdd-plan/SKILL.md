---
name: sdd-plan
description: >-
  You must use this skill when a PRD exists under specs/prd/ and needs
  adversarial review before work is cut, or when the task graph must be
  bootstrapped from it. It rubber-ducks the requirements, names the goals that
  mark each task finished, emits the initial YAML task files under specs/tasks/,
  wires their dependsOn graph, and back-fills the PRD tasks list. It writes no
  implementation code, and does not maintain those task files afterwards.
---

# SDD Plan

## Locate the artifact
- Read `specs/prd/<NNN>-<slug>.md`; with no PRD there is nothing to review, so stop and offer `sdd-prd`.
- This skill produces no plan document and no `specs/plan/` directory. Its outputs are the review findings, the goals, and the bootstrap task files.
- Write task files under `specs/tasks/` only, and update the PRD's `tasks` list to point at them.
- Ask before creating anything outside `specs/`, and ask before committing.

## Rubber-duck the PRD
- Read `references/rubber-duck-rules.md` for the review protocol, then `references/adr-rules.md` when the review reaches a decision that is hard to reverse.
- Attack the requirements before adding anything: contradictions, unstated assumptions, untestable criteria, missing failure and edge cases, missing non-functional requirements, and scope no requirement justifies.
- Report each finding with the requirement id it attacks, and ask the user to resolve it.
- Once the user gives direction, apply it: revise the PRD in the same work rather than reporting again. Never rewrite the PRD unasked to make it pass.

## Bootstrap the tasks
- Read `references/bootstrap-rules.md` for grouping, naming, and DAG rules, then copy `assets/tasks-bootstrap.yml` as the file skeleton.
- Group tasks into files named `specs/tasks/<TNN>-<group-slug>.yml`, one file per phase or wave, each holding a YAML sequence of task mappings.
- Derive `goals` from the requirement a task satisfies, written as the conditions that mean the task is finished and checkable by a command, a test, or an observable behavior.
- Wire `dependsOn` so the whole graph resolves; take dependencies from real ordering constraints, never from convenience.
- Write every bootstrapped task as `status: draft`, so a human reviews the graph before anything runs.
- Back-fill the PRD's `tasks` list with the emitted paths, then move the PRD's `updatedAt`.

## Hard rules
- Bootstrap only. The user edits the YAML by hand afterwards or asks an agent to edit it; that work belongs to `sdd-tasks`.
- Keep the nine keys in template order, use ISO-8601 UTC timestamps, set `createdAt` once and move `updatedAt` on every write.
- Never invent a requirement to justify a task; report the gap instead.
- No code, no branch, no commit without asking.

## Finish
- Report the PRD path, each task file emitted with its task count, the dependency order, and any cycle you could not resolve.
- Report every review finding the user has not yet answered.
- State plainly that the graph is a draft awaiting review.