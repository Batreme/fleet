---
title: "UI & Design System: morrow-valerian-studio"
date: 2026-11-14
target: "[[overview|morrow-valerian-studio]]"
---

# UI Architecture & Design Tokens: morrow-valerian-studio

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--font-pp-neue-montreal` | `"ppNeueMontreal", "ppNeueMontreal Fallback"}
@font-face{font` |
| `--font-editorial-new` | `"editorialNew", "editorialNew Fallback"}
.shipping-banner-an` |
| `--tw-translate-x` | `0` |
| `--tw-translate-y` | `0` |
| `--tw-translate-z` | `0` |
| `--tw-rotate-x` | `initial` |
| `--tw-rotate-y` | `initial` |
| `--tw-rotate-z` | `initial` |
| `--tw-skew-x` | `initial` |
| `--tw-skew-y` | `initial` |
| `--tw-space-y-reverse` | `0` |
| `--tw-border-style` | `solid` |
| `--tw-gradient-position` | `initial` |
| `--tw-gradient-from` | `#0000` |
| `--tw-gradient-via` | `#0000` |
| `--tw-gradient-to` | `#0000` |
| `--tw-gradient-stops` | `initial` |
| `--tw-gradient-via-stops` | `initial` |
| `--tw-gradient-from-position` | `0%` |
| `--tw-gradient-via-position` | `50%` |
| `--tw-gradient-to-position` | `100%` |
| `--tw-leading` | `initial` |
| `--tw-font-weight` | `initial` |
| `--tw-tracking` | `initial` |
| `--tw-ordinal` | `initial` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `site-nav-toolbar grid grid-cols-[1fr_auto_1fr] items-center gap-x-gutter px-page lg:grid-cols-12 lg:` |
| `<nav>` | `-` | `site-mobile-menu-content px-page` |
| `<nav>` | `-` | `col-span-4 min-w-0 self-start lg:row-start-1 lg:col-span-2 lg:col-start-7` |
| `<nav>` | `-` | `col-span-4 min-w-0 self-start lg:row-start-1 lg:col-span-2 lg:col-start-9` |
| `<nav>` | `-` | `col-span-4 min-w-0 self-start lg:row-start-1 lg:col-span-2 lg:col-start-11` |
| `<nav>` | `-` | `col-span-12 lg:col-span-10` |
| `<header>` | `-` | `site-nav col-start-1 row-start-1` |
| `<header>` | `-` | `cart-header` |
| `<aside>` | `-` | `relative z-20 overflow-hidden border-y border-neutral-200 bg-white font-sans text-body text-neutral-` |
| `<main>` | `-` | `relative z-10 bg-white` |
| `<footer>` | `-` | `relative z-0 flex min-h-[40svh] flex-col px-page font-sans text-body lg:px-page-lg bg-[#030d07] text` |
| `<dialog>` | `_R_2lflb_` | `site-mobile-menu` |
| `<dialog>` | `morrow-cart` | `cart-dialog` |
