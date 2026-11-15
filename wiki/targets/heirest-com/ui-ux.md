# UI & UX Architecture: heirest-com

## Overview & Design Identity
- **Target**: `heirest-com` (**HEIREST · Fine Jewellery, Authored By You**)
- **Production URL**: [https://heirest.com/](https://heirest.com/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#DFDFDF` canvas, `#000000` ink, `#ffffff` accent)
- **Summary**: Fine jewellery for those who choose to author what others inherit. Configured by you and crafted to last.
- **Total Clean CSS Variables Extracted**: `1464` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Moderat-Regular`
- **Monospace / Technical Font Stack**: `ModeratMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--loyalty-shimmer-display: none`, `--font-h1--spacing: var(--font-heading--spacing)`, `--font-h1--color: var(--color-foreground-heading)`; rule `h1` (`line-height: var(--line-height--di...`)
- **Section Heading (`H2`)**: CSS variables `--loyalty-banner-subtitle-size: 14px`, `--font-h2--spacing: var(--font-heading--spacing)`, `--font-h2--color: var(--color-foreground-heading)`; rule `h2` (`font-size: var(--heading-font-size)`, `font-weight: var(--heading...`)
- **Body Copy**: CSS variables `--paragraph-color: #202020`, `--paragraph-font-size: 16px`, `--paragraph-font-weight: 400`; rule `p` (`line-height: var(--line-height--bo...`)
- **Metadata & Labels**: CSS variables `--default-mono-font-family: var(--font-mono)`, `--bundle-product-label-color: #000000`, `--bundle-product-label-size: 16px`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#DFDFDF` | `var(--accordion-border-color)` in `:root` |
| **Primary Typography Ink** | `#f9f8f6` | `var(--product-image-tint)` in `:root` |
| **Elevated Surface / Card Substrate** | `#000000` | `var(--bundle-component-title-color)` in `:root` |
| **Interactive Accent / Highlight** | `#ffffff` | `var(--bundle-component-background)` in `:root` |
| **Secondary / Muted Copy** | `#cccccc` | `var(--bundle-option-border-color)` in `:root` |
| **Structural Hairline Border** | `#202020` | `var(--paragraph-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--hover-lift-amount` | `4px` | Dimension / Scale Token |
| `--hover-scale-amount` | `1.03` | Design System Custom Token |
| `--hover-subtle-zoom-amount` | `1.015` | Design System Custom Token |
| `--hover-shadow-color` | `var(--color-shadow)` | Brand / Palette Token |
| `--hover-transition-duration` | `var(--global-transition-duration)` | Motion / Easing Token |
| `--hover-transition-timing` | `var(--global-transition-timing-function)` | Motion / Easing Token |
| `--surface-transition-duration` | `var(--global-transition-duration)` | Canvas / Surface Token |
| `--surface-transition-timing` | `var(--global-transition-timing-function)` | Canvas / Surface Token |
| `--submenu-animation-speed` | `.36s` | Motion / Easing Token |
| `--submenu-animation-easing` | `cubic-bezier(.25, .1, .25, 1)` | Motion / Easing Token |
| `--icon-stroke-width` | `1px` | Layout / Spatial Grid Token |
| `--backdrop-color-rgb` | `var(--color-shadow-rgb)` | Brand / Palette Token |
| `--page-margin` | `16px` | Layout / Spatial Grid Token |
| `--full-page-grid-margin` | `minmax(var(--page-margin), 1fr)` | Layout / Spatial Grid Token |
| `--full-page-margin-inline-offset` | `calc(((100vw - var(--full-page-grid-central-column-width)) / 2) * -1)` | Layout / Spatial Grid Token |
| `--dot-size` | `var(--section-dot-size, 1.5px)` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.shopify-section> — `heirest-com`)**:
   - Landmark `<header class="shopify-section shopify-section-group-header-group">` hosting `HEIREST · Fine Jewellery, Authored B` navigation (`Bespoke · Our Standards · Sizing Kits`), DOM attributes (`data-swym-guest-login-bound="1"`, `data-source-attribution="shopify.exit_intersti..."`, `data-source-attribution="shopify.event_observe..."`, `data-shopify`), and stylesheet rule `body { scrollbar-width:none;-ms-overflow-style:none }`.
2. **Hero Stage & Focal Lead (<section.shopify-pc__banner__dialog> — `Cookie consent`)**:
   - Landmark `<section class="shopify-pc__banner__dialog">` presenting display lead `Cookie consent` and copy excerpt *"cookies are used on this site. Privacy Policy"* over `#DFDFDF` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.shopify-section> — `Your Cart Your cart is empty`)**:
   - Landmark `<section class="shopify-section shopify-section-group-header-group">` rendering section `Your Cart Your cart is empty` with copy *"SHOP THE HEIREST SIZING KIT · ONLY $19 + FREE SHIPPING SHOP THE H"*, asset references (`clarity.js`, `y0e70x819z`, `gtm.js`, `cdn.shopify.com`), and grid rule `body::-webkit-scrollbar { width:0;height:0;display:none }`.
4. **Interactive Detail & Feature Matrix (<section.shopify-section> — `Subscribe to our newsletter`)**:
   - Landmark `<section class="shopify-section shopify-section-group-header-group">` framing `Subscribe to our newsletter` and `Slideshow` (*"SHOP THE HEIREST SIZING KIT · ONLY $19 + FREE SHIPPING"*) with `#000000` surface cards, `#ffffff` accents, and `svg { display:block;max-width:100% }`.
5. **Colophon & Global Directory Footer (<footer.announcement-bar--show> — `https://heirest.com/`)**:
   - Landmark `<footer class="announcement-bar--show">` anchoring `HEIREST · Fine Jewellery, Author` footer links (`Bespoke · Our Standards · Sizing Kits`), copy *"Translation missing: en.localization.currency_label AED AUD "*, and `#202020` structural dividers.
