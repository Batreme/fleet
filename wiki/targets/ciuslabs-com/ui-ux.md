---
title: "UI & Design System: ciuslabs-com"
date: 2026-11-14
target: "[[overview|ciuslabs-com]]"
---

# UI Architecture & Design Tokens: ciuslabs-com

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
| `--tw-border-style` | `solid` |
| `--tw-leading` | `initial` |
| `--tw-font-weight` | `initial` |
| `--tw-tracking` | `initial` |
| `--tw-ordinal` | `initial` |
| `--tw-slashed-zero` | `initial` |
| `--tw-numeric-figure` | `initial` |
| `--tw-numeric-spacing` | `initial` |
| `--tw-numeric-fraction` | `initial` |
| `--tw-shadow` | `0 0 #0000` |
| `--tw-shadow-color` | `initial` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `ds-container relative h-full grid grid-cols-[1fr_auto] md:grid-cols-2 gap-x-(--ds-space-l) items-cen` |
| `<nav>` | `-` | `grid grid-cols-2 gap-(--ds-space-xl) sm:grid-cols-3 md:col-span-6 md:col-start-7` |
| `<nav>` | `-` | `flex flex-wrap items-center gap-(--ds-space-l)` |
| `<nav>` | `-` | `flex flex-col gap-(--ds-space-m)` |
| `<nav>` | `-` | `flex flex-col gap-(--ds-space-s)` |
| `<header>` | `-` | `flex max-w-[24em] shrink-0 flex-col gap-(--ds-space-s) in-[.js-motion]:md:w-[min(calc(var(--ds-text-` |
| `<header>` | `-` | `relative flex items-center justify-between w-full h-(--ds-navbar-height) shrink-0` |
| `<aside>` | `-` | `fixed inset-0 z-(--ds-z-max) pointer-events-auto select-none overflow-hidden` |
| `<main>` | `main` | `` |
| `<footer>` | `-` | `relative z-(--ds-z-raised) w-full overflow-x-clip bg-inverse text-fg pt-(--ds-space-section-m) md:pt` |
| `<footer>` | `-` | `w-full shrink-0 grid gap-(--ds-space-l) md:gap-x-(--ds-space-xxl) md:grid-cols-2 items-end pb-(--ds-` |
