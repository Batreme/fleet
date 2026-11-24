---
title: "UI & UX Architecture: navtec-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: navtec-com

## Overview & Design Identity
- **Target**: `navtec-com` (**Moab Adventure Tours · Navtec Expeditions Since 1896**)
- **Production URL**: [https://navtec.com/](https://navtec.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×5796px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ebe6d8` canvas, `#0000ee` ink, `#ff0000` accent)
- **Summary**: Explore Moab's canyons with expert guides. Rafting, 4x4 tours, canyoneering & hiking in Arches & Canyonlands. Family-owned since 1896. Bo...
- **Total Clean CSS Variables Extracted**: `95` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Eczar`
- **Body Font Stack**: `Geologica`
- **Monospace / Technical Font Stack**: `IBM Plex Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 52px`, `line-height: 65px`, `font-weight: 400`); CSS variables `--_headings---h1--font-family: var(--_fonts---font-headings)`, `--_headings---h1--font-size: 5.2rem`, `--_headings---h1--line-height: 1.25em`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 40px`, `line-height: 50px`, `font-weight: 400`); CSS variables `--_headings---h2--font-family: var(--_fonts---font-headings)`, `--_headings---h2--font-size: 4rem`, `--_headings---h2--line-height: 1.25em`
- **Body Copy**: live computed `body` (`font-size: 18px`, `line-height: 27px`, `font-weight: 400`); CSS variables `--_base-styles---body--background: var(--sand)`, `--_base-styles---body--font-family: var(--_fonts---font-base)`, `--_base-styles---typography--font-size-base: 1.8rem`; rule `p` (`font-size: var(--_base-styles---typograp...`, `line-height: var(--_base-styles---...`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 18px`, `line-height: 27px`, `font-weight: 400`); CSS variables `--_base-styles---typography--letter-spacing: 0em`, `--_headings---h1--letter-spacing: 0em`, `--_headings---h2--letter-spacing: 0em`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ebe6d8` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffff00` | `mark { background: #ffff00 }` |
| **Interactive Accent / Highlight** | `#ff0000` | `.list-steps-content-block a:hover { color: red }` (`#ff0000`) |
| **Secondary / Muted Copy** | `#062c3c` | live computed `body` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e2e2e2` | `blockquote { border-left: #e2e2e2 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--_base-styles---body--background` | `var(--sand)` | Canvas / Surface Token |
| `--_base-styles---body--font-family` | `var(--_fonts---font-base)` | Typography / Scale Token |
| `--_base-styles---body--font-color` | `var(--deep-teal)` | Brand / Palette Token |
| `--_base-styles---typography--font-size-base` | `1.8rem` | Typography / Scale Token |
| `--_base-styles---typography--line-height` | `1.5em` | Typography / Scale Token |
| `--_base-styles---typography--font-weight` | `400` | Typography / Scale Token |
| `--_base-styles---typography--letter-spacing` | `0em` | Typography / Scale Token |
| `--_headings---h1--font-family` | `var(--_fonts---font-headings)` | Typography Ink Token |
| `--_headings---h1--font-size` | `5.2rem` | Typography Ink Token |
| `--_headings---h1--line-height` | `1.25em` | Typography Ink Token |
| `--_headings---h1--font-weight` | `400` | Typography Ink Token |
| `--_headings---h1--letter-spacing` | `0em` | Typography Ink Token |
| `--_headings---h2--font-family` | `var(--_fonts---font-headings)` | Typography Ink Token |
| `--_headings---h2--font-size` | `4rem` | Typography Ink Token |
| `--_headings---h2--line-height` | `1.25em` | Typography Ink Token |
| `--_headings---h2--font-weight` | `400` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.nav> — `navtec-com`)**:
   - Landmark `<nav class="nav">` (`858x84px`) hosting `Moab Adventure Tours · Navtec Expedi` navigation (`Half Day · Full Day · 2-3 Days · 4-6 Days · River & Rafting`), DOM attributes (`data-wf-domain="navtec.com"`, `data-wf-page="6a310f67244daebf3f62c77e"`, `data-wf-site="6a310f64244daebf3f62c717"`, `data-wf-intellimize-customer-id="117402178"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.header> — `Wild Places, Thoughtfully Explored`)**:
   - Landmark `<section class="header">` presenting display lead `Wild Places, Thoughtfully Explored.` and copy excerpt *"Scramble through fins and potholes to two dramatic desert rappels"* over `#ebe6d8` canvas and `#0000ee` ink.
3. **Primary Showcase & Content Grid (<section.section> — `Scramble through fins and potholes`)**:
   - Landmark `<section class="section">` rendering section `Scramble through fins and potholes to two dramat` with copy *"Expeditions Browse Our Expeditions by Duration Half Day Full Day "*, asset references (`cdn.prod.website-files.com`, `navtec.webflow.shared.6acfbfa82.m...`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.section-wave> — `Expeditions Browse Our Expeditions`)**:
   - Landmark `<section class="section-wave">` framing `Expeditions Browse Our Expeditions by Duration H` and `Arches National Park` (*"Arches National Park"*) with `#ffff00` surface cards, `#ff0000` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://navtec.com/`)**:
   - Landmark `<footer class="footer">` anchoring `Moab Adventure Tours · Navtec Ex` footer links (`Half Day · Full Day · 2-3 Days · 4-6 Days · River & Rafting`), copy *"Canyonlands National Park"*, and `#e2e2e2` structural dividers.
