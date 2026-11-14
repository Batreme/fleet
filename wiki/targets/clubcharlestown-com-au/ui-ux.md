---
title: "UI & Design System: clubcharlestown-com-au"
date: 2026-11-14
target: "[[overview|clubcharlestown-com-au]]"
---

# UI Architecture & Design Tokens: clubcharlestown-com-au

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--e-off-canvas-width` | `400px` |
| `--e-off-canvas-height` | `100vh` |
| `--e-off-canvas-justify-content` | `flex-start` |
| `--e-off-canvas-align-items` | `flex-start` |
| `--e-off-canvas-animation-duration` | `1.5s` |
| `--e-off-canvas-content-overflow` | `auto` |
| `--e-off-canvas-overlay-opacity` | `1` |
| `--e-off-canvas-animation-duration-minimum` | `Max(0.001s,var(--e-off-canvas-animation-duration))}.elemento` |
| `--kit-widget-spacing` | `0px}body:not(.elementor-editor-active) .elementor-section .e` |
| `--display` | `flex` |
| `--flex-direction` | `row` |
| `--container-widget-width` | `calc( ( 1 - var( --container-widget-flex-grow ) ) * 100% )` |
| `--container-widget-height` | `100%` |
| `--container-widget-flex-grow` | `1` |
| `--container-widget-align-self` | `stretch` |
| `--flex-wrap-mobile` | `wrap` |
| `--justify-content` | `space-between` |
| `--align-items` | `center` |
| `--e-icon-list-icon-size` | `14px` |
| `--icon-vertical-offset` | `0px` |
| `--display` | `flex` |
| `--flex-direction` | `row` |
| `--container-widget-width` | `calc( ( 1 - var( --container-widget-flex-grow ) ) * 100% )` |
| `--container-widget-height` | `100%` |
| `--container-widget-flex-grow` | `1` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `e-n-menu` |
| `<header>` | `-` | `elementor elementor-27 elementor-location-header` |
| `<main>` | `content` | `site-main post-7 page type-page status-publish hentry` |
| `<footer>` | `-` | `elementor elementor-63 elementor-location-footer` |
