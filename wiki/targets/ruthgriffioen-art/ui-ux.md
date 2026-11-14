---
title: "UI & Design System: ruthgriffioen-art"
date: 2026-11-14
target: "[[overview|ruthgriffioen-art]]"
---

# UI Architecture & Design Tokens: ruthgriffioen-art

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--ink` | `#111111` |
| `--paper` | `#ffffff` |
| `--muted` | `#6f6f6f` |
| `--line` | `rgba(17, 17, 17, .12)` |
| `--soft` | `#f8f1eb` |
| `--accent` | `#4d1224` |
| `--accent-ink` | `#ffffff` |
| `--accent-light` | `#c77b8c` |
| `--font-display` | `"Playfair Display", Georgia, "Times New Roman", serif` |
| `--font-body` | `"Inter", system-ui, -apple-system, "Segoe UI", sans-serif` |
| `--step--2` | `.6875rem` |
| `--step--1` | `.8125rem` |
| `--step-0` | `1rem` |
| `--step-1` | `clamp(1.125rem, 1.042rem + .3704vw, 1.375rem)` |
| `--step-2` | `clamp(1.312rem, 1.125rem + .8333vw, 1.875rem)` |
| `--step-3` | `clamp(1.75rem, 1.417rem + 1.481vw, 2.75rem)` |
| `--step-4` | `clamp(2.125rem, 1.5rem + 2.778vw, 4rem)` |
| `--step-5` | `clamp(2.75rem, 1.667rem + 4.815vw, 6rem)` |
| `--step-6` | `clamp(3.5rem, 1.75rem + 7.778vw, 8.75rem)` |
| `--step-7` | `clamp(4rem, 2rem + 8.889vw, 10rem)` |
| `--space-3xs` | `.25rem` |
| `--space-2xs` | `clamp(.375rem, .3333rem + .1852vw, .5rem)` |
| `--space-xs` | `clamp(.5rem, .4167rem + .3704vw, .75rem)` |
| `--space-s` | `clamp(.75rem, .6667rem + .3704vw, 1rem)` |
| `--space-m` | `clamp(1rem, .8333rem + .7407vw, 1.5rem)` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `site-nav` |
| `<nav>` | `-` | `menu-panel__links` |
| `<nav>` | `-` | `site-footer__legal` |
| `<header>` | `-` | `site-header` |
| `<header>` | `-` | `cart-drawer__head` |
| `<main>` | `MainContent` | `page-main` |
| `<footer>` | `-` | `site-footer site-footer--overlay` |
| `<footer>` | `-` | `cart-drawer__foot` |
