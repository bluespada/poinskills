---
name: unit-test-discipline
description: >-
  You must use this skill when writing or changing production code that needs
  unit tests held to a fixed standard. It enforces an execution-gated
  procedure: derive coverage obligations before coding, write the tests first,
  drive them from red to green, and refuse to finish until a checklist of
  coverage and assertion-strength criteria passes. It ships the default
  obligations for boundary values, null and empty inputs, error paths and state
  changes, plus rules that reject weak assertions and a reusable gate
  checklist that can be enforced in CI.
---

# Unit Test Discipline

## Trigger
- Use when implementing a new unit, changing behavior, or fixing a bug: tests ship with the change, never as a follow-up task.
- Skip only for generated code, throwaway scripts, and pure configuration where behavior cannot regress.

## Procedure
- Take the test command from the project manifest, task runner, or CI workflow; never invent one.
- Enumerate obligations from the diff before coding: branches, boundaries, error paths, and state transitions the change introduces or touches.
- Write the failing test first, then the minimum code that makes it pass, then refactor while the suite stays green.
- Observe the test fail at least once against missing or deliberately wrong behavior; a test never seen failing may be a false positive.
- Keep one behavior per test, name it `should_x_when_y`, and structure it Arrange-Act-Assert with no conditionals or loops in the body.
- Loop generate, run, inspect, repair until the gate passes; never report done on a suite whose failure you have not observed.

## Coverage
- Default per function: happy path, boundary values at minimum, maximum and zero, null and empty inputs, negative and invalid inputs, every branch including catch and default arms, the exact exception type, and state changes verified before and after.
- Read `references/coverage-obligations.md` when deciding what a function owes; it carries the full matrix and the reasoning per category.

## Gate
- Reject assertions that are tautological, only check non-null, or sit inside a try/catch that swallows the failure.
- Require determinism: no network, no real clock, no unseeded randomness, no shared mutable state between tests.
- Mock only external boundaries and keep real dependencies where feasible; an over-mocked test hides how much protection it actually gives.
- On critical paths, inject faults or mutants into the changed lines only and justify every survivor before merging.
- Walk `assets/gate-checklist.md` item by item and treat any unchecked box as a blocker, not a note.

## Assets
- `assets/gate-checklist.md` — the pass/fail checklist for every change; embed it in CI when the project wants an enforced gate.
- `references/coverage-obligations.md` — the default coverage matrix with examples per category.
