---
title: "UI & Design System: ksenpanchenko-com"
date: 2026-11-14
target: "[[overview|ksenpanchenko-com]]"
---

# UI Architecture & Design Tokens: ksenpanchenko-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--ar` | `332/420}.wrow__img--6{grid-column:span 6` |
| `--ar` | `680/420}.wrow__img--9{grid-column:span 9` |
| `--ar` | `1028/420}.wrow__img img{width:100%` |
| `--q` | `clamp(0,calc((var(--p, 1) - var(--s)) / .45),1)` |
| `--n` | `4` |
| `--notch` | `11deg` |
| `--R` | `62vw` |
| `--step` | `30vh` |
| `--stage` | `min(560px,70vh)` |
| `--T` | `calc((100vh - var(--stage)) / 2 + 24px)` |
| `--range` | `cover calc(100vh - var(--T)) cover calc(100vh - var(--T) + (` |
| `--c4` | `calc((100% - 8 * var(--layout-grid-gutter)) / 9 * 3 + 3 * va` |
| `--color-text-primary` | `#f1f0ec` |
| `--color-text-secondary` | `rgb(241 240 236/.68)` |
| `--color-text-tertiary` | `rgb(241 240 236/.56)` |
| `--color-border-subtle` | `rgb(241 240 236/.16)` |
| `--color-text-accent` | `#ff6a3d` |
| `--color-text-accent-strong` | `#ff7a52` |
| `--color-bg-tag` | `rgb(241 240 236/.1)` |
| `--band-bg` | `#141413` |
| `--color-text-primary` | `#141414` |
| `--color-text-secondary` | `rgb(20 20 20/.7)` |
| `--color-text-tertiary` | `rgb(20 20 20/.62)` |
| `--color-border-subtle` | `rgb(20 20 20/.14)` |
| `--color-text-accent` | `#e8501f` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `nav__links` |
| `<header>` | `-` | `nav` |
| `<main>` | `main` | `` |
| `<footer>` | `-` | `footer` |
