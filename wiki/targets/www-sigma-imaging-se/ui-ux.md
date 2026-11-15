---
title: "UI & Design System: www-sigma-imaging-se"
date: 2026-11-15
target: "[[overview|www-sigma-imaging-se]]"
---

# UI Architecture & Design Tokens: www-sigma-imaging-se

> Ground-truth CSS custom properties and DOM layout primitives extracted from `www-sigma-imaging-se` (`SIGMA Imaging Nordics & Baltics · Optical Lenses, Cameras & Cine-Lenses`). All values are sanitized, deduplicated, and mapped to their semantic UI roles. Also see [[prompt-blueprint|UI Prompt Blueprint]].

## 🎨 Design Tokens (CSS Variables)

| Token Name | Extracted Value | Semantic UI Role |
|---|---|---|
| `--ps-white` | `#fefefd` | Primary optical white substrate |
| `--ps-tint` | `#f7f7f7` | Secondary product card tint surface |
| `--ps-text` | `#333` | Primary charcoal typography ink |
| `--ps-text-muted` | `rgba(51, 51, 51, 0.5)` | Muted technical specification ink |
| `--ps-font-ui` | `"Sigma Sans", sans-serif` | Primary technical UI & lens designation font |
| `--ps-font-body` | `"Sigma Serif", serif` | Editorial monograph & body serif font |
| `--snap-cols` | `1` | Responsive scroll-snap column divisor |
| `--snap-gap` | `1rem` | Scroll-snap grid gutter spacing |
| `--snap-size` | `calc((100% - var(--snap-gap)*(var(--snap-cols) - 1))/var(--snap-cols))` | Dynamic card width calculation |
| `--ammenu-main-menu-background` | `#fefefd` | Header mega-menu background |
| `--ammenu-main-menu-text` | `#333333` | Header navigation link ink |
| `--ammenu-submenu-text-hover` | `#4d4d4d` | Submenu hover ink state |
| `--ammenu-border` | `#757575` | Navigation structural divider color |
| `--amcart-background` | `#FFFFFF` | Cart drawer background surface |
| `--amcart-product-name` | `#000000` | Cart product title ink |
| `--amscroll--transition-duration` | `.2s` | Fast UI transition duration |
| `--amscroll--hover-filter` | `brightness(.8)` | Optical image hover darkening filter |
| `--amscroll-border-color` | `#cccfd6` | Card & pagination border token |
| `--ambar-toggle-active-color` | `#2563eb` | Active interactive toggle accent |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<header>` | `ammenu-header-container` | `ammenu-header-container page-header` |
| `<header>` | `-` | `relative p-4` |
| `<header>` | `-` | `relative p-4 flex items-center justify-between` |
| `<nav>` | `-` | `navigation sr-only` |
| `<nav>` | `-` | `-` |
| `<nav>` | `am-account-menu` | `flex flex-col` |
| `<main>` | `maincontent` | `page-main` |
| `<section>` | `-` | `message global noscript border-b-2 border-blue-500 bg-blue-5` |
| `<section>` | `cart-drawer` | `-` |
| `<section>` | `search-drawer` | `-` |
| `<section>` | `store-switcher-drawer` | `-` |
| `<section>` | `customer-drawer` | `-` |
| `<section>` | `messages` | `-` |
| `<section>` | `-` | `-` |
