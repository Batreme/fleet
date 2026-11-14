---
title: "UI & Design System: madetodisrupt-com"
date: 2026-11-14
target: "[[overview|madetodisrupt-com]]"
---

# UI Architecture & Design Tokens: madetodisrupt-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--display` | `flex` |
| `--flex-direction` | `column` |
| `--container-widget-width` | `100%` |
| `--container-widget-height` | `initial` |
| `--container-widget-flex-grow` | `0` |
| `--container-widget-align-self` | `initial` |
| `--flex-wrap-mobile` | `wrap` |
| `--gap` | `32px 32px` |
| `--row-gap` | `32px` |
| `--column-gap` | `32px` |
| `--display` | `flex` |
| `--flex-direction` | `row` |
| `--container-widget-width` | `calc( ( 1 - var( --container-widget-flex-grow ) ) * 100% )` |
| `--container-widget-height` | `100%` |
| `--container-widget-flex-grow` | `1` |
| `--container-widget-align-self` | `stretch` |
| `--flex-wrap-mobile` | `wrap` |
| `--justify-content` | `space-between` |
| `--align-items` | `center` |
| `--main` | `not(.e--pointer-framed) .elementor-item:before,
					.elemen` |
| `--e-nav-menu-divider-color` | `var( --e-global-color-text )` |
| `--display` | `flex` |
| `--flex-direction` | `row` |
| `--container-widget-width` | `initial` |
| `--container-widget-height` | `100%` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `elementor-nav-menu--main elementor-nav-menu__container elementor-nav-menu--layout-horizontal e--poin` |
| `<nav>` | `-` | `elementor-nav-menu--dropdown elementor-nav-menu__container` |
| `<nav>` | `-` | `elementor-nav-menu--main elementor-nav-menu__container elementor-nav-menu--layout-vertical e--pointe` |
| `<nav>` | `-` | `elementor-nav-menu--dropdown elementor-nav-menu__container` |
| `<header>` | `-` | `entry-header ast-no-thumbnail ast-no-title ast-header-without-markup` |
| `<main>` | `main` | `site-main` |
| `<footer>` | `-` | `elementor elementor-425 elementor-location-footer` |
