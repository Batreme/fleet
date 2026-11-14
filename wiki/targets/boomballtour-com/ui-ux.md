---
title: "UI & Design System: boomballtour-com"
date: 2026-11-14
target: "[[overview|boomballtour-com]]"
---

# UI Architecture & Design Tokens: boomballtour-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--_fa-family` | `var(--fa-family,var(--fa-style-family,"Font Awesome 7 Free")` |
| `--fa-width` | `auto}.fa-fw,.fa-width-fixed{--fa-width:1.25em}.fa-ul{list-st` |
| `--fa-animation-direction` | `reverse}.fa-pulse,.fa-spin-pulse{animation-name:fa-spin` |
| `--fa-width` | `100%` |
| `--fa-family-classic` | `"Font Awesome 7 Free"` |
| `--fa-font-regular` | `normal 400 1em/1 var(--fa-family-classic)` |
| `--fa-style-family-classic` | `var(--fa-family-classic)}@font-face{font-family:"Font Awesom` |
| `--bb-color-pink` | `#ff1e96` |
| `--bb-color-blue` | `#1f335e` |
| `--bb-color-gold` | `#c2a155` |
| `--bb-color-ink` | `#43433d` |
| `--bb-color-paper` | `#f3ebdc` |
| `--bb-color-white` | `#ffffff` |
| `--bb-color-slate` | `#79859f` |
| `--bb-color-frame` | `rgb(255 255 255 / 35%)` |
| `--bb-color-divider` | `#B8B3A8` |
| `--bb-color-inactive` | `#f894c5` |
| `--bb-font-body` | `"Inter-400", Arial, Helvetica, sans-serif` |
| `--bb-font-body-medium` | `"Inter-500", Arial, Helvetica, sans-serif` |
| `--bb-font-heading` | `"Hamburg-700", Arial, Helvetica, sans-serif` |
| `--bb-font-display` | `"Groundout", Georgia, serif` |
| `--bb-font-script` | `"Brooklyn-700", Georgia, serif` |
| `--bb-font-mono` | `"Roboto-600", "Courier New", monospace` |
| `--bb-radius-media` | `10px` |
| `--bb-border-media` | `4px` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `footer-nav` |
| `<footer>` | `-` | `site-footer` |
| `<dialog>` | `bb-consent-dialog` | `bb-consent-dialog` |
