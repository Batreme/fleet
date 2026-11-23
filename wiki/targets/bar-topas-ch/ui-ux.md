---
title: "UI & UX Architecture: bar-topas-ch"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: bar-topas-ch

## Overview & Design Identity
- **Target**: `bar-topas-ch` (**Tòpas - bar-topas.ch**)
- **Production URL**: [https://bar-topas.ch/](https://bar-topas.ch/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#b21236` / `#feb914`)
- **Summary**: Tòpas by Topaze — Tapas & Bar. Découvrez la nouvelle cuisine hispano-suisse du Topaze.
- **Total Clean CSS Variables Extracted**: `21` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Source Sans 3`
- **Body Font Stack**: `Source Sans 3`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 42px`, `line-height: 60.9px`, `font-weight: 700`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 115.2px`, `line-height: 97.92px`, `font-weight: 800`)
- **Body Copy**: live computed `body` (`font-size: 21px`, `line-height: 30.45px`, `font-weight: 400`); rule `body` (`font-size: clamp(17px, 1.05vw + 10px, 21px)`, `line-height: 1.45`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 14px`, `line-height: 14px`, `font-weight: 800`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#b21236` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#efefe3` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#1d5f61` | `.vmap__frame { background: #1d5f61 }` |
| **Interactive Accent / Highlight** | `#feb914` | live computed `a` `background-color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#808080` | `.has-cyan-bluish-gray-color { color: gray }` (`#808080`) |
| **Structural Hairline Border** | `#bf435c` | `.s-visit__marquee-track { stroke: #bf435c }` |
| **Variable Token (`--creme-fond`)** | `#edeae0` | `var(--creme-fond)` in `:root` |
| **Variable Token (`--orange`)** | `#fe8826` | `var(--orange)` in `:root` |
| **Variable Token (`--orange-rouge`)** | `#f03812` | `var(--orange-rouge)` in `:root` |
| **Variable Token (`--bleu`)** | `#2c9fa2` | `var(--bleu)` in `:root` |
| **Variable Token (`--bordeaux`)** | `#7c1820` | `var(--bordeaux)` in `:root` |
| **Variable Token (`--brun`)** | `#60150d` | `var(--brun)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--rouge` | `#B21236` | Color / Atmospheric Token |
| `--creme` | `#EFEFE3` | Color / Atmospheric Token |
| `--creme-fond` | `#EDEAE0` | Color / Atmospheric Token |
| `--jaune` | `#FEB914` | Color / Atmospheric Token |
| `--orange` | `#FE8826` | Color / Atmospheric Token |
| `--orange-rouge` | `#F03812` | Color / Atmospheric Token |
| `--bleu` | `#2C9FA2` | Color / Atmospheric Token |
| `--bordeaux` | `#7C1820` | Color / Atmospheric Token |
| `--brun` | `#60150D` | Color / Atmospheric Token |
| `--f-title` | `"Archivo", "Arial Black", system-ui, sans-serif` | Dimension / Scale Token |
| `--f-cond` | `"Barlow Condensed", "Arial Narrow", system-ui, sans-serif` | Dimension / Scale Token |
| `--f-text` | `"Source Sans 3", Arial, system-ui, sans-serif` | Typography Ink Token |
| `--gutter` | `clamp(16px, 4vw, 56px)` | Layout / Spatial Grid Token |
| `--radius` | `22px` | Elevation / Border Token |
| `--ease` | `cubic-bezier(.2, .8, .2, 1)` | Motion / Easing Token |
| `--topbar-h` | `76px` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.topbar> — `bar-topas-ch`)**:
   - Landmark `<header class="topbar">` (`1440x76px`) hosting `Tòpas - bar-topas.ch` navigation (`Bar Le Topaze`), DOM attributes (`data-intro`, `data-intro-bar`, `data-intro-done`, `data-cursor`), and stylesheet rule `after { box-sizing: border-box; }`.
2. **Hero Stage & Focal Lead (<section.s-hero> — `Tòpas by Topaze — Tapas & Bar à Vi`)**:
   - Landmark `<section class="s-hero">` presenting display lead `Tòpas by Topaze — Tapas & Bar à Vicques` and copy excerpt *"Tapas & Bar by Topaze Vicques · JU"* over `#b21236` canvas and `#efefe3` ink.
3. **Primary Showcase & Content Grid (<section.s-marquee> — `Un pincho, c’est simple.`)**:
   - Landmark `<section class="s-marquee">` rendering section `Un pincho, c’est simple.` with copy *"Tòpas by Topaze — Tapas & Bar à Vicques"*, asset references (`1640559617463684`, `fbevents.js`, `gtm.js`, `archivo-var-latin.woff2`), and grid rule `html.lenis body { height: auto; }`.
4. **Interactive Detail & Feature Matrix (<section.s-def> — `Mucho délicieuse.`)**:
   - Landmark `<section class="s-def">` framing `Mucho délicieuse.` and `Seize noms, un seul conseil :` (*"Découvrez la nouvelle cuisine hispano-suisse du Topaze."*) with `#1d5f61` surface cards, `#feb914` accents, and `.lenis.lenis-smooth { scroll-behavior: auto !important; }`.
5. **Colophon & Global Directory Footer (<footer.s-end> — `https://bar-topas.ch/`)**:
   - Landmark `<footer class="s-end edge-wave">` anchoring `Tòpas - bar-topas.ch` footer links (`Bar Le Topaze`), copy *"MER & JEU dès 18H30 · VEN dès 17H00"*, and `#bf435c` structural dividers.
