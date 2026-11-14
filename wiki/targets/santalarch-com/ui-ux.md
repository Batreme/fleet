---
title: "UI & Design System: santalarch-com"
date: 2026-11-14
target: "[[overview|santalarch-com]]"
---

# UI Architecture & Design Tokens: santalarch-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--viewport-width` | `1440` |
| `--viewport-height` | `800}@media(max-width:1023px){:root{--viewport-width:416` |
| `--viewport-height` | `824}}:root{--font-helvetica:"Helvetica",sans-serif` |
| `--ease-out` | `cubic-bezier(.25,1,.5,1)` |
| `--transition` | `.5s var(--ease-out)` |
| `--transition-fast` | `.3s var(--ease-out)` |
| `--transition-slow` | `.8s var(--ease-out)` |
| `--c-base-light-primary` | `#f0f0f0` |
| `--c-base-line-highlight` | `#f2f0f033` |
| `--c-base-line-dark-bg` | `#f2f0f00d` |
| `--c-pure-black` | `#000` |
| `--c-pure-white` | `#fff` |
| `--c-pure-black-rgb` | `0,0,0` |
| `--c-pure-black-0` | `rgba(var(--c-pure-black-rgb),0)` |
| `--c-light-primary` | `var(--c-base-light-primary)` |
| `--c-light-secondary` | `#f2f0f066` |
| `--c-base-dark-primary` | `#0f0f0f` |
| `--c-base-dark-primary-rgb` | `15,15,15` |
| `--c-base-dark-primary-07` | `rgba(var(--c-base-dark-primary-rgb),.07)` |
| `--c-base-dark-primary-20` | `rgba(var(--c-base-dark-primary-rgb),.2)` |
| `--c-base-dark-primary-30` | `rgba(var(--c-base-dark-primary-rgb),.3)` |
| `--c-base-dark-primary-40` | `rgba(var(--c-base-dark-primary-rgb),.4)` |
| `--c-dark-primary` | `var(--c-base-dark-primary)` |
| `--c-dark-secondary` | `#0f0f0f66` |
| `--c-line-highlight` | `var(--c-base-line-highlight)` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `header-container grid-container` |
| `<header>` | `header` | `header difference` |
| `<aside>` | `-` | `cookies` |
| `<main>` | `main-page` | `main-page` |
