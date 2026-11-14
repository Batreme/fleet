---
title: "UI & Design System: www-feelreformed-com"
date: 2026-11-14
target: "[[overview|www-feelreformed-com]]"
---

# UI Architecture & Design Tokens: www-feelreformed-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--hover-lift-amount` | `4px` |
| `--hover-scale-amount` | `1` |
| `--hover-subtle-zoom-amount` | `1.015` |
| `--hover-shadow-color` | `var(--color-shadow)` |
| `--hover-transition-duration` | `.25s` |
| `--hover-transition-timing` | `ease-out}html{scrollbar-width:thin` |
| `--cursor` | `pointer}.predictive-search-results__card .product-card,.pred` |
| `--backdrop-color-rgb` | `var(--color-shadow-rgb)` |
| `--page-margin` | `16px}@media screen and (min-width:750px){.page-width-wide,.p` |
| `--page-width` | `calc(var(--page-content-width) + (var(--page-margin) * 2))}.` |
| `--page-width` | `calc(var(--page-content-width) + (var(--page-margin) * 2))}.` |
| `--page-width` | `calc(var(--page-content-width) + (var(--page-margin) * 2))}.` |
| `--page-width` | `calc(var(--page-content-width) + (var(--page-margin) * 2))}.` |
| `--full-page-grid-margin` | `minmax(var(--page-margin), 1fr)` |
| `--full-page-grid-with-margins` | `var(--full-page-grid-margin) var(--full-page-grid-central-co` |
| `--util-page-margin-offset` | `max( var(--page-margin), calc((100% - min(var(--page-content` |
| `--full-page-margin-inline-offset` | `calc(((min(100vw, 100%) - var(--full-page-grid-central-colum` |
| `--section-min-height` | `var(--section-height-small)}.section--height-medium{--sectio` |
| `--centered-column-number` | `12` |
| `--full-width-column-number` | `14` |
| `--centered` | `column-1 / span var(--centered-column-number)` |
| `--full-width` | `column-0 / span var(--full-width-column-number)` |
| `--text-align` | `left` |
| `--text-align` | `center` |
| `--text-align` | `right` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `menu-drawer__navigation` |
| `<nav>` | `-` | `` |
| `<header>` | `shopify-section-sections--27422728290681__header_section` | `shopify-section shopify-section-group-header-group header-section` |
| `<header>` | `-` | `drawer__head` |
| `<aside>` | `-` | `announcement-bar spacing-style section section--page-width color-scheme-4` |
| `<main>` | `MainContent` | `content-for-layout` |
| `<footer>` | `shopify-section-sections--27422728257913__footer` | `shopify-section shopify-section-group-footer-group section-wrapper` |
| `<dialog>` | `-` | `cart-drawer__dialog dialog-modal dialog-drawer color-scheme-1 cart-drawer--empty` |
| `<dialog>` | `-` | `search-modal__content dialog-modal` |
