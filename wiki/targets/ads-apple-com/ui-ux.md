---
title: "UI & Design System: ads-apple-com"
date: 2026-11-14
target: "[[overview|ads-apple-com]]"
---

# UI Architecture & Design Tokens: ads-apple-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--r-globalnav-background-opened` | `#fafafc` |
| `--r-globalnav-background-opened-dark` | `#161617}#globalnav:not([dir=rtl]){--r-globalnav-start: var(-` |
| `--r-globalnav-end` | `var(--r-sk-end, right)` |
| `--r-globalnav-safe-area-inset-start` | `var(--sk-safe-area-inset-start, env(safe-area-inset-left))` |
| `--r-globalnav-safe-area-inset-end` | `var(--sk-safe-area-inset-end, env(safe-area-inset-right))` |
| `--r-globalnav-logical-factor` | `1}#globalnav[dir=rtl]{--r-globalnav-start: var(--r-sk-start,` |
| `--r-globalnav-end` | `var(--r-sk-end, left)` |
| `--r-globalnav-safe-area-inset-start` | `var(--sk-safe-area-inset-start, env(safe-area-inset-right))` |
| `--r-globalnav-safe-area-inset-end` | `var(--sk-safe-area-inset-end, env(safe-area-inset-left))` |
| `--r-globalnav-logical-factor` | `-1}#globalnav{--r-globalnav-flyout-close-delay: .12s` |
| `--r-globalnav-flyout-link-opacity-duration` | `.5s` |
| `--r-globalnav-flyout-spacing` | `88px` |
| `--r-globalnav-next-flyout-height` | `0px` |
| `--r-globalnav-previous-flyout-height` | `0px` |
| `--r-globalnav-height` | `44px` |
| `--r-globalnav-color` | `rgba(0, 0, 0, .8)` |
| `--r-globalnav-color-secondary` | `#333336` |
| `--r-globalnav-color-hover` | `#000000` |
| `--r-globalnav-font-size` | `17px` |
| `--globalnav-background` | `none` |
| `--globalnav-backdrop-filter` | `none}#globalnav.globalnav-dark,#globalnav.globalheader-dark,` |
| `--r-globalnav-color-secondary` | `#E8E8ED` |
| `--r-globalnav-color-hover` | `#FFFFFF}#globalnav.globalnav-light,#globalnav.globalheader-l` |
| `--r-globalnav-color-secondary` | `#333336` |
| `--r-globalnav-color-hover` | `#000000}#globalnav{position:absolute` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `rebrand-localnav` | `localnav localnav--custom-background css-sticky rebrand-localnav` |
| `<nav>` | `-` | `ac-gf-breadcrumbs sa-breadcrumbs` |
| `<main>` | `-` | `page-content` |
| `<footer>` | `ac-globalfooter` | `js sa-footer rebrand-footer` |
