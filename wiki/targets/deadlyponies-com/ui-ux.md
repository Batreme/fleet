---
title: "UI & Design System: deadlyponies-com"
date: 2026-11-14
target: "[[overview|deadlyponies-com]]"
---

# UI Architecture & Design Tokens: deadlyponies-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--height-full` | `100vh` |
| `--height-fill` | `calc( 100vh - var(--nav-height) )` |
| `--font-deadly` | `"Deadly", sans-serif` |
| `--nav-main-height` | `46px` |
| `--nav-height` | `var(--nav-main-height)}.navbar__announcement{padding:0` |
| `--fore-color` | `#000` |
| `--link` | `:after{display:none}.announcement-bar__item p{display:block` |
| `--StackItem-gap` | `var(--x-spacing-small-100)` |
| `--StackWrapper-vertical-padding` | `var(--x-spacing-large-200) 1.2rem` |
| `--StackItem-max-width` | `26.2rem` |
| `--Skeleton-animation-duration` | `calc(2 * var(--x-duration-slowest))` |
| `--StackWrapper-vertical-padding` | `var(--x-spacing-large-100) 2rem}}@media screen and (min-widt` |
| `--StackItem-height` | `4.8rem` |
| `--StackItem-max-width` | `262px` |
| `--StackItem-columns` | `100%` |
| `--StackItem-columns` | `calc(50% - (var(--StackItem-gap) / 2))}:is(.HLgiC.CadfY>*):f` |
| `--hiddenButtonPosition` | `relative` |
| `--hiddenButtonWidth` | `auto` |
| `--hiddenButtonVisibility` | `visible` |
| `--hiddenButtonOpacity` | `1}@media screen and (min-width:280px){.w6E2R[data-count="3"]` |
| `--hiddenButtonPosition` | `relative` |
| `--hiddenButtonWidth` | `auto` |
| `--hiddenButtonVisibility` | `visible` |
| `--hiddenButtonOpacity` | `1}}@media screen and (min-width:375px){.w6E2R[data-count="4"` |
| `--hiddenButtonPosition` | `relative` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `header__nav` |
| `<header>` | `-` | `header header--dark` |
| `<main>` | `-` | `content-for-layout` |
| `<footer>` | `-` | `footer` |
