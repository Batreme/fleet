---
title: "UI & Design System: theperformancelab-ca"
date: 2026-11-14
target: "[[overview|theperformancelab-ca]]"
---

# UI Architecture & Design Tokens: theperformancelab-ca

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--font-display-family` | `"display","display Fallback"}@font-face{font-family:mono` |
| `--font-mono-family` | `"mono","mono Fallback"}@font-face{font-family:diatype` |
| `--font-diatype-family` | `"diatype","diatype Fallback"}

/*! tailwindcss v4.2.4 | MIT ` |
| `--tw-translate-y` | `0` |
| `--tw-translate-z` | `0` |
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
| `--tw-shadow` | `0 0 #0000` |
| `--tw-shadow-color` | `initial` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `absolute hidden md:block left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2` |
| `<nav>` | `-` | `absolute top-[1.75rem] left-[68.5625rem] flex flex-col gap-[2rem] font-[family:var(--font-display)] ` |
| `<header>` | `-` | `fixed inset-x-0 top-0 z-50 h-[3.5rem] md:h-[5.25rem] transition-[height,background-color,color] dura` |
| `<aside>` | `-` | `hidden md:flex fixed z-[60] flex-col items-start justify-center` |
| `<aside>` | `-` | `md:hidden fixed z-[60] flex flex-col items-start justify-center` |
| `<main>` | `-` | `` |
| `<footer>` | `-` | `md:hidden mx-auto max-w-[26.875rem] flex flex-col gap-[0.5rem] bg-white` |
| `<footer>` | `-` | `flex flex-col gap-[1rem] bg-white mx-auto` |
