---
title: "UI & Design System: www-villiers-ai"
date: 2026-11-14
target: "[[overview|www-villiers-ai]]"
---

# UI Architecture & Design Tokens: www-villiers-ai

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--font-inter` | `"Inter","Inter Fallback",system-ui,-apple-system,BlinkMacSys` |
| `--font-poppins` | `"Poppins","Poppins Fallback",-apple-system,BlinkMacSystemFon` |
| `--font-jetbrains-mono` | `"JetBrains Mono","JetBrains Mono Fallback",Menlo,ui-monospac` |
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

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `relative row-span-2 flex h-full min-h-0 flex-col justify-start gap-[0.25em] overflow-y-auto overflow` |
| `<nav>` | `-` | `grid grid-cols-2 gap-1 md:flex md:flex-col` |
| `<header>` | `-` | `fixed left-0 right-0 top-0 z-50 my-auto flex h-[var(--nav-height)] w-full flex-col border-b border-n` |
| `<footer>` | `-` | `flex flex-col justify-between bg-neutral-500 px-4 pt-16 text-white md:px-8 md:pt-section-lg h-full` |
