---
title: "UI & Design System: www-governorsmansion-org"
date: 2026-11-14
target: "[[overview|www-governorsmansion-org]]"
---

# UI Architecture & Design Tokens: www-governorsmansion-org

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--large` | `before{border-width:5px` |
| `--large` | `after{border-width:5px` |
| `--vertical` | `before,.w-widget-twitter-count-shim.w--vertical:after{conten` |
| `--vertical` | `before{border-width:5px` |
| `--vertical` | `after{border-width:4px` |
| `--_theme---background` | `var(--swatch--light-100)` |
| `--_text-style---font-family` | `var(--_typography---font--secondary-family)` |
| `--_theme---text` | `var(--swatch--dark-900)` |
| `--_text-style---font-size` | `var(--_typography---font-size--text-main)` |
| `--_text-style---line-height` | `var(--_typography---line-height--huge)` |
| `--_text-style---font-weight` | `var(--_typography---font--secondary-book)` |
| `--_text-style---letter-spacing` | `var(--_typography---letter-spacing--normal)` |
| `--site--gutter` | `clamp(1*1rem,((1 - ((1 - 1)/(var(--site--viewport-max) - var` |
| `--_spacing---space--8` | `clamp(2.5*1rem,((2.5 - ((4 - 2.5)/(var(--site--viewport-max)` |
| `--radius--main` | `1rem` |
| `--_theme---background-2` | `var(--_brand---color-200)` |
| `--site--column-count` | `12` |
| `--site--column-width` | `calc((min(var(--max-width--main),100% - var(--site--margin)*` |
| `--_responsive---large` | `1` |
| `--_responsive---medium` | `0` |
| `--_responsive---small` | `0` |
| `--_responsive---xsmall` | `0` |
| `--_spacing---space--6` | `clamp(2*1rem,((2 - ((2.5 - 2)/(var(--site--viewport-max) - v` |
| `--_spacing---section-space--main` | `clamp(4*1rem,((4 - ((7 - 4)/(var(--site--viewport-max) - var` |
| `--_spacing---space--5` | `clamp(1.75*1rem,((1.75 - ((2 - 1.75)/(var(--site--viewport-m` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `nav_links_component w-variant-23049969-09ac-2789-520b-3c6ae895bbc6` |
| `<nav>` | `-` | `nav_mobile_menu_wrap w-nav-menu` |
| `<nav>` | `-` | `nav_links_component` |
| `<header>` | `-` | `nav_desktop_wrap` |
| `<header>` | `-` | `tour_wrap` |
| `<main>` | `main` | `page_main` |
| `<footer>` | `-` | `footer_wrap u-theme-dark` |
