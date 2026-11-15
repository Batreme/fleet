# UI & UX Architecture: tamasolajos-com

## Overview & Design Identity
- **Target**: `tamasolajos-com` (**Tamás Olajos — AI Filmmaker & Director · London & Budapest**)
- **Production URL**: [https://tamasolajos.com/](https://tamasolajos.com/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#0000`)
- **Summary**: Tamás Olajos is an award-winning AI filmmaker and director, Runway and Dreamina Creative Partner. Cinematic commercial campaigns and expe...
- **Total Clean CSS Variables Extracted**: `1` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `system-ui, -apple-system, sans-serif` (no custom `@font-face` extracted)
- **Body Font Stack**: `system-ui, -apple-system, sans-serif` (no custom `@font-face` extracted)
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `10px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `10px`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `10px`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `10px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `html { background-color: #000 }` |
| **Primary Typography Ink** | `#0000` | `.ui .button { border: #0000 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--inner-height` | `900px` | Layout / Spatial Grid Token |
| `--tamasolajos-com-bg` | `#000` | Canvas Substrate (from `html { background-color: #000 }`) |
| `--tamasolajos-com-ink` | `#0000` | Primary Typography Ink (stylesheet-derived) |
| `--tamasolajos-com-surface` | `#000` | Surface Substrate (stylesheet-derived) |
| `--tamasolajos-com-accent` | `#0000` | Interactive Accent (stylesheet-derived) |
| `--tamasolajos-com-muted` | `#0000` | Secondary Ink (stylesheet-derived) |
| `--tamasolajos-com-border` | `#0000` | Structural Border (stylesheet-derived) |
| `--tamasolajos-com-container` | `none` | Container Bound (stylesheet-derived) |
| `--tamasolajos-com-gap` | `0px` | Grid Gutter (stylesheet-derived) |
| `--tamasolajos-com-pad` | `1rem` | Lateral Padding (stylesheet-derived) |
| `--tamasolajos-com-ease` | `cubic-bezier(0.25,0.1,0.25,1)` | Primary Easing Function |
| `--tamasolajos-com-radius` | `4rem` | Corner Radius (stylesheet-derived) |
| `--tamasolajos-com-fs-base` | `10px` | Observed Font Size Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.webgl> — `tamasolajos-com`)**:
   - Landmark `<header class="webgl">` hosting `Tamás Olajos — AI Filmmaker & Direct` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-engine="three.js r181"`), and stylesheet rule `body { overscroll-behavior:none;touch-action:none;margin:0;padding:0;overflow:h... }`.
2. **Hero Stage & Focal Lead (<div.webgl> — `Tamás Olajos — AI Filmmaker & Dire`)**:
   - Landmark `<div class="webgl">` presenting display lead `Tamás Olajos — AI Filmmaker & Director · London ` and copy excerpt *"Tamás Olajos is an award-winning AI filmmaker and director, Runwa"* over `#000` canvas and `#0000` ink.
3. **Primary Showcase & Content Grid (<div.webgl> — `Featured Work & Interactive Showca`)**:
   - Landmark `<div class="webgl">` rendering section `Featured Work & Interactive Showcase` with copy *"Tamás Olajos — AI Filmmaker & Director · London "*, asset references (`favicon.svg`, `index-BZCf80GG.js`, `index-DcXtDSRr.css`, `showreel_short.mp4`), and grid rule `html { background-color:000;font-size:10px }`.
4. **Interactive Detail & Feature Matrix (<div.webgl> — `Technical Architecture & Narrative`)**:
   - Landmark `<div class="webgl">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Work & Interactive Showcase"*) with `#000` surface cards, `#0000` accents, and `.webgl { -webkit-user-select:none;user-select:none;width:100dvw;height:100dvh;pos... }`.
5. **Colophon & Global Directory Footer (<footer> — `https://tamasolajos.com/`)**:
   - Landmark `<footer>` landmark anchoring `Tamás Olajos — AI Filmmaker & Di` footer links (`Overview · Index · Archive · About · Contact`), copy *"Technical Architecture & Narrative"*, and `#0000` structural dividers.
