---
title: "UI & Design System: runtimewire-com"
date: 2026-11-14
target: "[[overview|runtimewire-com]]"
---

# UI Architecture & Design Tokens: runtimewire-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--tw-translate-x` | `0` |
| `--tw-translate-y` | `0` |
| `--tw-translate-z` | `0` |
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
| `--tw-space-x-reverse` | `0` |
| `--tw-divide-x-reverse` | `0` |
| `--tw-border-style` | `solid` |
| `--tw-divide-y-reverse` | `0` |
| `--tw-gradient-position` | `initial` |
| `--tw-gradient-from` | `#0000` |
| `--tw-gradient-via` | `#0000` |
| `--tw-gradient-to` | `#0000` |
| `--tw-gradient-stops` | `initial` |
| `--tw-gradient-via-stops` | `initial` |
| `--tw-gradient-from-position` | `0%` |
| `--tw-gradient-via-position` | `50%` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `rw-nojs-nav` |
| `<nav>` | `-` | `flex items-center gap-8 rw-tag whitespace-nowrap w-full overflow-x-auto no-scrollbar` |
| `<header>` | `-` | `public-site-header flex flex-col bg-background/95 backdrop-blur-md sticky top-0 z-50 border-b border` |
| `<header>` | `-` | `mb-5 space-y-1` |
| `<header>` | `-` | `mb-3` |
| `<aside>` | `-` | `lg:col-span-4 lg:border-l lg:border-border lg:pl-8` |
| `<aside>` | `-` | `relative border border-border bg-card p-5 md:p-6` |
| `<aside>` | `-` | `@container relative overflow-hidden border border-border bg-card text-card-foreground mb-6 lg:hidden` |
| `<aside>` | `-` | `lg:col-span-4 space-y-6` |
| `<aside>` | `-` | `relative border border-border bg-card w-[300px] max-w-full min-h-[250px] p-5` |
| `<aside>` | `-` | `@container relative overflow-hidden border border-border bg-card text-card-foreground hidden lg:bloc` |
| `<aside>` | `-` | `border border-border border-t-2 border-t-primary bg-card p-5` |
| `<main>` | `main-content` | `public-main flex-1 relative z-10 scroll-mt-36` |
| `<footer>` | `-` | `border-t border-border mt-20 transition-opacity duration-300 relative z-10 bg-background/85 backdrop` |
| `<footer>` | `-` | `rw-nojs-footer` |
