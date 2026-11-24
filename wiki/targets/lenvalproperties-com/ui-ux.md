---
title: "UI & UX Architecture: lenvalproperties-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: lenvalproperties-com

## Overview & Design Identity
- **Target**: `lenvalproperties-com` (**Lenval Properties — Creators of Refined Living & Iconic Spaces**)
- **Production URL**: [https://lenvalproperties.com](https://lenvalproperties.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×1744px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#211a19` / `#0082f3`)
- **Summary**: Boutique residential developments in Abu Dhabi, built with intention and designed to endure.
- **Total Clean CSS Variables Extracted**: `177` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Financier Display`
- **Body Font Stack**: `Helvetica Now Display`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 57.6px`, `line-height: 43.2px`, `font-weight: 400`, `letter-spacing: -1.8432px`); CSS variables `--_fonts---font-display: "Financier Display","Times New Roman",sans-serif`, `--_fonts---h1--size: calc(64rem/var(--_special-units---scale-ratio))`, `--_fonts---h1--line-height: 75%`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 57.6px`, `line-height: 43.2px`, `font-weight: 400`, `letter-spacing: -1.8432px`); CSS variables `--_fonts---h2--size: calc(40rem/var(--_special-units---scale-ratio))`, `--_fonts---h2--line-height: 100%`, `--_fonts---h2--letter-spacing: -.024em`
- **Body Copy**: live computed `body` (`font-size: 14.4px`, `line-height: 14.4px`, `font-weight: 400`); CSS variables `--_fonts---font-body: "Helvetica Now Display",Arial,sans-serif`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 14.4px`, `line-height: 14.4px`, `font-weight: 400`); CSS variables `--_fonts---h1--letter-spacing: -.032em`, `--_fonts---h2--letter-spacing: -.024em`, `--_fonts---h3--letter-spacing: 0em`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#211a19` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#222222` | `.w-slider-nav-invert>div.w-active { background-color: #222222 }` |
| **Interactive Accent / Highlight** | `#0082f3` | `.w-dropdown-link.w--current { color: #0082f3 }` |
| **Secondary / Muted Copy** | `#f9f4ee` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#3898ec` | `.w-select:focus { border-color: #3898ec }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--_fonts---font-body` | `"Helvetica Now Display",Arial,sans-serif` | Typography / Scale Token |
| `--_colors---base-1000--primary` | `var(--_global-colors---base-1000--100)` | Brand / Palette Token |
| `--_fonts---font-display` | `"Financier Display","Times New Roman",sans-serif` | Typography / Scale Token |
| `--_fonts---h1--size` | `calc(64rem/var(--_special-units---scale-ratio))` | Typography / Scale Token |
| `--_fonts---h1--line-height` | `75%` | Typography / Scale Token |
| `--_fonts---h1--letter-spacing` | `-.032em` | Typography / Scale Token |
| `--_fonts---h2--size` | `calc(40rem/var(--_special-units---scale-ratio))` | Typography / Scale Token |
| `--_fonts---h2--line-height` | `100%` | Typography / Scale Token |
| `--_fonts---h2--letter-spacing` | `-.024em` | Typography / Scale Token |
| `--_fonts---h3--size` | `calc(16rem/var(--_special-units---scale-ratio))` | Typography / Scale Token |
| `--_fonts---h3--line-height` | `100%` | Typography / Scale Token |
| `--_fonts---h3--letter-spacing` | `0em` | Typography / Scale Token |
| `--_fonts---h4--size` | `0rem` | Typography / Scale Token |
| `--_fonts---h4--line-height` | `100%` | Typography / Scale Token |
| `--_fonts---h4--letter-spacing` | `-.048em` | Typography / Scale Token |
| `--_fonts---h5--size` | `0rem` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `lenvalproperties-com`)**:
   - Landmark `<header class="header theme_on-color">` (`1440x43px`) hosting `Lenval Properties — Creators of Refi` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-wf-domain="lenvalproperties.com"`, `data-wf-page="69e0bb41d2ab22009f0e60bb"`, `data-wf-site="69e0bb41d2ab22009f0e60c1"`, `data-barba="wrapper"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.section> — `Creators of Refined Living & Iconi`)**:
   - Landmark `<section class="section theme_on-color">` presenting display lead `Creators of Refined Living & Iconic Spaces` and copy excerpt *"TO CRAFT EXCEPTIONAL PROPERTIES AND REFINED EXPERIENCES."* over `#211a19` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.theme_on-dark> — `Lenval develops timeless landmarks`)**:
   - Landmark `<section class="section theme_on-dark">` rendering section `Lenval develops timeless landmarks shaped by arch...` with copy *"Creators of Refined"*, asset references (`cdn.prod.website-files.com`, `lenvalproperties.webflow.shared.2...`, `6a8c839c1d892f3111d574bd_landscap... (This experience is designed for portr...)`, `6a8c839c1d892f3111d574bc_landscap...`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.section:nth(2)> — `Exceptional Exceptional Spaces for`)**:
   - Landmark `<section class="section theme_on-dark">` framing `Exceptional Exceptional Spaces for Refined Living` and `Architecture for a Bespoke Life` (*"s c r o l l t o e x p l o r e s c r o l l t o e x p l o r e"*) with `#222222` surface cards, `#0082f3` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.section> — `https://lenvalproperties.com`)**:
   - Landmark `<footer class="section clip">` anchoring `Lenval Properties — Creators of ` footer links (`Overview · Index · Archive · About · Contact`), copy *"Jubail Island, Abu Dhabi"*, and `#3898ec` structural dividers.
