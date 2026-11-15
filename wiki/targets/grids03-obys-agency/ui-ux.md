# UI & UX Architecture: grids03-obys-agency

## Overview & Design Identity
- **Target**: `grids03-obys-agency` (**Grids — DES Season 03**)
- **Production URL**: [https://grids03.obys.agency/](https://grids03.obys.agency/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#e1e1e1`)
- **Summary**: Grids is an interactive project exploring grids, composition, and key design principles through visual experiments. First launched in 202...
- **Total Clean CSS Variables Extracted**: `20` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Obys Sans`
- **Body Font Stack**: `Helvetica Neue`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--small-size)`, `var(--caption-size)`, `var(--size)`, `var(--about-size)`, `12px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--small-size)`, `var(--caption-size)`, `var(--size)`, `var(--about-size)`, `12px`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--small-size)`, `var(--caption-size)`, `var(--size)`, `var(--about-size)`, `12px`)
- **Metadata & Labels**: CSS variables `--caption-size: 90px`, `--small-size: 12px`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--color-bg)` in `:root` |
| **Primary Typography Ink** | `#000` | `var(--color-ink)` in `:root` |
| **Elevated Surface / Card Substrate** | `#dedfd9` | `var(--color-ground)` in `:root` |
| **Interactive Accent / Highlight** | `#e1e1e1` | `var(--color-rule)` in `:root` |
| **Secondary / Muted Copy** | `#d9d9d9` | `.grid-entry__picture { background: #d9d9d9 }` |
| **Structural Hairline Border** | `#b2b2b2` | `.about__line--quiet i { color: #b2b2b2 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-bg` | `#fff` | Canvas / Surface Token |
| `--color-ink` | `#000` | Typography Ink Token |
| `--color-ground` | `#dedfd9` | Brand / Palette Token |
| `--color-rule` | `#e1e1e1` | Brand / Palette Token |
| `--layer-gl` | `0` | Design System Custom Token |
| `--layer-content` | `2` | Design System Custom Token |
| `--layer-header` | `3` | Layout / Spatial Grid Token |
| `--layer-preloader` | `50` | Design System Custom Token |
| `--grid-columns` | `12` | Layout / Spatial Grid Token |
| `--grid-margin` | `20` | Layout / Spatial Grid Token |
| `--grid-gutter` | `20` | Layout / Spatial Grid Token |
| `--vw` | `1440px` | Layout / Spatial Grid Token |
| `--vh` | `900px` | Layout / Spatial Grid Token |
| `--caption-size` | `90px` | Layout / Spatial Grid Token |
| `--small-size` | `12px` | Layout / Spatial Grid Token |
| `--edge` | `18px` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.lenis> — `grids03-obys-agency`)**:
   - Landmark `<header class="lenis">` hosting `Grids — DES Season 03` navigation (`Grids · More About Season · Enroll Now · Learn for Free · Obys`), DOM attributes (`data-preloader`, `data-ground`, `data-bar`, `data-letter="G"`), and stylesheet rule `body { overflow-x:hidden }`.
2. **Hero Stage & Focal Lead (<section.intro> — `G r i d s S 0 3`)**:
   - Landmark `<section class="intro">` presenting display lead `G r i d s S 0 3` and copy excerpt *"Design Education Series® Obys"* over `#fff` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.grid-block> — `4 - C o l u m n`)**:
   - Landmark `<section class="grid-block">` rendering section `4 - C o l u m n` with copy *"Grids — DES Season 03. 17 lectures."*, asset references (`favicon.svg`, `favicon-32.png`, `favicon-180.png`, `ObysSans-Regular.woff2`), and grid rule `.stage { width:100%;height:100%;z-index:var(--layer-gl);pointer-events:none;posit... }`.
4. **Interactive Detail & Feature Matrix (<section.story> — `G r i d`)**:
   - Landmark `<section class="story">` framing `G r i d` and `1 0 p x` (*"4+ hours on grids and composition."*) with `#dedfd9` surface cards, `#e1e1e1` accents, and `.preloader { z-index:var(--layer-preloader);pointer-events:none;position:fixed;inset:... }`.
5. **Colophon & Global Directory Footer (<footer.preloader> — `https://grids03.obys.agency/`)**:
   - Landmark `<footer class="preloader">` anchoring `Grids — DES Season 03` footer links (`Grids · More About Season · Enroll Now · Learn for Free · Obys`), copy *"About Grids, Season"*, and `#b2b2b2` structural dividers.
