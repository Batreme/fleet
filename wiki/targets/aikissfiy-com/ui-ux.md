---
title: "UI & Design System: aikissfiy-com"
date: 2026-11-14
target: "[[overview|aikissfiy-com]]"
---

# UI Architecture & Design Tokens: aikissfiy-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--tw-border-spacing-x` | `0` |
| `--tw-border-spacing-y` | `0` |
| `--tw-translate-x` | `0` |
| `--tw-translate-y` | `0` |
| `--tw-rotate` | `0` |
| `--tw-skew-x` | `0` |
| `--tw-skew-y` | `0` |
| `--tw-scale-x` | `1` |
| `--tw-scale-y` | `1` |
| `--tw-pan-x` | `` |
| `--tw-pan-y` | `` |
| `--tw-pinch-zoom` | `` |
| `--tw-scroll-snap-strictness` | `proximity` |
| `--tw-gradient-from-position` | `` |
| `--tw-gradient-via-position` | `` |
| `--tw-gradient-to-position` | `` |
| `--tw-ordinal` | `` |
| `--tw-slashed-zero` | `` |
| `--tw-numeric-figure` | `` |
| `--tw-numeric-spacing` | `` |
| `--tw-numeric-fraction` | `` |
| `--tw-ring-inset` | `` |
| `--tw-ring-offset-width` | `0px` |
| `--tw-ring-offset-color` | `#fff` |
| `--tw-ring-color` | `rgba(59,130,246,.5)` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `app-navigation__nav desktop-only` |
| `<nav>` | `-` | `app-navigation__nav mobile-only` |
| `<nav>` | `-` | `navigation-top-surface flex h-full min-w-0 items-center gap-2 rounded-full px-2 md:px-4` |
| `<header>` | `-` | `navigate-new sticky top-0 z-[100] md:z-[102] -mb-[var(--ui-header-height)] w-[calc(100%-12px)] ml-[6` |
| `<main>` | `-` | `aikiss-page` |
| `<footer>` | `-` | `w-full border-t border-slate-200 bg-[#F7F8FB] pt-8` |
