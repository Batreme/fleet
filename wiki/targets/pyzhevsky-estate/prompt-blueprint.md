---
title: "UI Prompt Blueprint: pyzhevsky-estate"
date: 2026-11-15
target: "pyzhevsky-estate"
status: analyzed
capture: dom
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#12100e` / `#75736d`)"
---

# UI Design System & Master Generation Blueprint: pyzhevsky-estate

> **Pyzhevsky — official website of a deluxe residence five minutes from the...** (https://pyzhevsky.estate/) — An intimate residential project. Apartments in the historic centre. Panoramic views and original architecture.

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Pyzhevsky — official website of a deluxe residence five minutes from the...** (`https://pyzhevsky.estate/`). An intimate residential project. Apartments in the historic centre. Panoramic views and original architecture.
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#12100e` / `#75736d`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#12100e` (`var(--c-black)` in `:root`) paired with `#fff` primary typography and `#75736d` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Garamond Light` for display copy (`Pyzhevsky`) with `Halvar Breitschrift` and `Consolas`.
  - **Calibrated Spatial Grid & Motion**: Combines `667px` container bounds (`gap: 3px`, padding `10px`) with `cubic-bezier(.25,.74,.22,.99)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `667px` extracted from `pyzhevsky-estate` stylesheet.
- **Canvas Lateral Padding & Spacing**: `10px` lateral canvas padding with `3px` grid gap.
- **Border Radius Scale**: `3px`, `6px`, `var(--btn-rx)`, `50%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 667px`, `gap: 3px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `10px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:568px) and (max-width:667px) and (max-aspect-r...`, `@media (min-width:1px)`, `@media (min-aspect-ratio:13/9) and (min-width:1px),(min-width:56...`, `@media (min-width:1440px) and (min-width:1px),(min-width:980px)...`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#12100e` | `var(--c-black)` in `:root` |
| **Primary Typography Ink** | `#2f2b27` | `var(--c-black-hover)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff` | `var(--c-white)` in `:root` |
| **Interactive Accent / Highlight** | `#75736d` | `var(--c-dark-beige)` in `:root` |
| **Secondary / Muted Copy** | `#88857e` | `var(--c-dark-beige-hover)` in `:root` |
| **Structural Hairline Border** | `#bdb6a9` | `var(--c-beige)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
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

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Garamond Light`.
- **Primary Body Stack**: `Halvar Breitschrift`.
- **Technical / Metadata Stack**: `Consolas`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `,h1` (`font-size: 2em`).
- **Section Heading (`H2`)**: rule `,h2` (`font-weight: 400`).
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `2em`, `1em`, `80%`, `75%`, `100%`).
- **Metadata & Navigation Labels**: CSS variables `--t-small: var(--c-pale-dark)`, `--t-small-rgb: var(--c-pale-dark-rgb)`, `--t-button-color-small-text: var(--t-small)`; rule `,small` (`font-weight: 500`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.25,.74,.22,.99)`, `cubic-bezier(.7,0,.4,1)`, `cubic-bezier(0.7,0,0.4,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `vig-smooth-scroll::part(scrollbar)`**: `transition: .4s` extracted from `pyzhevsky-estate` stylesheet.
- **Selector `--checkmark .form-control-radio__...`**: `transition: .6s` extracted from `pyzhevsky-estate` stylesheet.
- **Selector `a.link-text:where(:not(.btn))`**: `transition: .8s` extracted from `pyzhevsky-estate` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.25,.74,.22,.99)`)**: Governs interactive state transitions across `<header.header>` and `<section.section>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Pyzhevsky — official website of a deluxe r │
│ ====================================================================== │
│ [ <header.header>          | Select an apartment · 3D area map      ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.section>                                    |   │
│ | H1: Pyzhevsky                                                    |   │
│ | Substrate: #12100e    | Ink: #fff       | Accent: #75736d        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.section>         ) max-w: 667px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Facade                       |  | Views                        | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 3px   ) | │
│ | [<header.header>] -> [<section.section>] -> [<section.section>] |    │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.section>      ) | https://pyzhevsky.estate/          │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
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

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: pyzhevsky-estate (Pyzhevsky — official website of a deluxe residence five minutes from the...)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `pyzhevsky-estate` (**Pyzhevsky — official website of a deluxe residence five minutes from the...** — `https://pyzhevsky.estate/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#12100e` / `#75736d`).
- **Identity & Domain Context**: An intimate residential project. Apartments in the historic centre. Panoramic views and original architecture.
- **Primary Substrate**: `#12100e` (`var(--c-black)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#75736d`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#12100e` (`var(--c-black)` in `:root`) paired with `#fff` primary typography and `#75736d` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Garamond Light` for display copy (`Pyzhevsky`) with `Halvar Breitschrift` and `Consolas`.
  - **Calibrated Spatial Grid & Motion**: Combines `667px` container bounds (`gap: 3px`, padding `10px`) with `cubic-bezier(.25,.74,.22,.99)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `pyzhevsky-estate` in your global stylesheet:

:root {
  /* Pyzhevsky — official website of a deluxe residence five minutes from the... (pyzhevsky-estate) — Ground-Truth Extracted CSS Variables */
  --text-box-edge: cap; /* Typography Ink Token (pyzhevsky-estate) */
  --baseline-size: 1cap; /* Layout / Spatial Grid Token (pyzhevsky-estate) */
  --fos: -0.1365em; /* Dimension / Scale Token (pyzhevsky-estate) */
  --foe: -0.1635em; /* Dimension / Scale Token (pyzhevsky-estate) */
  --lh: var(--xxxxl,1.8em) var(--n-xxxxl,1.5em); /* Dimension / Scale Token (pyzhevsky-estate) */
  --scale-px: 1px; /* Dimension / Scale Token (pyzhevsky-estate) */
  --scale-rem: 1rem; /* Dimension / Scale Token (pyzhevsky-estate) */
  --scale-em: 1em; /* Dimension / Scale Token (pyzhevsky-estate) */
  --scale-text-px: 1px; /* Typography Ink Token (pyzhevsky-estate) */
  --scale-text-rem: 1rem; /* Typography Ink Token (pyzhevsky-estate) */
  --scale-text-em: 1em; /* Typography Ink Token (pyzhevsky-estate) */
  --scale-none-px: 1px; /* Dimension / Scale Token (pyzhevsky-estate) */
  --scale-none-rem: 1rem; /* Dimension / Scale Token (pyzhevsky-estate) */
  --n-sm: initial; /* Design System Custom Token (pyzhevsky-estate) */
  --n-md: initial; /* Design System Custom Token (pyzhevsky-estate) */
  --n-lg: initial; /* Design System Custom Token (pyzhevsky-estate) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#12100e` — grounded in `var(--c-black)` in `:root`
- **Primary Typography Ink**: `#2f2b27` — grounded in `var(--c-black-hover)` in `:root`
- **Elevated Surface / Card Substrate**: `#fff` — grounded in `var(--c-white)` in `:root`
- **Interactive Accent / Highlight**: `#75736d` — grounded in `var(--c-dark-beige)` in `:root`
- **Secondary / Muted Copy**: `#88857e` — grounded in `var(--c-dark-beige-hover)` in `:root`
- **Structural Hairline Border**: `#bdb6a9` — grounded in `var(--c-beige)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `667px` extracted from `pyzhevsky-estate` stylesheet
- **Padding & Gutters**: `10px` lateral canvas padding with `3px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 667px`, `gap: 3px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `10px` horizontal padding
- **Media Queries**: `@media (min-width:568px) and (max-width:667px) and (max-aspect-r...`, `@media (min-width:1px)`, `@media (min-aspect-ratio:13/9) and (min-width:1px),(min-width:56...`, `@media (min-width:1440px) and (min-width:1px),(min-width:980px)...`
- **Corner Radii**: `3px`, `6px`, `var(--btn-rx)`, `50%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Garamond Light`
- **Body Font Stack**: `Halvar Breitschrift`
- **Monospace / Technical Font Stack**: `Consolas`
- **H1 Display Rule**: rule `,h1` (`font-size: 2em`)
- **H2 Section Rule**: rule `,h2` (`font-weight: 400`)
- **Body Copy Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `2em`, `1em`, `80%`, `75%`, `100%`)
- **Metadata & Index Rule**: CSS variables `--t-small: var(--c-pale-dark)`, `--t-small-rgb: var(--c-pale-dark-rgb)`, `--t-button-color-small-text: var(--t-small)`; rule `,small` (`font-weight: 500`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `pyzhevsky-estate` (`Pyzhevsky — official website of a deluxe residence five minutes from the...`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.header> — `pyzhevsky-estate`)**:
   - DOM & Selectors: Landmark `<header class="header is-hidden--print">` hosting `Pyzhevsky — official website of a de` navigation (`Select an apartment · 3D area map`), DOM attributes (`data-barba="wrapper"`, `data-nosnippet`, `data-plugin="preloader"`, `data-preloader-animation-name-in="preloader-in"`), and stylesheet rule `html { line-height:1.15;-webkit-text-size-adjust:100% }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.header> — `pyzhevsky-estate`)` (`pyzhevsky-estate`) adapts across `@media (min-width:568px) and (max-width:667px) and (max-aspect-r...`, `@media (min-width:1px)`, `@media (min-aspect-ratio:13/9) and (min-width:1px),(min-width:56...`, `@media (min-width:1440px) and (min-width:1px),(min-width:980px)...` with `cubic-bezier(.25,.74,.22,.99)`, `cubic-bezier(.7,0,.4,1)`, `cubic-bezier(0.7,0,0.4,1)` transitions and links `Select an apartment · 3D area map`.
2. **Hero Stage & Focal Lead (<section.section> — `Pyzhevsky`)**:
   - DOM & Selectors: Landmark `<section class="section l-intro-section">` presenting display lead `Pyzhevsky` and copy excerpt *"Skip to main content"* over `#12100e` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#12100e` background with `#fff` headline `Pyzhevsky`.
3. **Primary Showcase & Content Grid (<section.section> — `Facade`)**:
   - DOM & Selectors: Landmark `<section class="section ui-dark">` rendering section `Facade` with copy *"A d e l u x e p r o j e c t i n t h e h i s t o r i c q u a r t e"*, asset references (`storage.googleapis.com`, `itc-garamond_light.woff2`, `Halvar-Breitschrift-Regular-Web.w...`, `Halvar-Breitschrift-Medium-Web.woff2`), and grid rule `pre { font-family:monospace,monospace;font-size:1em }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.section> — `Facade`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 667px`, `gap: 3px`) on desktop and Single-column vertical stack at `390px` viewport width with `10px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.section> — `Views`)**:
   - DOM & Selectors: Landmark `<section class="section section--top-2">` framing `Views` and `Location` (*"Restrained, assured, timeless — they put the city on pause, so al"*) with `#fff` surface cards, `#75736d` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.section> — `Views`)` uses `3px`, `6px`, `var(--btn-rx)`, `50%` radii, `#75736d` highlights, and assets (storage.googleapis.com, itc-garamond_light.woff2, Halvar-Breitschrift-Regular-Web.w...).
