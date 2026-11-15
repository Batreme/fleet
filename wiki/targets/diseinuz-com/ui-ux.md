# UI & UX Architecture: diseinuz-com

## Overview & Design Identity
- **Target**: `diseinuz-com` (**DISEINUZ — Bilbao Bizkaia Design Summit**)
- **Production URL**: [https://diseinuz.com/](https://diseinuz.com/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#0000` canvas, `#000000` ink, `#830100` accent)
- **Summary**: Un encuentro para impulsar el diseño como herramienta de transformación económica, empresarial y social. 19 y 20 de noviembre de 2026 en...
- **Total Clean CSS Variables Extracted**: `40` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `UniversPro93ExtraBlackExtended`
- **Body Font Stack**: `IBM Plex Mono`
- **Monospace / Technical Font Stack**: `IBM Plex Mono`
- **Hero Display (`H1`)**: rule `.title` (`font-size: 1.5rem`, `line-height: .91667`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: max(20px,1.5rem)`, `line-height: .91667`, `letter-spacing: var(--title-letter-sp...`, `font-weight: 900`)
- **Body Copy**: rule `p` (`font-size: max(12px,.875rem)`, `line-height: 1.3334`)
- **Metadata & Labels**: CSS variables `--title-letter-spacing: -.07em`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0000` | `.hidden { color: #0000 }` |
| **Primary Typography Ink** | `#000000` | `body { background: black }` (`#000000`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `body { color: white }` (`#ffffff`) |
| **Interactive Accent / Highlight** | `#830100` | SVG/DOM `stop-color="#830100"` attribute in `dom.html` |
| **Secondary / Muted Copy** | `#FF2E01` | SVG/DOM `stop-color="#FF2E01"` attribute in `dom.html` |
| **Structural Hairline Border** | `#FFD702` | SVG/DOM `stop-color="#FFD702"` attribute in `dom.html` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--grid-gutter` | `.75rem` | Layout / Spatial Grid Token |
| `--grid-margin` | `.75rem` | Layout / Spatial Grid Token |
| `--grid-margin-negative` | `-.75rem` | Layout / Spatial Grid Token |
| `--grid-columns` | `12` | Layout / Spatial Grid Token |
| `--color-black` | `0, 0, 0` | Canvas / Surface Token |
| `--color-white` | `255, 255, 255` | Canvas / Surface Token |
| `--title-letter-spacing` | `-.07em` | Typography / Scale Token |
| `--easing-handle-01` | `cubic-bezier(.48, .1, 0, 1)` | Motion / Easing Token |
| `--easing-handle-02` | `cubic-bezier(.01, .8, .5, 1)` | Motion / Easing Token |
| `--filter-blur` | `blur(5rem)` | Elevation / Border Token |
| `--context` | `1440` | Typography Ink Token |
| `--quarter` | `3.25rem` | Dimension / Scale Token |
| `--menu-width` | `calc(var(--grid-one-column) * var(--grid-columns))` | Layout / Spatial Grid Token |
| `--modal-top` | `2rem` | Dimension / Scale Token |
| `--flashlight-x` | `50%` | Canvas / Surface Token |
| `--flashlight-y` | `50%` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `diseinuz-com`)**:
   - Landmark `<header class="header top">` hosting `DISEINUZ — Bilbao Bizkaia Design Sum` navigation (`Aviso legal · Privacidad · Cookies`), DOM attributes (`data-type="desktop"`, `data-url="/privacidad"`, `data-to="default__page"`, `data-lenis-prevent`), and stylesheet rule `root { --grid-columns:6;--context:402;--menu-width:calc(var(--grid-one-column)... }`.
2. **Hero Stage & Focal Lead (<section.home__hero> — `Configurar Cookies`)**:
   - Landmark `<section class="home__hero">` presenting display lead `Configurar Cookies` and copy excerpt *"El uso de cookies tiene como objetivo el análisis del uso de este"* over `#0000` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.home__intro> — `Ponentes`)**:
   - Landmark `<section class="home__intro">` rendering section `Ponentes` with copy *"política de privacidad"*, asset references (`favicon-96x96.png`, `favicon.svg`, `favicon.ico`, `apple-touch-icon.png`), and grid rule `html.lenis body { height:auto }`.
4. **Interactive Detail & Feature Matrix (<section.home__featured> — `19-20 nov sala multibox eitb bilba`)**:
   - Landmark `<section class="home__featured shader__section">` framing `19-20 nov sala multibox eitb bilbao` and `Contacto` (*"Estas cookies son esenciales para el correcto funcionamiento del "*) with `#ffffff` surface cards, `#830100` accents, and `.lenis.lenis-smooth { scroll-behavior:auto!important }`.
5. **Colophon & Global Directory Footer (<footer.page__footer> — `https://diseinuz.com/`)**:
   - Landmark `<footer class="page__footer">` anchoring `DISEINUZ — Bilbao Bizkaia Design` footer links (`Aviso legal · Privacidad · Cookies`), copy *"Estas cookies permiten recopilar información anónima sobre e"*, and `#FFD702` structural dividers.
