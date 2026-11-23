---
title: "UI & UX Architecture: bluntumbrellas-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: bluntumbrellas-com

## Overview & Design Identity
- **Target**: `bluntumbrellas-com` (**BLUNT Umbrellas · Built to Resist Every Weather**)
- **Production URL**: [https://bluntumbrellas.com](https://bluntumbrellas.com)
- **Final Redirected URL**: [https://bluntumbrellas.eu/](https://bluntumbrellas.eu/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f1f1f1` canvas, `#1c1c1c` ink, `#ffc700` accent)
- **Summary**: Discover Blunt Umbrellas: premium stormproof umbrellas designed to withstand extreme weather. Innovative design, superior durability, and...
- **Total Clean CSS Variables Extracted**: `1035` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Poppins`
- **Body Font Stack**: `Poppins`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 28px`, `line-height: 46.2px`, `font-weight: 700`); CSS variables `--loyalty-shimmer-display: none`, `--x-shell-disclosure-display: block`, `--x-shell-order-summary-display: none`; rule `,.h1` (`font-size: 140px`, `line-height: .99em`, `font-weight: 600`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 28px`, `line-height: 39.2px`, `font-weight: 400`, `letter-spacing: 2.8px`); CSS variables `--loyalty-banner-subtitle-size: 14px`; rule `,.h2` (`font-size: 95px`, `line-height: .95em`, `font-weight: 600`)
- **Body Copy**: live computed `body` (`font-size: 14px`, `line-height: 23.1px`, `font-weight: 400`); CSS variables `--text-base: 0.875rem`, `--paragraph-font-size: 16px`, `--paragraph-font-weight: 400`; rule `p` (`font-size: 13px`, `line-height: 17px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 14px`, `line-height: 23.1px`, `font-weight: 400`); CSS variables `--heading-letter-spacing: 0.1em`, `--text-letter-spacing: 0.0em`, `--button-letter-spacing: 0.18em`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f1f1f1` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#1c1c1c` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `var(--bundle-component-background)` in `:root` |
| **Interactive Accent / Highlight** | `#ffc700` | `oduct-review .question-form .ra... { color: #ffc700 }` |
| **Secondary / Muted Copy** | `#7b7b7b` | `var(--jdgm-snippet-lighter-text-color)` in `:root` |
| **Structural Hairline Border** | `#cccccc` | `var(--bundle-option-border-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--container-max-width` | `100%` | Layout / Spatial Grid Token |
| `--container-xxs-max-width` | `27.5rem` | Layout / Spatial Grid Token |
| `--container-xs-max-width` | `42.5rem` | Layout / Spatial Grid Token |
| `--container-sm-max-width` | `61.25rem` | Layout / Spatial Grid Token |
| `--container-md-max-width` | `71.875rem` | Layout / Spatial Grid Token |
| `--container-lg-max-width` | `78.75rem` | Layout / Spatial Grid Token |
| `--container-xl-max-width` | `85rem` | Layout / Spatial Grid Token |
| `--container-gutter` | `1.25rem` | Layout / Spatial Grid Token |
| `--section-vertical-spacing` | `2.5rem` | Layout / Spatial Grid Token |
| `--section-vertical-spacing-tight` | `2.5rem` | Layout / Spatial Grid Token |
| `--section-stack-gap` | `2.25rem` | Layout / Spatial Grid Token |
| `--section-stack-gap-tight` | `2.25rem` | Layout / Spatial Grid Token |
| `--form-gap` | `1.25rem` | Layout / Spatial Grid Token |
| `--fieldset-gap` | `1rem` | Layout / Spatial Grid Token |
| `--form-control-gap` | `0.625rem` | Layout / Spatial Grid Token |
| `--checkbox-control-gap` | `0.75rem` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.jdgm-settings-script> — `bluntumbrellas-com`)**:
   - Landmark `<header class="jdgm-settings-script">` (`1440x75px`) hosting `BLUNT Umbrellas · Built to Resist Ev` navigation (`Regular Models · Limited Editions · UV Umbrellas · All Umbrellas · Our Design`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-source-attribution="shopify.loadfeatures"`, `data-source-attribution="shopify.dynamic_check..."`, `data-source-attribution="shopify.dynamic_check..."`), and stylesheet rule `.shopify-payment-button__button--... { visibility:hidden }`.
2. **Hero Stage & Focal Lead (<section.shopify-section> — `BLUNT Umbrellas EU`)**:
   - Landmark `<section class="shopify-section shopify-section--neo-hero">` presenting display lead `BLUNT Umbrellas EU` and copy excerpt *"Our smallest and lightest yet. Folds to just 26 cm and slips into"* over `#f1f1f1` canvas and `#1c1c1c` ink.
3. **Primary Showcase & Content Grid (<section.shopify-section--scrolling-content> — `What others say about Blunt`)**:
   - Landmark `<section class="shopify-section shopify-section--scrolling-content">` rendering section `What others say about Blunt` with copy *"Your trusted sidekick. Compact, collapsible and convenient for li"*, asset references (`blunt_favicon.png`, `fonts.shopifycdn.com`, `poppins_n4.0ba78fa5af9b0e1a374041...`, `es-modules-shim.2.4.0.js`), and grid rule `opify-payment-button__button--unb... { background-color:1990c6;padding:1em 2em }`.
4. **Interactive Detail & Feature Matrix (<section.shopify-section:nth(2)> — `Your trusted sidekick. Compact, co`)**:
   - Landmark `<section class="shopify-section">` framing `Your trusted sidekick. Compact, collapsible and ` and `The original full length umbrella, inspired by t` (*"The original full length umbrella, inspired by tradition and desi"*) with `#ffffff` surface cards, `#ffc700` accents, and `ptions.shopify-payment-button__sk... { width:50%;margin-left:25%;margin-right:25%;border-radius:4px!important;h... }`.
5. **Colophon & Global Directory Footer (<footer.analytics> — `https://bluntumbrellas.com`)**:
   - Landmark `<footer class="analytics">` anchoring `BLUNT Umbrellas · Built to Resis` footer links (`Regular Models · Limited Editions · UV Umbrellas · All Umbrellas · Our Design`), copy *"In the business of keeping you dry with relentless performan"*, and `#cccccc` structural dividers.
