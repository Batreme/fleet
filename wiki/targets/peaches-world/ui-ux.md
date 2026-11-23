---
title: "UI & UX Architecture: peaches-world"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: peaches-world

## Overview & Design Identity
- **Target**: `peaches-world` (**Peaches – Webdesign Pratteln, Basel · Websites worth pressing Enter for**)
- **Production URL**: [https://peaches.world/](https://peaches.world/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0a0b0e` / `#ff5a00`)
- **Summary**: Peaches is a web design studio in Pratteln near Basel, Switzerland. Custom-designed, animated websites that feel like a game and stay in...
- **Total Clean CSS Variables Extracted**: `0` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Space Mono`
- **Body Font Stack**: `JetBrains Mono`
- **Monospace / Technical Font Stack**: `Space Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 129.6px`, `line-height: 123.12px`, `font-weight: 700`, `letter-spacing: -2.592px`)
- **Section Heading (`H2`)**: observed font-size ladder: `129.6px`, `16px`, `12px`, `clamp(16px,1.25vw,18px)`, `15px`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0a0b0e` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f2f2ee` | `.sr:focus-within { background: #f2f2ee }` |
| **Interactive Accent / Highlight** | `#ff5a00` | `html legend em { color: #ff5a00 }` |
| **Secondary / Muted Copy** | `#f2f2ee` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#7e7e7e` | `body.voll #satz { border-color: #7e7e7e }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--peaches-world-bg` | `#0a0b0e` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--peaches-world-ink` | `#ffffff` | Primary Typography Ink (computed-derived) |
| `--peaches-world-surface` | `#f2f2ee` | Surface Substrate (computed-derived) |
| `--peaches-world-accent` | `#ff5a00` | Interactive Accent (computed-derived) |
| `--peaches-world-muted` | `#f2f2ee` | Secondary Ink (computed-derived) |
| `--peaches-world-border` | `#7e7e7e` | Structural Border (computed-derived) |
| `--peaches-world-container` | `1440px` | Container Bound (computed-derived) |
| `--peaches-world-gap` | `14px` | Grid Gutter (computed-derived) |
| `--peaches-world-pad` | `9px` | Lateral Padding (computed-derived) |
| `--peaches-world-ease` | `cubic-bezier(0.25,0.1,0.25,1)` | Primary Easing Function |
| `--peaches-world-radius` | `8px` | Corner Radius (computed-derived) |
| `--peaches-world-fs-base` | `129.6px` | Observed Font Size Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.sr> — `peaches-world`)**:
   - Landmark `<nav class="sr">` (`1x1px`) hosting `Peaches – Webdesign Pratteln, Basel ` navigation (`Home · Who is talking · Work · References`), DOM attributes (`data-s="Chapter 01 / Home"`, `data-s="Pratteln 47.52 N 7.69 E"`, `data-s="Peaches"`, `data-s="Websites worth pressi..."`), and stylesheet rule `html body { font-family:var(--f-text) }`.
2. **Hero Stage & Focal Lead (<div.sr> — `Peaches – Webdesign Pratteln, Base`)**:
   - Landmark `<div class="sr">` presenting display lead `Peaches – Webdesign Pratteln, Basel · Websites w` and copy excerpt *"WEB DESIGN · PRATTELN NEAR BASEL · SWITZERLAND"* over `#0a0b0e` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<div.schild> — `Featured Work & Interactive Showca`)**:
   - Landmark `<div class="schild">` rendering section `Featured Work & Interactive Showcase` with copy *"Web design · Pratteln near Basel · Switzerland"*, asset references (`logo.svg`, `favicon-192.png`, `favicon-48.png`, `apple-touch-icon.png`), and grid rule `oede a { font-family:var(--f-titel) }`.
4. **Interactive Detail & Feature Matrix (<div#kopf> — `Technical Architecture & Narrative`)**:
   - Landmark `<div id="kopf">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Work & Interactive Showcase"*) with `#f2f2ee` surface cards, `#ff5a00` accents, and `runter { font-family:var(--f-titel) }`.
5. **Colophon & Global Directory Footer (<footer> — `https://peaches.world/`)**:
   - Landmark `<footer>` landmark anchoring `Peaches – Webdesign Pratteln, Ba` footer links (`Home · Who is talking · Work · References`), copy *"Technical Architecture & Narrative"*, and `#7e7e7e` structural dividers.
