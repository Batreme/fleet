---
title: "UI & UX Architecture: ofrenda-davidlangarica-dev"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: ofrenda-davidlangarica-dev

## Overview & Design Identity
- **Target**: `ofrenda-davidlangarica-dev` (**OFRENDA — Create a personal Día de Muertos altar**)
- **Production URL**: [https://ofrenda.davidlangarica.dev](https://ofrenda.davidlangarica.dev)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#20201f` / `#e4b687`)
- **Summary**: Create a personal Día de Muertos ofrenda with a photograph, flowers, candles, and meaningful offerings. A quiet place to remember someone...
- **Total Clean CSS Variables Extracted**: `37` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Marqen`
- **Body Font Stack**: `Georgia`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 210px`, `line-height: 180.6px`, `font-weight: 400`); rule `h1` (`font-size: clamp(44px,12vw,72px)`, `line-height: 1.08`, `font-weight: 400`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 30px`, `line-height: 1.1`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--ui-font-body: Georgia, "Times New Roman", serif`, `--ui-body-size: clamp(16px, 1.5vw, 19px)`, `--ui-body-line-height: 1.55`; rule `p` (`font-size: 16px`, `line-height: 1.4`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 14px`, `line-height: 23.1px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#20201f` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | `.app-shell { background: #000000 }` |
| **Interactive Accent / Highlight** | `#e4b687` | `.primary-button { background: #e4b687 }` |
| **Secondary / Muted Copy** | `#ef893b` | `var(--ui-heading)` in `:root` |
| **Structural Hairline Border** | `#79756f` | `.recenter-button { border: #79756f }` |
| **Variable Token (`--ui-text`)** | `#f4e6cf` | `var(--ui-text)` in `:root` |
| **Variable Token (`--ui-muted`)** | `#d5c4a9` | `var(--ui-muted)` in `:root` |
| **Variable Token (`--ui-home-heading`)** | `#f3e3c7` | `var(--ui-home-heading)` in `:root` |
| **Variable Token (`--ui-focus`)** | `#efd6a4` | `var(--ui-focus)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ui-font-heading` | `"Marqen", Georgia, "Times New Roman", serif` | Typography Ink Token |
| `--ui-font-body` | `Georgia, "Times New Roman", serif` | Typography / Scale Token |
| `--ui-text-shadow` | `0 2px 14px #000` | Typography Ink Token |
| `--ui-backdrop` | `#000` | Color / Atmospheric Token |
| `--ui-text` | `#f4e6cf` | Typography Ink Token |
| `--ui-muted` | `#d5c4a9` | Color / Atmospheric Token |
| `--ui-heading` | `#ef893b` | Typography Ink Token |
| `--ui-home-heading` | `#f3e3c7` | Typography Ink Token |
| `--ui-amber-rgb` | `189 149 91` | Design System Custom Token |
| `--ui-amber` | `rgb(var(--ui-amber-rgb))` | Color / Atmospheric Token |
| `--ui-surface-rgb` | `70 39 17` | Canvas / Surface Token |
| `--ui-surface` | `rgb(var(--ui-surface-rgb) / .18)` | Canvas / Surface Token |
| `--ui-surface-hover` | `rgb(160 110 49 / .2)` | Canvas / Surface Token |
| `--ui-surface-pressed` | `rgb(184 133 67 / .28)` | Canvas / Surface Token |
| `--ui-border` | `rgb(var(--ui-amber-rgb) / .74)` | Elevation / Border Token |
| `--ui-focus` | `#efd6a4` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.experience-chrome> — `ofrenda-davidlangarica-dev`)**:
   - Landmark `<header class="experience-chrome">` (`1440x900px`) hosting `OFRENDA — Create a personal Día de M` navigation (`David Langarica`), DOM attributes (`data-cf-beacon="("token":"e723bd39f9d..."`, `data-engine="three.js r180 webgpu"`, `data-on="true"`, `data-loading-progress="0.7500000000000001"`), and stylesheet rule `html.lenis body { height:auto }`.
2. **Hero Stage & Focal Lead (<section.floating-menu> — `OFRENDA`)**:
   - Landmark `<section class="floating-menu">` presenting display lead `OFRENDA` and copy excerpt *"For you, who still have a place here."* over `#20201f` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.floating-menu:nth(2)> — `For you, who still have a place he`)**:
   - Landmark `<section class="floating-menu">` rendering section `For you, who still have a place here.` with copy *"Language Choose English or Spanish."*, asset references (`favicon.ico`, `Marqen.woff2`, `index-CUtJAqPO.js`, `index-BRkV915_.css`), and grid rule `.lenis-stopped { overflow:clip }`.
4. **Interactive Detail & Feature Matrix (<section.floating-menu:nth(3)> — `Language Choose English or Spanish`)**:
   - Landmark `<section class="floating-menu">` framing `Language Choose English or Spanish.` and `Sound Music and ambience.` (*"Sound Music and ambience."*) with `#000000` surface cards, `#e4b687` accents, and `.lenis.lenis-smooth iframe { pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.menu-footer> — `https://ofrenda.davidlangarica.dev`)**:
   - Landmark `<footer class="menu-footer">` anchoring `OFRENDA — Create a personal Día ` footer links (`David Langarica`), copy *"Graphics Available after the water and salt."*, and `#79756f` structural dividers.
