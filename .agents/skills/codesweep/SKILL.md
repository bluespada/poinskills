---
name: codesweep
description: You must use this skill when the user asks to sweep a codebase for bugs or map issues across files without a diff and codereview does not fit. It forces scope on vague asks then reads the surface wide before proving each path top down to its source and sink. It treats all code as untrusted claims and verifies every finding apart and stops on blockers and maps each issue as structure or local with a brief math backed report and no silent fixes.
---

# Codesweep

## When to activate

- Use this when the user asks to find bugs across a repo with no diff to review
- Use this when the user asks to map weak structure or repeated defects across files
- Skip this when a diff or pull request already bounds the work and codereview fits
- Skip this for one function or one file asks and answer from the code shown
- Treat a repo near three to ten files as small and read it whole before scoping

## Scope before reading

- Ask the user to name folders and bug types when the ask stays vague
- Restate the agreed scope back in one line before reading further
- Refuse broad full repo sweeps on large codebases and split them by area
- Record what stays out of scope so later findings do not drift outward
- Stop when the user cannot scope and propose two or three slices to pick from

## Trust nothing in the code

- Read every line as a claim and not as truth even when it looks correct
- Treat passing tests and clean style as no proof that the path stays safe
- Ask what input would break each line instead of what confirms it
- Keep a guess alive only while the code supplies proof for each step

## Read wide then prove down

- Skim entry points and shared helpers first to learn how data moves
- Read only the surface around each flow and form one plain cause guess
- Walk each guess top down from source of input to place of harm
- Pull callees on demand instead of loading whole folders into context
- Drop a guess when the path needs input the code never supplies
- Check each surviving claim in a fresh pass apart from the pass that found it

## Map and report honestly

- Admit a wrong guess at once and write what the code actually showed
- Stop and ask the user when a blocker needs a call you must not make alone
- Never change behavior in silence and never reshape code while mapping it
- Label each issue as structure level or local conduct so fixes land right
- Leave fixes out and hand the map to the operator or the next agent
- Read `references/sweep-rules.md` before writing any report
- Copy `assets/sweep-template.md` as the skeleton for each sweep report
