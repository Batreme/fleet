---
title: "UI & UX Architecture: www-avilus-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-avilus-com

## Overview & Design Identity
- **Target**: `www-avilus-com` (**Avilus · Dual-Use Uncrewed Aircraft for Evacuation, Logistics and Survei...**)
- **Production URL**: [https://www.avilus.com/](https://www.avilus.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f7f7f7` canvas, `#183032` ink, `#0082f3` accent)
- **Summary**: Manufacturer and certified operator of dual-use uncrewed aircraft for medical evacuation, logistics, surveillance, and reconnaissance.
- **Total Clean CSS Variables Extracted**: `164` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `Robotomono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 72px`, `line-height: 72px`, `font-weight: 700`, `letter-spacing: -2.16px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 30px`, `line-height: 33px`, `font-weight: 700`, `letter-spacing: -0.9px`)
- **Body Copy**: live computed `body` (`font-size: 18px`, `line-height: 25.2px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 18px`, `line-height: 25.2px`, `font-weight: 400`); CSS variables `--_text-style---letter-spacing: var(--_typography---letter-spacing--normal)`, `--_responsive---small: 0`, `--_responsive---xsmall: 0`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f7f7f7` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#183032` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffff00` | `mark { background: #ffff00 }` |
| **Interactive Accent / Highlight** | `#0082f3` | `.w-dropdown-link.w--current { color: #0082f3 }` |
| **Secondary / Muted Copy** | `#ddff2c` | live computed `h2` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e2e2e2` | `blockquote { border-left: #e2e2e2 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--_theme---background` | `var(--swatch--light-200)` | Canvas / Surface Token |
| `--_text-style---font-family` | `var(--_typography---font--primary-family)` | Typography Ink Token |
| `--_theme---text` | `var(--swatch--dark-900)` | Typography Ink Token |
| `--_text-style---font-size` | `var(--_typography---font-size--text-main)` | Typography Ink Token |
| `--_text-style---line-height` | `var(--_typography---line-height--huge)` | Typography Ink Token |
| `--_text-style---font-weight` | `var(--_typography---font--primary-regular)` | Typography Ink Token |
| `--_text-style---letter-spacing` | `var(--_typography---letter-spacing--normal)` | Typography Ink Token |
| `--_text-style---text-wrap` | `pretty` | Typography Ink Token |
| `--radius--main` | `.5rem` | Elevation / Border Token |
| `--_theme---background-2` | `var(--swatch--light-100)` | Canvas / Surface Token |
| `--site--column-count` | `12` | Layout / Spatial Grid Token |
| `--_responsive---large` | `1` | Design System Custom Token |
| `--_responsive---medium` | `0` | Design System Custom Token |
| `--_responsive---small` | `0` | Design System Custom Token |
| `--_responsive---xsmall` | `0` | Design System Custom Token |
| `--max-width--small` | `50rem` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.nav_desktop_wrap> — `www-avilus-com`)**:
   - Landmark `<header class="nav_desktop_wrap">` (`1440x50px`) hosting `Avilus · Dual-Use Uncrewed Aircraft ` navigation (`01 Grille · 02 Wespe · 03 Bussard · 04 RasCore · 05 Missions`), DOM attributes (`data-wf-domain="www.avilus.com"`, `data-wf-page="6a3f87ff2dc47a02eacbeb15"`, `data-wf-site="6a3f87fb2dc47a02eacbead0"`, `data-padding-bottom="none"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.u-section> — `Rescue. Protect. Provide.`)**:
   - Landmark `<section class="u-section u-min-height-screen">` presenting display lead `Rescue. Protect. Provide.` and copy excerpt *"Avilus builds autonomous critical air support for a world where h"* over `#f7f7f7` canvas and `#183032` ink.
3. **Primary Showcase & Content Grid (<section.u-padding-top-small> — `9Z - Bussard`)**:
   - Landmark `<section class="u-section u-padding-top-small">` rendering section `9Z - Bussard` with copy *"Evacuation. Resupply."*, asset references (`cdn.prod.website-files.com`, `avilus-staging.webflow.shared.f03...`, `gtm.js`, `6a521a02912e539c1f3a6bbb_avilus_w...`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.u-padding-bottom-small> — `Aircraft as a Service`)**:
   - Landmark `<section class="u-section u-padding-top-small">` framing `Aircraft as a Service` and `Elevate your career at Avilus` (*"Multi-Role. Cargo."*) with `#ffff00` surface cards, `#0082f3` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.footer_inner> — `https://www.avilus.com/`)**:
   - Landmark `<footer class="footer_inner">` anchoring `Avilus · Dual-Use Uncrewed Aircr` footer links (`01 Grille · 02 Wespe · 03 Bussard · 04 RasCore · 05 Missions`), copy *"Intelligence. Surveillance."*, and `#e2e2e2` structural dividers.
