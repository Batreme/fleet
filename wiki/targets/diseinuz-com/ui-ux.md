---
title: "UI & UX Architecture: diseinuz-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: diseinuz-com

## Overview & Design Identity
- **Target**: `diseinuz-com` (**DISEINUZ — Bilbao Bizkaia Design Summit**)
- **Production URL**: [https://diseinuz.com/](https://diseinuz.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#ffffff` ink, `#ff2e01` accent)
- **Summary**: Un encuentro para impulsar el diseño como herramienta de transformación económica, empresarial y social. 19 y 20 de noviembre de 2026 en...
- **Total Clean CSS Variables Extracted**: `40` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Univers LT Std`
- **Body Font Stack**: `IBM Plex Mono`
- **Monospace / Technical Font Stack**: `IBM Plex Mono`
- **Hero Display (`H1`)**: rule `.title` (`font-size: 1.5rem`, `line-height: .91667`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 192px`, `line-height: 157.44px`, `font-weight: 900`, `letter-spacing: -13.44px`); rule `h2` (`font-size: max(20px,1.5rem)`, `line-height: .91667`, `letter-spacing: var(--title-letter-sp...`, `font-weight: 900`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 0px`, `font-weight: 400`); rule `p` (`font-size: max(12px,.875rem)`, `line-height: 1.3334`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 0px`, `font-weight: 400`); CSS variables `--title-letter-spacing: -.07em`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | live computed `footer` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ff2e01` | SVG/DOM `stop-color="#FF2E01"` attribute in `dom.html` |
| **Secondary / Muted Copy** | `#ffffff` | secondary opacity step of live computed `main` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#ffffff` | `var(--border)` in `:root` (`rgb(var(--color-white))`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--grid-gutter` | `.75rem` | Layout / Spatial Grid Token |
| `--grid-margin` | `.75rem` | Layout / Spatial Grid Token |
| `--grid-margin-negative` | `-.75rem` | Layout / Spatial Grid Token |
| `--grid-columns` | `12` | Layout / Spatial Grid Token |
| `--color-black` | `0, 0, 0` | Canvas / Surface Token |
| `--color-white` | `255, 255, 255` | Canvas / Surface Token |
| `--title-letter-spacing` | `-.07em` | Typography / Scale Token |
| `--easing-handle-01` | `cubic-bezier(.48, .1, 0, 1)` | Motion / Easing Token |
| `--easing-handle-02` | `cubic-bezier(.01, .8, .5, 1)` | Motion / Easing Token |
| `--filter-blur` | `blur(5rem)` | Elevation / Border Token |
| `--context` | `1440` | Typography Ink Token |
| `--quarter` | `3.25rem` | Dimension / Scale Token |
| `--menu-width` | `calc(var(--grid-one-column) * var(--grid-columns))` | Layout / Spatial Grid Token |
| `--modal-top` | `2rem` | Dimension / Scale Token |
| `--flashlight-x` | `50%` | Canvas / Surface Token |
| `--flashlight-y` | `50%` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `diseinuz-com`)**:
   - Landmark `<header class="header top">` (`1425x900px`) hosting `DISEINUZ — Bilbao Bizkaia Design Sum` navigation (`Aviso legal · Privacidad`), DOM attributes (`data-type="desktop"`, `data-url="/privacidad"`, `data-to="default__page"`, `data-lenis-prevent`), and stylesheet rule `root { --grid-columns:6;--context:402;--menu-width:calc(var(--grid-one-column)... }`.
2. **Hero Stage & Focal Lead (<section.home__hero> — `19-20 nov sala multibox eitb bilba`)**:
   - Landmark `<section class="home__hero">` presenting display lead `19-20 nov sala multibox eitb bilbao` and copy excerpt *"El uso de cookies tiene como objetivo el análisis del uso de este"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.home__intro> — `Ponentes`)**:
   - Landmark `<section class="home__intro">` rendering section `Ponentes` with copy *"DISEINUZ nace como un nuevo espacio para situar el diseño en el c"*, asset references (`favicon-96x96.png`, `favicon.svg`, `favicon.ico`, `apple-touch-icon.png`), and grid rule `html.lenis body { height:auto }`.
4. **Interactive Detail & Feature Matrix (<section.home__featured> — `Contacto`)**:
   - Landmark `<section class="home__featured shader__section">` framing `Contacto` and `Durante dos jornadas, DISEINUZ se convierte en e` (*"Durante dos jornadas, DISEINUZ se convierte en el punto de encuen"*) with `#ffffff` surface cards, `#ff2e01` accents, and `.lenis.lenis-smooth { scroll-behavior:auto!important }`.
5. **Colophon & Global Directory Footer (<footer.page__footer> — `https://diseinuz.com/`)**:
   - Landmark `<footer class="page__footer">` anchoring `DISEINUZ — Bilbao Bizkaia Design` footer links (`Aviso legal · Privacidad`), copy *"Conectar personas e ideas, compartir conocimiento, y activar"*, and `#ffffff` structural dividers.
