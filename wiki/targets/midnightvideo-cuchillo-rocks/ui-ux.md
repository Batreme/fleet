# UI & UX Architecture: midnightvideo-cuchillo-rocks

## Overview & Design Identity
- **Target**: `midnightvideo-cuchillo-rocks` (**Cuchillo Midnight Video**)
- **Production URL**: [https://midnightvideo.cuchillo.rocks/](https://midnightvideo.cuchillo.rocks/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#fff`)
- **Summary**: An endless VHS store at midnight, lost somewhere between nostalgia and the uncanny. A liminal experiment by Cuchillo.
- **Total Clean CSS Variables Extracted**: `6` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `VT323`
- **Body Font Stack**: `IBM Plex Serif`
- **Monospace / Technical Font Stack**: `IBM Plex Serif`
- **Hero Display (`H1`)**: rule `.title` (`font-size: max(19px, 1.85vw)`, `letter-spacing: -.04em`, `font-weight: 400`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--osd-size)`, `1.3em`, `1.2em`, `.62em`, `1.84em`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--osd-size)`, `1.3em`, `1.2em`, `.62em`, `1.84em`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--osd-size)`, `1.3em`, `1.2em`, `.62em`, `1.84em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `body { background: #000 }` |
| **Primary Typography Ink** | `#0b0c12` | `#loader { background: #0b0c12 }` |
| **Elevated Surface / Card Substrate** | `#d9def3` | `#loader .ld-text { color: #d9def3 }` |
| **Interactive Accent / Highlight** | `#fff` | `#loader .ld-bar i { background: #fff }` |
| **Secondary / Muted Copy** | `#fff0` | `#loader .ld-bar:after { background: #fff0 }` |
| **Structural Hairline Border** | `#f3f6ff` | `.ev-t { color: #f3f6ff }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--osd-size` | `max(20px, 2.3vw)` | Layout / Spatial Grid Token |
| `--vh` | `1vh` | Layout / Spatial Grid Token |
| `--legend-bottom` | `13.5%` | Dimension / Scale Token |
| `--opt-r` | `1px` | Dimension / Scale Token |
| `--logo-foot` | `64.875%` | Dimension / Scale Token |
| `--logo-cm` | `0.8033%` | Dimension / Scale Token |
| `--midnightvideo-cu-bg` | `#000` | Canvas Substrate (from `body { background: #000 }`) |
| `--midnightvideo-cu-ink` | `#fff` | Primary Typography Ink (stylesheet-derived) |
| `--midnightvideo-cu-surface` | `#d9def3` | Surface Substrate (stylesheet-derived) |
| `--midnightvideo-cu-accent` | `#fff` | Interactive Accent (stylesheet-derived) |
| `--midnightvideo-cu-muted` | `#fff0` | Secondary Ink (stylesheet-derived) |
| `--midnightvideo-cu-border` | `#f3f6ff` | Structural Border (stylesheet-derived) |
| `--midnightvideo-cu-container` | `60vw` | Container Bound (stylesheet-derived) |
| `--midnightvideo-cu-gap` | `0px` | Grid Gutter (stylesheet-derived) |
| `--midnightvideo-cu-pad` | `2px` | Lateral Padding (stylesheet-derived) |
| `--midnightvideo-cu-ease` | `cubic-bezier(.16,1,.3,1)` | Primary Easing Function |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.ev-lens> — `midnightvideo-cuchillo-rocks`)**:
   - Landmark `<header class="ev-lens">` hosting `Cuchillo Midnight Video` navigation (`INFORMATION`), DOM attributes (`data-website-id="53cd27c8-8f3a-4115-bc..."`, `data-engine="three.js r186"`, `data-opt="clean"`, `data-opt="halloween"`), and stylesheet rule `app { position:fixed;inset:0 }`.
2. **Hero Stage & Focal Lead (<div.ev-ui> — `Cuchillo Midnight Video`)**:
   - Landmark `<div class="ev-ui">` presenting display lead `Cuchillo Midnight Video` and copy excerpt *"CLICK / E PUT BACK"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<div.osd-pic> — `CLICK / E PUT BACK`)**:
   - Landmark `<div class="osd-pic">` rendering section `CLICK / E PUT BACK` with copy *"OPEN 24 HOURS. ALWAYS."*, asset references (`favicon-96x96.png`, `favicon.svg`, `favicon.ico`, `apple-touch-icon.png`), and grid rule `app canvas { width:100%;height:100%;display:block }`.
4. **Interactive Detail & Feature Matrix (<div.ev-hud> — `OPEN 24 HOURS. ALWAYS.`)**:
   - Landmark `<div class="ev-hud">` framing `OPEN 24 HOURS. ALWAYS.` and `A liminal experiment by` (*"A liminal experiment by"*) with `#d9def3` surface cards, `#fff` accents, and `ui { pointer-events:none;position:fixed;inset:0 }`.
5. **Colophon & Global Directory Footer (<footer.ev-osd> — `https://midnightvideo.cuchillo.rocks/`)**:
   - Landmark `<footer class="ev-osd">` anchoring `Cuchillo Midnight Video` footer links (`INFORMATION`), copy *"Legal notice, credits and privacy policy: open as a text pag"*, and `#f3f6ff` structural dividers.