5. **Colophon & Global Directory Footer (<footer.section> — `https://pyzhevsky.estate/`)**:
   - DOM & Selectors: Landmark `<footer class="section section--no-overflow">` anchoring `Pyzhevsky — official website of ` footer links (`Select an apartment · 3D area map`), copy *"The minimalist form of the three buildings draws on the sign"*, and `#bdb6a9` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.section> — `https://pyzhevsky.estate/`)` aligns to `667px` extracted from `pyzhevsky-estate` stylesheet with `10px` lateral canvas padding with `3px` grid gap and attributes (data-barba="wrapper", data-nosnippet, data-plugin="preloader").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Skip to main content"*
- Copy Excerpt 2: *"A d e l u x e p r o j e c t i n t h e h i s t o r i c q u a r t e r"*
- Copy Excerpt 3: *"Restrained, assured, timeless — they put the city on pause, so all that matters ca..."*
- Copy Excerpt 4: *"The minimalist form of the three buildings draws on the signature archetypes of th..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.25,.74,.22,.99)`, `cubic-bezier(.7,0,.4,1)`, `cubic-bezier(0.7,0,0.4,1)`
- **Extracted Stylesheet Rules (`pyzhevsky-estate`)**:
- `html { line-height:1.15;-webkit-text-size-adjust:100% }`
- `pre { font-family:monospace,monospace;font-size:1em }`
- `strong { font-weight:bolder }`
- `samp { font-family:monospace,monospace;font-size:1em }`
- `small { font-size:80% }`
- **Per-Selector Transition Rules**:
- **Selector `vig-smooth-scroll::part(scrollbar)`**: `transition: .4s` extracted from `pyzhevsky-estate` stylesheet.
- **Selector `--checkmark .form-control-radio__...`**: `transition: .6s` extracted from `pyzhevsky-estate` stylesheet.
- **Selector `a.link-text:where(:not(.btn))`**: `transition: .8s` extracted from `pyzhevsky-estate` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.25,.74,.22,.99)`)**: Governs interactive state transitions across `<header.header>` and `<section.section>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `pyzhevsky-estate`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
