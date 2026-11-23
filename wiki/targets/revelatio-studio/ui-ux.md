---
title: "UI & UX Architecture: revelatio-studio"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: revelatio-studio

## Overview & Design Identity
- **Target**: `revelatio-studio` (**Revelatio · Branding, Product Design & Code**)
- **Production URL**: [https://revelatio.studio/](https://revelatio.studio/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×2400px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#0082f3`)
- **Summary**: Revelatio is an integrated studio for branding, product design, and code, building digital experiences and brand systems for ambitious co...
- **Total Clean CSS Variables Extracted**: `22` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Neue Haas Grotesk Text Pro 55 Roman`
- **Body Font Stack**: `Neue Haas Grotesk Text Pro 55 Roman`
- **Monospace / Technical Font Stack**: `Inconsolata`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 35.9856px`, `line-height: 39.5842px`, `font-weight: 400`, `letter-spacing: -1.07957px`); rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 35.9856px`, `line-height: 39.5842px`, `font-weight: 400`, `letter-spacing: -1.07957px`); rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: live computed `body` (`font-size: 11.9952px`, `line-height: 17.9928px`, `font-weight: 400`); rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 11.9952px`, `line-height: 17.9928px`, `font-weight: 400`); rule `small` (`font-size: 80%`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#222222` | `.w-slider-nav-invert > div.w-ac... { background-color: #222222 }` |
| **Interactive Accent / Highlight** | `#0082f3` | `.w-dropdown-link.w--current { color: #0082f3 }` |
| **Secondary / Muted Copy** | `#7e8894` | `GateOverlay_module_dismissButto... { color: #7e8894 }` |
| **Structural Hairline Border** | `#3898ec` | `.w-select:focus { border-color: #3898ec }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color--neutral--light` | `white` | Canvas / Surface Token |
| `--color--neutral--dark` | `black` | Canvas / Surface Token |
| `--color--neutral--900` | `#ffffff52` | Brand / Palette Token |
| `--color--neutral--200` | `#00000014` | Brand / Palette Token |
| `--color--neutral--800` | `#ffffff29` | Brand / Palette Token |
| `--color--neutral--300` | `#00000029` | Brand / Palette Token |
| `--color--neutral--400` | `#00000052` | Brand / Palette Token |
| `--color--neutral--500` | `#000000a3` | Brand / Palette Token |
| `--color--neutral--600` | `#ffffff0a` | Brand / Palette Token |
| `--color--neutral--700` | `#ffffff14` | Brand / Palette Token |
| `--color--neutral--1000` | `#ffffffa3` | Brand / Palette Token |
| `--color--neutral--100` | `#0000000a` | Brand / Palette Token |
| `--tbg` | `#fff` | Canvas / Surface Token |
| `--tfg` | `#000` | Typography Ink Token |
| `--tt` | `hsla(0, 0%, 0%, .08)` | Color / Atmospheric Token |
| `--tline` | `hsla(0, 0%, 0%, .85)` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.navbar> — `revelatio-studio`)**:
   - Landmark `<nav class="navbar">` (`1440x63px`) hosting `Revelatio · Branding, Product Design` navigation (`Work · Approach · About · Careers · EN`), DOM attributes (`data-wf-domain="revelatio.studio"`, `data-wf-page="6a1dba8694fc8f455cf55833"`, `data-wf-site="6a1dba8694fc8f455cf5585d"`, `data-scale-hover-bound="1"`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<div.w-mod-ix> — `Branding, Product Design & Code. O`)**:
   - Landmark `<div class="w-mod-ix">` presenting display lead `Branding, Product Design & Code. One integrated v...` and copy excerpt *"Fractional Brand Leadership Innovation Advisory Dedicated Brand S"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<div.is-preloading> — `Fractional Brand Leadership Innova`)**:
   - Landmark `<div class="is-preloading">` rendering section `Fractional Brand Leadership Innovation Advisory ` with copy *"Fractional Brand Leadership"*, asset references (`cdn.prod.website-files.com`, `pt-br`, `revelatio-studio.webflow.shared.6...`, `6a1adb7b38c8bf5b0bcefe1c_revelati...`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<div.lenis> — `Fractional Brand Leadership`)**:
   - Landmark `<div class="lenis">` framing `Fractional Brand Leadership` and `Innovation Advisory` (*"Innovation Advisory"*) with `#222222` surface cards, `#0082f3` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://revelatio.studio/`)**:
   - Landmark `<footer class="footer">` anchoring `Revelatio · Branding, Product De` footer links (`Work · Approach · About · Careers · EN`), copy *"Dedicated Brand Squads"*, and `#3898ec` structural dividers.
