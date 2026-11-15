---
title: "UI & Design System: www-anduril-com"
date: 2026-11-15
target: "www-anduril-com"
---

# UI Architecture & Design Tokens: www-anduril-com

> Ground-truth CSS custom properties and DOM layout primitives extracted from `www-anduril-com` (`Anduril Industries · Transforming U.S. Defense Capabilities with Advanced Technology`). All values are sanitized, deduplicated, and mapped to their semantic UI roles. Also see [UI Prompt Blueprint](prompt-blueprint.md).

## 🎨 Design Tokens (CSS Variables)

| Token Name | Extracted Value | Semantic UI Role |
|---|---|---|
| `--is-mob` | `0` | Viewport breakpoint flag (switches to `1` at `max-width: 768px`) |
| `--theme-color-background` | `#010101` | Primary stealth carbon background surface |
| `--theme-color-text` | `#fff` | Primary high-contrast text ink |
| `--base-color` | `black` | Base substrate color keyword |
| `--contrast-color` | `white` | High-contrast foreground keyword |
| `--linkbutton-color` | `#fff` | Default `.LinkButton` & `.CircleButton` foreground |
| `--linkbutton-hover-color` | `#010101` | Inverted button label ink on hover fill |
| `--roller-scale` | `1` | Scale multiplier for mechanical odometer counters |
| `--roller-font-size` | `calc(3rem*var(--roller-scale))` | Odometer digit font size |
| `--roller-column-height` | `calc(2.5rem*var(--roller-scale))` | Odometer vertical slot height |
| `--roller-digit-width` | `calc(1.8rem*var(--roller-scale))` | Odometer fixed monospace digit width |
| `--links-height` | `0px` | Collapsible navigation submenu height state |
| `--frosted` | `0` | Header backdrop frosted glass state toggle |
| `--backgroundOpacity` | `0` | Dynamic scroll overlay opacity value |
| `--in-production-h` | `max(505px,100vw*505/403)` | Responsive aspect-ratio height for production showcase |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<header>` | `-` | `header` |
| `<nav>` | `-` | `HeaderDesktop` |
| `<nav>` | `-` | `HeaderMobile lenis` |
| `<main>` | `-` | `-` |
| `<footer>` | `-` | `Footer` |
