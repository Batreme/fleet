---
title: "UI & Design System: its-tomo-dev"
date: 2026-11-14
target: "[[overview|its-tomo-dev]]"
---

# UI Architecture & Design Tokens: its-tomo-dev

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--bg` | `#0b0b0c` |
| `--fg` | `#ecebe6` |
| `--fg-2` | `rgb(236 235 230 / 70%)` |
| `--fg-3` | `rgb(236 235 230 / 60%)` |
| `--rule` | `rgb(236 235 230 / 16%)` |
| `--neon` | `#f7b334` |
| `--f-display` | `archivo, "Helvetica Neue", arial, sans-serif` |
| `--f-mono` | `"JetBrains Mono", ui-monospace, menlo, monospace` |
| `--f-logo` | `var(--f-mono)` |
| `--t-hero` | `clamp(2.6rem, 6.2vw, 7.2rem)` |
| `--t-h2` | `clamp(1.9rem, 3.2vw, 3.4rem)` |
| `--t-lede` | `clamp(1.05rem, 1.2vw, 1.3rem)` |
| `--t-body` | `clamp(0.95rem, 0.95vw, 1.05rem)` |
| `--t-mono` | `clamp(0.75rem, 0.75vw, 0.8125rem)` |
| `--gutter` | `clamp(1rem, 3vw, 3rem)` |
| `--header-h` | `clamp(3.5rem, 6vw, 5.25rem)` |
| `--dash-h` | `2.75rem` |
| `--ease-out` | `cubic-bezier(0.16, 1, 0.3, 1)` |
| `--ui-fade` | `0.4s` |
| `--ui-gap` | `0.2s` |
| `--unfocus` | `15px` |
| `--focus-pull` | `4.2s` |
| `--unfocus` | `8px` |
| `--focus-pull` | `2.5s}.c-stage__poster,.c-stage__canvas{position:absolute` |
| `--side-dark` | `rgb(5 5 6 / 74%)` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `c-nav` |
| `<header>` | `-` | `c-header` |
| `<main>` | `top` | `c-garage` |
| `<footer>` | `-` | `c-footer js-fade` |
