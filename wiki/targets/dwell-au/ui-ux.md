# UI & UX Architecture: dwell-au

## Overview & Design Identity
- **Target**: `dwell-au` (**Dwell · A new way home**)
- **Production URL**: [https://dwell.au/](https://dwell.au/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#3e3e38` / `#badcf7`)
- **Summary**: Dwell is a third housing option that lets you have a home and build wealth without a deposit or mortgage. Discover a new way home.
- **Total Clean CSS Variables Extracted**: `201` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `bo`
- **Body Font Stack**: `fr`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--n-font)`, `clamp(16*max(1px,min(.0661376vw,....`, `14vw`, `clamp(30*max(1px,min(.0661376vw,....`, `clamp(28px,5svh,34*max(1px,min(.0...`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: calc(34*max(1px,min(.0661376v...`, `line-height: 1.02`)
- **Body Copy**: CSS variables `--font-weight-body: 359`, `--font-width-body: 95%`; rule `p` (`line-height: 1.05`)
- **Metadata & Labels**: CSS variables `--field-label: var(--color-moss)`, `--step-label-top: 12%`, `--font-mono: "fr",monospace`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#3e3e38` | `var(--g-native-base)` in `:root` |
| **Primary Typography Ink** | `#87b6d9` | `var(--field-selector-hover)` in `:root` |
| **Elevated Surface / Card Substrate** | `#aad1ee` | `var(--color-sky)` in `:root` |
| **Interactive Accent / Highlight** | `#badcf7` | `var(--color-dawn)` in `:root` |
| **Secondary / Muted Copy** | `#c4dcee` | `var(--color-mist)` in `:root` |
| **Structural Hairline Border** | `#d1e5f4` | `var(--color-cloud)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--header-height` | `calc(108*max(1px,min(.0661376vw,.124069svh)))` | Layout / Spatial Grid Token |
| `--viewport-height` | `100vh` | Layout / Spatial Grid Token |
| `--v-fade` | `opacity .6s var(--io2)` | Design System Custom Token |
| `--n-toggle` | `2.91667vw` | Dimension / Scale Token |
| `--n-gap` | `3.75vw` | Layout / Spatial Grid Token |
| `--menu-offset` | `calc(var(--n-toggle)*-3.8/42)` | Design System Custom Token |
| `--n-img` | `36.1111vw` | Dimension / Scale Token |
| `--n-cut` | `33.3333vw` | Dimension / Scale Token |
| `--n-cut-w` | `min(calc(360*max(1px,min(.0661376vw,.124069svh))),var(--n-cut))` | Dimension / Scale Token |
| `--n-cut-x` | `calc(-58*max(1px,min(.0661376vw,.124069svh)))` | Dimension / Scale Token |
| `--n-cut-y` | `calc(143*max(1px,min(.0661376vw,.124069svh)))` | Dimension / Scale Token |
| `--n-font` | `calc(40.06*max(1px,min(.0661376vw,.124069svh)))` | Typography / Scale Token |
| `--n-photo` | `min(calc(400*max(1px,min(.0661376vw,.124069svh))),var(--n-img))` | Dimension / Scale Token |
| `--n-font-s` | `9.25vw` | Typography / Scale Token |
| `--n-art-y` | `126.5vw` | Dimension / Scale Token |
| `--n-phone-unit` | `clamp(.75px,100svh/764,1px)` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.skip-link> — `dwell-au`)**:
   - Landmark `<header class="skip-link">` hosting `Dwell · A new way home` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-fab-register`, `data-header="sky"`, `data-hero="true"`, `data-hero-title="true"`), and stylesheet rule `body { background-image:none }`.
2. **Hero Stage & Focal Lead (<section.hero-scroll> — `A new A n e w way w a y home h o m`)**:
   - Landmark `<section class="hero-scroll hero-rest">` presenting display lead `A new A n e w way w a y home h o m e` and copy excerpt *"Build your home Build your home Build your home Build your home"* over `#3e3e38` canvas and `#d1e5f4` ink.
3. **Primary Showcase & Content Grid (<section.scroll> — `meet m e e t Dwell D w e l l`)**:
   - Landmark `<section class="scroll">` rendering section `meet m e e t Dwell D w e l l` with copy *"Build your home Build your home"*, asset references (`loader-house.webp`, `favicon-96x96.png`, `favicon.svg`, `favicon.ico`), and grid rule `main { flex:1;min-block-size:0 }`.
4. **Interactive Detail & Feature Matrix (<section.scroll> — `Build B u i l d for the f o r t h `)**:
   - Landmark `<section class="scroll">` framing `Build B u i l d for the f o r t h e future f u t...` and `The T h e freedom f r e e d o m to move t o m o v e` (*"How it works How it works How it works How it works"*) with `#aad1ee` surface cards, `#badcf7` accents, and `.page_ { display:block;overflow:visible;block-size:auto }`.
5. **Colophon & Global Directory Footer (<footer.button-text> — `https://dwell.au/`)**:
   - Landmark `<footer class="button-text">` anchoring `Dwell · A new way home` footer links (`Overview · Index · Archive · About · Contact`), copy *"How it works How it works"*, and `#d1e5f4` structural dividers.
