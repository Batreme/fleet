# UI & UX Architecture: pyzhevsky-estate

## Overview & Design Identity
- **Target**: `pyzhevsky-estate` (**Pyzhevsky — official website of a deluxe residence five minutes from the...**)
- **Production URL**: [https://pyzhevsky.estate/](https://pyzhevsky.estate/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#12100e` / `#75736d`)
- **Summary**: An intimate residential project. Apartments in the historic centre. Panoramic views and original architecture.
- **Total Clean CSS Variables Extracted**: `484` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Garamond Light`
- **Body Font Stack**: `Halvar Breitschrift`
- **Monospace / Technical Font Stack**: `Consolas`
- **Hero Display (`H1`)**: rule `,h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: rule `,h2` (`font-weight: 400`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `2em`, `1em`, `80%`, `75%`, `100%`)
- **Metadata & Labels**: CSS variables `--t-small: var(--c-pale-dark)`, `--t-small-rgb: var(--c-pale-dark-rgb)`, `--t-button-color-small-text: var(--t-small)`; rule `,small` (`font-weight: 500`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#12100e` | `var(--c-black)` in `:root` |
| **Primary Typography Ink** | `#2f2b27` | `var(--c-black-hover)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff` | `var(--c-white)` in `:root` |
| **Interactive Accent / Highlight** | `#75736d` | `var(--c-dark-beige)` in `:root` |
| **Secondary / Muted Copy** | `#88857e` | `var(--c-dark-beige-hover)` in `:root` |
| **Structural Hairline Border** | `#bdb6a9` | `var(--c-beige)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--text-box-edge` | `cap` | Typography Ink Token |
| `--baseline-size` | `1cap` | Layout / Spatial Grid Token |
| `--fos` | `-0.1365em` | Dimension / Scale Token |
| `--foe` | `-0.1635em` | Dimension / Scale Token |
| `--lh` | `var(--xxxxl,1.8em) var(--n-xxxxl,1.5em)` | Dimension / Scale Token |
| `--scale-px` | `1px` | Dimension / Scale Token |
| `--scale-rem` | `1rem` | Dimension / Scale Token |
| `--scale-em` | `1em` | Dimension / Scale Token |
| `--scale-text-px` | `1px` | Typography Ink Token |
| `--scale-text-rem` | `1rem` | Typography Ink Token |
| `--scale-text-em` | `1em` | Typography Ink Token |
| `--scale-none-px` | `1px` | Dimension / Scale Token |
| `--scale-none-rem` | `1rem` | Dimension / Scale Token |
| `--n-sm` | `initial` | Design System Custom Token |
| `--n-md` | `initial` | Design System Custom Token |
| `--n-lg` | `initial` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `pyzhevsky-estate`)**:
   - Landmark `<header class="header is-hidden--print">` hosting `Pyzhevsky — official website of a de` navigation (`Select an apartment · 3D area map`), DOM attributes (`data-barba="wrapper"`, `data-nosnippet`, `data-plugin="preloader"`, `data-preloader-animation-name-in="preloader-in"`), and stylesheet rule `html { line-height:1.15;-webkit-text-size-adjust:100% }`.
2. **Hero Stage & Focal Lead (<section.section> — `Pyzhevsky`)**:
   - Landmark `<section class="section l-intro-section">` presenting display lead `Pyzhevsky` and copy excerpt *"Skip to main content"* over `#12100e` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.section> — `Facade`)**:
   - Landmark `<section class="section ui-dark">` rendering section `Facade` with copy *"A d e l u x e p r o j e c t i n t h e h i s t o r i c q u a r t e"*, asset references (`storage.googleapis.com`, `itc-garamond_light.woff2`, `Halvar-Breitschrift-Regular-Web.w...`, `Halvar-Breitschrift-Medium-Web.woff2`), and grid rule `pre { font-family:monospace,monospace;font-size:1em }`.
4. **Interactive Detail & Feature Matrix (<section.section> — `Views`)**:
   - Landmark `<section class="section section--top-2">` framing `Views` and `Location` (*"Restrained, assured, timeless — they put the city on pause, so al"*) with `#fff` surface cards, `#75736d` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.section> — `https://pyzhevsky.estate/`)**:
   - Landmark `<footer class="section section--no-overflow">` anchoring `Pyzhevsky — official website of ` footer links (`Select an apartment · 3D area map`), copy *"The minimalist form of the three buildings draws on the sign"*, and `#bdb6a9` structural dividers.
