---
title: "UI & UX Architecture: www-motorq-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-motorq-com

## Overview & Design Identity
- **Target**: `www-motorq-com` (**Motorq · Turn Connected Vehicle Data Into Decisions**)
- **Production URL**: [https://www.motorq.com/](https://www.motorq.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f3f0ec` canvas, `#1c1c1c` ink, `#ffa500` accent)
- **Summary**: More than telematics. Motorq turns data from 25+ automaker brands into decisions, with no hardware to install. Run safer, leaner, more pr...
- **Total Clean CSS Variables Extracted**: `281` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Manrope`
- **Body Font Stack**: `Manrope`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 56px`, `line-height: 61.6px`, `font-weight: 400`); CSS variables `--_typography---h1--size: 3.5rem`, `--_typography---h1--line-height: 1.1`, `--_typography---h1--weight: var(--_typography---weights--400-normal)`; rule `h1` (`font-size: 2.125rem`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 64px`, `line-height: 70.4px`, `font-weight: 400`); CSS variables `--_typography---h2--size: 3rem`, `--_typography---h2--line-height: 1.1`, `--_typography---h2--weight: var(--_typography---weights--400-normal)`; rule `h2` (`font-size: 1.125rem`, `font-weight: var(--_typogr...`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 22.4px`, `font-weight: 400`); CSS variables `--_themes---typography--paragraph: var(--_color-palette---black)`; rule `p` (`font-size: var(--_typography---text-md--...`, `line-height: 1.5`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 22.4px`, `font-weight: 400`); CSS variables `--_typography---base--letter-spacing: 0rem`, `--_typography---h1--letter-spacing: 0rem`, `--_typography---h2--letter-spacing: 0rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f3f0ec` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#1c1c1c` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f59958` | live computed `footer` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ffa500` | `.arrow-button:hover { color: orange }` (`#ffa500`) |
| **Secondary / Muted Copy** | `#686868` | `var(--_themes---form--input-placeholder)` in `:root` |
| **Structural Hairline Border** | `#c8c6c2` | `var(--_themes---form--input-border)` in `:root` (`1c1c1c33`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--_themes---background--primary` | `var(--_color-palette---cream)` | Canvas / Surface Token |
| `--_typography---base--font` | `var(--_typography---primary-font)` | Typography / Scale Token |
| `--_themes---typography--paragraph` | `var(--_color-palette---black)` | Brand / Palette Token |
| `--_typography---base--size` | `1rem` | Layout / Spatial Grid Token |
| `--_typography---base--line-height` | `1.4` | Typography / Scale Token |
| `--_typography---base--weight` | `var(--_typography---weights--400-normal)` | Design System Custom Token |
| `--_typography---base--letter-spacing` | `0rem` | Typography / Scale Token |
| `--_typography---primary-font` | `Manrope,Arial,sans-serif` | Brand / Palette Token |
| `--_themes---typography--heading` | `var(--_color-palette---black)` | Typography Ink Token |
| `--_typography---h1--size` | `3.5rem` | Typography / Scale Token |
| `--_typography---h1--line-height` | `1.1` | Typography / Scale Token |
| `--_typography---h1--weight` | `var(--_typography---weights--400-normal)` | Typography / Scale Token |
| `--_typography---h1--letter-spacing` | `0rem` | Typography / Scale Token |
| `--_typography---h2--size` | `3rem` | Typography / Scale Token |
| `--_typography---h2--line-height` | `1.1` | Typography / Scale Token |
| `--_typography---h2--weight` | `var(--_typography---weights--400-normal)` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.nav_menu> — `www-motorq-com`)**:
   - Landmark `<nav class="nav_menu w-nav-menu">` (`640x38px`) hosting `Motorq · Turn Connected Vehicle Data` navigation (`Commercial Fleets · Rental Fleets · Dealerships · Lenders · OEMs`), DOM attributes (`data-wf-domain="www.motorq.com"`, `data-wf-page="6a61fa87ccdad47899c19eb0"`, `data-wf-site="6a61fa87ccdad47899c19edd"`, `data-ads-portal-id="44687642"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Turn vehicle intelligence into act`)**:
   - Landmark `<section class="hero u-overflow-hidden">` presenting display lead `Turn vehicle intelligence into action` and copy excerpt *"Motorq turns raw vehicle signals into confident decisions for fle"* over `#f3f0ec` canvas and `#1c1c1c` ink.
3. **Primary Showcase & Content Grid (<section.section> — `Turn vehicle intelligence into act`)**:
   - Landmark `<section class="section u-bg-transparent">` rendering section `Turn vehicle intelligence into action into action` with copy *"Thursday, December 10"*, asset references (`cdn.prod.website-files.com`, `motorq123.webflow.shared.f3e1ce02...`, `pixels.js`, `44687642.js`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.u-bg-transparent> — `Live Webinar: Scaling Connected Fl`)**:
   - Landmark `<section class="section u-bg-transparent">` framing `Live Webinar: Scaling Connected Fleets Without Ha...` and `Skip telematics devices. Connect directly to OEM-...` (*"The infrastructure powering every decision"*) with `#f59958` surface cards, `#ffa500` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://www.motorq.com/`)**:
   - Landmark `<footer class="footer">` anchoring `Motorq · Turn Connected Vehicle ` footer links (`Commercial Fleets · Rental Fleets · Dealerships · Lenders · OEMs`), copy *"Vehicle-direct data from 25+ automotive brands, no hardware "*, and `#c8c6c2` structural dividers.
