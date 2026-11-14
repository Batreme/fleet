---
title: "UI & Design System: emmaus-agir-31-fr"
date: 2026-11-14
target: "[[overview|emmaus-agir-31-fr]]"
---

# UI Architecture & Design Tokens: emmaus-agir-31-fr

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--fond` | `#f1ece1` |
| `--fond-2` | `#e7e1d3` |
| `--gris` | `#1b1b1b` |
| `--gris-doux` | `#5f5d57` |
| `--ligne` | `rgba(27,27,27,0.18)` |
| `--jaune` | `#ebc017` |
| `--bleu` | `#33669b` |
| `--vert` | `#43744e` |
| `--ink` | `var(--gris)` |
| `--gutter` | `max(clamp(20px,4vw,64px),env(safe-area-inset-left,0px),env(s` |
| `--header-h` | `clamp(56px,8vw,88px)` |
| `--radius-pill` | `999px` |
| `--tap` | `44px` |
| `--z-flower` | `2` |
| `--z-guide` | `3` |
| `--z-scene` | `4` |
| `--z-scene-raised` | `5` |
| `--z-scene-top` | `6` |
| `--z-menu` | `55` |
| `--z-header` | `60` |
| `--z-paper` | `90` |
| `--z-loader` | `100` |
| `--z-cursor` | `200` |
| `--z-skip` | `1000` |
| `--ease-out` | `cubic-bezier(0.16,1,0.3,1)` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `menu` | `menu` |
| `<nav>` | `-` | `footer__legal` |
| `<nav>` | `-` | `footer__social` |
| `<header>` | `-` | `header` |
| `<header>` | `-` | `activites__header` |
| `<header>` | `-` | `carte__header wrap` |
| `<header>` | `-` | `boutiques__header` |
| `<main>` | `contenu` | `` |
| `<footer>` | `-` | `footer` |
