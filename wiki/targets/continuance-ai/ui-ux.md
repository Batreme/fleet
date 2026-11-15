# UI & UX Architecture: continuance-ai

## Overview & Design Identity
- **Target**: `continuance-ai` (**Continuance - A novel by Chris Bennett**)
- **Production URL**: [https://continuance.ai/](https://continuance.ai/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#d9d9d9`)
- **Summary**: A near-future thriller about the people we'd do anything to keep — and what it costs when we succeed.
- **Total Clean CSS Variables Extracted**: `46` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Roboto Mono`
- **Body Font Stack**: `Roboto Mono Fallback`
- **Monospace / Technical Font Stack**: `Roboto Mono`
- **Hero Display (`H1`)**: rule `,h1` (`font-size: var(--font-size-4xl)`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--font-size-sm)`, `.875rem`, `clamp(.6875rem,calc(.6875rem + .3...`, `var(--font-size-ssm)`, `var(--font-size-4xl)`)
- **Body Copy**: CSS variables `--font-family-body: "Roboto Mono","Roboto Mono Fallback"`
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--font-size-sm)`, `.875rem`, `clamp(.6875rem,calc(.6875rem + .3...`, `var(--font-size-ssm)`, `var(--font-size-4xl)`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `4Ye .AnimatedButtonReveal_cr-fi... { color: #fff }` |
| **Primary Typography Ink** | `#ffa500` | `to { stroke: orange }` (`#ffa500`) |
| **Elevated Surface / Card Substrate** | `#808080` | `meraAccessError_camera-access-e... { color: gray }` (`#808080`) |
| **Interactive Accent / Highlight** | `#d9d9d9` | `.CubeLine_cube-line__dot__A1usj { background-color: #d9d9d9 }` |
| **Secondary / Muted Copy** | `#ff0000` | `.Hero_line__TlETo { background: red }` (`#ff0000`) |
| **Structural Hairline Border** | `#000` | `HeaderNav_header__nav--active-b... { background-color: #000 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--after-height` | `20px` | Layout / Spatial Grid Token |
| `--after-rotate` | `0deg` | Design System Custom Token |
| `--frame-stroke` | `var(--c-brand-secondary)` | Elevation / Border Token |
| `--hover-bg` | `var(--c-brand-primary)` | Canvas / Surface Token |
| `--text-color-active` | `rgba(var(--c-brand-primary-rgb),0.5)` | Typography Ink Token |
| `--font-family-body` | `"Roboto Mono","Roboto Mono Fallback"` | Typography / Scale Token |
| `--card-back-radius` | `calc(13rem / var(--fz-base))` | Elevation / Border Token |
| `--font-family-title` | `"objectSans","objectSans Fallback"` | Typography / Scale Token |
| `--hero-tilt-gap` | `5px` | Layout / Spatial Grid Token |
| `--c-brand-primary-rgb` | `52,56,73` | Brand / Palette Token |
| `--c-brand-primary` | `rgb(var(--c-brand-primary-rgb))` | Brand / Palette Token |
| `--c-brand-secondary-rgb` | `173,138,255` | Brand / Palette Token |
| `--c-brand-secondary` | `rgb(var(--c-brand-secondary-rgb))` | Brand / Palette Token |
| `--c-light-gray-rgb` | `217,217,217` | Canvas / Surface Token |
| `--c-light-gray` | `rgb(var(--c-light-gray-rgb))` | Canvas / Surface Token |
| `--c-orange-rgb` | `255,153,0,1` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.page> — `continuance-ai`)**:
   - Landmark `<header class="page">` hosting `Continuance - A novel by Chris Benne` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `kItem_answers-block-item__lottie_... { width:100%;height:100%;position:absolute }`.
2. **Hero Stage & Focal Lead (<main.home> — `Continuance - A novel by Chris Ben`)**:
   - Landmark `<main class="home">` presenting display lead `Continuance - A novel by Chris Bennett` and copy excerpt *"Mapping neural signatures..."* over `#fff` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<main.home> — `Featured Work & Interactive Showca`)**:
   - Landmark `<main class="home">` rendering section `Featured Work & Interactive Showcase` with copy *"34-year-old researcher fighting to save rare-variant patients the"*, asset references (`0807ff31c16ab04c.css`, `1ee6f0f6dd8fb3fa.css`, `a5188067206b89ec.css`, `5b6568268f4e7c11.css`), and grid rule `.AnswersBlock_answers-block__vC9vt { left:10.6770833333% }`.
4. **Interactive Detail & Feature Matrix (<main.home> — `Technical Architecture & Narrative`)**:
   - Landmark `<main class="home">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Kaiku / V2030 1125 K a i k u / V 2 0 3 0 1 1 2 5"*) with `#808080` surface cards, `#d9d9d9` accents, and `nswersBlock_answers-block__items_... { flex-direction:column }`.
5. **Colophon & Global Directory Footer (<footer.Footer_footer__2_6CR> — `https://continuance.ai/`)**:
   - Landmark `<footer class="Footer_footer__2_6CR">` anchoring `Continuance - A novel by Chris B` footer links (`Overview · Index · Archive · About · Contact`), copy *"Kaiku / V2030 1125"*, and `#000` structural dividers.
