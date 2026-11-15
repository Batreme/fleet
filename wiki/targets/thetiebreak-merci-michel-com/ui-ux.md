# UI & UX Architecture: thetiebreak-merci-michel-com

## Overview & Design Identity
- **Target**: `thetiebreak-merci-michel-com` (**The Tie-break!**)
- **Production URL**: [https://thetiebreak.merci-michel.com/](https://thetiebreak.merci-michel.com/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#fff302`)
- **Summary**: Play the game and discover the latest New Balance X Miu Miu collection with Coco Gauff.
- **Total Clean CSS Variables Extracted**: `16` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Instrument`
- **Body Font Stack**: `WorkSans`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1.4em`, `2.4em`, `15em`, `8.4em`, `1.6em`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1.4em`, `2.4em`, `15em`, `8.4em`, `1.6em`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1.4em`, `2.4em`, `15em`, `8.4em`, `1.6em`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1.4em`, `2.4em`, `15em`, `8.4em`, `1.6em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--ui-color-bg-primary)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--ui-color-primary)` in `:root` |
| **Elevated Surface / Card Substrate** | `#142a48` | `var(--ui-color-blue)` in `:root` |
| **Interactive Accent / Highlight** | `#fff302` | `var(--ui-color-primary-hover)` in `:root` |
| **Secondary / Muted Copy** | `#05152d` | `#preloader .preloader-background { background: #05152d }` |
| **Structural Hairline Border** | `#fffc` | `::-moz-selection { background: #fffc }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ball-size` | `max(35px, 1.8vw)` | Layout / Spatial Grid Token |
| `--bounce-height` | `90px` | Layout / Spatial Grid Token |
| `--floor-height` | `0px` | Layout / Spatial Grid Token |
| `--duration` | `.8s` | Motion / Easing Token |
| `--exit-duration` | `.3s` | Motion / Easing Token |
| `--base-text` | `10px` | Typography Ink Token |
| `--padding` | `max(6px, calc(var(--base-text) * .15))` | Layout / Spatial Grid Token |
| `--ui-colors` | `bg-primary:#000 / primary:#fff / blue:#142a48 / primary-hover:#fff302` | Brand / Palette Token |
| `--ui-color-bg-primary` | `#000` | Canvas / Surface Token |
| `--ui-color-primary` | `#fff` | Brand / Palette Token |
| `--ui-color-blue` | `#142a48` | Brand / Palette Token |
| `--ui-color-primary-hover` | `#fff302` | Brand / Palette Token |
| `--miumiu-header` | `1.5em` | Layout / Spatial Grid Token |
| `--scrollbar-width` | `0px` | Layout / Spatial Grid Token |
| `--inner-height` | `900px` | Layout / Spatial Grid Token |
| `--vp-height` | `900px` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.desktop> — `thetiebreak-merci-michel-com`)**:
   - Landmark `<header class="desktop">` hosting `The Tie-break!` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-v-app`, `data-can-control`, `data-engine="three.js r184"`), and stylesheet rule `.webgl-canvas { outline:none }`.
2. **Hero Stage & Focal Lead (<main.ui> — `The Tie-break!`)**:
   - Landmark `<main class="ui">` presenting display lead `The Tie-break!` and copy excerpt *"Play the game and discover the latest New Balance X Miu Miu colle"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<main.ui> — `Featured Work & Interactive Showca`)**:
   - Landmark `<main class="ui">` rendering section `Featured Work & Interactive Showcase` with copy *"The Tie-break!"*, asset references (`utag.js`, `favicon.ico`, `favicon_dark.svg`, `favicon_light.svg`), and grid rule `hover { border-color:transparent }`.
4. **Interactive Detail & Feature Matrix (<main.ui> — `Technical Architecture & Narrative`)**:
   - Landmark `<main class="ui">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Work & Interactive Showcase"*) with `#142a48` surface cards, `#fff302` accents, and `before { transform:scale(1.1) }`.
5. **Colophon & Global Directory Footer (<footer.is-exiting> — `https://thetiebreak.merci-michel.com/`)**:
   - Landmark `<footer class="is-exiting">` anchoring `The Tie-break!` footer links (`Overview · Index · Archive · About · Contact`), copy *"Technical Architecture & Narrative"*, and `#fffc` structural dividers.
