---
title: "UI & Design System: www-paragonproductions-co"
date: 2026-11-14
target: "[[overview|www-paragonproductions-co]]"
---

# UI Architecture & Design Tokens: www-paragonproductions-co

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--_theme---background--primary` | `var(--_color---swatch--white)` |
| `--_text-style---font-family` | `var(--_typography---font-family--tertiary)` |
| `--_theme---text--primary` | `var(--_color---swatch--black)` |
| `--_text-style---font-size` | `var(--_typography---font-size--text-main)` |
| `--_text-style---line-height` | `var(--_typography---line-height--131-5)` |
| `--_text-style---font-weight` | `var(--_typography---font-weight--normal)` |
| `--_text-style---letter-spacing` | `var(--_typography---letter-spacing--0em)` |
| `--_typography---font-family--secondary` | `"Review Condensed",Arial,sans-serif` |
| `--_typography---font-weight--medium` | `500` |
| `--_text-style---margin-top` | `var(--_spacing---space--4)` |
| `--_text-style---margin-bottom` | `var(--_spacing---space--5)` |
| `--_spacing---space--6` | `clamp(1.5*1rem,((1.5 - ((2.5 - 1.5)/(var(--site--viewport-ma` |
| `--_spacing---space--5` | `clamp(1.25*1rem,((1.25 - ((2 - 1.25)/(var(--site--viewport-m` |
| `--_color---swatch--red` | `#ff5b4b` |
| `--_typography---font-family--primary` | `"Proxima Nova",Arial,sans-serif` |
| `--_theme---text--secondary` | `var(--_color---swatch--grey-500)` |
| `--_typography---font-weight--thin` | `100` |
| `--_typography---font-weight--extra-light` | `200` |
| `--_typography---font-weight--light` | `300` |
| `--_typography---font-weight--normal` | `400` |
| `--_typography---font-weight--semibold` | `600` |
| `--_typography---font-weight--extra-bold` | `800` |
| `--_typography---font-weight--bold` | `700` |
| `--_typography---font-weight--black` | `900` |
| `--_color---swatch--transparent` | `transparent` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `nav_wrap` |
| `<main>` | `main` | `page_main` |
| `<footer>` | `-` | `footer_wrap` |
