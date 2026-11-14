---
title: "UI & Design System: becore-se"
date: 2026-11-14
target: "[[overview|becore-se]]"
---

# UI Architecture & Design Tokens: becore-se

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--unbranded` | `hover:not([disabled]){background-color:#136f99}.shopify-paym` |
| `--border-color` | `var(--text-color) / .6}.accordion{--accordion-block-padding:` |
| `--accordion-inline-padding` | `0` |
| `--accordion-block-padding` | `1.25rem}.accordion--large{--accordion-block-padding: 1.65rem` |
| `--accordion-inline-padding` | `1.75rem}}.big-link{align-items:center` |
| `--opacity` | `hover~.big-link--opacity>*{opacity:.3}.big-link--opacity:has` |
| `--colors` | `hover>*{transform:translate(1.75rem)}.big-link--colors:hover` |
| `--button-padding-block` | `.75rem` |
| `--button-padding-inline` | `1.5rem` |
| `--button-background` | `var(--button-background-primary)` |
| `--button-text-color` | `var(--button-text-primary)` |
| `--button-border-color` | `0 0 0 / 0` |
| `--button-padding-inline` | `1.5rem` |
| `--button-padding-block` | `.625rem` |
| `--button-padding-inline` | `1.25rem` |
| `--button-padding-block` | `.875rem` |
| `--button-padding-inline` | `2.5rem}}@media screen and (pointer:fine){.button__content[ro` |
| `--glowing-shape-width` | `min(40px, 60%)` |
| `--unbranded` | `hover:not([disabled]){background-color:rgb(var(--button-back` |
| `--shopify-accelerated-checkout-button-block-size` | `44px` |
| `--shopify-accelerated-checkout-button-border-radius` | `var(--button-border-radius)` |
| `--shopify-accelerated-checkout-button-box-shadow` | `none}.circle-button{--button-size: 1.75rem` |
| `--button-size` | `2.5rem}.circle-button--blurred{-webkit-backdrop-filter:blur(` |
| `--blurred` | `before{opacity:.6}@media screen and (min-width:1000px){.circ` |
| `--content-box-spacing` | `max(1.5rem, var(--container-gutter))` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `mode-tabs mode-tabs-sections--27158676930896__announcement-bar` |
| `<nav>` | `-` | `header__primary-nav md:justify-center` |
| `<nav>` | `-` | `header__secondary-nav` |
| `<header>` | `-` | `` |
| `<header>` | `-` | `` |
| `<header>` | `-` | `` |
| `<header>` | `shopify-section-sections--27158676930896__header` | `shopify-section shopify-section-group-header-group shopify-section--header` |
| `<aside>` | `shopify-section-sections--27158676930896__announcement-bar` | `shopify-section shopify-section-group-header-group shopify-section--announcement-bar` |
| `<main>` | `main` | `anchor` |
| `<footer>` | `-` | `` |
| `<footer>` | `shopify-section-sections--27158676898128__footer` | `shopify-section shopify-section-group-footer-group shopify-section--footer` |
