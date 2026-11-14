---
title: "UI & Design System: kindi-land"
date: 2026-11-14
target: "[[overview|kindi-land]]"
---

# UI Architecture & Design Tokens: kindi-land

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--font-custom` | `"customFont","customFont Fallback"}
@font-face{font-family:c` |
| `--font-custom2` | `"customFont2","customFont2 Fallback"}
@layer properties{@sup` |
| `--tw-translate-y` | `0` |
| `--tw-translate-z` | `0` |
| `--tw-rotate-x` | `initial` |
| `--tw-rotate-y` | `initial` |
| `--tw-rotate-z` | `initial` |
| `--tw-skew-x` | `initial` |
| `--tw-skew-y` | `initial` |
| `--tw-space-y-reverse` | `0` |
| `--tw-border-style` | `solid` |
| `--tw-leading` | `initial` |
| `--tw-font-weight` | `initial` |
| `--tw-tracking` | `initial` |
| `--tw-shadow` | `0 0 #0000` |
| `--tw-shadow-color` | `initial` |
| `--tw-shadow-alpha` | `100%` |
| `--tw-inset-shadow` | `0 0 #0000` |
| `--tw-inset-shadow-color` | `initial` |
| `--tw-inset-shadow-alpha` | `100%` |
| `--tw-ring-color` | `initial` |
| `--tw-ring-shadow` | `0 0 #0000` |
| `--tw-inset-ring-color` | `initial` |
| `--tw-inset-ring-shadow` | `0 0 #0000` |
| `--tw-ring-inset` | `initial` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<header>` | `-` | `staggered-menu-header pointer-events-none absolute top-0 left-0 z-20 flex w-full items-center justif` |
| `<aside>` | `staggered-menu-panel` | `staggered-menu-panel bg-primary pointer-events-auto absolute top-0 right-0 z-10 flex h-full flex-col` |
| `<footer>` | `-` | `relative z-10 m-0` |
