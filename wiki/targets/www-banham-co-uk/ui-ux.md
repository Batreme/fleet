---
title: "UI & Design System: www-banham-co-uk"
date: 2026-11-14
target: "[[overview|www-banham-co-uk]]"
---

# UI Architecture & Design Tokens: www-banham-co-uk

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
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
| `--tw-ring-offset-width` | `0px` |
| `--tw-ring-offset-color` | `#fff` |
| `--tw-ring-color` | `#3b82f680` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `z-20 navigation leading-none` |
| `<nav>` | `-` | `absolute right-0 z-20 w-40 py-2 mt-2 -mr-4 px-1 overflow-auto origin-top-right rounded-sm shadow-lg ` |
| `<nav>` | `-` | `breadcrumbs text-black border-b hidden` |
| `<header>` | `-` | `page-header` |
| `<header>` | `-` | `relative flex justify-between items-center px-5 sm:px-6 md:px-10 bg-white text-primary` |
| `<main>` | `maincontent` | `page-main` |
| `<footer>` | `-` | `footer-container` |
| `<dialog>` | `authentication-popup` | `open:flex flex-col transition ease-out duration-300 motion-reduce:duration-0 p-0` |
| `<dialog>` | `newsletter-modal` | `open:flex flex-col justify-end md:justify-center md:h-fit h-full max-md:mt-auto my-0 md:m-auto bg-tr` |
