---
title: "UI Prompt Blueprint: coloniazacamil-com"
date: 2026-11-15
target: "[[overview|coloniazacamil-com]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#B48E46` / `#000`)"
---

# UI Design System & Master Generation Blueprint: coloniazacamil-com

> **Colonia Zacamil** (https://coloniazacamil.com/) — Colonia Zacamil

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/coloniazacamil-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Colonia Zacamil** (`https://coloniazacamil.com/`). Colonia Zacamil
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#B48E46` / `#000`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#B48E46` (`var(--color)` in `:root`) paired with `#000` primary typography and `#000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Roboto Mono` for display copy (`Colonia Zacamil`) with `Reckless Neue` and `Roboto Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `767px` container bounds (`gap: 19px`, padding `27px`) with `cubic-bezier(.25,1,.5,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/coloniazacamil-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `767px` extracted from `coloniazacamil-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `27px` lateral canvas padding with `19px` grid gap.
- **Border Radius Scale**: `18px`, `30px`, `50%`, `10px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 767px`, `gap: 19px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `27px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:767px)`, `@media (min-width:768px)`, `@media (max-width:1024px) and (min-width:768px)`, `@media (min-width:1025px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#B48E46` | `var(--color)` in `:root` |
| **Primary Typography Ink** | `#ffffff` | `var(--dark-color)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff` | `:after { background: #fff }` |
| **Interactive Accent / Highlight** | `#000` | `:before { background: #000 }` |
| **Secondary / Muted Copy** | `#d9d9d9` | `:before { background: #d9d9d9 }` |
| **Structural Hairline Border** | `#af0000` | `:after { background: #af0000 }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--delay` | `.2s` | Motion / Easing Token |
| `--width` | `200px` | Layout / Spatial Grid Token |
| `--translate-multiplier` | `1` | Design System Custom Token |
| `--direction` | `1` | Design System Custom Token |
| `--slide-direction` | `0` | Design System Custom Token |
| `--video-progress` | `0%` | Dimension / Scale Token |
| `--iub-granular-background` | `rgba(0, 0, 0, .02)` | Canvas / Surface Token |
| `--iub-granular-border` | `rgba(0, 0, 0, 0.08)` | Elevation / Border Token |
| `--iub-granular-toggle-background` | `rgba(0, 0, 0, 0.2)` | Canvas / Surface Token |
| `--vh` | `9.000px` | Layout / Spatial Grid Token |
| `--vw` | `14.40px` | Layout / Spatial Grid Token |
| `--vwRaw` | `14.40` | Layout / Spatial Grid Token |
| `--dvh` | `9.00px` | Layout / Spatial Grid Token |
| `--svh` | `9.00px` | Layout / Spatial Grid Token |
| `--color` | `#B48E46` | Brand / Palette Token |
| `--dark-color` | `#ffffff` | Canvas / Surface Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Roboto Mono`.
- **Primary Body Stack**: `Reckless Neue`.
- **Technical / Metadata Stack**: `Roboto Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `40px`, `14px`, `12px`, `10px`, `24px`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `40px`, `14px`, `12px`, `10px`, `24px`).
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `40px`, `14px`, `12px`, `10px`, `24px`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `40px`, `14px`, `12px`, `10px`, `24px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.25,1,.5,1)`, `cubic-bezier(.55,.055,.675,.19)`, `cubic-bezier(.5,0,.75,0)`.

### Per-Element Transition & Choreography Rules
- **Selector `.fade-leave-active[data-v-4887bba3]`**: `transition: opacity .5s` extracted from `coloniazacamil-com` stylesheet.
- **Selector `.fade-delayed-leave-active[data-v...`**: `transition: opacity .5s` extracted from `coloniazacamil-com` stylesheet.
- **Selector `.fade-fast-leave-active[data-v-48...`**: `transition: opacity .2s` extracted from `coloniazacamil-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.25,1,.5,1)`)**: Governs interactive state transitions across `<header.cmplazyload>` and `<section.hidden>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Colonia Zacamil                            │
│ ====================================================================== │
│ [ <header.cmplazyload>     | [powered by CMS ] · en · / es · cookie ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.webgl>                                      |   │
│ | H1: Colonia Zacamil                                              |   │
│ | Substrate: #B48E46    | Ink: #000       | Accent: #000           |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.hidden>          ) max-w: 767px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Featured Work & Interactive  |  | Technical Architecture & Nar | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 19px  ) | │
│ | [<header.cmplazyloa] -> [<section.webgl>] -> [<section.hidden>] |    │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.not-clickable>) | https://coloniazacamil.com/        │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.cmplazyload> — `coloniazacamil-com`)**:
   - Landmark `<header class="cmplazyload">` hosting `Colonia Zacamil` navigation (`[powered by CMS ] · en · / es · cookie policy`), DOM attributes (`data-capo`, `data-cmp-ab="2"`, `data-cmp-info="2"`, `data-cmp-info="13"`), and stylesheet rule `first-child { transition:opacity .6s ease-in-out 0s }`.
2. **Hero Stage & Focal Lead (<section.webgl> — `Colonia Zacamil`)**:
   - Landmark `<section class="webgl">` presenting display lead `Colonia Zacamil` and copy excerpt *"A Better Childhood"* over `#B48E46` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.hidden> — `Featured Work & Interactive Showca`)**:
   - Landmark `<section class="hidden">` rendering section `Featured Work & Interactive Showcase` with copy *"[powered by CMS ] Zacamil"*, asset references (`core-en-GB.js`, `4037b39e-9661-4616-8093-abccf645c...`, `entry.t46wWHdU.css`, `_payload.json`), and grid rule `after { display:none }`.
