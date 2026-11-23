---
title: "UI & UX Architecture: continuance-ai"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: continuance-ai

## Overview & Design Identity
- **Target**: `continuance-ai` (**Continuance - A novel by Chris Bennett**)
- **Production URL**: [https://continuance.ai/](https://continuance.ai/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f4f4f4` / `#343849`)
- **Summary**: A near-future thriller about the people we'd do anything to keep — and what it costs when we succeed.
- **Total Clean CSS Variables Extracted**: `46` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `objectSans`
- **Body Font Stack**: `Roboto Mono`
- **Monospace / Technical Font Stack**: `Roboto Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 187.864px`, `line-height: 216.044px`, `font-weight: 400`, `letter-spacing: -3px`); rule `,h1` (`font-size: var(--font-size-4xl)`)
- **Section Heading (`H2`)**: observed font-size ladder: `187.864px`, `16px`, `11.068px`, `.75rem`, `var(--font-size-sx)`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 18.4px`, `font-weight: 400`); CSS variables `--font-family-body: "Roboto Mono","Roboto Mono Fallback"`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 18.4px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f4f4f4` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `button` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#c8c8ca` | live computed `main` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#343849` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#343849` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#ffa500` | `to { stroke: #ffa500 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--hero-tilt-gap` | `5px` | Layout / Spatial Grid Token |
| `--c-brand-primary-rgb` | `52,56,73` | Brand / Palette Token |
| `--c-brand-primary` | `rgb(var(--c-brand-primary-rgb))` | Brand / Palette Token |
| `--c-brand-secondary-rgb` | `173,138,255` | Brand / Palette Token |
| `--c-brand-secondary` | `rgb(var(--c-brand-secondary-rgb))` | Brand / Palette Token |
| `--c-light-gray-rgb` | `217,217,217` | Canvas / Surface Token |
| `--c-light-gray` | `rgb(var(--c-light-gray-rgb))` | Canvas / Surface Token |
| `--c-orange-rgb` | `255,153,0,1` | Design System Custom Token |
| `--c-orange` | `rgb(var(--c-orange-rgb))` | Color / Atmospheric Token |
| `--c-bg-primary-rgb` | `244,244,244` | Canvas / Surface Token |
| `--c-bg-primary` | `rgb(var(--c-bg-primary-rgb))` | Canvas / Surface Token |
| `--c-bg-secondary-rgb` | `0,0,0` | Canvas / Surface Token |
| `--c-bg-secondary` | `rgb(var(--c-bg-secondary-rgb))` | Canvas / Surface Token |
| `--c-bg-tertiary-rgb` | `255,255,255` | Canvas / Surface Token |
| `--c-bg-tertiary` | `rgb(var(--c-bg-tertiary-rgb))` | Canvas / Surface Token |
| `--c-bg-soft-gray-rgb` | `244,244,244` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.SiteIndexNav_site-index-nav__60kV3> — `continuance-ai`)**:
   - Landmark `<nav class="SiteIndexNav_site-index-nav__60kV3">` (`1x1px`) hosting `Continuance - A novel by Chris Benne` navigation (`Get the book · Why now · About the author · Top secret · Privacy policy`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.Device_device__yuADF { position:absolute;top:0;left:0;width:100%;height:100% }`.
2. **Hero Stage & Focal Lead (<main.home> — `C O N T I N U A N C E`)**:
   - Landmark `<main class="home">` presenting display lead `C O N T I N U A N C E` and copy excerpt *"MAPPING NEURAL SIGNATURES..."* over `#f4f4f4` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<main.home:nth(2)> — `C o n t i n u a n c e`)**:
   - Landmark `<main class="home">` rendering section `C o n t i n u a n c e` with copy *"Mapping neural signatures..."*, asset references (`0807ff31c16ab04c.css`, `a4eac32ba22d1fcc.css`, `a5188067206b89ec.css`, `5b6568268f4e7c11.css`), and grid rule `.Device_device__rune___9Rho { border:0;outline:0;box-shadow:none;-webkit-appearance:none;-moz-appearan... }`.
4. **Interactive Detail & Feature Matrix (<main.home:nth(3)> — `Mapping neural signatures...`)**:
   - Landmark `<main class="home">` framing `Mapping neural signatures...` and `Synchronizing with Kaiku System _` (*"Synchronizing with Kaiku System _"*) with `#c8c8ca` surface cards, `#343849` accents, and `evice_device__rune___9Rho:focus-v... { outline:0;box-shadow:none }`.
5. **Colophon & Global Directory Footer (<footer.Footer_footer__2_6CR> — `https://continuance.ai/`)**:
   - Landmark `<footer class="Footer_footer__2_6CR">` anchoring `Continuance - A novel by Chris B` footer links (`Get the book · Why now · About the author · Top secret · Privacy policy`), copy *"Synchronizing with Kaiku System"*, and `#ffa500` structural dividers.
