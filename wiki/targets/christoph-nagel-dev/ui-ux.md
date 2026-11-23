---
title: "UI & UX Architecture: christoph-nagel-dev"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: christoph-nagel-dev

## Overview & Design Identity
- **Target**: `christoph-nagel-dev` (**Christoph Nagel · Webentwickler, Fotograf & Videograf in Dorsten**)
- **Production URL**: [https://christoph-nagel.dev/](https://christoph-nagel.dev/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#080808` / `#000000`)
- **Summary**: Christoph Nagel aus Dorsten: Webentwicklung mit WordPress, HTML, CSS und JavaScript. Einblicke in eigene Projekte, Fotografie und Videogr...
- **Total Clean CSS Variables Extracted**: `19` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Anton`
- **Body Font Stack**: `Manrope`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 15.2px`, `line-height: 22.04px`, `font-weight: 400`, `letter-spacing: 0.608px`); rule `.hero-title` (`font-size: clamp(4rem, 13vw, 12.8rem)`, `line-height: 0.84`, `letter-spacing: -0.005em`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 187.2px`, `line-height: 157.248px`, `font-weight: 400`, `letter-spacing: -0.936px`); rule `h2` (`font-size: clamp(2.25rem, 4.25vw, 4.7rem)`, `line-height: 1.15`, `letter-spacing: -0.018em`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: clamp(0.9rem, 1vw, 1rem)`, `line-height: 1.68`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--label-width: 150px`, `--label-top: 52%`, `--label-z-index: 40`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#080808` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#0a0a0a` | `.site-shell { background: #0a0a0a }` |
| **Interactive Accent / Highlight** | `#000000` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#f4f4f1` | live computed `nav` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#343434` | `var(--line)` in `:root` (`rgba(255, 255, 255, 0.18)`) |
| **Variable Token (`--red`)** | `#ff4b3e` | `var(--red)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#080808` | Canvas / Surface Token |
| `--text` | `#f4f4f1` | Typography Ink Token |
| `--muted` | `rgba(244, 244, 241, 0.68)` | Color / Atmospheric Token |
| `--line` | `rgba(255, 255, 255, 0.18)` | Color / Atmospheric Token |
| `--glass` | `rgba(12, 12, 12, 0.38)` | Color / Atmospheric Token |
| `--red` | `#ff4b3e` | Color / Atmospheric Token |
| `--safe-top` | `max(1.25rem, env(safe-area-inset-top))` | Dimension / Scale Token |
| `--safe-right` | `max(1.25rem, env(safe-area-inset-right))` | Dimension / Scale Token |
| `--safe-bottom` | `max(1.25rem, env(safe-area-inset-bottom))` | Dimension / Scale Token |
| `--safe-left` | `max(1.25rem, env(safe-area-inset-left))` | Dimension / Scale Token |
| `--cursor-x` | `-120px` | Dimension / Scale Token |
| `--cursor-y` | `-120px` | Dimension / Scale Token |
| `--cursor-size` | `3.75rem` | Layout / Spatial Grid Token |
| `--label-width` | `150px` | Layout / Spatial Grid Token |
| `--label-top` | `52%` | Dimension / Scale Token |
| `--label-z-index` | `40` | Elevation / Border Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.topbar> — `christoph-nagel-dev`)**:
   - Landmark `<header class="topbar">` (`1400x64px`) hosting `Christoph Nagel · Webentwickler, Fot` navigation (`Kontakt`), DOM attributes (`data-inline-css="/styles.css?v=8b9c708..."`, `data-inline-css="/assets/css/seo-check..."`, `data-inline-css="/assets/css/wind-labe..."`, `data-inline-css="/assets/css/site-enha..."`), and stylesheet rule `html { background: 080808; }`.
2. **Hero Stage & Focal Lead (<section.panel> — `CHRISTOPH NAGEL Webentwickler, Fot`)**:
   - Landmark `<section class="panel panel--intro">` presenting display lead `CHRISTOPH NAGEL Webentwickler, Fotograf und Video...` and copy excerpt *"Webentwickler, Fotograf und Videograf aus Dorsten im Ruhrgebiet"* over `#080808` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.panel--content> — `Christoph Nagel Webentwickler, Fot`)**:
   - Landmark `<section class="panel panel--content">` rendering section `Christoph Nagel Webentwickler, Fotograf und Video...` with copy *"Code. Kamera. Klartext."*, asset references (`intro.jpg`, `anton-v27-latin-regular.woff2`, `site-media.js`, `llms.txt`), and grid rule `body { background: 080808; }`.
4. **Interactive Detail & Feature Matrix (<section.panel:nth(2)> — `Code. Kamera. Klartext.`)**:
   - Landmark `<section class="panel panel--content">` framing `Code. Kamera. Klartext.` and `Digitale Lösungen mit Substanz` (*"Seit 2001 beschäftige ich mich mit Webdesign und Webentwicklung. "*) with `#0a0a0a` surface cards, `#000000` accents, and `button { font: inherit; }`.
5. **Colophon & Global Directory Footer (<footer.legal-links> — `https://christoph-nagel.dev/`)**:
   - Landmark `<footer class="legal-links">` anchoring `Christoph Nagel · Webentwickler,` footer links (`Kontakt`), copy *"Auf Just a Web-Developer teile ich eigene Projekte, praktisc"*, and `#343434` structural dividers.
