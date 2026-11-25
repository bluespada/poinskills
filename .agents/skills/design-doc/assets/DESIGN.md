---
version: alpha
name: {{PRODUCT}}
description: {{one line describing the product's visual identity}}
omitted:
  - section: {{SECTION_NAME}}
    reason: "{{why this design system does not carry it}}"
colors:
  primary: "{{#RRGGBB}}"
  secondary: "{{#RRGGBB}}"
  neutral: "{{#RRGGBB}}"
typography:
  {{level-name}}:
    fontFamily: {{Font Family}}
    fontSize: {{16px}}
    fontWeight: {{400}}
    lineHeight: {{1.5}}
rounded:
  {{scale-level}}: {{8px}}
spacing:
  {{scale-level}}: {{16px}}
components:
  {{component-name}}:
    backgroundColor: "{colors.primary}"
    textColor: "{{#RRGGBB}}"
    rounded: "{rounded.{{scale-level}}}"
    padding: {{12px}}
---

# {{PRODUCT}} design system

## Overview

{{Holistic look and feel: brand personality, audience, and the response the interface should evoke.}}

## Colors

{{The palette and the role each color plays. Name each color and its token in the same bullet.}}

## Typography

{{The typeface strategy and what each level is for.}}

## Layout

{{The layout and spacing model.}}

## Elevation & Depth

{{How hierarchy is conveyed: shadow, tone, or border.}}

## Shapes

{{The corner-radius language.}}

## Components

{{Per-component guidance, one entry per component defined in the front matter.}}

## Do's and Don'ts

- Do {{guideline}}.
- Don't {{pitfall}}.