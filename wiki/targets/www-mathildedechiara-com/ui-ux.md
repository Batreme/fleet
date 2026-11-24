---
title: "UI & UX Architecture: www-mathildedechiara-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-mathildedechiara-com

## Overview & Design Identity
- **Target**: `www-mathildedechiara-com` (**Mathilde De Chiara, designer and interior architect**)
- **Production URL**: [https://www.mathildedechiara.com/](https://www.mathildedechiara.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×828px`, Mobile `390×872px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f7f5f2` / `#000000`)
- **Summary**: Portfolio of Mathilde De Chiara: interior architecture, scenography and object design, from the Basque Country to Paris. Projects, exhibi...
- **Total Clean CSS Variables Extracted**: `30` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `PP Editorial New`
- **Body Font Stack**: `Helvetica Neue`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: observed font-size ladder: `72px`, `16px`, `14.4px`, `13.3333px`, `100%`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 72px`, `line-height: 79.2px`, `font-weight: 500`, `letter-spacing: -1.44px`); rule `,h2` (`font-weight: 500`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 16px`, `font-weight: 400`); rule `p` (`font-size: 14px`, `letter-spacing: .04em`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 16px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f7f5f2` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `button` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f0f0f0` | `.editorial-block__image-wrap { background: #f0f0f0 }` |
| **Interactive Accent / Highlight** | `#000000` | live computed `button` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#333333` | live computed `body` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#f8f6f3` | `.grid--rows-overlay .grid__item { border: #f8f6f3 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#f7f5f2` | Canvas / Surface Token |
| `--default-padding` | `5vw` | Layout / Spatial Grid Token |
| `--spacer-3xs` | `4px` | Layout / Spatial Grid Token |
| `--spacer-2xs` | `5px` | Layout / Spatial Grid Token |
| `--spacer-xs` | `10px` | Layout / Spatial Grid Token |
| `--hit-area` | `8px` | Dimension / Scale Token |
| `--spacer-s` | `20px` | Layout / Spatial Grid Token |
| `--spacer-sm` | `30px` | Layout / Spatial Grid Token |
| `--spacer-md` | `40px` | Layout / Spatial Grid Token |
| `--spacer-m` | `50px` | Layout / Spatial Grid Token |
| `--spacer-l` | `100px` | Layout / Spatial Grid Token |
| `--spacer-xl` | `200px` | Layout / Spatial Grid Token |
| `--spacer-xxl` | `300px` | Layout / Spatial Grid Token |
| `--font-primary` | `"PP Editorial New", Georgia, serif` | Brand / Palette Token |
| `--font-secondary` | `"Helvetica Neue", Helvetica, Arial, sans-serif` | Brand / Palette Token |
| `--page-px` | `clamp(16px, 3vw, 48px)` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.home-page__filters> — `www-mathildedechiara-com`)**:
   - Landmark `<nav class="home-page__filters">` (`274x143px`) hosting `Mathilde De Chiara, designer and int` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-rh="true"`, `data-rh="true"`, `data-rh="true"`, `data-rh="true"`), and stylesheet rule `video { margin:0;padding:0;border:0;font-size:100%;vertical-align:baseline }`.
2. **Hero Stage & Focal Lead (<main.page-content> — `Mathilde De Chiara, designer and i`)**:
   - Landmark `<main class="page-content home-page">` presenting display lead `Mathilde De Chiara, designer and interior archit` and copy excerpt *"Photography & Communication"* over `#f7f5f2` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<main.home-page> — `Featured Work & Interactive Showca`)**:
   - Landmark `<main class="page-content home-page">` rendering section `Featured Work & Interactive Showcase` with copy *"Mathilde De Chiara, designer and interior archit"*, asset references (`favicon.svg`, `apple-touch-icon.png`, `site.webmanifest`, `b2mcdo5v.apicdn.sanity.io`), and grid rule `section { display:block }`.
4. **Interactive Detail & Feature Matrix (<main.page-content:nth(2)> — `Technical Architecture & Narrative`)**:
   - Landmark `<main class="page-content home-page">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Work & Interactive Showcase"*) with `#f0f0f0` surface cards, `#000000` accents, and `body { line-height:1 }`.
5. **Colophon & Global Directory Footer (<footer.home-page> — `https://www.mathildedechiara.com/`)**:
   - Landmark `<footer class="home-page">` anchoring `Mathilde De Chiara, designer and` footer links (`Overview · Index · Archive · About · Contact`), copy *"Technical Architecture & Narrative"*, and `#f8f6f3` structural dividers.
