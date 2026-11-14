---
title: "UI & Design System: www-areyoudami-com"
date: 2026-11-14
target: "[[overview|www-areyoudami-com]]"
---

# UI Architecture & Design Tokens: www-areyoudami-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--font-inter` | `"Inter", "Inter Fallback"}
@font-face{font-family:Work Sans` |
| `--font-work-sans` | `"Work Sans", "Work Sans Fallback"}
@layer properties{@suppor` |
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
| `--tw-space-y-reverse` | `0` |
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

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `pointer-events-auto absolute left-[var(--gutter)] top-[60svh] flex flex-col items-center gap-1.5` |
| `<header>` | `-` | `fixed left-[var(--gutter)] top-5 z-50 md:top-6` |
| `<main>` | `main` | `` |
| `<footer>` | `-` | `relative overflow-hidden px-[var(--gutter)] py-[200px] bg-ink` |
