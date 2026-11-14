---
title: "UI & Design System: henwoodcourt-co-uk"
date: 2026-11-14
target: "[[overview|henwoodcourt-co-uk]]"
---

# UI Architecture & Design Tokens: henwoodcourt-co-uk

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--tw-translate-x` | `0` |
| `--tw-translate-y` | `0` |
| `--tw-translate-z` | `0` |
| `--tw-rotate-x` | `initial` |
| `--tw-rotate-y` | `initial` |
| `--tw-rotate-z` | `initial` |
| `--tw-skew-x` | `initial` |
| `--tw-skew-y` | `initial` |
| `--tw-divide-y-reverse` | `0` |
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
| `--tw-blur` | `initial` |
| `--tw-brightness` | `initial` |
| `--tw-contrast` | `initial` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `nav` | `z-50 pointer-events-auto fixed top-0 inset-x-0 bottom-0 xl:relative xl:top-auto xl:inset-x-auto xl:b` |
| `<nav>` | `-` | `hidden md:flex flex-col gap-6` |
| `<nav>` | `-` | `hidden md:flex flex-col gap-6` |
| `<header>` | `header` | `fixed top-0 inset-x-0 z-60 pointer-events-none transition-[top] duration-300 group-[.header-hide]/bo` |
| `<main>` | `main` | `grow pt-page-top group-[.theme-flush-hero]/body:pt-0` |
| `<footer>` | `footer` | `bg-linear-to-b from-med-purple to-dark-purple text-white` |
| `<dialog>` | `vimeo-modal` | `modal-wrap m-0 max-h-none max-w-none w-screen h-(--vh-100,100vh) bg-transparent p-0 open:flex open:i` |
