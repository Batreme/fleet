---
title: "UI & UX Architecture: pyzhevsky-estate"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: pyzhevsky-estate

## Overview & Design Identity
- **Target**: `pyzhevsky-estate` (**Pyzhevsky — official website of a deluxe residence five minutes from the...**)
- **Production URL**: [https://pyzhevsky.estate/](https://pyzhevsky.estate/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f7f2e8` / `#75736d`)
- **Summary**: An intimate residential project. Apartments in the historic centre. Panoramic views and original architecture.
- **Total Clean CSS Variables Extracted**: `484` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Halvar Breitschrift`
- **Body Font Stack**: `Garamond Light`
- **Monospace / Technical Font Stack**: `Consolas`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 107px`, `line-height: 140px`, `font-weight: 400`); rule `,h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 60px`, `line-height: 60px`, `font-weight: 400`); rule `,h2` (`font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 20px`, `font-weight: 400`, `letter-spacing: 0.32px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 20px`, `font-weight: 400`, `letter-spacing: 0.32px`); CSS variables `--t-small: var(--c-pale-dark)`, `--t-small-rgb: var(--c-pale-dark-rgb)`; rule `,small` (`font-weight: 500`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f7f2e8` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#12100e` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `.overlay { background: #ffffff }` |
| **Interactive Accent / Highlight** | `#75736d` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#75736d` | live computed `footer` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#000000` | `var(--t-button-border-black-text)` in `:root` |
| **Variable Token (`--c-black-hover`)** | `#2f2b27` | `var(--c-black-hover)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--scale-px` | `1px` | Dimension / Scale Token |
| `--scale-rem` | `1rem` | Dimension / Scale Token |
| `--scale-em` | `1em` | Dimension / Scale Token |
| `--scale-text-px` | `1px` | Typography Ink Token |
| `--scale-text-rem` | `1rem` | Typography Ink Token |
| `--scale-text-em` | `1em` | Typography Ink Token |
| `--scale-none-px` | `1px` | Dimension / Scale Token |
| `--scale-none-rem` | `1rem` | Dimension / Scale Token |
| `--vw` | `1vw` | Layout / Spatial Grid Token |
| `--vw100` | `100vw` | Layout / Spatial Grid Token |
| `--c-black` | `#12100e` | Canvas / Surface Token |
| `--c-black-rgb` | `18,16,14` | Canvas / Surface Token |
| `--c-black-hover` | `#2f2b27` | Canvas / Surface Token |
| `--c-black-hover-rgb` | `47,43,39` | Canvas / Surface Token |
| `--c-white` | `#fff` | Canvas / Surface Token |
| `--c-white-rgb` | `255,255,255` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `pyzhevsky-estate`)**:
   - Landmark `<header class="header is-hidden--print">` (`1440x50px`) hosting `Pyzhevsky — official website of a de` navigation (`Select an apartment · 3D area map`), DOM attributes (`data-barba="wrapper"`, `data-nosnippet`, `data-plugin="preloader"`, `data-preloader-animation-name-in="preloader-in"`), and stylesheet rule `html { line-height:1.15;-webkit-text-size-adjust:100% }`.
2. **Hero Stage & Focal Lead (<section.section> — `PYZHEVSKY`)**:
   - Landmark `<section class="section l-intro-section">` presenting display lead `PYZHEVSKY` and copy excerpt *"ADELUXEPROJECT INTHEHISTORICQUARTER"* over `#f7f2e8` canvas and `#12100e` ink.
3. **Primary Showcase & Content Grid (<section.ui-dark> — `Pyzhevsky`)**:
   - Landmark `<section class="section ui-dark">` rendering section `Pyzhevsky` with copy *"A d e l u x e p r o j e c t i n t h e h i s t o r i c q u a r t e"*, asset references (`storage.googleapis.com`, `itc-garamond_light.woff2`, `Halvar-Breitschrift-Regular-Web.w...`, `Halvar-Breitschrift-Medium-Web.woff2`), and grid rule `pre { font-family:monospace,monospace;font-size:1em }`.
4. **Interactive Detail & Feature Matrix (<section.section--top-2> — `Smart systems`)**:
   - Landmark `<section class="section section--top-2">` framing `Smart systems` and `Service entrance` (*"Restrained, assured, timeless — they put the city on pause, so al"*) with `#ffffff` surface cards, `#75736d` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.section> — `https://pyzhevsky.estate/`)**:
   - Landmark `<footer class="section section--no-overflow">` anchoring `Pyzhevsky — official website of ` footer links (`Select an apartment · 3D area map`), copy *"The minimalist form of the three buildings draws on the sign"*, and `#000000` structural dividers.
