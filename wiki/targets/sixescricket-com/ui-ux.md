---
title: "UI & Design System: sixescricket-com"
date: 2026-11-14
target: "[[overview|sixescricket-com]]"
---

# UI Architecture & Design Tokens: sixescricket-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--sa-uid` | `'CiQwMWExZGI3YS00Y2ViLTc2NjgtYWExYy0yYmI1NjJkNjUwYWYQBBoERU1` |
| `--font-inter` | `"Inter", "Inter Fallback"}
@font-face{font-family:fontSoehne` |
| `--tw-translate-x` | `0` |
| `--tw-translate-y` | `0` |
| `--tw-translate-z` | `0` |
| `--tw-rotate-x` | `initial` |
| `--tw-rotate-y` | `initial` |
| `--tw-rotate-z` | `initial` |
| `--tw-skew-x` | `initial` |
| `--tw-skew-y` | `initial` |
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
| `--tw-gradient-to-position` | `100%` |
| `--tw-leading` | `initial` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `hidden h-full flex-col items-start lg:flex` |
| `<nav>` | `-` | `my-auto flex flex-col items-center py-16 text-wool-500` |
| `<nav>` | `-` | `flex flex-col items-start gap-3 font-inter text-p-xs` |
| `<nav>` | `-` | `flex flex-col items-start gap-3 font-inter text-p-xs` |
| `<nav>` | `-` | `flex flex-col items-start gap-3 font-inter text-p-xs` |
| `<nav>` | `-` | `flex flex-col items-start gap-3 font-inter text-p-xs` |
| `<header>` | `-` | `sticky top-0 z-50 flex h-nav w-full flex-col items-center justify-center border-b border-current/10 ` |
| `<aside>` | `-` | `pointer-events-none fixed top-nav right-0 left-0 z-40 h-screen-nav bg-mahogany-500` |
| `<main>` | `main-content` | `relative flex w-full flex-col [&>*:last-child:not(:only-child)]:mb-auto` |
| `<footer>` | `-` | `relative bg-mahogany-500 px-buffer text-wool-500` |
