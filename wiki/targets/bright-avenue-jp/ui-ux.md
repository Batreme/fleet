---
title: "UI & Design System: bright-avenue-jp"
date: 2026-11-14
target: "[[overview|bright-avenue-jp]]"
---

# UI Architecture & Design Tokens: bright-avenue-jp

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--lightningcss-light` | `initial` |
| `--lightningcss-dark` | `` |
| `--blue` | `focus-visible{box-shadow:inset 0 0 0 1px #fffc}.insulation-c` |
| `--scrollbar-width` | `15px` |
| `--bottom-offset` | `1px` |
| `--line-width` | `1px` |
| `--window-width` | `calc(100vw - var(--scrollbar-width))` |
| `--grid-outer` | `4rem` |
| `--grid-outer-sp` | `1.5rem` |
| `--grid-gap` | `4rem` |
| `--four-column-grid` | `calc( ((var(--window-width) - var(--grid-outer) * 2) - (var(` |
| `--five-column-grid` | `calc( ((var(--window-width) - var(--grid-outer) * 2) - (var(` |
| `--five-column-grid--liquid` | `calc((100% - var(--grid-gap) * 4) / 5)` |
| `--color-text` | `#333333` |
| `--color-background` | `#f6f6f6` |
| `--color-white` | `#fff` |
| `--color-beige-1` | `#D9D4D4` |
| `--color-beige-2` | `#e3d3d3` |
| `--color-beige-3` | `#afa3a3` |
| `--color-blue-1` | `#609aae` |
| `--color-gray-1` | `#ededed` |
| `--color-fb` | `#396fed` |
| `--color-x` | `#000` |
| `--color-share` | `#5f717f` |
| `--color-red` | `#e20013` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `l-header__nav sp-hidden` |
| `<nav>` | `-` | `l-header__drawer-nav` |
| `<nav>` | `-` | `l-footer__nav` |
| `<header>` | `-` | `l-header is-nav-white` |
| `<aside>` | `-` | `p-top-case__filter u-scrollBar-hidden` |
| `<main>` | `-` | `p-top` |
| `<footer>` | `-` | `l-footer` |
| `<dialog>` | `drawerMenu` | `l-header__drawer-menu js-modal-content` |
