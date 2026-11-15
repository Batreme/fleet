# UI & UX Architecture: almadalabel-com

## Overview & Design Identity
- **Target**: `almadalabel-com` (**ALMADA LABEL - A modern take on a seasonless wardrobe**)
- **Production URL**: [https://almadalabel.com/](https://almadalabel.com/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#17140f` ink, `#a6a6a5` accent)
- **Summary**: Seasonless modern wardrobe staples designed with Scandinavian minimalism, resonating beyond trends. Responsibly crafted from high-quality...
- **Total Clean CSS Variables Extracted**: `101` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Heading Font Italic`
- **Body Font Stack**: `Heading Font Regular`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 32px`, `line-height: normal`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: .875rem`, `line-height: 1.125rem`, `letter-spacing: 0`, `font-weight: 400`)
- **Body Copy**: CSS variables `--body_color: #FFF`, `--type_primary_paragraph_font: 'Paragraph Primary Font'`, `--weight_paragraph_font: 400`; rule `p` (`font-size: .75rem`, `line-height: 1.125rem`, `letter-spacing: 0`)
- **Metadata & Labels**: CSS variables `--mobile-menu-label-gap: .375rem`, `--label_onSale_Bg: #A6A6A5`, `--label_onSale_text: #A6A6A5`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | `var(--background_color)` in `:root` |
| **Primary Typography Ink** | `#f3f2f2` | `var(--background_color_2)` in `:root` |
| **Elevated Surface / Card Substrate** | `#17140f` | `var(--primary_text)` in `:root` |
| **Interactive Accent / Highlight** | `#a6a6a5` | `var(--primary_accent)` in `:root` |
| **Secondary / Muted Copy** | `#38302e` | `var(--secondary_accent)` in `:root` |
| **Structural Hairline Border** | `#55534e` | `var(--primary_gray)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--adjustment_m` | `0px` | Dimension / Scale Token |
| `--adjustment_d` | `0px` | Dimension / Scale Token |
| `--pc-indicator-h` | `0px` | Dimension / Scale Token |
| `--pc-slide-base` | `200%` | Dimension / Scale Token |
| `--favorites-drawer-inline-padding` | `1.25rem` | Layout / Spatial Grid Token |
| `--favorites-recent-swiper-inline-offset` | `16px` | Dimension / Scale Token |
| `--favorites-recent-skeleton-per-view` | `2.476` | Design System Custom Token |
| `--favorites-recent-skeleton-gap` | `1rem` | Layout / Spatial Grid Token |
| `--mobile-menu-label-gap` | `.375rem` | Layout / Spatial Grid Token |
| `--aspect-ratio` | `.75` | Design System Custom Token |
| `--Drawer-bg` | `var(--background_color)` | Canvas / Surface Token |
| `--background_color` | `#ffffff` | Canvas / Surface Token |
| `--background_color_2` | `#f3f2f2` | Canvas / Surface Token |
| `--primary_text` | `#17140f` | Typography Ink Token |
| `--secondary_text` | `#ffffff` | Typography Ink Token |
| `--primary_accent` | `#a6a6a5` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.Drawer__header> — `almadalabel-com`)**:
   - Landmark `<header class="Drawer__header">` hosting `ALMADA LABEL - A modern take on a se` navigation (`Journal · New Arrivals · Coming Soon · Belts New · Signatures`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-shop-id="25465225306"`, `data-venmo-supported="false"`, `data-environment="production"`), and stylesheet rule `.shopify-payment-button__button--... { visibility:hidden }`.
2. **Hero Stage & Focal Lead (<article.favorites-drawer__item> — `Wishlist`)**:
   - Landmark `<article class="favorites-drawer__item">` presenting display lead `Wishlist` and copy excerpt *"Free shipping to Finland on orders over 300€"* over `#ffffff` canvas and `#17140f` ink.
3. **Primary Showcase & Content Grid (<article.favorites-drawer__item> — `ALMADA`)**:
   - Landmark `<article class="favorites-drawer__item">` rendering section `ALMADA` with copy *"Search Wishlist Cart 0"*, asset references (`trsdk`, `clarity.js`, `vwmug8kkd7`, `cdn.shopify.com`), and grid rule `opify-payment-button__button--unb... { background-color:1990c6;padding:1em 2em }`.
4. **Interactive Detail & Feature Matrix (<article.favorites-drawer__item> — `Search`)**:
   - Landmark `<article class="favorites-drawer__item">` framing `Search` and `JOIN OUR MAILING LIST` (*"Autumn / Winter 26"*) with `#17140f` surface cards, `#a6a6a5` accents, and `ptions.shopify-payment-button__sk... { width:50%;margin-left:25%;margin-right:25%;border-radius:4px!important;h... }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://almadalabel.com/`)**:
   - Landmark `<footer class="footer colorGroup--primary">` anchoring `ALMADA LABEL - A modern take on ` footer links (`Journal · New Arrivals · Coming Soon · Belts New · Signatures`), copy *"Silk Wool Cashmere"*, and `#55534e` structural dividers.
