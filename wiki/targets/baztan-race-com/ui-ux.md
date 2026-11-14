---
title: "UI & Design System: baztan-race-com"
date: 2026-11-14
target: "[[overview|baztan-race-com]]"
---

# UI Architecture & Design Tokens: baztan-race-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--m2ccb-gap` | `1rem` |
| `--menu-ease-out` | `cubic-bezier(0.16, 1, 0.3, 1)` |
| `--menu-ease-in-out` | `cubic-bezier(0.65, 0, 0.35, 1)` |
| `--menu-ease-in` | `cubic-bezier(0.5, 0, 0.75, 0)` |
| `--menu-btn-r` | `calc(var(--menu-btn-h, 44px) / 2)` |
| `--gradient-progress` | `0%` |
| `--gradient-progress` | `0%` |
| `--gradient-progress` | `0%` |
| `--gradient-progress` | `0%` |
| `--hero-ease-out` | `cubic-bezier(0.16, 1, 0.3, 1)` |
| `--hero-ease-in-out` | `cubic-bezier(0.87, 0, 0.13, 1)` |
| `--hero-ease-back` | `cubic-bezier(0.34, 1.56, 0.64, 1)}[data-hero-footer].is-invi` |
| `--font-sans` | `ui-sans-serif, system-ui, sans-serif, "Apple Color Emoji",
 ` |
| `--font-mono` | `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Libe` |
| `--color-red-500` | `oklch(63.7% 0.237 25.331)` |
| `--color-gray-200` | `oklch(92.8% 0.006 264.531)` |
| `--color-gray-300` | `oklch(87.2% 0.01 258.338)` |
| `--color-gray-400` | `oklch(70.7% 0.022 261.325)` |
| `--color-gray-500` | `oklch(55.1% 0.027 264.364)` |
| `--color-gray-900` | `oklch(21% 0.034 264.665)` |
| `--color-black` | `#000000` |
| `--color-white` | `#FFFFFF` |
| `--spacing` | `0.25rem` |
| `--container-3xl` | `48rem` |
| `--container-4xl` | `56rem` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `main-menu` | `main-menu fixed z-[240] bg-green-deep overflow-hidden` |
| `<nav>` | `-` | `header-socials hidden lg:flex items-center gap-3` |
| `<nav>` | `-` | `footer-menu-container` |
| `<nav>` | `-` | `footer-menu-container` |
| `<nav>` | `-` | `flex flex-row items-center gap-3 mt-4` |
| `<header>` | `header` | `main-header fixed top-0 left-0 right-0 z-[250] transition-all duration-300` |
| `<main>` | `main` | `site-main` |
| `<footer>` | `footer-baztan` | `bg-dark-1 h-[1500px] lg:h-[750px] pb-16 pt-32 relative flex justify-center items-center` |
| `<dialog>` | `m2ccb-prefs` | `m2ccb-prefs` |
