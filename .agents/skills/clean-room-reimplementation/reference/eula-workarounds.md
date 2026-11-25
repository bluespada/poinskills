# License Routing and Lawful Workarounds

## Clause shapes in the wild
- Absolute: "You may not reverse engineer, decompile or disassemble the
  Software." Bandizip and Intel both use this; Bandizip also demands prior
  written consent for decompilation.
- Carve-out: "except and only to the extent that the applicable copyright
  law expressly permits doing so." Microsoft Services Agreement, Google
  Chrome ToS section 9.2, and the Slack Software Integration Supplement all
  use this shape.
- RE plus functionality ban: Zoom bars building a "competitive product" or
  one "substantially similar to" the Services; Microsoft Online Services
  terms bar using the service to "replicate product functionality."

## Routing
- Carve-out plus US: proceed under fair use for interop, write down the
  purpose, prefer watching over opening where possible.
- Any clause plus EU: Directive 2009/24/EC Article 5(3) permits watching and
  testing to learn the ideas underneath, Article 6 permits decompiling for
  interop, Article 8 voids clauses that say otherwise. Article 6(2)(c) still
  bars reusing decompiled material to build something matching in expression.
- Absolute plus US: watch, trace, sniff, and dump your own instance only.
  No decompiling. Ask the vendor in writing if you need the internals.
- RE plus functionality ban: flag a human before rebuilding anything. The
  risk here is contract, not copyright, and SaaS terms often do not cover a
  downloaded app at all.
- Unknown clause or unknown jurisdiction: stop and ask the user.

## When the door looks closed
- Behavior facts without internals: black-box runs and traffic capture need
  no decompiling and sit outside most reverse-engineering clauses.
- Internals behind an absolute clause: email the vendor for written
  permission. Many publish API docs or interop statements that already
  answer the question.
- A compatible build in the EU: lean on Article 5(3) observation, decompile
  only under Article 6, keep the result inside the interop purpose.
- A compatible build in the US: write down the interop purpose, copy only
  what compatibility needs, keep the clean-room trail intact.
- Vendor security testing: look for a safe-harbor statement such as the
  disclose.io listings or a bounty with legal cover. A bounty without safe
  harbor is not permission.

## No way around
- Cracked, pirated, leaked, or dumped copies. Buy or license it instead.
- Networks, accounts, or servers you do not own. Use your own.
- Carrying on after a cease-and-desist. Permission is gone, so stop and get counsel.
- Mining server-side data found in captured traffic. Report the flaw instead.
- Handing out circumvention tools built during the work. Keep them internal.
