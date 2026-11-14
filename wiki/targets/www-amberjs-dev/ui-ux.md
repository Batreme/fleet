---
title: "UI & Design System: www-amberjs-dev"
date: 2026-11-14
target: "[[overview|www-amberjs-dev]]"
---

# UI Architecture & Design Tokens: www-amberjs-dev

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--link-arrow-color` | `#fff}.proto-header nav .has-link-arrow,.footer-copy nav .has` |
| `--camera-exit` | `0` |
| `--camera-entry` | `1` |
| `--camera-focus-scale` | `1.3` |
| `--camera-focus-opacity` | `0` |
| `--camera-inset-x` | `3.2vw` |
| `--camera-inset-top` | `max(28px, env(safe-area-inset-top))` |
| `--camera-inset-bottom` | `max(28px, env(safe-area-inset-bottom))` |
| `--camera-inset-x` | `6vw}.camera-frame-graphics{font-size:10px}.camera-focus{widt` |
| `--sans` | `"Instrument Sans Variable",sans-serif` |
| `--serif` | `"Instrument Serif",serif` |
| `--mono` | `"Fragment Mono",monospace` |
| `--paper` | `#fcfbf8` |
| `--ink` | `#101010` |
| `--red` | `#cf001c` |
| `--muted` | `#767570` |
| `--line` | `#e0dfd9` |
| `--gutter` | `clamp(20px,4.2vw,78px)` |
| `--header-top` | `32px` |
| `--header-logo-size` | `49px` |
| `--ink` | `#f2f0eb` |
| `--muted` | `#aaa7a0` |
| `--line` | `#ffffff24` |
| `--red` | `#ee354e` |
| `--control-ease` | `cubic-bezier(.22,1,.36,1)` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `` |
| `<nav>` | `-` | `box-nav` |
| `<nav>` | `-` | `footprint-package-links` |
| `<nav>` | `-` | `full-circle-links` |
| `<nav>` | `-` | `book-mobile-controls` |
| `<header>` | `-` | `home-header` |
| `<header>` | `-` | `footprint-header` |
| `<main>` | `app` | `` |
| `<footer>` | `-` | `home-baseline` |
| `<footer>` | `-` | `footprint-footer` |
| `<footer>` | `-` | `full-circle-baseline` |
| `<dialog>` | `docs-dialog` | `docs-dialog` |
