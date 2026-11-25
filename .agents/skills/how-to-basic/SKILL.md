---
name: how-to-basic
description: >-
  You must use this skill when the user invokes how-to-basic or asks for grounding before building with an unfamiliar system or library. It clarifies working assumptions and derives behavior from base rules plus grouped patterns so operators see the whole design at once. It closes with provenance on who shaped the system and why it looks that way for durable understanding. It never replaces hands-on build steps or deep reference dives afterward.
---

# How-To Basic

## Clarify assumptions first
- Before any steps, state in one sharp contrast what the system promises and what it never does.
- Data or messages flow through named parts end to end, and that flow is the sketch you give first.
- Its place in the operator app and its outside dependencies get named explicitly.
- Newcomers hit two failure modes first. Both get listed with the signal each one gives.
- One sentence confirms the operator mental model, then rules take over.

## Derive from base rules
- Two to four base rules admit no exceptions. The whole system obeys them.
- Nothing feels arbitrary because every visible behavior traces to exactly one base rule.
- A single concrete trace shows inputs meeting rules and producing the observed output.
- Steps without a justifying rule get refused. The rule behind each step stays named.
- Ruleless behavior parks as an open question. Justifications never get invented.

## Group into wider patterns
- Parts cluster into named groups by job, transport or identity or discovery or storage among them.
- One pattern repeats across groups, dial then handshake then multiplex or publish then subscribe as examples.
- The groups compose into the whole in a single zoom-out, with no part re-explained.
- Touching anything needs a blast radius prediction, so what changes together stays named.

## Add provenance notes
- The originator gets named, plus the earlier system this one descends from or reacts against.
- Its shape answers the limits of its predecessor. That response is the explanation.
- One jargon term translates through the design choice that coined it.
- Provenance stays limited to what explains current shape. Trivia that changes no decision gets cut.

## Finish ready to build
- The final response follows `references/format.md` with five fixed moves in order and verification checks holding.
- Assumptions plus base rules plus groups plus provenance report in that fixed order every time.
- Every base rule gets exercised at once by one smallest first build handed to the operator.
- Basic scope ends explicitly. Each advanced topic names the deep dive that unlocks it.
