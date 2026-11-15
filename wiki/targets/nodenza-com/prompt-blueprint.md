---
title: "UI Prompt Blueprint: nodenza-com"
date: 2026-11-15
target: "nodenza-com"
status: analyzed
capture: dom
capture_desktop: dom
capture_mobile: dom
archetype: "Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#e6efff` accent)"
---

# UI Design System & Master Generation Blueprint: nodenza-com

> **Home · Nodenza** (https://nodenza.com/) — Nosenza invests globally in early-stage biotech, medtech, and healthcare companies advancing life sciences and improving patient outcomes.

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Home · Nodenza** (`https://nodenza.com/`). Nosenza invests globally in early-stage biotech, medtech, and healthcare companies advancing life sciences and improving patient outcomes.
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#e6efff` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#ffffff` (`var(--c0)` in `:root`) paired with `#000000` primary typography and `#e6efff` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Aspekta` for display copy (`Experience the explosive power of wh`) with `Aspekta` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `var(--mw)` container bounds (`gap: 20rem`, padding `var(--headroom-height)`) with `cubic-bezier(0.2,1,0.3,1)` easing and GSAP Timeline & ScrollTrigger, Swiper Touch Carousel Engine.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×3230px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `var(--mw)` extracted from `nodenza-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--headroom-height)` lateral canvas padding with `20rem` grid gap.
- **Border Radius Scale**: `50%`, `10rem`, `16rem`, `var(--br1)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--mw)`, `gap: 20rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--headroom-height)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width: 1024px)`, `@media (max-width: 1023.98px)`, `@media (min-width: 1920px)`, `@media (hover: hover) and (pointer: fine) and (min-width: 1024px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | `var(--c0)` in `:root` |
| **Primary Typography Ink** | `#000000` | `var(--c1)` in `:root` |
| **Elevated Surface / Card Substrate** | `#32006f` | `var(--c2)` in `:root` |
| **Interactive Accent / Highlight** | `#e6efff` | `var(--c3)` in `:root` |
| **Secondary / Muted Copy** | `#ee0000` | `var(--c5)` in `:root` |
| **Structural Hairline Border** | `#bfbfbf` | `var(--c7)` in `:root` |
| **Variable Token (`--c8`)** | `#5e5e5e` | `var(--c8)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--app-height` | `100vh` | Layout / Spatial Grid Token |
| `--headroom-height` | `auto` | Layout / Spatial Grid Token |
| `--c0` | `#ffffff` | Color / Atmospheric Token |
| `--c1` | `#000000` | Color / Atmospheric Token |
| `--c2` | `#32006f` | Color / Atmospheric Token |
| `--c3` | `#e6efff` | Color / Atmospheric Token |
| `--c4` | `rgba(127, 173, 255, 0.2)` | Color / Atmospheric Token |
| `--c5` | `#ee0000` | Color / Atmospheric Token |
| `--c6` | `rgba(0, 0, 0, 0.7)` | Color / Atmospheric Token |
| `--c7` | `#bfbfbf` | Color / Atmospheric Token |
| `--c8` | `#5e5e5e` | Color / Atmospheric Token |
| `--wr` | `20rem` | Dimension / Scale Token |
| `--awr` | `calc(-1 * var(--wr))` | Design System Custom Token |
| `--gap` | `20rem` | Layout / Spatial Grid Token |
| `--sl` | `max(1px, 1rem)` | Dimension / Scale Token |
| `--br1` | `10rem` | Dimension / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Aspekta`.
- **Primary Body Stack**: `Aspekta`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `.title` (`line-height: 0.95`, `letter-spacing: -0.03em`, `font-weight: 500`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: var(--f-b)`, `line-height: 1`, `font-weight: 600`).
- **Body Copy**: rule `p` (`font-size: var(--f-d)`, `line-height: 1.3`, `font-weight: 400`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `0.0625vw`, `var(--f-d)`, `var(--f-xl)`, `var(--f-xxl)`, `300rem`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.2,1,0.3,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.preloader`**: `transition: all 0.25s 0.3s` extracted from `nodenza-com` stylesheet.
- **Selector `.loading .preloader`**: `transition: 0s` extracted from `nodenza-com` stylesheet.
- **Selector `.unload .preloader`**: `transition: 0.5s` extracted from `nodenza-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.2,1,0.3,1)`)**: Governs interactive state transitions across `<header.hide-scrollbar>` and `<section.hero-snap__slide>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Home · Nodenza                             │
│ ====================================================================== │
│ [ <header.hide-scrollbar>  | Home · Our Team · Portfolio · News · W ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero-snap__slide>                           |   │
│ | H1: Experience the explosive power of when science me...         |   │
│ | Substrate: #ffffff    | Ink: #000000    | Accent: #e6efff        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.hero-snap__slide>) max-w: var(--mw)      |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Our Mission                  |  | Our Approach                 | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 20rem ) | │
│ | [<header.hide-scrol] -> [<section.hero-snap] -> [<section.hero-snap] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.acsb-sr-alert>) | https://nodenza.com/               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.hide-scrollbar> — `nodenza-com`)**:
   - Landmark `<header class="hide-scrollbar">` hosting `Home · Nodenza` navigation (`Home · Our Team · Portfolio · News · Webinars`), DOM attributes (`data-acsb-sr-alert="true"`, `data-acsb-sr-only="true"`, `data-acsb-force-visible="true"`, `data-acsb`), and stylesheet rule `html { font-size: 0.0625vw; background-color: var(--c3); }`.
