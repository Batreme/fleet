---
title: "UI & UX Architecture: www-routedurhum-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-routedurhum-com

## Overview & Design Identity
- **Target**: `www-routedurhum-com` (**Route du Rhum 2026 – Destination Guadeloupe · Site Officiel**)
- **Production URL**: [https://www.routedurhum.com/](https://www.routedurhum.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#fcf150` accent)
- **Summary**: Suivez la Route du Rhum, course légendaire entre Saint-Malo et la Guadeloupe. Skippers, actualités, villages de Saint-Malo à la Guadeloupe.
- **Total Clean CSS Variables Extracted**: `492` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Montserrat`
- **Body Font Stack**: `Varien`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 20px`, `line-height: normal`, `font-weight: 700`); CSS variables `--display: inline-block`, `--comp-display: unset`, `--container-display: grid`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 63.36px`, `line-height: 65.2608px`, `font-weight: 700`); CSS variables `--wst-font-style-h2: var(--font_2)`, `--item-depth2-direction: inherit`, `--item-depth2-align: inherit`; rule `h2` (`font-size: clamp(34px,min(4.6vw,7.4vh),7...`, `line-height: 1.1`)
- **Body Copy**: live computed `body` (`font-size: 10px`, `line-height: normal`, `font-weight: 400`); CSS variables `--wst-font-style-body-large: var(--font_7)`, `--wst-font-style-body-medium: var(--font_8)`, `--wst-font-style-body-small: var(--font_9)`; rule `p` (`font-size: 13.5px`, `font-weight: 700`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 10px`, `line-height: normal`, `font-weight: 400`); CSS variables `--wst-font-style-body-small: var(--font_9)`, `--wst-font-style-body-x-small: var(--font_10)`; rule `small` (`font-size: 8px`, `letter-spacing: .16em`, `font-weight: 700`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `browser-default` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f2f6f9` | `var(--rn-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#fcf150` | `rdr-dernieres-infos .rdi-badge-... { background: #fcf150 }` |
| **Secondary / Muted Copy** | `#7b8aa0` | `var(--ink-3)` in `:root` |
| **Structural Hairline Border** | `#e1e6ee` | `var(--line)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--one-unit` | `1vw` | Dimension / Scale Token |
| `--section-max-width` | `9999px` | Layout / Spatial Grid Token |
| `--spx-stopper-max` | `9999px` | Dimension / Scale Token |
| `--spx-stopper-min` | `0px` | Dimension / Scale Token |
| `--browser-zoom` | `1` | Design System Custom Token |
| `--wst-button-color-fill-primary` | `rgb(var(--color_48))` | Brand / Palette Token |
| `--wst-button-color-border-primary` | `rgb(var(--color_49))` | Brand / Palette Token |
| `--wst-button-color-text-primary` | `rgb(var(--color_50))` | Typography Ink Token |
| `--wst-button-color-fill-primary-hover` | `rgb(var(--color_51))` | Brand / Palette Token |
| `--wst-button-color-border-primary-hover` | `rgb(var(--color_52))` | Brand / Palette Token |
| `--wst-button-color-text-primary-hover` | `rgb(var(--color_53))` | Typography Ink Token |
| `--wst-button-color-fill-primary-disabled` | `rgb(var(--color_54))` | Brand / Palette Token |
| `--wst-button-color-border-primary-disabled` | `rgb(var(--color_55))` | Brand / Palette Token |
| `--wst-button-color-text-primary-disabled` | `rgb(var(--color_56))` | Typography Ink Token |
| `--wst-button-color-fill-secondary` | `rgb(var(--color_57))` | Brand / Palette Token |
| `--wst-button-color-border-secondary` | `rgb(var(--color_58))` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.gt> — `www-routedurhum-com`)**:
   - Landmark `<header class="gt est-pause">` (`1440px`) hosting `Route du Rhum 2026 – Destination Gua` navigation (`Cartographie Carto · Classement`), DOM attributes (`data-rdr-entete="dessus"`, `data-url="https://static.parast..."`, `data-url="https://static.parast..."`, `data-url="https://static.parast..."`), and stylesheet rule `root:active-view-transition { view-transition-name:none }`.
2. **Hero Stage & Focal Lead (<section.ke5pl1> — `Route du Rhum, Destination Guadelo`)**:
   - Landmark `<section class="ke5pl1 comp-muf996vx">` presenting display lead `Route du Rhum, Destination Guadeloupe` and copy excerpt *"ARRIVÉES EN GUADELOUPE · COMMENT LES SUIVRE EN COURSE SUIVEZ LA F"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.em> — `Saint-Malo est en fête !`)**:
   - Landmark `<section class="em">` rendering section `Saint-Malo est en fête !` with copy *"Là où les rêves prennent le large"*, asset references (`7bb303_9e59bb8f77444a2fbb905831b5...`, `bundle.tracing.es5.min.js`, `minified.js`, `focus-within-polyfill.js`), and grid rule `root::view-transition { pointer-events:none }`.
4. **Interactive Detail & Feature Matrix (<section.hero> — `Jean Le Cam, le retour du Roi`)**:
   - Landmark `<section class="hero est-photo">` framing `Jean Le Cam, le retour du Roi` and `Se souvenir des belles choses` (*"Route du Rhum Destination Guadeloupe Départ le dimanche 1 er nove"*) with `#f2f6f9` surface cards, `#fcf150` accents, and `SITE_HEADER { view-transition-name:header-group }`.
5. **Colophon & Global Directory Footer (<footer.comp-mmxzg4ms> — `https://www.routedurhum.com/`)**:
   - Landmark `<footer class="comp-mmxzg4ms S829f_">` anchoring `Route du Rhum 2026 – Destination` footer links (`Cartographie Carto · Classement`), copy *"Route du Rhum Destination Guadeloupe"*, and `#e1e6ee` structural dividers.
