---
title: "UI & Design System: pixlpin-com_designs"
date: 2026-11-14
target: "[[overview|pixlpin-com_designs]]"
---

# UI Architecture & Design Tokens: pixlpin-com_designs

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--view-cols` | `2` |
| `--view-col-w` | `calc((100cqw - (var(--view-cols) - 1) * var(--grid-gap)) / v` |
| `--lead-span` | `var(--shape-span)` |
| `--lead-main` | `calc(var(--stage-h) + var(--grid-gap))` |
| `--span-wide` | `var(--view-cols)` |
| `--span-narrow` | `var(--view-cols)` |
| `--shape-span` | `calc(var(--span-wide) - var(--lead-alt,0) * (var(--span-wide` |
| `--shape-w` | `calc(var(--shape-span) * var(--view-col-w) + (var(--shape-sp` |
| `--fit-w` | `var(--shape-w)` |
| `--stage-w` | `var(--shape-w)` |
| `--stage-h` | `min(var(--fit-w) * var(--media-hw), var(--stage-cap))` |
| `--stage-cap` | `calc(100svh - var(--stage-room) + var(--lead-alt,0) * 1000sv` |
| `--stage-w` | `100cqw` |
| `--stage-cap` | `calc(100svh - var(--stage-room-row))}.design-view--row{--lea` |
| `--button-shadow` | `var(--shadow-s)}.design-view__bar{padding-bottom:var(--space` |
| `--view-cols` | `3}.design-view--portrait,.design-view__stage--portrait,.desi` |
| `--span-narrow` | `1}.design-view--landscape,.design-view__stage--landscape{--s` |
| `--view-cols` | `4}.design-view--square,.design-view__stage--square{--span-wi` |
| `--span-narrow` | `2}}@media not (min-width:768px){.design-view{--view-bleed:ca` |
| `--shape-w` | `calc(100cqw + 2 * var(--view-bleed))` |
| `--stage-room` | `calc(var(--topbar-height) + var(--space-2))}.design-view--ro` |
| `--button-bg` | `var(--color-glass)` |
| `--color-bg` | `var(--color-toast-bg)` |
| `--color-text` | `var(--color-toast-text)` |
| `--color-text-muted` | `var(--color-toast-text-muted)` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `category-nav` |
| `<nav>` | `-` | `shell-panel__legal` |
| `<header>` | `-` | `top-bar` |
| `<header>` | `-` | `sidebar` |
| `<header>` | `-` | `grid-header grid-header--pills-first` |
| `<main>` | `main` | `app-shell__main app-shell__main--docked` |
| `<footer>` | `-` | `shell-footer` |
| `<dialog>` | `-` | `drawer` |
| `<dialog>` | `-` | `palette` |