2. **Hero Stage & Focal Lead (<section.hero-snap__slide> — `Experience the explosive power of `)**:
   - Landmark `<section class="hero-snap__slide">` presenting display lead `Experience the explosive power of when science me...` and copy excerpt *"Press Option+1 for screen-reader mode, Option+0 to cancel"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.hero-snap__slide> — `Our Mission`)**:
   - Landmark `<section class="hero-snap__slide">` rendering section `Our Mission` with copy *"Accessibility Screen-Reader Guide, Feedback, and Issue Reporting "*, asset references (`embed`, `styles.css`, `style.css`, `main.css`), and grid rule `body { overflow-x: hidden; }`.
4. **Interactive Detail & Feature Matrix (<section.hero-snap__slide> — `Our Approach`)**:
   - Landmark `<section class="hero-snap__slide">` framing `Our Approach` and `What brings you to Nodenza?` (*"Enabling disruptive life sciences technology."*) with `#32006f` surface cards, `#e6efff` accents, and `.wrapper { width: 100%; margin: 0 auto; padding: 0 var(--wr); max-width: var(--mw); }`.
5. **Colophon & Global Directory Footer (<footer.acsb-sr-alert> — `https://nodenza.com/`)**:
   - Landmark `<footer class="acsb-sr-alert">` anchoring `Home · Nodenza` footer links (`Home · Our Team · Portfolio · News · Webinars`), copy *"Established by a team of experienced life sciences entrepren"*, and `#bfbfbf` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: nodenza-com (Home · Nodenza)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `nodenza-com` (**Home · Nodenza** — `https://nodenza.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#e6efff` accent).
- **Identity & Domain Context**: Nosenza invests globally in early-stage biotech, medtech, and healthcare companies advancing life sciences and improving patient outcomes.
- **Primary Substrate**: `#ffffff` (`var(--c0)` in `:root`), **Primary Ink**: `#000000`, **Accent / Highlight**: `#e6efff`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#ffffff` (`var(--c0)` in `:root`) paired with `#000000` primary typography and `#e6efff` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Aspekta` for display copy (`Experience the explosive power of wh`) with `Aspekta` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `var(--mw)` container bounds (`gap: 20rem`, padding `var(--headroom-height)`) with `cubic-bezier(0.2,1,0.3,1)` easing and GSAP Timeline & ScrollTrigger, Swiper Touch Carousel Engine.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `nodenza-com` in your global stylesheet:

