# UI & UX Architecture: www-halcyon-co-nz

## Overview & Design Identity
- **Target**: `www-halcyon-co-nz` (**Halcyon · Leading Lighting Specialists**)
- **Production URL**: [https://www.halcyon.co.nz/](https://www.halcyon.co.nz/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#32e26e` / `#f59e0b`)
- **Summary**: Driven by innovation and an unwavering commitment to quality, Halcyon works with leading architects, specifiers and electrical experts to...
- **Total Clean CSS Variables Extracted**: `735` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `etica-display`
- **Body Font Stack**: `lft-etica`
- **Monospace / Technical Font Stack**: `Halcyon Monument Grotesk Semi-Mono`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `30px`, `40px`, `var(--boostsd-filter-search-optio...`, `20px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `30px`, `40px`, `var(--boostsd-filter-search-optio...`, `20px`)
- **Body Copy**: CSS variables `--boostsd-general-font-size-base: 16px`, `--boostsd-cart-body-padding: 16px`, `--boostsd-cart-body-padding-medium: 24px`; rule `p` (`font-size: 13px`, `line-height: 17px`, `letter-spacing: 0`, `font-weight: 500`)
- **Metadata & Labels**: CSS variables `--boostsd-product-label-padding: 2px 6px`, `--boostsd-product-label-border-radius: 2px`, `--boostsd-product-label-border-radius-capsule: 40px`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#32e26e` | `var(--halcyon-toast-success)` in `:root` |
| **Primary Typography Ink** | `#e75619` | `var(--halcyon-toast-error)` in `:root` |
| **Elevated Surface / Card Substrate** | `#3b82f6` | `var(--halcyon-toast-info)` in `:root` |
| **Interactive Accent / Highlight** | `#f59e0b` | `var(--halcyon-toast-warning)` in `:root` |
| **Secondary / Muted Copy** | `#000` | `var(--halcyon-toast-text)` in `:root` |
| **Structural Hairline Border** | `#222` | `var(--boostsd-general-color-primary)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--height-full` | `100vh` | Layout / Spatial Grid Token |
| `--height-fill` | `calc(100vh - var(--nav-height))` | Layout / Spatial Grid Token |
| `--font-orion` | `"Untitled", sans-serif` | Typography / Scale Token |
| `--annoucement-height` | `37px` | Layout / Spatial Grid Token |
| `--nav-main-height` | `44px` | Layout / Spatial Grid Token |
| `--nav-height` | `calc(var(--nav-main-height))` | Layout / Spatial Grid Token |
| `--halcyon-toast-success` | `#32e26e` | Color / Atmospheric Token |
| `--halcyon-toast-error` | `#e75619` | Color / Atmospheric Token |
| `--halcyon-toast-info` | `#3b82f6` | Color / Atmospheric Token |
| `--halcyon-toast-warning` | `#f59e0b` | Color / Atmospheric Token |
| `--halcyon-toast-text` | `#000` | Typography Ink Token |
| `--halcyon-toast-max-width` | `500px` | Layout / Spatial Grid Token |
| `--halcyon-toast-sweep-duration` | `5s` | Motion / Easing Token |
| `--boostsd-general-page-width-desktop` | `1216px` | Layout / Spatial Grid Token |
| `--boostsd-general-color-primary` | `#222` | Brand / Palette Token |
| `--boostsd-general-font-size-base` | `16px` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.js> — `www-halcyon-co-nz`)**:
   - Landmark `<header class="js">` hosting `Halcyon · Leading Lighting Specialis` navigation (`Return · Products · About · Highlights · Stockists`), DOM attributes (`data-collection-view="grid"`, `data-source-attribution="shopify.exit_intersti..."`, `data-source-attribution="shopify.loadfeatures"`, `data-source-attribution="shopify.dynamic_check..."`), and stylesheet rule `.shopify-payment-button__button--... { visibility:hidden }`.
2. **Hero Stage & Focal Lead (<section.main-hero> — `Confirmation`)**:
   - Landmark `<section class="main-hero hero-main-section">` presenting display lead `Confirmation` and copy excerpt *"No wishlists found"* over `#32e26e` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.featured-product> — `Dark Art Slim Trim`)**:
   - Landmark `<section class="featured-product">` rendering section `Dark Art Slim Trim` with copy *"SAVE ITEM TO FAVOURITES LIST"*, asset references (`inventoryLocation.js`, `clarity.js`, `wwzwszat2d`, `gtm.js`), and grid rule `opify-payment-button__button--unb... { background-color:1990c6;padding:1em 2em }`.
4. **Interactive Detail & Feature Matrix (<section.tabbed-collection> — `Trade Flex Pro`)**:
   - Landmark `<section class="tabbed-collection">` framing `Trade Flex Pro` and `Mini Mariner` (*"Remove from this list"*) with `#3b82f6` surface cards, `#f59e0b` accents, and `ptions.shopify-payment-button__sk... { width:50%;margin-left:25%;margin-right:25%;border-radius:4px!important;h... }`.
5. **Colophon & Global Directory Footer (<footer.js-ajax-cart-empty> — `https://www.halcyon.co.nz/`)**:
   - Landmark `<footer class="js-ajax-cart-empty">` anchoring `Halcyon · Leading Lighting Speci` footer links (`Return · Products · About · Highlights · Stockists`), copy *"Create a personalised list to organise your favourite items"*, and `#222` structural dividers.
