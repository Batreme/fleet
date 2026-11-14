---
title: "UI & Design System: www-oregonoutdooralliance-org"
date: 2026-11-14
target: "[[overview|www-oregonoutdooralliance-org]]"
---

# UI Architecture & Design Tokens: www-oregonoutdooralliance-org

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--connected-color` | `var(--color-two)}.ChromecastButton_module_chromecastButton__` |
| `--menu-width` | `16em}.ChaptersPanelMenuOption_module_chapterListItem__22a198` |
| `--menu-transition-settings` | `height 200ms ease,max-height 200ms ease` |
| `--clock-rotate-direction` | `1}.AnimatedClock_module_hands__8976d762{transform-origin:cen` |
| `--clock-rotate-direction` | `-1}@media (prefers-reduced-motion:reduce){.AnimatedClock_mod` |
| `--large` | `before {
  border-width: 5px` |
| `--large` | `after {
  border-width: 5px` |
| `--vertical` | `before, .w-widget-twitter-count-shim.w--vertical:after {
  c` |
| `--vertical` | `before {
  border-width: 5px` |
| `--vertical` | `after {
  border-width: 4px` |
| `--_theme---background` | `var(--swatch--light-200)` |
| `--_text-style---font-family` | `var(--_typography---font--primary-family)` |
| `--_theme---text` | `var(--swatch--dark-400)` |
| `--_text-style---font-size` | `var(--_typography---font-size--text-main)` |
| `--_text-style---line-height` | `var(--_typography---line-height--1-5)` |
| `--_text-style---font-weight` | `var(--_typography---font--primary-regular)` |
| `--_text-style---letter-spacing` | `var(--_typography---letter-spacing--0em)` |
| `--size--0-5rem` | `clamp(.5 * 1rem, ((.5 - ((.5 - .5) / (90 - 20) * 20)) * 1rem` |
| `--_theme---heading` | `var(--swatch--dark-800)` |
| `--_text-style---margin-top` | `var(--_spacing---space--4)` |
| `--_text-style---margin-bottom` | `var(--_spacing---space--4)` |
| `--_spacing---space--6` | `var(--size--2-5rem)` |
| `--size--1rem` | `clamp(1 * 1rem, ((1 - ((1 - 1) / (90 - 20) * 20)) * 1rem + (` |
| `--_spacing---space--7` | `var(--size--3rem)` |
| `--swatch--brand` | `var(--swatch--brand-base)` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `nav_desktop_layout u-position-relative` |
| `<nav>` | `w-dropdown-list-0` | `nav_dropdown_main_wrap is-desktop w-dropdown-list` |
| `<nav>` | `w-dropdown-list-1` | `nav_dropdown_main_wrap is-desktop w-dropdown-list` |
| `<nav>` | `w-dropdown-list-2` | `nav_dropdown_main_wrap is-desktop w-dropdown-list` |
| `<nav>` | `-` | `nav_menu_wrap w-nav-menu` |
| `<nav>` | `w-dropdown-list-3` | `nav_dropdown_main_wrap w-dropdown-list` |
| `<nav>` | `w-dropdown-list-4` | `nav_dropdown_main_wrap w-dropdown-list` |
| `<nav>` | `w-dropdown-list-5` | `nav_dropdown_main_wrap w-dropdown-list` |
| `<nav>` | `-` | `footer_layout u-grid-above` |
| `<main>` | `main` | `page_main` |
| `<footer>` | `-` | `footer_wrap u-overflow-hidden` |