:root {
  /* Home · Nodenza (nodenza-com) — Ground-Truth Extracted CSS Variables */
  --app-height: 100vh; /* Layout / Spatial Grid Token (nodenza-com) */
  --headroom-height: auto; /* Layout / Spatial Grid Token (nodenza-com) */
  --c0: #ffffff; /* Color / Atmospheric Token (nodenza-com) */
  --c1: #000000; /* Color / Atmospheric Token (nodenza-com) */
  --c2: #32006f; /* Color / Atmospheric Token (nodenza-com) */
  --c3: #e6efff; /* Color / Atmospheric Token (nodenza-com) */
  --c4: rgba(127, 173, 255, 0.2); /* Color / Atmospheric Token (nodenza-com) */
  --c5: #ee0000; /* Color / Atmospheric Token (nodenza-com) */
  --c6: rgba(0, 0, 0, 0.7); /* Color / Atmospheric Token (nodenza-com) */
  --c7: #bfbfbf; /* Color / Atmospheric Token (nodenza-com) */
  --c8: #5e5e5e; /* Color / Atmospheric Token (nodenza-com) */
  --wr: 20rem; /* Dimension / Scale Token (nodenza-com) */
  --awr: calc(-1 * var(--wr)); /* Design System Custom Token (nodenza-com) */
  --gap: 20rem; /* Layout / Spatial Grid Token (nodenza-com) */
  --sl: max(1px, 1rem); /* Dimension / Scale Token (nodenza-com) */
  --br1: 10rem; /* Dimension / Scale Token (nodenza-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in `var(--c0)` in `:root`
- **Primary Typography Ink**: `#000000` — grounded in `var(--c1)` in `:root`
- **Elevated Surface / Card Substrate**: `#32006f` — grounded in `var(--c2)` in `:root`
- **Interactive Accent / Highlight**: `#e6efff` — grounded in `var(--c3)` in `:root`
- **Secondary / Muted Copy**: `#ee0000` — grounded in `var(--c5)` in `:root`
- **Structural Hairline Border**: `#bfbfbf` — grounded in `var(--c7)` in `:root`
- **Variable Token (`--c8`)**: `#5e5e5e` — grounded in `var(--c8)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×3230px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `var(--mw)` extracted from `nodenza-com` stylesheet
- **Padding & Gutters**: `var(--headroom-height)` lateral canvas padding with `20rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--mw)`, `gap: 20rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--headroom-height)` horizontal padding
- **Media Queries**: `@media (min-width: 1024px)`, `@media (max-width: 1023.98px)`, `@media (min-width: 1920px)`, `@media (hover: hover) and (pointer: fine) and (min-width: 1024px)`
- **Corner Radii**: `50%`, `10rem`, `16rem`, `var(--br1)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Aspekta`
- **Body Font Stack**: `Aspekta`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: rule `.title` (`line-height: 0.95`, `letter-spacing: -0.03em`, `font-weight: 500`)
- **H2 Section Rule**: rule `h2` (`font-size: var(--f-b)`, `line-height: 1`, `font-weight: 600`)
- **Body Copy Rule**: rule `p` (`font-size: var(--f-d)`, `line-height: 1.3`, `font-weight: 400`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `0.0625vw`, `var(--f-d)`, `var(--f-xl)`, `var(--f-xxl)`, `300rem`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `nodenza-com` (`Home · Nodenza`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.hide-scrollbar> — `nodenza-com`)**:
   - DOM & Selectors: Landmark `<header class="hide-scrollbar">` hosting `Home · Nodenza` navigation (`Home · Our Team · Portfolio · News · Webinars`), DOM attributes (`data-acsb-sr-alert="true"`, `data-acsb-sr-only="true"`, `data-acsb-force-visible="true"`, `data-acsb`), and stylesheet rule `html { font-size: 0.0625vw; background-color: var(--c3); }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.hide-scrollbar> — `nodenza-com`)` (`nodenza-com`) adapts across `@media (min-width: 1024px)`, `@media (max-width: 1023.98px)`, `@media (min-width: 1920px)`, `@media (hover: hover) and (pointer: fine) and (min-width: 1024px)` with `cubic-bezier(0.2,1,0.3,1)` transitions and links `Home · Our Team · Portfolio · News · Webinars`.
2. **Hero Stage & Focal Lead (<section.hero-snap__slide> — `Experience the explosive power of `)**:
   - DOM & Selectors: Landmark `<section class="hero-snap__slide">` presenting display lead `Experience the explosive power of when science me...` and copy excerpt *"Press Option+1 for screen-reader mode, Option+0 to cancel"* over `#ffffff` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1440×3230px` desktop / `390×2400px` mobile) sets `#ffffff` background with `#000000` headline `Experience the explosive power of when science me...`.
3. **Primary Showcase & Content Grid (<section.hero-snap__slide> — `Our Mission`)**:
   - DOM & Selectors: Landmark `<section class="hero-snap__slide">` rendering section `Our Mission` with copy *"Accessibility Screen-Reader Guide, Feedback, and Issue Reporting "*, asset references (`embed`, `styles.css`, `style.css`, `main.css`), and grid rule `body { overflow-x: hidden; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.hero-snap__slide> — `Our Mission`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--mw)`, `gap: 20rem`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--headroom-height)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.hero-snap__slide> — `Our Approach`)**:
   - DOM & Selectors: Landmark `<section class="hero-snap__slide">` framing `Our Approach` and `What brings you to Nodenza?` (*"Enabling disruptive life sciences technology."*) with `#32006f` surface cards, `#e6efff` accents, and `.wrapper { width: 100%; margin: 0 auto; padding: 0 var(--wr); max-width: var(--mw); }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.hero-snap__slide> — `Our Approach`)` uses `50%`, `10rem`, `16rem`, `var(--br1)` radii, `#e6efff` highlights, and assets (embed, styles.css, style.css).
5. **Colophon & Global Directory Footer (<footer.acsb-sr-alert> — `https://nodenza.com/`)**:
   - DOM & Selectors: Landmark `<footer class="acsb-sr-alert">` anchoring `Home · Nodenza` footer links (`Home · Our Team · Portfolio · News · Webinars`), copy *"Established by a team of experienced life sciences entrepren"*, and `#bfbfbf` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.acsb-sr-alert> — `https://nodenza.com/`)` aligns to `var(--mw)` extracted from `nodenza-com` stylesheet with `var(--headroom-height)` lateral canvas padding with `20rem` grid gap and attributes (data-acsb-sr-alert="true", data-acsb-sr-only="true", data-acsb-force-visible="true").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Press Option+1 for screen-reader mode, Option+0 to cancel"*
- Copy Excerpt 2: *"Accessibility Screen-Reader Guide, Feedback, and Issue Reporting · New window"*
- Copy Excerpt 3: *"Enabling disruptive life sciences technology."*
- Copy Excerpt 4: *"Established by a team of experienced life sciences entrepreneurs, founders and lea..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.2,1,0.3,1)`
- **Extracted Stylesheet Rules (`nodenza-com`)**:
- `html { font-size: 0.0625vw; background-color: var(--c3); }`
- `body { overflow-x: hidden; }`
- `.wrapper { width: 100%; margin: 0 auto; padding: 0 var(--wr); max-width: var(--mw); }`
- `.loading { pointer-events: none; }`
- `.loading .preloader { transition-duration: 0s; opacity: 1; visibility: visible; }`
- **Per-Selector Transition Rules**:
- **Selector `.preloader`**: `transition: all 0.25s 0.3s` extracted from `nodenza-com` stylesheet.
- **Selector `.loading .preloader`**: `transition: 0s` extracted from `nodenza-com` stylesheet.
- **Selector `.unload .preloader`**: `transition: 0.5s` extracted from `nodenza-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.2,1,0.3,1)`)**: Governs interactive state transitions across `<header.hide-scrollbar>` and `<section.hero-snap__slide>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `nodenza-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
