---
title: "UI & Design System: macmillan-studio"
date: 2026-11-14
target: "[[overview|macmillan-studio]]"
---

# UI Architecture & Design Tokens: macmillan-studio

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--black` | `#000` |
| `--white` | `#fff` |
| `--lime` | `#bdff00` |
| `--light-grey` | `#d3d6da` |
| `--dark-grey` | `#818388` |
| `--layout-max-width` | `1800px` |
| `--layout-columns` | `8` |
| `--layout-margin` | `1.6rem` |
| `--layout-gutter` | `.8rem` |
| `--layout-width` | `calc(min(100vw, var(--layout-max-width)) - var(--layout-marg` |
| `--layout-column-width` | `calc(var(--layout-width)/var(--layout-columns))}@media scree` |
| `--layout-gutter` | `1.6rem}}@supports (height:1svh){:root{--vh:100svh}}@supports` |
| `--touch` | `1}}.observer-el{height:.1rem` |
| `--columns` | `1` |
| `--columns-width` | `calc((var(--columns)/var(--layout-columns))*100%)` |
| `--columns-gap-width` | `calc(var(--layout-gutter)*(1 - 1/(var(--layout-columns)/var(` |
| `--col` | `33.3333%}.grid__rule-of-thirds__col[data-v-58bd18d1]{height:` |
| `--layout-margin` | `min(3.1%,5.58rem)` |
| `--col-xs` | `2.65%` |
| `--col-s` | `10%` |
| `--col-m` | `10.65%` |
| `--col-l` | `13.35%` |
| `--layout-margin` | `min(3.1%,5.58rem)` |
| `--col-xs` | `2.65%` |
| `--col-s` | `10%` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `header__nav--main` |
| `<nav>` | `-` | `header__nav--sub` |
| `<nav>` | `-` | `footer__nav` |
| `<header>` | `-` | `header` |
| `<main>` | `-` | `__main` |
| `<footer>` | `contact-target` | `footer` |
