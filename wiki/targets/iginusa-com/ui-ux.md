# UI & UX Architecture: iginusa-com

## Overview & Design Identity
- **Target**: `iginusa-com` (**IGIN USA · Official Home of IGIN in the United States**)
- **Production URL**: [https://iginusa.com](https://iginusa.com)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#f5f3f0`)
- **Summary**: IGIN in the USA. Doodle merch, non-alcoholic Apple Citrus and Apple Peach, and where to find IGIN near you. Official store.
- **Total Clean CSS Variables Extracted**: `699` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Anton`
- **Body Font Stack**: `Archivo`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **Hero Display (`H1`)**: CSS variables `--x-shell-disclosure-display: block`, `--x-shell-order-summary-display: none`, `--x-shell-content-display: grid`; rule `,.h1` (`font-size: calc(var(--font-heading-scale...`)
- **Section Heading (`H2`)**: rule `,.h2` (`font-size: calc(var(--font-heading-scale...`)
- **Body Copy**: CSS variables `--body: "Inter", "Helvetica Neue", Arial, sans-serif`, `--font-body-family: Assistant, sans-serif`, `--font-body-style: normal`; rule `p` (`font-size: 19px`, `line-height: 1.15`)
- **Metadata & Labels**: CSS variables `--mono: "JetBrains Mono", ui-monospace, "SF Mono", Menlo, monospace`, `--x-border-radius-small: 8px`, `--x-product-thumbnail-small-outer-size: 4.2rem`; rule `small` (`font-size: 10px`, `letter-spacing: .12em`, `font-weight: 600`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | `var(--igin-white)` in `:root` |
| **Primary Typography Ink** | `#111111` | `var(--igin-black)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ed302a` | `var(--igin-red)` in `:root` |
| **Interactive Accent / Highlight** | `#f5f3f0` | `var(--igin-gray-light)` in `:root` |
| **Secondary / Muted Copy** | `#999` | `var(--igin-gray-mid)` in `:root` |
| **Structural Hairline Border** | `#333` | `var(--igin-gray-dark)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--alpha-button-background` | `1` | Canvas / Surface Token |
| `--alpha-button-border` | `1` | Elevation / Border Token |
| `--alpha-link` | `.85` | Typography Ink Token |
| `--alpha-badge-border` | `.1` | Elevation / Border Token |
| `--focused-base-outline` | `.2rem solid rgba(var(--color-foreground), .5)` | Elevation / Border Token |
| `--focused-base-outline-offset` | `.3rem` | Elevation / Border Token |
| `--border-radius` | `var(--product-card-corner-radius)` | Elevation / Border Token |
| `--border-width` | `var(--product-card-border-width)` | Layout / Spatial Grid Token |
| `--border-opacity` | `var(--product-card-border-opacity)` | Elevation / Border Token |
| `--shadow-horizontal-offset` | `var(--product-card-shadow-horizontal-offset)` | Elevation / Border Token |
| `--shadow-vertical-offset` | `var(--product-card-shadow-vertical-offset)` | Elevation / Border Token |
| `--shadow-blur-radius` | `var(--product-card-shadow-blur-radius)` | Elevation / Border Token |
| `--shadow-opacity` | `var(--product-card-shadow-opacity)` | Elevation / Border Token |
| `--shadow-visible` | `var(--product-card-shadow-visible)` | Elevation / Border Token |
| `--image-padding` | `var(--product-card-image-padding)` | Layout / Spatial Grid Token |
| `--text-alignment` | `var(--product-card-text-alignment)` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.igin-rv> — `iginusa-com`)**:
   - Landmark `<header class="igin-rv hdr">` hosting `IGIN USA · Official Home of IGIN in ` navigation (`SHOP · Drinks · Our Story · Where to Buy · Play Doodle Pop`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-shop-id="100223058239"`, `data-venmo-supported="false"`, `data-environment="production"`), and stylesheet rule `.shopify-payment-button__button--... { visibility:hidden }`.
2. **Hero Stage & Focal Lead (<section.shopify-section> — `Are you 21 or over?`)**:
   - Landmark `<section class="shopify-section shopify-section-group-header-group">` presenting display lead `Are you 21 or over?` and copy excerpt *"Welcome to IGIN USA"* over `#ffffff` canvas and `#111111` ink.
3. **Primary Showcase & Content Grid (<section.shopify-section> — `IGIN USA: Where Smiles Begin`)**:
   - Landmark `<section class="shopify-section igin-doodle-pop-section">` rendering section `IGIN USA: Where Smiles Begin` with copy *"You must be 21 or over to enter this site."*, asset references (`2721185198297886`, `fbevents.js`, `LOGO-IGIN_USA_SNS_Profile.png`, `fonts.shopifycdn.com`), and grid rule `opify-payment-button__button--unb... { background-color:1990c6;padding:1em 2em }`.
4. **Interactive Detail & Feature Matrix (<section.shopify-section> — `Zero proof, same apples.`)**:
   - Landmark `<section class="shopify-section igin-rv-section">` framing `Zero proof, same apples.` and `Two fans chatting about the new IGIN non alcoholi...` (*"Please enjoy responsibly."*) with `#ed302a` surface cards, `#f5f3f0` accents, and `ptions.shopify-payment-button__sk... { width:50%;margin-left:25%;margin-right:25%;border-radius:4px!important;h... }`.
5. **Colophon & Global Directory Footer (<footer.igin-rv> — `https://iginusa.com`)**:
   - Landmark `<footer class="igin-rv ftr">` anchoring `IGIN USA · Official Home of IGIN` footer links (`SHOP · Drinks · Our Story · Where to Buy · Play Doodle Pop`), copy *"Shipping and tax at checkout."*, and `#333` structural dividers.
