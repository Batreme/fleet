---
title: "UI & UX Architecture: www-kubehotel-saint-tropez-com_fr"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-kubehotel-saint-tropez-com_fr

## Overview & Design Identity
- **Target**: `www-kubehotel-saint-tropez-com_fr` (**Layne Saint-Tropez, hôtel 5 étoiles : ouverture le 1er mai 2027**)
- **Production URL**: [https://www.kubehotel-saint-tropez.com/fr](https://www.kubehotel-saint-tropez.com/fr)
- **Final Redirected URL**: [https://www.layne-sainttropez.com/fr](https://www.layne-sainttropez.com/fr)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fdf9f4` canvas, `#000000` ink, `#0082f3` accent)
- **Summary**: Face au golfe de Saint-Tropez, découvrez Layne, un nouvel hôtel 5 étoiles à Gassin. Ouverture le 1er mai 2027. Contact : info@layne-saint...
- **Total Clean CSS Variables Extracted**: `160` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Kallisto`
- **Body Font Stack**: `Anth`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 30.3333px`, `line-height: normal`, `font-weight: 700`, `letter-spacing: 1.21333px`); rule `h1` (`font-size: var(--_text-style---font-size)`, `line-height: var(--_text-style---l...`, `letter-spacing: var(--_text-style---l...`, `font-weight: var(--_text-s...`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: var(--_text-style---font-size)`, `line-height: var(--_text-style---l...`, `letter-spacing: var(--_text-style---l...`, `font-weight: var(--_text-s...`)
- **Body Copy**: live computed `body` (`font-size: 14px`, `line-height: 21px`, `font-weight: 300`, `letter-spacing: -0.28px`); rule `p` (`line-height: var(--_typography---l...`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 14px`, `line-height: 21px`, `font-weight: 300`, `letter-spacing: -0.28px`); CSS variables `--_text-style---letter-spacing: var(--_typography---letter-spacing--tight)`, `--_responsive---small: 0`, `--_responsive---xsmall: 0`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#fdf9f4` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffff00` | `mark { background: #ffff00 }` |
| **Interactive Accent / Highlight** | `#0082f3` | `.w-dropdown-link.w--current { color: #0082f3 }` |
| **Secondary / Muted Copy** | `#ffffff` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e2e2e2` | `blockquote { border-left: #e2e2e2 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--_theme---background` | `var(--swatch--beige)` | Canvas / Surface Token |
| `--_text-style---font-family` | `var(--_typography---font--primary-family)` | Typography Ink Token |
| `--_theme---text` | `var(--swatch--black)` | Typography Ink Token |
| `--_text-style---font-size` | `var(--_typography---font-size--text-main)` | Typography Ink Token |
| `--_text-style---line-height` | `var(--_typography---line-height--large)` | Typography Ink Token |
| `--_text-style---font-weight` | `var(--_typography---font--primary-light)` | Typography Ink Token |
| `--_text-style---letter-spacing` | `var(--_typography---letter-spacing--tight)` | Typography Ink Token |
| `--radius--main` | `.5rem` | Elevation / Border Token |
| `--_theme---background-2` | `var(--swatch--beige-2)` | Canvas / Surface Token |
| `--site--column-count` | `12` | Layout / Spatial Grid Token |
| `--_responsive---large` | `1` | Design System Custom Token |
| `--_responsive---medium` | `0` | Design System Custom Token |
| `--_responsive---small` | `0` | Design System Custom Token |
| `--_responsive---xsmall` | `0` | Design System Custom Token |
| `--max-width--small` | `calc(var(--site--viewport-max)*1rem)` | Layout / Spatial Grid Token |
| `--_gap---size` | `var(--site--gutter)` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.hero_header_wrap> — `www-kubehotel-saint-tropez-com_fr`)**:
   - Landmark `<header class="hero_header_wrap">` (`1356x40px`) hosting `Layne Saint-Tropez, hôtel 5 étoiles ` navigation (`fr · en · it · ru`), DOM attributes (`data-wf-domain="www.layne-sainttropez..."`, `data-wf-page="69c122f05101301b0245c797"`, `data-wf-site="69c122f05101301b0245c7c6"`, `data-nosnippet`), and stylesheet rule `root { --swiper-theme-color:007aff }`.
2. **Hero Stage & Focal Lead (<section.hero_wrap> — `LES PLUS BELLES VACANCES ONT LE GO`)**:
   - Landmark `<section class="hero_wrap u-section">` presenting display lead `LES PLUS BELLES VACANCES ONT LE GOÛT DE L’INSOUCI...` and copy excerpt *"HÔTEL - RESTAURANT - SPA - PISCINES"* over `#fdf9f4` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.u-section> — `Les plus belles vacances ont le go`)**:
   - Landmark `<section class="hero_wrap u-section">` rendering section `Les plus belles vacances ont le goût de l’insouci...` with copy *"Hôtel - Restaurant - Spa - Piscines"*, asset references (`cdn.prod.website-files.com`, `layne-sainttropez.webflow.shared....`, `state.js`, `widgetIcon.min.js`), and grid rule `.swiper { margin-left:auto;margin-right:auto;position:relative;overflow:hidden;lis... }`.
4. **Interactive Detail & Feature Matrix (<section.u-theme-dark> — `Hôtel - Restaurant - Spa - Piscine`)**:
   - Landmark `<section class="hero_wrap u-section">` framing `Hôtel - Restaurant - Spa - Piscines` and `Ouverture 1 er mai 2027` (*"Ouverture 1 er mai 2027"*) with `#ffff00` surface cards, `#0082f3` accents, and `.swiper-vertical>.swiper-wrapper { flex-direction:column }`.
5. **Colophon & Global Directory Footer (<footer.CybotCookiebotDialogContentWrapper> — `https://www.kubehotel-saint-tropez.com/fr`)**:
   - Landmark `<footer class="CybotCookiebotDialogContentWrapper">` anchoring `Layne Saint-Tropez, hôtel 5 étoi` footer links (`fr · en · it · ru`), copy *"Informations et réservations : info@layne-sainttropez.com"*, and `#e2e2e2` structural dividers.
