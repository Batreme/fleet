---
title: "UI Prompt Blueprint: continuance-ai"
date: 2026-11-15
target: "continuance-ai"
status: analyzed
capture: specimen
capture_desktop: specimen
capture_mobile: specimen
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#d9d9d9`)"
---

# UI Design System & Master Generation Blueprint: continuance-ai

> **Continuance - A novel by Chris Bennett** (https://continuance.ai/) — A near-future thriller about the people we'd do anything to keep — and what it costs when we succeed.

![Desktop Design Specimen (Offline WebGL/JS Fallback — not live site capture)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Continuance - A novel by Chris Bennett** (`https://continuance.ai/`). A near-future thriller about the people we'd do anything to keep — and what it costs when we succeed.
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#d9d9d9`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`4Ye .AnimatedButtonReveal_cr-fi... { color: #fff }`) paired with `#000` primary typography and `#d9d9d9` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Roboto Mono` for display copy (`Continuance - A novel by Chris Benne`) with `Roboto Mono Fallback` and `Roboto Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1023px` container bounds (`gap: .8125rem`, padding `20px`) with `cubic-bezier(.85,0,.15,1)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Design Specimen (Offline WebGL/JS Fallback — not live site capture)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `1023px` extracted from `continuance-ai` stylesheet.
- **Canvas Lateral Padding & Spacing**: `20px` lateral canvas padding with `.8125rem` grid gap.
- **Border Radius Scale**: `4px`, `50%`, `.5rem`, `5px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1023px`, `gap: .8125rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `20px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:1023px)`, `@media (min-width:1921px)`, `@media (min-width:1440px)`, `@media (min-width:600px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `4Ye .AnimatedButtonReveal_cr-fi... { color: #fff }` |
| **Primary Typography Ink** | `#ffa500` | `to { stroke: orange }` (`#ffa500`) |
| **Elevated Surface / Card Substrate** | `#808080` | `meraAccessError_camera-access-e... { color: gray }` (`#808080`) |
| **Interactive Accent / Highlight** | `#d9d9d9` | `.CubeLine_cube-line__dot__A1usj { background-color: #d9d9d9 }` |
| **Secondary / Muted Copy** | `#ff0000` | `.Hero_line__TlETo { background: red }` (`#ff0000`) |
| **Structural Hairline Border** | `#000` | `HeaderNav_header__nav--active-b... { background-color: #000 }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
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

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Roboto Mono`.
- **Primary Body Stack**: `Roboto Mono Fallback`.
- **Technical / Metadata Stack**: `Roboto Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `,h1` (`font-size: var(--font-size-4xl)`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--font-size-sm)`, `.875rem`, `clamp(.6875rem,calc(.6875rem + .3...`, `var(--font-size-ssm)`, `var(--font-size-4xl)`).
- **Body Copy**: CSS variables `--font-family-body: "Roboto Mono","Roboto Mono Fallback"`.
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--font-size-sm)`, `.875rem`, `clamp(.6875rem,calc(.6875rem + .3...`, `var(--font-size-ssm)`, `var(--font-size-4xl)`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.85,0,.15,1)`, `cubic-bezier(.87,0,.13,1)`, `cubic-bezier(.8,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `imatedButtonReveal_btn__inner__jJ...`**: `transition: transform .3s ease-out` extracted from `continuance-ai` stylesheet.
- **Selector `imatedButtonReveal_btn__inner__jJ...`**: `transition: transform .3s cubic-bezier(.85,0,.15,1)` extracted from `continuance-ai` stylesheet.
- **Selector `oUEb .AnimatedButtonReveal_cr-obj...`**: `transition: .3s cubic-bezier(.85,0,.15,1)` extracted from `continuance-ai` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.85,0,.15,1)`)**: Governs interactive state transitions across `<header.page>` and `<main.home>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Continuance - A novel by Chris Bennett     │
│ ====================================================================== │
│ [ <header.page>            | Overview · Index · Archive · About · C ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <main.home>                                          |   │
│ | H1: Continuance - A novel by Chris Bennett                       |   │
│ | Substrate: #fff       | Ink: #000       | Accent: #d9d9d9        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<main.home>               ) max-w: 1023px         |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Featured Work & Interactive  |  | Technical Architecture & Nar | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .8125r) | │
│ | [<header.page>] -> [<main.home>] -> [<main.home>] |                  │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.Footer_footer_) | https://continuance.ai/            │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
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

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: continuance-ai (Continuance - A novel by Chris Bennett)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `continuance-ai` (**Continuance - A novel by Chris Bennett** — `https://continuance.ai/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#d9d9d9`).
- **Identity & Domain Context**: A near-future thriller about the people we'd do anything to keep — and what it costs when we succeed.
- **Primary Substrate**: `#fff` (`4Ye .AnimatedButtonReveal_cr-fi... { color: #fff }`), **Primary Ink**: `#000`, **Accent / Highlight**: `#d9d9d9`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`4Ye .AnimatedButtonReveal_cr-fi... { color: #fff }`) paired with `#000` primary typography and `#d9d9d9` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Roboto Mono` for display copy (`Continuance - A novel by Chris Benne`) with `Roboto Mono Fallback` and `Roboto Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1023px` container bounds (`gap: .8125rem`, padding `20px`) with `cubic-bezier(.85,0,.15,1)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `continuance-ai` in your global stylesheet:

