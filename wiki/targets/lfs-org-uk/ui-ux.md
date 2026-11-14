---
title: "UI & Design System: lfs-org-uk"
date: 2026-11-14
target: "[[overview|lfs-org-uk]]"
---

# UI Architecture & Design Tokens: lfs-org-uk

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--cc-font-family` | `-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica` |
| `--cc-modal-border-radius` | `.5rem` |
| `--cc-btn-border-radius` | `.4rem` |
| `--cc-modal-transition-duration` | `.25s` |
| `--cc-link-color` | `var(--cc-btn-primary-bg)` |
| `--cc-modal-margin` | `1rem` |
| `--cc-z-index` | `2147480000` |
| `--cc-bg` | `#fff` |
| `--cc-primary-color` | `#2c2f31` |
| `--cc-secondary-color` | `#5e6266` |
| `--cc-btn-primary-bg` | `#30363c` |
| `--cc-btn-primary-color` | `#fff` |
| `--cc-btn-primary-border-color` | `var(--cc-btn-primary-bg)` |
| `--cc-btn-primary-hover-bg` | `#000` |
| `--cc-btn-primary-hover-color` | `#fff` |
| `--cc-btn-primary-hover-border-color` | `var(--cc-btn-primary-hover-bg)` |
| `--cc-btn-secondary-bg` | `#eaeff2` |
| `--cc-btn-secondary-color` | `var(--cc-primary-color)` |
| `--cc-btn-secondary-border-color` | `var(--cc-btn-secondary-bg)` |
| `--cc-btn-secondary-hover-bg` | `#d4dae0` |
| `--cc-btn-secondary-hover-color` | `#000` |
| `--cc-btn-secondary-hover-border-color` | `#d4dae0` |
| `--cc-separator-border-color` | `#f0f4f7` |
| `--cc-toggle-on-bg` | `var(--cc-btn-primary-bg)` |
| `--cc-toggle-off-bg` | `#667481` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `primary-nav js-menu` |
| `<header>` | `-` | `header js-header` |
| `<aside>` | `-` | `video-overlay js-overlay` |
| `<main>` | `-` | `site-wrapper` |
| `<footer>` | `-` | `footer grid-container` |
