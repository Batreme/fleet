---
title: "UI & UX Architecture: www-vanderhotel-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-vanderhotel-com

## Overview & Design Identity
- **Target**: `www-vanderhotel-com` (**Hotel & Restaurant Ljubljana · Vander Urbani Resort**)
- **Production URL**: [https://www.vanderhotel.com](https://www.vanderhotel.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f4f2f1` canvas, `#353230` ink, `#0082f3` accent)
- **Summary**: This Design Hotel offers 20 beautiful rooms. For the foodies we have our HAUS & À la carte restaurant or for a glass of champagne we sugg...
- **Total Clean CSS Variables Extracted**: `25` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Sohne Buch`
- **Body Font Stack**: `Sohne Buch`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 112px`, `line-height: 134.4px`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 80px`, `line-height: 80px`, `font-weight: 400`); rule `h2` (`font-size: 2.5rem`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--_typography---font-styles--body: "Sohne Buch",Arial,sans-serif`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--_ui-styles---radius--small: 0px`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f4f2f1` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#353230` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffff00` | `mark { background: #ffff00 }` |
| **Interactive Accent / Highlight** | `#0082f3` | `.w-dropdown-link.w--current { color: #0082f3 }` |
| **Secondary / Muted Copy** | `#967850` | live computed `h2` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e2e2e2` | `blockquote { border-left: #e2e2e2 }` |
| **Variable Token (`--main-light-color`)** | `#f3f5fb` | `var(--main-light-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--main-light-color` | `#F3F5FB` | Canvas / Surface Token |
| `--main-dark-color` | `#353230` | Canvas / Surface Token |
| `--main-active-color` | `#353230` | Brand / Palette Token |
| `--color-scheme-1--background-primary` | `var(--_primitives---colors--white)` | Canvas / Surface Token |
| `--_typography---font-styles--body` | `"Sohne Buch",Arial,sans-serif` | Typography / Scale Token |
| `--color-scheme-1--text-primary` | `var(--_primitives---colors--dark)` | Typography Ink Token |
| `--_typography---font-styles--heading` | `"Sohne Buch",Arial,sans-serif` | Typography Ink Token |
| `--_primitives---colors--neutral-darkest` | `black` | Canvas / Surface Token |
| `--_primitives---colors--white` | `#f4f2f1` | Canvas / Surface Token |
| `--color-scheme-1--text-secondary` | `var(--_primitives---colors--brown)` | Typography Ink Token |
| `--color-scheme-1--background-secondary` | `var(--_primitives---colors--dark)` | Canvas / Surface Token |
| `--color-scheme-1--text-white` | `var(--_primitives---colors--white)` | Canvas / Surface Token |
| `--color-scheme-1--background-brown` | `var(--_primitives---colors--brown)` | Canvas / Surface Token |
| `--_ui-styles---stroke--border-width` | `1px` | Layout / Spatial Grid Token |
| `--color-scheme-1--border` | `var(--_primitives---colors--brown)` | Brand / Palette Token |
| `--_ui-styles---radius--medium` | `0px` | Elevation / Border Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.navbar> — `www-vanderhotel-com`)**:
   - Landmark `<header class="navbar">` (`1440x135px`) hosting `Hotel & Restaurant Ljubljana · Vande` navigation (`Hotel · Food & Drink · meetings & Events · book now · journal`), DOM attributes (`data-wf-domain="www.vanderhotel.com"`, `data-wf-page="67f3b8c25d374ee9920d88c8"`, `data-wf-site="67f3b8c25d374ee9920d885b"`, `data-w-id="792db6bb-fe71-b745-03..."`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.section-hero> — `WHERE COMFORT MEETS CULTURE`)**:
   - Landmark `<section class="section-hero">` presenting display lead `WHERE COMFORT MEETS CULTURE` and copy excerpt *"Experience a stylish, relaxed city break filled with comfort and "* over `#f4f2f1` canvas and `#353230` ink.
3. **Primary Showcase & Content Grid (<section.section-wake-up> — `where comfort meets culture`)**:
   - Landmark `<section class="section-wake-up">` rendering section `where comfort meets culture` with copy *"Welcome to our Vander Hotel. Perfect rooms for all Vanderers by h"*, asset references (`cdn.prod.website-files.com`, `vander-hotel.webflow.shared.087c8...`, `vander-hotel.webflow.67f3b8c25d37...`, `1910953583635711`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.section-experience> — `mailing list`)**:
   - Landmark `<section class="section-experience">` framing `mailing list` and `rooftop terrace` (*"Early check-in & late check-out"*) with `#ffff00` surface cards, `#0082f3` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://www.vanderhotel.com`)**:
   - Landmark `<footer class="footer">` anchoring `Hotel & Restaurant Ljubljana · V` footer links (`Hotel · Food & Drink · meetings & Events · book now · journal`), copy *"If you are in for some VanderFul and funky tastes, then come"*, and `#e2e2e2` structural dividers.
