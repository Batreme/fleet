# UI & UX Architecture: herasymenkox-com

## Overview & Design Identity
- **Target**: `herasymenkox-com` (**Yehor Herasymenko — Digital Designer**)
- **Production URL**: [https://herasymenkox.com/](https://herasymenkox.com/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#cee49f` / `#008000`)
- **Summary**: Z I R K A I N T E R C E P T O R
- **Total Clean CSS Variables Extracted**: `16` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `PP Neue Montreal`
- **Body Font Stack**: `PP Neue Montreal Mono`
- **Monospace / Technical Font Stack**: `PP Neue Montreal Mono`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--fs)`, `10px`, `6px`)
- **Section Heading (`H2`)**: rule `h2` (`font-weight: inherit`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--fs)`, `10px`, `6px`)
- **Metadata & Labels**: CSS variables `--cap-mono: 0.143em`; rule `.mono` (`font-size: calc(10 * var(--px))`, `line-height: 1`, `font-weight: 500`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#cee49f` | `var(--green)` in `:root` |
| **Primary Typography Ink** | `#0b0b0b` | `var(--black)` in `:root` |
| **Elevated Surface / Card Substrate** | `#000000` | `body { background: black }` (`#000000`) |
| **Interactive Accent / Highlight** | `#008000` | `body { color: green }` (`#008000`) |
| **Secondary / Muted Copy** | `#fff` | SVG/DOM `fill="#fff"` attribute in `dom.html` |
| **Structural Hairline Border** | `#000` | SVG/DOM `fill="#000"` attribute in `dom.html` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--design-width` | `1440` | Layout / Spatial Grid Token |
| `--container` | `clamp(1440px, 100vw, 2560px)` | Layout / Spatial Grid Token |
| `--px` | `calc(var(--container) / var(--design-width))` | Design System Custom Token |
| `--green` | `#cee49f` | Color / Atmospheric Token |
| `--black` | `#0b0b0b` | Canvas / Surface Token |
| `--green-12` | `rgba(206, 228, 159, 0.12)` | Color / Atmospheric Token |
| `--cap-bold` | `0.0215em` | Dimension / Scale Token |
| `--cap-mono` | `0.143em` | Typography / Scale Token |
| `--cap-height` | `0.715em` | Layout / Spatial Grid Token |
| `--fs` | `calc((100vw - 32 * var(--px)) / 6.6006)` | Dimension / Scale Token |
| `--y-w` | `600` | Design System Custom Token |
| `--y-h` | `580` | Design System Custom Token |
| `--cap` | `0.0915em` | Dimension / Scale Token |
| `--ext` | `calc(5.5 * var(--px) - 0.0635em)` | Dimension / Scale Token |
| `--left` | `0` | Design System Custom Token |
| `--width` | `12` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.blend> — `herasymenkox-com`)**:
   - Landmark `<nav class="blend menu">` hosting `Yehor Herasymenko — Digital Designer` navigation (`Work (05) WORK (05) · Profile PROFILE · Connect CONNECT`), DOM attributes (`data-orbit`, `data-engine="three.js r171"`, `data-gl`, `data-ui`), and stylesheet rule `after { box-sizing: border-box; }`.
2. **Hero Stage & Focal Lead (<div.gl> — `Z I R K A I N T E R C E P T O R`)**:
   - Landmark `<div class="gl">` presenting display lead `Z I R K A I N T E R C E P T O R` and copy excerpt *"Work (05) WORK (05) Profile PROFILE Connect CONNECT"* over `#cee49f` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<div.blend> — `E V O Q U E`)**:
   - Landmark `<div class="blend">` rendering section `E V O Q U E` with copy *"Work (05) WORK (05)"*, asset references (`favicon.svg`, `PPNeueMontreal-Bold.woff2`, `PPNeueMontrealMono-Medium.woff2`, `FHPhemister-Light.woff2`), and grid rule `body { margin: 0; height: 100%; overflow: hidden; background: var(--black); }`.
4. **Interactive Detail & Feature Matrix (<div.h3> — `D A R K N O D E`)**:
   - Landmark `<div class="h3">` framing `D A R K N O D E` and `F I T O S A U N A` (*"I N T E R C E P T O R"*) with `#000000` surface cards, `#008000` accents, and `h2 { margin: 0; font-weight: inherit; }`.
5. **Colophon & Global Directory Footer (<footer.corner> — `https://herasymenkox.com/`)**:
   - Landmark `<footer class="corner">` anchoring `Yehor Herasymenko — Digital Desi` footer links (`Work (05) WORK (05) · Profile PROFILE · Connect CONNECT`), copy *"Real Estate / 2025"*, and `#000` structural dividers.
