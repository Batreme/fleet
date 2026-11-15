---
title: "UI Prompt Blueprint: www-lingers-it_en"
date: 2026-11-15
target: "www-lingers-it_en"
status: analyzed
capture: specimen
archetype: "Light-Substrate Editorial & Modular Grid System (`#777162` canvas, `#ffffff` ink, `#e0ddd7` accent)"
---

# UI Design System & Master Generation Blueprint: www-lingers-it_en

> **Lingers – your hotel in Girlan** (https://www.lingers.it/en) — Lingers is more than a hotel in Girlan. It’s your hideaway that makes you want to stay a little longer. And we can’t wait to welcome you.

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Lingers – your hotel in Girlan** (`https://www.lingers.it/en`). Lingers is more than a hotel in Girlan. It’s your hideaway that makes you want to stay a little longer. And we can’t wait to welcome you.
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#777162` canvas, `#ffffff` ink, `#e0ddd7` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#777162` (`var(--bl-color-primary)` in `:root`) paired with `#ffffff` primary typography and `#e0ddd7` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Cormorant Garamond` for display copy (`Linger a little longer. In our charm`) with `Cinzel` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1024px` container bounds (`gap: .3rem`, padding `8px`) with `cubic-bezier(0,0,0.25,1)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Design Specimen (Offline WebGL/JS Fallback — not live site capture)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×13480px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `1024px` extracted from `www-lingers-it_en` stylesheet.
- **Canvas Lateral Padding & Spacing**: `8px` lateral canvas padding with `.3rem` grid gap.
- **Border Radius Scale**: `2px`, `50%`, `3px`, `8px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1024px`, `gap: .3rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `8px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width: 1024px)`, `@media (max-width: 767px)`, `@media (min-width: 1025px)`, `@media (max-width: 1700px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#777162` | `var(--bl-color-primary)` in `:root` |
| **Primary Typography Ink** | `#ffffff` | `var(--bl-trigger-text)` in `:root` |
| **Elevated Surface / Card Substrate** | `#9f9b91` | `var(--bl-color-secondary)` in `:root` |
| **Interactive Accent / Highlight** | `#e0ddd7` | `.DNA-module__pagination__dot { background-color: #e0ddd7 }` |
| **Secondary / Muted Copy** | `#F7F7F7` | `:after { background: #F7F7F7 }` |
| **Structural Hairline Border** | `#777367` | `a { color: #777367 }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--track-width` | `52px` | Layout / Spatial Grid Token |
| `--track-height` | `28px` | Layout / Spatial Grid Token |
| `--thumb-size` | `23px` | Layout / Spatial Grid Token |
| `--thumb-gap` | `3px` | Layout / Spatial Grid Token |
| `--track-radius` | `999px` | Elevation / Border Token |
| `--vh` | `9px` | Layout / Spatial Grid Token |
| `--bl-size` | `45px` | Layout / Spatial Grid Token |
| `--bl-desktop-top` | `auto` | Design System Custom Token |
| `--bl-desktop-bottom` | `1.5em` | Dimension / Scale Token |
| `--bl-desktop-left` | `auto` | Design System Custom Token |
| `--bl-desktop-right` | `1.5em` | Dimension / Scale Token |
| `--bl-desktop-box-left` | `auto` | Design System Custom Token |
| `--bl-desktop-box-right` | `1.5em` | Dimension / Scale Token |
| `--bl-tablet-top` | `auto` | Design System Custom Token |
| `--bl-tablet-bottom` | `1em` | Dimension / Scale Token |
| `--bl-tablet-left` | `auto` | Design System Custom Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Cormorant Garamond`.
- **Primary Body Stack**: `Cinzel`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`line-height: 1.2`, `letter-spacing: 2.1px`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 1em`, `line-height: 1`, `letter-spacing: 1.8px`).
- **Body Copy**: rule `p` (`font-size: 12px`).
- **Metadata & Navigation Labels**: rule `small` (`font-size: 80%`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0,0,0.25,1)`, `cubic-bezier(0.215,0.61,0.355,1)`, `cubic-bezier(0.17,0.88,0.32,1.28)`.

### Per-Element Transition & Choreography Rules
- **Selector `dule[data-id=Impressions] .DNA-mo...`**: `transition: transform 2s,opacity 2s` extracted from `www-lingers-it_en` stylesheet.
- **Selector `ta-id=Impressions] .DNA-module__i...`**: `transition: background-color .25s` extracted from `www-lingers-it_en` stylesheet.
- **Selector `d=Impressions] .DNA-module__pagin...`**: `transition: background-color .25s` extracted from `www-lingers-it_en` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,0.25,1)`)**: Governs interactive state transitions across `<header.DNA-section>` and `<section.DNA-module>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Lingers – your hotel in Girlan             │
│ ====================================================================== │
│ [ <header.DNA-section>     | DE · IT · EN                           ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.DNA-module>                                 |   │
│ | H1: Linger a little longer. In our charming hotel in...          |   │
│ | Substrate: #777162    | Ink: #ffffff    | Accent: #e0ddd7        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.DNA-module>      ) max-w: 1024px         |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Culinary concept: morning &  |  | Get active at our hotel in G | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .3rem ) | │
│ | [<header.DNA-sectio] -> [<section.DNA-modul] -> [<section.DNA-modul] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.DNA-section>  ) | https://www.lingers.it/en          │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.DNA-section> — `www-lingers-it_en`)**:
   - Landmark `<header class="DNA-section">` hosting `Lingers – your hotel in Girlan` navigation (`DE · IT · EN`), DOM attributes (`data-asset-id="Scss/presets"`, `data-asset-id="Scss/vendors"`, `data-asset-id="Globals/Main"`, `data-asset-id="Sections/Header"`), and stylesheet rule `.DNA-module__wrap { transition:transform 2s,opacity 2s;overflow:hidden }`.
2. **Hero Stage & Focal Lead (<section.DNA-module> — `Linger a little longer. In our cha`)**:
   - Landmark `<section class="DNA-module">` presenting display lead `Linger a little longer. In our charming hotel in...` and copy excerpt *"Lingers Morning & afternoon delights Pool & garden Massages & spo"* over `#777162` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.DNA-module> — `Culinary concept: morning & aftern`)**:
   - Landmark `<section class="DNA-module">` rendering section `Culinary concept: morning & afternoon` with copy *"Morning & afternoon delights"*, asset references (`favicon-96x96.png`, `favicon.svg`, `favicon.ico`, `apple-touch-icon.png`), and grid rule `.DNA-module__upper { padding-left:4em;padding-right:4em;max-width:calc(102.4em + 4em + 4em) }`.
