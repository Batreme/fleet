---
title: "UI & Design System: dwell-au"
date: 2026-11-14
target: "[[overview|dwell-au]]"
---

# UI Architecture & Design Tokens: dwell-au

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--header-height` | `calc(108*max(1px,min(.0661376vw,.124069svh)))` |
| `--viewport-height` | `100vh` |
| `--viewport-height` | `100dvh}}@media print{body{display:block` |
| `--v-fade` | `opacity .6s var(--io2)` |
| `--v-fade` | `opacity 0s` |
| `--n-toggle` | `2.91667vw}@media (min-aspect-ratio:1440/865){#h{--n-toggle:4` |
| `--n-gap` | `3.75vw` |
| `--n-row` | `max(calc(44*max(1px,min(.0661376vw,.124069svh))),calc(calc(8` |
| `--n-gap` | `1.875svh}}@media (max-width:700px) and (orientation:portrait` |
| `--n-row` | `max(calc(44*max(1px,min(.0661376vw,.124069svh))),calc(calc(6` |
| `--n-gap` | `1.875svh}}@media (max-width:1200px) and (max-height:500px) a` |
| `--menu-offset` | `calc(var(--n-toggle)*-3.8/42)}.menu-icon:after{--menu-offset` |
| `--n-img` | `36.1111vw}@media (min-aspect-ratio:1440/865){#nav{--n-img:60` |
| `--n-cut-x` | `calc(-58*max(1px,min(.0661376vw,.124069svh)))` |
| `--n-cut-y` | `calc(143*max(1px,min(.0661376vw,.124069svh)))` |
| `--n-font` | `calc(40.06*max(1px,min(.0661376vw,.124069svh)))` |
| `--n-photo` | `min(calc(400*max(1px,min(.0661376vw,.124069svh))),var(--n-im` |
| `--n-font-s` | `9.25vw` |
| `--n-img` | `83.25vw` |
| `--n-cut` | `72.25vw` |
| `--n-cut-w` | `min(calc(260*max(1px,min(.0661376vw,.124069svh))),var(--n-cu` |
| `--n-cut-x` | `calc(-56*max(1px,min(.0661376vw,.124069svh)))` |
| `--n-cut-y` | `calc(130*max(1px,min(.0661376vw,.124069svh)))` |
| `--n-font` | `min(calc(33*max(1px,min(.0661376vw,.124069svh))),var(--n-fon` |
| `--n-photo` | `min(calc(300*max(1px,min(.0661376vw,.124069svh))),var(--n-im` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `h-links` | `txt-lm` |
| `<nav>` | `nav` | `` |
| `<nav>` | `fab` | `txt-lm _ns` |
| `<nav>` | `foo-links` | `txt-lm` |
| `<nav>` | `foo-legal` | `` |
| `<header>` | `h` | `` |
| `<header>` | `-` | `fab-form-header` |
| `<header>` | `-` | `fab-questions-header fab-form-header` |
| `<header>` | `-` | `cookie-header` |
| `<aside>` | `-` | `cookie-notice txt-ls` |
| `<main>` | `main` | `` |
| `<footer>` | `foo` | `` |
| `<dialog>` | `cookie-dialog` | `` |
