# Default Coverage Obligations

What every function owes by default. Derive the list from the signature, the branches, and the change under review; treat this file as the floor, not the ceiling.

## Boundary values
- Numeric parameters: the minimum, maximum, and zero of the accepted range, plus one value just outside each inferred bound. A comparison like `x < 5` owes `4`, `5`, and `6`.
- Why: off-by-one errors cluster at comparisons, and a suite holding only typical values cannot see them.

## Null and empty
- Reference parameters: null.
- Strings and collections: empty, and for collections a single element as well as many elements.
- Why: degenerate inputs are where guards live, and this category is most often skipped because nothing in the signature announces it.

## Negative and invalid
- Signed numbers: at least one negative value.
- Validated inputs: one value the validation should reject, asserted to raise the specific error the contract names.
- Why: error paths are behavior too; a suite that only proves the happy path cannot catch a guard that was removed.

## Control flow
- Every branch: if/else arms, ternaries, switch cases and the default arm, catch blocks, and explicit throws.
- Assert the outcome of the branch, not merely that the function returned.
- Why: the default arm and the catch block are the least exercised constructs and the likeliest place for a swallowed failure to hide.

## Exceptions
- Assert the exact type and, where the contract specifies it, the message or error code.
- Do not assert a broad parent type when a specific one exists; a broad assertion accepts replacements it should reject.
- Why: a test that accepts any exception cannot tell two failure modes apart.

## State and side effects
- Capture state before the action and assert the delta after it: returned value, mutated fields, emitted events, written records.
- Verify cleanup happened: temporary files removed, connections closed, globals restored.
- Why: a function can return the right value and still corrupt shared state.

## Public surface
- Test through the public interface; do not reach into private members to make a test pass.
- Why: tests coupled to internals break on refactors that preserve behavior, which trains people to weaken tests instead of trusting them.

## Fault detection
- For critical paths, inject faults or mutants into changed lines only and require every survivor to be justified.
- Why: a passing suite and a high line count say nothing about whether the tests detect wrong behavior.