4. **Interactive Detail & Feature Matrix (<section.DNA-module> — `Get active at our hotel in Girlan `)**:
   - Landmark `<section class="DNA-module">` framing `Get active at our hotel in Girlan in South Tyrol` and `Wellness at our hotel in Girlan in South Tyrol` (*"The taste of Lingers"*) with `#9f9b91` surface cards, `#e0ddd7` accents, and `.DNA-module__list { padding-left:0em;padding-right:0em;max-width:calc(102.4em + 0em + 0em) }`.
5. **Colophon & Global Directory Footer (<footer.DNA-section> — `https://www.lingers.it/en`)**:
   - Landmark `<footer class="DNA-section">` anchoring `Lingers – your hotel in Girlan` footer links (`DE · IT · EN`), copy *"Location & arrival"*, and `#777367` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-lingers-it_en (Lingers – your hotel in Girlan)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-lingers-it_en` (**Lingers – your hotel in Girlan** — `https://www.lingers.it/en`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#777162` canvas, `#ffffff` ink, `#e0ddd7` accent).
- **Identity & Domain Context**: Lingers is more than a hotel in Girlan. It’s your hideaway that makes you want to stay a little longer. And we can’t wait to welcome you.
- **Primary Substrate**: `#777162` (`var(--bl-color-primary)` in `:root`), **Primary Ink**: `#ffffff`, **Accent / Highlight**: `#e0ddd7`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#777162` (`var(--bl-color-primary)` in `:root`) paired with `#ffffff` primary typography and `#e0ddd7` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Cormorant Garamond` for display copy (`Linger a little longer. In our charm`) with `Cinzel` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1024px` container bounds (`gap: .3rem`, padding `8px`) with `cubic-bezier(0,0,0.25,1)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-lingers-it_en` in your global stylesheet:

