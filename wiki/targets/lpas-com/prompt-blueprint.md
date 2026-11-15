---
title: "UI Prompt Blueprint: lpas-com"
date: 2026-11-15
target: "[[overview|lpas-com]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#111` ink, `#eee` accent)"
---

# UI Design System & Master Generation Blueprint: lpas-com

> **LPAS - Architecture and Interiors** (https://lpas.com/) — Clear Process. Creative Results. Human-centered. Always Curious. At LPAS, we design with people at the center and purpose at every turn.

![Desktop Viewport Capture (1440x9363)](file:///root/projects/fleet/wiki/targets/lpas-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **LPAS - Architecture and Interiors** (`https://lpas.com/`). Clear Process. Creative Results. Human-centered. Always Curious. At LPAS, we design with people at the center and purpose at every turn.
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#111` ink, `#eee` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`body { color: #fff }`) paired with `#111` primary typography and `#eee` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Aeonik` for display copy (`Sacramento`) with `Aeonik` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `100vw` container bounds (`gap: 1rem`, padding `1px`) with `cubic-bezier(.14,.83,.4,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/lpas-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×9363px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `100vw` extracted from `lpas-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `1px` lateral canvas padding with `1rem` grid gap.
- **Border Radius Scale**: `50%`, `.2rem`, `1.3rem`, `.5rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 100vw`, `gap: 1rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `1px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width: 480px)`, `@media (min-width: 768px)`, `@media (min-width: 1280px)`, `@media (min-width: 2150px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `body { color: #fff }` |
| **Primary Typography Ink** | `#111` | `main { color: #111 }` |
| **Elevated Surface / Card Substrate** | `#393a3b` | `.template__title:before { background-color: #393a3b }` |
| **Interactive Accent / Highlight** | `#eee` | `.template code { background-color: #eee }` |
| **Secondary / Muted Copy** | `#0000` | `#slideOut-overlay::backdrop { background-color: #0000 }` |
| **Structural Hairline Border** | `#262626` | `.slideOut__aside { background-color: #262626 }` |
| **Variable Token (`--swiper-theme-color`)** | `#007aff` | `var(--swiper-theme-color)` in stylesheet |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--row-gap` | `0` | Layout / Spatial Grid Token |
| `--column-gap` | `1rem` | Layout / Spatial Grid Token |
| `--xxlSpace` | `8.5rem` | Layout / Spatial Grid Token |
| `--marketMainColor` | `rgb(98, 86, 83)` | Brand / Palette Token |
| `--marketSecondaryColor` | `rgb(123, 105, 100)` | Brand / Palette Token |
| `--marketContentColor` | `rgb(255, 255, 255)` | Brand / Palette Token |
| `--marketContentContrast` | `rgb(38, 38, 38)` | Color / Atmospheric Token |
| `--scrollbarWidth` | `0px` | Layout / Spatial Grid Token |
| `--ctaBarHeight` | `0px` | Brand / Palette Token |
| `--viewportWidth` | `calc(100vw - var(--scrollbarWidth))` | Layout / Spatial Grid Token |
| `--cut` | `2rem` | Dimension / Scale Token |
| `--sticky-offset` | `505px` | Dimension / Scale Token |
| `--swiper-theme-color` | `#007aff` | Brand / Palette Token |
| `--swiper-preloader-color` | `#fff` | Brand / Palette Token |
| `--lpas-com-bg` | `#fff` | Canvas Substrate (from `body { color: #fff }`) |
| `--lpas-com-ink` | `#111` | Primary Typography Ink (stylesheet-derived) |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Aeonik`.
- **Primary Body Stack**: `Aeonik`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `100%`, `62.5%`, `clamp(4.6rem,.25rem + 5.6640625vw...`, `clamp(4.4rem,.2857142857rem + 5.3...`, `clamp(3.2rem,-2.9714285714rem + 8...`).
- **Section Heading (`H2`)**: rule `h2` (`line-height: 110%`, `font-weight: 400`).
- **Body Copy**: rule `,body` (`line-height: 135%`, `font-weight: 400`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `100%`, `62.5%`, `clamp(4.6rem,.25rem + 5.6640625vw...`, `clamp(4.4rem,.2857142857rem + 5.3...`, `clamp(3.2rem,-2.9714285714rem + 8...`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.14,.83,.4,1)`, `cubic-bezier(0,0,.13,.99)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `:focus-visible`**: `transition: none` extracted from `lpas-com` stylesheet.
- **Selector `.is-previous-container:after`**: `transition: opacity .5s ease` extracted from `lpas-com` stylesheet.
- **Selector `.is-previous-container.is-darkene...`**: `transition: opacity .5s ease,backdrop-filter .6s ease` extracted from `lpas-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.14,.83,.4,1)`)**: Governs interactive state transitions across `<header.mainHeader>` and `<section.blockIntroGeneral>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — LPAS - Architecture and Interiors          │
│ ====================================================================== │
│ [ <header.mainHeader>      | Housing · Interiors · Higher Education ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.homeHero>                                   |   │
│ | H1: Sacramento                                                   |   │
│ | Substrate: #fff       | Ink: #111       | Accent: #eee           |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.blockIntroGeneral) max-w: 100vw          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Oakland                      |  | We’re a process driven archi | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 1rem  ) | │
│ | [<header.mainHeader] -> [<section.homeHero>] -> [<section.blockIntr] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.navigationFoot) | https://lpas.com/                  │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.mainHeader> — `lpas-com`)**:
   - Landmark `<header class="mainHeader">` hosting `LPAS - Architecture and Interiors` navigation (`Housing · Interiors · Higher Education · Civic · Commercial`), DOM attributes (`data-browser="Chrome"`, `data-istoch="false"`, `data-logocolor="light"`, `data-first-visit="true"`), and stylesheet rule `video { margin:0;padding:0;border:0;font-size:100%;font:inherit;vertical-align:b... }`.
2. **Hero Stage & Focal Lead (<section.homeHero> — `Sacramento`)**:
   - Landmark `<section class="homeHero">` presenting display lead `Sacramento` and copy excerpt *"723 S Street, Suite 150 Sacramento, CA 95811"* over `#fff` canvas and `#111` ink.
3. **Primary Showcase & Content Grid (<section.blockIntroGeneral> — `Oakland`)**:
   - Landmark `<section class="blockIntroGeneral">` rendering section `Oakland` with copy *"10 Clay Street, Suite 250 Oakland, CA 94607"*, asset references (`main-DN-9Dm9S.css`, `swup-config-DoT-9FzL.js`, `preloader-CQAQSTAa.js`, `lenisSmooth-BjXMsNId.js`), and grid rule `section { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.blockProjectsHighlight> — `We’re a process driven architectur`)**:
   - Landmark `<section class="blockProjectsHighlight">` framing `We’re a process driven architecture and interior...` and `Housing` (*"Architecture + Interiors"*) with `#393a3b` surface cards, `#eee` accents, and `body { line-height:1 }`.
5. **Colophon & Global Directory Footer (<footer.navigationFooter> — `https://lpas.com/`)**:
   - Landmark `<footer class="navigationFooter">` anchoring `LPAS - Architecture and Interior` footer links (`Housing · Interiors · Higher Education · Civic · Commercial`), copy *"A Market-Focused Approach"*, and `#262626` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: lpas-com (LPAS - Architecture and Interiors)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `lpas-com` (**LPAS - Architecture and Interiors** — `https://lpas.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#111` ink, `#eee` accent).
- **Identity & Domain Context**: Clear Process. Creative Results. Human-centered. Always Curious. At LPAS, we design with people at the center and purpose at every turn.
- **Primary Substrate**: `#fff` (`body { color: #fff }`), **Primary Ink**: `#111`, **Accent / Highlight**: `#eee`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`body { color: #fff }`) paired with `#111` primary typography and `#eee` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Aeonik` for display copy (`Sacramento`) with `Aeonik` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `100vw` container bounds (`gap: 1rem`, padding `1px`) with `cubic-bezier(.14,.83,.4,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `lpas-com` in your global stylesheet:

:root {
  /* LPAS - Architecture and Interiors (lpas-com) — Ground-Truth Extracted CSS Variables */
  --row-gap: 0; /* Layout / Spatial Grid Token (lpas-com) */
  --column-gap: 1rem; /* Layout / Spatial Grid Token (lpas-com) */
  --xxlSpace: 8.5rem; /* Layout / Spatial Grid Token (lpas-com) */
  --marketMainColor: rgb(98, 86, 83); /* Brand / Palette Token (lpas-com) */
  --marketSecondaryColor: rgb(123, 105, 100); /* Brand / Palette Token (lpas-com) */
  --marketContentColor: rgb(255, 255, 255); /* Brand / Palette Token (lpas-com) */
  --marketContentContrast: rgb(38, 38, 38); /* Color / Atmospheric Token (lpas-com) */
  --scrollbarWidth: 0px; /* Layout / Spatial Grid Token (lpas-com) */
  --ctaBarHeight: 0px; /* Brand / Palette Token (lpas-com) */
  --viewportWidth: calc(100vw - var(--scrollbarWidth)); /* Layout / Spatial Grid Token (lpas-com) */
  --cut: 2rem; /* Dimension / Scale Token (lpas-com) */
  --sticky-offset: 505px; /* Dimension / Scale Token (lpas-com) */
  --swiper-theme-color: #007aff; /* Brand / Palette Token (lpas-com) */
  --swiper-preloader-color: #fff; /* Brand / Palette Token (lpas-com) */
  --lpas-com-bg: #fff; /* Canvas Substrate (from `body { color: #fff }`) (lpas-com) */
  --lpas-com-ink: #111; /* Primary Typography Ink (stylesheet-derived) (lpas-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fff` — grounded in `body { color: #fff }`
- **Primary Typography Ink**: `#111` — grounded in `main { color: #111 }`
- **Elevated Surface / Card Substrate**: `#393a3b` — grounded in `.template__title:before { background-color: #393a3b }`
- **Interactive Accent / Highlight**: `#eee` — grounded in `.template code { background-color: #eee }`
- **Secondary / Muted Copy**: `#0000` — grounded in `#slideOut-overlay::backdrop { background-color: #0000 }`
- **Structural Hairline Border**: `#262626` — grounded in `.slideOut__aside { background-color: #262626 }`
- **Variable Token (`--swiper-theme-color`)**: `#007aff` — grounded in `var(--swiper-theme-color)` in stylesheet

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×9363px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `100vw` extracted from `lpas-com` stylesheet
- **Padding & Gutters**: `1px` lateral canvas padding with `1rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 100vw`, `gap: 1rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `1px` horizontal padding
- **Media Queries**: `@media (min-width: 480px)`, `@media (min-width: 768px)`, `@media (min-width: 1280px)`, `@media (min-width: 2150px)`
- **Corner Radii**: `50%`, `.2rem`, `1.3rem`, `.5rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Aeonik`
- **Body Font Stack**: `Aeonik`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `100%`, `62.5%`, `clamp(4.6rem,.25rem + 5.6640625vw...`, `clamp(4.4rem,.2857142857rem + 5.3...`, `clamp(3.2rem,-2.9714285714rem + 8...`)
- **H2 Section Rule**: rule `h2` (`line-height: 110%`, `font-weight: 400`)
- **Body Copy Rule**: rule `,body` (`line-height: 135%`, `font-weight: 400`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `100%`, `62.5%`, `clamp(4.6rem,.25rem + 5.6640625vw...`, `clamp(4.4rem,.2857142857rem + 5.3...`, `clamp(3.2rem,-2.9714285714rem + 8...`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `lpas-com` (`LPAS - Architecture and Interiors`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.mainHeader> — `lpas-com`)**:
   - DOM & Selectors: Landmark `<header class="mainHeader">` hosting `LPAS - Architecture and Interiors` navigation (`Housing · Interiors · Higher Education · Civic · Commercial`), DOM attributes (`data-browser="Chrome"`, `data-istoch="false"`, `data-logocolor="light"`, `data-first-visit="true"`), and stylesheet rule `video { margin:0;padding:0;border:0;font-size:100%;font:inherit;vertical-align:b... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.mainHeader> — `lpas-com`)` (`lpas-com`) adapts across `@media (min-width: 480px)`, `@media (min-width: 768px)`, `@media (min-width: 1280px)`, `@media (min-width: 2150px)` with `cubic-bezier(.14,.83,.4,1)`, `cubic-bezier(0,0,.13,.99)`, `cubic-bezier(.4,0,.2,1)` transitions and links `Housing · Interiors · Higher Education · Civic · Commercial`.
2. **Hero Stage & Focal Lead (<section.homeHero> — `Sacramento`)**:
   - DOM & Selectors: Landmark `<section class="homeHero">` presenting display lead `Sacramento` and copy excerpt *"723 S Street, Suite 150 Sacramento, CA 95811"* over `#fff` canvas and `#111` ink.
   - Responsive Contract: Hero stage (`1440×9363px` desktop / `390×2400px` mobile) sets `#fff` background with `#111` headline `Sacramento`.
3. **Primary Showcase & Content Grid (<section.blockIntroGeneral> — `Oakland`)**:
   - DOM & Selectors: Landmark `<section class="blockIntroGeneral">` rendering section `Oakland` with copy *"10 Clay Street, Suite 250 Oakland, CA 94607"*, asset references (`main-DN-9Dm9S.css`, `swup-config-DoT-9FzL.js`, `preloader-CQAQSTAa.js`, `lenisSmooth-BjXMsNId.js`), and grid rule `section { display:block }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.blockIntroGeneral> — `Oakland`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 100vw`, `gap: 1rem`) on desktop and Single-column vertical stack at `390px` viewport width with `1px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.blockProjectsHighlight> — `We’re a process driven architectur`)**:
   - DOM & Selectors: Landmark `<section class="blockProjectsHighlight">` framing `We’re a process driven architecture and interior...` and `Housing` (*"Architecture + Interiors"*) with `#393a3b` surface cards, `#eee` accents, and `body { line-height:1 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.blockProjectsHighlight> — `We’re a process driven architectur`)` uses `50%`, `.2rem`, `1.3rem`, `.5rem` radii, `#eee` highlights, and assets (main-DN-9Dm9S.css, swup-config-DoT-9FzL.js, preloader-CQAQSTAa.js).
5. **Colophon & Global Directory Footer (<footer.navigationFooter> — `https://lpas.com/`)**:
   - DOM & Selectors: Landmark `<footer class="navigationFooter">` anchoring `LPAS - Architecture and Interior` footer links (`Housing · Interiors · Higher Education · Civic · Commercial`), copy *"A Market-Focused Approach"*, and `#262626` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.navigationFooter> — `https://lpas.com/`)` aligns to `100vw` extracted from `lpas-com` stylesheet with `1px` lateral canvas padding with `1rem` grid gap and attributes (data-browser="Chrome", data-istoch="false", data-logocolor="light").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"723 S Street, Suite 150 Sacramento, CA 95811"*
- Copy Excerpt 2: *"10 Clay Street, Suite 250 Oakland, CA 94607"*
- Copy Excerpt 3: *"Architecture + Interiors"*
- Copy Excerpt 4: *"A Market-Focused Approach"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.14,.83,.4,1)`, `cubic-bezier(0,0,.13,.99)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`lpas-com`)**:
- `video { margin:0;padding:0;border:0;font-size:100%;font:inherit;vertical-align:b... }`
- `section { display:block }`
- `body { line-height:1 }`
- `q:after { content:"";content:none }`
- `table { border-collapse:collapse;border-spacing:0 }`
- **Per-Selector Transition Rules**:
- **Selector `:focus-visible`**: `transition: none` extracted from `lpas-com` stylesheet.
- **Selector `.is-previous-container:after`**: `transition: opacity .5s ease` extracted from `lpas-com` stylesheet.
- **Selector `.is-previous-container.is-darkene...`**: `transition: opacity .5s ease,backdrop-filter .6s ease` extracted from `lpas-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.14,.83,.4,1)`)**: Governs interactive state transitions across `<header.mainHeader>` and `<section.blockIntroGeneral>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `lpas-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
