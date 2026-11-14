---
title: "UI & Design System: bettr-academy"
date: 2026-11-14
target: "[[overview|bettr-academy]]"
---

# UI Architecture & Design Tokens: bettr-academy

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--w-backdrop-animation` | `initial` |
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
| `--color-scheme-1--background` | `var(--_primitives---colors--cream)` |
| `--_typography---font-styles--body` | `Roboto, sans-serif` |
| `--color-scheme-1--text` | `var(--_primitives---colors--coffee)` |
| `--_typography---font-styles--heading` | `Jobclarendon, Arial, sans-serif` |
| `--_primitives---colors--white` | `#fff` |
| `--_primitives---opacity--transparent` | `transparent` |
| `--_primitives---opacity--neutral-darkest-5` | `#0c0c0c0d` |
| `--_primitives---opacity--neutral-darkest-15` | `#0c0c0c26` |
| `--_primitives---colors--neutral-darkest` | `#0c0c0c` |
| `--_primitives---opacity--white-10` | `#ffffff1a` |
| `--_primitives---opacity--white-20` | `#fff3` |
| `--_primitives---colors--sunshine` | `#fcbf27` |
| `--_primitives---colors--coffee` | `#2c1c0f` |
| `--_primitives---colors--cream` | `#f7f4ed` |
| `--_primitives---colors--earth` | `#ed612f` |
| `--_primitives---colors--latte` | `#edd5b7` |
| `--_ui-styles---radius--small` | `.25rem` |
| `--_primitives---opacity--neutral-darkest-60` | `#0c0c0c99` |
| `--_primitives---opacity--white-60` | `#fff9` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `navbar_menu w-nav-menu` |
| `<nav>` | `w-dropdown-list-0` | `navbar_dropdown-list w-dropdown-list` |
| `<nav>` | `w-dropdown-list-1` | `navbar_dropdown-list w-dropdown-list` |
| `<nav>` | `w-dropdown-list-2` | `navbar_dropdown-list w-dropdown-list` |
| `<nav>` | `w-dropdown-list-3` | `navbar_dropdown-list w-dropdown-list` |
| `<nav>` | `w-dropdown-list-4` | `search-dropdown_list w-dropdown-list` |
| `<nav>` | `w-dropdown-list-5` | `search-dropdown_list w-dropdown-list` |
| `<header>` | `-` | `section_header` |
| `<main>` | `-` | `main-wrapper` |
| `<footer>` | `-` | `footer_component color-scheme-3` |
