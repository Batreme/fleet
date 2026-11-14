---
title: "UI & Design System: suho-studio"
date: 2026-11-14
target: "[[overview|suho-studio]]"
---

# UI Architecture & Design Tokens: suho-studio

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--lightningcss-light` | `` |
| `--lightningcss-dark` | `initial` |
| `--secondary-loop-gap` | `clamp(4rem, 13vh, 7rem)` |
| `--trust-viewport` | `calc(var(--screen) - var(--browser-chrome))` |
| `--trust-top` | `max(.5rem, env(safe-area-inset-top,0px))` |
| `--trust-content-height` | `calc(var(--trust-viewport) - var(--trust-top) - var(--nav-ra` |
| `--trust-viewport` | `min(100svh, var(--screen))}}.client-trust-module-scss-module` |
| `--secondary-loop-gap` | `clamp(2rem, 8vw, 3.25rem)` |
| `--cover-media-left` | `55vw` |
| `--cover-media-width` | `clamp(10.5rem, 22vw, 19rem)` |
| `--blend-left` | `calc(var(--cover-media-left) - var(--page-gutter))` |
| `--blend-right` | `calc(var(--cover-media-left) + var(--cover-media-width) - va` |
| `--cover-description-offset` | `clamp(0rem, 8vw, 8rem)` |
| `--blend-left` | `calc(var(--cover-media-left) - var(--page-gutter) - var(--co` |
| `--blend-right` | `calc(var(--cover-media-left) + var(--cover-media-width) - va` |
| `--cover-media-left` | `min(55vw, 52rem)` |
| `--cover-media-width` | `clamp(22rem, min(20vw, 48svh), 32rem)}}@font-face{font-famil` |
| `--font-film-magazine` | `var(--font-major)` |
| `--font-film-reze` | `var(--font-major)` |
| `--font-film-silksong` | `var(--font-major)` |
| `--font-film-magazine` | `"Magazine Letter Web", var(--font-major)` |
| `--font-film-reze` | `"Awakenning Web", var(--font-major)` |
| `--font-film-silksong` | `"Trajanus Roman Web", var(--font-major)}.experimental-univer` |
| `--film-wipe` | `1` |
| `--blend-left` | `calc(var(--cover-media-left) - var(--page-gutter))` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<header>` | `-` | `light-table-module-scss-module__qu5a9G__head` |
| `<header>` | `-` | `experimental-universe-module-scss-module__zLkruq__chapterHead` |
| `<header>` | `-` | `experimental-universe-module-scss-module__zLkruq__chapterHead` |
| `<header>` | `-` | `experimental-universe-module-scss-module__zLkruq__chapterHead` |
| `<header>` | `-` | `client-trust-module-scss-module__Quy3sa__statement` |
| `<header>` | `-` | `client-trust-module-scss-module__Quy3sa__contactHeader` |
| `<aside>` | `-` | `client-trust-module-scss-module__Quy3sa__secondary` |
| `<main>` | `main-content` | `` |
