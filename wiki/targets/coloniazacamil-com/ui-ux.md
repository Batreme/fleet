# UI & UX Architecture: coloniazacamil-com

## Overview & Design Identity
- **Target**: `coloniazacamil-com` (**Colonia Zacamil**)
- **Production URL**: [https://coloniazacamil.com/](https://coloniazacamil.com/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#B48E46` / `#000`)
- **Summary**: Colonia Zacamil
- **Total Clean CSS Variables Extracted**: `17` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Roboto Mono`
- **Body Font Stack**: `Reckless Neue`
- **Monospace / Technical Font Stack**: `Roboto Mono`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `40px`, `14px`, `12px`, `10px`, `24px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `40px`, `14px`, `12px`, `10px`, `24px`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `40px`, `14px`, `12px`, `10px`, `24px`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `40px`, `14px`, `12px`, `10px`, `24px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#B48E46` | `var(--color)` in `:root` |
| **Primary Typography Ink** | `#ffffff` | `var(--dark-color)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff` | `:after { background: #fff }` |
| **Interactive Accent / Highlight** | `#000` | `:before { background: #000 }` |
| **Secondary / Muted Copy** | `#d9d9d9` | `:before { background: #d9d9d9 }` |
| **Structural Hairline Border** | `#af0000` | `:after { background: #af0000 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--delay` | `.2s` | Motion / Easing Token |
| `--width` | `200px` | Layout / Spatial Grid Token |
| `--translate-multiplier` | `1` | Design System Custom Token |
| `--direction` | `1` | Design System Custom Token |
| `--slide-direction` | `0` | Design System Custom Token |
| `--video-progress` | `0%` | Dimension / Scale Token |
| `--iub-granular-background` | `rgba(0, 0, 0, .02)` | Canvas / Surface Token |
| `--iub-granular-border` | `rgba(0, 0, 0, 0.08)` | Elevation / Border Token |
| `--iub-granular-toggle-background` | `rgba(0, 0, 0, 0.2)` | Canvas / Surface Token |
| `--vh` | `9.000px` | Layout / Spatial Grid Token |
| `--vw` | `14.40px` | Layout / Spatial Grid Token |
| `--vwRaw` | `14.40` | Layout / Spatial Grid Token |
| `--dvh` | `9.00px` | Layout / Spatial Grid Token |
| `--svh` | `9.00px` | Layout / Spatial Grid Token |
| `--color` | `#B48E46` | Brand / Palette Token |
| `--dark-color` | `#ffffff` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.cmplazyload> — `coloniazacamil-com`)**:
   - Landmark `<header class="cmplazyload">` hosting `Colonia Zacamil` navigation (`[powered by CMS ] · en · / es · cookie policy`), DOM attributes (`data-capo`, `data-cmp-ab="2"`, `data-cmp-info="2"`, `data-cmp-info="13"`), and stylesheet rule `first-child { transition:opacity .6s ease-in-out 0s }`.
2. **Hero Stage & Focal Lead (<section.webgl> — `Colonia Zacamil`)**:
   - Landmark `<section class="webgl">` presenting display lead `Colonia Zacamil` and copy excerpt *"A Better Childhood"* over `#B48E46` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.hidden> — `Featured Work & Interactive Showca`)**:
   - Landmark `<section class="hidden">` rendering section `Featured Work & Interactive Showcase` with copy *"[powered by CMS ] Zacamil"*, asset references (`core-en-GB.js`, `4037b39e-9661-4616-8093-abccf645c...`, `entry.t46wWHdU.css`, `_payload.json`), and grid rule `after { display:none }`.
4. **Interactive Detail & Feature Matrix (<section.pin> — `Technical Architecture & Narrative`)**:
   - Landmark `<section class="pin">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"click and drag to explore"*) with `#fff` surface cards, `#000` accents, and `hover { max-width:var(--width);z-index:1 }`.
5. **Colophon & Global Directory Footer (<footer.not-clickable> — `https://coloniazacamil.com/`)**:
   - Landmark `<footer class="not-clickable">` anchoring `Colonia Zacamil` footer links (`[powered by CMS ] · en · / es · cookie policy`), copy *"pinch to zoom in & out"*, and `#af0000` structural dividers.
