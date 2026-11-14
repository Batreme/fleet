---
title: "UI & Design System: bybang-co"
date: 2026-11-14
target: "[[overview|bybang-co]]"
---

# UI Architecture & Design Tokens: bybang-co

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--bg` | `#f5f5f2` |
| `--panel` | `#e1e1e1` |
| `--panel-dark` | `#d7d7d0` |
| `--text` | `#141414` |
| `--muted` | `rgba(20, 20, 20, .3)` |
| `--border` | `rgba(20, 20, 20, .08)` |
| `--accent` | `#946ec4` |
| `--shadow` | `0 24px 80px rgba(11, 12, 11, .12)` |
| `--mono` | `"Geist Mono", ui-monospace, monospace` |
| `--sans` | `"Geist", "Helvetica Neue", Arial, sans-serif` |
| `--stable-viewport-height` | `100vh}*{box-sizing:border-box}::selection{background:#000` |
| `--not-found-row-height` | `clamp(50px, 5.28vw, 76px)` |
| `--not-found-type-size` | `clamp(48px, 5.14vw, 74px)` |
| `--not-found-row-height` | `clamp(38px, 10.2vw, 56px)` |
| `--not-found-type-size` | `clamp(36px, 10vw, 54px)}.not-found__footer{bottom:20px` |
| `--site-bg` | `#ffffff` |
| `--site-ink` | `#141414` |
| `--site-muted` | `rgba(20, 20, 20, .3)` |
| `--site-faint` | `rgba(20, 20, 20, .2)` |
| `--site-grid-edge` | `32px` |
| `--site-grid-gap` | `32px` |
| `--site-card-shadow` | `442px 694px 231px rgba(0, 0, 0, 0), 283px 444px 211px rgba(0` |
| `--site-card-shadow-muted` | `442px 694px 231px rgba(0, 0, 0, 0), 283px 444px 211px rgba(0` |
| `--intro-loader-mark-scale` | `1.872` |
| `--intro-loader-media-size` | `min(217px, calc((100vw - 64px)*.448) )` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `site-nav site-nav--home` |
| `<header>` | `-` | `site-chrome` |
| `<main>` | `-` | `site-home` |
