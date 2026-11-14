---
title: "UI & Design System: www-sigma-imaging-se"
date: 2026-11-14
target: "[[overview|www-sigma-imaging-se]]"
---

# UI Architecture & Design Tokens: www-sigma-imaging-se

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
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
| `--adp-background-color-selected-other-month` | `#a2ddf6` |
| `--adp-color` | `#4a4a4a` |
| `--adp-color-secondary` | `#9c9c9c` |
| `--adp-accent-color` | `#4eb5e6` |
| `--adp-color-current-date` | `var(--adp-accent-color)` |
| `--adp-color-other-month` | `#dedede` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `navigation sr-only` |
| `<nav>` | `-` | `` |
| `<nav>` | `am-account-menu` | `flex flex-col` |
| `<nav>` | `-` | `` |
| `<nav>` | `-` | `` |
| `<header>` | `ammenu-header-container` | `ammenu-header-container page-header` |
| `<header>` | `-` | `relative p-4` |
| `<header>` | `-` | `relative p-4` |
| `<header>` | `-` | `relative p-4 flex items-center justify-between` |
| `<header>` | `-` | `relative p-4` |
| `<header>` | `-` | `relative p-4` |
| `<aside>` | `-` | `box-content fixed z-50 font-normal text-base shadow-lg pb-5 w-screen max-sm:max-w-full max-w-[390px]` |
| `<aside>` | `-` | `bg-[var(--ammenu-main-menu-background)] box-content fixed z-50 font-normal text-base shadow-lg pt-5 ` |
| `<main>` | `maincontent` | `page-main` |
| `<footer>` | `-` | `page-footer` |
