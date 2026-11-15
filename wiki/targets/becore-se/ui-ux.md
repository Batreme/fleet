# UI & UX Architecture: becore-se

## Overview & Design Identity
- **Target**: `becore-se` (**Becore**)
- **Production URL**: [https://becore.se/](https://becore.se/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#1990c6` canvas, `#fff` ink, `#121212` accent)
- **Summary**: Experience the latest in activewear from our new Becore collection
- **Total Clean CSS Variables Extracted**: `240` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Roboto`
- **Body Font Stack**: `Cabin`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `100%`, `.6875rem`, `.8125rem`, `.625rem`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 120%`, `font-weight: bold`)
- **Body Copy**: CSS variables `--drawer-body-padding-block: min(2rem, var(--container-gutter))`, `--drawer-body-padding-inline: min(2rem, var(--container-gutter))`, `--modal-body-padding-block: 1.25rem`; rule `p` (`line-height: 1.3`)
- **Metadata & Labels**: CSS variables `--subheading-letter-spacing: -0.01em`, `--heading-letter-spacing: 0.01em`, `--text-letter-spacing: -0.01em`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#1990c6` | `.shopify-payment-button__button... { background-color: #1990c6 }` |
| **Primary Typography Ink** | `#0000` | `pify-payment-button__button.but... { color: #0000 }` |
| **Elevated Surface / Card Substrate** | `#fff` | `on.loading>.loading-overlay__sp... { stroke: #fff }` |
| **Interactive Accent / Highlight** | `#121212` | `.shopify-payment-button__button... { stroke: #121212 }` |
| **Secondary / Muted Copy** | `#1a1a1a` | `.toast__message { background: #1a1a1a }` |
| **Structural Hairline Border** | `#e51c00` | `.toast__message--error { background: #e51c00 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--border-color` | `var(--text-color) / .6` | Brand / Palette Token |
| `--accordion-block-padding` | `.875rem` | Layout / Spatial Grid Token |
| `--accordion-inline-padding` | `0` | Layout / Spatial Grid Token |
| `--button-padding-block` | `.75rem` | Layout / Spatial Grid Token |
| `--button-padding-inline` | `1.5rem` | Layout / Spatial Grid Token |
| `--button-background` | `var(--button-background-primary)` | Canvas / Surface Token |
| `--button-text-color` | `var(--button-text-primary)` | Typography Ink Token |
| `--button-border-color` | `0 0 0 / 0` | Brand / Palette Token |
| `--glowing-shape-width` | `min(40px, 60%)` | Layout / Spatial Grid Token |
| `--button-size` | `1.75rem` | Layout / Spatial Grid Token |
| `--content-box-spacing` | `max(1.5rem, var(--container-gutter))` | Layout / Spatial Grid Token |
| `--scroll-marker-group-gap` | `.3125rem .75rem` | Layout / Spatial Grid Token |
| `--scroll-marker-size` | `.375rem` | Layout / Spatial Grid Token |
| `--scroll-marker-width` | `.5rem` | Layout / Spatial Grid Token |
| `--scroll-marker-height` | `1px` | Layout / Spatial Grid Token |
| `--scroll-marker-group-justify-content` | `start` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.hydrated> — `becore-se`)**:
   - Landmark `<header class="hydrated">` hosting `Becore` navigation (`MOVE · SHOP`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-locksmith`, `data-styles`, `data-shop-id="85529952592"`), and stylesheet rule `.shopify-payment-button__button--... { visibility:hidden }`.
2. **Hero Stage & Focal Lead (<section.shopify-pc__banner__dialog> — `Cookie consent`)**:
   - Landmark `<section class="shopify-pc__banner__dialog">` presenting display lead `Cookie consent` and copy excerpt *"We and our partners, including Shopify, use cookies and other tec"* over `#1990c6` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.shopify-section> — `Becore`)**:
   - Landmark `<section class="shopify-section shopify-section-group-overlay-group">` rendering section `Becore` with copy *"Manage preferences"*, asset references (`mixpanel-2-latest.min.js`, `jquery-3.6.4.min-dad6fdf250e31dfa...`, `jquery-migrate-3.4.1.min-6a381abc...`, `jquery-ui-1.13.2.widget-32e3429b3...`), and grid rule `opify-payment-button__button--unb... { background-color:1990c6;padding:1em 2em }`.
4. **Interactive Detail & Feature Matrix (<section.shopify-section> — `Cart`)**:
   - Landmark `<section class="shopify-section shopify-section-group-overlay-group">` framing `Cart` and `Favourites ( 0 )` (*"BLACK FRIDAY · 10 CREDITS FOR 2 500 SEK · SHOP NOW"*) with `#fff` surface cards, `#121212` accents, and `ptions.shopify-payment-button__sk... { width:50%;margin-left:25%;margin-right:25%;border-radius:4px!important;h... }`.
5. **Colophon & Global Directory Footer (<footer.shopify-pc__banner__dialog> — `https://becore.se/`)**:
   - Landmark `<footer class="shopify-pc__banner__dialog">` anchoring `Becore` footer links (`MOVE · SHOP`), copy *"Studio Join Membership & credits Gift card FAQ Studio login "*, and `#e51c00` structural dividers.
