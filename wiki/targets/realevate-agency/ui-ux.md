---
title: "UI & Design System: realevate-agency"
date: 2026-11-14
target: "[[overview|realevate-agency]]"
---

# UI Architecture & Design Tokens: realevate-agency

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--brand-navy` | `#1F2B5E` |
| `--navy` | `var(--brand-navy)` |
| `--muted` | `#626C95` |
| `--white` | `#FFFFFF` |
| `--category-color-light` | `var(--white)` |
| `--category-by-the-sea-color` | `#222A4C` |
| `--category-by-the-sea-muted` | `#5D668D` |
| `--category-evergreen-color` | `#36614D` |
| `--category-evergreen-muted` | `#80988E` |
| `--category-urban-living-color` | `#2D1C2D` |
| `--category-urban-living-muted` | `#6B5A6B` |
| `--category-rare-gems-color` | `#1C181D` |
| `--category-rare-gems-muted` | `#5C585D` |
| `--custom-scrollbar-thumb-color` | `var(--muted)` |
| `--sans-font` | `"Google Sans", Arial, Helvetica, sans-serif` |
| `--display-font` | `"Roslindale Display", Georgia, "Times New Roman", serif` |
| `--standard-easing` | `cubic-bezier(.7, .6, 0, 1)` |
| `--cta-motion-easing` | `cubic-bezier(.7, .6, 0, 1)` |
| `--overlay-duration` | `.8s` |
| `--body-leading` | `1.35` |
| `--underline-offset` | `-.3em` |
| `--desktop-size-scale` | `1` |
| `--tablet-size-scale` | `1.54` |
| `--mobile-size-scale` | `2.25` |
| `--responsive-size-scale` | `var(--desktop-size-scale)` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `selection-menu` | `` |
| `<nav>` | `-` | `site-nav` |
| `<nav>` | `-` | `nav-menu__links` |
| `<header>` | `-` | `logo` |
| `<main>` | `-` | `` |
| `<footer>` | `-` | `site-footer` |
