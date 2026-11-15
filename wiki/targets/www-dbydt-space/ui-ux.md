# UI & UX Architecture: www-dbydt-space

## Overview & Design Identity
- **Target**: `www-dbydt-space` (**Deebak Tamilmani · Design Portfolio**)
- **Production URL**: [https://www.dbydt.space](https://www.dbydt.space)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#EEEBE4` / `#000`)
- **Summary**: Design portfolio of Deebak Tamilmani. Fragments of architecture and design projects, held as memory rather than archive, drawn in real ti...
- **Total Clean CSS Variables Extracted**: `25` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Lay Grotesk`
- **Body Font Stack**: `Geist Pixel`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `10px`, `8px`, `11px`, `16px`, `clamp(1.05rem,.24rem + 1.9vw,2rem)`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `10px`, `8px`, `11px`, `16px`, `clamp(1.05rem,.24rem + 1.9vw,2rem)`)
- **Body Copy**: rule `p` (`font-size: 10px`, `line-height: 1.4`, `font-weight: 300`)
- **Metadata & Labels**: CSS variables `--bhp-caption-row-height: 44px`, `--bhp-caption-top-padding: 16px`, `--ruler-label-top: 30px`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#EEEBE4` | `var(--project-surface)` in `:root` |
| **Primary Typography Ink** | `#2b2b2b` | `.project-content-text-legend { color: #2b2b2b }` |
| **Elevated Surface / Card Substrate** | `#6b675f` | `t-content-text p.project-conten... { color: #6b675f }` |
| **Interactive Accent / Highlight** | `#000` | `.bento-hello { background: #000 }` |
| **Secondary / Muted Copy** | `#fff` | SVG/DOM `fill="#fff"` attribute in `dom.html` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--pg-annot-mark-thickness` | `1.5px` | Dimension / Scale Token |
| `--pg-annot-bracket-size` | `8px` | Layout / Spatial Grid Token |
| `--fullscreen-ruler-reveal-inset` | `0%` | Dimension / Scale Token |
| `--project-surface` | `#EEEBE4` | Canvas / Surface Token |
| `--scene-clip-left` | `100%` | Dimension / Scale Token |
| `--bhp-caption-row-height` | `44px` | Layout / Spatial Grid Token |
| `--bhp-caption-top-padding` | `16px` | Layout / Spatial Grid Token |
| `--card-slot` | `max(300px, 25%)` | Dimension / Scale Token |
| `--ruler-height` | `30px` | Layout / Spatial Grid Token |
| `--ruler-label-top` | `30px` | Dimension / Scale Token |
| `--bento-title-size` | `clamp(5rem, min(16vw, 15vh), 8rem)` | Layout / Spatial Grid Token |
| `--stack-unit` | `40px` | Dimension / Scale Token |
| `--frame-inset` | `24px` | Dimension / Scale Token |
| `--page-height` | `900px` | Layout / Spatial Grid Token |
| `--ruler-top` | `184px` | Dimension / Scale Token |
| `--ruler-right` | `364px` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.bento-hello-scrub-scroller> — `www-dbydt-space`)**:
   - Landmark `<header class="bento-hello-scrub-scroller">` hosting `Deebak Tamilmani · Design Portfolio` navigation (`Hues of Al'Ula · A Street Within · Olakh · Atmos & Aura · Club & Courts`), DOM attributes (`data-website-id="8efd2acd-25e0-4014-bc..."`, `data-host-url="https://www.dbydt.space"`, `data-aspect="landscape"`, `data-engine="three.js r184 webgpu"`), and stylesheet rule `root { font-family:system-ui,-apple-system,Segoe UI,sans-serif;color:eeebe4;bac... }`.
2. **Hero Stage & Focal Lead (<main.lenis> — `Deebak Tamilmani · Design Portfoli`)**:
   - Landmark `<main class="lenis">` presenting display lead `Deebak Tamilmani · Design Portfolio` and copy excerpt *"Over the years, I have worked on many projects. Some were built, "* over `#EEEBE4` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<main.bento-hello-page> — `Projects`)**:
   - Landmark `<main class="bento-hello-page">` rendering section `Projects` with copy *"Hues of Al'Ula is a farm dwelling in the Cultural Oasis of Al'Ula"*, asset references (`favicon.svg`, `favicon-512.png`, `favicon-180.png`, `GeistPixel-Square.woff2`), and grid rule `.app { width:100%;height:100%;margin:0 }`.
4. **Interactive Detail & Feature Matrix (<main.bento-hello> — `Research`)**:
   - Landmark `<main class="bento-hello">` framing `Research` and `Experience and education` (*"A Street Within is an office for a real estate developer in Ahmed"*) with `#6b675f` surface cards, `#000` accents, and `html { -webkit-text-size-adjust:100%;text-size-adjust:100% }`.
5. **Colophon & Global Directory Footer (<footer.bento-hello-scene> — `https://www.dbydt.space`)**:
   - Landmark `<footer class="bento-hello-scene">` anchoring `Deebak Tamilmani · Design Portfo` footer links (`Hues of Al'Ula · A Street Within · Olakh · Atmos & Aura · Club & Courts`), copy *"Olakh , the Marathi word for identity, reimagines the Pre-Em"*, and `#000` structural dividers.
