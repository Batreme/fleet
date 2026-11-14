---
title: "UI & Design System: jjettas-com"
date: 2026-11-14
target: "[[overview|jjettas-com]]"
---

# UI Architecture & Design Tokens: jjettas-com

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
| `--tw-space-y-reverse` | `0` |
| `--tw-divide-y-reverse` | `0` |
| `--tw-border-style` | `solid` |
| `--tw-gradient-position` | `initial` |
| `--tw-gradient-from` | `#0000` |
| `--tw-gradient-via` | `#0000` |
| `--tw-gradient-to` | `#0000` |
| `--tw-gradient-stops` | `initial` |
| `--tw-gradient-via-stops` | `initial` |
| `--tw-gradient-from-position` | `0%` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `jj-menu-links relative m-auto flex shrink-0 flex-col items-center gap-y-2.5 md:gap-y-[min(20px,calc(` |
| `<nav>` | `-` | `mt-1.5` |
| `<nav>` | `-` | `flex flex-col gap-4 md:gap-[min(20px,2.6cqh)]` |
| `<header>` | `-` | `pointer-events-none fixed inset-x-0 top-0 z-[90] flex items-center justify-between px-6 py-5 md:px-[` |
| `<main>` | `main` | `` |
| `<footer>` | `-` | `relative flex h-auto w-full flex-col overflow-hidden md:block md:h-[var(--footer-desktop-height)]` |
