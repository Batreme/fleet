---
title: "UI & Design System: theinfinitysocks-com"
date: 2026-11-14
target: "[[overview|theinfinitysocks-com]]"
---

# UI Architecture & Design Tokens: theinfinitysocks-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
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
| `--cc-color-muted` | `#6b6b6b` |
| `--cc-color-border` | `color-mix(in srgb, var(--cc-color-fg) 14%, transparent)` |
| `--cc-color-divider` | `color-mix(in srgb, var(--cc-color-fg) 10%, transparent)` |
| `--cc-color-surface` | `color-mix(in srgb, var(--cc-color-fg) 5%, transparent)` |
| `--cc-color-accent` | `#171717` |
| `--cc-color-accent-hover` | `#000000` |
| `--cc-color-accent-fg` | `#ffffff` |
| `--cc-color-focus` | `#2f6acf` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `cc__links` |
| `<nav>` | `-` | `cc__links` |
| `<nav>` | `-` | `foot__nav` |
| `<header>` | `-` | `cc__dialog-head` |
| `<header>` | `bar` | `bar` |
| `<main>` | `main` | `site__main` |
| `<footer>` | `-` | `cc__dialog-actions cc__actions` |
| `<footer>` | `footer` | `foot` |
