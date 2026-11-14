---
title: "UI & Design System: jld2nd-dev"
date: 2026-11-14
target: "[[overview|jld2nd-dev]]"
---

# UI Architecture & Design Tokens: jld2nd-dev

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--base-vh` | `1vh` |
| `--base-transition` | `all .2s` |
| `--color-primary` | `#ffd64f` |
| `--color-secondary` | `#fc5778` |
| `--base-text-dark` | `#212121` |
| `--base-text-medium` | `#616161` |
| `--base-text-light` | `#9e9e9e` |
| `--base-text-info` | `#00b0f4` |
| `--base-text-success` | `#11b76b` |
| `--base-text-warning` | `#ffa100` |
| `--base-text-danger` | `#fa4362` |
| `--base-bg-info` | `#e5f3ff` |
| `--base-bg-success` | `#e6f6ed` |
| `--base-bg-warning` | `#fff2d7` |
| `--base-bg-danger` | `#ffe6ec` |
| `--base-bg-dark` | `#263238` |
| `--base-bg-light` | `#f5f6f7` |
| `--base-border-color` | `#dddedf` |
| `--base-border-radius` | `4px` |
| `--base-tooltip-bg` | `#23282d` |
| `--base-tooltip-text` | `#eaecef}html{-webkit-text-size-adjust:100%` |
| `--page-gutter` | `40px}@media (width<=991px){:root{--page-gutter:16px}}:root{-` |
| `--fs-display-xl` | `clamp(3.5rem, calc(3.4rem + .5vw), 4rem)` |
| `--fs-display-lg` | `clamp(3.125rem, 2.9018rem + 1.1161vw, 4.6875rem)` |
| `--fs-display-md` | `clamp(2.8125rem, 2.6339rem + .8929vw, 4.0625rem)` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `section-nav` | `is-in` |
| `<nav>` | `world-socials` | `` |
| `<header>` | `masthead` | `sticky` |
| `<main>` | `main-content` | `` |
| `<footer>` | `home-footer` | `home-footer` |
| `<dialog>` | `-` | `contact-modal popup hide` |
