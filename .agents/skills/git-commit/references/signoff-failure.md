# Sign-off failure

The whole point of this file is that the agent must **not** repair a missing git identity. It reports the
failure and stops.

## The rule

Do not check `user.name` or `user.email` before committing. Do not run `git config --list`, do not run
`git config --get user.email`, and do not read `.git/config`. There is no pre-flight and no validation step.

`git commit -s` is the check. Let it fail.

## What the failure looks like

When the identity is unset, `git commit -s` aborts before creating the commit:

```
Author identity unknown

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'user@host.(none)')
```

Related variants worth recognising:

```
*** Please tell me who you are.
fatal: could not lookup user.email
error: unable to auto-detect email address
```

## What to do

1. Report the error text verbatim. Do not paraphrase it.
2. Tell the user to set their **project** identity, and give the exact commands to run themselves.
3. Stop and wait. Do not retry.

The message to give the user:

```
The commit was rejected because this repository has no author identity set.
Please set it for this project and I'll retry:

  git config user.name "Your Name"
  git config user.email "you@example.com"

Run those from inside the repository, and omit --global so it stays project-scoped.
```

Note that git's own error text suggests `--global`. Follow the user's instruction, not git's suggestion:
project-scoped config is what was asked for, and `--global` would change every repository on the machine.

## Prohibited workarounds

None of these are acceptable, and each one appears in the list because it is a plausible thing an agent
might do to be helpful. Do not do any of them, even partially, even "just to test".

- Writing the identity: `git config user.name "..."`, `git config user.email "..."`, with or without
  `--global`.
- Injecting it per-command: `git -c user.name=... -c user.email=... commit`.
- Injecting it through the environment: `GIT_AUTHOR_NAME`, `GIT_AUTHOR_EMAIL`, `GIT_COMMITTER_NAME`,
  `GIT_COMMITTER_EMAIL`, or `EMAIL`.
- Editing `.git/config` directly, or any tool that rewrites it.
- Overriding just the author with `git commit --author="..."`.
- Asking for, guessing at, or reusing an email address found elsewhere on the system.
- Dropping `-s` so the commit succeeds. This is the most tempting bypass and it defeats the requirement
  outright: the sign-off is not optional.
- Disabling hooks or signing to get past an unrelated failure (`--no-verify`, `-c commit.gpgsign=false`).

## Why the agent must not set it

- A `Signed-off-by` trailer is the user's attestation that they have the right to contribute the work
  under the project's licence. Writing it on their behalf makes the attestation false.
- The identity is a personal credential, not project configuration the agent owns.
- A wrong or invented address in the permanent history is worse than a commit that did not happen: it is
  hard to remove, and it attributes work to the wrong person.

## Failures that are not the identity

Do not misdiagnose these, and do not reach for the workaround list above.

- **Nothing staged** — `nothing added to commit`. Stage the right paths; do not `git add -A`.
- **A failing hook** — report the hook's output. Never `--no-verify`.
- **GPG signing failure** — that is `-S`, not `-s`. A missing key or a locked agent is reported to the
  user; do not disable `commit.gpgsign`, and do not confuse it with the sign-off trailer.
- **Detached HEAD** — say so and ask which branch to use. Do not create a branch unasked.
- **Nothing to commit / empty commit** — report it rather than reaching for `--allow-empty`.