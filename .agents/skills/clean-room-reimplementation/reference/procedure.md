# Full Procedure

## Phase 1 — Preflight gate
- Create `ACQUISITION.md` with these fields before any analysis tool runs:
  - `copy_source`: store listing or vendor URL plus receipt or license key
  - `eula_text`: the license as accepted, with the reverse-engineering clause quoted verbatim
  - `clause_class`: carve-out, absolute, or RE-plus-functionality ban
  - `jurisdiction`: US, EU, or other, taken from the license's governing-law clause
  - `access_control`: DRM, encrypted payload, or authentication handshake that blocks reading the binary
  - `c_and_d`: any cease-and-desist or revocation on file; present means stop
- Stop conditions: cracked or pirated copy, unknown provenance, existing cease-and-desist
- Yellow conditions: absolute clause, RE-plus-functionality ban, or unknown jurisdiction; route to `eula-workarounds.md` and pause for human sign-off

## Phase 2 — Observation ladder
- Rung 1 black-box: install from the store, exercise every feature, log input and output pairs into the spec draft
- Rung 2 network: own device, own network, own account through mitmproxy or Burp; capture endpoints, message layouts, status codes, timing
- Rung 3 trace: strace, ltrace, Procmon, API Monitor, or Frida to log files, sockets, and library calls the app makes
- Rung 4 memory: dump the running instance you own; keep it on the dirty side and never ship or share it
- Rung 5 decompile: Ghidra, Hopper, or jadx, permitted only when Phase 1 shows a carve-out clause or EU governing law, or written authorization exists
- Stop as soon as the spec covers observable behavior; later rungs are opt-in, not a checklist to complete

## Phase 3 — Spec extraction
- Spec includes: message layouts as offset, length, type tables; state transitions; error codes and constants; timing and edge cases; test vectors with expected outputs
- Spec excludes: any decompiled snippet, pseudocode tracking the target's control flow, internal names, comments, data structures, and documentation prose
- Evidence ledger: every spec claim carries an evidence ID pointing to the observation, address, or capture; the ledger stays on the dirty side
- Gatekeeper checklist per entry: no code, no copied prose, no internal identifiers, no implementation detail below what compatibility requires, cited lawful source
- Abstraction test: describe what the product must do, never how the target chose to do it

## Phase 4 — Clean implementation
- Packet manifest: list every file the implementer may read with SHA-256 hashes; spec, public docs, build instructions, new codebase
- Excluded from the packet: binary, dumps, disassembly, decompiler output, evidence ledger, prior analysis conversations
- Fresh context: never carry analysis chat into the implementation task
- Question flow: implementer writes an exact missing-behavior question, gatekeeper forwards it, the answer returns as a revised spec entry, implementation resumes with a fresh packet
- Design independence: implementer records its own architecture and naming choices as evidence of independent creation

## Phase 5 — Differential test
- Run target and rebuild on identical inputs; the target is the oracle
- Normalize before comparing: sort equivalent orderings, round floats, canonicalize error categories
- Report mismatches as facts only: test ID, input, expected, actual, never an explanation of the target's internals
- Adjudication ladder: check the spec entry, check invariants, minimize the input, resolve into a permanent regression test
- Add property-based tests and known-answer vectors at the edges, since two implementations sharing a spec gap agree on the wrong answer
- If a mismatch reveals a spec gap, the dirty side revises the spec through the gatekeeper; the implementer never sees the target's explanation

## Records to keep
- `ACQUISITION.md`, spec versions with the review log, evidence ledger, packet manifests, commit history with design notes, test reports
- These exist to be produced in litigation; design them from day one to be readable by a court