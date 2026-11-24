---
title: "UI & UX Architecture: tamasolajos-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: tamasolajos-com

## Overview & Design Identity
- **Target**: `tamasolajos-com` (**Tamás Olajos — AI Filmmaker & Director · London & Budapest**)
- **Production URL**: [https://tamasolajos.com/](https://tamasolajos.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×828px`, Mobile `390×2616px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#ffffff`)
- **Summary**: Tamás Olajos is an award-winning AI filmmaker and director, Runway and Dreamina Creative Partner. Cinematic commercial campaigns and expe...
- **Total Clean CSS Variables Extracted**: `1` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `system-ui, -apple-system, sans-serif` (live computed system stack)
- **Body Font Stack**: `system-ui, -apple-system, sans-serif` (live computed system stack)
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: observed font-size ladder: `10px`
- **Section Heading (`H2`)**: observed font-size ladder: `10px`
- **Body Copy**: live computed `body` (`font-size: 10px`, `line-height: normal`, `font-weight: 400`)
- **Metadata & Labels**: observed font-size ladder: `10px`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | `body` default contrast ink (`#ffffff`) |
| **Elevated Surface / Card Substrate** | `#000000` | transparent/inherited card surface over live computed `html` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ffffff` | `body` default contrast ink (`#ffffff`) |
| **Secondary / Muted Copy** | `#ffffff` | secondary opacity step of `body` default contrast ink (`#ffffff`) |
| **Structural Hairline Border** | `#ffffff` | hairline divider derived from secondary opacity step of `body` default contrast ink (`#ffffff`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--inner-height` | `900px` | Layout / Spatial Grid Token |
| `--tamasolajos-com-bg` | `#000000` | Canvas Substrate (from live computed `html` `background-color` (`computed_styles.json`)) |
| `--tamasolajos-com-ink` | `#ffffff` | Primary Typography Ink (computed-derived) |
| `--tamasolajos-com-surface` | `#000000` | Surface Substrate (computed-derived) |
| `--tamasolajos-com-accent` | `#ffffff` | Interactive Accent (computed-derived) |
| `--tamasolajos-com-muted` | `#ffffff` | Secondary Ink (computed-derived) |
| `--tamasolajos-com-border` | `#ffffff` | Structural Border (computed-derived) |
| `--tamasolajos-com-container` | `1440px` | Container Bound (computed-derived) |
| `--tamasolajos-com-gap` | `0px` | Grid Gutter (computed-derived) |
| `--tamasolajos-com-pad` | `1rem` | Lateral Padding (computed-derived) |
| `--tamasolajos-com-ease` | `cubic-bezier(0.25,0.1,0.25,1)` | Primary Easing Function |
| `--tamasolajos-com-radius` | `4rem` | Corner Radius (computed-derived) |
| `--tamasolajos-com-fs-base` | `10px` | Observed Font Size Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.webgl> — `tamasolajos-com`)**:
   - Landmark `<header class="webgl">` (`1440px`) hosting `Tamás Olajos — AI Filmmaker & Direct` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-engine="three.js r181"`), and stylesheet rule `body { overscroll-behavior:none;touch-action:none;margin:0;padding:0;overflow:h... }`.
2. **Hero Stage & Focal Lead (<div.webgl> — `Tamás Olajos — AI Filmmaker & Dire`)**:
   - Landmark `<div class="webgl">` presenting display lead `Tamás Olajos — AI Filmmaker & Director · London ` and copy excerpt *"Tamás Olajos is an award-winning AI filmmaker and director, Runwa"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<div.webgl:nth(2)> — `Featured Work & Interactive Showca`)**:
   - Landmark `<div class="webgl">` rendering section `Featured Work & Interactive Showcase` with copy *"Tamás Olajos — AI Filmmaker & Director · London "*, asset references (`favicon.svg`, `index-BZCf80GG.js`, `index-DcXtDSRr.css`, `showreel_short.mp4`), and grid rule `html { background-color:000;font-size:10px }`.
4. **Interactive Detail & Feature Matrix (<div.webgl:nth(3)> — `Technical Architecture & Narrative`)**:
   - Landmark `<div class="webgl">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Work & Interactive Showcase"*) with `#000000` surface cards, `#ffffff` accents, and `.webgl { -webkit-user-select:none;user-select:none;width:100dvw;height:100dvh;pos... }`.
5. **Colophon & Global Directory Footer (<footer> — `https://tamasolajos.com/`)**:
   - Landmark `<footer>` landmark anchoring `Tamás Olajos — AI Filmmaker & Di` footer links (`Overview · Index · Archive · About · Contact`), copy *"Technical Architecture & Narrative"*, and `#ffffff` structural dividers.
