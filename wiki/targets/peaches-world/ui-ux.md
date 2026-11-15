# UI & UX Architecture: peaches-world

## Overview & Design Identity
- **Target**: `peaches-world` (**Peaches – Webdesign Pratteln, Basel · Websites worth pressing Enter for**)
- **Production URL**: [https://peaches.world/](https://peaches.world/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ff5a00` / `#fff`)
- **Summary**: Peaches is a web design studio in Pratteln near Basel, Switzerland. Custom-designed, animated websites that feel like a game and stay in...
- **Total Clean CSS Variables Extracted**: `0` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Space Mono`
- **Body Font Stack**: `JetBrains Mono`
- **Monospace / Technical Font Stack**: `Space Mono`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(16px,1.25vw,18px)`, `15px`, `12px`, `13px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(16px,1.25vw,18px)`, `15px`, `12px`, `13px`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(16px,1.25vw,18px)`, `15px`, `12px`, `13px`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(16px,1.25vw,18px)`, `15px`, `12px`, `13px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ff5a00` | `html legend em { color: #ff5a00 }` |
| **Primary Typography Ink** | `#f2f2ee` | `:hover { color: #f2f2ee }` |
| **Elevated Surface / Card Substrate** | `#0a0b0e` | `body { background: #0a0b0e }` |
| **Interactive Accent / Highlight** | `#fff` | `.t { color: #fff }` |
| **Secondary / Muted Copy** | `#05070b` | `<meta name="theme-color" content="#05070b">` in `dom.html` |
| **Structural Hairline Border** | `#ff8a2a` | SVG/DOM `stop-color="#ff8a2a"` attribute in `dom.html` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--peaches-world-bg` | `#ff5a00` | Canvas Substrate (from `html legend em { color: #ff5a00 }`) |
| `--peaches-world-ink` | `#fff` | Primary Typography Ink (stylesheet-derived) |
| `--peaches-world-surface` | `#0a0b0e` | Surface Substrate (stylesheet-derived) |
| `--peaches-world-accent` | `#fff` | Interactive Accent (stylesheet-derived) |
| `--peaches-world-muted` | `#05070b` | Secondary Ink (stylesheet-derived) |
| `--peaches-world-border` | `#ff8a2a` | Structural Border (stylesheet-derived) |
| `--peaches-world-container` | `90vw` | Container Bound (stylesheet-derived) |
| `--peaches-world-gap` | `14px` | Grid Gutter (stylesheet-derived) |
| `--peaches-world-pad` | `9px` | Lateral Padding (stylesheet-derived) |
| `--peaches-world-ease` | `cubic-bezier(0.25,0.1,0.25,1)` | Primary Easing Function |
| `--peaches-world-radius` | `8px` | Corner Radius (stylesheet-derived) |
| `--peaches-world-fs-base` | `clamp(16px,1.25vw,18px)` | Observed Font Size Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.sr> — `peaches-world`)**:
   - Landmark `<nav class="sr">` hosting `Peaches – Webdesign Pratteln, Basel ` navigation (`Home · Who is talking · Work · References`), DOM attributes (`data-s="Chapter 01 / Home"`, `data-s="Pratteln 47.52 N 7.69 E"`, `data-s="Peaches"`, `data-s="Websites worth pressi..."`), and stylesheet rule `html body { font-family:var(--f-text) }`.
2. **Hero Stage & Focal Lead (<div.sr> — `Peaches – Webdesign Pratteln, Base`)**:
   - Landmark `<div class="sr">` presenting display lead `Peaches – Webdesign Pratteln, Basel · Websites w` and copy excerpt *"Web design · Pratteln near Basel · Switzerland"* over `#ff5a00` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<div.schild> — `Featured Work & Interactive Showca`)**:
   - Landmark `<div class="schild">` rendering section `Featured Work & Interactive Showcase` with copy *"Peaches – Webdesign Pratteln, Basel · Websites w"*, asset references (`logo.svg`, `favicon-192.png`, `favicon-48.png`, `apple-touch-icon.png`), and grid rule `oede a { font-family:var(--f-titel) }`.
4. **Interactive Detail & Feature Matrix (<div#kopf> — `Technical Architecture & Narrative`)**:
   - Landmark `<div id="kopf">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Work & Interactive Showcase"*) with `#0a0b0e` surface cards, `#fff` accents, and `runter { font-family:var(--f-titel) }`.
5. **Colophon & Global Directory Footer (<footer> — `https://peaches.world/`)**:
   - Landmark `<footer>` landmark anchoring `Peaches – Webdesign Pratteln, Ba` footer links (`Home · Who is talking · Work · References`), copy *"Technical Architecture & Narrative"*, and `#ff8a2a` structural dividers.
