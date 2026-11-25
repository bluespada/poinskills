# Unit Test Gate Checklist

Every box must be checked before the change is reported complete. An unchecked box is a blocker, not a note.

## Runnability
- [ ] Tests compile and run with the project's own test command.
- [ ] No test fails, is skipped, or is quarantined without a written reason.
- [ ] The suite runs from a clean checkout with no manual setup steps.

## Assertion strength
- [ ] Every test asserts a specific expected value, exception type, or state change.
- [ ] No assertion is tautological, only a non-null check, or missing because it sits in a try/catch.
- [ ] Object returns are checked field by field, not just for existence.
- [ ] Assertions target behavior through the public interface, not private implementation details.

## Coverage obligations
- [ ] Happy path with a typical valid input.
- [ ] Boundary values: minimum, maximum, and zero where the type allows.
- [ ] Null and empty inputs: null references, empty strings, empty collections.
- [ ] Negative and invalid inputs produce the documented error.
- [ ] Every branch is exercised, including catch blocks and default/else arms.
- [ ] The exact exception type is asserted, not a broad parent type.
- [ ] State and side effects are verified before and after the action.

## Isolation and determinism
- [ ] No network calls, real clock reads, or unseeded randomness.
- [ ] Each test sets up its own data and shares no mutable state with another test.
- [ ] External boundaries are mocked or faked; real dependencies kept where feasible.
- [ ] Tests clean up after themselves and leave no residue for the next run.

## Quality
- [ ] One behavior per test, named in the form `should_x_when_y`.
- [ ] Arrange-Act-Assert structure with no conditionals or loops in the body.
- [ ] Setup shared by several tests lives in a fixture or helper, not copy-pasted.
- [ ] A failure message points at the exact expectation that broke.

## Fault detection (critical paths only)
- [ ] Faults or mutants were injected into changed lines only.
- [ ] Every surviving mutant is justified in a comment or issue.
