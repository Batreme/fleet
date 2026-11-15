# UI & UX Architecture: bluntumbrellas-com

## Overview & Design Identity
- **Target**: `bluntumbrellas-com` (**BLUNT Umbrellas · Built to Resist Every Weather**)
- **Production URL**: [https://bluntumbrellas.com](https://bluntumbrellas.com)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#121212` canvas, `#fff` ink, `#000` accent)
- **Summary**: Discover Blunt Umbrellas: premium stormproof umbrellas designed to withstand extreme weather. Innovative design, superior durability, and...
- **Total Clean CSS Variables Extracted**: `811` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Poppins`
- **Body Font Stack**: `F6F6F7`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--x-shell-disclosure-display: block`, `--x-shell-order-summary-display: none`, `--x-shell-content-display: grid`; rule `h1` (`font-size: var(--x-heading-level1-font-s...`, `line-height: var(--x-typography-li...`, `letter-spacing: var(--x-heading-level...`, `font-weight: var(--x-headi...`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: var(--x-heading-level2-font-s...`, `line-height: var(--x-typography-li...`, `letter-spacing: var(--x-heading-level...`, `font-weight: var(--x-headi...`)
- **Body Copy**: CSS variables `--modal-body-padding-block: 1.25rem`, `--modal-body-padding-inline: 1.25rem`, `--modal-body-max-width: 30rem`; rule `p` (`font-size: 14px`, `line-height: 20px`, `font-weight: 450`)
- **Metadata & Labels**: CSS variables `--heading-letter-spacing: 0`, `--ts-geo-label-color: #121212`, `--ts-expand-label-color: #5C5F62`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#121212` | `var(--ts-text-color)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--ts-geo-bg)` in `:root` |
| **Elevated Surface / Card Substrate** | `#F6F6F7` | `var(--ts-geo-body-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#000` | `var(--ts-geo-icon)` in `:root` |
| **Secondary / Muted Copy** | `#155DFC` | `var(--ts-geo-btn-bg)` in `:root` |
| **Structural Hairline Border** | `#004299` | `var(--ts-geo-btn-bg-hover)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--border-color` | `var(--text-color) / .6` | Brand / Palette Token |
| `--blog-post-list-items-per-row` | `1` | Design System Custom Token |
| `--blog-post-list-column-gap` | `1.875rem` | Layout / Spatial Grid Token |
| `--blog-post-list-row-gap` | `var(--section-stack-gap)` | Layout / Spatial Grid Token |
| `--blog-post-list-card-width` | `40vw` | Layout / Spatial Grid Token |
| `--hover-gradient` | `linear-gradient(transparent, transparent)` | Design System Custom Token |
| `--initial-background-position` | `var(--transform-origin-end)` | Canvas / Surface Token |
| `--hover-background-position` | `var(--transform-origin-start)` | Canvas / Surface Token |
| `--initial-gradient` | `linear-gradient(transparent, transparent)` | Design System Custom Token |
| `--circle-button-size` | `2.75rem` | Layout / Spatial Grid Token |
| `--content-over-media-gap` | `1.25rem` | Layout / Spatial Grid Token |
| `--content-over-media-calculated-row-gap` | `var(--content-over-media-row-gap, var(--content-over-media-gap))` | Layout / Spatial Grid Token |
| `--content-over-media-calculated-column-gap` | `var(--content-over-media-column-gap, var(--content-over-media-gap))` | Layout / Spatial Grid Token |
| `--content-over-media-height` | `clamp(15rem, 65vw, 25rem)` | Layout / Spatial Grid Token |
| `--dot-size` | `.375rem` | Layout / Spatial Grid Token |
| `--floating-controls-inset-inline` | `1.5rem` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.jdgm-settings-script> — `bluntumbrellas-com`)**:
   - Landmark `<header class="jdgm-settings-script">` hosting `BLUNT Umbrellas · Built to Resist Ev` navigation (`Regular Models · Limited Editions · UV Umbrellas · All Umbrellas · Our Design`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-source-attribution="shopify.loadfeatures"`, `data-source-attribution="shopify.dynamic_check..."`, `data-source-attribution="shopify.dynamic_check..."`), and stylesheet rule `.shopify-payment-button__button--... { visibility:hidden }`.
2. **Hero Stage & Focal Lead (<section.shopify-pc__banner__dialog> — `Cookie consent`)**:
   - Landmark `<section class="shopify-pc__banner__dialog">` presenting display lead `Cookie consent` and copy excerpt *"We and our partners, including Shopify, use cookies and other tec"* over `#121212` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.shopify-section> — `BLUNT Umbrellas EU`)**:
   - Landmark `<section class="shopify-section shopify-section-group-overlay-group">` rendering section `BLUNT Umbrellas EU` with copy *"Manage preferences"*, asset references (`blunt_favicon.png`, `fonts.shopifycdn.com`, `poppins_n4.0ba78fa5af9b0e1a374041...`, `es-modules-shim.2.4.0.js`), and grid rule `opify-payment-button__button--unb... { background-color:1990c6;padding:1em 2em }`.
4. **Interactive Detail & Feature Matrix (<section.shopify-section> — `New. Small. Neo.`)**:
   - Landmark `<section class="shopify-section shopify-section--neo-hero">` framing `New. Small. Neo.` and `What others say about Blunt` (*"Free UPS shipping to Germany & neighbouring countries"*) with `#F6F6F7` surface cards, `#000` accents, and `ptions.shopify-payment-button__sk... { width:50%;margin-left:25%;margin-right:25%;border-radius:4px!important;h... }`.
5. **Colophon & Global Directory Footer (<footer.analytics> — `https://bluntumbrellas.com`)**:
   - Landmark `<footer class="analytics">` anchoring `BLUNT Umbrellas · Built to Resis` footer links (`Regular Models · Limited Editions · UV Umbrellas · All Umbrellas · Our Design`), copy *"BLUNT Umbrellas EU"*, and `#004299` structural dividers.
