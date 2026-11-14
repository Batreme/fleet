---
title: "UI & Design System: palaceskateboards-com"
date: 2026-11-14
target: "[[overview|palaceskateboards-com]]"
---

# UI Architecture & Design Tokens: palaceskateboards-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--tw-border-spacing-x` | `0` |
| `--tw-border-spacing-y` | `0` |
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
| `<nav>` | `-` | `h-full [&_a]:focus-visible:outline-2 [&_a]:focus-visible:outline-offset-2` |
| `<header>` | `-` | `fixed pointer-events-none left-0 top-0 z-220 pt-(--header-padding) w-full flex justify-center` |
| `<main>` | `-` | `min-h-dvh flex flex-col` |
| `<footer>` | `footer` | `relative z-1 pt-20 pb-5` |