4. **Interactive Detail & Feature Matrix (<section.pin> — `Technical Architecture & Narrative`)**:
   - Landmark `<section class="pin">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"click and drag to explore"*) with `#fff` surface cards, `#000` accents, and `hover { max-width:var(--width);z-index:1 }`.
5. **Colophon & Global Directory Footer (<footer.not-clickable> — `https://coloniazacamil.com/`)**:
   - Landmark `<footer class="not-clickable">` anchoring `Colonia Zacamil` footer links (`[powered by CMS ] · en · / es · cookie policy`), copy *"pinch to zoom in & out"*, and `#af0000` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: coloniazacamil-com (Colonia Zacamil)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `coloniazacamil-com` (**Colonia Zacamil** — `https://coloniazacamil.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#B48E46` / `#000`).
- **Identity & Domain Context**: Colonia Zacamil
- **Primary Substrate**: `#B48E46` (`var(--color)` in `:root`), **Primary Ink**: `#000`, **Accent / Highlight**: `#000`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#B48E46` (`var(--color)` in `:root`) paired with `#000` primary typography and `#000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Roboto Mono` for display copy (`Colonia Zacamil`) with `Reckless Neue` and `Roboto Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `767px` container bounds (`gap: 19px`, padding `27px`) with `cubic-bezier(.25,1,.5,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `coloniazacamil-com` in your global stylesheet:

:root {
  /* Colonia Zacamil (coloniazacamil-com) — Ground-Truth Extracted CSS Variables */
  --delay: .2s; /* Motion / Easing Token (coloniazacamil-com) */
  --width: 200px; /* Layout / Spatial Grid Token (coloniazacamil-com) */
  --translate-multiplier: 1; /* Design System Custom Token (coloniazacamil-com) */
  --direction: 1; /* Design System Custom Token (coloniazacamil-com) */
  --slide-direction: 0; /* Design System Custom Token (coloniazacamil-com) */
  --video-progress: 0%; /* Dimension / Scale Token (coloniazacamil-com) */
  --iub-granular-background: rgba(0, 0, 0, .02); /* Canvas / Surface Token (coloniazacamil-com) */
  --iub-granular-border: rgba(0, 0, 0, 0.08); /* Elevation / Border Token (coloniazacamil-com) */
  --iub-granular-toggle-background: rgba(0, 0, 0, 0.2); /* Canvas / Surface Token (coloniazacamil-com) */
  --vh: 9.000px; /* Layout / Spatial Grid Token (coloniazacamil-com) */
  --vw: 14.40px; /* Layout / Spatial Grid Token (coloniazacamil-com) */
  --vwRaw: 14.40; /* Layout / Spatial Grid Token (coloniazacamil-com) */
  --dvh: 9.00px; /* Layout / Spatial Grid Token (coloniazacamil-com) */
  --svh: 9.00px; /* Layout / Spatial Grid Token (coloniazacamil-com) */
  --color: #B48E46; /* Brand / Palette Token (coloniazacamil-com) */
  --dark-color: #ffffff; /* Canvas / Surface Token (coloniazacamil-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#B48E46` — grounded in `var(--color)` in `:root`
- **Primary Typography Ink**: `#ffffff` — grounded in `var(--dark-color)` in `:root`
- **Elevated Surface / Card Substrate**: `#fff` — grounded in `:after { background: #fff }`
- **Interactive Accent / Highlight**: `#000` — grounded in `:before { background: #000 }`
- **Secondary / Muted Copy**: `#d9d9d9` — grounded in `:before { background: #d9d9d9 }`
- **Structural Hairline Border**: `#af0000` — grounded in `:after { background: #af0000 }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `767px` extracted from `coloniazacamil-com` stylesheet
- **Padding & Gutters**: `27px` lateral canvas padding with `19px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 767px`, `gap: 19px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `27px` horizontal padding
- **Media Queries**: `@media (max-width:767px)`, `@media (min-width:768px)`, `@media (max-width:1024px) and (min-width:768px)`, `@media (min-width:1025px)`
- **Corner Radii**: `18px`, `30px`, `50%`, `10px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Roboto Mono`
- **Body Font Stack**: `Reckless Neue`
- **Monospace / Technical Font Stack**: `Roboto Mono`
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `40px`, `14px`, `12px`, `10px`, `24px`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `40px`, `14px`, `12px`, `10px`, `24px`)
- **Body Copy Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `40px`, `14px`, `12px`, `10px`, `24px`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `40px`, `14px`, `12px`, `10px`, `24px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `coloniazacamil-com` (`Colonia Zacamil`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.cmplazyload> — `coloniazacamil-com`)**:
   - DOM & Selectors: Landmark `<header class="cmplazyload">` hosting `Colonia Zacamil` navigation (`[powered by CMS ] · en · / es · cookie policy`), DOM attributes (`data-capo`, `data-cmp-ab="2"`, `data-cmp-info="2"`, `data-cmp-info="13"`), and stylesheet rule `first-child { transition:opacity .6s ease-in-out 0s }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.cmplazyload> — `coloniazacamil-com`)` (`coloniazacamil-com`) adapts across `@media (max-width:767px)`, `@media (min-width:768px)`, `@media (max-width:1024px) and (min-width:768px)`, `@media (min-width:1025px)` with `cubic-bezier(.25,1,.5,1)`, `cubic-bezier(.55,.055,.675,.19)`, `cubic-bezier(.5,0,.75,0)` transitions and links `[powered by CMS ] · en · / es · cookie policy`.
2. **Hero Stage & Focal Lead (<section.webgl> — `Colonia Zacamil`)**:
   - DOM & Selectors: Landmark `<section class="webgl">` presenting display lead `Colonia Zacamil` and copy excerpt *"A Better Childhood"* over `#B48E46` canvas and `#000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#B48E46` background with `#000` headline `Colonia Zacamil`.
