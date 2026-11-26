# Sweep report rules

Field rules for the report copied from `assets/sweep-template.md`.

## Purpose

A sweep report is a map not a fix. It tells the operator where each issue lives and whether the cause sits in the structure or in one local spot. It never reshapes code on its own.

## Sections

- Keep sections in this order: Scope, Method, Findings, Dropped, Blockers, Handoff.
- Write no Dropped section when every guess survived, and no Blockers section when nothing waits on the user.
- One finding per `###` heading, each with all seven fields filled.

## Fields

- Location cites one `path:line` so the reader lands on the exact spot.
- Claim states the defect in one line with no hedging words.
- Path names the source of input and the place of harm in the form source leads to sink.
- Proof cites the trace test or check output that shows the path can run, never a bare opinion.
- Level uses structure for architecture causes and local for one spot defects, never both.
- Severity uses critical high medium or low, picked by harm times reach.
- Confidence uses high medium or low with one reason naming the evidence behind it.

## Rules

- No finding ships without a cited path and its proof.
- A guess that lost its proof moves to Dropped with the reason, not into Findings.
- A blocker stops the sweep for that area until the user answers, with no silent workaround.
- Fixes stay out of the report. Name the next step in Handoff and stop.
