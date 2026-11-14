---
title: "UI & Design System: diseinuz-com"
date: 2026-11-14
target: "[[overview|diseinuz-com]]"
---

# UI Architecture & Design Tokens: diseinuz-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--grid-gutter` | `.75rem` |
| `--grid-margin` | `.75rem` |
| `--grid-margin-negative` | `-.75rem` |
| `--grid-columns` | `12` |
| `--grid-one-column` | `calc(((100vw - 2 * var(--grid-margin) - ((var(--grid-columns` |
| `--menu-width` | `calc(var(--grid-one-column) * calc(var(--grid-columns) / 4) ` |
| `--color-black` | `0, 0, 0` |
| `--color-white` | `255, 255, 255` |
| `--title-letter-spacing` | `-.07em` |
| `--easing-handle-01` | `cubic-bezier(.48, .1, 0, 1)` |
| `--easing-handle-02` | `cubic-bezier(.01, .8, .5, 1)` |
| `--filter-blur` | `blur(5rem)` |
| `--context` | `1440` |
| `--gradient` | `#830100 0%, #ff2e01 20%, #ffd702 40%, #7fff81 60%, #04d3ff 8` |
| `--gradient-loop` | `#830100 0%, #ff2e01 8.333%, #ffd702 16.667%, #7fff81 25%, #0` |
| `--quarter` | `3.25rem}@media (width<=1180px) and (width>=681px){:root{--gr` |
| `--context` | `820` |
| `--menu-width` | `calc(var(--grid-one-column) * calc(var(--grid-columns) / 3) ` |
| `--context` | `402` |
| `--menu-width` | `calc(var(--grid-one-column) * var(--grid-columns))}}html.len` |
| `--scrollbar` | `:-webkit-scrollbar{display:none}.flex{display:flex}.flex--co` |
| `--white` | `hover{border-color:rgb(var(--color-black))` |
| `--black` | `hover{border-color:rgb(var(--color-white))` |
| `--ghost-white` | `hover{border-color:rgb(var(--color-white))` |
| `--ghost-black` | `hover{border-color:rgb(var(--color-black))` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `footer__end__legal` |
| `<header>` | `-` | `header top` |
| `<main>` | `-` | `page__container` |
| `<footer>` | `-` | `page__footer` |
