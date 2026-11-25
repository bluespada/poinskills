# EULA Routing and Lawful Workarounds

## Clause types seen in the wild
- Absolute: "You may not reverse engineer, decompile or disassemble the Software." Bandizip and Intel both use this; Bandizip additionally requires prior written consent for decompilation
- Carve-out: "except and only to the extent that the applicable copyright law expressly permits doing so" Microsoft Services Agreement, Google Chrome ToS section 9.2, and the Slack Software Integration Supplement all use this shape
- RE plus functionality ban: Zoom bars building a "competitive product" or a product "substantially similar to" the Services; Microsoft Online Services terms bar using the service to "replicate product functionality"

## Routing
- Carve-out plus US: proceed under fair use for interoperability, document the purpose, prefer observation over decompilation where possible
- Any class plus EU: Directive 2009/24/EC Article 5(3) permits observing and testing to determine the ideas and principles, Article 6 permits interoperability decompilation, and Article 8 makes contradicting clauses null and void; note Article 6(2)(c) bars using decompiled information to build something substantially similar in expression
- Absolute plus US: observation, tracing, sniffing, and memory dumps of your own instance only, no decompilation; request written authorization if internals are required
- RE plus functionality ban: flag to a human before reimplementation begins; the exposure is contract rather than copyright, and SaaS terms often do not govern a downloaded app at all
- Unknown clause or unknown jurisdiction: stop and ask the user

## Workarounds when the door is closed
- Want behavior facts: black-box runs and MITM capture need no decompilation and sit outside most reverse-engineering clauses
- Want internals behind an absolute clause: email the vendor for written authorization; many publish API docs or interoperability statements that already cover the need
- Want a compatible implementation in the EU: lean on Article 5(3) observation, decompile only under Article 6, and keep the result inside the interoperability purpose
- Want a compatible implementation in the US: document the interoperability purpose, copy only what compatibility requires, keep the clean-room trail intact
- Want to test vendor security: check for a safe-harbor statement, such as the disclose.io listings or a bug bounty with legal protection; a bounty without safe harbor is not authorization

## No workaround exists for
- Cracked, pirated, leaked, or dumped copies; acquire lawfully instead
- Networks, accounts, or servers you do not own; use your own
- Continuing after a cease-and-desist; authorization is revoked, so stop and get counsel
- Server-side data mining discovered through captured traffic; disclose the flaw instead
- Distributing circumvention tools built during research; keep them internal