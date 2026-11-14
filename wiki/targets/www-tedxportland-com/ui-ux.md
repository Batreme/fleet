---
title: "UI & Design System: www-tedxportland-com"
date: 2026-11-14
target: "[[overview|www-tedxportland-com]]"
---

# UI Architecture & Design Tokens: www-tedxportland-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--tw-translate-x` | `0` |
| `--tw-translate-y` | `0` |
| `--tw-translate-z` | `0` |
| `--tw-scale-x` | `1` |
| `--tw-scale-y` | `1` |
| `--tw-scale-z` | `1` |
| `--tw-rotate-x` | `initial` |
| `--tw-rotate-y` | `initial` |
| `--tw-rotate-z` | `initial` |
| `--tw-skew-x` | `initial` |
| `--tw-skew-y` | `initial` |
| `--tw-pan-x` | `initial` |
| `--tw-pan-y` | `initial` |
| `--tw-pinch-zoom` | `initial` |
| `--tw-scroll-snap-strictness` | `proximity` |
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

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `hidden gap-6 self-stretch min-[85rem]:flex` |
| `<nav>` | `-` | `grid grid-cols-2 gap-x-6 gap-y-[clamp(0.75rem,2.6vh,1.75rem)]` |
| `<nav>` | `-` | `mt-3 flex flex-wrap gap-x-6 gap-y-2` |
| `<nav>` | `-` | `grid grid-cols-[repeat(2,max-content)] gap-x-12 gap-y-3 md:grid-cols-[repeat(3,max-content)]` |
| `<header>` | `-` | `site-header sticky top-0 z-40 bg-white/85 backdrop-blur-md` |
| `<header>` | `-` | `mb-8 md:mb-10 reveal-out` |
| `<main>` | `-` | `` |
| `<footer>` | `-` | `mt-16 rounded-t-[2rem] bg-ted-black text-white md:rounded-t-[2.5rem]` |
