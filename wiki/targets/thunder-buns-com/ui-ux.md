# UI & UX Architecture: thunder-buns-com

## Overview & Design Identity
- **Target**: `thunder-buns-com` (**Thunderbuns · Smashburgers Delivered**)
- **Production URL**: [https://thunder-buns.com/](https://thunder-buns.com/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#30363c`)
- **Summary**: The best smash burgers, 100% halal. Delivered across the Netherlands, Belgium and Germany. Order through your usual delivery app.
- **Total Clean CSS Variables Extracted**: `124` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Bowlby One`
- **Body Font Stack**: `Anton`
- **Monospace / Technical Font Stack**: `Haffer Mono`
- **Hero Display (`H1`)**: rule `h1` (`font-size: min(14.5em,130px)`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 3.3em`, `line-height: .88`)
- **Body Copy**: rule `p` (`font-size: 1.4em`, `line-height: 1.2`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `10px`, `14px`, `16px`, `100%`, `1.05em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--cc-bg)` in `:root` |
| **Primary Typography Ink** | `#2c2f31` | `var(--cc-primary-color)` in `:root` |
| **Elevated Surface / Card Substrate** | `#5e6266` | `var(--cc-secondary-color)` in `:root` |
| **Interactive Accent / Highlight** | `#30363c` | `var(--cc-btn-primary-bg)` in `:root` |
| **Secondary / Muted Copy** | `#000` | `var(--cc-btn-primary-hover-bg)` in `:root` |
| **Structural Hairline Border** | `#eaeff2` | `var(--cc-btn-secondary-bg)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--cc-modal-border-radius` | `.5rem` | Elevation / Border Token |
| `--cc-btn-border-radius` | `.4rem` | Elevation / Border Token |
| `--cc-modal-transition-duration` | `.25s` | Motion / Easing Token |
| `--cc-link-color` | `var(--cc-btn-primary-bg)` | Typography Ink Token |
| `--cc-modal-margin` | `1rem` | Layout / Spatial Grid Token |
| `--cc-z-index` | `2147483647` | Elevation / Border Token |
| `--cc-bg` | `#fff` | Canvas / Surface Token |
| `--cc-primary-color` | `#2c2f31` | Brand / Palette Token |
| `--cc-secondary-color` | `#5e6266` | Brand / Palette Token |
| `--cc-btn-primary-bg` | `#30363c` | Canvas / Surface Token |
| `--cc-btn-primary-color` | `#fff` | Brand / Palette Token |
| `--cc-btn-primary-border-color` | `var(--cc-btn-primary-bg)` | Brand / Palette Token |
| `--cc-btn-primary-hover-bg` | `#000` | Canvas / Surface Token |
| `--cc-btn-primary-hover-color` | `#fff` | Brand / Palette Token |
| `--cc-btn-primary-hover-border-color` | `var(--cc-btn-primary-hover-bg)` | Brand / Palette Token |
| `--cc-btn-secondary-bg` | `#eaeff2` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.lenis> — `thunder-buns-com`)**:
   - Landmark `<header class="lenis">` hosting `Thunderbuns · Smashburgers Delivered` navigation (`English · Nederlands · Deutsch · Français · Order`), DOM attributes (`data-ga-id="G-DKWN4TYM2V"`, `data-barba="wrapper"`, `data-scrolling-started="false"`, `data-scrolling-direction="up"`), and stylesheet rule `.mapboxgl-canvas { position:absolute;left:0;top:0 }`.
2. **Hero Stage & Focal Lead (<section.award> — `Burgers that hit like lightning.`)**:
   - Landmark `<section class="award">` presenting display lead `Burgers that hit like lightning.` and copy excerpt *"Order Thunderbuns Online - Order Thunderbuns Online - Order Thund"* over `#fff` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.award> — `Who are we? What do we do? Where a`)**:
   - Landmark `<section class="award">` rendering section `Who are we? What do we do? Where are we?` with copy *"Order Thunderbuns Online -"*, asset references (`tb-favicon2.png`, `BowlbyOne-Regular.woff2`, `Satoshi-Regular.woff2`, `image.mux.com`), and grid rule `.mapboxgl-map:-webkit-full-screen { width:100%;height:100% }`.
4. **Interactive Detail & Feature Matrix (<section.award> — `Winner Thuisbezorgd.nl Award 2025 `)**:
   - Landmark `<section class="award">` framing `Winner Thuisbezorgd.nl Award 2025 “Best National...` and `Best National Chain` (*"We make smashburgers. Two patties, smashed onto a screaming hot p"*) with `#5e6266` surface cards, `#30363c` accents, and `.mapboxgl-canary { background-color:salmon }`.
5. **Colophon & Global Directory Footer (<footer.shape> — `https://thunder-buns.com/`)**:
   - Landmark `<footer class="shape">` anchoring `Thunderbuns · Smashburgers Deliv` footer links (`English · Nederlands · Deutsch · Français · Order`), copy *"You'll now find us in 130+ locations across the Netherlands,"*, and `#eaeff2` structural dividers.
