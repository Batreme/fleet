---
title: "UI & Design System: zeyraglow-com"
date: 2026-10-31
target: "[[overview|zeyraglow-com]]"
---

# UI Architecture & Design Tokens: zeyraglow-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--e-nav-menu-horizontal-menu-item-margin` | `calc( 0em / 2 )` |
| `--main` | `not(.elementor-nav-menu--layout-horizontal) .elementor-nav-m` |
| `--e-nav-menu-horizontal-menu-item-margin` | `calc( 0.02em / 2 )` |
| `--main` | `not(.elementor-nav-menu--layout-horizontal) .elementor-nav-m` |
| `--e-nav-menu-horizontal-menu-item-margin` | `calc( 0.02em / 2 )` |
| `--main` | `not(.elementor-nav-menu--layout-horizontal) .elementor-nav-m` |
| `--e-icon-list-icon-size` | `14px` |
| `--icon-vertical-offset` | `0px` |
| `--e-icon-list-icon-size` | `14px` |
| `--icon-vertical-offset` | `0px` |
| `--display` | `flex` |
| `--flex-grow` | `0` |
| `--flex-shrink` | `0` |
| `--page-title-display` | `none` |
| `--woocommerce` | `#720eec` |
| `--wc-green` | `#007518` |
| `--wc-red` | `#a00` |
| `--wc-orange` | `#ffba00` |
| `--wc-blue` | `#2ea2cc` |
| `--wc-primary` | `#720eec` |
| `--wc-primary-text` | `#fcfbfe` |
| `--wc-secondary` | `#e9e6ed` |
| `--wc-secondary-text` | `#515151` |
| `--wc-highlight` | `#958e09` |
| `--wc-highligh-text` | `white` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `elementor-nav-menu--main elementor-nav-menu__container elementor-nav-menu--layout-horizontal e--poin` |
| `<nav>` | `-` | `elementor-nav-menu--dropdown elementor-nav-menu__container` |
| `<nav>` | `-` | `zg-home-footer-nav` |
| `<header>` | `-` | `elementor elementor-1083 elementor-location-header` |
| `<header>` | `-` | `cart-header` |
| `<aside>` | `-` | `cart-drawer` |
| `<main>` | `shop` | `` |
| `<footer>` | `-` | `cart-footer cart-footer--empty` |
| `<footer>` | `-` | `footer zg-home-official-footer` |
