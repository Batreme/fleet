---
title: "UI & Design System: vastworld-ai"
date: 2026-11-14
target: "[[overview|vastworld-ai]]"
---

# UI Architecture & Design Tokens: vastworld-ai

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
| `--tw-leading` | `initial` |
| `--tw-font-weight` | `initial` |
| `--tw-tracking` | `initial` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `hidden lg:flex col-span-8 justify-center items-center pointer-events-auto` |
| `<nav>` | `navbarMenu` | `lg:hidden fixed inset-0 z-20 hidden-sb` |
| `<header>` | `navbar` | `fixed z-30 top-0 left-0 w-full hidden-sb font-ui` |
| `<header>` | `-` | `grid grid-cols-vast items-start gap-x-vast pt-vast-top text-left max-w-vast mx-auto px-vast` |
| `<footer>` | `-` | `pointer-events-none w-full` |
| `<footer>` | `siteFooter` | `relative w-full isolate z-7 bg-black pb-4` |
