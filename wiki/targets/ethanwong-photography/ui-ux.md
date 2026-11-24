---
title: "UI & UX Architecture: ethanwong-photography"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: ethanwong-photography

## Overview & Design Identity
- **Target**: `ethanwong-photography` (**Ethan W · Film-Inspired Wedding & Editorial Photographer · Washington DC...**)
- **Production URL**: [http://ethanwong.photography](http://ethanwong.photography)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×2484px`, Mobile `390×872px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#efede7` canvas, `#1c1813` ink, `#ff0000` accent)
- **Summary**: Documentary wedding, editorial, portrait and commercial photography by Ethan Wong of Ethan W Photography. Film-inspired, vintage-leaning...
- **Total Clean CSS Variables Extracted**: `52` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Hanken Grotesk`
- **Body Font Stack**: `Hanken Grotesk`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 32px`, `line-height: normal`, `font-weight: 700`)
- **Section Heading (`H2`)**: observed font-size ladder: `32px`, `16px`, `18px`, `29px`, `var(--lab-quiet)`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: clamp(14px,1.05vw,17px)`, `line-height: 1.5`, `font-weight: 600`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#efede7` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#1c1813` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f4efe4` | `.idx-slash { background: #f4efe4 }` |
| **Interactive Accent / Highlight** | `#ff0000` | `.cta-fill { background: red }` (`#ff0000`) |
| **Secondary / Muted Copy** | `#6a6154` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#d3cfc9` | `var(--sf-rule)` in `:root` (`rgba(36, 26, 16, .14)`) |
| **Variable Token (`--red`)** | `#9b1120` | `var(--red)` in `:root` |
| **Variable Token (`--red-hover`)** | `#b3162a` | `var(--red-hover)` in `:root` |
| **Variable Token (`--red-lift`)** | `#ab182c` | `var(--red-lift)` in `:root` |
| **Variable Token (`--red-lift-hover`)** | `#c01f34` | `var(--red-lift-hover)` in `:root` |
| **Variable Token (`--red-deep`)** | `#8a0f1e` | `var(--red-deep)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--red` | `#9b1120` | Color / Atmospheric Token |
| `--red-hover` | `#b3162a` | Color / Atmospheric Token |
| `--red-lift` | `#ab182c` | Color / Atmospheric Token |
| `--red-lift-hover` | `#c01f34` | Color / Atmospheric Token |
| `--red-deep` | `#8a0f1e` | Color / Atmospheric Token |
| `--lab-nav` | `13px` | Layout / Spatial Grid Token |
| `--lab` | `12px` | Dimension / Scale Token |
| `--lab-sm` | `11px` | Dimension / Scale Token |
| `--lab-dock` | `9.5px` | Dimension / Scale Token |
| `--lab-quiet` | `10px` | Dimension / Scale Token |
| `--lab-w` | `400` | Design System Custom Token |
| `--lab-w-nav` | `400` | Layout / Spatial Grid Token |
| `--lab-w-dock` | `500` | Design System Custom Token |
| `--head-band` | `74px` | Dimension / Scale Token |
| `--foot-band` | `58px` | Dimension / Scale Token |
| `--lap-vh` | `100vw` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site> — `ethanwong-photography`)**:
   - Landmark `<header class="site nav-on-dark">` (`1440x74px`) hosting `Ethan W · Film-Inspired Wedding & Ed` navigation (`Editorial Exchange`), DOM attributes (`data-cursor="always"`, `data-nav`, `data-cta-ink`, `data-nav-theme="dark"`), and stylesheet rule `body { --red: var(--red-lift);--red-hover: var(--red-lift-hover) }`.
2. **Hero Stage & Focal Lead (<main.idx-main> — `Ethan W (Ethan Wong), film-inspire`)**:
   - Landmark `<main class="idx-main">` presenting display lead `Ethan W (Ethan Wong), film-inspired documentary w...` and copy excerpt *"The full collection in one grid. Any frame opens large."* over `#efede7` canvas and `#1c1813` ink.
3. **Primary Showcase & Content Grid (<main.idx-main:nth(2)> — `The full collection in one grid. A`)**:
   - Landmark `<main class="idx-main">` rendering section `The full collection in one grid. Any frame opens` with copy *"W e d d i n g s W e d d i n g s"*, asset references (`favicon-32.png`, `favicon-16.png`, `favicon-32-dark.png`, `favicon-16-dark.png`), and grid rule `.idx-wrap { position:relative;min-height:100vh;min-height:100svh;background:0f0e0c }`.
4. **Interactive Detail & Feature Matrix (<main.idx-main:nth(3)> — `W e d d i n g s W e d d i n g s`)**:
   - Landmark `<main class="idx-main">` framing `W e d d i n g s W e d d i n g s` and `Stories & galleries` (*"Stories & galleries"*) with `#f4efe4` surface cards, `#ff0000` accents, and `.idx-backdrop { position:absolute;inset:0;z-index:0;overflow:hidden }`.
5. **Colophon & Global Directory Footer (<footer.sf> — `http://ethanwong.photography`)**:
   - Landmark `<footer class="sf sf--fixed">` anchoring `Ethan W · Film-Inspired Wedding ` footer links (`Editorial Exchange`), copy *"All visual stories"*, and `#d3cfc9` structural dividers.
