---
title: "UI & Design System: findra-art"
date: 2026-11-14
target: "[[overview|findra-art]]"
---

# UI Architecture & Design Tokens: findra-art

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--font-geist` | `"Geist", "Geist Fallback"}
@font-face{font-family:Anton` |
| `--font-anton` | `"Anton", "Anton Fallback"}
@font-face{font-family:Permanent ` |
| `--font-permanent-marker` | `"Permanent Marker", "Permanent Marker Fallback"}
@layer prop` |
| `--tw-rotate-y` | `initial` |
| `--tw-rotate-z` | `initial` |
| `--tw-skew-x` | `initial` |
| `--tw-skew-y` | `initial` |
| `--tw-scroll-snap-strictness` | `proximity` |
| `--tw-space-x-reverse` | `0` |
| `--tw-divide-y-reverse` | `0` |
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
| `--tw-slashed-zero` | `initial` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `` |
| `<nav>` | `-` | `-mx-3` |
| `<header>` | `-` | `bg-background/70 sticky top-0 z-30 backdrop-blur-xl backdrop-saturate-150` |
| `<main>` | `main` | `mx-auto flex w-full max-w-[100rem] flex-col gap-12 px-4 pt-8 sm:gap-16 sm:px-6 sm:pt-14` |
| `<footer>` | `-` | `text-muted mx-auto flex w-full max-w-[100rem] flex-col gap-4 px-4 py-12 text-sm sm:flex-row sm:items` |
