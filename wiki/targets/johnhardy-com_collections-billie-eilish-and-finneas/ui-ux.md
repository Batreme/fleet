# UI & UX Architecture: johnhardy-com_collections-billie-eilish-and-finneas

## Overview & Design Identity
- **Target**: `johnhardy-com_collections-billie-eilish-and-finneas` (**Billie Eilish and FINNEAS – John Hardy**)
- **Production URL**: [https://johnhardy.com/collections/billie-eilish-and-finneas](https://johnhardy.com/collections/billie-eilish-and-finneas)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#161514` / `#535353`)
- **Summary**: John Hardy fine luxury jewelry. Made in Bali since 1975. Enjoy complimentary shipping and returns on all orders. Bracelets, Rings, Neckla...
- **Total Clean CSS Variables Extracted**: `477` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `itc-avant-garde-gothic-pro`
- **Body Font Stack**: `ivypresto-text`
- **Monospace / Technical Font Stack**: `Source Code Pro`
- **Hero Display (`H1`)**: CSS variables `--option-select-label-display: none`, `--bonsai-agent-share-display: none`; rule `h1` (`font-size: 1.5rem`, `line-height: 1.2`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: var(--hero-title-size-mobile,...`)
- **Body Copy**: CSS variables `--bonsai-font-body: var(--font-family-general-sans)`, `--bonsai-agent-body-bold-weight: 550`; rule `,p` (`font-size: var(--font-size-3)`, `line-height: var(--line-height-0)`, `letter-spacing: var(--letter-spacing-0)`, `font-weight: var(--font-we...`)
- **Metadata & Labels**: CSS variables `--letter-spacing-0: 0.5px`, `--letter-spacing-1: 1px`, `--letter-spacing-2: 1px`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#161514` | `var(--color-neutral-black)` in `:root` |
| **Primary Typography Ink** | `#212529` | `var(--jh-concierge-bubble-bg)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ffffff` | `var(--rb-smart-search-quick-view-button-text-color)` in `:root` |
| **Interactive Accent / Highlight** | `#535353` | `var(--rb-smart-search-quick-view-reviews-text-color)` in `:root` |
| **Secondary / Muted Copy** | `#232323` | `var(--rb-smart-search-results-product-title-color)` in `:root` |
| **Structural Hairline Border** | `#000000` | `var(--rb-smart-search-results-button-border-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--arrow-size` | `40px` | Layout / Spatial Grid Token |
| `--arrow-icon-size` | `calc(var(--arrow-size) / 2)` | Layout / Spatial Grid Token |
| `--arrows-padding` | `0 var(--spacing-l)` | Layout / Spatial Grid Token |
| `--arrows-width` | `100%` | Layout / Spatial Grid Token |
| `--arrows-translate` | `0 -50%` | Dimension / Scale Token |
| `--arrows-top` | `50%` | Dimension / Scale Token |
| `--pagination-margin-y` | `var(--spacing-2xl)` | Layout / Spatial Grid Token |
| `--pagination-padding-x` | `0` | Layout / Spatial Grid Token |
| `--page-active-bg` | `var(--color-neutral-black)` | Canvas / Surface Token |
| `--page-bg` | `var(--color-neutral-medium-grey)` | Canvas / Surface Token |
| `--page-height` | `4px` | Layout / Spatial Grid Token |
| `--page-width` | `4px` | Layout / Spatial Grid Token |
| `--page-radius` | `0` | Elevation / Border Token |
| `--padding` | `var(--spacing-s)` | Layout / Spatial Grid Token |
| `--ratio-height` | `273` | Layout / Spatial Grid Token |
| `--ratio-height-px` | `273px` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `johnhardy-com_collections-billie-eilish-and-finneas`)**:
   - Landmark `<header class="site-header">` hosting `Billie Eilish and FINNEAS – John Har` navigation (`Wishlist · New Arrivals · Best Sellers · Holiday Gifting · Bracelets`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-rapid="true"`, `data-shop-id="72737456428"`, `data-venmo-supported="true"`), and stylesheet rule `.shopify-payment-button__button--... { visibility:hidden }`.
2. **Hero Stage & Focal Lead (<section.accessibility> — `Billie Eilish & FINNEAS`)**:
   - Landmark `<section class="accessibility critical-hide">` presenting display lead `Billie Eilish & FINNEAS` and copy excerpt *"Enable accessibility"* over `#161514` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.site-header-group> — `Two Expressions of One Creative Vi`)**:
   - Landmark `<section class="site-header-group is-open">` rendering section `Two Expressions of One Creative Vision Two Expres...` with copy *"Press Option/Alt + K at any time to jump back to these sign posts"*, asset references (`rebuy.js`, `loader.js`, `01HNXAYFWDBE125P1ZK44ZZ829`, `117791.ct.js`), and grid rule `opify-payment-button__button--unb... { background-color:1990c6;padding:1em 2em }`.
4. **Interactive Detail & Feature Matrix (<section.template-collection> — `“Jewelry has always been an enormo`)**:
   - Landmark `<section class="template-collection">` framing `“Jewelry has always been an enormous part of how...` and `Two years in the making` (*"Skip to main content"*) with `#ffffff` surface cards, `#535353` accents, and `ptions.shopify-payment-button__sk... { width:50%;margin-left:25%;margin-right:25%;border-radius:4px!important;h... }`.
5. **Colophon & Global Directory Footer (<footer.has-overlay> — `https://johnhardy.com/collections/billie-eilish-and-finneas`)**:
   - Landmark `<footer class="has-overlay">` anchoring `Billie Eilish and FINNEAS – John` footer links (`Wishlist · New Arrivals · Best Sellers · Holiday Gifting · Bracelets`), copy *"Skip to site header"*, and `#000000` structural dividers.
