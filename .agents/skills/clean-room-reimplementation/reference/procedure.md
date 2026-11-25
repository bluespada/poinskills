# Runbook

Read this before touching the target. It expands the sections in
`SKILL.md` with the exact fields, checks, and records.

## Acquisition record
- Fill `ACQUISITION.md` before any analysis tool runs:
  - `copy_source`: store listing or vendor URL plus receipt or license key
  - `eula_text`: the license as accepted, with the reverse-engineering clause quoted word for word
  - `clause_class`: carve-out, absolute, or RE-plus-functionality ban
  - `jurisdiction`: US, EU, or other, taken from the governing-law clause
  - `access_control`: DRM, encrypted payload, or auth handshake that blocks reading the binary
  - `c_and_d`: any cease-and-desist or revocation on file; present means stop
- Stop on a cracked or pirated copy, unknown provenance, or an active cease-and-desist.
- Slow down on an absolute clause, an RE-plus-functionality ban, or unknown
  jurisdiction: read `eula-workarounds.md` and get human sign-off first.

## Observation order
- Start outside the binary and move inward only until the spec covers what
  the eye can see:
  - Run it: install from the store, exercise every feature, log input and output pairs.
  - Sniff it: your own device, network, and account through mitmproxy or Burp.
  - Trace it: strace, ltrace, Procmon, API Monitor, or Frida for files, sockets, calls.
  - Dump it: your own running instance, kept on the dirty side, never shipped.
  - Open it: Ghidra, Hopper, or jadx, only when the license routing permits.
- Each step must earn its place. If the spec is already complete, stop climbing.

## Spec rules
- The spec holds message shapes as offset, length, and type tables, state
  changes, error codes and constants, timing and edge cases, test vectors
  with expected outputs.
- The spec never holds decompiled snippets, control-flow notes, internal
  names, comments, data structures, or lifted documentation prose.
- Every claim carries an evidence ID pointing at the observation, address,
  or capture. The ledger stays dirty-side only.
- Check each entry before filing: no code, no copied prose, no internal
  identifiers, no detail below what compatibility needs, lawful source cited.
- Say what the product must do, never how the target chose to do it.

## Build packet
- List every file the implementer may read with SHA-256 hashes: spec,
  public docs, build instructions, new codebase.
- Left out: binary, dumps, disassembly, decompiler output, evidence ledger,
  earlier analysis chats.
- Fresh context every time. Never carry analysis chat into the build task.
- Missing behavior goes back as an exact question through the gatekeeper
  and returns as a revised spec entry.
- The implementer records its own architecture and naming choices as proof
  of independent design.

## Testing misses
- Run target and rebuild on identical inputs. The target is the oracle.
- Normalize first: sort orders that do not matter, round floats, fold error
  categories together.
- Report a miss as facts only: test ID, input, expected, actual.
- Work it down: check the spec entry, check invariants, shrink the input,
  lock the fix into a regression test.
- Add property tests and known-answer vectors at the edges.
- A miss that exposes a spec gap goes back through the gatekeeper. The
  implementer never hears the target's side of it.

## Prose pass
- Run the unslop pass as a separate review step after the technical content settles.
- Word choice in behavior descriptions shows independent authorship, so strip
  machine tells without shifting meaning. Offsets, hashes, codes, addresses,
  and verbatim quotes stay untouched.
- Only approved text enters `SPEC.md`, `ACQUISITION.md`, or the record set.

## Records to keep
- `ACQUISITION.md`, spec versions with the review log, evidence ledger,
  packet manifests, commit history with design notes, test reports.
- These may end up in front of a court. Write them from day one so a
  stranger can follow them.
