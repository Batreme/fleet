---
title: "UI & Design System: www-sharplink-com"
date: 2026-11-14
target: "[[overview|www-sharplink-com]]"
---

# UI Architecture & Design Tokens: www-sharplink-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--layout-columns-count` | `4` |
| `--layout-columns-gap` | `16px` |
| `--layout-rows-gap` | `8px` |
| `--layout-margin` | `16px` |
| `--layout-width` | `calc(100vw - var(--layout-margin)*2)` |
| `--layout-column-width` | `calc((var(--layout-width) - ((var(--layout-columns-count) - ` |
| `--layout-columns-gap` | `28px` |
| `--layout-rows-gap` | `8px` |
| `--layout-margin` | `28px}}@media(min-width:1920px){[data-v-747d5bb3]:root{--layo` |
| `--pin-color` | `var(--brand-blue-primary)}.has-pin.has-pin__dark[data-v-747d` |
| `--pin-color` | `var(--brand-blue-primary)}.has-pin--top-left.has-pin__dark[d` |
| `--pin-color` | `var(--brand-blue-primary)}.has-pin--top-right.has-pin__dark[` |
| `--pin-color` | `var(--brand-blue-primary)}.has-pin--bottom-right.has-pin__da` |
| `--pin-color` | `var(--brand-blue-primary)}.has-pin--bottom-left.has-pin__dar` |
| `--layout-columns-count` | `4` |
| `--layout-columns-gap` | `16px` |
| `--layout-rows-gap` | `8px` |
| `--layout-margin` | `16px` |
| `--layout-width` | `calc(100vw - var(--layout-margin)*2)` |
| `--layout-column-width` | `calc((var(--layout-width) - ((var(--layout-columns-count) - ` |
| `--layout-columns-gap` | `28px` |
| `--layout-rows-gap` | `8px` |
| `--layout-margin` | `28px}}@media(min-width:1920px){[data-v-9ac96042]:root{--layo` |
| `--pin-color` | `var(--brand-blue-primary)}.has-pin.has-pin__dark[data-v-9ac9` |
| `--pin-color` | `var(--brand-blue-primary)}.has-pin--top-left.has-pin__dark[d` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `layout-flex navbar` |
| `<header>` | `-` | `site-header theme-dark` |
| `<main>` | `-` | `no-js-screen` |
| `<main>` | `-` | `page-index` |
| `<footer>` | `-` | `site-footer` |
