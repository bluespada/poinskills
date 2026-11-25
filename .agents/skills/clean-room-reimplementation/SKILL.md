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

## Locate the artifacts
- `ACQUISITION.md` proves the copy is lawful: source plus receipt, the EULA
  with its reverse-engineering clause, the governing law, any cease-and-desist.
- `SPEC.md` holds behavior only: message shapes as offset and type tables,
  state changes, error codes, timing, test vectors.
- The evidence ledger stays on the dirty side: observations, captures, and
  the IDs behind every spec claim. The implementer never opens it.

## Prove the copy first
- Write `ACQUISITION.md` before any tool runs; the field list lives in
  `reference/procedure.md`.
- Walk away from cracked, pirated, leaked, or dumped copies. One bad copy
  poisons every defense built on top of it.
- Sort the license clause with `reference/eula-workarounds.md`, then follow
  its routing. Stop and get human sign-off on anything yellow or unknown.
- Call out locks that need a DMCA answer, like DRM or an auth handshake
  guarding the binary.

## Observe, then open only as needed
- Start outside the binary: run the app, sniff its traffic, trace what it
  touches. Dump your own instance. Decompile last, and only when the
  license routing above permits it.
- Pulling apart a copy you own is analysis, not cracking, but the license
  routing above still decides.
- Pick tools from `reference/tools.md`. Prefer the lightest touch that
  answers the question.

## Write the spec
- Say what the product must do, never how the target chose to do it.
- Keep decompiled snippets, control-flow notes, internal names, and lifted
  prose out of the spec.
- Litmus test: `compute CRC-16 over bytes 2-10` belongs in the spec.
  `loop like the original at 0x4F20` does not.

## Build clean
- Hand the implementer a fresh context and a short allow-list: the spec,
  public docs, the new codebase. Nothing else.
- Questions travel through the gatekeeper and come back as revised spec
  entries, never as explanations of the target's guts.
- The implementer writes down its own architecture and naming choices as
  proof the design came from its own head.

## Test the build
- Run target and rebuild on identical inputs; report misses as bare facts:
  `test 4.12 failed: expected 0x21, got 0x1F`.
- Pin the edges with property tests and known-answer vectors. Two builds
  that share a spec gap agree on the wrong answer unless forced apart.

## Prose pass
- After the clean side drafts filed prose, run one pass per
  `../unslop/SKILL.md`: strip machine tells, keep the meaning.
- Touch only prose written in this run. Tables, offsets, hashes, error
  codes, addresses, and quoted license text stay byte-identical.
- Show the rewrite for approval before it lands in any filed record.

## Hard rules
- Crack, patch, strip license checks, repackage, or re-sign the target:
  never.
- Paste decompiled code, dumps, or target identifiers into implementer
  prompts or the new repo: never.
- Touch pirated copies, networks or accounts you do not own, mine
  server-side data, or continue after a cease-and-desist: never.
- Hand out circumvention tools built during the work: never.

## Bundled files
- `reference/procedure.md` holds the full runbook and record templates.
- `reference/eula-workarounds.md` holds clause sorting and lawful routes
  around a closed door.
- `reference/tools.md` holds the platform tool ladder.
