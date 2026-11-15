# UI & UX Architecture: www-sentientx-com

## Overview & Design Identity
- **Target**: `www-sentientx-com` (**SentientX · Enterprise AI & Digital Likeness Protection**)
- **Production URL**: [https://www.sentientx.com](https://www.sentientx.com)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#757575` / `#dbfac4`)
- **Summary**: SentientX is an AI operating partner for consumer products and retail. Production-grade AI across supply chain, finance, and operations....
- **Total Clean CSS Variables Extracted**: `318` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `wf_2751996ff9224fc486a0c6fe1`
- **Body Font Stack**: `din-next-w01-light`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--display: inline-block`, `--comp-display: unset`, `--container-display: grid`
- **Section Heading (`H2`)**: CSS variables `--wst-color-subtitle: rgb(var(--color_46))`, `--wst-font-style-h2: var(--font_2)`, `--item-depth2-direction: inherit`; rule `h2` (`font-size: 16px`, `line-height: 1.05`, `font-weight: 400`)
- **Body Copy**: CSS variables `--wst-font-style-body-large: var(--font_7)`, `--wst-font-style-body-medium: var(--font_8)`, `--wst-font-style-body-small: var(--font_9)`; rule `p` (`font-size: 13px`, `line-height: 1.4`, `font-weight: 400`)
- **Metadata & Labels**: CSS variables `--wst-font-style-body-small: var(--font_9)`, `--wst-font-style-body-x-small: var(--font_10)`, `--label-align: center`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#757575` | `var(--stroke)` in `:root` |
| **Primary Typography Ink** | `#FFFFFF` | `var(--fill)` in `:root` |
| **Elevated Surface / Card Substrate** | `#5f6360` | `device-mobile-non-optimized.ful... { background-color: #5f6360 }` |
| **Interactive Accent / Highlight** | `#dbfac4` | `.sx-toggle-track:before { background: #dbfac4 }` |
| **Secondary / Muted Copy** | `#000` | `.StylableButton2545352419__link { color: #000 }` |
| **Structural Hairline Border** | `#080808` | `ol.font_100 { color: #080808 }` |

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
1. **Brand Header & Navigation Bar (<header.comp-mqurid64> — `www-sentientx-com`)**:
   - Landmark `<header class="comp-mqurid64 S829f_">` hosting `SentientX · Enterprise AI & Digital ` navigation (`Home`), DOM attributes (`data-url="https://static.parast..."`, `data-url="https://static.parast..."`, `data-url="https://static.parast..."`, `data-url="https://static.parast..."`), and stylesheet rule `root:active-view-transition { view-transition-name:none }`.
2. **Hero Stage & Focal Lead (<section.ke5pl1> — `The Autonomous Enterprise`)**:
   - Landmark `<section class="ke5pl1 comp-mqurid64_r_comp-kbgajy18">` presenting display lead `The Autonomous Enterprise` and copy excerpt *"Necessary 14 Necessary cookies help make a website usable by enab"* over `#757575` canvas and `#FFFFFF` ink.
3. **Primary Showcase & Content Grid (<section.ke5pl1> — `One intelligence, three layers`)**:
   - Landmark `<section class="ke5pl1 comp-mr0mk2kw-container">` rendering section `One intelligence, three layers` with copy *"Cookiebot 1 Learn more about this provider CookieConsent Stores t"*, asset references (`0b6ff1_2de67bd90d924a449a9260fe7d...`, `cc.js`, `minified.js`, `focus-within-polyfill.js`), and grid rule `root::view-transition { pointer-events:none }`.
4. **Interactive Detail & Feature Matrix (<section.ke5pl1> — `A new institutional layer for huma`)**:
   - Landmark `<section class="ke5pl1 comp-mrnlzewt-container">` framing `A new institutional layer for human identity.` and `Monitor, protect, control and enforce.` (*"Learn more about this provider"*) with `#5f6360` surface cards, `#dbfac4` accents, and `SITE_HEADER { view-transition-name:header-group }`.
5. **Colophon & Global Directory Footer (<footer.comp-kbgakxmn> — `https://www.sentientx.com`)**:
   - Landmark `<footer class="comp-kbgakxmn S829f_">` anchoring `SentientX · Enterprise AI & Digi` footer links (`Home`), copy *"Stores the user's cookie consent state for the current domai"*, and `#080808` structural dividers.
