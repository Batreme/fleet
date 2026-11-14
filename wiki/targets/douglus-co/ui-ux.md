---
title: "UI & Design System: douglus-co"
date: 2026-11-14
target: "[[overview|douglus-co]]"
---

# UI Architecture & Design Tokens: douglus-co

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--page-padding` | `clamp(20px, 2.3vw, 40px)` |
| `--header-height` | `112px` |
| `--footer-right-width` | `clamp(38.75rem, 45.14vw, 48.75rem)` |
| `--white-color` | `#fefff8` |
| `--black-color` | `#1e1e1e` |
| `--neutral-color` | `#292724` |
| `--muted-color` | `#ebebeb` |
| `--default-easing` | `cubic-bezier(.25, 1, .5, 1)` |
| `--gw` | `4.16667vw}@media (width<=23.75rem){:root{--page-padding:.75r` |
| `--rv-ease` | `var(--default-easing)` |
| `--rv-ease-img` | `cubic-bezier(.76, 0, .24, 1)` |
| `--rv-d-s` | `.5s` |
| `--rv-d-m` | `.7s` |
| `--rv-d-l` | `.9s` |
| `--rv-step-t` | `40ms` |
| `--rv-step-l` | `80ms}:where([data-rv-group])>:where(:first-child){--i:0}:whe` |
| `--rv-step` | `var(--rv-step-l)}:where([data-rv-group=body]){--rv-d:var(--r` |
| `--rv-step` | `var(--rv-step-t)}:where([data-rv-group=label]){--rv-d:var(--` |
| `--rv-step` | `var(--rv-step-t)}:where([data-rv-group=media]){--rv-d:var(--` |
| `--rv-step` | `var(--rv-step-l)}:where([data-rv=line]){padding:var(--rv-pt,` |
| `--fast-start-easing` | `cubic-bezier(.17, .67, .1, .99)` |
| `--01` | `before,.site-header__menu:not(.is-opened-navi):hover .site-h` |
| `--cross01` | `before,.site-header__menu.is-opened-navi:hover .site-header_` |
| `--menu-panel-top` | `clamp(4.75rem, calc(3.5rem + 4vw), 8.25rem)` |
| `--menu-panel-bottom` | `clamp(1.875rem, 2vw, 2.75rem)` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `menu-overlay__nav` |
| `<header>` | `-` | `site-header` |
| `<aside>` | `-` | `menu-overlay__panel` |
| `<main>` | `-` | `` |
