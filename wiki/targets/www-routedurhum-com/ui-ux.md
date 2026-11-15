# UI & UX Architecture: www-routedurhum-com

## Overview & Design Identity
- **Target**: `www-routedurhum-com` (**Route du Rhum 2026 – Destination Guadeloupe · Site Officiel**)
- **Production URL**: [https://www.routedurhum.com/](https://www.routedurhum.com/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#0E111D` ink, `#006F7B` accent)
- **Summary**: Suivez la Route du Rhum, course légendaire entre Saint-Malo et la Guadeloupe. Skippers, actualités, villages de Saint-Malo à la Guadeloupe.
- **Total Clean CSS Variables Extracted**: `491` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Varien`
- **Body Font Stack**: `wf_1e5b9ef92f5440db968e5ef2f`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--display: inline-block`, `--comp-display: unset`, `--container-display: grid`
- **Section Heading (`H2`)**: CSS variables `--wst-color-subtitle: rgb(var(--color_46))`, `--wst-font-style-h2: var(--font_2)`, `--item-depth2-direction: inherit`; rule `h2` (`font-size: clamp(34px,min(4.6vw,7.4vh),7...`, `line-height: 1.1`)
- **Body Copy**: CSS variables `--wst-font-style-body-large: var(--font_7)`, `--wst-font-style-body-medium: var(--font_8)`, `--wst-font-style-body-small: var(--font_9)`; rule `p` (`font-size: 13px`, `line-height: 1.5`)
- **Metadata & Labels**: CSS variables `--wst-font-style-body-small: var(--font_9)`, `--wst-font-style-body-x-small: var(--font_10)`; rule `small` (`letter-spacing: 0`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--sqb)` in `:root` |
| **Primary Typography Ink** | `#0A1228` | `var(--sqf)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ED1566` | `var(--stroke)` in `:root` |
| **Interactive Accent / Highlight** | `#006F7B` | `var(--fill)` in `:root` |
| **Secondary / Muted Copy** | `#0E111D` | `var(--marine)` in `:root` |
| **Structural Hairline Border** | `#16355D` | `var(--marine2)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--scrollbar-width` | `0px` | Layout / Spatial Grid Token |
| `--one-unit` | `1vw` | Dimension / Scale Token |
| `--section-max-width` | `9999px` | Layout / Spatial Grid Token |
| `--spx-stopper-max` | `9999px` | Dimension / Scale Token |
| `--spx-stopper-min` | `0px` | Dimension / Scale Token |
| `--browser-zoom` | `1` | Design System Custom Token |
| `--safari-sticky-fix` | `opacity` | Design System Custom Token |
| `--experimental-safari-sticky-fix` | `translateZ(0)` | Design System Custom Token |
| `--wst-button-color-fill-primary` | `rgb(var(--color_48))` | Brand / Palette Token |
| `--wst-button-color-border-primary` | `rgb(var(--color_49))` | Brand / Palette Token |
| `--wst-button-color-text-primary` | `rgb(var(--color_50))` | Typography Ink Token |
| `--wst-button-color-fill-primary-hover` | `rgb(var(--color_51))` | Brand / Palette Token |
| `--wst-button-color-border-primary-hover` | `rgb(var(--color_52))` | Brand / Palette Token |
| `--wst-button-color-text-primary-hover` | `rgb(var(--color_53))` | Typography Ink Token |
| `--wst-button-color-fill-primary-disabled` | `rgb(var(--color_54))` | Brand / Palette Token |
| `--wst-button-color-border-primary-disabled` | `rgb(var(--color_55))` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.gt> — `www-routedurhum-com`)**:
   - Landmark `<header class="gt est-pause">` hosting `Route du Rhum 2026 – Destination Gua` navigation (`Cartographie Carto · Classement`), DOM attributes (`data-rdr-entete="dessus"`, `data-url="https://static.parast..."`, `data-url="https://static.parast..."`, `data-url="https://static.parast..."`), and stylesheet rule `root:active-view-transition { view-transition-name:none }`.
2. **Hero Stage & Focal Lead (<section.Lnr3dj> — `Route du Rhum, Destination Guadelo`)**:
   - Landmark `<section class="Lnr3dj comp-muf9fz41_r_comp-mucghtyv">` presenting display lead `Route du Rhum, Destination Guadeloupe` and copy excerpt *"Boutique officielle (nouvel onglet)"* over `#fff` canvas and `#0E111D` ink.
3. **Primary Showcase & Content Grid (<section.ke5pl1> — `Saint-Malo est en fête !`)**:
   - Landmark `<section class="ke5pl1 comp-muf996vx">` rendering section `Saint-Malo est en fête !` with copy *"Boutique officielle"*, asset references (`7bb303_9e59bb8f77444a2fbb905831b5...`, `bundle.tracing.es5.min.js`, `minified.js`, `focus-within-polyfill.js`), and grid rule `root::view-transition { pointer-events:none }`.
4. **Interactive Detail & Feature Matrix (<section.em> — `Achille Nebout : « c’est rageant m`)**:
   - Landmark `<section class="em">` framing `Achille Nebout : « c’est rageant mais c’est le je...` and `Chasseurs, chassés, qui aura le dernier mot ?` (*"Jeu officiel (nouvel onglet)"*) with `#ED1566` surface cards, `#006F7B` accents, and `SITE_HEADER { view-transition-name:header-group }`.
5. **Colophon & Global Directory Footer (<footer.comp-mmxzg4ms> — `https://www.routedurhum.com/`)**:
   - Landmark `<footer class="comp-mmxzg4ms S829f_">` anchoring `Route du Rhum 2026 – Destination` footer links (`Cartographie Carto · Classement`), copy *"En course depuis J+13 05 : 14 : 38"*, and `#16355D` structural dividers.
