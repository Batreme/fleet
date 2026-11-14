---
title: "UI & Design System: errormade-tech"
date: 2026-11-14
target: "[[overview|errormade-tech]]"
---

# UI Architecture & Design Tokens: errormade-tech

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--mobile-footer-bottom` | `calc(12px + var(--safe-bottom))` |
| `--grid-gap` | `6px` |
| `--column` | `calc((100vw - 2 * var(--page-margin) - 5 * var(--grid-gap)) ` |
| `--header-content-gap` | `12px` |
| `--media-column` | `calc(2.5 * var(--column) + 1.5 * var(--grid-gap))` |
| `--title-band-clearance` | `24px` |
| `--title-band-feed-gap` | `12px` |
| `--title-band-footer-gap` | `64px` |
| `--case-ruler-top` | `calc(115px + var(--safe-top))` |
| `--case-end-gap` | `200px` |
| `--case-step-height` | `200px` |
| `--case-header-width` | `calc((100vw - 2 * var(--page-margin) - 2 * var(--grid-gap)) ` |
| `--case-progress-ease` | `cubic-bezier(.22, 1, .36, 1)` |
| `--case-divider-color` | `rgb(255 255 255 / 15%)` |
| `--case-divider-color` | `var(--rule)` |
| `--case-end-gap` | `0px` |
| `--case-preview-width` | `48px` |
| `--case-preview-duration` | `450ms` |
| `--case-preview-hidden` | `inset(100% 0 0 0)` |
| `--case-ruler-weight` | `2` |
| `--case-ruler-weight` | `2` |
| `--case-step-duration` | `420ms` |
| `--case-step-reveal` | `0` |
| `--case-step-preview-height` | `24px` |
| `--case-step-reveal` | `1` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `main-nav` |
| `<nav>` | `-` | `social-nav` |
| `<header>` | `-` | `site-header header-motion-ready` |
| `<aside>` | `-` | `site-utilities` |
| `<aside>` | `-` | `work-title-band` |
| `<main>` | `works` | `works gallery-view` |
| `<footer>` | `-` | `site-footer` |
