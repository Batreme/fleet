# UI & UX Architecture: www-lingers-it_en

## Overview & Design Identity
- **Target**: `www-lingers-it_en` (**Lingers – your hotel in Girlan**)
- **Production URL**: [https://www.lingers.it/en](https://www.lingers.it/en)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#777162` canvas, `#ffffff` ink, `#e0ddd7` accent)
- **Summary**: Lingers is more than a hotel in Girlan. It’s your hideaway that makes you want to stay a little longer. And we can’t wait to welcome you.
- **Total Clean CSS Variables Extracted**: `32` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Cormorant Garamond`
- **Body Font Stack**: `Cinzel`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: rule `h1` (`line-height: 1.2`, `letter-spacing: 2.1px`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 1em`, `line-height: 1`, `letter-spacing: 1.8px`)
- **Body Copy**: rule `p` (`font-size: 12px`)
- **Metadata & Labels**: rule `small` (`font-size: 80%`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#777162` | `var(--bl-color-primary)` in `:root` |
| **Primary Typography Ink** | `#ffffff` | `var(--bl-trigger-text)` in `:root` |
| **Elevated Surface / Card Substrate** | `#9f9b91` | `var(--bl-color-secondary)` in `:root` |
| **Interactive Accent / Highlight** | `#e0ddd7` | `.DNA-module__pagination__dot { background-color: #e0ddd7 }` |
| **Secondary / Muted Copy** | `#F7F7F7` | `:after { background: #F7F7F7 }` |
| **Structural Hairline Border** | `#777367` | `a { color: #777367 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--track-width` | `52px` | Layout / Spatial Grid Token |
| `--track-height` | `28px` | Layout / Spatial Grid Token |
| `--thumb-size` | `23px` | Layout / Spatial Grid Token |
| `--thumb-gap` | `3px` | Layout / Spatial Grid Token |
| `--track-radius` | `999px` | Elevation / Border Token |
| `--vh` | `9px` | Layout / Spatial Grid Token |
| `--bl-size` | `45px` | Layout / Spatial Grid Token |
| `--bl-desktop-top` | `auto` | Design System Custom Token |
| `--bl-desktop-bottom` | `1.5em` | Dimension / Scale Token |
| `--bl-desktop-left` | `auto` | Design System Custom Token |
| `--bl-desktop-right` | `1.5em` | Dimension / Scale Token |
| `--bl-desktop-box-left` | `auto` | Design System Custom Token |
| `--bl-desktop-box-right` | `1.5em` | Dimension / Scale Token |
| `--bl-tablet-top` | `auto` | Design System Custom Token |
| `--bl-tablet-bottom` | `1em` | Dimension / Scale Token |
| `--bl-tablet-left` | `auto` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.DNA-section> — `www-lingers-it_en`)**:
   - Landmark `<header class="DNA-section">` hosting `Lingers – your hotel in Girlan` navigation (`DE · IT · EN`), DOM attributes (`data-asset-id="Scss/presets"`, `data-asset-id="Scss/vendors"`, `data-asset-id="Globals/Main"`, `data-asset-id="Sections/Header"`), and stylesheet rule `.DNA-module__wrap { transition:transform 2s,opacity 2s;overflow:hidden }`.
2. **Hero Stage & Focal Lead (<section.DNA-module> — `Linger a little longer. In our cha`)**:
   - Landmark `<section class="DNA-module">` presenting display lead `Linger a little longer. In our charming hotel in...` and copy excerpt *"Lingers Morning & afternoon delights Pool & garden Massages & spo"* over `#777162` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.DNA-module> — `Culinary concept: morning & aftern`)**:
   - Landmark `<section class="DNA-module">` rendering section `Culinary concept: morning & afternoon` with copy *"Morning & afternoon delights"*, asset references (`favicon-96x96.png`, `favicon.svg`, `favicon.ico`, `apple-touch-icon.png`), and grid rule `.DNA-module__upper { padding-left:4em;padding-right:4em;max-width:calc(102.4em + 4em + 4em) }`.
4. **Interactive Detail & Feature Matrix (<section.DNA-module> — `Get active at our hotel in Girlan `)**:
   - Landmark `<section class="DNA-module">` framing `Get active at our hotel in Girlan in South Tyrol` and `Wellness at our hotel in Girlan in South Tyrol` (*"The taste of Lingers"*) with `#9f9b91` surface cards, `#e0ddd7` accents, and `.DNA-module__list { padding-left:0em;padding-right:0em;max-width:calc(102.4em + 0em + 0em) }`.
5. **Colophon & Global Directory Footer (<footer.DNA-section> — `https://www.lingers.it/en`)**:
   - Landmark `<footer class="DNA-section">` anchoring `Lingers – your hotel in Girlan` footer links (`DE · IT · EN`), copy *"Location & arrival"*, and `#777367` structural dividers.
