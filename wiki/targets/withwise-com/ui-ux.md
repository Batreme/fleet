---
title: "UI & Design System: withwise-com"
date: 2026-11-14
target: "[[overview|withwise-com]]"
---

# UI Architecture & Design Tokens: withwise-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--_fa-family` | `var(--fa-family, var(--fa-style-family, "Font Awesome 7 Free` |
| `--fa` | `"\30 "}.fa-1{--fa:"\31 "}.fa-2{--fa:"\32 "}.fa-3{--fa:"\33 "` |
| `--fa-font-brands` | `normal 400 1em/1 var(--fa-family-brands)}@font-face{font-fam` |
| `--fa-family` | `var(--fa-family-brands)` |
| `--fa-style` | `400}.fa-firefox-browser{--fa:""}.fa-ideal{--fa:""}.fa-micr` |
| `--fa-font-regular` | `normal 400 1em/1 var(--fa-family-classic)` |
| `--fa-style-family-classic` | `var(--fa-family-classic)}@font-face{font-family:"Font Awesom` |
| `--fa-family` | `var(--fa-family-classic)` |
| `--fa-style` | `400}.fa-classic{--fa-family: var(--fa-family-classic)}.fa-re` |
| `--fa-font-solid` | `normal 900 1em/1 var(--fa-family-classic)` |
| `--fa-style-family-classic` | `var(--fa-family-classic)}@font-face{font-family:"Font Awesom` |
| `--fa-family` | `var(--fa-family-classic)` |
| `--fa-style` | `900}.fa-classic{--fa-family: var(--fa-family-classic)}.fa-so` |
| `--gf-radius` | `3px` |
| `--gf-radius-max-sm` | `2px` |
| `--gf-radius-max-md` | `3px` |
| `--gf-radius-max-lg` | `8px}.gform-theme--api,.gform-theme--framework{--gf-color-pri` |
| `--gf-color-primary-rgb` | `45,127,251` |
| `--gf-color-primary-contrast` | `#fff` |
| `--gf-color-primary-contrast-rgb` | `255,255,255` |
| `--gf-color-primary-darker` | `#044ad3` |
| `--gf-color-primary-lighter` | `#044ad3` |
| `--gf-color-secondary` | `#fff` |
| `--gf-color-secondary-rgb` | `255,255,255` |
| `--gf-color-secondary-contrast` | `#112337` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `main-menu` | `top-bar` |
| `<header>` | `-` | `header` |
| `<main>` | `-` | `main-content` |
| `<footer>` | `-` | `footer` |
