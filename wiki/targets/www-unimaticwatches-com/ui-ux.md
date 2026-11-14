---
title: "UI & Design System: www-unimaticwatches-com"
date: 2026-11-14
target: "[[overview|www-unimaticwatches-com]]"
---

# UI Architecture & Design Tokens: www-unimaticwatches-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--space-1` | `.4rem` |
| `--space-2` | `.8rem` |
| `--space-2-5` | `1rem` |
| `--space-3` | `1.2rem` |
| `--space-4` | `1.6rem` |
| `--space-5` | `2.4rem` |
| `--space-6` | `3.2rem` |
| `--color-tag-ink` | `#222` |
| `--editorial-sticky-top` | `6.4rem` |
| `--drawer-top-base` | `calc(var(--space-4) + var(--space-2-5) * 2 + 1.6rem + var(--` |
| `--drawer-top` | `var(--drawer-top-base)` |
| `--drawer-width` | `33rem` |
| `--sticky-top` | `calc(var(--drawer-top-base) + var(--space-6))}.container{wid` |
| `--padding-block-start` | `0px` |
| `--padding-block-end` | `0px` |
| `--slider-gap` | `var(--space-3)` |
| `--card-basis` | `var(--col)` |
| `--slider-gap` | `var(--gutter)}}.slider__track::-webkit-scrollbar{display:non` |
| `--drawer-top` | `calc(max(env(safe-area-inset-top), 6.4rem) + 4rem) }}@media(` |
| `--coin-image` | `url(https://cdn.shopify.com/shop-assets/static_uploads/shop-` |
| `--coin-image-checked` | `url(https://cdn.shopify.com/shop-assets/static_uploads/shop-` |
| `--x-opacity-disabled` | `1}[dir=ltr] .yY3sV [type=checkbox]{left:-.14285714285714285e` |
| `--unbranded` | `hover:not([disabled]){background-color:#136f99}.shopify-paym` |
| `--i6e6fx0` | `calc((var(--x-typography-size-default) * 40) / 14)` |
| `--i6e6fx1` | `calc((var(--x-typography-size-default) * 24) / 14)` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `header__nav nav-pill` |
| `<nav>` | `-` | `header__actions nav-pill nav-pill--sm` |
| `<nav>` | `-` | `header__mobile` |
| `<nav>` | `-` | `footer-column__links t-body` |
| `<nav>` | `-` | `footer-column__links t-body` |
| `<nav>` | `-` | `footer-column__links t-body` |
| `<nav>` | `-` | `footer-column__links t-body` |
| `<nav>` | `-` | `footer-utilities__widget footer-utilities__legal t-eyebrow` |
| `<header>` | `shopify-section-sections--30951437533514__header` | `shopify-section shopify-section-group-header-group header-section` |
| `<main>` | `MainContent` | `main` |
| `<footer>` | `shopify-section-sections--30951437500746__footer` | `shopify-section shopify-section-group-footer-group footer` |
| `<dialog>` | `-` | `header__drawer` |
| `<dialog>` | `-` | `drawer cart-drawer` |
