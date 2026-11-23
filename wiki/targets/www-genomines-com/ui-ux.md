---
title: "UI & UX Architecture: www-genomines-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: www-genomines-com

## Overview & Design Identity
- **Target**: `www-genomines-com` (**Genomines — We Grow Metal**)
- **Production URL**: [https://www.genomines.com/](https://www.genomines.com/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#efebe1` / `#b3261e`)
- **Summary**: Plants that grow metal. Genomines uses phytomining and genomics to extract battery-grade nickel from low-grade soils, with no waste rock...
- **Total Clean CSS Variables Extracted**: `22` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Causten`
- **Body Font Stack**: `Causten`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 60px`, `line-height: 57px`, `font-weight: 500`, `letter-spacing: -1.8px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 48px`, `line-height: 45.6px`, `font-weight: 500`, `letter-spacing: -1.44px`)
- **Body Copy**: live computed `body` (`font-size: 14px`, `line-height: 19.6px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 14px`, `line-height: 19.6px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#efebe1` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#373735` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#d4ff8f` | `header__nav>ul .nav__item .nav_... { background: #d4ff8f }` |
| **Interactive Accent / Highlight** | `#b3261e` | `al__form .contact-modal__feedba... { color: #b3261e }` |
| **Secondary / Muted Copy** | `#cec5b0` | `apper .team__content .team__hea... { color: #cec5b0 }` |
| **Structural Hairline Border** | `#c1beb6` | `ntact-modal__form .contact-moda... { border: #c1beb6 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--gridCell` | `0px` | Layout / Spatial Grid Token |
| `--gridGap` | `0px` | Layout / Spatial Grid Token |
| `--gridMargin` | `0px` | Layout / Spatial Grid Token |
| `--wrapper-margin` | `max(18px, 2.0833vw)` | Layout / Spatial Grid Token |
| `--margin-xl` | `72px` | Layout / Spatial Grid Token |
| `--margin-l` | `48px` | Layout / Spatial Grid Token |
| `--margin-m` | `24px` | Layout / Spatial Grid Token |
| `--margin-s` | `12px` | Layout / Spatial Grid Token |
| `--controls-backdrop-color` | `rgba(0, 0, 0, .4)` | Brand / Palette Token |
| `--media-range-track-background` | `rgba(239, 235, 225, .25)` | Canvas / Surface Token |
| `--media-time-range-buffered-color` | `rgba(239, 235, 225, .45)` | Brand / Palette Token |
| `--gradient-steps` | `transparent 0%, transparent 100%` | Dimension / Scale Token |
| `--media-control-hover-background` | `rgba(239, 235, 225, .1)` | Canvas / Surface Token |
| `--media-menu-background` | `rgba(55, 55, 53, .5)` | Canvas / Surface Token |
| `--media-menu-item-hover-background` | `rgba(239, 235, 225, .1)` | Canvas / Surface Token |
| `--quotes-extra-height` | `111px` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.global__header> — `www-genomines-com`)**:
   - Landmark `<header class="global__header">` (`1440x90px`) hosting `Genomines — We Grow Metal` navigation (`Homepage · Technology · Systemic Return · About us · Work with us`), DOM attributes (`data-taxi-ignore="true"`, `data-action="contact"`, `data-taxi-ignore="true"`, `data-action="contact"`), and stylesheet rule `after { margin:0;padding:0;box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.section__hero> — `We Grow Metal`)**:
   - Landmark `<section class="section__hero">` presenting display lead `We Grow Metal` and copy excerpt *"Biological infrastructure for critical metal extraction."* over `#efebe1` canvas and `#373735` ink.
3. **Primary Showcase & Content Grid (<section.section__paradigm-shift> — `The payload.`)**:
   - Landmark `<section class="section__paradigm-shift">` rendering section `The payload.` with copy *"Battery-grade nickel, harvested at best-in-class costs."*, asset references (`favicon-96x96.png`, `favicon.svg`, `favicon.ico`, `apple-touch-icon.png`), and grid rule `video { max-width:100%;display:block }`.
4. **Interactive Detail & Feature Matrix (<section.section__scenes> — `More than profit. More than sustai`)**:
   - Landmark `<section class="section__scenes">` framing `More than profit. More than sustainability. Syste...` and `We’re growing. Genomines in the News.` (*"Inside the team replacing the"*) with `#d4ff8f` surface cards, `#b3261e` accents, and `button { background:none;border:none;cursor:pointer;font:inherit;color:inherit }`.
5. **Colophon & Global Directory Footer (<footer.global__footer> — `https://www.genomines.com/`)**:
   - Landmark `<footer class="global__footer">` anchoring `Genomines — We Grow Metal` footer links (`Homepage · Technology · Systemic Return · About us · Work with us`), copy *"excavator with plants, and the"*, and `#c1beb6` structural dividers.
