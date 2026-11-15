# UI & UX Architecture: errormade-tech

## Overview & Design Identity
- **Target**: `errormade-tech` (**Entrance — Errormade**)
- **Production URL**: [https://errormade.tech/](https://errormade.tech/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#fff`)
- **Summary**: Selected graphic design and art direction by Errormade.
- **Total Clean CSS Variables Extracted**: `82` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `end`
- **Body Font Stack**: `Times New Roman`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`letter-spacing: inherit`)
- **Section Heading (`H2`)**: rule `h2` (`letter-spacing: -.48px`)
- **Body Copy**: rule `p` (`font-size: 11px`, `line-height: 1.5`)
- **Metadata & Labels**: CSS variables `--object-caption-height: 36.5px`, `--object-caption-bottom: calc(var(--mobile-footer-bottom) + 25px)`; rule `small` (`font-size: 9px`, `line-height: 1.4`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--viewport-background)` in `:root` |
| **Primary Typography Ink** | `#d8d8d8` | `var(--tools-line)` in `:root` |
| **Elevated Surface / Card Substrate** | `#747474` | `var(--tools-muted)` in `:root` |
| **Interactive Accent / Highlight** | `#fff` | `var(--ink)` in `:root` |
| **Secondary / Muted Copy** | `#1a1a1a` | `var(--media-hover-outline)` in `:root` |
| **Structural Hairline Border** | `#eeeeed` | `.about-tools-launcher { color: #eeeeed }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--grid-gap` | `6px` | Layout / Spatial Grid Token |
| `--column` | `calc((100vw - 2 * var(--page-margin) - 5 * var(--grid-gap)) / 6)` | Layout / Spatial Grid Token |
| `--about-overview-top` | `calc(var(--site-header-bottom) + 12px)` | Dimension / Scale Token |
| `--book-spread-columns` | `10` | Layout / Spatial Grid Token |
| `--book-tick-active` | `1` | Design System Custom Token |
| `--case-ruler-top` | `calc(115px + var(--safe-top))` | Dimension / Scale Token |
| `--case-end-gap` | `200px` | Layout / Spatial Grid Token |
| `--case-step-height` | `200px` | Layout / Spatial Grid Token |
| `--case-header-width` | `calc((100vw - 2 * var(--page-margin) - 2 * var(--grid-gap)) / 3)` | Layout / Spatial Grid Token |
| `--case-progress-ease` | `cubic-bezier(.22, 1, .36, 1)` | Motion / Easing Token |
| `--case-divider-color` | `rgb(255 255 255 / 15%)` | Brand / Palette Token |
| `--case-preview-width` | `48px` | Layout / Spatial Grid Token |
| `--case-preview-duration` | `450ms` | Motion / Easing Token |
| `--case-preview-hidden` | `inset(100% 0 0 0)` | Dimension / Scale Token |
| `--case-ruler-weight` | `2` | Design System Custom Token |
| `--case-step-duration` | `420ms` | Motion / Easing Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `errormade-tech`)**:
   - Landmark `<header class="site-header header-motion-ready">` hosting `Entrance — Errormade` navigation (`Entrance · Work · Errormade · About · .obj`), DOM attributes (`data-read-only-preview`, `data-static-export="959f9f266ae66e5a"`, `data-theme="light"`, `data-mobile-glass="webgl"`), and stylesheet rule `.about-tools-launcher { font: 12px/1.4 Arial, Helvetica, sans-serif; color: eeeeed; box-sizing:... }`.
2. **Hero Stage & Focal Lead (<section.home-intro> — `Entrance — Errormade`)**:
   - Landmark `<section class="home-intro">` presenting display lead `Entrance — Errormade` and copy excerpt *"Visual, Art direction, Motion Design"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<article.project> — `Bushido Zho S&T`)**:
   - Landmark `<article class="project has-custom-layout">` rendering section `Bushido Zho S&T` with copy *"Digital, Art direction"*, asset references (`favicon.svg`, `5by7-bold.ttf`, `lenis.css`, `styles.css`), and grid rule `after { box-sizing: border-box; }`.
4. **Interactive Detail & Feature Matrix (<article.project> — `Krakatau`)**:
   - Landmark `<article class="project has-custom-layout">` framing `Krakatau` and `Memoria` (*"Visual, Art direction, Merchandise Design, Graphic Design, AI Cam"*) with `#747474` surface cards, `#fff` accents, and `.about-tools-drag { display: flex; align-items: center; gap: 10px; cursor: grab; touch-actio... }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://errormade.tech/`)**:
   - Landmark `<footer class="site-footer">` anchoring `Entrance — Errormade` footer links (`Entrance · Work · Errormade · About · .obj`), copy *"Visual, Art direction"*, and `#eeeeed` structural dividers.
