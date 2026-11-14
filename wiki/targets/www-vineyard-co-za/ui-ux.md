---
title: "UI & Design System: www-vineyard-co-za"
date: 2026-11-14
target: "[[overview|www-vineyard-co-za]]"
---

# UI Architecture & Design Tokens: www-vineyard-co-za

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--disabled` | `hover {
    background-color: #999999` |
| `--disabled` | `hover {
    background-color: #666666` |
| `--highlighted` | `hover {
    cursor: pointer` |
| `--moz-device-pixel-ratio` | `1.5),
	   only screen and (min-device-pixel-ratio: 1.5){

	#` |
| `--swiper-theme-color` | `#007aff}:host{position:relative` |
| `--swiper-preloader-color` | `#fff}.swiper-lazy-preloader-black{--swiper-preloader-color: ` |
| `--action` | `hover{background:var(--adp-background-color-hover)}.air-date` |
| `--title` | `hover{background:var(--adp-background-color-hover)}.air-date` |
| `--current-hours` | `after,.air-datepicker-time--current-minutes:after{content:""` |
| `--row` | `first-child{margin-bottom:4px}.air-datepicker-time--row inpu` |
| `--adp-font-family` | `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helve` |
| `--adp-font-size` | `14px` |
| `--adp-width` | `246px` |
| `--adp-z-index` | `100` |
| `--adp-padding` | `4px` |
| `--adp-grid-areas` | `"nav" "body" "timepicker" "buttons"` |
| `--adp-transition-duration` | `.3s` |
| `--adp-transition-ease` | `ease-out` |
| `--adp-transition-offset` | `8px` |
| `--adp-background-color` | `#fff` |
| `--adp-background-color-hover` | `#f0f0f0` |
| `--adp-background-color-active` | `#eaeaea` |
| `--adp-background-color-in-range` | `rgba(92, 196, 239, .1)` |
| `--adp-background-color-in-range-focused` | `rgba(92, 196, 239, .2)` |
| `--adp-background-color-selected-other-month-focused` | `#8ad5f4` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `air-datepicker-nav` |
| `<nav>` | `-` | `air-datepicker-nav` |
| `<nav>` | `-` | `nav-inner` |
| `<nav>` | `-` | `nav` |
| `<nav>` | `-` | `nav desktop-only` |
| `<nav>` | `-` | `air-datepicker-nav` |
| `<nav>` | `-` | `air-datepicker-nav` |
| `<header>` | `-` | `header header-light` |
| `<main>` | `home` | `main` |
| `<footer>` | `-` | `footer` |
