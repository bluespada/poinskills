---
name: clean-room-reimplementation
description: >-
  You must use this skill when the user wants to reverse engineer an app or
  service and reimplement its behavior from scratch without violating
  copyright, or asks to legally rebuild or clean-room a proprietary product.
  It enforces a lawful acquisition and EULA gate before analysis, works from
  black-box observation toward decompilation only as needed, routes license
  obstacles to lawful workarounds, and keeps decompiled code and memory
  dumps away from the independently written implementation.
---

# Clean-Room Reimplementation

## Gate the copy first
- Write `ACQUISITION.md` before any tool runs; the field list lives in `reference/procedure.md`.
- Walk away from cracked, pirated, leaked, or dumped copies; one bad copy poisons every defense built on it.
- Sort the license clause with `reference/eula-workarounds.md` and stop for human sign-off on yellow or unknown.
- Call out DMCA locks like DRM or an auth handshake guarding the binary before touching them.
- Keep the evidence ledger dirty-side only with observations, captures, and claim IDs; the implementer never opens it.

## Observe outward in
- Start outside the binary: run the app, sniff its traffic, trace what it touches, dump your own instance, and decompile last and only when the license routing permits it.
- Pick tools from `reference/tools.md` and prefer the lightest touch that answers the open question.
- Stop climbing inward once the spec covers observable behavior; every deeper step must earn its place.

## Spec behavior only
- Keep `SPEC.md` to message shapes as offset and type tables plus state changes, error codes, timing, and test vectors.
- Keep decompiled snippets, control-flow notes, internal names, and lifted prose out of the spec.
- Litmus test: `compute CRC-16 over bytes 2-10` belongs in the spec and `loop like the original at 0x4F20` does not.

## Build and test clean
- Hand the implementer a fresh context with an allow-list only: the spec, public docs, and the new codebase.
- Route questions through the gatekeeper so they return as revised spec entries, never as explanations of target internals.
- Run target and rebuild on identical inputs and report misses as bare facts like `test 4.12 failed: expected 0x21, got 0x1F`.
- Pin the edges with property tests and known-answer vectors since two builds sharing a spec gap agree on the wrong answer.
- Run one prose pass per `../unslop/SKILL.md` on filed prose only, keep tables and hashes byte-identical, and show the rewrite for approval.

## Hard rules
- Never crack, patch, strip license checks, repackage, or re-sign the target.
- Never paste decompiled code, dumps, or target identifiers into implementer prompts or the new repo.
- Never touch pirated copies, foreign networks or accounts, mine server-side data, continue after a cease-and-desist, or hand out circumvention tools.
- Full runbook and templates live in `reference/procedure.md`, clause routes in `reference/eula-workarounds.md`, and the tool ladder in `reference/tools.md`.
