# Rubber-duck rules

The review protocol for this step. The name is deliberate: the goal is to make the author say the
requirement out loud until the hole in it becomes visible, not to agree with it.

Evidence for why this step carries the weight: in Anthropic's analysis of roughly 400,000 coding-agent
sessions, people make about 70% of the planning decisions and the agent about 80% of the execution
decisions. Planning is the human half of the division of labour, and this step is where it happens. The
same study found that sessions rated expert reach verified success more than twice as often as sessions
rated novice, and that novice sessions are abandoned at three to four times the rate once they hit
trouble — precise framing is the difference being measured.

## Sequence

Work in this order. Each pass is cheap; discovering the same defect after the task graph exists is not.

1. **Read the whole PRD once without commenting.** Note where you had to re-read a sentence.
2. **Attack each requirement in isolation.** Apply the tests below; record an id for every failure.
3. **Attack the requirement set as a whole.** Look for contradictions, gaps, and requirements that
   cannot all hold at once.
4. **Attack the framing.** Is this the right problem, and is the stated scope the smallest version of it?
5. **Report.** Short list, requirement id, the specific question the author must answer.

## Per-requirement tests

A requirement fails if any of these is unanswered.

- **Testable**: can someone write the check without knowing the implementation? If the answer is no, the
  requirement is a wish.
- **Single**: does it join two capabilities with "and"? Split it.
- **Bounded**: what happens on failure, on timeout, on empty input, on concurrent access? Unstated
  failure behavior is the most common defect in otherwise good requirements.
- **Measured**: does any word imply a number — fast, scalable, secure, reliable — without one? Replace it
  with a target and a measurement window.
- **Sourced**: does it come from a stakeholder, a regulation, or the author's preference? The last one is
  scope creep wearing a requirement's clothes.
- **Stable**: will it survive a stack change? A requirement that names a technology has drifted out of
  the PRD and into a design decision.

## Set-level tests

- **Contradiction**: two requirements that cannot both be satisfied, especially across functional and
  non-functional sections.
- **Gap**: a journey that starts and never finishes, an entity created and never deleted, an error raised
  with no stated handling.
- **Orphan**: a requirement nothing else references, which usually means it is speculative.
- **Missing non-functional coverage**: no latency, availability, or capacity requirement on a system that
  plainly needs one.
- **Missing explicit exclusion**: nothing is out of scope, which means nothing has been decided.
- **Traceability**: can every requirement be reached by a task later, and every task by a requirement?

## Known failure modes of this step

- **Verbatim agreement.** Restating the PRD back is not a review.
- **Rewriting the PRD unasked.** During review, report the defect and ask. Once the user gives direction,
  apply it: update the PRD, ADR, or task in the same work instead of stopping at the report.
- **Volume over severity.** A list of fifteen style notes buries the one contradiction that matters.
  Order by impact and drop the noise.
- **Assuming the implementation.** A finding that depends on a design choice leaks the design phase into
  the requirements phase.
- **False precision.** Demanding a number the author cannot supply yet is a finding about the author's
  uncertainty, not about the requirement. Ask which reading they intend instead.

## What counts as a finding

A finding names a requirement id, states the specific defect, and ends in a question the author can
answer. "FR-004 has no failure behavior — what should happen when the upstream call times out?" is a
finding. "FR-004 could be clearer" is not.

## When to stop

The review ends when the remaining findings are all resolved or explicitly accepted by the author.
Unresolved findings are reported with the task graph, not hidden, because a task built on an unanswered
question is a task that will be redone.