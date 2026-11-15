# UI & UX Architecture: deadlyponies-com

## Overview & Design Identity
- **Target**: `deadlyponies-com` (**Deadly Ponies - Luxury Leather Bags & Accessories**)
- **Production URL**: [https://deadlyponies.com](https://deadlyponies.com)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#000000` accent)
- **Summary**: Discover Deadly Ponies, a New Zealand-based label, crafting luxury bags & accessories. Coveted luxury leather handbags and accessories.
- **Total Clean CSS Variables Extracted**: `530` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Poppins`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--x-shell-disclosure-display: block`, `--x-shell-order-summary-display: none`, `--x-shell-content-display: grid`; rule `h1` (`font-size: 26px`, `line-height: 32px`, `letter-spacing: -.78px`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 15px!important`, `line-height: 21px!important`, `letter-spacing: .1px!important`, `font-weight: 400!important`)
- **Body Copy**: rule `p` (`font-size: 11px`, `line-height: 17px`, `letter-spacing: -0.12px`)
- **Metadata & Labels**: CSS variables `--x-border-radius-small: 8px`, `--x-product-thumbnail-small-outer-size: 4.2rem`, `--x-spacing-small-500: .2rem`; rule `small` (`font-size: calc(var(--kl-reviews-reviews...`, `font-weight: var(--kl-revi...`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--fore-color)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--back-color)` in `:root` |
| **Elevated Surface / Card Substrate** | `#8B8A89` | `var(--wishlist-color)` in `:root` |
| **Interactive Accent / Highlight** | `#000000` | `var(--text-color)` in `:root` |
| **Secondary / Muted Copy** | `#8f8f8f` | `var(--apd-muted)` in `:root` |
| **Structural Hairline Border** | `#dadada` | `var(--apd-line)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--height-full` | `100vh` | Layout / Spatial Grid Token |
| `--height-fill` | `calc( 100vh - var(--nav-height) )` | Layout / Spatial Grid Token |
| `--font-deadly` | `"Deadly", sans-serif` | Typography / Scale Token |
| `--nav-main-height` | `46px` | Layout / Spatial Grid Token |
| `--nav-height` | `var(--nav-main-height)` | Layout / Spatial Grid Token |
| `--fore-color` | `#000` | Brand / Palette Token |
| `--back-color` | `#fff` | Brand / Palette Token |
| `--top-padding` | `100px` | Layout / Spatial Grid Token |
| `--wishlist-color` | `#8B8A89` | Brand / Palette Token |
| `--row-gap` | `40px` | Layout / Spatial Grid Token |
| `--col-gap` | `10px` | Layout / Spatial Grid Token |
| `--text-color` | `#000000` | Typography Ink Token |
| `--section-height` | `90vh` | Layout / Spatial Grid Token |
| `--apd-bg` | `#fff` | Canvas / Surface Token |
| `--apd-text` | `#000` | Typography Ink Token |
| `--apd-muted` | `#8f8f8f` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `deadlyponies-com`)**:
   - Landmark `<header class="header header--dark">` hosting `Deadly Ponies - Luxury Leather Bags ` navigation (`Bags · New Arrivals · View All · Tote Bags · Shoulder Bags`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-shop-id="71218823442"`, `data-venmo-supported="false"`, `data-environment="production"`), and stylesheet rule `root { --swiper-theme-color:007aff }`.
2. **Hero Stage & Focal Lead (<section.shopify-section> — `Bags`)**:
   - Landmark `<section class="shopify-section content-section">` presenting display lead `Bags` and copy excerpt *"Complimentary Express shipping on all orders"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.shopify-section> — `Shoes`)**:
   - Landmark `<section class="shopify-section content-section">` rendering section `Shoes` with copy *"Receive 10% off your first purchase · Sign up"*, asset references (`93837`, `loader.js`, `01H2CKQHWBM22V9RBNTG4KH275`, `swym-ext-shopify.js`), and grid rule `swiper-container { margin-left:auto;margin-right:auto;position:relative;overflow:hidden;lis... }`.
4. **Interactive Detail & Feature Matrix (<section.shopify-section> — `Accessories`)**:
   - Landmark `<section class="shopify-section content-section">` framing `Accessories` and `Loyalty` (*"Bags Category New Arrivals View All Tote Bags Shoulder Bags Cross"*) with `#8B8A89` surface cards, `#000000` accents, and `.swiper-vertical>.swiper-wrapper { flex-direction:column }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://deadlyponies.com`)**:
   - Landmark `<footer class="footer">` anchoring `Deadly Ponies - Luxury Leather B` footer links (`Bags · New Arrivals · View All · Tote Bags · Shoulder Bags`), copy *"Occassion Dressing"*, and `#dadada` structural dividers.
