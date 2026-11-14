---
title: "UI & Design System: www-allerstudio-com"
date: 2026-11-14
target: "[[overview|www-allerstudio-com]]"
---

# UI Architecture & Design Tokens: www-allerstudio-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--ease-out` | `cubic-bezier(.16, 1, .3, 1)` |
| `--ease-in-out` | `cubic-bezier(.37, 0, .63, 1)` |
| `--active` | `0` |
| `--font-inter` | `"Inter", "Inter Fallback"}
@font-face{font-family:Rajdhani` |
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

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `relative flex h-16 items-center justify-between rounded-full bg-dark-950 py-2 pr-2 pl-6 lg:pl-8` |
| `<header>` | `-` | `header-in fixed top-4 left-1/2 w-[954px] max-w-[calc(100%-32px)] -translate-x-1/2 lg:top-[17px] z-41` |
| `<main>` | `-` | `relative mx-2 max-w-content md:mx-4 lg:mx-auto` |
| `<footer>` | `-` | `relative z-42 overflow-hidden bg-dark-950 lg:h-[1080px]` |
