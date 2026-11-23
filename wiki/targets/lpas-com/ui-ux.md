---
title: "UI & UX Architecture: lpas-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: lpas-com

## Overview & Design Identity
- **Target**: `lpas-com` (**LPAS - Architecture and Interiors**)
- **Production URL**: [https://lpas.com/](https://lpas.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#0e0e0e` accent)
- **Summary**: Clear Process. Creative Results. Human-centered. Always Curious. At LPAS, we design with people at the center and purpose at every turn.
- **Total Clean CSS Variables Extracted**: `12` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Aeonik`
- **Body Font Stack**: `Aeonik`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 75px`, `line-height: 75px`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 38px`, `line-height: 41.8px`, `font-weight: 400`); rule `h2` (`line-height: 110%`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 21.6px`, `font-weight: 400`); rule `,body` (`line-height: 135%`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 21.6px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#eeeeee` | `.template code { background-color: #eeeeee }` |
| **Interactive Accent / Highlight** | `#0e0e0e` | live computed `button` `background-color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#747474` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e5e5e5` | `.template__title { border-bottom: #e5e5e5 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--row-gap` | `0` | Layout / Spatial Grid Token |
| `--column-gap` | `1rem` | Layout / Spatial Grid Token |
| `--xxlSpace` | `8.5rem` | Layout / Spatial Grid Token |
| `--marketMainColor` | `rgb(98, 86, 83)` | Brand / Palette Token |
| `--marketSecondaryColor` | `rgb(123, 105, 100)` | Brand / Palette Token |
| `--marketContentColor` | `rgb(255, 255, 255)` | Brand / Palette Token |
| `--marketContentContrast` | `rgb(38, 38, 38)` | Color / Atmospheric Token |
| `--scrollbarWidth` | `0px` | Layout / Spatial Grid Token |
| `--ctaBarHeight` | `0px` | Brand / Palette Token |
| `--viewportWidth` | `calc(100vw - var(--scrollbarWidth))` | Layout / Spatial Grid Token |
| `--cut` | `2rem` | Dimension / Scale Token |
| `--sticky-offset` | `505px` | Dimension / Scale Token |
| `--wp--preset--aspect-ratio--square` | `1` | Design System Custom Token |
| `--wp--preset--aspect-ratio--4-3` | `4/3` | Design System Custom Token |
| `--lpas-com-bg` | `#ffffff` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--lpas-com-ink` | `#000000` | Primary Typography Ink (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.mainHeader> — `lpas-com`)**:
   - Landmark `<header class="mainHeader">` (`900x225px`) hosting `LPAS - Architecture and Interiors` navigation (`Housing · Interiors · Higher Education · Civic · Commercial`), DOM attributes (`data-browser="Chrome"`, `data-istoch="false"`, `data-logocolor="light"`, `data-first-visit="true"`), and stylesheet rule `video { margin:0;padding:0;border:0;font-size:100%;font:inherit;vertical-align:b... }`.
2. **Hero Stage & Focal Lead (<section.homeHero> — `We’re a process driven architectur`)**:
   - Landmark `<section class="homeHero">` presenting display lead `We’re a process driven architecture and interior...` and copy excerpt *"Happy Halloween from LPAS! Teamwork makes the scream work."* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.blockIntroGeneral> — `Higher Education`)**:
   - Landmark `<section class="blockIntroGeneral">` rendering section `Higher Education` with copy *"Architecture + Interiors"*, asset references (`main-DN-9Dm9S.css`, `swup-config-DoT-9FzL.js`, `preloader-CQAQSTAa.js`, `lenisSmooth-BjXMsNId.js`), and grid rule `section { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.blockProjectsHighlight> — `Clear Process. Creative Results. H`)**:
   - Landmark `<section class="blockProjectsHighlight">` framing `Clear Process. Creative Results. Human Centered....` and `Listen. Plan. Analyze. Shape.` (*"A Market-Focused Approach"*) with `#eeeeee` surface cards, `#0e0e0e` accents, and `body { line-height:1 }`.
5. **Colophon & Global Directory Footer (<footer.navigationFooter> — `https://lpas.com/`)**:
   - Landmark `<footer class="navigationFooter">` anchoring `LPAS - Architecture and Interior` footer links (`Housing · Interiors · Higher Education · Civic · Commercial`), copy *"Swipe up to explore"*, and `#e5e5e5` structural dividers.
