# UI & UX Architecture: offpossible-com

## Overview & Design Identity
- **Target**: `offpossible-com` (**OffPossible · Interfaces Between People and Their Own Minds**)
- **Production URL**: [https://offpossible.com/](https://offpossible.com/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#0006`)
- **Summary**: OffPossible builds and backs interfaces between people and their own minds. In-house products live at Noumen, including Actually and None...
- **Total Clean CSS Variables Extracted**: `21` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `ABC Diatype Semi Mono`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `ABC Diatype Semi Mono`
- **Hero Display (`H1`)**: CSS variables `--font-display: var(--font-mono)`; rule `h1` (`font-size: clamp(46px,8vw,88px)`, `line-height: .95`, `letter-spacing: -.045em`, `font-weight: 400`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 18px`, `line-height: 1.2`, `letter-spacing: -.02em`, `font-weight: 400`)
- **Body Copy**: rule `p` (`font-size: 20px`, `line-height: 1.25`, `letter-spacing: -.2px`)
- **Metadata & Labels**: CSS variables `--font-mono: "ABC Diatype Semi Mono", ui-monospace, "SF Mono", Menlo, monospace`; rule `.label` (`font-size: 16px`, `line-height: 1.25`, `letter-spacing: -.16px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--scramble-color)` in `:root` |
| **Primary Typography Ink** | `#fff` | `.chrome-hit { color: #fff }` |
| **Elevated Surface / Card Substrate** | `#fff6` | `.footer-action-muted { color: #fff6 }` |
| **Interactive Accent / Highlight** | `#0006` | `.footer-action-muted { color: #0006 }` |
| **Secondary / Muted Copy** | `#0b351c` | `.stack-line-accent { color: #0b351c }` |
| **Structural Hairline Border** | `#f4cae3` | `.stack-line-accent { color: #f4cae3 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--edge-inset` | `max(20px, 2vmin)` | Dimension / Scale Token |
| `--header-logo-width` | `24.53vw` | Layout / Spatial Grid Token |
| `--header-logo-height` | `calc(var(--header-logo-width) * 75 / 533)` | Layout / Spatial Grid Token |
| `--header-logo-ink-top` | `calc(var(--header-logo-height) * 2.98828 / 75)` | Typography Ink Token |
| `--site-symbol-size` | `calc(var(--header-logo-height) * 70.39 / 75)` | Layout / Spatial Grid Token |
| `--font-mono` | `"ABC Diatype Semi Mono", ui-monospace, "SF Mono", Menlo, monospace` | Typography / Scale Token |
| `--font-display` | `var(--font-mono)` | Typography / Scale Token |
| `--font-ui` | `"Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif` | Typography / Scale Token |
| `--instrument-panel-gap` | `clamp(16px, 1.5vw, 24px)` | Layout / Spatial Grid Token |
| `--scramble-color` | `#000!important` | Brand / Palette Token |
| `--mobile-screen-inset` | `24px` | Dimension / Scale Token |
| `--mobile-screen-padding-x` | `8px` | Layout / Spatial Grid Token |
| `--mobile-shader-overscan-y` | `240px` | Dimension / Scale Token |
| `--instrument-intensity` | `1.000` | Design System Custom Token |
| `--instrument-certainty` | `0.000` | Design System Custom Token |
| `--instrument-agency` | `1.000` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.backdrop-grid> — `offpossible-com`)**:
   - Landmark `<header class="backdrop-grid">` hosting `OffPossible · Interfaces Between Peo` navigation (`Noumen · Privacy · seenoumen.com`), DOM attributes (`data-shader-layer="fixed"`, `data-field-sound="muted"`, `data-agency-mode="steer"`, `data-content-mode="base"`), and stylesheet rule `body { background-color:000;width:100%;min-height:100vh;overflow-x:hidden }`.
2. **Hero Stage & Focal Lead (<section.easter-prompt> — `We build and back interfaces betwe`)**:
   - Landmark `<section class="easter-prompt">` presenting display lead `We build and back interfaces between people and t...` and copy excerpt *"M h a t w o u l d y o u b u i l d ?"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.scroll-section> — `No one has direct sight of their o`)**:
   - Landmark `<section class="scroll-section">` rendering section `No one has direct sight of their own mind.` with copy *"Privacy Policy Privacy"*, asset references (`clarity.js`, `z1sq4va9rn`, `sitemap.xml`, `llms.txt`), and grid rule `webkit-scrollbar { display:none }`.
4. **Interactive Detail & Feature Matrix (<section.scroll-section> — `We support builders who make peopl`)**:
   - Landmark `<section class="scroll-section">` framing `We support builders who make people more legible...` and `We work early enough to change the question, not...` (*"Prompts and generated results may be privately retained and revie"*) with `#fff6` surface cards, `#0006` accents, and `html.no-js .sound-toggle { display:none }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://offpossible.com/`)**:
   - Landmark `<footer class="site-footer">` anchoring `OffPossible · Interfaces Between` footer links (`Noumen · Privacy · seenoumen.com`), copy *"Lenses gave people sight of cells and distant planets."*, and `#f4cae3` structural dividers.
