---
title: "UI & UX Architecture: ladolfinajumping-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: ladolfinajumping-com

## Overview & Design Identity
- **Target**: `ladolfinajumping-com` (**La Dolfina Jumping. World class genetics, breed in Argentina**)
- **Production URL**: [https://ladolfinajumping.com/](https://ladolfinajumping.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×872px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#fbe0b6` accent)
- **Summary**: We are dedicated to create the finest show jumping horses through our cutting-edge breeding program in Argentina by sourcing and importin...
- **Total Clean CSS Variables Extracted**: `12` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Marcellus`
- **Body Font Stack**: `Dualis Lite`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 60px`, `line-height: 75px`, `font-weight: 400`, `letter-spacing: 15px`); rule `h1` (`letter-spacing: .25em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 60px`, `line-height: 72px`, `font-weight: 400`, `letter-spacing: 7.5px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-weight: 500`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `main` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f3f3f3` | `.loader__progress:before { background-color: #f3f3f3 }` |
| **Interactive Accent / Highlight** | `#fbe0b6` | `var(--color-primary)` in `:root` |
| **Secondary / Muted Copy** | `#c7bcac` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#be7e21` | `.cursor-dot { border: #be7e21 }` |
| **Variable Token (`--color-secondary`)** | `#0a1b2e` | `var(--color-secondary)` in `:root` |
| **Variable Token (`--color-p`)** | `#475768` | `var(--color-p)` in `:root` |
| **Variable Token (`--color-dark-strong`)** | `#0d1620` | `var(--color-dark-strong)` in `:root` |
| **Variable Token (`--color-footer`)** | `#162638` | `var(--color-footer)` in `:root` |
| **Variable Token (`--form-brdr`)** | `#efe7dc` | `var(--form-brdr)` in `:root` |
| **Variable Token (`--swiper-theme-color`)** | `#007aff` | `var(--swiper-theme-color)` in stylesheet |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-primary` | `"Noto Sans Display", sans-serif` | Brand / Palette Token |
| `--font-tertiary` | `"Marcellus", "Dualis Lite", "Noto Sans Display", sans-serif` | Typography / Scale Token |
| `--color-primary` | `#fbe0b6` | Brand / Palette Token |
| `--color-secondary` | `#0a1b2e` | Brand / Palette Token |
| `--color-tertiary` | `#be7e21` | Brand / Palette Token |
| `--color-quaternary` | `#c7bcac` | Brand / Palette Token |
| `--color-form` | `rgb(175, 145, 95)` | Brand / Palette Token |
| `--color-p` | `#475768` | Brand / Palette Token |
| `--color-dark-strong` | `#0d1620` | Canvas / Surface Token |
| `--color-footer` | `#162638` | Brand / Palette Token |
| `--form-brdr` | `2px solid #efe7dc` | Color / Atmospheric Token |
| `--font-secondary` | `"Alpine Script"` | Brand / Palette Token |
| `--swiper-theme-color` | `#007aff` | Brand / Palette Token |
| `--swiper-navigation-size` | `44px` | Layout / Spatial Grid Token |
| `--ladolfinajumping-bg` | `#ffffff` | Canvas Substrate (from live computed `main` `background-color` (`computed_styles.json`)) |
| `--ladolfinajumping-ink` | `#000000` | Primary Typography Ink (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `ladolfinajumping-com`)**:
   - Landmark `<header class="header has--bg-darken">` (`1440x900px`) hosting `La Dolfina Jumping. World class gene` navigation (`Breeding Cría · Saddles · Bridles · Monturas · Cabezadas`), DOM attributes (`data-speed="0.5"`, `data-transition="opacity-in"`, `data-speed="0.25"`, `data-transition="opacity-scale-in-group"`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<article.modal__wrapper> — `DELIVERING ACCESS TO EXCEPTIONAL B`)**:
   - Landmark `<article class="modal__wrapper record">` presenting display lead `DELIVERING ACCESS TO EXCEPTIONAL BLOODLINES` and copy excerpt *"LA DOLFINA JUMPING IS A CUTTING-EDGE BREEDING PROGRAM CREATED BY "* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.record__header> — `La Dolfina Balouna`)**:
   - Landmark `<section class="record__header">` rendering section `La Dolfina Balouna` with copy *"La Dolfina Balouna"*, asset references (`289546863693632`, `fbevents.js`, `gtm.js`, `favicon.png`), and grid rule `html { height:auto;font-size:16px }`.
4. **Interactive Detail & Feature Matrix (<section.record__title> — `Premium studs`)**:
   - Landmark `<section class="record__title main">` framing `Premium studs` and `Casallco` (*"Information & details are coming soon."*) with `#f3f3f3` surface cards, `#fbe0b6` accents, and `html.lenis { height:auto;scroll-behavior:initial }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://ladolfinajumping.com/`)**:
   - Landmark `<footer class="footer bg-white">` anchoring `La Dolfina Jumping. World class ` footer links (`Breeding Cría · Saddles · Bridles · Monturas · Cabezadas`), copy *"La Dolfina Jumping Balouna Gama Z Balou du Rouet Baloubet Du"*, and `#be7e21` structural dividers.