:root {
  /* Continuance - A novel by Chris Bennett (continuance-ai) — Ground-Truth Extracted CSS Variables */
  --after-height: 20px; /* Layout / Spatial Grid Token (continuance-ai) */
  --after-rotate: 0deg; /* Design System Custom Token (continuance-ai) */
  --frame-stroke: var(--c-brand-secondary); /* Elevation / Border Token (continuance-ai) */
  --hover-bg: var(--c-brand-primary); /* Canvas / Surface Token (continuance-ai) */
  --text-color-active: rgba(var(--c-brand-primary-rgb),0.5); /* Typography Ink Token (continuance-ai) */
  --font-family-body: "Roboto Mono","Roboto Mono Fallback"; /* Typography / Scale Token (continuance-ai) */
  --card-back-radius: calc(13rem / var(--fz-base)); /* Elevation / Border Token (continuance-ai) */
  --font-family-title: "objectSans","objectSans Fallback"; /* Typography / Scale Token (continuance-ai) */
  --hero-tilt-gap: 5px; /* Layout / Spatial Grid Token (continuance-ai) */
  --c-brand-primary-rgb: 52,56,73; /* Brand / Palette Token (continuance-ai) */
  --c-brand-primary: rgb(var(--c-brand-primary-rgb)); /* Brand / Palette Token (continuance-ai) */
  --c-brand-secondary-rgb: 173,138,255; /* Brand / Palette Token (continuance-ai) */
  --c-brand-secondary: rgb(var(--c-brand-secondary-rgb)); /* Brand / Palette Token (continuance-ai) */
  --c-light-gray-rgb: 217,217,217; /* Canvas / Surface Token (continuance-ai) */
  --c-light-gray: rgb(var(--c-light-gray-rgb)); /* Canvas / Surface Token (continuance-ai) */
  --c-orange-rgb: 255,153,0,1; /* Design System Custom Token (continuance-ai) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fff` — grounded in `4Ye .AnimatedButtonReveal_cr-fi... { color: #fff }`
- **Primary Typography Ink**: `#ffa500` — grounded in `to { stroke: orange }` (`#ffa500`)
- **Elevated Surface / Card Substrate**: `#808080` — grounded in `meraAccessError_camera-access-e... { color: gray }` (`#808080`)
- **Interactive Accent / Highlight**: `#d9d9d9` — grounded in `.CubeLine_cube-line__dot__A1usj { background-color: #d9d9d9 }`
- **Secondary / Muted Copy**: `#ff0000` — grounded in `.Hero_line__TlETo { background: red }` (`#ff0000`)
- **Structural Hairline Border**: `#000` — grounded in `HeaderNav_header__nav--active-b... { background-color: #000 }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1023px` extracted from `continuance-ai` stylesheet
- **Padding & Gutters**: `20px` lateral canvas padding with `.8125rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1023px`, `gap: .8125rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `20px` horizontal padding
- **Media Queries**: `@media (max-width:1023px)`, `@media (min-width:1921px)`, `@media (min-width:1440px)`, `@media (min-width:600px)`
- **Corner Radii**: `4px`, `50%`, `.5rem`, `5px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Roboto Mono`
- **Body Font Stack**: `Roboto Mono Fallback`
- **Monospace / Technical Font Stack**: `Roboto Mono`
- **H1 Display Rule**: rule `,h1` (`font-size: var(--font-size-4xl)`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--font-size-sm)`, `.875rem`, `clamp(.6875rem,calc(.6875rem + .3...`, `var(--font-size-ssm)`, `var(--font-size-4xl)`)
- **Body Copy Rule**: CSS variables `--font-family-body: "Roboto Mono","Roboto Mono Fallback"`
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--font-size-sm)`, `.875rem`, `clamp(.6875rem,calc(.6875rem + .3...`, `var(--font-size-ssm)`, `var(--font-size-4xl)`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `continuance-ai` (`Continuance - A novel by Chris Bennett`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.page> — `continuance-ai`)**:
   - DOM & Selectors: Landmark `<header class="page">` hosting `Continuance - A novel by Chris Benne` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `kItem_answers-block-item__lottie_... { width:100%;height:100%;position:absolute }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.page> — `continuance-ai`)` (`continuance-ai`) adapts across `@media (max-width:1023px)`, `@media (min-width:1921px)`, `@media (min-width:1440px)`, `@media (min-width:600px)` with `cubic-bezier(.85,0,.15,1)`, `cubic-bezier(.87,0,.13,1)`, `cubic-bezier(.8,0,.2,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<main.home> — `Continuance - A novel by Chris Ben`)**:
   - DOM & Selectors: Landmark `<main class="home">` presenting display lead `Continuance - A novel by Chris Bennett` and copy excerpt *"Mapping neural signatures..."* over `#fff` canvas and `#000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#fff` background with `#000` headline `Continuance - A novel by Chris Bennett`.
3. **Primary Showcase & Content Grid (<main.home> — `Featured Work & Interactive Showca`)**:
   - DOM & Selectors: Landmark `<main class="home">` rendering section `Featured Work & Interactive Showcase` with copy *"34-year-old researcher fighting to save rare-variant patients the"*, asset references (`0807ff31c16ab04c.css`, `1ee6f0f6dd8fb3fa.css`, `a5188067206b89ec.css`, `5b6568268f4e7c11.css`), and grid rule `.AnswersBlock_answers-block__vC9vt { left:10.6770833333% }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<main.home> — `Featured Work & Interactive Showca`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1023px`, `gap: .8125rem`) on desktop and Single-column vertical stack at `390px` viewport width with `20px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<main.home> — `Technical Architecture & Narrative`)**:
   - DOM & Selectors: Landmark `<main class="home">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Kaiku / V2030 1125 K a i k u / V 2 0 3 0 1 1 2 5"*) with `#808080` surface cards, `#d9d9d9` accents, and `nswersBlock_answers-block__items_... { flex-direction:column }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<main.home> — `Technical Architecture & Narrative`)` uses `4px`, `50%`, `.5rem`, `5px` radii, `#d9d9d9` highlights, and assets (0807ff31c16ab04c.css, 1ee6f0f6dd8fb3fa.css, a5188067206b89ec.css).
5. **Colophon & Global Directory Footer (<footer.Footer_footer__2_6CR> — `https://continuance.ai/`)**:
   - DOM & Selectors: Landmark `<footer class="Footer_footer__2_6CR">` anchoring `Continuance - A novel by Chris B` footer links (`Overview · Index · Archive · About · Contact`), copy *"Kaiku / V2030 1125"*, and `#000` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.Footer_footer__2_6CR> — `https://continuance.ai/`)` aligns to `1023px` extracted from `continuance-ai` stylesheet with `20px` lateral canvas padding with `.8125rem` grid gap and attributes (data-precedence="next", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Mapping neural signatures..."*
- Copy Excerpt 2: *"34-year-old researcher fighting to save rare-variant patients the system abandoned"*
- Copy Excerpt 3: *"Kaiku / V2030 1125 K a i k u / V 2 0 3 0 1 1 2 5"*
- Copy Excerpt 4: *"Kaiku / V2030 1125"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.85,0,.15,1)`, `cubic-bezier(.87,0,.13,1)`, `cubic-bezier(.8,0,.2,1)`
- **Extracted Stylesheet Rules (`continuance-ai`)**:
- `kItem_answers-block-item__lottie_... { width:100%;height:100%;position:absolute }`
- `.AnswersBlock_answers-block__vC9vt { left:10.6770833333% }`
- `nswersBlock_answers-block__items_... { flex-direction:column }`
- `wersBlock_answers-block__counter_... { margin-right:0 }`
- `Reveal_mute-button__inner__omo_4:... { position:absolute;top:0;left:0;width:100%;height:100% }`
- **Per-Selector Transition Rules**:
- **Selector `imatedButtonReveal_btn__inner__jJ...`**: `transition: transform .3s ease-out` extracted from `continuance-ai` stylesheet.
- **Selector `imatedButtonReveal_btn__inner__jJ...`**: `transition: transform .3s cubic-bezier(.85,0,.15,1)` extracted from `continuance-ai` stylesheet.
- **Selector `oUEb .AnimatedButtonReveal_cr-obj...`**: `transition: .3s cubic-bezier(.85,0,.15,1)` extracted from `continuance-ai` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.85,0,.15,1)`)**: Governs interactive state transitions across `<header.page>` and `<main.home>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `continuance-ai`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