:root {
  /* Lingers – your hotel in Girlan (www-lingers-it_en) — Ground-Truth Extracted CSS Variables */
  --track-width: 52px; /* Layout / Spatial Grid Token (www-lingers-it_en) */
  --track-height: 28px; /* Layout / Spatial Grid Token (www-lingers-it_en) */
  --thumb-size: 23px; /* Layout / Spatial Grid Token (www-lingers-it_en) */
  --thumb-gap: 3px; /* Layout / Spatial Grid Token (www-lingers-it_en) */
  --track-radius: 999px; /* Elevation / Border Token (www-lingers-it_en) */
  --vh: 9px; /* Layout / Spatial Grid Token (www-lingers-it_en) */
  --bl-size: 45px; /* Layout / Spatial Grid Token (www-lingers-it_en) */
  --bl-desktop-top: auto; /* Design System Custom Token (www-lingers-it_en) */
  --bl-desktop-bottom: 1.5em; /* Dimension / Scale Token (www-lingers-it_en) */
  --bl-desktop-left: auto; /* Design System Custom Token (www-lingers-it_en) */
  --bl-desktop-right: 1.5em; /* Dimension / Scale Token (www-lingers-it_en) */
  --bl-desktop-box-left: auto; /* Design System Custom Token (www-lingers-it_en) */
  --bl-desktop-box-right: 1.5em; /* Dimension / Scale Token (www-lingers-it_en) */
  --bl-tablet-top: auto; /* Design System Custom Token (www-lingers-it_en) */
  --bl-tablet-bottom: 1em; /* Dimension / Scale Token (www-lingers-it_en) */
  --bl-tablet-left: auto; /* Design System Custom Token (www-lingers-it_en) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#777162` — grounded in `var(--bl-color-primary)` in `:root`
- **Primary Typography Ink**: `#ffffff` — grounded in `var(--bl-trigger-text)` in `:root`
- **Elevated Surface / Card Substrate**: `#9f9b91` — grounded in `var(--bl-color-secondary)` in `:root`
- **Interactive Accent / Highlight**: `#e0ddd7` — grounded in `.DNA-module__pagination__dot { background-color: #e0ddd7 }`
- **Secondary / Muted Copy**: `#F7F7F7` — grounded in `:after { background: #F7F7F7 }`
- **Structural Hairline Border**: `#777367` — grounded in `a { color: #777367 }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×13480px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1024px` extracted from `www-lingers-it_en` stylesheet
- **Padding & Gutters**: `8px` lateral canvas padding with `.3rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1024px`, `gap: .3rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `8px` horizontal padding
- **Media Queries**: `@media (max-width: 1024px)`, `@media (max-width: 767px)`, `@media (min-width: 1025px)`, `@media (max-width: 1700px)`
- **Corner Radii**: `2px`, `50%`, `3px`, `8px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Cormorant Garamond`
- **Body Font Stack**: `Cinzel`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: rule `h1` (`line-height: 1.2`, `letter-spacing: 2.1px`)
- **H2 Section Rule**: rule `h2` (`font-size: 1em`, `line-height: 1`, `letter-spacing: 1.8px`)
- **Body Copy Rule**: rule `p` (`font-size: 12px`)
- **Metadata & Index Rule**: rule `small` (`font-size: 80%`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-lingers-it_en` (`Lingers – your hotel in Girlan`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.DNA-section> — `www-lingers-it_en`)**:
   - DOM & Selectors: Landmark `<header class="DNA-section">` hosting `Lingers – your hotel in Girlan` navigation (`DE · IT · EN`), DOM attributes (`data-asset-id="Scss/presets"`, `data-asset-id="Scss/vendors"`, `data-asset-id="Globals/Main"`, `data-asset-id="Sections/Header"`), and stylesheet rule `.DNA-module__wrap { transition:transform 2s,opacity 2s;overflow:hidden }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.DNA-section> — `www-lingers-it_en`)` (`www-lingers-it_en`) adapts across `@media (max-width: 1024px)`, `@media (max-width: 767px)`, `@media (min-width: 1025px)`, `@media (max-width: 1700px)` with `cubic-bezier(0,0,0.25,1)`, `cubic-bezier(0.215,0.61,0.355,1)`, `cubic-bezier(0.17,0.88,0.32,1.28)` transitions and links `DE · IT · EN`.
2. **Hero Stage & Focal Lead (<section.DNA-module> — `Linger a little longer. In our cha`)**:
   - DOM & Selectors: Landmark `<section class="DNA-module">` presenting display lead `Linger a little longer. In our charming hotel in...` and copy excerpt *"Lingers Morning & afternoon delights Pool & garden Massages & spo"* over `#777162` canvas and `#ffffff` ink.
   - Responsive Contract: Hero stage (`1440×13480px` desktop / `390×2400px` mobile) sets `#777162` background with `#ffffff` headline `Linger a little longer. In our charming hotel in...`.
3. **Primary Showcase & Content Grid (<section.DNA-module> — `Culinary concept: morning & aftern`)**:
   - DOM & Selectors: Landmark `<section class="DNA-module">` rendering section `Culinary concept: morning & afternoon` with copy *"Morning & afternoon delights"*, asset references (`favicon-96x96.png`, `favicon.svg`, `favicon.ico`, `apple-touch-icon.png`), and grid rule `.DNA-module__upper { padding-left:4em;padding-right:4em;max-width:calc(102.4em + 4em + 4em) }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.DNA-module> — `Culinary concept: morning & aftern`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1024px`, `gap: .3rem`) on desktop and Single-column vertical stack at `390px` viewport width with `8px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.DNA-module> — `Get active at our hotel in Girlan `)**:
   - DOM & Selectors: Landmark `<section class="DNA-module">` framing `Get active at our hotel in Girlan in South Tyrol` and `Wellness at our hotel in Girlan in South Tyrol` (*"The taste of Lingers"*) with `#9f9b91` surface cards, `#e0ddd7` accents, and `.DNA-module__list { padding-left:0em;padding-right:0em;max-width:calc(102.4em + 0em + 0em) }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.DNA-module> — `Get active at our hotel in Girlan `)` uses `2px`, `50%`, `3px`, `8px` radii, `#e0ddd7` highlights, and assets (favicon-96x96.png, favicon.svg, favicon.ico).
5. **Colophon & Global Directory Footer (<footer.DNA-section> — `https://www.lingers.it/en`)**:
   - DOM & Selectors: Landmark `<footer class="DNA-section">` anchoring `Lingers – your hotel in Girlan` footer links (`DE · IT · EN`), copy *"Location & arrival"*, and `#777367` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.DNA-section> — `https://www.lingers.it/en`)` aligns to `1024px` extracted from `www-lingers-it_en` stylesheet with `8px` lateral canvas padding with `.3rem` grid gap and attributes (data-asset-id="Scss/presets", data-asset-id="Scss/vendors", data-asset-id="Globals/Main").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Lingers Morning & afternoon delights Pool & garden Massages & sport The taste of L..."*
- Copy Excerpt 2: *"Morning & afternoon delights"*
- Copy Excerpt 3: *"The taste of Lingers"*
- Copy Excerpt 4: *"Location & arrival"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0,0,0.25,1)`, `cubic-bezier(0.215,0.61,0.355,1)`, `cubic-bezier(0.17,0.88,0.32,1.28)`
- **Extracted Stylesheet Rules (`www-lingers-it_en`)**:
- `.DNA-module__wrap { transition:transform 2s,opacity 2s;overflow:hidden }`
- `.DNA-module__upper { padding-left:4em;padding-right:4em;max-width:calc(102.4em + 4em + 4em) }`
- `.DNA-module__list { padding-left:0em;padding-right:0em;max-width:calc(102.4em + 0em + 0em) }`
- `.DNA-module__list__wrap { margin:0 -2.5em;display:flex;flex-wrap:wrap }`
- `.DNA-module__item { padding:0 2.5em;width:53.5em;cursor:pointer }`
- **Per-Selector Transition Rules**:
- **Selector `dule[data-id=Impressions] .DNA-mo...`**: `transition: transform 2s,opacity 2s` extracted from `www-lingers-it_en` stylesheet.
- **Selector `ta-id=Impressions] .DNA-module__i...`**: `transition: background-color .25s` extracted from `www-lingers-it_en` stylesheet.
- **Selector `d=Impressions] .DNA-module__pagin...`**: `transition: background-color .25s` extracted from `www-lingers-it_en` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,0.25,1)`)**: Governs interactive state transitions across `<header.DNA-section>` and `<section.DNA-module>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-lingers-it_en`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
