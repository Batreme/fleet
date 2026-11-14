---
title: "UI & Design System: www-huxleysaga-com"
date: 2026-11-14
target: "[[overview|www-huxleysaga-com]]"
---

# UI Architecture & Design Tokens: www-huxleysaga-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--white` | `#fff}:root .--white{color:#fff}:root{--white-0:hsla(0,0%,100` |
| `--layout-columns-count` | `4` |
| `--layout-columns-gap` | `12px` |
| `--layout-margin` | `12px` |
| `--layout-width` | `calc(100vw - var(--layout-margin)*2)` |
| `--layout-column-width` | `calc((var(--layout-width) - ((var(--layout-columns-count) - ` |
| `--layout-columns-gap` | `12px` |
| `--layout-margin` | `12px}}.layout-block,.layout-grid{margin-left:auto` |
| `--theme-bg` | `#fff` |
| `--theme-fg` | `#000` |
| `--theme-contrast` | `red}:root .theme-dark{--theme-bg:#000` |
| `--theme-fg` | `#fff` |
| `--theme-contrast` | `red}:root{--spacer-4:4px` |
| `--spacer-8` | `8px` |
| `--spacer-16` | `16px` |
| `--spacer-32` | `32px` |
| `--spacer-64` | `64px}html{overflow-x:hidden` |
| `--tp-base-background-color` | `rgba(26,26,26,.9)` |
| `--tp-base-shadow-color` | `rgba(0,0,0,.2)` |
| `--tp-button-background-color` | `#ccc` |
| `--tp-button-background-color-active` | `#fff` |
| `--tp-button-background-color-focus` | `#f2f2f2` |
| `--tp-button-background-color-hover` | `#d9d9d9` |
| `--tp-button-foreground-color` | `rgba(0,0,0,.8)` |
| `--tp-container-background-color` | `rgba(0,0,0,.3)` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `o-nav` |
| `<header>` | `-` | `e-nav` |
| `<main>` | `-` | `page-index layout-block` |
| `<footer>` | `-` | `e-footer layout-block` |
