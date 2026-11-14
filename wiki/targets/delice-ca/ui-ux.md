---
title: "UI & Design System: delice-ca"
date: 2026-11-14
target: "[[overview|delice-ca]]"
---

# UI Architecture & Design Tokens: delice-ca

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--full-ui` | `after,.plyr--full-ui :before{box-sizing:inherit}.plyr--full-` |
| `--full-ui` | `:-webkit-media-text-track-container{display:none}.plyr__capt` |
| `--full-ui` | `:-webkit-media-controls{display:none}.plyr__controls{text-al` |
| `--forward` | `after{border-left-color:#728197` |
| `--forward` | `hover:after{border-left-color:initial}.plyr__menu__container` |
| `--back` | `after{border-right-color:#728197` |
| `--back` | `before{background:#dcdfe5` |
| `--back` | `hover:after{border-right-color:initial}.plyr__menu__containe` |
| `--overlaid` | `focus,.plyr__control--overlaid:hover{opacity:1}.plyr--playin` |
| `--header-banner-height` | `2.75rem` |
| `--header-inner-height` | `clamp(64px, 47.0986px + 4.50704vw, 7rem)` |
| `--header-height` | `calc(var(--header-banner-height) + var(--header-inner-height` |
| `--menu-banner-height` | `2.5rem` |
| `--menu-nav-height` | `6rem` |
| `--promotion-media-size` | `min(34rem, 55vh)` |
| `--plyr-color-main` | `var(--primary-500)` |
| `--section-spacing-top-default` | `clamp(64px, 41.4648px + 6.00939vw, 8rem)` |
| `--section-spacing-bottom-default` | `clamp(64px, 41.4648px + 6.00939vw, 8rem)` |
| `--section-spacing-top-compact` | `clamp(64px, 64px + 0vw, 4rem)` |
| `--section-spacing-bottom-compact` | `clamp(64px, 64px + 0vw, 4rem)` |
| `--container-spacing-md` | `clamp(32px, 20.7324px + 3.0047vw, 4rem)` |
| `--primary-300` | `#f5dbca` |
| `--primary-300-rgb` | `245, 219, 202` |
| `--on-primary-300` | `#de2b2b` |
| `--on-primary-300-rgb` | `222, 43, 43` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `c-header_nav -left` |
| `<nav>` | `-` | `c-header_nav -right` |
| `<nav>` | `-` | `c-burger-menu_nav` |
| `<nav>` | `-` | `c-burger-menu_nav` |
| `<nav>` | `-` | `c-burger-menu_buttons` |
| `<nav>` | `-` | `c-nav` |
| `<nav>` | `-` | `c-footer_nav || u-gc-1/4 u-gc-1/1@tablet` |
| `<nav>` | `-` | `c-footer_nav -secondary || u-gc-4/7 u-gc-1/1@tablet` |
| `<header>` | `-` | `c-header` |
| `<main>` | `swup` | `` |
| `<footer>` | `-` | `c-footer` |
