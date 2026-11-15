---
title: "UI Prompt Blueprint: grids03-obys-agency"
date: 2026-11-15
target: "[[overview|grids03-obys-agency]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#e1e1e1`)"
---

# UI Design System & Master Generation Blueprint: grids03-obys-agency

> **Grids — DES Season 03** (https://grids03.obys.agency/) — Grids is an interactive project exploring grids, composition, and key design principles through visual experiments. First launched in 202...

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/grids03-obys-agency/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Grids — DES Season 03** (`https://grids03.obys.agency/`). Grids is an interactive project exploring grids, composition, and key design principles through visual experiments. First launched in 202...
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#e1e1e1`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`var(--color-bg)` in `:root`) paired with `#000` primary typography and `#e1e1e1` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Obys Sans` for display copy (`G r i d s S 0 3`) with `Helvetica Neue` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `260px` container bounds (`gap: 0px (flush layout)`, padding `4px`) with `cubic-bezier(0.25,0.1,0.25,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/grids03-obys-agency/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `260px` extracted from `grids03-obys-agency` stylesheet.
- **Canvas Lateral Padding & Spacing**: `4px` lateral canvas padding with `0px (flush layout)` grid gap.
- **Border Radius Scale**: `50%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 260px`, `gap: 0px (flush layout)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `4px` horizontal padding.
- **Extracted CSS Media Queries**: no `@media` queries in static stylesheet (fluid viewport scaling).

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--color-bg)` in `:root` |
| **Primary Typography Ink** | `#000` | `var(--color-ink)` in `:root` |
| **Elevated Surface / Card Substrate** | `#dedfd9` | `var(--color-ground)` in `:root` |
| **Interactive Accent / Highlight** | `#e1e1e1` | `var(--color-rule)` in `:root` |
| **Secondary / Muted Copy** | `#d9d9d9` | `.grid-entry__picture { background: #d9d9d9 }` |
| **Structural Hairline Border** | `#b2b2b2` | `.about__line--quiet i { color: #b2b2b2 }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-bg` | `#fff` | Canvas / Surface Token |
| `--color-ink` | `#000` | Typography Ink Token |
| `--color-ground` | `#dedfd9` | Brand / Palette Token |
| `--color-rule` | `#e1e1e1` | Brand / Palette Token |
| `--layer-gl` | `0` | Design System Custom Token |
| `--layer-content` | `2` | Design System Custom Token |
| `--layer-header` | `3` | Layout / Spatial Grid Token |
| `--layer-preloader` | `50` | Design System Custom Token |
| `--grid-columns` | `12` | Layout / Spatial Grid Token |
| `--grid-margin` | `20` | Layout / Spatial Grid Token |
| `--grid-gutter` | `20` | Layout / Spatial Grid Token |
| `--vw` | `1440px` | Layout / Spatial Grid Token |
| `--vh` | `900px` | Layout / Spatial Grid Token |
| `--caption-size` | `90px` | Layout / Spatial Grid Token |
| `--small-size` | `12px` | Layout / Spatial Grid Token |
| `--edge` | `18px` | Dimension / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Obys Sans`.
- **Primary Body Stack**: `Helvetica Neue`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--small-size)`, `var(--caption-size)`, `var(--size)`, `var(--about-size)`, `12px`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--small-size)`, `var(--caption-size)`, `var(--size)`, `var(--about-size)`, `12px`).
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--small-size)`, `var(--caption-size)`, `var(--size)`, `var(--about-size)`, `12px`).
- **Metadata & Navigation Labels**: CSS variables `--caption-size: 90px`, `--small-size: 12px`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.intro__link`**: `transition: opacity .3s` extracted from `grids03-obys-agency` stylesheet.
- **Selector `.about__copy .about__link`**: `transition: opacity .3s` extracted from `grids03-obys-agency` stylesheet.
- **Selector `.about__row`**: `transition: opacity .35s` extracted from `grids03-obys-agency` stylesheet.
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in static CSS).
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Grids — DES Season 03                      │
│ ====================================================================== │
│ [ <header.lenis>           | Grids · More About Season · Enroll Now ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.intro>                                      |   │
│ | H1: G r i d s S 0 3                                              |   │
│ | Substrate: #fff       | Ink: #000       | Accent: #e1e1e1        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.grid-block>      ) max-w: 260px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | 4 - C o l u m n              |  | G r i d                      | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 0px (f) | │
│ | [<header.lenis>] -> [<section.intro>] -> [<section.grid-bloc] |      │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.preloader>    ) | https://grids03.obys.agency/       │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.lenis> — `grids03-obys-agency`)**:
   - Landmark `<header class="lenis">` hosting `Grids — DES Season 03` navigation (`Grids · More About Season · Enroll Now · Learn for Free · Obys`), DOM attributes (`data-preloader`, `data-ground`, `data-bar`, `data-letter="G"`), and stylesheet rule `body { overflow-x:hidden }`.
2. **Hero Stage & Focal Lead (<section.intro> — `G r i d s S 0 3`)**:
   - Landmark `<section class="intro">` presenting display lead `G r i d s S 0 3` and copy excerpt *"Design Education Series® Obys"* over `#fff` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.grid-block> — `4 - C o l u m n`)**:
   - Landmark `<section class="grid-block">` rendering section `4 - C o l u m n` with copy *"Grids — DES Season 03. 17 lectures."*, asset references (`favicon.svg`, `favicon-32.png`, `favicon-180.png`, `ObysSans-Regular.woff2`), and grid rule `.stage { width:100%;height:100%;z-index:var(--layer-gl);pointer-events:none;posit... }`.
