---
title: "UI & Design System: www-polpharmabiologics-com"
date: 2026-11-14
target: "[[overview|www-polpharmabiologics-com]]"
---

# UI Architecture & Design Tokens: www-polpharmabiologics-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--nav-bg-blur` | `15.196px` |
| `--nav-link-color` | `white` |
| `--nav-drop-bg` | `rgba(230, 239, 239, .12)` |
| `--nav-drop-stroke` | `transparent` |
| `--nav-drop-shadow` | `inset -1.129px 1.129px 2.257px rgba(255, 255, 255, .15)` |
| `--nav-drop-blur` | `blur(var(--nav-bg-blur))` |
| `--nav-link-color` | `var(--_\1f7e2-colors---primary--deep-green, #005453)` |
| `--nav-drop-bg` | `white` |
| `--nav-drop-stroke` | `#E5E5E5` |
| `--nav-drop-shadow` | `none` |
| `--nav-drop-blur` | `none` |
| `--nav-link-color` | `white` |
| `--nav-drop-bg` | `rgba(230, 239, 239, .12)` |
| `--nav-drop-stroke` | `transparent` |
| `--nav-drop-shadow` | `inset -1.129px 1.129px 2.257px rgba(255, 255, 255, .15)` |
| `--nav-drop-blur` | `blur(var(--nav-bg-blur))` |
| `--nav-shape-mask` | `url("data:image/svg+xml` |
| `--tape-zoom` | `1` |
| `--tape-h` | `auto` |
| `--tape-shift-y` | `0px` |
| `--bottle-size` | `14` |
| `--bottle-w` | `calc(var(--bottle-size) * var(--tape-zoom) * 1%)` |
| `--bottle-h` | `calc(var(--bottle-size) * var(--tape-zoom) * 1.25vw)` |
| `--bottle-nudge-y` | `0%` |
| `--bottle-overlap` | `0px` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `nav_links-component` |
| `<nav>` | `w-dropdown-list-0` | `form_dropdown_nav w-dropdown-list` |
| `<header>` | `-` | `nav_component` |
| `<main>` | `-` | `main-wrapper` |
| `<footer>` | `-` | `section is-dark is-100dvh is-flex` |
