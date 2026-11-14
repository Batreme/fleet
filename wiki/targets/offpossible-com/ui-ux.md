---
title: "UI & Design System: offpossible-com"
date: 2026-11-14
target: "[[overview|offpossible-com]]"
---

# UI Architecture & Design Tokens: offpossible-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--edge-inset` | `max(20px, 2vmin)` |
| `--header-logo-width` | `24.53vw` |
| `--header-logo-height` | `calc(var(--header-logo-width) * 75 / 533)` |
| `--header-logo-ink-top` | `calc(var(--header-logo-height) * 2.98828 / 75)` |
| `--site-symbol-size` | `calc(var(--header-logo-height) * 70.39 / 75)` |
| `--font-mono` | `"ABC Diatype Semi Mono", ui-monospace, "SF Mono", Menlo, mon` |
| `--font-display` | `var(--font-mono)` |
| `--font-ui` | `"Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Robo` |
| `--font-symbol` | `"ABC Diatype Semi Mono", "Apple Symbols", "Segoe UI Symbol",` |
| `--instrument-panel-gap` | `clamp(16px, 1.5vw, 24px)` |
| `--scramble-color` | `#000!important}html[data-easter-phase=generated] .stack-line` |
| `--edge-inset` | `max(20px, 3vmin)` |
| `--header-logo-width` | `min(250px, 70vw)` |
| `--mobile-screen-inset` | `24px` |
| `--mobile-screen-padding-x` | `8px` |
| `--mobile-shader-overscan-y` | `240px}.ribbon-container{inset:calc(var(--mobile-shader-overs` |
| `--instrument-panel-gap` | `0px` |
| `--header-logo-width` | `min(24.53vw, 200px)}#home .stack-line{letter-spacing:-.02em` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<aside>` | `instrument-panel` | `instrument-panel` |
| `<main>` | `-` | `scroll-wrapper` |
| `<footer>` | `-` | `site-footer` |
