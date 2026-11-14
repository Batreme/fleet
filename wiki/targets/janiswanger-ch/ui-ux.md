---
title: "UI & Design System: janiswanger-ch"
date: 2026-11-14
target: "[[overview|janiswanger-ch]]"
---

# UI Architecture & Design Tokens: janiswanger-ch

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

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `pointer-events-none fixed top-0 left-1/2 z-50 -translate-x-1/2 -translate-y-full transition-transfor` |
| `<nav>` | `main-navigation` | `z-2 in-[body:has(.hover-backdrop-link-hover)]:opacity-20 in-[body:has(.hover-backdrop-link-hover)]:b` |
| `<nav>` | `-` | `z-2 in-[body:has(.hover-backdrop-link-hover)]:opacity-20 in-[body:has(.hover-backdrop-link-hover)]:b` |
| `<header>` | `-` | `hero-home relative z-10 flex w-full min-h-screen flex-col items-center justify-center gap-2` |
| `<main>` | `main-content` | `relative` |
| `<footer>` | `-` | `site-footer relative z-10 overflow-x-clip bg-accent max-md:py-8 md:h-20` |
