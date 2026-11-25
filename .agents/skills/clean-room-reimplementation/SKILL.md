---
name: clean-room-reimplementation
description: You must use this skill when the user wants to reverse engineer an app or service and reimplement its behavior from scratch without violating copyright, or asks to legally rebuild or clean-room a proprietary product. It enforces a lawful acquisition and EULA gate before analysis, drives an observation ladder from black-box testing through decompilation, routes license obstacles to lawful workarounds, and keeps decompiled code and memory dumps away from the independently written implementation.
---

# Clean-Room Reimplementation

## Goal
- Ship a new implementation of the target's observable behavior with records proving independent creation; cracking or patching it is never a deliverable

## Phase 1 — Preflight gate
- Fill `ACQUISITION.md` first: copy source plus receipt, EULA and its reverse-engineering clause, jurisdiction, any cease-and-desist
- Stop on cracked, pirated, leaked, or dumped copies; one tainted copy destroys every defense downstream
- Classify the clause as carve-out, absolute, or RE-plus-functionality ban, then read `reference/eula-workarounds.md`
- Flag any access control needing a DMCA basis

## Phase 2 — Observation ladder
- Climb in order, stop when the spec is complete: black-box I/O, MITM, tracing, memory dumps of your own instance, decompilation
- Decompiling a lawfully owned copy is analysis, not cracking, but it stays gated by the Phase 1 check
- Read `reference/tools.md` before picking tools

## Phase 3 — Spec extraction
- Write `SPEC.md` in behavior only: message layouts as offset/type tables, state transitions, error codes, timing, test vectors
- Keep decompiled output, dumps, addresses, and internal identifiers in an evidence ledger the implementer never sees
- Litmus test: `compute CRC-16 over bytes 2-10` belongs in the spec, `loop like the original at 0x4F20` does not

## Phase 4 — Clean implementation
- Give the implementer a fresh context and an allow-listed packet: spec, public docs, new codebase only
- Route questions through the gatekeeper; answers come back as revised spec entries, never explanations of internals
- Record same-machine separation as procedural, not technical

## Phase 5 — Differential test
- Run target and rebuild on identical inputs; report mismatches as facts only: `test 4.12 failed: expected 0x21, got 0x1F`
- Add property-based tests and known-answer vectors; shared spec gaps otherwise pass silently

## Never do
- Crack, patch, strip license checks, repackage, or re-sign the target
- Paste decompiled code, dumps, or target identifiers into implementer prompts or the new repository
- Use pirated copies, touch networks or accounts you do not own, mine server-side data, or continue after a cease-and-desist
- Distribute circumvention tools built during research

## Bundled files
- `reference/procedure.md` — full procedure and record templates; read before Phase 1
- `reference/eula-workarounds.md` — clause classification and lawful workarounds; read when Phase 1 flags a restrictive license
- `reference/tools.md` — platform tool ladder; read before Phase 2