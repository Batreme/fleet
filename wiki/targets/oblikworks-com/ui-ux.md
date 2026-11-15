# UI & UX Architecture: oblikworks-com

## Overview & Design Identity
- **Target**: `oblikworks-com` (**oblikworks · Architectural Visualization & 3D Rendering Studio**)
- **Production URL**: [https://oblikworks.com/](https://oblikworks.com/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#eee` canvas, `#000` ink, `#000` accent)
- **Summary**: oblikworks is an architectural visualization studio creating photorealistic 3D renderings, architectural imagery, and visual storytelling...
- **Total Clean CSS Variables Extracted**: `5` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Antique Legacy`
- **Body Font Stack**: `Suisseintl`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: rule `small` (`font-size: 80%`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#eee` | `var(--_colors---line-color)` in `:root` |
| **Primary Typography Ink** | `#f0f0f0` | `var(--_colors---button-grey)` in `:root` |
| **Elevated Surface / Card Substrate** | `#0000` | `a { background-color: #0000 }` |
| **Interactive Accent / Highlight** | `#000` | `mark { color: #000 }` |
| **Secondary / Muted Copy** | `#ff0` | `mark { background: #ff0 }` |
| **Structural Hairline Border** | `#333` | `body { color: #333 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--_font-sizes---p16` | `clamp(14px, 1vw, 16px)` | Typography / Scale Token |
| `--_colors---line-color` | `#eee` | Brand / Palette Token |
| `--_colors---button-grey` | `#f0f0f0` | Brand / Palette Token |
| `--cases-width` | `calc(220vw + 25px)` | Layout / Spatial Grid Token |
| `--oblikworks-com-bg` | `#eee` | Canvas Substrate (from `var(--_colors---line-color)` in `:root`) |
| `--oblikworks-com-ink` | `#000` | Primary Typography Ink (stylesheet-derived) |
| `--oblikworks-com-surface` | `#0000` | Surface Substrate (stylesheet-derived) |
| `--oblikworks-com-accent` | `#000` | Interactive Accent (stylesheet-derived) |
| `--oblikworks-com-muted` | `#ff0` | Secondary Ink (stylesheet-derived) |
| `--oblikworks-com-border` | `#333` | Structural Border (stylesheet-derived) |
| `--oblikworks-com-container` | `940px` | Container Bound (stylesheet-derived) |
| `--oblikworks-com-gap` | `16px` | Grid Gutter (stylesheet-derived) |
| `--oblikworks-com-pad` | `9px` | Lateral Padding (stylesheet-derived) |
| `--oblikworks-com-ease` | `cubic-bezier(.625,.05,0,1)` | Primary Easing Function |
| `--oblikworks-com-radius` | `3px` | Corner Radius (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.w-mod-js> — `oblikworks-com`)**:
   - Landmark `<header class="w-mod-js">` hosting `oblikworks · Architectural Visualiza` navigation (`Studio · Projects · News 3 · Contact · Archive`), DOM attributes (`data-wf-domain="oblikworks.com"`, `data-wf-page="69c2caad0ee663f0795cd0bb"`, `data-wf-site="69c2caab0ee663f0795ccce3"`, `data-wf-ignore`), and stylesheet rule `html.lenis body { height:auto }`.
2. **Hero Stage & Focal Lead (<div.preloader> — `Oblik is an Architectural 3D Visua`)**:
   - Landmark `<div class="preloader">` presenting display lead `Oblik is an Architectural 3D Visualization Studio...` and copy excerpt *"info@oblikworks.com"* over `#eee` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<div.preloader> — `More information`)**:
   - Landmark `<div class="preloader">` rendering section `More information` with copy *"August 8, 2026 New work: Faculty of Philology is now published on"*, asset references (`cdn.prod.website-files.com`, `oblik-studio.webflow.shared.30697...`, `1135743295497216`, `fbevents.js`), and grid rule `.lenis.lenis-stopped { overflow:clip }`.
4. **Interactive Detail & Feature Matrix (<div.preloader> — `Let’s start a conversation about y`)**:
   - Landmark `<div class="preloader">` framing `Let’s start a conversation about your project.` and `Contact us` (*"New work: Faculty of Philology is now published on our website."*) with `#0000` surface cards, `#000` accents, and `.lenis.lenis-smooth iframe { pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.body> — `https://oblikworks.com/`)**:
   - Landmark `<footer class="body">` anchoring `oblikworks · Architectural Visua` footer links (`Studio · Projects · News 3 · Contact · Archive`), copy *"June 24, 2026 In the Press: Our Visualizations of The Alfred"*, and `#333` structural dividers.
