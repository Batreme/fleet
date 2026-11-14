---
title: "UI & Design System: www-avilus-com"
date: 2026-11-14
target: "[[overview|www-avilus-com]]"
---

# UI Architecture & Design Tokens: www-avilus-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--w-backdrop-animation` | `initial}.w-popover-mask{opacity:0!important` |
| `--large` | `before{border-width:5px` |
| `--large` | `after{border-width:5px` |
| `--vertical` | `before,.w-widget-twitter-count-shim.w--vertical:after{conten` |
| `--vertical` | `before{border-width:5px` |
| `--vertical` | `after{border-width:4px` |
| `--_theme---background` | `var(--swatch--light-200)` |
| `--_text-style---font-family` | `var(--_typography---font--primary-family)` |
| `--_theme---text` | `var(--swatch--dark-900)` |
| `--_text-style---font-size` | `var(--_typography---font-size--text-main)` |
| `--_text-style---line-height` | `var(--_typography---line-height--huge)` |
| `--_text-style---font-weight` | `var(--_typography---font--primary-regular)` |
| `--_text-style---letter-spacing` | `var(--_typography---letter-spacing--normal)` |
| `--_text-style---text-wrap` | `pretty` |
| `--site--gutter` | `clamp(1*1rem,((1 - ((1.25 - 1)/(var(--site--viewport-max) - ` |
| `--_spacing---space--8` | `clamp(2.5*1rem,((2.5 - ((4 - 2.5)/(var(--site--viewport-max)` |
| `--radius--main` | `.5rem` |
| `--_theme---background-2` | `var(--swatch--light-100)` |
| `--site--column-count` | `12` |
| `--site--column-width` | `calc((min(var(--max-width--main),100% - var(--site--margin)*` |
| `--_responsive---large` | `1` |
| `--_responsive---medium` | `0` |
| `--_responsive---small` | `0` |
| `--_responsive---xsmall` | `0` |
| `--_spacing---space--6` | `clamp(2*1rem,((2 - ((2.5 - 2)/(var(--site--viewport-max) - v` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `nav_links_component w-variant-23049969-09ac-2789-520b-3c6ae895bbc6` |
| `<nav>` | `w-dropdown-list-0` | `dropdown_list w-variant-23049969-09ac-2789-520b-3c6ae895bbc6 w-dropdown-list` |
| `<nav>` | `-` | `nav_links_component` |
| `<nav>` | `w-dropdown-list-1` | `dropdown_list w-dropdown-list` |
| `<header>` | `-` | `nav_desktop_wrap` |
| `<main>` | `main` | `page_main` |
| `<footer>` | `-` | `footer_inner` |
