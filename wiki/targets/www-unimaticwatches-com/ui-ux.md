---
title: "UI & Design System: www-unimaticwatches-com"
date: 2026-11-15
target: "[[overview|www-unimaticwatches-com]]"
---

# UI Architecture & Design Tokens: www-unimaticwatches-com

> Ground-truth CSS custom properties and DOM layout primitives extracted from `www-unimaticwatches-com` (`UNIMATIC Watches · Italian Minimalist Tool Watch Lab`). All values are sanitized, deduplicated, and mapped to their semantic UI roles. Also see [[prompt-blueprint|UI Prompt Blueprint]].

## 🎨 Design Tokens (CSS Variables)

| Token Name | Extracted Value | Semantic UI Role |
|---|---|---|
| `--color-bg` | `#F6F6F6` | Primary laboratory light gray background |
| `--color-surface-page` | `#F6F6F6` | Page wrapper background surface |
| `--color-ink` | `#000000` | Primary pure black typography & icon ink |
| `--color-accent` | `#AFFF00` | High-visibility Super-LumiNova volt-lime accent |
| `--color-media` | `#D9D9D9` | Neutral gray backdrop for studio watch photography |
| `--color-white` | `#ffffff` | Pure white highlight surface |
| `--color-ink-70` | `color-mix(in srgb, var(--color-ink) 70%, transparent)` | Secondary body copy ink (70% black) |
| `--color-ink-50` | `color-mix(in srgb, var(--color-ink) 50%, transparent)` | Muted specification label ink (50% black) |
| `--color-ink-30` | `color-mix(in srgb, var(--color-ink) 30%, transparent)` | Disabled / inactive slider control ink |
| `--color-hairline` | `color-mix(in srgb, var(--color-ink) 15%, transparent)` | 1px structural grid hairline rule |
| `--color-border` | `color-mix(in srgb, var(--color-ink) 20%, transparent)` | Interactive button & input border |
| `--color-surface` | `color-mix(in srgb, var(--color-ink) 5%, transparent)` | Subtle elevated spec table surface |
| `--color-scrim` | `color-mix(in srgb, var(--color-ink) 60%, transparent)` | Modal & drawer backdrop scrim |
| `--color-glass-base` | `#FFFFFF` | Base color for frosted navigation pills |
| `--color-glass-80` | `color-mix(in srgb, var(--color-glass-base) 80%, transparent)` | 80% translucent frosted pill background |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<header>` | `shopify-section-sections--30951437533514__header` | `shopify-section shopify-section-group-header-group header-se` |
| `<nav>` | `-` | `header__nav nav-pill` |
| `<nav>` | `-` | `header__actions nav-pill nav-pill--sm` |
| `<nav>` | `-` | `header__mobile` |
| `<nav>` | `-` | `footer-column__links t-body` |
| `<nav>` | `-` | `footer-utilities__widget footer-utilities__legal t-eyebrow` |
| `<main>` | `MainContent` | `main` |
| `<section>` | `shopify-pc__banner` | `shopify-pc__banner__dialog` |
| `<section>` | `shopify-section-template--30951437730122__hero_XxHWhT` | `shopify-section hero` |
| `<section>` | `shopify-section-template--30951437730122__bestseller` | `shopify-section product-carousel-section` |
| `<section>` | `shopify-section-template--30951437730122__editorial` | `shopify-section editorial` |
| `<section>` | `shopify-section-template--30951437730122__product-row` | `shopify-section prodrow-section` |
| `<footer>` | `shopify-section-sections--30951437500746__footer` | `shopify-section shopify-section-group-footer-group footer` |
