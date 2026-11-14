---
title: "UI & Design System: rialto-com-au"
date: 2026-11-14
target: "[[overview|rialto-com-au]]"
---

# UI Architecture & Design Tokens: rialto-com-au

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--color-white` | `#fff` |
| `--color-white-thin` | `rgba(255, 255, 255, 0.5)` |
| `--color-black` | `#000` |
| `--color-current-thin` | `color-mix(in srgb, currentColor 50%, transparent 50%)` |
| `--color-current-thin-md` | `color-mix(in srgb, currentColor 75%, transparent 25%)` |
| `--color-gray-300` | `#d1d4d6` |
| `--color-gray-700` | `#3d3d3b` |
| `--color-gray-800` | `#231f20` |
| `--color-gray-900` | `#080808` |
| `--color-blue-700` | `#004bff` |
| `--color-pink-400` | `#ffc8ff` |
| `--color-body-bg` | `#080808` |
| `--color-body-color` | `#fff` |
| `--color-accent` | `var(--color-blue-700)` |
| `--color-secondary` | `var(--color-gray-900)` |
| `--color-light` | `var(--color-white)` |
| `--theme-name` | `rialto-2026` |
| `--ff-sharp-grotesk` | `"Sharp Grotesk"` |
| `--ff-gotham` | `"Gotham"` |
| `--t-duration` | `0.3s}.gfield input:not([type=radio]):not([type=checkbox]):no` |
| `--button-border-color` | `var(--color-white)` |
| `--button-background-color` | `var(--color-white)` |
| `--button-text-color` | `var(--color-secondary)}.gform_button:is(:hover,:focus-visibl` |
| `--button-background-color` | `transparent` |
| `--button-text-color` | `var(--color-white)}.active.gform_button,.active.gform-button` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `nav` |
| `<nav>` | `-` | `nav` |
| `<header>` | `-` | `header borders` |
| `<main>` | `content` | `` |
| `<footer>` | `-` | `footer` |
