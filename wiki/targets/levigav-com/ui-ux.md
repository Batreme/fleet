---
title: "UI & Design System: levigav-com"
date: 2026-11-14
target: "[[overview|levigav-com]]"
---

# UI Architecture & Design Tokens: levigav-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--pg-serif` | `"Instrument Serif", "Times New Roman", Times, serif` |
| `--pg-tag` | `"LVG Pick L", "LVG Pick Tag", "LVG Tag L", "Sedgwick Ave Dis` |
| `--pg-stencil` | `"LVG Pick Stencil", "Big Shoulders Stencil Display", Impact,` |
| `--pg-red` | `#e3241b` |
| `--pg-red-hot` | `#ff3b2f` |
| `--pg-yellow` | `#ffe11a` |
| `--pg-ink` | `#0b0b0c` |
| `--pg-chalk` | `#f4f2ec` |
| `--pg-speckle` | `url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000` |
| `--pg-dust` | `url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000` |
| `--gold` | `focus-visible .pick__cta{box-shadow:inset 0 1px #ffffff61,in` |
| `--pk-fs` | `clamp(110px, 12.8vw, 220px)` |
| `--x` | `20%` |
| `--l` | `1` |
| `--d` | `0s` |
| `--street` | `focus-visible .pick__cta{background-color:var(--pg-red-hot)` |
| `--pk-fs` | `clamp(80px, 23vw, 118px)}.pick__sticker{padding:8px 12px 7px` |
| `--pk-fs` | `clamp(72px, 9vw, 130px)}.pick__hangtag{display:none}}@media ` |
| `--at` | `0` |
| `--vh` | `1vh` |
| `--h` | `min(calc(var(--vh) * 64), 75vw)` |
| `--w` | `calc(var(--h) * .7085)` |
| `--bw` | `calc(var(--h) * .3)` |
| `--ring` | `calc(var(--h) * .82)` |
| `--line` | `calc(var(--h) * .8)` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `nav__links` |
| `<nav>` | `-` | `menu__links` |
| `<nav>` | `-` | `links` |
| `<nav>` | `-` | `` |
| `<nav>` | `-` | `` |
| `<header>` | `-` | `nav` |
| `<header>` | `-` | `work__head wrap` |
| `<header>` | `-` | `aim__sheet-head` |
| `<main>` | `main` | `` |
| `<footer>` | `-` | `` |
| `<footer>` | `-` | `sx__ref kicker kicker--yellow` |
| `<footer>` | `-` | `sx__cref kicker kicker--yellow` |
| `<footer>` | `-` | `footer` |
