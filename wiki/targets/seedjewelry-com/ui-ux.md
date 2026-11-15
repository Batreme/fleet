---
title: "UI & Design System: seedjewelry-com"
date: 2026-11-15
target: "seedjewelry-com"
---

# UI Architecture & Design Tokens: seedjewelry-com

> Ground-truth CSS custom properties and DOM layout primitives extracted from `seedjewelry-com` (`Seed Jewelry · Lab-Grown Diamond High Jewelry Atelier, Dubai`). All values are sanitized, deduplicated, and mapped to their semantic UI roles. Also see [UI Prompt Blueprint](prompt-blueprint.md).

## 🎨 Design Tokens (CSS Variables)

| Token Name | Extracted Value | Semantic UI Role |
|---|---|---|
| `--container-lg-max-width` | `90rem` | 1440px primary desktop container width |
| `--container-xl-max-width` | `1920px` | Full-bleed widescreen showcase max-width |
| `--container-md-max-width` | `71.875rem` | 1150px medium editorial container width |
| `--container-gutter` | `1.25rem` | 20px horizontal container gutter |
| `--section-vertical-spacing` | `2.5rem` | 40px vertical section rhythm |
| `--section-stack-gap` | `2.25rem` | 36px internal stack gap |
| `--header-grid` | `"primary-nav logo secondary-nav" / minmax(0, 1fr) auto minmax(0, 1fr)` | Tri-zone CSS Grid template for sticky header |
| `--header-logo-width` | `70px` | Centered Seed Jewelry emblem width |
| `--seed-grid-cols` | `4` | 4-column desktop jewelry product grid |
| `--seed-grid-cols-mobile` | `2` | 2-column mobile jewelry product grid |
| `--seed-cta-bg` | `#e8d3a8` | Warm champagne gold primary CTA background |
| `--seed-cta-color` | `#000000` | Black text ink on champagne gold CTA |
| `--accent` | `48 79 72` | Botanical emerald RGB triplet (#304f48) |
| `--button-background` | `48 79 72` | Emerald button background RGB triplet |
| `--border-color` | `217 217 217` | 1px neutral border RGB triplet (#d9d9d9) |
| `--heading-font-family` | `"Plus Jakarta Sans", sans-serif` | Primary geometric heading font family |
| `--text-font-family` | `Poppins, sans-serif` | Primary body copy font family |
| `--button-border-radius` | `3.125rem` | 50px pill radius for primary buttons |
| `--drawer-max-width` | `min(94vw, 30rem)` | Slide-over cart & filter drawer width (480px) |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<header>` | `-` | `-` |
| `<header>` | `shopify-section-sections--24564126580933__header` | `shopify-section shopify-section-group-header-group shopify-s` |
| `<header>` | `-` | `seed-product-grid__header` |
| `<nav>` | `-` | `header__primary-nav` |
| `<nav>` | `-` | `header__secondary-nav` |
| `<nav>` | `-` | `seed-footer__nav seed-footer__nav--shop` |
| `<nav>` | `-` | `seed-footer__nav seed-footer__nav--about` |
| `<nav>` | `-` | `seed-footer__nav seed-footer__nav--contact` |
| `<main>` | `main` | `anchor` |
| `<section>` | `shopify-pc__banner` | `shopify-pc__banner__dialog` |
| `<section>` | `shopify-section-sections--24564127596741__cart-drawer` | `shopify-section shopify-section-group-overlay-group shopify-` |
| `<section>` | `shopify-section-template--24564131987653__hero` | `shopify-section seed-hero-section` |
| `<section>` | `-` | `seed-hero` |
| `<section>` | `shopify-section-template--24564131987653__seed_best_sellers_kJKTM6` | `shopify-section seed-product-grid-section` |
