# UI & UX Architecture: www-feelreformed-com

## Overview & Design Identity
- **Target**: `www-feelreformed-com` (**Reformed: The biggest thing to happen to Coffee since Coffee.**)
- **Production URL**: [https://www.feelreformed.com/](https://www.feelreformed.com/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#FAFBFF`)
- **Summary**: Reformed: Arabica coffee and ceremonial matcha, enriched with functionality: collagen or creatine, adaptogens and twenty-one vitamins.
- **Total Clean CSS Variables Extracted**: `1313` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Chivo`
- **Body Font Stack**: `Hanken Grotesk`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--header-logo-display: none`, `--header-logo-inverse-display: block`, `--x-shell-disclosure-display: block`; rule `h1` (`line-height: var(--line-height--di...`)
- **Section Heading (`H2`)**: CSS variables `--font-h2--spacing: 0.25em`, `--font-h2--color: var(--color-foreground-heading)`, `--font-size--h2: clamp(1.75rem, 4.8vw, 3.0rem)`; rule `h2` (`font-size: 24px!important`)
- **Body Copy**: CSS variables `--font-paragraph--line-height: 1`, `--font-body--family: Inter, sans-serif`, `--font-body--style: normal`; rule `p` (`line-height: var(--line-height--bo...`)
- **Metadata & Labels**: CSS variables `--checkbox-label-padding: 8px`, `--image-height-small: calc(var(--image-height-basis) * 2)`, `--facets-input-label-color: rgb(var(--color-input-text-rgb) / var(--opacity-60))`; rule `small` (`font-size: 80%`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--color-foreground)` in `:root` |
| **Primary Typography Ink** | `#005BD1` | `var(--swn0j0)` in `:root` |
| **Elevated Surface / Card Substrate** | `#FFFFFF` | `var(--swn0j1)` in `:root` |
| **Interactive Accent / Highlight** | `#FAFBFF` | `var(--swn0j3)` in `:root` |
| **Secondary / Muted Copy** | `#F5F6FF` | `var(--swn0j4)` in `:root` |
| **Structural Hairline Border** | `#EBEDFF` | `var(--swn0j5)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--hover-lift-amount` | `4px` | Dimension / Scale Token |
| `--hover-scale-amount` | `1` | Design System Custom Token |
| `--hover-subtle-zoom-amount` | `1.015` | Design System Custom Token |
| `--hover-shadow-color` | `var(--color-shadow)` | Brand / Palette Token |
| `--hover-transition-duration` | `.25s` | Motion / Easing Token |
| `--hover-transition-timing` | `ease-out` | Motion / Easing Token |
| `--cursor` | `pointer` | Design System Custom Token |
| `--backdrop-color-rgb` | `var(--color-shadow-rgb)` | Brand / Palette Token |
| `--page-margin` | `16px` | Layout / Spatial Grid Token |
| `--page-content-width` | `var(--wide-page-width)` | Layout / Spatial Grid Token |
| `--page-width` | `calc(var(--page-content-width) + (var(--page-margin) * 2))` | Layout / Spatial Grid Token |
| `--full-page-grid-margin` | `minmax(var(--page-margin), 1fr)` | Layout / Spatial Grid Token |
| `--section-min-height` | `var(--section-height-small)` | Layout / Spatial Grid Token |
| `--centered-column-number` | `12` | Layout / Spatial Grid Token |
| `--full-width-column-number` | `14` | Layout / Spatial Grid Token |
| `--centered` | `column-1 / span var(--centered-column-number)` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.shopify-section> — `www-feelreformed-com`)**:
   - Landmark `<header class="shopify-section shopify-section-group-header-group">` hosting `Reformed: The biggest thing to happe` navigation (`Black Coffee · Mocha · Matcha · Shop All · Mocha with Collagen`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-shopify`, `data-shop-id="81515184414"`, `data-venmo-supported="false"`), and stylesheet rule `svg { display:block;max-width:100% }`.
2. **Hero Stage & Focal Lead (<section.shopify-section> — `Country/Region`)**:
   - Landmark `<section class="shopify-section section-wrapper">` presenting display lead `Country/Region` and copy excerpt *"Get Extra 10% off with the code REFORMED10 at Checkout"* over `#fff` canvas and `#005BD1` ink.
3. **Primary Showcase & Content Grid (<section.shopify-section> — `All Natural, Reformed Coffee & Mat`)**:
   - Landmark `<section class="shopify-section hero-wrapper">` rendering section `All Natural, Reformed Coffee & Matcha` with copy *"Cart Total items in cart: 0 0"*, asset references (`storefront.js`, `page-load`, `shopify.js`, `klaviyo.js`), and grid rule `img { width:100%;height:auto }`.
4. **Interactive Detail & Feature Matrix (<section.shopify-section> — `Discover Our Products`)**:
   - Landmark `<section class="shopify-section hero-wrapper">` framing `Discover Our Products` and `Frequently Purchased With` (*"Total items in cart: 0 0"*) with `#FFFFFF` surface cards, `#FAFBFF` accents, and `select { font:inherit;border-radius:var(--style-border-radius-inputs) }`.
5. **Colophon & Global Directory Footer (<footer.shopify-section> — `https://www.feelreformed.com/`)**:
   - Landmark `<footer class="shopify-section shopify-section-group-footer-group">` anchoring `Reformed: The biggest thing to h` footer links (`Black Coffee · Mocha · Matcha · Shop All · Mocha with Collagen`), copy *"Total items in cart: 0"*, and `#EBEDFF` structural dividers.
