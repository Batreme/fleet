---
title: "UI & UX Architecture: www-dbydt-space"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: www-dbydt-space

## Overview & Design Identity
- **Target**: `www-dbydt-space` (**Deebak Tamilmani · Design Portfolio**)
- **Production URL**: [https://www.dbydt.space](https://www.dbydt.space)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1280×828px`, Mobile `390×872px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#eeebe4` canvas, `#0000ee` ink, `#2b2b2b` accent)
- **Summary**: Design portfolio of Deebak Tamilmani. Fragments of architecture and design projects, held as memory rather than archive, drawn in real ti...
- **Total Clean CSS Variables Extracted**: `12` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Segoe UI`
- **Body Font Stack**: `Segoe UI`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 32px`, `line-height: normal`, `font-weight: 700`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 24px`, `line-height: normal`, `font-weight: 700`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 10px`, `line-height: 1.4`, `font-weight: 300`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--bhp-caption-row-height: 44px`, `--bhp-caption-top-padding: 16px`, `--ruler-label-top: 30px`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#eeebe4` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#2b2b2b` | `.bento-strip-cell-bhp { background: #2b2b2b }` |
| **Interactive Accent / Highlight** | `#2b2b2b` | `.bento-hello-open-btn { color: #2b2b2b }` |
| **Secondary / Muted Copy** | `#6b675f` | `t-content-text p.project-conten... { color: #6b675f }` |
| **Structural Hairline Border** | `#dbd8d2` | `.timeline-entry { border-top: #dbd8d2 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--pg-annot-mark-thickness` | `1.5px` | Dimension / Scale Token |
| `--pg-annot-bracket-size` | `8px` | Layout / Spatial Grid Token |
| `--fullscreen-ruler-reveal-inset` | `0%` | Dimension / Scale Token |
| `--project-surface` | `#EEEBE4` | Canvas / Surface Token |
| `--scene-clip-left` | `100%` | Dimension / Scale Token |
| `--bhp-caption-row-height` | `44px` | Layout / Spatial Grid Token |
| `--bhp-caption-top-padding` | `16px` | Layout / Spatial Grid Token |
| `--card-slot` | `max(300px, 25%)` | Dimension / Scale Token |
| `--ruler-height` | `30px` | Layout / Spatial Grid Token |
| `--ruler-label-top` | `30px` | Dimension / Scale Token |
| `--bento-title-size` | `clamp(5rem, min(16vw, 15vh), 8rem)` | Layout / Spatial Grid Token |
| `--stack-unit` | `40px` | Dimension / Scale Token |
| `--www-dbydt-space-bg` | `#eeebe4` | Canvas Substrate (from live computed `html` `background-color` (`computed_styles.json`)) |
| `--www-dbydt-space-ink` | `#0000ee` | Primary Typography Ink (computed-derived) |
| `--www-dbydt-space-surface` | `#2b2b2b` | Surface Substrate (computed-derived) |
| `--www-dbydt-space-accent` | `#2b2b2b` | Interactive Accent (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header> — `www-dbydt-space`)**:
   - Landmark `<header>` landmark (`1440px`) hosting `Deebak Tamilmani · Design Portfolio` navigation (`Hues of Al'Ula · A Street Within · Olakh · Atmos & Aura · Club & Courts`), DOM attributes (`data-website-id="8efd2acd-25e0-4014-bc..."`, `data-host-url="https://www.dbydt.space"`), and stylesheet rule `root { font-family:system-ui,-apple-system,Segoe UI,sans-serif;color:eeebe4;bac... }`.
2. **Hero Stage & Focal Lead (<main#seo-content> — `Deebak Tamilmani · Design Portfoli`)**:
   - Landmark `<main id="seo-content">` presenting display lead `Deebak Tamilmani · Design Portfolio` and copy excerpt *"Over the years, I have worked on many projects. Some were built, "* over `#eeebe4` canvas and `#0000ee` ink.
3. **Primary Showcase & Content Grid (<main#seo-content:nth(3)> — `Experience and education`)**:
   - Landmark `<main id="seo-content">` rendering section `Experience and education` with copy *"Hues of Al'Ula is a farm dwelling in the Cultural Oasis of Al'Ula"*, asset references (`favicon.svg`, `favicon-512.png`, `favicon-180.png`, `GeistPixel-Square.woff2`), and grid rule `.app { width:100%;height:100%;margin:0 }`.
4. **Interactive Detail & Feature Matrix (<main#seo-content:nth(4)> — `Projects`)**:
   - Landmark `<main id="seo-content">` framing `Projects` and `Research` (*"A Street Within is an office for a real estate developer in Ahmed"*) with `#2b2b2b` surface cards, `#2b2b2b` accents, and `html { -webkit-text-size-adjust:100%;text-size-adjust:100% }`.
5. **Colophon & Global Directory Footer (<footer> — `https://www.dbydt.space`)**:
   - Landmark `<footer>` landmark anchoring `Deebak Tamilmani · Design Portfo` footer links (`Hues of Al'Ula · A Street Within · Olakh · Atmos & Aura · Club & Courts`), copy *"Olakh , the Marathi word for identity, reimagines the Pre-Em"*, and `#dbd8d2` structural dividers.