4. **Interactive Detail & Feature Matrix (<section.story> — `G r i d`)**:
   - Landmark `<section class="story">` framing `G r i d` and `1 0 p x` (*"4+ hours on grids and composition."*) with `#dedfd9` surface cards, `#e1e1e1` accents, and `.preloader { z-index:var(--layer-preloader);pointer-events:none;position:fixed;inset:... }`.
5. **Colophon & Global Directory Footer (<footer.preloader> — `https://grids03.obys.agency/`)**:
   - Landmark `<footer class="preloader">` anchoring `Grids — DES Season 03` footer links (`Grids · More About Season · Enroll Now · Learn for Free · Obys`), copy *"About Grids, Season"*, and `#b2b2b2` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: grids03-obys-agency (Grids — DES Season 03)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `grids03-obys-agency` (**Grids — DES Season 03** — `https://grids03.obys.agency/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#e1e1e1`).
- **Identity & Domain Context**: Grids is an interactive project exploring grids, composition, and key design principles through visual experiments. First launched in 202...
- **Primary Substrate**: `#fff` (`var(--color-bg)` in `:root`), **Primary Ink**: `#000`, **Accent / Highlight**: `#e1e1e1`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`var(--color-bg)` in `:root`) paired with `#000` primary typography and `#e1e1e1` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Obys Sans` for display copy (`G r i d s S 0 3`) with `Helvetica Neue` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `260px` container bounds (`gap: 0px (flush layout)`, padding `4px`) with `cubic-bezier(0.25,0.1,0.25,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `grids03-obys-agency` in your global stylesheet:

:root {
  /* Grids — DES Season 03 (grids03-obys-agency) — Ground-Truth Extracted CSS Variables */
  --color-bg: #fff; /* Canvas / Surface Token (grids03-obys-agency) */
  --color-ink: #000; /* Typography Ink Token (grids03-obys-agency) */
  --color-ground: #dedfd9; /* Brand / Palette Token (grids03-obys-agency) */
  --color-rule: #e1e1e1; /* Brand / Palette Token (grids03-obys-agency) */
  --layer-gl: 0; /* Design System Custom Token (grids03-obys-agency) */
  --layer-content: 2; /* Design System Custom Token (grids03-obys-agency) */
  --layer-header: 3; /* Layout / Spatial Grid Token (grids03-obys-agency) */
  --layer-preloader: 50; /* Design System Custom Token (grids03-obys-agency) */
  --grid-columns: 12; /* Layout / Spatial Grid Token (grids03-obys-agency) */
  --grid-margin: 20; /* Layout / Spatial Grid Token (grids03-obys-agency) */
  --grid-gutter: 20; /* Layout / Spatial Grid Token (grids03-obys-agency) */
  --vw: 1440px; /* Layout / Spatial Grid Token (grids03-obys-agency) */
  --vh: 900px; /* Layout / Spatial Grid Token (grids03-obys-agency) */
  --caption-size: 90px; /* Layout / Spatial Grid Token (grids03-obys-agency) */
  --small-size: 12px; /* Layout / Spatial Grid Token (grids03-obys-agency) */
  --edge: 18px; /* Dimension / Scale Token (grids03-obys-agency) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fff` — grounded in `var(--color-bg)` in `:root`
- **Primary Typography Ink**: `#000` — grounded in `var(--color-ink)` in `:root`
- **Elevated Surface / Card Substrate**: `#dedfd9` — grounded in `var(--color-ground)` in `:root`
- **Interactive Accent / Highlight**: `#e1e1e1` — grounded in `var(--color-rule)` in `:root`
- **Secondary / Muted Copy**: `#d9d9d9` — grounded in `.grid-entry__picture { background: #d9d9d9 }`
- **Structural Hairline Border**: `#b2b2b2` — grounded in `.about__line--quiet i { color: #b2b2b2 }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `260px` extracted from `grids03-obys-agency` stylesheet
- **Padding & Gutters**: `4px` lateral canvas padding with `0px (flush layout)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 260px`, `gap: 0px (flush layout)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `4px` horizontal padding
- **Media Queries**: no `@media` queries in static stylesheet (fluid viewport scaling)
- **Corner Radii**: `50%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Obys Sans`
- **Body Font Stack**: `Helvetica Neue`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--small-size)`, `var(--caption-size)`, `var(--size)`, `var(--about-size)`, `12px`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--small-size)`, `var(--caption-size)`, `var(--size)`, `var(--about-size)`, `12px`)
- **Body Copy Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--small-size)`, `var(--caption-size)`, `var(--size)`, `var(--about-size)`, `12px`)
- **Metadata & Index Rule**: CSS variables `--caption-size: 90px`, `--small-size: 12px`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `grids03-obys-agency` (`Grids — DES Season 03`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.lenis> — `grids03-obys-agency`)**:
   - DOM & Selectors: Landmark `<header class="lenis">` hosting `Grids — DES Season 03` navigation (`Grids · More About Season · Enroll Now · Learn for Free · Obys`), DOM attributes (`data-preloader`, `data-ground`, `data-bar`, `data-letter="G"`), and stylesheet rule `body { overflow-x:hidden }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.lenis> — `grids03-obys-agency`)` (`grids03-obys-agency`) adapts across no `@media` queries in static stylesheet (fluid viewport scaling) with `cubic-bezier(0.25,0.1,0.25,1)` transitions and links `Grids · More About Season · Enroll Now · Learn for Free · Obys`.
2. **Hero Stage & Focal Lead (<section.intro> — `G r i d s S 0 3`)**:
   - DOM & Selectors: Landmark `<section class="intro">` presenting display lead `G r i d s S 0 3` and copy excerpt *"Design Education Series® Obys"* over `#fff` canvas and `#000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#fff` background with `#000` headline `G r i d s S 0 3`.
3. **Primary Showcase & Content Grid (<section.grid-block> — `4 - C o l u m n`)**:
   - DOM & Selectors: Landmark `<section class="grid-block">` rendering section `4 - C o l u m n` with copy *"Grids — DES Season 03. 17 lectures."*, asset references (`favicon.svg`, `favicon-32.png`, `favicon-180.png`, `ObysSans-Regular.woff2`), and grid rule `.stage { width:100%;height:100%;z-index:var(--layer-gl);pointer-events:none;posit... }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.grid-block> — `4 - C o l u m n`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 260px`, `gap: 0px (flush layout)`) on desktop and Single-column vertical stack at `390px` viewport width with `4px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.story> — `G r i d`)**:
   - DOM & Selectors: Landmark `<section class="story">` framing `G r i d` and `1 0 p x` (*"4+ hours on grids and composition."*) with `#dedfd9` surface cards, `#e1e1e1` accents, and `.preloader { z-index:var(--layer-preloader);pointer-events:none;position:fixed;inset:... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.story> — `G r i d`)` uses `50%` radii, `#e1e1e1` highlights, and assets (favicon.svg, favicon-32.png, favicon-180.png).
5. **Colophon & Global Directory Footer (<footer.preloader> — `https://grids03.obys.agency/`)**:
   - DOM & Selectors: Landmark `<footer class="preloader">` anchoring `Grids — DES Season 03` footer links (`Grids · More About Season · Enroll Now · Learn for Free · Obys`), copy *"About Grids, Season"*, and `#b2b2b2` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.preloader> — `https://grids03.obys.agency/`)` aligns to `260px` extracted from `grids03-obys-agency` stylesheet with `4px` lateral canvas padding with `0px (flush layout)` grid gap and attributes (data-preloader, data-ground, data-bar).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Design Education Series® Obys"*
- Copy Excerpt 2: *"Grids — DES Season 03. 17 lectures."*
- Copy Excerpt 3: *"4+ hours on grids and composition."*
- Copy Excerpt 4: *"About Grids, Season"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`
- **Extracted Stylesheet Rules (`grids03-obys-agency`)**:
- `body { overflow-x:hidden }`
- `.stage { width:100%;height:100%;z-index:var(--layer-gl);pointer-events:none;posit... }`
- `.preloader { z-index:var(--layer-preloader);pointer-events:none;position:fixed;inset:... }`
- `.preloader__ground { background:var(--color-ground);will-change:transform;width:100%;height:1... }`
- `.preloader__bar { background:var(--color-ink);will-change:transform;height:1px;margin-top:... }`
- **Per-Selector Transition Rules**:
- **Selector `.intro__link`**: `transition: opacity .3s` extracted from `grids03-obys-agency` stylesheet.
- **Selector `.about__copy .about__link`**: `transition: opacity .3s` extracted from `grids03-obys-agency` stylesheet.
- **Selector `.about__row`**: `transition: opacity .35s` extracted from `grids03-obys-agency` stylesheet.
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in static CSS).
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `grids03-obys-agency`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
