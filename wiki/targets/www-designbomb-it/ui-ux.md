# UI & UX Architecture: www-designbomb-it

## Overview & Design Identity
- **Target**: `www-designbomb-it` (**Design Bomb Festival**)
- **Production URL**: [https://www.designbomb.it/](https://www.designbomb.it/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#4a60ff` / `#31a362`)
- **Summary**: The Wave presenta la nuova edizione di Design Bomb, che cresce e diventa festival. 22-23-24 Maggio, Catania.
- **Total Clean CSS Variables Extracted**: `36` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `PP Frama Extrabold Italic`
- **Body Font Stack**: `PP Frama Black Italic`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `var(--font-size)`, `var(--framer-font-size)`, `16px`, `1px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `var(--font-size)`, `var(--framer-font-size)`, `16px`, `1px`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `var(--font-size)`, `var(--framer-font-size)`, `16px`, `1px`)
- **Metadata & Labels**: CSS variables `--letter-spacing: var(--framer-letter-spacing)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#4a60ff` | `var(--token-0689d26c-723f-45fc-b97a-089acbcfc796)` in `:root` |
| **Primary Typography Ink** | `#ceff00` | `var(--token-7cb9fefc-a8e8-4059-91ee-bd65906318ee)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ff3eba` | `var(--token-4809db6f-b397-4188-a942-074244c77dac)` in `:root` |
| **Interactive Accent / Highlight** | `#31a362` | `var(--token-797c06e2-082b-4d59-9429-4a87c1a6bdd2)` in `:root` |
| **Secondary / Muted Copy** | `#f7f6eb` | `var(--token-f1aabd16-a90b-4a64-bd76-31330e5c4d0f)` in `:root` |
| **Structural Hairline Border** | `#141414` | `var(--token-cd7ed41b-0134-43b6-beec-bf340d65ac87)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--token-0689d26c-723f-45fc-b97a-089acbcfc796` | `#4a60ff` | Color / Atmospheric Token |
| `--token-7cb9fefc-a8e8-4059-91ee-bd65906318ee` | `#ceff00` | Color / Atmospheric Token |
| `--token-4809db6f-b397-4188-a942-074244c77dac` | `#ff3eba` | Color / Atmospheric Token |
| `--token-797c06e2-082b-4d59-9429-4a87c1a6bdd2` | `#31a362` | Color / Atmospheric Token |
| `--token-f1aabd16-a90b-4a64-bd76-31330e5c4d0f` | `#f7f6eb` | Color / Atmospheric Token |
| `--token-cd7ed41b-0134-43b6-beec-bf340d65ac87` | `#141414` | Color / Atmospheric Token |
| `--token-8e1f8495-735c-4bc6-8090-6a9a9f74db16` | `#141414` | Color / Atmospheric Token |
| `--text-decoration-skip-ink` | `var(--framer-text-decoration-skip-ink)` | Typography Ink Token |
| `--text-underline-offset` | `var(--framer-text-decoration-offset)` | Typography Ink Token |
| `--font-family` | `var(--framer-font-family)` | Typography / Scale Token |
| `--font-style` | `var(--framer-font-style)` | Typography / Scale Token |
| `--font-weight` | `var(--framer-font-weight)` | Typography / Scale Token |
| `--text-color` | `var(--framer-text-color)` | Typography Ink Token |
| `--letter-spacing` | `var(--framer-letter-spacing)` | Typography / Scale Token |
| `--font-size` | `var(--framer-font-size)` | Typography / Scale Token |
| `--text-transform` | `var(--framer-text-transform)` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.lenis> — `www-designbomb-it`)**:
   - Landmark `<header class="lenis">` hosting `Design Bomb Festival` navigation (`Programma · Workshop · cameretta · Shop · TICKET`), DOM attributes (`data-framer-font-css`, `data-framer-breakpoint-css`, `data-framer-css-ssr-minified`, `data-framer-components="framer-lib-cursors-ho..."`), and stylesheet rule `.hidden-16glhda { display:none!important }`.
2. **Hero Stage & Focal Lead (<section.framer-hw4kQ> — `Design Bomb Festival`)**:
   - Landmark `<section class="framer-hw4kQ">` presenting display lead `Design Bomb Festival` and copy excerpt *"Un festival per tutta la community"* over `#4a60ff` canvas and `#f7f6eb` ink.
3. **Primary Showcase & Content Grid (<section.framer-6q1hH> — `Featured Work & Interactive Showca`)**:
   - Landmark `<section class="framer-6q1hH">` rendering section `Featured Work & Interactive Showcase` with copy *"Un festival per tutta"*, asset references (`CHxdCbEfx7lZs5B6CqTOXcfZQo.jpg`, `script`, `sNmVGd3Q3ckANl0dcx338qCTY4.png`, `yuFzZzaiq6SXFBvCqfED1Hgy4.png`), and grid rule `.hidden-1qs623s { display:none!important }`.
4. **Interactive Detail & Feature Matrix (<section.framer-LuCAZ> — `Technical Architecture & Narrative`)**:
   - Landmark `<section class="framer-LuCAZ">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Tre giorni, tantissimi ospiti, centinaia di persone che respirano"*) with `#ff3eba` surface cards, `#31a362` accents, and `.hidden-1tdjaai { display:none!important }`.
5. **Colophon & Global Directory Footer (<footer.framer-1qs623s> — `https://www.designbomb.it/`)**:
   - Landmark `<footer class="framer-1qs623s">` anchoring `Design Bomb Festival` footer links (`Programma · Workshop · cameretta · Shop · TICKET`), copy *"Awwwards Studio of the Year / Enea Rossi, CEO, Co-Founder e "*, and `#141414` structural dividers.
