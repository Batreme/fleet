---
title: "UI & UX Architecture: milky-solar"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: milky-solar

## Overview & Design Identity
- **Target**: `milky-solar` (**Earth**)
- **Production URL**: [https://milky.solar](https://milky.solar)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×828px`, Mobile `390×872px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#ff0000` accent)
- **Summary**: Follow Wolfs journeys on Earth, navigating eternal cycles of conflict and transformation.
- **Total Clean CSS Variables Extracted**: `0` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `system-ui, -apple-system, sans-serif` (live computed system stack)
- **Body Font Stack**: `system-ui, -apple-system, sans-serif` (live computed system stack)
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: observed font-size ladder: `16px`, `13.3333px`
- **Section Heading (`H2`)**: observed font-size ladder: `16px`, `13.3333px`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 13.3333px`, `line-height: normal`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ff0000` | `select option:checked { background-color: red }` (`#ff0000`) |
| **Interactive Accent / Highlight** | `#ff0000` | live computed `button` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#ff0000` | `.footer-container a { color: red }` (`#ff0000`) |
| **Structural Hairline Border** | `#000000` | `footer { border-top: #000000 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--milky-solar-bg` | `#ffffff` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--milky-solar-ink` | `#000000` | Primary Typography Ink (computed-derived) |
| `--milky-solar-surface` | `#ff0000` | Surface Substrate (computed-derived) |
| `--milky-solar-accent` | `#ff0000` | Interactive Accent (computed-derived) |
| `--milky-solar-muted` | `#ff0000` | Secondary Ink (computed-derived) |
| `--milky-solar-border` | `#000000` | Structural Border (computed-derived) |
| `--milky-solar-container` | `1440px` | Container Bound (computed-derived) |
| `--milky-solar-gap` | `0px` | Grid Gutter (computed-derived) |
| `--milky-solar-pad` | `4px` | Lateral Padding (computed-derived) |
| `--milky-solar-ease` | `cubic-bezier(0.25,0.1,0.25,1)` | Primary Easing Function |
| `--milky-solar-radius` | `1px` | Corner Radius (computed-derived) |
| `--milky-solar-fs-base` | `16px` | Observed Font Size Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.button> — `milky-solar`)**:
   - Landmark `<header class="button">` (`800x415px`) hosting `Earth` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-scenario="new"`, `data-scenario="otherworld"`, `data-scenario="random"`, `data-scenario="israel"`), and stylesheet rule `body { background-color: white; color: black; width: 800px; text-align: center;... }`.
2. **Hero Stage & Focal Lead (<main.empty-space> — `Earth`)**:
   - Landmark `<main class="empty-space">` presenting display lead `Earth` and copy excerpt *"Follow Wolfs journeys on Earth, navigating eternal cycles of conf"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<main.float-up> — `Featured Work & Interactive Showca`)**:
   - Landmark `<main class="float-up">` rendering section `Featured Work & Interactive Showcase` with copy *"Earth"*, asset references (`milky.solar`, `Logo.ico`, `Logo.svg`, `Logo.jpg`), and grid rule `header { width: 100%; }`.
4. **Interactive Detail & Feature Matrix (<main.balloon> — `Technical Architecture & Narrative`)**:
   - Landmark `<main class="balloon">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Work & Interactive Showcase"*) with `#ff0000` surface cards, `#ff0000` accents, and `main { margin-bottom: 20px; }`.
5. **Colophon & Global Directory Footer (<footer.float-down> — `https://milky.solar`)**:
   - Landmark `<footer class="float-down">` anchoring `Earth` footer links (`Overview · Index · Archive · About · Contact`), copy *"Technical Architecture & Narrative"*, and `#000000` structural dividers.
