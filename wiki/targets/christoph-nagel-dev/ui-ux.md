# UI & UX Architecture: christoph-nagel-dev

## Overview & Design Identity
- **Target**: `christoph-nagel-dev` (**Christoph Nagel · Webentwickler, Fotograf & Videograf in Dorsten**)
- **Production URL**: [https://christoph-nagel.dev/](https://christoph-nagel.dev/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#080808` / `#fff`)
- **Summary**: Christoph Nagel aus Dorsten: Webentwicklung mit WordPress, HTML, CSS und JavaScript. Einblicke in eigene Projekte, Fotografie und Videogr...
- **Total Clean CSS Variables Extracted**: `19` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Anton`
- **Body Font Stack**: `Manrope`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `.hero-title` (`font-size: clamp(4rem, 13vw, 12.8rem)`, `line-height: 0.84`, `letter-spacing: -0.005em`, `font-weight: 400`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(2.25rem, 4.25vw, 4.7rem)`, `line-height: 1.15`, `letter-spacing: -0.018em`, `font-weight: 400`)
- **Body Copy**: rule `p` (`font-size: clamp(0.9rem, 1vw, 1rem)`, `line-height: 1.68`)
- **Metadata & Labels**: CSS variables `--label-width: 150px`, `--label-top: 52%`, `--label-z-index: 40`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#080808` | `var(--bg)` in `:root` |
| **Primary Typography Ink** | `#f4f4f1` | `var(--text)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ff4b3e` | `var(--red)` in `:root` |
| **Interactive Accent / Highlight** | `#fff` | `.skip-link { background: #fff }` |
| **Secondary / Muted Copy** | `#000` | `.skip-link { color: #000 }` |
| **Structural Hairline Border** | `#0a0a0a` | `.site-shell { background: #0a0a0a }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#080808` | Canvas / Surface Token |
| `--text` | `#f4f4f1` | Typography Ink Token |
| `--muted` | `rgba(244, 244, 241, 0.68)` | Color / Atmospheric Token |
| `--line` | `rgba(255, 255, 255, 0.18)` | Color / Atmospheric Token |
| `--glass` | `rgba(12, 12, 12, 0.38)` | Color / Atmospheric Token |
| `--red` | `#ff4b3e` | Color / Atmospheric Token |
| `--safe-top` | `max(1.25rem, env(safe-area-inset-top))` | Dimension / Scale Token |
| `--safe-right` | `max(1.25rem, env(safe-area-inset-right))` | Dimension / Scale Token |
| `--safe-bottom` | `max(1.25rem, env(safe-area-inset-bottom))` | Dimension / Scale Token |
| `--safe-left` | `max(1.25rem, env(safe-area-inset-left))` | Dimension / Scale Token |
| `--cursor-x` | `-120px` | Dimension / Scale Token |
| `--cursor-y` | `-120px` | Dimension / Scale Token |
| `--cursor-size` | `3.75rem` | Layout / Spatial Grid Token |
| `--label-width` | `150px` | Layout / Spatial Grid Token |
| `--label-top` | `52%` | Dimension / Scale Token |
| `--label-z-index` | `40` | Elevation / Border Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.topbar> — `christoph-nagel-dev`)**:
   - Landmark `<header class="topbar">` hosting `Christoph Nagel · Webentwickler, Fot` navigation (`Kontakt`), DOM attributes (`data-inline-css="/styles.css?v=8b9c708..."`, `data-inline-css="/assets/css/seo-check..."`, `data-inline-css="/assets/css/wind-labe..."`, `data-inline-css="/assets/css/site-enha..."`), and stylesheet rule `html { background: 080808; }`.
2. **Hero Stage & Focal Lead (<section.panel> — `Christoph Nagel Webentwickler, Fot`)**:
   - Landmark `<section class="panel panel--intro">` presenting display lead `Christoph Nagel Webentwickler, Fotograf und Video...` and copy excerpt *"Der Mensch dahinter"* over `#080808` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.panel> — `Code. Kamera. Klartext.`)**:
   - Landmark `<section class="panel panel--content">` rendering section `Code. Kamera. Klartext.` with copy *"SEO & GEO Schnelltest"*, asset references (`favicon.svg`, `site.webmanifest`, `intro.jpg`, `anton-v27-latin-regular.woff2`), and grid rule `body { background: 080808; }`.
4. **Interactive Detail & Feature Matrix (<section.panel> — `Digitale Lösungen mit Substanz`)**:
   - Landmark `<section class="panel panel--content">` framing `Digitale Lösungen mit Substanz` and `Ein klarer Blick für den richtigen Moment` (*"Webentwickler, Fotograf und Videograf aus Dorsten im Ruhrgebiet"*) with `#ff4b3e` surface cards, `#fff` accents, and `button { font: inherit; }`.
5. **Colophon & Global Directory Footer (<footer.legal-links> — `https://christoph-nagel.dev/`)**:
   - Landmark `<footer class="legal-links">` anchoring `Christoph Nagel · Webentwickler,` footer links (`Kontakt`), copy *"Code. Kamera. Klartext."*, and `#0a0a0a` structural dividers.