3. **Primary Showcase & Content Grid (<section.hidden> — `Featured Work & Interactive Showca`)**:
   - DOM & Selectors: Landmark `<section class="hidden">` rendering section `Featured Work & Interactive Showcase` with copy *"[powered by CMS ] Zacamil"*, asset references (`core-en-GB.js`, `4037b39e-9661-4616-8093-abccf645c...`, `entry.t46wWHdU.css`, `_payload.json`), and grid rule `after { display:none }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.hidden> — `Featured Work & Interactive Showca`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 767px`, `gap: 19px`) on desktop and Single-column vertical stack at `390px` viewport width with `27px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.pin> — `Technical Architecture & Narrative`)**:
   - DOM & Selectors: Landmark `<section class="pin">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"click and drag to explore"*) with `#fff` surface cards, `#000` accents, and `hover { max-width:var(--width);z-index:1 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.pin> — `Technical Architecture & Narrative`)` uses `18px`, `30px`, `50%`, `10px` radii, `#000` highlights, and assets (core-en-GB.js, 4037b39e-9661-4616-8093-abccf645c..., entry.t46wWHdU.css).
5. **Colophon & Global Directory Footer (<footer.not-clickable> — `https://coloniazacamil.com/`)**:
   - DOM & Selectors: Landmark `<footer class="not-clickable">` anchoring `Colonia Zacamil` footer links (`[powered by CMS ] · en · / es · cookie policy`), copy *"pinch to zoom in & out"*, and `#af0000` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.not-clickable> — `https://coloniazacamil.com/`)` aligns to `767px` extracted from `coloniazacamil-com` stylesheet with `27px` lateral canvas padding with `19px` grid gap and attributes (data-capo, data-cmp-ab="2", data-cmp-info="2").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"A Better Childhood"*
- Copy Excerpt 2: *"[powered by CMS ] Zacamil"*
- Copy Excerpt 3: *"click and drag to explore"*
- Copy Excerpt 4: *"pinch to zoom in & out"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.25,1,.5,1)`, `cubic-bezier(.55,.055,.675,.19)`, `cubic-bezier(.5,0,.75,0)`
- **Extracted Stylesheet Rules (`coloniazacamil-com`)**:
- `first-child { transition:opacity .6s ease-in-out 0s }`
- `after { display:none }`
- `hover { max-width:var(--width);z-index:1 }`
- `last-child { opacity:1;transition:opacity .4s linear }`
- `first-of-type { transform:translate(-4px) }`
- **Per-Selector Transition Rules**:
- **Selector `.fade-leave-active[data-v-4887bba3]`**: `transition: opacity .5s` extracted from `coloniazacamil-com` stylesheet.
- **Selector `.fade-delayed-leave-active[data-v...`**: `transition: opacity .5s` extracted from `coloniazacamil-com` stylesheet.
- **Selector `.fade-fast-leave-active[data-v-48...`**: `transition: opacity .2s` extracted from `coloniazacamil-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.25,1,.5,1)`)**: Governs interactive state transitions across `<header.cmplazyload>` and `<section.hidden>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `coloniazacamil-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
