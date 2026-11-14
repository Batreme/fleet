---
title: "UI & Design System: siglitos-com"
date: 2026-11-14
target: "[[overview|siglitos-com]]"
---

# UI Architecture & Design Tokens: siglitos-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--kncc-primary` | `var(--color-black)` |
| `--kncc-primary-hover` | `var(--color-black)` |
| `--kncc-primary-text` | `var(--color-white)` |
| `--font-primary` | `"Hobeaux",sans-serif` |
| `--font-secondary` | `"Golos Text",sans-serif` |
| `--cursor-default` | `url(imgs/cursor/basic.svg) 0 0,auto!important` |
| `--cursor-pointer` | `url(imgs/cursor/pointer.svg) 0 0,auto!important` |
| `--cursor-click` | `url(imgs/cursor/click.svg) 0 0,auto!important` |
| `--color-white` | `#fff` |
| `--color-black` | `#0e0e0e` |
| `--color-yellow-0` | `#fee214` |
| `--color-yellow-1` | `#ffed00` |
| `--color-yellow-2` | `#fff700` |
| `--color-yellow-3` | `#fcfc63` |
| `--color-green-0` | `#a2f708` |
| `--color-green-1` | `#93f100` |
| `--color-green-2` | `#62dd08` |
| `--color-green-3` | `#12b612` |
| `--color-green-4` | `#006300` |
| `--color-blue-0` | `#36f2ed` |
| `--color-blue-1` | `#25e9f2` |
| `--color-blue-2` | `#1cbdf4` |
| `--color-blue-3` | `#1b90f6` |
| `--color-blue-4` | `#00476b` |
| `--color-pink-0` | `#ff7cbe` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `b-header__menu` |
| `<main>` | `-` | `wa-main` |
