---
title: "UI & UX Architecture: www-governorsmansion-org"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-governorsmansion-org

## Overview & Design Identity
- **Target**: `www-governorsmansion-org` (**Louisiana's House · Louisiana Governor's Mansion**)
- **Production URL**: [https://www.governorsmansion.org/](https://www.governorsmansion.org/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#002b59` canvas, `#ffffff` ink, `#0082f3` accent)
- **Summary**: Step inside the Louisiana Governor’s Mansion and discover a rich blend of history, culture, and civic pride. Take a virtual tour, explore...
- **Total Clean CSS Variables Extracted**: `171` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `ivypresto-display`
- **Body Font Stack**: `stevie-sans`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 86.4px`, `line-height: 86.4px`, `font-weight: 300`); rule `h1` (`font-size: var(--_text-style---font-size)`, `line-height: var(--_text-style---l...`, `letter-spacing: var(--_text-style---l...`, `font-weight: var(--_text-s...`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 64px`, `line-height: 64px`, `font-weight: 300`); rule `h2` (`font-size: var(--_text-style---font-size)`, `line-height: var(--_text-style---l...`, `letter-spacing: var(--_text-style---l...`, `font-weight: var(--_text-s...`)
- **Body Copy**: live computed `body` (`font-size: 18px`, `line-height: 27px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 18px`, `line-height: 27px`, `font-weight: 400`); CSS variables `--_text-style---letter-spacing: var(--_typography---letter-spacing--normal)`, `--_responsive---small: 0`, `--_responsive---xsmall: 0`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#002b59` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#222222` | `.w-slider-nav-invert>div.w-active { background-color: #222222 }` |
| **Interactive Accent / Highlight** | `#0082f3` | `.w-dropdown-link.w--current { color: #0082f3 }` |
| **Secondary / Muted Copy** | `#000000` | live computed `h1` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#3898ec` | `.w-select:focus { border-color: #3898ec }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--_theme---background` | `var(--swatch--light-100)` | Canvas / Surface Token |
| `--_text-style---font-family` | `var(--_typography---font--secondary-family)` | Typography Ink Token |
| `--_theme---text` | `var(--swatch--dark-900)` | Typography Ink Token |
| `--_text-style---font-size` | `var(--_typography---font-size--text-main)` | Typography Ink Token |
| `--_text-style---line-height` | `var(--_typography---line-height--huge)` | Typography Ink Token |
| `--_text-style---font-weight` | `var(--_typography---font--secondary-book)` | Typography Ink Token |
| `--_text-style---letter-spacing` | `var(--_typography---letter-spacing--normal)` | Typography Ink Token |
| `--radius--main` | `1rem` | Elevation / Border Token |
| `--_theme---background-2` | `var(--_brand---color-200)` | Canvas / Surface Token |
| `--site--column-count` | `12` | Layout / Spatial Grid Token |
| `--_responsive---large` | `1` | Design System Custom Token |
| `--_responsive---medium` | `0` | Design System Custom Token |
| `--_responsive---small` | `0` | Design System Custom Token |
| `--_responsive---xsmall` | `0` | Design System Custom Token |
| `--max-width--small` | `50rem` | Layout / Spatial Grid Token |
| `--_gap---size` | `var(--site--gutter)` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.nav_desktop_wrap> — `www-governorsmansion-org`)**:
   - Landmark `<header class="nav_desktop_wrap">` (`1440x2835px`) hosting `Louisiana's House · Louisiana Govern` navigation (`Tour · History · Activities · Preserve · Contact`), DOM attributes (`data-wf-domain="www.governorsmansion.org"`, `data-wf-page="68f8ead2dc9339599a128c26"`, `data-wf-site="68f8ead1dc9339599a128b88"`, `data-number="10"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.u-section> — `LOUISIANA GOVERNOR'S MANSION`)**:
   - Landmark `<section class="u-section u-background-3">` presenting display lead `LOUISIANA GOVERNOR'S MANSION` and copy excerpt *"Start Virtual Tour"* over `#002b59` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.u-width-full> — `Louisiana Governor's Mansion`)**:
   - Landmark `<section class="u-section u-width-full">` rendering section `Louisiana Governor's Mansion` with copy *"Since it was built in 1963, the Louisiana Governor’s Mansion has "*, asset references (`cdn.prod.website-files.com`, `governors-mansion.webflow.shared....`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.u-section:nth(2)> — `The Legacy of the Governor's Mansi`)**:
   - Landmark `<section class="u-section u-width-full">` framing `The Legacy of the Governor's Mansion` and `Meet Our Governor` (*"Beginning with the administration of Jimmie Davis, the mansion ha"*) with `#222222` surface cards, `#0082f3` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.footer_wrap> — `https://www.governorsmansion.org/`)**:
   - Landmark `<footer class="footer_wrap u-theme-dark">` anchoring `Louisiana's House · Louisiana Go` footer links (`Tour · History · Activities · Preserve · Contact`), copy *"Additionally, the mansion serves as the headquarters of the "*, and `#3898ec` structural dividers.
