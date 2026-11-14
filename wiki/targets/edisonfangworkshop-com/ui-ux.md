---
title: "UI & Design System: edisonfangworkshop-com"
date: 2026-11-14
target: "[[overview|edisonfangworkshop-com]]"
---

# UI Architecture & Design Tokens: edisonfangworkshop-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--menu-control-gap` | `10px` |
| `--menu-control-stop` | `calc(var(--menu-control-gap) - 1px)` |
| `--menu-control-gap` | `8px` |
| `--lightningcss-light` | `initial` |
| `--lightningcss-dark` | `` |
| `--size` | `340px` |
| `--case-depth` | `11.9px` |
| `--case-half` | `5.95px` |
| `--shelf-footer-height` | `calc(26px + env(safe-area-inset-bottom,0px))` |
| `--exchange-size` | `min(36vw,260px,42dvh)` |
| `--exchange-direction` | `1` |
| `--exchange-direction` | `-1}.edition-exchange[data-suspended=true],.edition-exchange[` |
| `--tray-close-duration` | `.4s` |
| `--tray-close-delay` | `.65s}.edition-exchange .exchange-in{--tray-open-duration:.7s` |
| `--tray-close-delay` | `.45s` |
| `--tray-close-duration` | `.5s}.edition-exchange[data-collection=false] .edition-exchan` |
| `--leaf-angle` | `90deg` |
| `--leaf-angle` | `-90deg` |
| `--tray-close-duration` | `.47s` |
| `--tray-close-delay` | `.845s}.edition-exchange[data-collection=false] .exchange-in{` |
| `--nf-ink` | `#171814` |
| `--nf-paper` | `#fff` |
| `--nf-accent` | `#ad573f` |
| `--mood-line` | `color-mix(in srgb,var(--mood-fg) 30%,transparent)}html[data-` |
| `--project-text` | `var(--mood-fg)` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `collection-menu-navigation` |
| `<header>` | `-` | `portfolio-header smart-header` |
| `<header>` | `-` | `collection-menu-masthead` |
| `<aside>` | `-` | `home-formation-rail` |
| `<main>` | `-` | `portfolio-home unreleased-home home-poster` |
| `<footer>` | `-` | `collection-menu-footer` |
| `<footer>` | `-` | `portfolio-footer unreleased-footer home-studio-footer` |
| `<dialog>` | `_R_12q56_` | `collection-menu-dialog` |
