---
title: "UI & Design System: dairyfoodbg-com"
date: 2026-11-14
target: "[[overview|dairyfoodbg-com]]"
---

# UI Architecture & Design Tokens: dairyfoodbg-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--w-backdrop-animation` | `initial}.w-popover-mask{opacity:0!important` |
| `--large` | `before{border-width:5px` |
| `--large` | `after{border-width:5px` |
| `--vertical` | `before,.w-widget-twitter-count-shim.w--vertical:after{conten` |
| `--vertical` | `before{border-width:5px` |
| `--vertical` | `after{border-width:4px` |
| `--hero-ease-spring` | `cubic-bezier(.34, 1.3, .64, 1)` |
| `--hero-ease-smooth` | `cubic-bezier(.22, 1, .36, 1)}[data-hero-stat]{opacity:0` |
| `--cc-font-family` | `inherit` |
| `--cc-font-family-heading` | `var(--cc-font-family)` |
| `--cc-font-family-mono` | `ui-monospace, SFMono-Regular, Menlo, Consolas, monospace` |
| `--cc-font-size` | `1em` |
| `--cc-line-height` | `1.5` |
| `--cc-title-size` | `1.125em` |
| `--cc-title-weight` | `600` |
| `--cc-title-transform` | `none` |
| `--cc-title-spacing` | `0` |
| `--cc-text-size` | `.9375em` |
| `--cc-small-size` | `.8125em` |
| `--cc-btn-size` | `.9375em` |
| `--cc-btn-weight` | `500` |
| `--cc-btn-spacing` | `0` |
| `--cc-btn-transform` | `none` |
| `--cc-color-bg` | `#ffffff` |
| `--cc-color-fg` | `#171717` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `hero__nav is-hidden is-labelled` |
| `<nav>` | `-` | `cc__links` |
| `<nav>` | `-` | `cc__links` |
| `<header>` | `-` | `navbar` |
| `<header>` | `-` | `cc__dialog-head` |
| `<main>` | `main-content` | `` |
| `<footer>` | `-` | `site-footer` |
| `<footer>` | `-` | `cc__dialog-actions cc__actions` |
