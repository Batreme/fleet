---
title: "UI & UX Architecture: www-lamagadan-studio"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-lamagadan-studio

## Overview & Design Identity
- **Target**: `www-lamagadan-studio` (**La Magadán · Branding y diseño para emprendedoras**)
- **Production URL**: [https://www.lamagadan.studio/](https://www.lamagadan.studio/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f5f5f5` canvas, `#222222` ink, `#ff5f26` accent)
- **Summary**: Soy Cristina, diseñadora y creativa en La Magadán. Ayudo a emprendedoras como tú a crear marcas que conectan, destacan y venden.
- **Total Clean CSS Variables Extracted**: `0` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Animal Condensed`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 129.6px`, `line-height: 132.192px`, `font-weight: 400`, `letter-spacing: -1.296px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 92.16px`, `line-height: 87.552px`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f5f5f5` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#222222` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ff5f26` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ff5f26` | live computed `button` `background-color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#ffffff` | live computed `footer` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#7a7a7a` | `.sc-interp.sc-missing { border: #7a7a7a }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--www-lamagadan-st-bg` | `#f5f5f5` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--www-lamagadan-st-ink` | `#222222` | Primary Typography Ink (computed-derived) |
| `--www-lamagadan-st-surface` | `#ff5f26` | Surface Substrate (computed-derived) |
| `--www-lamagadan-st-accent` | `#ff5f26` | Interactive Accent (computed-derived) |
| `--www-lamagadan-st-muted` | `#ffffff` | Secondary Ink (computed-derived) |
| `--www-lamagadan-st-border` | `#7a7a7a` | Structural Border (computed-derived) |
| `--www-lamagadan-st-container` | `1440px` | Container Bound (computed-derived) |
| `--www-lamagadan-st-gap` | `16px` | Grid Gutter (computed-derived) |
| `--www-lamagadan-st-pad` | `4px` | Lateral Padding (computed-derived) |
| `--www-lamagadan-st-ease` | `cubic-bezier(0.4,0,0.2,1)` | Primary Easing Function |
| `--www-lamagadan-st-radius` | `28px` | Corner Radius (computed-derived) |
| `--www-lamagadan-st-fs-base` | `129.6px` | Observed Font Size Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.sc-host> — `www-lamagadan-studio`)**:
   - Landmark `<header class="sc-host">` (`1408x64px`) hosting `La Magadán · Branding y diseño para ` navigation (`Quién soy · Proyectos · Servicios · Mi proceso · Testimonios`), DOM attributes (`data-dc-tpl="1"`, `data-dc-tpl="2"`, `data-dc-tpl="3"`, `data-dc-tpl="4"`), and stylesheet rule `l.sc-dc-streaming .sc-interp.sc-m... { position:relative; background:color-mix(in srgb,currentColor 5%,transpar... }`.
2. **Hero Stage & Focal Lead (<section.scp0> — `Branding para emprendedoras con un`)**:
   - Landmark `<section class="scp0">` presenting display lead `Branding para emprendedoras con una historia que...` and copy excerpt *"Acompaño a mujeres emprendedoras como tú a construir su identidad"* over `#f5f5f5` canvas and `#222222` ink.
3. **Primary Showcase & Content Grid (<section.scp1> — `Acompaño a mujeres emprendedoras c`)**:
   - Landmark `<section class="scp1">` rendering section `Acompaño a mujeres emprendedoras como tú a const` with copy *"¿Hablamos? ¿Hablamos?"*, asset references (`favicon.png`, `apple-touch-icon.png`, `support.js`, `react.production.min.js`), and grid rule `before { animation:none; background:color-mix(in srgb,currentColor 8%,transparent) }`.
4. **Interactive Detail & Feature Matrix (<section.sc-interp> — `¿Hablamos? ¿Hablamos?`)**:
   - Landmark `<section class="sc-interp">` framing `¿Hablamos? ¿Hablamos?` and `Busco la esencia de tu proyecto para que tu marc` (*"Busco la esencia de tu proyecto para que tu marca sea fiel a quié"*) with `#ff5f26` surface cards, `#ff5f26` accents, and `.sc-host.sc-has-error { position:relative }`.
5. **Colophon & Global Directory Footer (<footer.scp3> — `https://www.lamagadan.studio/`)**:
   - Landmark `<footer class="scp3">` anchoring `La Magadán · Branding y diseño p` footer links (`Quién soy · Proyectos · Servicios · Mi proceso · Testimonios`), copy *"Transformo tus ideas en relatos memorables: marcas que conec"*, and `#7a7a7a` structural dividers.
