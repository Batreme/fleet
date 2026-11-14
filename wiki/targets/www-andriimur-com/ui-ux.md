---
title: "UI & Design System: www-andriimur-com"
date: 2026-11-14
target: "[[overview|www-andriimur-com]]"
---

# UI Architecture & Design Tokens: www-andriimur-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--pswp-bg` | `#000` |
| `--pswp-placeholder-bg` | `#222` |
| `--pswp-root-z-index` | `100000` |
| `--pswp-preloader-color` | `#4f4f4f66` |
| `--pswp-preloader-color-secondary` | `#ffffffe6` |
| `--pswp-icon-color` | `#fff` |
| `--pswp-icon-color-secondary` | `#4f4f4f` |
| `--pswp-icon-stroke-color` | `#4f4f4f` |
| `--pswp-icon-stroke-width` | `2px` |
| `--pswp-error-text-color` | `var(--pswp-icon-color)` |
| `--arrow` | `disabled{cursor:default` |
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
| `--tw-space-y-reverse` | `0` |
| `--tw-space-x-reverse` | `0` |
| `--tw-border-style` | `solid` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `mobile-menu` | `fixed inset-0 z-(--z-overlay) flex flex-col items-end gap-y-6 bg-primary/40 px-4 pt-24 text-right ba` |
| `<nav>` | `-` | `flex flex-col gap-y-2 overflow-y-auto` |
| `<header>` | `-` | `sticky top-0 z-20 flex flex-wrap items-center gap-x-5 bg-transparent px-4 py-4 backdrop-blur md:px-1` |
| `<aside>` | `projects-panel` | `fixed inset-y-0 left-0 z-(--z-overlay) flex w-[22rem] max-w-[85vw] flex-col bg-primary/80 px-6 pt-24` |
| `<footer>` | `-` | `relative z-[var(--z-chrome)] bottom-0 w-full bg-neutral-900 py-6 md:py-8 text-center` |
