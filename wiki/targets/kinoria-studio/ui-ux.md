# UI & UX Architecture: kinoria-studio

## Overview & Design Identity
- **Target**: `kinoria-studio` (**KINORIA**)
- **Production URL**: [https://kinoria.studio/](https://kinoria.studio/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#F2EDE4`)
- **Summary**: KINORIA 135 is a concept for a fully mechanical 35mm film camera, made as an interactive website. Pick a film, look through the viewfinde...
- **Total Clean CSS Variables Extracted**: `1` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `system-ui, -apple-system, sans-serif` (no custom `@font-face` extracted)
- **Body Font Stack**: `system-ui, -apple-system, sans-serif` (no custom `@font-face` extracted)
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `14px`, `13px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `14px`, `13px`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `14px`, `13px`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `14px`, `13px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `body { background: #000 }` |
| **Primary Typography Ink** | `#7ee6ff` | `#hud { color: #7ee6ff }` |
| **Elevated Surface / Card Substrate** | `#ff6b6b` | `#err { color: #ff6b6b }` |
| **Interactive Accent / Highlight** | `#F2EDE4` | `#deadnote { color: #F2EDE4 }` |
| **Secondary / Muted Copy** | `#a39a8f` | `#deadnote .db { color: #a39a8f }` |
| **Structural Hairline Border** | `#e8e2d6` | `#deadnote .dr:focus-visible { background: #e8e2d6 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--kpx` | `clamp(1px, min(100vw / 1920, 100vh / 911), 3px)` | Dimension / Scale Token |
| `--kinoria-studio-bg` | `#000` | Canvas Substrate (from `body { background: #000 }`) |
| `--kinoria-studio-ink` | `#F2EDE4` | Primary Typography Ink (stylesheet-derived) |
| `--kinoria-studio-surface` | `#ff6b6b` | Surface Substrate (stylesheet-derived) |
| `--kinoria-studio-accent` | `#F2EDE4` | Interactive Accent (stylesheet-derived) |
| `--kinoria-studio-muted` | `#a39a8f` | Secondary Ink (stylesheet-derived) |
| `--kinoria-studio-border` | `#e8e2d6` | Structural Border (stylesheet-derived) |
| `--kinoria-studio-container` | `70vw` | Container Bound (stylesheet-derived) |
| `--kinoria-studio-gap` | `0px` | Grid Gutter (stylesheet-derived) |
| `--kinoria-studio-pad` | `24px` | Lateral Padding (stylesheet-derived) |
| `--kinoria-studio-ease` | `cubic-bezier(0.25,0.1,0.25,1)` | Primary Easing Function |
| `--kinoria-studio-radius` | `999px` | Corner Radius (stylesheet-derived) |
| `--kinoria-studio-fs-base` | `12px` | Observed Font Size Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.kc-on> — `kinoria-studio`)**:
   - Landmark `<header class="kc-on">` hosting `KINORIA` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-doc="intro"`, `data-engine="three.js r185"`), and stylesheet rule `dot { display:none!important }`.
2. **Hero Stage & Focal Lead (<div.dzresp> — `KINORIA`)**:
   - Landmark `<div class="dzresp">` presenting display lead `KINORIA` and copy excerpt *"THE ROLL DID NOT LOAD"* over `#000` canvas and `#F2EDE4` ink.
3. **Primary Showcase & Content Grid (<div.bootd> — `Featured Work & Interactive Showca`)**:
   - Landmark `<div class="bootd">` rendering section `Featured Work & Interactive Showcase` with copy *"This page could not be drawn. The connection may have dropped, or"*, asset references (`Archivo-Variable.woff2`, `wordmark.svg`, `details_entry_1920x911-DmzTlZIo.webp`, `favicon.svg`), and grid rule `body { height: 100%; background: 000; overflow: hidden; }`.
4. **Interactive Detail & Feature Matrix (<div.bootvf> — `Technical Architecture & Narrative`)**:
   - Landmark `<div class="bootvf">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Reload to try again."*) with `#ff6b6b` surface cards, `#F2EDE4` accents, and `stage { position: fixed; inset: 0; touch-action: none; }`.
5. **Colophon & Global Directory Footer (<footer.intro-drawn> — `https://kinoria.studio/`)**:
   - Landmark `<footer class="intro-drawn">` anchoring `KINORIA` footer links (`Overview · Index · Archive · About · Contact`), copy *"Technical Architecture & Narrative"*, and `#e8e2d6` structural dividers.
