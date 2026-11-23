---
title: "UI & UX Architecture: agnestoth-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: agnestoth-com

## Overview & Design Identity
- **Target**: `agnestoth-com` (**AGNESTOTH · House of Luxurious Embroidery**)
- **Production URL**: [https://agnestoth.com](https://agnestoth.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#121212` ink, `#1990c6` accent)
- **Summary**: Discover one-of-a-kind luxury embroidered handbags by AGNESTOTH, created in Budapest from apple leather with original artist-led designs.
- **Total Clean CSS Variables Extracted**: `232` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `FreightBig Pro`
- **Body Font Stack**: `Jost`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 100px`, `line-height: 100px`, `font-weight: 300`); rule `h1` (`font-size: 5.2rem`, `line-height: 1.3`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 34px`, `line-height: 34px`, `font-weight: 400`, `letter-spacing: 0.34px`); rule `h2` (`font-size: 2.8rem`, `line-height: 1.3`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 28.8px`, `font-weight: 400`, `letter-spacing: 0.6px`); CSS variables `--font-body-family: Assistant, sans-serif`, `--font-body-style: normal`, `--font-body-weight: 400`; rule `p` (`font-size: 1.6rem`, `line-height: 2.4rem`, `letter-spacing: .02em`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 28.8px`, `font-weight: 400`, `letter-spacing: 0.6px`); CSS variables `--agnes-label-size: 1.3rem`, `--agnes-label-weight: 500`, `--agnes-label-tracking: .14em`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#121212` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f0eee9` | `var(--agnes-tile-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#1990c6` | `.shopify-payment-button__button... { background-color: #1990c6 }` |
| **Secondary / Muted Copy** | `#707c7a` | `var(--agnes-muted)` in `:root` |
| **Structural Hairline Border** | `#d1d3d3` | `var(--agnes-hairline)` in `:root` (`rgba(46, 57, 55, .22)`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-background` | `255,255,255` | Canvas / Surface Token |
| `--gradient-background` | `#FFFFFF` | Canvas / Surface Token |
| `--color-foreground` | `18,18,18` | Typography Ink Token |
| `--color-background-contrast` | `191,191,191` | Canvas / Surface Token |
| `--color-shadow` | `18,18,18` | Brand / Palette Token |
| `--color-button` | `18,18,18` | Brand / Palette Token |
| `--color-button-text` | `255,255,255` | Typography Ink Token |
| `--color-secondary-button` | `255,255,255` | Brand / Palette Token |
| `--color-secondary-button-text` | `18,18,18` | Typography Ink Token |
| `--color-link` | `18,18,18` | Typography Ink Token |
| `--color-badge-foreground` | `18,18,18` | Typography Ink Token |
| `--color-badge-background` | `255,255,255` | Canvas / Surface Token |
| `--color-badge-border` | `18,18,18` | Brand / Palette Token |
| `--payment-terms-background-color` | `rgb(255 255 255)` | Canvas / Surface Token |
| `--font-body-family` | `Assistant, sans-serif` | Typography / Scale Token |
| `--font-body-style` | `normal` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.shopify-section> — `agnestoth-com`)**:
   - Landmark `<header class="shopify-section shopify-section-group-header-group">` (`1360x78px`) hosting `AGNESTOTH · House of Luxurious Embro` navigation (`Bespoke Atelier · Our World · The Artist · Shop`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-shopify`, `data-shop-id="110210285906"`, `data-venmo-supported="false"`), and stylesheet rule `.shopify-payment-button__button--... { visibility:hidden }`.
2. **Hero Stage & Focal Lead (<section.shopify-section> — `House of Luxurious Embroidery`)**:
   - Landmark `<section class="shopify-section agnes-section">` presenting display lead `House of Luxurious Embroidery` and copy excerpt *"AGNESTOTH • est. Budapest"* over `#ffffff` canvas and `#121212` ink.
3. **Primary Showcase & Content Grid (<section.agnes-hero> — `H o u s e o f L u x u r i o u s E `)**:
   - Landmark `<section class="agnes-hero color-scheme-1">` rendering section `H o u s e o f L u x u r i o u s E m b r o i d e r y` with copy *"A g n e s T o t h • e s t . B u d a p e s t"*, asset references (`693823798186760`, `fbevents.js`, `favicon.ico`, `favicon-32x32.png`), and grid rule `opify-payment-button__button--unb... { background-color:1990c6;padding:1em 2em }`.
4. **Interactive Detail & Feature Matrix (<section.agnes-section> — `The Poppy Collection`)**:
   - Landmark `<section class="shopify-section agnes-section">` framing `The Poppy Collection` and `Discover the Poppy Collection` (*"Each handcrafted piece is more than a handbag — it is a one-of-a-"*) with `#f0eee9` surface cards, `#1990c6` accents, and `ptions.shopify-payment-button__sk... { width:50%;margin-left:25%;margin-right:25%;border-radius:4px!important;h... }`.
5. **Colophon & Global Directory Footer (<footer.shopify-section> — `https://agnestoth.com`)**:
   - Landmark `<footer class="shopify-section shopify-section-group-footer-group">` anchoring `AGNESTOTH · House of Luxurious E` footer links (`Bespoke Atelier · Our World · The Artist · Shop`), copy *"— Agnes Toth, Artist & Founder"*, and `#d1d3d3` structural dividers.
