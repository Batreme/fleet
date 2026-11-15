# UI & UX Architecture: degacsid-com

## Overview & Design Identity
- **Target**: `degacsid-com` (**DEGACSID**)
- **Production URL**: [https://degacsid.com/](https://degacsid.com/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fffcf9` / `#E55655`)
- **Summary**: The Only Creative Partner You'll Need. Full Service Creative Agency that handles everything from strategy, conception, design, execution,...
- **Total Clean CSS Variables Extracted**: `1` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Return of the Boss`
- **Body Font Stack**: `Crimson Text`
- **Monospace / Technical Font Stack**: `IBM Plex Mono`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `11px`, `10px`, `0.62em`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `11px`, `10px`, `0.62em`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `11px`, `10px`, `0.62em`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `11px`, `10px`, `0.62em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fffcf9` | `body { background: #fffcf9 }` |
| **Primary Typography Ink** | `#FFF4E7` | `.navkkwuna-mi .navkkwuna-lbl { color: #FFF4E7 }` |
| **Elevated Surface / Card Substrate** | `#E55655` | `.navkkwuna-mi .navkkwuna-arw { color: #E55655 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--crt-safe` | `31px` | Dimension / Scale Token |
| `--degacsid-com-bg` | `#fffcf9` | Canvas Substrate (from `body { background: #fffcf9 }`) |
| `--degacsid-com-ink` | `#E55655` | Primary Typography Ink (stylesheet-derived) |
| `--degacsid-com-surface` | `#E55655` | Surface Substrate (stylesheet-derived) |
| `--degacsid-com-accent` | `#E55655` | Interactive Accent (stylesheet-derived) |
| `--degacsid-com-muted` | `#E55655` | Secondary Ink (stylesheet-derived) |
| `--degacsid-com-border` | `#E55655` | Structural Border (stylesheet-derived) |
| `--degacsid-com-container` | `none` | Container Bound (stylesheet-derived) |
| `--degacsid-com-gap` | `12px` | Grid Gutter (stylesheet-derived) |
| `--degacsid-com-pad` | `10px` | Lateral Padding (stylesheet-derived) |
| `--degacsid-com-ease` | `cubic-bezier(0.5,0,0.2,1)` | Primary Easing Function |
| `--degacsid-com-radius` | `50%` | Corner Radius (stylesheet-derived) |
| `--degacsid-com-fs-base` | `11px` | Observed Font Size Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.cls-1> — `degacsid-com`)**:
   - Landmark `<header class="cls-1">` hosting `DEGACSID` navigation (`▶︎ SERVICES · ▶︎ PROCESS · ▶︎ CASE STUDIES · ▶︎ ABOUT · ▶︎ CONTACT`), DOM attributes (`data-name="Layer 1"`), and stylesheet rule `font-face { font-family:Return of the Boss;src:url(/fonts/ReturnOfTheBoss.ttf) forma... }`.
2. **Hero Stage & Focal Lead (<div.navkkwuna-mi> — `DEGACSID`)**:
   - Landmark `<div class="navkkwuna-mi">` presenting display lead `DEGACSID` and copy excerpt *"← Back to the room"* over `#fffcf9` canvas and `#E55655` ink.
3. **Primary Showcase & Content Grid (<div.navkkwuna-lbl> — `Featured Work & Interactive Showca`)**:
   - Landmark `<div class="navkkwuna-lbl">` rendering section `Featured Work & Interactive Showcase` with copy *"DEGACSID"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `main-D5gnYzr4.js`), and grid rule `root { margin:0;padding:0;width:100%;height:100% }`.
4. **Interactive Detail & Feature Matrix (<div.navkkwuna-arw> — `Technical Architecture & Narrative`)**:
   - Landmark `<div class="navkkwuna-arw">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Work & Interactive Showcase"*) with `#E55655` surface cards, `#E55655` accents, and `body { background:fffcf9;overflow:hidden;-webkit-font-smoothing:antialiased }`.
5. **Colophon & Global Directory Footer (<footer> — `https://degacsid.com/`)**:
   - Landmark `<footer>` landmark anchoring `DEGACSID` footer links (`▶︎ SERVICES · ▶︎ PROCESS · ▶︎ CASE STUDIES · ▶︎ ABOUT · ▶︎ CONTACT`), copy *"Technical Architecture & Narrative"*, and `#E55655` structural dividers.
