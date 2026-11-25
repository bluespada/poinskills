# PRD checklist

Run this before submitting the PRD. Report every unchecked box with the reason it stays unchecked rather
than ticking it optimistically.

## Completeness

- [ ] No `[NEEDS CLARIFICATION]` markers remain, or each one is reported to the user as an open decision
- [ ] Every requirement has an ID, and no ID is reused from a retired requirement
- [ ] Every requirement carries priority, status, and verification method
- [ ] No speculative or "might need later" requirements
- [ ] Out-of-scope items are listed wherever a reader would otherwise assume inclusion

## Quality

- [ ] No implementation details: no product names, cloud providers, frameworks, APIs, or file layout
- [ ] Requirements are testable and unambiguous, read as constraints rather than intentions
- [ ] Success criteria are measurable and checkable without knowing the implementation
- [ ] SLOs state a target and a measurement window
- [ ] No requirement contains "and" joining two capabilities
- [ ] Assumptions are stated explicitly rather than silently embedded
- [ ] Cost constraints cover setup and ongoing spend, when the section is used
- [ ] Compliance frameworks and data-handling rules are named, when the section is used

## Frontmatter

- [ ] All seven keys present, in the declared order
- [ ] `status` is one of `draft`, `pending`, `complete`, `canceled`
- [ ] `tasks` is a list, empty at this stage unless the plan step already ran
- [ ] `authored` lists the contributors rather than a single placeholder
- [ ] `createdAt` and `updatedAt` are ISO-8601 UTC and consistent with each other
- [ ] The path is `specs/prd/<NNN>-<slug>.md` and the number does not collide

## Traceability

- [ ] Every requirement can be linked forward to a plan decision
- [ ] Requirements not yet planned are marked, not silently left bare
- [ ] The header records that later requirement changes must propagate into the task files under `tasks`
- [ ] Spec ID, directory name, and intended branch name agree

## Scope discipline

- [ ] The PRD describes one feature, not a roadmap
- [ ] Dependencies on other systems or teams are named
- [ ] No commitment is made about schedule or sequence; that is planning's job