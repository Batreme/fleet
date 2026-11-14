---
title: "UI & Design System: mauricemoynihan-com"
date: 2026-11-14
target: "[[overview|mauricemoynihan-com]]"
---

# UI Architecture & Design Tokens: mauricemoynihan-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--bone` | `#EFEDE6` |
| `--bone-deep` | `#E6E3D9` |
| `--ink` | `#161511` |
| `--ink-soft` | `#4c4a43` |
| `--red` | `#161511` |
| `--red-deep` | `#161511` |
| `--red-lift` | `#EFEDE6` |
| `--paper` | `#FFFFFF` |
| `--sans` | `"Archivo","Helvetica Neue",Helvetica,Arial,sans-serif` |
| `--mono` | `"Space Mono","Courier New",monospace` |
| `--serif` | `"Archivo","Helvetica Neue",Helvetica,Arial,sans-serif` |
| `--pad` | `clamp(1rem, 3.4vw, 3rem)` |
| `--hair` | `1.5px solid var(--ink)` |
| `--card` | `clamp(7rem,13.2vw,11.5rem)` |
| `--shelf-pad` | `clamp(1rem,3vh,2.4rem)` |
| `--shelf` | `calc(var(--card) * 1.22 + var(--shelf-pad) + var(--nav-h) + ` |
| `--nav-h` | `6.7rem` |
| `--shelf` | `calc(var(--card) * 1.1 + var(--nav-h))` |
| `--shelf` | `calc(var(--card) * 1.02 + var(--shelf-pad) + var(--nav-h) + ` |
| `--stage` | `0vh` |
| `--peek` | `0rem` |
| `--cards` | `focus-visible{background:var(--ink)` |
| `--cards` | `hover{background:var(--ink)` |
| `--cards` | `focus-visible .item__cards{opacity:1` |
| `--cards` | `hover .item__cards{opacity:1` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `` |
| `<nav>` | `menu` | `menu` |
| `<header>` | `-` | `nav nav--home` |
| `<main>` | `content` | `` |
| `<footer>` | `-` | `footer` |
