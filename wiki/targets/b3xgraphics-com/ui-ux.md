---
title: "UI & Design System: b3xgraphics-com"
date: 2026-11-14
target: "[[overview|b3xgraphics-com]]"
---

# UI Architecture & Design Tokens: b3xgraphics-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--b3xh-side` | `clamp(20px,2.2vw,50px)` |
| `--b3xh-max` | `1820px` |
| `--b3xh-sky` | `#04b5ff` |
| `--b3xh-glass` | `linear-gradient(155deg,rgba(9,26,54,0.66) 0%,rgba(3,13,30,0.` |
| `--PhoneInput-color--focus` | `#03b2cb` |
| `--PhoneInputInternationalIconPhone-opacity` | `0.8` |
| `--PhoneInputInternationalIconGlobe-opacity` | `0.65` |
| `--PhoneInputCountrySelect-marginRight` | `0.35em` |
| `--PhoneInputCountrySelectArrow-width` | `0.3em` |
| `--PhoneInputCountrySelectArrow-marginLeft` | `var(--PhoneInputCountrySelect-marginRight)` |
| `--PhoneInputCountrySelectArrow-borderWidth` | `1px` |
| `--PhoneInputCountrySelectArrow-opacity` | `0.45` |
| `--PhoneInputCountrySelectArrow-color` | `currentColor` |
| `--PhoneInputCountrySelectArrow-color--focus` | `var(--PhoneInput-color--focus)` |
| `--PhoneInputCountrySelectArrow-transform` | `rotate(45deg)` |
| `--PhoneInputCountryFlag-aspectRatio` | `1.5` |
| `--PhoneInputCountryFlag-height` | `1em` |
| `--PhoneInputCountryFlag-borderWidth` | `1px` |
| `--PhoneInputCountryFlag-borderColor` | `rgba(0,0,0,.5)` |
| `--PhoneInputCountryFlag-borderColor--focus` | `var(--PhoneInput-color--focus)` |
| `--PhoneInputCountryFlag-backgroundColor--loading` | `rgba(0,0,0,.1)}
:root{--wp--preset--aspect-ratio--square: 1` |
| `--wp--preset--aspect-ratio--4-3` | `4/3` |
| `--wp--preset--aspect-ratio--3-4` | `3/4` |
| `--wp--preset--aspect-ratio--3-2` | `3/2` |
| `--wp--preset--aspect-ratio--2-3` | `2/3` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `b3xhNav` | `b3xh-nav` |
| `<header>` | `b3xhBar` | `b3xh-bar` |
| `<main>` | `content` | `site-main post-1301 page type-page status-publish hentry` |
| `<footer>` | `-` | `site-footer` |
