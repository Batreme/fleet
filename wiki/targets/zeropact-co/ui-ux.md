---
title: "UI & Design System: zeropact-co"
date: 2026-11-14
target: "[[overview|zeropact-co]]"
---

# UI Architecture & Design Tokens: zeropact-co

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--swiper-theme-color` | `#007aff}.swiper{margin-left:auto` |
| `--swiper-navigation-size` | `44px}.swiper-button-next,.swiper-button-prev{position:absolu` |
| `--swiper-preloader-color` | `#fff}.swiper-lazy-preloader-black{--swiper-preloader-color:#` |
| `--animation-none` | `after,.e--pointer-double-line.e--animation-none:before,.e--p` |
| `--animation-none` | `after,.e--pointer-framed.e--animation-none:before,.e--pointe` |
| `--animation-none` | `after,.e--pointer-background.e--animation-none:before,.e--po` |
| `--menu-height` | `100vh}.elementor-nav-menu--toggle .elementor-menu-toggle:not` |
| `--display` | `flex` |
| `--flex-direction` | `column` |
| `--container-widget-width` | `calc( ( 1 - var( --container-widget-flex-grow ) ) * 100% )` |
| `--container-widget-height` | `initial` |
| `--container-widget-flex-grow` | `0` |
| `--container-widget-align-self` | `initial` |
| `--flex-wrap-mobile` | `wrap` |
| `--align-items` | `center` |
| `--padding-top` | `200px` |
| `--padding-bottom` | `100px` |
| `--padding-left` | `10px` |
| `--padding-right` | `10px}.elementor-2129 .elementor-element.elementor-element-28` |
| `--container-widget-width` | `1000px` |
| `--container-widget-flex-grow` | `0` |
| `--container-widget-width` | `650px` |
| `--container-widget-flex-grow` | `0` |
| `--e-search-input-color` | `var( --e-global-color-text )}.elementor-widget-search.e-focu` |
| `--container-widget-width` | `500px` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `elementor-nav-menu--main elementor-nav-menu__container elementor-nav-menu--layout-horizontal e--poin` |
| `<nav>` | `-` | `elementor-nav-menu--dropdown elementor-nav-menu__container` |
| `<nav>` | `-` | `elementor-nav-menu--dropdown elementor-nav-menu__container` |
| `<nav>` | `-` | `elementor-nav-menu--main elementor-nav-menu__container elementor-nav-menu--layout-vertical e--pointe` |
| `<nav>` | `-` | `elementor-nav-menu--dropdown elementor-nav-menu__container` |
| `<header>` | `-` | `elementor elementor-198 elementor-location-header` |
| `<footer>` | `-` | `elementor elementor-172 elementor-location-footer` |
