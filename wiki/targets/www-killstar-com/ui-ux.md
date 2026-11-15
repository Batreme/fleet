# UI & UX Architecture: www-killstar-com

## Overview & Design Identity
- **Target**: `www-killstar-com` (**KILLSTAR**)
- **Production URL**: [https://www.killstar.com/](https://www.killstar.com/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#e9e9eb` canvas, `#1d1e20` ink, `#518b22` accent)
- **Summary**: Clothing & Lifestyle company with a twist of darkness, channeling emotional power and raw energy into every thread.
- **Total Clean CSS Variables Extracted**: `224` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `PPPlayground`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--atlas-font-size-display: 40px`, `--atlas-line-height-display: 52px`, `--atlas-margin-display: 24px`; rule `.title` (`font-size: 13px`)
- **Section Heading (`H2`)**: CSS variables `--atlas-font-size-h2: 32px`, `--atlas-line-height-h2: 40px`, `--atlas-margin-h2: 24px`; rule `h2` (`font-size: 2.5em`, `font-weight: 900`)
- **Body Copy**: rule `p` (`line-height: 1.6`)
- **Metadata & Labels**: CSS variables `--atlas-font-size-small: 14px`, `--atlas-line-height-small: 20px`, `--atlas-margin-small: 8px`; rule `.label` (`font-size: .875em`, `letter-spacing: 2.8px`, `font-weight: 500`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#e9e9eb` | `var(--kl-reviews-color-light-gray)` in `:root` |
| **Primary Typography Ink** | `#faf9f8` | `var(--atlas-background-main)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ffffff` | `var(--atlas-background-content)` in `:root` |
| **Interactive Accent / Highlight** | `#518b22` | `var(--atlas-background-success)` in `:root` |
| **Secondary / Muted Copy** | `#be2119` | `var(--atlas-background-error)` in `:root` |
| **Structural Hairline Border** | `#1d1e20` | `var(--atlas-text-primary)` in `:root` |
| **Variable Token (`--atlas-text-secondary`)** | `#4b4d4e` | `var(--atlas-text-secondary)` in `:root` |
| **Variable Token (`--atlas-text-positive`)** | `#366d12` | `var(--atlas-text-positive)` in `:root` |
| **Variable Token (`--atlas-text-placeholder`)** | `#747576` | `var(--atlas-text-placeholder)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--kl-reviews-color-light-gray` | `#e9e9eb` | Canvas / Surface Token |
| `--kl-local-border-radius` | `var(--atlas-button-border-radius-normal)` | Elevation / Border Token |
| `--kl-local-button-color` | `var(--atlas-text-primary-inverse)` | Brand / Palette Token |
| `--kl-local-button-background` | `var(--atlas-button-primary)` | Canvas / Surface Token |
| `--kl-local-icon-size` | `var(--atlas-icon-size-medium)` | Layout / Spatial Grid Token |
| `--kl-local-border-color` | `var(--atlas-button-primary)` | Brand / Palette Token |
| `--atlas-background-main` | `#faf9f8` | Canvas / Surface Token |
| `--atlas-background-content` | `#ffffff` | Canvas / Surface Token |
| `--atlas-background-success` | `#518b22` | Canvas / Surface Token |
| `--atlas-background-error` | `#be2119` | Canvas / Surface Token |
| `--atlas-text-primary` | `#1d1e20` | Typography Ink Token |
| `--atlas-text-secondary` | `#4b4d4e` | Typography Ink Token |
| `--atlas-text-negative` | `#be2119` | Typography Ink Token |
| `--atlas-text-positive` | `#366d12` | Typography Ink Token |
| `--atlas-text-placeholder` | `#747576` | Typography Ink Token |
| `--atlas-text-primary-inverse` | `#ffffff` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.shopify-section> — `www-killstar-com`)**:
   - Landmark `<header class="shopify-section shopify-section-group-header-group">` hosting `KILLSTAR` navigation (`NEW IN · DRESSES · WOMENS · PLUS · MENS`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-shop-id="53907226789"`, `data-venmo-supported="false"`, `data-environment="production"`), and stylesheet rule `root { --swiper-navigation-size:44px }`.
2. **Hero Stage & Focal Lead (<section.shopify-pc__banner__dialog> — `HOW WE USE YOUR DATA`)**:
   - Landmark `<section class="shopify-pc__banner__dialog">` presenting display lead `HOW WE USE YOUR DATA` and copy excerpt *"We use cookies & other technologies to provide a personalised exp"* over `#e9e9eb` canvas and `#1d1e20` ink.
3. **Primary Showcase & Content Grid (<section.shopify-section> — `Winter's Vale Coat`)**:
   - Landmark `<section class="shopify-section shopify-section-group-header-group">` rendering section `Winter's Vale Coat` with copy *"Manage preferences"*, asset references (`reamaze-push.js`, `tp.min.js`, `37086_1783060609.js`, `init.js`), and grid rule `iper-button-next.swiper-button-di... { opacity:.35;cursor:auto;pointer-events:none }`.
4. **Interactive Detail & Feature Matrix (<section.shopify-section> — `Skultra Cropped Cardigan`)**:
   - Landmark `<section class="shopify-section shopify-section-group-header-group">` framing `Skultra Cropped Cardigan` and `Basilica Cape` (*"Black Friday 13th Sale - Shop Now Black Friday 13th Sale - Shop N"*) with `#ffffff` surface cards, `#518b22` accents, and `swiper-button-next.swiper-button-... { opacity:0;cursor:auto;pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.shopify-section> — `https://www.killstar.com/`)**:
   - Landmark `<footer class="shopify-section shopify-section-group-footer-group">` anchoring `KILLSTAR` footer links (`NEW IN · DRESSES · WOMENS · PLUS · MENS`), copy *"Black Friday 13th Sale - Shop Now"*, and `#1d1e20` structural dividers.
