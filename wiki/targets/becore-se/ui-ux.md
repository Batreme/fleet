---
title: "UI & UX Architecture: becore-se"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: becore-se

## Overview & Design Identity
- **Target**: `becore-se` (**Becore**)
- **Production URL**: [https://becore.se/](https://becore.se/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#007bff` accent)
- **Summary**: Experience the latest in activewear from our new Becore collection
- **Total Clean CSS Variables Extracted**: `240` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Cabin`
- **Body Font Stack**: `Cabin`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 28px`, `line-height: 39.2px`, `font-weight: 700`, `letter-spacing: -0.14px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 28.8925px`, `line-height: 37.5602px`, `font-weight: 400`, `letter-spacing: 0.288925px`); rule `h2` (`font-size: 120%`, `font-weight: bold`)
- **Body Copy**: live computed `body` (`font-size: 14px`, `line-height: 19.6px`, `font-weight: 400`, `letter-spacing: -0.14px`); CSS variables `--text-base: 0.875rem`, `--drawer-body-padding-block: min(2rem, var(--container-gutter))`, `--drawer-body-padding-inline: min(2rem, var(--container-gutter))`; rule `p` (`line-height: 1.3`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 14px`, `line-height: 19.6px`, `font-weight: 400`, `letter-spacing: -0.14px`); CSS variables `--subheading-letter-spacing: -0.01em`, `--heading-letter-spacing: 0.01em`, `--text-letter-spacing: -0.01em`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `section` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#56b6c2` | `.spinner>div { background-color: #56b6c2 }` |
| **Interactive Accent / Highlight** | `#007bff` | `.btn-primary { background-color: #007bff }` |
| **Secondary / Muted Copy** | `#392d2b` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#007bff` | `.btn-primary { border-color: #007bff }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--container-max-width` | `100%` | Layout / Spatial Grid Token |
| `--container-gutter` | `1.25rem` | Layout / Spatial Grid Token |
| `--section-vertical-spacing` | `2rem` | Layout / Spatial Grid Token |
| `--section-stack-row-gap` | `1.5rem` | Layout / Spatial Grid Token |
| `--form-gap` | `1rem` | Layout / Spatial Grid Token |
| `--fieldset-gap` | `0.5rem` | Layout / Spatial Grid Token |
| `--form-control-gap` | `0.5rem` | Layout / Spatial Grid Token |
| `--checkbox-control-gap` | `0.75rem` | Layout / Spatial Grid Token |
| `--input-padding-block` | `0.65rem` | Layout / Spatial Grid Token |
| `--input-padding-inline` | `1rem` | Layout / Spatial Grid Token |
| `--checkbox-size` | `0.875rem` | Layout / Spatial Grid Token |
| `--product-list-column-gap` | `0.125rem` | Layout / Spatial Grid Token |
| `--product-list-row-gap` | `1.5rem` | Layout / Spatial Grid Token |
| `--transform-logical-flip` | `1` | Design System Custom Token |
| `--transform-origin-start` | `left` | Design System Custom Token |
| `--transform-origin-end` | `right` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.hydrated> — `becore-se`)**:
   - Landmark `<header class="hydrated">` (`1440x48px`) hosting `Becore` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-locksmith`, `data-styles`, `data-shop-id="85529952592"`), and stylesheet rule `after { box-sizing:border-box;border-style:solid;border-width:0;border-color:rgb... }`.
2. **Hero Stage & Focal Lead (<section.shopify-section> — `Becore`)**:
   - Landmark `<section class="shopify-section shopify-section--slideshow">` presenting display lead `Becore` and copy excerpt *"Becore is a Swedish boutique fitness and wellness brand, bringing"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.shopify-section--vg-media-tabs> — `Welcome to Becore`)**:
   - Landmark `<section class="shopify-section shopify-section--vg-media-tabs">` rendering section `Welcome to Becore` with copy *"Five studios across Stockholm, open seven days a week from early "*, asset references (`mixpanel-2-latest.min.js`, `255516463088201`, `fbevents.js`, `jquery-3.6.4.min-dad6fdf250e31dfa...`), and grid rule `hr.horizontal-separator { border-width:0 0 0 1px;width:1px;height:100% }`.
4. **Interactive Detail & Feature Matrix (<section.shopify-section:nth(2)> — `Move with us`)**:
   - Landmark `<section class="shopify-section shopify-section--vg-media-tabs">` framing `Move with us` and `Digital studio` (*"Becore Signature class"*) with `#56b6c2` surface cards, `#007bff` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.shopify-pc__banner__dialog> — `https://becore.se/`)**:
   - Landmark `<footer class="shopify-pc__banner__dialog">` anchoring `Becore` footer links (`Overview · Index · Archive · About · Contact`), copy *"A 50-minute, full-body strength workout on the Becore Reform"*, and `#007bff` structural dividers.
