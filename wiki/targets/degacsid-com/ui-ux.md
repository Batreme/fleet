---
title: "UI & UX Architecture: degacsid-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: degacsid-com

## Overview & Design Identity
- **Target**: `degacsid-com` (**DEGACSID**)
- **Production URL**: [https://degacsid.com/](https://degacsid.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fffcf9` / `#e55655`)
- **Summary**: The Only Creative Partner You'll Need. Full Service Creative Agency that handles everything from strategy, conception, design, execution,...
- **Total Clean CSS Variables Extracted**: `1` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Helvetica Neue`
- **Body Font Stack**: `Return of the Boss`
- **Monospace / Technical Font Stack**: `IBM Plex Mono`
- **Hero Display (`H1`)**: observed font-size ladder: `16px`, `11px`, `10px`, `0.62em`
- **Section Heading (`H2`)**: observed font-size ladder: `16px`, `11px`, `10px`, `0.62em`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#fffcf9` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#0a0a0c` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#e55655` | `.navg9eskz-mi:focus-visible .na... { color: #e55655 }` |
| **Secondary / Muted Copy** | `#fff4e7` | live computed `a` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#fff4e7` | hairline divider derived from live computed `a` `color` (`computed_styles.json`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--crt-safe` | `31px` | Dimension / Scale Token |
| `--degacsid-com-bg` | `#fffcf9` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--degacsid-com-ink` | `#000000` | Primary Typography Ink (computed-derived) |
| `--degacsid-com-surface` | `#0a0a0c` | Surface Substrate (computed-derived) |
| `--degacsid-com-accent` | `#e55655` | Interactive Accent (computed-derived) |
| `--degacsid-com-muted` | `#fff4e7` | Secondary Ink (computed-derived) |
| `--degacsid-com-border` | `#fff4e7` | Structural Border (computed-derived) |
| `--degacsid-com-container` | `1440px` | Container Bound (computed-derived) |
| `--degacsid-com-gap` | `12px` | Grid Gutter (computed-derived) |
| `--degacsid-com-pad` | `10px` | Lateral Padding (computed-derived) |
| `--degacsid-com-ease` | `cubic-bezier(0.5,0,0.2,1)` | Primary Easing Function |
| `--degacsid-com-radius` | `50%` | Corner Radius (computed-derived) |
| `--degacsid-com-fs-base` | `16px` | Observed Font Size Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.cls-1> — `degacsid-com`)**:
   - Landmark `<header class="cls-1">` (`1440px`) hosting `DEGACSID` navigation (`▶︎ SERVICES · ▶︎ PROCESS · ▶︎ CASE STUDIES · ▶︎ ABOUT · ▶︎ CONTACT`), DOM attributes (`data-name="Layer 1"`), and stylesheet rule `font-face { font-family:Return of the Boss;src:url(/fonts/ReturnOfTheBoss.ttf) forma... }`.
2. **Hero Stage & Focal Lead (<div.navg9eskz-mi> — `DEGACSID`)**:
   - Landmark `<div class="navg9eskz-mi">` presenting display lead `DEGACSID` and copy excerpt *"The Only Creative Partner You'll Need. Full Service Creative Agen"* over `#fffcf9` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<div.navg9eskz-lbl> — `Featured Work & Interactive Showca`)**:
   - Landmark `<div class="navg9eskz-lbl">` rendering section `Featured Work & Interactive Showcase` with copy *"DEGACSID"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `main-D5gnYzr4.js`), and grid rule `root { margin:0;padding:0;width:100%;height:100% }`.
4. **Interactive Detail & Feature Matrix (<div.navg9eskz-arw> — `Technical Architecture & Narrative`)**:
   - Landmark `<div class="navg9eskz-arw">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Work & Interactive Showcase"*) with `#0a0a0c` surface cards, `#e55655` accents, and `body { background:fffcf9;overflow:hidden;-webkit-font-smoothing:antialiased }`.
5. **Colophon & Global Directory Footer (<footer> — `https://degacsid.com/`)**:
   - Landmark `<footer>` landmark anchoring `DEGACSID` footer links (`▶︎ SERVICES · ▶︎ PROCESS · ▶︎ CASE STUDIES · ▶︎ ABOUT · ▶︎ CONTACT`), copy *"Technical Architecture & Narrative"*, and `#fff4e7` structural dividers.
