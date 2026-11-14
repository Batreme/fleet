---
title: "UI & Design System: rubenwalma-nl"
date: 2026-11-14
target: "[[overview|rubenwalma-nl]]"
---

# UI Architecture & Design Tokens: rubenwalma-nl

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--primary` | `#5766ab` |
| `--black` | `#121212` |
| `--white` | `#fff` |
| `--grey` | `#1D1D1D` |
| `--size-container-ideal` | `390` |
| `--size-container-min` | `320px` |
| `--size-container-max` | `479px` |
| `--size-container` | `clamp(var(--size-container-min), 100vw, var(--size-container` |
| `--size-unit` | `10` |
| `--size-font` | `calc(var(--size-container) / (var(--size-container-ideal) / ` |
| `--grid-columns` | `4` |
| `--grid-gap` | `1em` |
| `--container-padding` | `2em}@media screen and (min-width:480px){:root{--size-contain` |
| `--size-container-min` | `480px` |
| `--size-container-max` | `767px}}@media screen and (min-width:768px){:root{--size-cont` |
| `--size-container-min` | `768px` |
| `--size-container-max` | `991px` |
| `--grid-columns` | `6` |
| `--grid-gap` | `2em}}@media screen and (min-width:992px){:root{--size-contai` |
| `--size-container-min` | `992px` |
| `--size-container-max` | `1920px` |
| `--grid-columns` | `12` |
| `--container-padding` | `3em}}@media screen and (min-width:1920px){:root{--size-conta` |
| `--size-container-max` | `3840px}}::selection{background-color:var(--primary)` |
| `--roll-line` | `1.45` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `` |
| `<nav>` | `sidebar` | `sidebar` |
| `<header>` | `-` | `` |
| `<main>` | `-` | `` |
| `<footer>` | `-` | `` |
