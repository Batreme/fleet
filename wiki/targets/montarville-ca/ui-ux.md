---
title: "UI & Design System: montarville-ca"
date: 2026-11-14
target: "[[overview|montarville-ca]]"
---

# UI Architecture & Design Tokens: montarville-ca

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--fa-animation-direction` | `reverse}.fa-pulse,.fa-spin-pulse{-webkit-animation-name:fa-s` |
| `--fa-style-family-brands` | `"Font Awesome 6 Brands"` |
| `--fa-font-brands` | `normal 400 1em/1 "Font Awesome 6 Brands"}@font-face{font-fam` |
| `--fa-font-regular` | `normal 400 1em/1 "Font Awesome 6 Free"}@font-face{font-famil` |
| `--fa-style-family-classic` | `"Font Awesome 6 Free"` |
| `--fa-font-solid` | `normal 900 1em/1 "Font Awesome 6 Free"}@font-face{font-famil` |
| `--grid-col-width` | `calc((100vw - (var(--grid-margin) * 2) - (var(--grid-gutter)` |
| `--success` | `before{content:""}.c-icon.--success-after:before{content:no` |
| `--plus` | `before{content:""}.c-icon.--plus-after:before{content:none}` |
| `--play` | `before{content:""}.c-icon.--play-after:before{content:none}` |
| `--minus` | `before{content:""}.c-icon.--minus-after:before{content:none` |
| `--map` | `before{content:""}.c-icon.--map-after:before{content:none}.` |
| `--error` | `before{content:""}.c-icon.--error-after:before{content:none` |
| `--copyright` | `before{content:""}.c-icon.--copyright-after:before{content:` |
| `--close` | `before{content:""}.c-icon.--close-after:before{content:none` |
| `--chevron-top` | `before{content:""}.c-icon.--chevron-top-after:before{conten` |
| `--chevron-right` | `before{content:""}.c-icon.--chevron-right-after:before{cont` |
| `--chevron-left` | `before{content:""}.c-icon.--chevron-left-after:before{conte` |
| `--chevron-down` | `before{content:""}.c-icon.--chevron-down-after:before{conte` |
| `--arrow-right` | `before{content:""}.c-icon.--arrow-right-after:before{conten` |
| `--arrow-left` | `before{content:""}.c-icon.--arrow-left-after:before{content` |
| `--arrow-down` | `before{content:""}.c-icon.--arrow-down-after:before{content` |
| `--arrow-bottom-right` | `before{content:""}.c-icon.--arrow-bottom-right-after:before` |
| `--font-size-h1` | `calc(128 / var(--base-px, 18) * 1rem)` |
| `--font-size-h2-xl` | `calc(96 / var(--base-px, 18) * 1rem)` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `c-header__main-navigation` |
| `<nav>` | `-` | `c-header__second-navigation` |
| `<nav>` | `-` | `c-screen-menu__navigation` |
| `<nav>` | `-` | `c-footer__menus` |
| `<header>` | `-` | `c-header --at-top` |
| `<main>` | `-` | `c-main` |
| `<footer>` | `-` | `c-footer` |
