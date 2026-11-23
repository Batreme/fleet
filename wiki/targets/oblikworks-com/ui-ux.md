---
title: "UI & UX Architecture: oblikworks-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: oblikworks-com

## Overview & Design Identity
- **Target**: `oblikworks-com` (**oblikworks · Architectural Visualization & 3D Rendering Studio**)
- **Production URL**: [https://oblikworks.com/](https://oblikworks.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×1331px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#0082f3` accent)
- **Summary**: oblikworks is an architectural visualization studio creating photorealistic 3D renderings, architectural imagery, and visual storytelling...
- **Total Clean CSS Variables Extracted**: `5` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Suisseintl`
- **Body Font Stack**: `Suisseintl`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 44.64px`, `line-height: 44.64px`, `font-weight: 600`, `letter-spacing: -0.8928px`); rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 44.64px`, `line-height: 44.64px`, `font-weight: 600`, `letter-spacing: -0.8928px`); rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 16px`, `font-weight: 400`); rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 16px`, `font-weight: 400`); rule `small` (`font-size: 80%`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffff00` | `mark { background: #ffff00 }` |
| **Interactive Accent / Highlight** | `#0082f3` | `.w-dropdown-link.w--current { color: #0082f3 }` |
| **Secondary / Muted Copy** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#eeeeee` | `var(--_colors---line-color)` in `:root` |
| **Variable Token (`--_colors---button-grey`)** | `#f0f0f0` | `var(--_colors---button-grey)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--_font-sizes---p16` | `clamp(14px, 1vw, 16px)` | Typography / Scale Token |
| `--_colors---line-color` | `#eee` | Brand / Palette Token |
| `--_colors---button-grey` | `#f0f0f0` | Brand / Palette Token |
| `--cases-width` | `calc(220vw + 25px)` | Layout / Spatial Grid Token |
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--oblikworks-com-bg` | `#ffffff` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--oblikworks-com-ink` | `#000000` | Primary Typography Ink (computed-derived) |
| `--oblikworks-com-surface` | `#ffff00` | Surface Substrate (computed-derived) |
| `--oblikworks-com-accent` | `#0082f3` | Interactive Accent (computed-derived) |
| `--oblikworks-com-muted` | `#0000ee` | Secondary Ink (computed-derived) |
| `--oblikworks-com-border` | `#eeeeee` | Structural Border (computed-derived) |
| `--oblikworks-com-container` | `1900px` | Container Bound (computed-derived) |
| `--oblikworks-com-gap` | `16px` | Grid Gutter (computed-derived) |
| `--oblikworks-com-pad` | `9px` | Lateral Padding (computed-derived) |
| `--oblikworks-com-ease` | `cubic-bezier(.625,.05,0,1)` | Primary Easing Function |
| `--oblikworks-com-radius` | `3px` | Corner Radius (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.w-mod-js> — `oblikworks-com`)**:
   - Landmark `<header class="w-mod-js">` (`1440px`) hosting `oblikworks · Architectural Visualiza` navigation (`Studio · Projects · News 3 · Contact · Archive`), DOM attributes (`data-wf-domain="oblikworks.com"`, `data-wf-page="69c2caad0ee663f0795cd0bb"`, `data-wf-site="69c2caab0ee663f0795ccce3"`, `data-wf-ignore`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<div.preloader> — `Oblik is an Architectural 3D Visua`)**:
   - Landmark `<div class="preloader">` presenting display lead `Oblik is an Architectural 3D Visualization Studio...` and copy excerpt *"info@oblikworks.com"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<div.preloader:nth(2)> — `info@oblikworks.com`)**:
   - Landmark `<div class="preloader">` rendering section `info@oblikworks.com` with copy *"New work: Faculty of Philology is now published on our website."*, asset references (`cdn.prod.website-files.com`, `oblik-studio.webflow.shared.30697...`, `1135743295497216`, `fbevents.js`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<div.preloader:nth(3)> — `New work: Faculty of Philology is `)**:
   - Landmark `<div class="preloader">` framing `New work: Faculty of Philology is now published ` and `In the Press: Our Visualizations of The Alfred f` (*"In the Press: Our Visualizations of The Alfred featured in Urban "*) with `#ffff00` surface cards, `#0082f3` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.body> — `https://oblikworks.com/`)**:
   - Landmark `<footer class="body">` anchoring `oblikworks · Architectural Visua` footer links (`Studio · Projects · News 3 · Contact · Archive`), copy *"We're integrating AI into our 3D Design pipeline."*, and `#eeeeee` structural dividers.
