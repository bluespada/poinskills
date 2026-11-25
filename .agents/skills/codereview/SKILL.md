---
name: codereview
description: You must use this skill when the user asks to review code or audit pull requests or set review policy or handle AI-generated and agent-authored changes to enforce small fast checks plus evidence-grounded oversight. It guides sizing diffs for single reviewers and enforcing fast first response and demanding runnable proof for agent claims and screening omission and security risks and using AI reviewers without anchoring bias and measuring adoption instead of felt speed and blocking unverified merges with explicit ownership.
---

# Code Review Methodology

## Human Changes
- Keep diffs at or under 200 lines and focused on one issue and reject oversized changes for stacking
- Assign exactly one primary reviewer and add a second only for a different axis like security or ownership
- Give first response within one business day and use conditional approval with follow-up comments to unblock time zones
- Require author annotation with context and entry checklist before requesting review
- Push style and formatting and static checks to automation and reserve human attention for logic and design and architecture
- Never use individual defect counts or review metrics for performance or compensation decisions

## Agent-Authored Changes
- Co-plan approach plus acceptance tests before the agent writes code and reject execution without agreed scope
- Demand groundable evidence for every agent claim with tests that fail without the patch plus execution logs plus static analysis
- Read requirements against the diff to hunt omitted branches and edge cases and skipped constraints first
- Run mandatory separate security review on agent code because functional tests pass on insecure code
- Graduate oversight by blast radius with automated monitoring for internal reversible changes and human approval for customer-facing and human-in-loop for regulated or strategic changes
- Treat median approval under one hour as triage signal and force deeper re-review with clear ownership

## AI Assistance Guardrails
- Use AI review only as first-pass screen with hard precision filter over a rule taxonomy and feed adoption back
- Do independent human pass before viewing AI output or deliberately re-check regions AI did not flag to defeat anchoring
- Favor explanations that invite scrutiny and distrust confident summaries and long traces without checkable artifacts
- Track comment adoption and outdated-line rate and closure time and never trust felt speedup without measurement
- Block merge on residual uncertainty and unclear ownership and unverified behavior regardless of AI approval