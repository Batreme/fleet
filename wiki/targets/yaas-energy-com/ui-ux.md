---
title: "UI & Design System: yaas-energy-com"
date: 2026-11-14
target: "[[overview|yaas-energy-com]]"
---

# UI Architecture & Design Tokens: yaas-energy-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--font-display` | `"Soledago", "Arial Narrow", system-ui, -apple-system, sans-s` |
| `--font-body` | `"Helvetica Neue", Arial, system-ui, -apple-system, sans-seri` |
| `--font-beiruti` | `"Bounded", "Helvetica Neue", Arial, system-ui, -apple-system` |
| `--ui-scale` | `1` |
| `--ink` | `#ffffff` |
| `--ink-soft` | `rgba(255, 255, 255, .85)` |
| `--ink-on-light` | `#212121` |
| `--ink-on-light-soft` | `rgba(33, 33, 33, .72)` |
| `--block-gap` | `calc(120px * var(--ui-scale))` |
| `--heading-gap` | `50px` |
| `--block-heading` | `clamp(30px, 4.17vw, calc(80px * var(--ui-scale)))` |
| `--text-body` | `calc(16px * var(--ui-scale))` |
| `--text-body-sm` | `calc(14px * var(--ui-scale))` |
| `--content-gutter` | `30px` |
| `--content-inline` | `var(--content-gutter)` |
| `--paper` | `#fdfaf1` |
| `--bg-color` | `#f3d118` |
| `--block-gap` | `80px` |
| `--block-gap-bottom` | `calc(var(--block-gap) + 40px)` |
| `--content-gutter` | `10px` |
| `--block-heading` | `clamp(30px, 10.26vw, 40px)}}@media (min-width: 960px) and (m` |
| `--content-inline` | `var(--hero-margin, var(--content-gutter))}}@media (min-width` |
| `--h2g` | `0}.hero-gradient-wrap{z-index:0}.app-root{position:absolute` |
| `--arrow-scale` | `1` |
| `--arrow-scale` | `1.08}.arrow-left{--ox: -10.5vw}.arrow-right{--ox: 10.5vw}.fl` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `hero-nav` |
| `<nav>` | `-` | `site-footer-nav` |
| `<footer>` | `-` | `site-footer is-reveal` |
