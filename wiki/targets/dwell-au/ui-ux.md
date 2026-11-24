---
title: "UI & UX Architecture: dwell-au"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: dwell-au

## Overview & Design Identity
- **Target**: `dwell-au` (**Dwell · A new way home**)
- **Production URL**: [https://dwell.au/](https://dwell.au/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×3312px`, Mobile `390×872px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#161605` / `#373710`)
- **Summary**: Dwell is a third housing option that lets you have a home and build wealth without a deposit or mortgage. Discover a new way home.
- **Total Clean CSS Variables Extracted**: `203` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `bo`
- **Body Font Stack**: `bo`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 160px`, `line-height: 147.2px`, `font-weight: 360`, `letter-spacing: -4.80001px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 140.849px`, `line-height: 108.454px`, `font-weight: 359`, `letter-spacing: -8.45094px`); rule `h2` (`font-size: calc(34*max(1px,min(.0661376v...`, `line-height: 1.02`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 360`); CSS variables `--font-weight-body: 359`, `--font-width-body: 95%`; rule `p` (`line-height: 1.05`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 16px`, `font-weight: 360`); CSS variables `--field-label: var(--color-moss)`, `--step-label-top: 12%`, `--font-mono: "fr",monospace`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#161605` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f5f4ed` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#3e3e38` | `.glass:before { background: #3e3e38 }` |
| **Interactive Accent / Highlight** | `#373710` | live computed `button` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#aad1ee` | live computed `h1` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#3a3a27` | `var(--field-hover-border)` in `:root` (`5d5d4980`) |

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
   - Landmark `<header class="skip-link">` (`1440x108px`) hosting `Dwell · A new way home` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-fab-register`, `data-header="sky"`, `data-hero="true"`, `data-hero-title="true"`), and stylesheet rule `body { background-image:none }`.
2. **Hero Stage & Focal Lead (<section.hero-scroll> — `a new a n e w way w a y home h o m`)**:
   - Landmark `<section class="hero-scroll hero-rest">` presenting display lead `a new a n e w way w a y home h o m e` and copy excerpt *"An accessible, debt-free path to having a home and growing your w"* over `#161605` canvas and `#f5f4ed` ink.
3. **Primary Showcase & Content Grid (<section.scroll> — `A new A n e w way w a y home h o m`)**:
   - Landmark `<section class="scroll">` rendering section `A new A n e w way w a y home h o m e` with copy *"An accessible, debt-free path to"*, asset references (`loader-house.webp`, `favicon-96x96.png`, `favicon.svg`, `favicon.ico`), and grid rule `main { flex:1;min-block-size:0 }`.
4. **Interactive Detail & Feature Matrix (<section.scroll:nth(2)> — `meet m e e t Dwell D w e l l`)**:
   - Landmark `<section class="scroll">` framing `meet m e e t Dwell D w e l l` and `Build B u i l d for the f o r t h e future f u t...` (*"having a home and growing your"*) with `#3e3e38` surface cards, `#373710` accents, and `.page_ { display:block;overflow:visible;block-size:auto }`.
5. **Colophon & Global Directory Footer (<footer.button-text> — `https://dwell.au/`)**:
   - Landmark `<footer class="button-text">` anchoring `Dwell · A new way home` footer links (`Overview · Index · Archive · About · Contact`), copy *"wealth - no deposit, no mortgage."*, and `#3a3a27` structural dividers.
