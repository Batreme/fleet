---
title: "UI & Design System: bar-topas-ch"
date: 2026-11-14
target: "[[overview|bar-topas-ch]]"
---

# UI Architecture & Design Tokens: bar-topas-ch

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--rouge` | `#B21236` |
| `--creme` | `#EFEFE3` |
| `--creme-fond` | `#EDEAE0` |
| `--jaune` | `#FEB914` |
| `--orange` | `#FE8826` |
| `--orange-rouge` | `#F03812` |
| `--bleu` | `#2C9FA2` |
| `--bordeaux` | `#7C1820` |
| `--brun` | `#60150D` |
| `--f-title` | `"Archivo", "Arial Black", system-ui, sans-serif` |
| `--f-cond` | `"Barlow Condensed", "Arial Narrow", system-ui, sans-serif` |
| `--f-text` | `"Source Sans 3", Arial, system-ui, sans-serif` |
| `--gutter` | `clamp(16px, 4vw, 56px)` |
| `--radius` | `22px` |
| `--ease` | `cubic-bezier(.2, .8, .2, 1)` |
| `--topbar-h` | `76px` |
| `--wave` | `clamp(14px, 1.6vw, 26px)` |
| `--bg` | `var(--creme)` |
| `--fg` | `var(--rouge)` |
| `--bg` | `transparent` |
| `--fg` | `currentColor` |
| `--R` | `calc(var(--wave) * 1.28)` |
| `--hole` | `9px` |
| `--step` | `26px` |
| `--topbar-h` | `68px` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<header>` | `-` | `topbar` |
| `<header>` | `-` | `s-def__head` |
| `<header>` | `-` | `s-gallery__head` |
| `<header>` | `-` | `s-amigos__head` |
| `<header>` | `-` | `s-hours__head` |
| `<header>` | `-` | `s-visit__head` |
| `<main>` | `contenu` | `` |
| `<footer>` | `-` | `s-end edge-wave` |
