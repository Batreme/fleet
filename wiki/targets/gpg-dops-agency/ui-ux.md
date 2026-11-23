---
title: "UI & UX Architecture: gpg-dops-agency"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: gpg-dops-agency

## Overview & Design Identity
- **Target**: `gpg-dops-agency` (**Garvinpromo**)
- **Production URL**: [https://gpg.dops.agency/](https://gpg.dops.agency/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#003c97` ink, `#7fa1d5` accent)
- **Summary**: Welcome to Garvin Promotion Group, a leading provider of rebate management, spiffs, and loyalty incentive programs
- **Total Clean CSS Variables Extracted**: `43` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `PPMori`
- **Body Font Stack**: `PPMori`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 64px`, `line-height: 65.28px`, `font-weight: 400`, `letter-spacing: -3.2px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 64px`, `line-height: 65.28px`, `font-weight: 400`, `letter-spacing: -3.2px`)
- **Body Copy**: live computed `body` (`font-size: 22px`, `line-height: 22px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 22px`, `line-height: 22px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#003c97` | live computed `h2` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#b0c8eb` | `:before { background-color: #b0c8eb }` |
| **Interactive Accent / Highlight** | `#7fa1d5` | `.btn--point__c { background-color: #7fa1d5 }` |
| **Secondary / Muted Copy** | `#898995` | live computed `h1` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#7fa1d5` | `:before { border: #7fa1d5 }` |
| **Variable Token (`--vc-clr-primary`)** | `#000000` | `var(--vc-clr-primary)` in `:root` |
| **Variable Token (`--vc-clr-secondary`)** | `#090f20` | `var(--vc-clr-secondary)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--vc-clr-primary` | `#000` | Brand / Palette Token |
| `--vc-clr-secondary` | `#090f207f` | Brand / Palette Token |
| `--vc-clr-white` | `#fff` | Canvas / Surface Token |
| `--vc-icn-width` | `1.2em` | Layout / Spatial Grid Token |
| `--vc-nav-width` | `30px` | Layout / Spatial Grid Token |
| `--vc-nav-height` | `30px` | Layout / Spatial Grid Token |
| `--vc-nav-border-radius` | `0` | Layout / Spatial Grid Token |
| `--vc-nav-color` | `var(--vc-clr-primary)` | Brand / Palette Token |
| `--vc-nav-color-hover` | `var(--vc-clr-secondary)` | Brand / Palette Token |
| `--vc-nav-background` | `transparent` | Canvas / Surface Token |
| `--vc-pgn-width` | `12px` | Layout / Spatial Grid Token |
| `--vc-pgn-height` | `4px` | Layout / Spatial Grid Token |
| `--vc-pgn-margin` | `4px` | Layout / Spatial Grid Token |
| `--vc-pgn-border-radius` | `0` | Elevation / Border Token |
| `--vc-pgn-background-color` | `var(--vc-clr-secondary)` | Canvas / Surface Token |
| `--vc-pgn-active-color` | `var(--vc-clr-primary)` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `gpg-dops-agency`)**:
   - Landmark `<header class="header header--light">` (`1430x79px`) hosting `Garvinpromo` navigation (`Services Services · About us About us · Let's Talk`), DOM attributes (`data-v-537c3597`, `data-v-5f87b270`, `data-v-05812e15`, `data-v-f8de3fbd`), and stylesheet rule `svg { display:block;height:100%;width:100% }`.
2. **Hero Stage & Focal Lead (<section.carousel> — `Welcome to Garvin Promotion Group,`)**:
   - Landmark `<section class="carousel home-strategic__carousel">` presenting display lead `Welcome to Garvin Promotion Group, a leading prov...` and copy excerpt *"Garvin Promotion Group"* over `#ffffff` canvas and `#003c97` ink.
3. **Primary Showcase & Content Grid (<section.carousel:nth(2)> — `Garvin Promotion Group`)**:
   - Landmark `<section class="carousel">` rendering section `Garvin Promotion Group` with copy *"Clients success Clients success"*, asset references (`garvinpromo.com`, `favicon.ico`, `favicon-16x16.png`, `favicon-32x32.png`), and grid rule `ellipse { animation:circle-5f87b270 1.8s ease infinite }`.
4. **Interactive Detail & Feature Matrix (<section.preloader--initial> — `Clients success Clients success`)**:
   - Landmark `<section class="preloader--initial">` framing `Clients success Clients success` and `Garvin Promotion Group 10220 South 51st Street P` (*"Garvin Promotion Group 10220 South 51st Street Phoenix, AZ 85044"*) with `#b0c8eb` surface cards, `#7fa1d5` accents, and `ellipse:first-child { animation-delay:.12s!important }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://gpg.dops.agency/`)**:
   - Landmark `<footer class="footer bg-dark">` anchoring `Garvinpromo` footer links (`Services Services · About us About us · Let's Talk`), copy *"Welcome to Garvin Promotion Group, a leading provider of reb"*, and `#7fa1d5` structural dividers.
