---
title: "UI & Design System: herasymenkox-com"
date: 2026-11-14
target: "[[overview|herasymenkox-com]]"
---

# UI Architecture & Design Tokens: herasymenkox-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--y-w` | `600` |
| `--y-h` | `580` |
| `--cap` | `0.0915em` |
| `--cap` | `var(--cap-bold)` |
| `--ext` | `calc(5.5 * var(--px) - 0.0635em)` |
| `--cap` | `0.1715em` |
| `--cap` | `0.1215em` |
| `--cap` | `var(--cap-mono)` |
| `--cap` | `0.293em` |
| `--cap` | `0.243em` |
| `--cap` | `0.1215em` |
| `--px` | `calc(min(100vw, 2560px) / var(--design-width))` |
| `--k` | `0.40487` |
| `--design-width` | `1440` |
| `--container` | `clamp(1440px, 100vw, 2560px)` |
| `--px` | `calc(var(--container) / var(--design-width))` |
| `--green` | `#cee49f` |
| `--black` | `#0b0b0b` |
| `--green-12` | `rgba(206, 228, 159, 0.12)` |
| `--cap-bold` | `0.0215em` |
| `--cap-mono` | `0.143em` |
| `--cap-height` | `0.715em` |
| `--design-width` | `375` |
| `--container` | `100vw` |
| `--fs` | `calc((100vw - 32 * var(--px)) / 6.6006)` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `blend menu ui-mask` |
| `<nav>` | `-` | `blend h3 view-switch ui-mask` |
