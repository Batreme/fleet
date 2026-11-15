# UI & UX Architecture: www-genomines-com

## Overview & Design Identity
- **Target**: `www-genomines-com` (**Home**)
- **Production URL**: [https://www.genomines.com/](https://www.genomines.com/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#efebe1` / `#fff`)
- **Summary**: Genomines pioneers sustainable mineral extraction using hyperaccumulator plants, harnessing genomics to mine critical metals from soil, a...
- **Total Clean CSS Variables Extracted**: `22` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Causten`
- **Body Font Stack**: `Geist Mono`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(1.19rem,.9722222222vw,1.61rem)`, `clamp(3.6rem,4.1666666667vw,7.8rem)`, `62.5%`, `10px`, `1.2rem`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(1.19rem,.9722222222vw,1.61rem)`, `clamp(3.6rem,4.1666666667vw,7.8rem)`, `62.5%`, `10px`, `1.2rem`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(1.19rem,.9722222222vw,1.61rem)`, `clamp(3.6rem,4.1666666667vw,7.8rem)`, `62.5%`, `10px`, `1.2rem`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(1.19rem,.9722222222vw,1.61rem)`, `clamp(3.6rem,4.1666666667vw,7.8rem)`, `62.5%`, `10px`, `1.2rem`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#efebe1` | `body { background: #efebe1 }` |
| **Primary Typography Ink** | `#373735` | `body { color: #373735 }` |
| **Elevated Surface / Card Substrate** | `#000` | `.grid__visualizer-toggle { background: #000 }` |
| **Interactive Accent / Highlight** | `#fff` | `.grid__visualizer-toggle { color: #fff }` |
| **Secondary / Muted Copy** | `#d4ff8f` | `header__nav>ul .nav__item .nav_... { background: #d4ff8f }` |
| **Structural Hairline Border** | `#b3261e` | `al__form .contact-modal__feedba... { color: #b3261e }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--gridCell` | `0px` | Layout / Spatial Grid Token |
| `--gridGap` | `0px` | Layout / Spatial Grid Token |
| `--gridMargin` | `0px` | Layout / Spatial Grid Token |
| `--wrapper-margin` | `max(18px, 2.0833vw)` | Layout / Spatial Grid Token |
| `--margin-xl` | `72px` | Layout / Spatial Grid Token |
| `--margin-l` | `48px` | Layout / Spatial Grid Token |
| `--margin-m` | `24px` | Layout / Spatial Grid Token |
| `--margin-s` | `12px` | Layout / Spatial Grid Token |
| `--controls-backdrop-color` | `rgba(0, 0, 0, .4)` | Brand / Palette Token |
| `--media-range-track-background` | `rgba(239, 235, 225, .25)` | Canvas / Surface Token |
| `--media-time-range-buffered-color` | `rgba(239, 235, 225, .45)` | Brand / Palette Token |
| `--gradient-steps` | `transparent 0%, transparent 100%` | Dimension / Scale Token |
| `--media-control-hover-background` | `rgba(239, 235, 225, .1)` | Canvas / Surface Token |
| `--media-menu-background` | `rgba(55, 55, 53, .5)` | Canvas / Surface Token |
| `--media-menu-item-hover-background` | `rgba(239, 235, 225, .1)` | Canvas / Surface Token |
| `--quotes-extra-height` | `111px` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.global__header> — `www-genomines-com`)**:
   - Landmark `<header class="global__header">` hosting `Home` navigation (`Homepage · Technology · Systemic Return · About us · Work with us`), DOM attributes (`data-taxi-ignore="true"`, `data-action="contact"`, `data-taxi-ignore="true"`, `data-action="contact"`), and stylesheet rule `after { margin:0;padding:0;box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.section__hero> — `Let's grow together.`)**:
   - Landmark `<section class="section__hero">` presenting display lead `Let's grow together.` and copy excerpt *"Company About us Work with us"* over `#efebe1` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.section__paradigm-shift> — `We Grow Metal`)**:
   - Landmark `<section class="section__paradigm-shift">` rendering section `We Grow Metal` with copy *"Biological infrastructure for critical metal extraction."*, asset references (`favicon-96x96.png`, `favicon.svg`, `favicon.ico`, `apple-touch-icon.png`), and grid rule `video { max-width:100%;display:block }`.
4. **Interactive Detail & Feature Matrix (<section.section__scenes> — `At scale.`)**:
   - Landmark `<section class="section__scenes">` framing `At scale.` and `The payload.` (*"Battery-grade nickel, harvested at best-in-class costs."*) with `#000` surface cards, `#fff` accents, and `button { background:none;border:none;cursor:pointer;font:inherit;color:inherit }`.
5. **Colophon & Global Directory Footer (<footer.global__footer> — `https://www.genomines.com/`)**:
   - Landmark `<footer class="global__footer">` anchoring `Home` footer links (`Homepage · Technology · Systemic Return · About us · Work with us`), copy *"Inside the team replacing the"*, and `#b3261e` structural dividers.
