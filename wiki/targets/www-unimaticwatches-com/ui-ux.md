---
title: "UI & UX Architecture: www-unimaticwatches-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-unimaticwatches-com

## Overview & Design Identity
- **Target**: `www-unimaticwatches-com` (**UNIMATIC Watches**)
- **Production URL**: [https://www.unimaticwatches.com/?srsltid=AfmBOor1S-k1GXW2WUlgmQd-YbKuDQWHeKBxyRjTFNyURmTvXoeNJXHD](https://www.unimaticwatches.com/?srsltid=AfmBOor1S-k1GXW2WUlgmQd-YbKuDQWHeKBxyRjTFNyURmTvXoeNJXHD)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f6f6f6` canvas, `#000000` ink, `#afff00` accent)
- **Summary**: Discover UNIMATIC watches, an independent Italian watch brand creating minimalist, functional watches made in Italy. Explore our Classic...
- **Total Clean CSS Variables Extracted**: `93` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Helvetica Neue`
- **Body Font Stack**: `Helvetica Neue`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 24px`, `line-height: 29.304px`, `font-weight: 700`, `letter-spacing: -0.48px`)
- **Section Heading (`H2`)**: live computed `h3 (primary section heading)` (`font-size: 28.08px`, `line-height: 34.2857px`, `font-weight: 700`, `letter-spacing: -0.48px`); CSS variables `--fs-subtitle: 1.6rem`; rule `h2` (`font-size: 120%`, `font-weight: bold`)
- **Body Copy**: live computed `body` (`font-size: 12px`, `line-height: 14.652px`, `font-weight: 400`); CSS variables `--fs-body: 1.2rem`; rule `p` (`line-height: 2.8rem`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: 14.652px`, `font-weight: 400`); CSS variables `--font-mono: "JetBrains Mono", ui-monospace, "SFMono-Regular", Menlo, monospace`, `--fs-mono: 1.2rem`, `--lh-mono: 1.32`; rule `small` (`font-size: var(--fs-eyebrow)`, `line-height: var(--lh-mono)`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f6f6f6` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `.b2b-terms { background-color: white }` (`#ffffff`) |
| **Interactive Accent / Highlight** | `#afff00` | `var(--color-accent)` in `:root` |
| **Secondary / Muted Copy** | `#222222` | `var(--color-tag-ink)` in `:root` |
| **Structural Hairline Border** | `#ffffff` | `on.loading>.loading-overlay__sp... { stroke: #ffffff }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--space-1` | `.4rem` | Layout / Spatial Grid Token |
| `--space-2` | `.8rem` | Layout / Spatial Grid Token |
| `--space-2-5` | `1rem` | Layout / Spatial Grid Token |
| `--space-3` | `1.2rem` | Layout / Spatial Grid Token |
| `--space-4` | `1.6rem` | Layout / Spatial Grid Token |
| `--space-5` | `2.4rem` | Layout / Spatial Grid Token |
| `--space-6` | `3.2rem` | Layout / Spatial Grid Token |
| `--color-tag-ink` | `#222` | Typography Ink Token |
| `--editorial-sticky-top` | `6.4rem` | Dimension / Scale Token |
| `--drawer-top-base` | `calc(var(--space-4) + var(--space-2-5) * 2 + 1.6rem + var(--space-2))` | Dimension / Scale Token |
| `--drawer-top` | `var(--drawer-top-base)` | Design System Custom Token |
| `--drawer-width` | `33rem` | Layout / Spatial Grid Token |
| `--sticky-top` | `calc(var(--drawer-top-base) + var(--space-6))` | Design System Custom Token |
| `--color-bg` | `#F6F6F6` | Canvas / Surface Token |
| `--color-ink` | `#000000` | Typography Ink Token |
| `--color-accent` | `#AFFF00` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.shopify-section> — `www-unimaticwatches-com`)**:
   - Landmark `<header class="shopify-section shopify-section-group-header-group">` (`1440x0px`) hosting `UNIMATIC Watches` navigation (`New in · Bracelets`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-shopify`, `data-shop-id="104415822154"`, `data-venmo-supported="false"`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.shopify-section> — `New Langhe Collection`)**:
   - Landmark `<section class="shopify-section hero">` presenting display lead `New Langhe Collection` and copy excerpt *"Truffle, Moss, Fog Dials"* over `#f6f6f6` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.product-carousel-section> — `Some landscapes are defined less b`)**:
   - Landmark `<section class="shopify-section product-carousel-section">` rendering section `Some landscapes are defined less by what can be s...` with copy *"A landscape interpreted through colour and texture."*, asset references (`596128728859448`, `fbevents.js`, `clarity.js`, `zg18q6f8jj`), and grid rule `html { font-size:10px;-webkit-text-size-adjust:100%;text-size-adjust:100% }`.
4. **Interactive Detail & Feature Matrix (<article.product-card> — `The ICON collection`)**:
   - Landmark `<article class="product-card">` framing `The ICON collection` and `Waterproof checked` (*"Meet The Collection"*) with `#ffffff` surface cards, `#afff00` accents, and `button { font:inherit;color:inherit;background:none;border:0;padding:0;cursor:poi... }`.
5. **Colophon & Global Directory Footer (<footer.shopify-section> — `https://www.unimaticwatches.com/?srsltid=AfmBOor1S-k1GXW2WUlgmQd-YbKuDQWHeKBxyRjTFNyURmTvXoeNJXHD`)**:
   - Landmark `<footer class="shopify-section shopify-section-group-footer-group">` anchoring `UNIMATIC Watches` footer links (`New in · Bracelets`), copy *"Limited Edition - Diver"*, and `#ffffff` structural dividers.
