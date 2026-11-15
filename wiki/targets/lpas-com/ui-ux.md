# UI & UX Architecture: lpas-com

## Overview & Design Identity
- **Target**: `lpas-com` (**LPAS - Architecture and Interiors**)
- **Production URL**: [https://lpas.com/](https://lpas.com/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#111` ink, `#eee` accent)
- **Summary**: Clear Process. Creative Results. Human-centered. Always Curious. At LPAS, we design with people at the center and purpose at every turn.
- **Total Clean CSS Variables Extracted**: `12` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Aeonik`
- **Body Font Stack**: `Aeonik`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `100%`, `62.5%`, `clamp(4.6rem,.25rem + 5.6640625vw...`, `clamp(4.4rem,.2857142857rem + 5.3...`, `clamp(3.2rem,-2.9714285714rem + 8...`)
- **Section Heading (`H2`)**: rule `h2` (`line-height: 110%`, `font-weight: 400`)
- **Body Copy**: rule `,body` (`line-height: 135%`, `font-weight: 400`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `100%`, `62.5%`, `clamp(4.6rem,.25rem + 5.6640625vw...`, `clamp(4.4rem,.2857142857rem + 5.3...`, `clamp(3.2rem,-2.9714285714rem + 8...`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `body { color: #fff }` |
| **Primary Typography Ink** | `#111` | `main { color: #111 }` |
| **Elevated Surface / Card Substrate** | `#393a3b` | `.template__title:before { background-color: #393a3b }` |
| **Interactive Accent / Highlight** | `#eee` | `.template code { background-color: #eee }` |
| **Secondary / Muted Copy** | `#0000` | `#slideOut-overlay::backdrop { background-color: #0000 }` |
| **Structural Hairline Border** | `#262626` | `.slideOut__aside { background-color: #262626 }` |
| **Variable Token (`--swiper-theme-color`)** | `#007aff` | `var(--swiper-theme-color)` in stylesheet |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--row-gap` | `0` | Layout / Spatial Grid Token |
| `--column-gap` | `1rem` | Layout / Spatial Grid Token |
| `--xxlSpace` | `8.5rem` | Layout / Spatial Grid Token |
| `--marketMainColor` | `rgb(98, 86, 83)` | Brand / Palette Token |
| `--marketSecondaryColor` | `rgb(123, 105, 100)` | Brand / Palette Token |
| `--marketContentColor` | `rgb(255, 255, 255)` | Brand / Palette Token |
| `--marketContentContrast` | `rgb(38, 38, 38)` | Color / Atmospheric Token |
| `--scrollbarWidth` | `0px` | Layout / Spatial Grid Token |
| `--ctaBarHeight` | `0px` | Brand / Palette Token |
| `--viewportWidth` | `calc(100vw - var(--scrollbarWidth))` | Layout / Spatial Grid Token |
| `--cut` | `2rem` | Dimension / Scale Token |
| `--sticky-offset` | `505px` | Dimension / Scale Token |
| `--swiper-theme-color` | `#007aff` | Brand / Palette Token |
| `--swiper-preloader-color` | `#fff` | Brand / Palette Token |
| `--lpas-com-bg` | `#fff` | Canvas Substrate (from `body { color: #fff }`) |
| `--lpas-com-ink` | `#111` | Primary Typography Ink (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.mainHeader> — `lpas-com`)**:
   - Landmark `<header class="mainHeader">` hosting `LPAS - Architecture and Interiors` navigation (`Housing · Interiors · Higher Education · Civic · Commercial`), DOM attributes (`data-browser="Chrome"`, `data-istoch="false"`, `data-logocolor="light"`, `data-first-visit="true"`), and stylesheet rule `video { margin:0;padding:0;border:0;font-size:100%;font:inherit;vertical-align:b... }`.
2. **Hero Stage & Focal Lead (<section.homeHero> — `Sacramento`)**:
   - Landmark `<section class="homeHero">` presenting display lead `Sacramento` and copy excerpt *"723 S Street, Suite 150 Sacramento, CA 95811"* over `#fff` canvas and `#111` ink.
3. **Primary Showcase & Content Grid (<section.blockIntroGeneral> — `Oakland`)**:
   - Landmark `<section class="blockIntroGeneral">` rendering section `Oakland` with copy *"10 Clay Street, Suite 250 Oakland, CA 94607"*, asset references (`main-DN-9Dm9S.css`, `swup-config-DoT-9FzL.js`, `preloader-CQAQSTAa.js`, `lenisSmooth-BjXMsNId.js`), and grid rule `section { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.blockProjectsHighlight> — `We’re a process driven architectur`)**:
   - Landmark `<section class="blockProjectsHighlight">` framing `We’re a process driven architecture and interior...` and `Housing` (*"Architecture + Interiors"*) with `#393a3b` surface cards, `#eee` accents, and `body { line-height:1 }`.
5. **Colophon & Global Directory Footer (<footer.navigationFooter> — `https://lpas.com/`)**:
   - Landmark `<footer class="navigationFooter">` anchoring `LPAS - Architecture and Interior` footer links (`Housing · Interiors · Higher Education · Civic · Commercial`), copy *"A Market-Focused Approach"*, and `#262626` structural dividers.
