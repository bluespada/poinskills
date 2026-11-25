# DESIGN.md format

The normative format for `specs/DESIGNS.md` and every `specs/designs/*-designs.md`. Source:
`github.com/google-labs-code/design.md` (spec version `alpha`).

A `DESIGN.md` is a plain-text representation of a design system: a visual identity that humans and
coding agents both read. It has two parts.

- YAML front matter carrying machine-readable design tokens, opened and closed by a line containing
  exactly `---`.
- A markdown body carrying human-readable rationale, in a fixed section order.

Tokens are normative. Prose explains why a value exists and how to apply it. A document may omit the
front matter entirely, but a file with tokens must put them in it.

## Front matter schema

```yaml
version: <string>                          # optional, current: "alpha"
name: <string>                             # required
description: <string>                      # optional
omitted: <string[] | OmittedSection[]>     # optional, sections deliberately absent
colors:
  <token-name>: <Color>
typography:
  <token-name>: <Typography>
rounded:
  <scale-level>: <Dimension>
spacing:
  <scale-level>: <Dimension | number>
components:
  <component-name>:
    <token-name>: <string | token reference>
```

## Token types

- Color: any CSS color string, including `#RRGGBB`, `#RRGGBBAA`, named colors, `rgb()`, `hsl()`,
  `oklch()`, `lab()`, and `color-mix()`. Hex is the recommended default.
- Dimension: a number with a `px`, `em`, or `rem` unit.
- Typography: an object of `fontFamily`, `fontSize`, `fontWeight`, `lineHeight`, `letterSpacing`,
  `fontFeature`, `fontVariation`. `lineHeight` also accepts a unitless multiplier.
- Token reference: `{path.to.token}`, for example `{colors.primary}`. It must resolve to a primitive,
  except inside `components`, where a composite reference such as `{typography.label-md}` is allowed.
- Component property tokens: `backgroundColor`, `textColor`, `typography`, `rounded`, `padding`,
  `size`, `height`, `width`. A component variant is a sibling entry with a related key, such as
  `button-primary-hover`.
- Omitted: a list of section names, or `{section, reason}` objects, for sections this design system
  deliberately does not carry. It suppresses the linter's missing-section findings.

## Section order

Sections are `##` headings. They may be omitted, but those present must appear in this order:

1. Overview — also accepted as "Brand & Style"
2. Colors
3. Typography
4. Layout — also accepted as "Layout & Spacing"
5. Elevation & Depth — also accepted as "Elevation"
6. Shapes
7. Components
8. Do's and Don'ts

An optional `#` title may appear for document titling and is not parsed as a section.

## Lint rules

`npx @google/design.md lint <file>` exits 1 on errors, 0 otherwise, and emits JSON.

- `broken-ref` (error): a `{…}` reference resolves to no defined token.
- `missing-primary` (warning): colors exist but none is `primary`.
- `contrast-ratio` (warning): a component's `textColor` on `backgroundColor` falls below WCAG AA,
  4.5:1.
- `orphaned-tokens` (warning): a color token no component references.
- `missing-typography` (warning): colors exist but no typography tokens do.
- `section-order` (warning): sections are out of the canonical order.
- `unknown-key` (warning): a top-level key looks like a typo of a schema key.
- `token-like-ignored` (warning): an unknown key holds token-like values.
- `missing-sections` (info): optional sections absent while other tokens exist.
- `token-summary` (info): how many tokens each section defines.
- `omitted-rules` (info): the `omitted` mapping names an unknown or redundant section.

Unknown section headings are preserved rather than rejected. Duplicate section headings are an error.

## Commands

- `npx @google/design.md lint <file>` — validate; `--format json` for machine output, `-` for stdin.
- `npx @google/design.md diff <before> <after>` — token-level regression check.
- `npx @google/design.md export --format json-tailwind|css-tailwind|dtcg <file>` — emit Tailwind or
  W3C DTCG tokens.
- `npx @google/design.md spec --rules` — print the format specification and the lint rules.
- On Windows the `design.md` bin name collides with the Markdown file association; use the `designmd`
  alias instead.