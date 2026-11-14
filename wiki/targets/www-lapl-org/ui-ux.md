---
title: "UI & Design System: www-lapl-org"
date: 2026-11-14
target: "[[overview|www-lapl-org]]"
---

# UI Architecture & Design Tokens: www-lapl-org

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--lapl-transition-easeInOutQuad` | `cubic-bezier(0.45,0,0.55,1)}
:root{--lapl-clr-sunburn:#ffccd` |
| `--lapl-clr-coral` | `#ff9eaf` |
| `--lapl-clr-red` | `#eb4646` |
| `--lapl-clr-brick` | `#bf2713` |
| `--lapl-clr-peach` | `#fc9` |
| `--lapl-clr-orange` | `#ff9326` |
| `--lapl-clr-burnt-orange` | `#bd5d2d` |
| `--lapl-clr-buttercream` | `#ffeba8` |
| `--lapl-clr-yellow` | `#ffde39` |
| `--lapl-clr-gold` | `#eb9c00` |
| `--lapl-clr-sage` | `#d6e5ae` |
| `--lapl-clr-green` | `#a2c746` |
| `--lapl-clr-dark-green` | `#20661a` |
| `--lapl-clr-robins-egg` | `#aedce5` |
| `--lapl-clr-teal` | `#3cbcd6` |
| `--lapl-clr-jade` | `#26464d` |
| `--lapl-clr-sky-blue` | `#a6cef5` |
| `--lapl-clr-azure` | `#6996f0` |
| `--lapl-clr-link-blue` | `#1554b2` |
| `--lapl-clr-navy` | `#002759` |
| `--lapl-clr-lavender` | `#e3c6f7` |
| `--lapl-clr-purple` | `#bf89e5` |
| `--lapl-clr-violet` | `#7b5099` |
| `--lapl-clr-millenial-pink` | `#ffcce4` |
| `--lapl-clr-pink` | `#ff8fc7` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `block-lapl-utility-navigation-header` | `` |
| `<nav>` | `main-navigation` | `site-header__menu-main` |
| `<nav>` | `main-navigation` | `site-header__menu-main` |
| `<nav>` | `block-lapl-utility-navigation-flyout` | `` |
| `<nav>` | `-` | `c-linked-card__menu` |
| `<nav>` | `-` | `c-cta-card__menu` |
| `<nav>` | `block-lapl-menu-footer` | `` |
| `<nav>` | `block-lapl-social-english-footer` | `` |
| `<nav>` | `block-lapl-social-spanish-footer` | `` |
| `<nav>` | `block-lapl-app-footer` | `` |
| `<header>` | `site-header` | `r-site-header` |
| `<header>` | `-` | `p-homepage__header lapl-gradient--blue-green` |
| `<main>` | `-` | `` |
| `<footer>` | `site-footer` | `r-site-footer` |
