---
title: "UI & UX Architecture: www-halcyon-co-nz"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-halcyon-co-nz

## Overview & Design Identity
- **Target**: `www-halcyon-co-nz` (**Halcyon · Leading Lighting Specialists**)
- **Production URL**: [https://www.halcyon.co.nz/](https://www.halcyon.co.nz/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×828px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#f7eb12`)
- **Summary**: Driven by innovation and an unwavering commitment to quality, Halcyon works with leading architects, specifiers and electrical experts to...
- **Total Clean CSS Variables Extracted**: `775` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Halcyon Monument Grotesk`
- **Body Font Stack**: `Untitled`
- **Monospace / Technical Font Stack**: `Halcyon Monument Grotesk Semi-Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 115.2px`, `line-height: 115.2px`, `font-weight: 500`, `letter-spacing: -3.76px`); rule `,.h1` (`font-size: 88px`, `line-height: 100%`, `letter-spacing: -1.76px`, `font-weight: 500`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 87.9984px`, `line-height: 87.9984px`, `font-weight: 500`, `letter-spacing: -1.76px`); rule `,.h2` (`font-size: 56px`, `line-height: 100%`, `letter-spacing: -.84px`, `font-weight: 500`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 18.4px`, `font-weight: 500`); CSS variables `--boostsd-general-font-size-base: 16px`, `--boostsd-cart-body-padding: 16px`, `--boostsd-cart-body-padding-medium: 24px`; rule `p` (`font-size: 12px`, `line-height: 90%`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 12px`, `font-weight: 500`); CSS variables `--boostsd-product-label-padding: 2px 6px`, `--boostsd-product-label-border-radius: 2px`, `--boostsd-product-label-border-radius-capsule: 40px`; rule `.label` (`font-size: 12px`, `line-height: 12px`, `letter-spacing: 0`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `browser-default` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffe5b4` | `var(--color-background)` in `:root` |
| **Interactive Accent / Highlight** | `#f7eb12` | `.primary-button--light:after { background: #f7eb12 }` |
| **Secondary / Muted Copy** | `#303030` | `var(--megamenu-item-text)` in `:root` |
| **Structural Hairline Border** | `#eeeeee` | `var(--megamenu-divider)` in `:root` |
| **Variable Token (`--megamenu-hover`)** | `#f8f6f7` | `var(--megamenu-hover)` in `:root` |
| **Variable Token (`--halcyon-toast-success`)** | `#32e26e` | `var(--halcyon-toast-success)` in `:root` |
| **Variable Token (`--halcyon-toast-error`)** | `#e75619` | `var(--halcyon-toast-error)` in `:root` |
| **Variable Token (`--halcyon-toast-info`)** | `#3b82f6` | `var(--halcyon-toast-info)` in `:root` |
| **Variable Token (`--halcyon-toast-warning`)** | `#f59e0b` | `var(--halcyon-toast-warning)` in `:root` |

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
| `--megamenu-hover` | `#f8f6f7` | Color / Atmospheric Token |
| `--megamenu-active` | `#eee` | Color / Atmospheric Token |
| `--megamenu-divider` | `#eee` | Color / Atmospheric Token |
| `--megamenu-item-text` | `#303030` | Typography Ink Token |
| `--transition-speed` | `2s` | Motion / Easing Token |
| `--halcyon-toast-success` | `#32e26e` | Color / Atmospheric Token |
| `--halcyon-toast-error` | `#e75619` | Color / Atmospheric Token |
| `--halcyon-toast-info` | `#3b82f6` | Color / Atmospheric Token |
| `--halcyon-toast-warning` | `#f59e0b` | Color / Atmospheric Token |
| `--halcyon-toast-text` | `#000` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.js> — `www-halcyon-co-nz`)**:
   - Landmark `<header class="js">` (`1440px`) hosting `Halcyon · Leading Lighting Specialis` navigation (`Return · Products · About · Highlights · Stockists`), DOM attributes (`data-collection-view="grid"`, `data-source-attribution="shopify.exit_intersti..."`, `data-source-attribution="shopify.loadfeatures"`, `data-source-attribution="shopify.dynamic_check..."`), and stylesheet rule `html { line-height:1.15;-webkit-text-size-adjust:100% }`.
2. **Hero Stage & Focal Lead (<section.main-hero> — `Good Light.`)**:
   - Landmark `<section class="main-hero hero-main-section">` presenting display lead `Good Light.` and copy excerpt *"At Halcyon we make lighting to perform, and we make lighting to l"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.featured-product> — `Cevon M-Type`)**:
   - Landmark `<section class="featured-product">` rendering section `Cevon M-Type` with copy *"M-Type is a modular system developed for refined interiors where "*, asset references (`inventoryLocation.js`, `clarity.js`, `wwzwszat2d`, `gtm.js`), and grid rule `main { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.tabbed-collection> — `Latest Collections`)**:
   - Landmark `<section class="tabbed-collection">` framing `Latest Collections` and `Trade Flex Pro` (*"From discreet illumination to feature lighting and general ambien"*) with `#ffe5b4` surface cards, `#f7eb12` accents, and `pre { font-family:monospace,monospace;font-size:1em }`.
5. **Colophon & Global Directory Footer (<footer.js-ajax-cart-empty> — `https://www.halcyon.co.nz/`)**:
   - Landmark `<footer class="js-ajax-cart-empty">` anchoring `Halcyon · Leading Lighting Speci` footer links (`Return · Products · About · Highlights · Stockists`), copy *"Cevon M80 Type 1 Dark Art Adjustable Black, Gold 3000K"*, and `#eeeeee` structural dividers.
