---
title: "UI & Design System: stillform-homes"
date: 2026-11-14
target: "[[overview|stillform-homes]]"
---

# UI Architecture & Design Tokens: stillform-homes

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--font-familjen-grotesk` | `"Familjen Grotesk", "Familjen Grotesk Fallback"}
@font-face{` |
| `--font-instrument-serif` | `"Instrument Serif", "Instrument Serif Fallback"}
@layer prop` |
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
| `--tw-space-x-reverse` | `0` |
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
| `<nav>` | `-` | `fixed left-0 top-0 z-50 w-full px-6 py-4 text-white mix-blend-difference md:px-10` |
| `<main>` | `top` | `overflow-x-clip` |
| `<footer>` | `contact` | `relative z-30 flex min-h-[100svh] w-full flex-col bg-[#EDE6D6] px-4 pb-[max(1rem,env(safe-area-inset` |
