---
title: "UI & UX Architecture: grids03-obys-agency"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: grids03-obys-agency

## Overview & Design Identity
- **Target**: `grids03-obys-agency` (**Grids — DES Season 03**)
- **Production URL**: [https://grids03.obys.agency/](https://grids03.obys.agency/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#000000`)
- **Summary**: Grids is an interactive project exploring grids, composition, and key design principles through visual experiments. First launched in 202...
- **Total Clean CSS Variables Extracted**: `20` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Obys Sans`
- **Body Font Stack**: `Obys Sans`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 90px`, `line-height: 108px`, `font-weight: 400`, `letter-spacing: -5.4px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 90px`, `line-height: 108px`, `font-weight: 400`, `letter-spacing: -5.4px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: 14px`, `font-weight: 400`, `letter-spacing: -0.24px`); CSS variables `--caption-size: 90px`, `--small-size: 12px`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#d9d9d9` | `.grid-entry__picture { background: #d9d9d9 }` |
| **Interactive Accent / Highlight** | `#000000` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#b2b2b2` | `.about__line--quiet i { color: #b2b2b2 }` |
| **Structural Hairline Border** | `#e1e1e1` | `var(--color-rule)` in `:root` |
| **Variable Token (`--color-ground`)** | `#dedfd9` | `var(--color-ground)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-bg` | `#fff` | Canvas / Surface Token |
| `--color-ink` | `#000` | Typography Ink Token |
| `--color-ground` | `#dedfd9` | Brand / Palette Token |
| `--color-rule` | `#e1e1e1` | Brand / Palette Token |
| `--layer-gl` | `0` | Design System Custom Token |
| `--layer-content` | `2` | Design System Custom Token |
| `--layer-header` | `3` | Layout / Spatial Grid Token |
| `--layer-preloader` | `50` | Design System Custom Token |
| `--grid-columns` | `12` | Layout / Spatial Grid Token |
| `--grid-margin` | `20` | Layout / Spatial Grid Token |
| `--grid-gutter` | `20` | Layout / Spatial Grid Token |
| `--vw` | `1440px` | Layout / Spatial Grid Token |
| `--vh` | `900px` | Layout / Spatial Grid Token |
| `--caption-size` | `90px` | Layout / Spatial Grid Token |
| `--small-size` | `12px` | Layout / Spatial Grid Token |
| `--edge` | `18px` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.is-up> — `grids03-obys-agency`)**:
   - Landmark `<header class="is-up">` (`1440px`) hosting `Grids — DES Season 03` navigation (`Grids · More About Season · Enroll Now · Learn for Free · Obys`), DOM attributes (`data-preloader`, `data-ground`, `data-bar`, `data-letter="G"`), and stylesheet rule `body { overflow-x:hidden }`.
2. **Hero Stage & Focal Lead (<section.intro> — `G R I D S S 0 3`)**:
   - Landmark `<section class="intro">` presenting display lead `G R I D S S 0 3` and copy excerpt *"Design Education Series®Obys"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.grid-block> — `G r i d s S 0 3`)**:
   - Landmark `<section class="grid-block">` rendering section `G r i d s S 0 3` with copy *"Design Education Series® Obys"*, asset references (`favicon.svg`, `favicon-32.png`, `favicon-180.png`, `ObysSans-Regular.woff2`), and grid rule `.stage { width:100%;height:100%;z-index:var(--layer-gl);pointer-events:none;posit... }`.
4. **Interactive Detail & Feature Matrix (<section.story> — `4 - C o l u m n`)**:
   - Landmark `<section class="story">` framing `4 - C o l u m n` and `G r i d` (*"Grids — DES Season 03. 17 lectures."*) with `#d9d9d9` surface cards, `#000000` accents, and `.preloader { z-index:var(--layer-preloader);pointer-events:none;position:fixed;inset:... }`.
5. **Colophon & Global Directory Footer (<footer.preloader__ground> — `https://grids03.obys.agency/`)**:
   - Landmark `<footer class="preloader__ground">` anchoring `Grids — DES Season 03` footer links (`Grids · More About Season · Enroll Now · Learn for Free · Obys`), copy *"4+ hours on grids and composition."*, and `#e1e1e1` structural dividers.
