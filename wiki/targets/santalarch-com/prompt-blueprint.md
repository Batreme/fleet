---
title: "UI Prompt Blueprint: santalarch-com"
date: 2026-11-23
captured_at: 2026-11-23
target: "santalarch-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#f0f0f0` / `#007aff`)"
---

# UI Design System & Master Generation Blueprint: santalarch-com

> **Santalarch** (https://santalarch.com) — Architectural studio built on uncompromising precision and intent.

![Desktop Viewport Capture (1440x900)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Santalarch** (`https://santalarch.com`). Architectural studio built on uncompromising precision and intent.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#f0f0f0` / `#007aff`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f0f0f0` (live computed `main` `background-color` (`computed_styles.json`)) paired with `#0f0f0f` primary typography and `#007aff` accents.
  - **Grounded Typographic Hierarchy**: Pairs `lil-gui` for display copy (`Intent Before Image`) with `Segoe UI` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 1rem`, padding `1rem`) with `cubic-bezier(.25,1,.5,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x844)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×900px` (`assets/desktop.png`, single-viewport 100vh live capture (900px)), Mobile `390×844px` (`assets/mobile.png`, single-viewport 100vh live capture (844px)).
- **Master Container Bounds**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport).
- **Canvas Lateral Padding & Spacing**: `1rem` lateral canvas padding with `1rem` grid gap.
- **Border Radius Scale**: `50%`, `2px`, `var(--scrollbar-width)`, `var(--widget-border-radius)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 1rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `1rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:1023px)`, `@media screen and (max-width:1023px)and (orientation:landscape)`, `@media (min-width:1024px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f0f0f0` | live computed `main` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0f0f0f` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `:hover { background-color: white }` (`#ffffff`) |
| **Interactive Accent / Highlight** | `#007aff` | `:root { color: #007aff }` |
| **Secondary / Muted Copy** | `#ebebeb` | `var(--text-color)` in `:root` |
| **Structural Hairline Border** | `#f9f9f9` | `ui .controller.color .display:h... { border: #f9f9f9 }` |
| **Variable Token (`--c-base-line-highlight`)** | `#f2f0f0` | `var(--c-base-line-highlight)` in `:root` |
| **Variable Token (`--c-pure-black`)** | `#000000` | `var(--c-pure-black)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--viewport-width` | `1440` | Layout / Spatial Grid Token |
| `--viewport-height` | `800` | Layout / Spatial Grid Token |
| `--font-helvetica` | `"Helvetica",sans-serif` | Typography / Scale Token |
| `--ease-out` | `cubic-bezier(.25,1,.5,1)` | Motion / Easing Token |
| `--transition` | `.5s var(--ease-out)` | Motion / Easing Token |
| `--transition-fast` | `.3s var(--ease-out)` | Motion / Easing Token |
| `--transition-slow` | `.8s var(--ease-out)` | Motion / Easing Token |
| `--c-base-light-primary` | `#f0f0f0` | Canvas / Surface Token |
| `--c-base-line-highlight` | `#f2f0f033` | Canvas / Surface Token |
| `--c-base-line-dark-bg` | `#f2f0f00d` | Canvas / Surface Token |
| `--c-pure-black` | `#000` | Canvas / Surface Token |
| `--c-pure-white` | `#fff` | Canvas / Surface Token |
| `--c-pure-black-rgb` | `0,0,0` | Canvas / Surface Token |
| `--c-pure-black-0` | `rgba(var(--c-pure-black-rgb),0)` | Canvas / Surface Token |
| `--c-light-primary` | `var(--c-base-light-primary)` | Canvas / Surface Token |
| `--c-light-secondary` | `#f2f0f066` | Canvas / Surface Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `lil-gui`.
- **Primary Body Stack**: `Segoe UI`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: rule `.title` (`line-height: calc(var(--title-heig...`, `font-weight: 600`).
- **Section Heading (`H2`)**: live computed `h3 (primary section heading)` (`font-size: 33px`, `line-height: 35.64px`, `font-weight: 400`, `letter-spacing: -0.99px`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 16px`, `font-weight: 400`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 16px`, `font-weight: 400`); CSS variables `--font-family-mono: Menlo, Monaco, Consolas, "Droid Sans Mono", monospace`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.25,1,.5,1)`, `cubic-bezier(0.2,0.6,0.35,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `input:-webkit-autofill:hover`**: `transition: background-color 5000s ease-in-out 0s` extracted from `santalarch-com` stylesheet.
- **Selector `:root`**: `transition: .5s var(--ease-out)` extracted from `santalarch-com` stylesheet.
- **Selector `html`**: `transition: --c-light-primary var(--transition),--c-light-secondary var(--...` extracted from `santalarch-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.25,1,.5,1)`)**: Governs interactive state transitions across `<header.header>` and `<section.cubes-wrap>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Santalarch                                 │
│ ====================================================================== │
│ [ <header.header> (1440x450px)        | Works Works · Services Servi ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero> (w=1440px)                              | │
│ | H1: Intent Before Image                                            | │
│ | Substrate: #f0f0f0 | Ink: #0f0f0f | Accent: #007aff                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.cubes-wrap>) max-w: 1440px                 | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Engineering as Foundation    |  | Material Intelligence        | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.approach>) — Detail as Discipline          | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.c2-sb>      ) | https://santalarch.com               │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 1rem)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.header>         ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.hero>) — 390px Vertical Lead                  | │
│ | H1: Intent Before Image                                            | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.cubes-wrap>) — 1-Col Stack                | │
│ | [ Item 1: Engineering as Foundation                              ] | │
│ | [ Item 2: Material Intelligence                                  ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.approach>) — 1-Col (Detail as Discipli)     | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.c2-sb>      ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.header> — `santalarch-com`)**:
   - Landmark `<header class="header difference">` (`1440x450px`) hosting `Santalarch` navigation (`Works Works · Services Services · Process Process · Company Company · Contact Contact`), DOM attributes (`data-theme="light"`, `data-v-fd5224ce`, `data-v-211bdc1c`, `data-v-52d76f34`), and stylesheet rule `before { box-sizing:border-box;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Intent Before Image`)**:
   - Landmark `<section class="hero">` presenting display lead `Intent Before Image` and copy excerpt *"This site uses cookies."* over `#f0f0f0` canvas and `#0f0f0f` ink.
3. **Primary Showcase & Content Grid (<section.cubes-wrap> — `Engineering as Foundation`)**:
   - Landmark `<section class="cubes-wrap">` rendering section `Engineering as Foundation` with copy *"Architectural studio built on uncompromising precision and intent"*, asset references (`entry.D7X7o5bn.css`, `CI8pdcr7.js`, `03be9e1c-9e63-48c6-b4db-59a6b0167...`, `ad.B18i8NGa.svg`), and grid rule `video { border:0;font-size:100%;font:inherit;margin:0;padding:0;vertical-align:b... }`.
4. **Interactive Detail & Feature Matrix (<section.approach> — `Material Intelligence`)**:
   - Landmark `<section class="approach grid-container">` framing `Material Intelligence` and `Detail as Discipline` (*"Architecture Shapes Perception"*) with `#ffffff` surface cards, `#007aff` accents, and `svg { display:block }`.
5. **Colophon & Global Directory Footer (<footer.c2-sb> — `https://santalarch.com`)**:
   - Landmark `<footer class="c2-sb">` anchoring `Santalarch` footer links (`Works Works · Services Services · Process Process · Company Company · Contact Contact`), copy *"Bold presence. Quiet execution."*, and `#f9f9f9` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: santalarch-com (Santalarch)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `santalarch-com` (**Santalarch** — `https://santalarch.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f0f0f0` / `#007aff`).
- **Identity & Domain Context**: Architectural studio built on uncompromising precision and intent.
- **Primary Substrate**: `#f0f0f0` (live computed `main` `background-color` (`computed_styles.json`)), **Primary Ink**: `#0f0f0f`, **Accent / Highlight**: `#007aff`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f0f0f0` (live computed `main` `background-color` (`computed_styles.json`)) paired with `#0f0f0f` primary typography and `#007aff` accents.
  - **Grounded Typographic Hierarchy**: Pairs `lil-gui` for display copy (`Intent Before Image`) with `Segoe UI` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 1rem`, padding `1rem`) with `cubic-bezier(.25,1,.5,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `santalarch-com` in your global stylesheet:

:root {
  /* Santalarch (santalarch-com) — Live-Grounded CSS Variables */
  --viewport-width: 1440; /* Layout / Spatial Grid Token (santalarch-com) */
  --viewport-height: 800; /* Layout / Spatial Grid Token (santalarch-com) */
  --font-helvetica: "Helvetica",sans-serif; /* Typography / Scale Token (santalarch-com) */
  --ease-out: cubic-bezier(.25,1,.5,1); /* Motion / Easing Token (santalarch-com) */
  --transition: .5s var(--ease-out); /* Motion / Easing Token (santalarch-com) */
  --transition-fast: .3s var(--ease-out); /* Motion / Easing Token (santalarch-com) */
  --transition-slow: .8s var(--ease-out); /* Motion / Easing Token (santalarch-com) */
  --c-base-light-primary: #f0f0f0; /* Canvas / Surface Token (santalarch-com) */
  --c-base-line-highlight: #f2f0f033; /* Canvas / Surface Token (santalarch-com) */
  --c-base-line-dark-bg: #f2f0f00d; /* Canvas / Surface Token (santalarch-com) */
  --c-pure-black: #000; /* Canvas / Surface Token (santalarch-com) */
  --c-pure-white: #fff; /* Canvas / Surface Token (santalarch-com) */
  --c-pure-black-rgb: 0,0,0; /* Canvas / Surface Token (santalarch-com) */
  --c-pure-black-0: rgba(var(--c-pure-black-rgb),0); /* Canvas / Surface Token (santalarch-com) */
  --c-light-primary: var(--c-base-light-primary); /* Canvas / Surface Token (santalarch-com) */
  --c-light-secondary: #f2f0f066; /* Canvas / Surface Token (santalarch-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f0f0f0` — grounded in live computed `main` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#0f0f0f` — grounded in live computed `main` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#ffffff` — grounded in `:hover { background-color: white }` (`#ffffff`)
- **Interactive Accent / Highlight**: `#007aff` — grounded in `:root { color: #007aff }`
- **Secondary / Muted Copy**: `#ebebeb` — grounded in `var(--text-color)` in `:root`
- **Structural Hairline Border**: `#f9f9f9` — grounded in `ui .controller.color .display:h... { border: #f9f9f9 }`
- **Variable Token (`--c-base-line-highlight`)**: `#f2f0f0` — grounded in `var(--c-base-line-highlight)` in `:root`
- **Variable Token (`--c-pure-black`)**: `#000000` — grounded in `var(--c-pure-black)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×900px` (single-viewport 100vh live capture (900px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×844px` (single-viewport 100vh live capture (844px), `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport)
- **Padding & Gutters**: `1rem` lateral canvas padding with `1rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 1rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `1rem` horizontal padding
- **Media Queries**: `@media (max-width:1023px)`, `@media screen and (max-width:1023px)and (orientation:landscape)`, `@media (min-width:1024px)`
- **Corner Radii**: `50%`, `2px`, `var(--scrollbar-width)`, `var(--widget-border-radius)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `lil-gui`
- **Body Font Stack**: `Segoe UI`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: rule `.title` (`line-height: calc(var(--title-heig...`, `font-weight: 600`)
- **H2 Section Rule**: live computed `h3 (primary section heading)` (`font-size: 33px`, `line-height: 35.64px`, `font-weight: 400`, `letter-spacing: -0.99px`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 16px`, `font-weight: 400`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 16px`, `font-weight: 400`); CSS variables `--font-family-mono: Menlo, Monaco, Consolas, "Droid Sans Mono", monospace`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `santalarch-com` (`Santalarch`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.header> — `santalarch-com`)**:
   - DOM & Selectors: Landmark `<header class="header difference">` (`1440x450px`) hosting `Santalarch` navigation (`Works Works · Services Services · Process Process · Company Company · Contact Contact`), DOM attributes (`data-theme="light"`, `data-v-fd5224ce`, `data-v-211bdc1c`, `data-v-52d76f34`), and stylesheet rule `before { box-sizing:border-box;margin:0;padding:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.header> — `santalarch-com`)` (`santalarch-com`) adapts across `@media (max-width:1023px)`, `@media screen and (max-width:1023px)and (orientation:landscape)`, `@media (min-width:1024px)` with `cubic-bezier(.25,1,.5,1)`, `cubic-bezier(0.2,0.6,0.35,1)` transitions and links `Works Works · Services Services · Process Process · Company Company · Contact Contact`.
2. **Hero Stage & Focal Lead (<section.hero> — `Intent Before Image`)**:
   - DOM & Selectors: Landmark `<section class="hero">` presenting display lead `Intent Before Image` and copy excerpt *"This site uses cookies."* over `#f0f0f0` canvas and `#0f0f0f` ink.
   - Responsive Contract: Hero stage (`1440×900px` desktop / `390×844px` mobile) sets `#f0f0f0` background with `#0f0f0f` headline `Intent Before Image`.
3. **Primary Showcase & Content Grid (<section.cubes-wrap> — `Engineering as Foundation`)**:
   - DOM & Selectors: Landmark `<section class="cubes-wrap">` rendering section `Engineering as Foundation` with copy *"Architectural studio built on uncompromising precision and intent"*, asset references (`entry.D7X7o5bn.css`, `CI8pdcr7.js`, `03be9e1c-9e63-48c6-b4db-59a6b0167...`, `ad.B18i8NGa.svg`), and grid rule `video { border:0;font-size:100%;font:inherit;margin:0;padding:0;vertical-align:b... }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.cubes-wrap> — `Engineering as Foundation`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 1rem`) on desktop and Single-column vertical stack at `390px` viewport width with `1rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.approach> — `Material Intelligence`)**:
   - DOM & Selectors: Landmark `<section class="approach grid-container">` framing `Material Intelligence` and `Detail as Discipline` (*"Architecture Shapes Perception"*) with `#ffffff` surface cards, `#007aff` accents, and `svg { display:block }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.approach> — `Material Intelligence`)` uses `50%`, `2px`, `var(--scrollbar-width)`, `var(--widget-border-radius)` radii, `#007aff` highlights, and assets (entry.D7X7o5bn.css, CI8pdcr7.js, 03be9e1c-9e63-48c6-b4db-59a6b0167...).
5. **Colophon & Global Directory Footer (<footer.c2-sb> — `https://santalarch.com`)**:
   - DOM & Selectors: Landmark `<footer class="c2-sb">` anchoring `Santalarch` footer links (`Works Works · Services Services · Process Process · Company Company · Contact Contact`), copy *"Bold presence. Quiet execution."*, and `#f9f9f9` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.c2-sb> — `https://santalarch.com`)` aligns to `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport) with `1rem` lateral canvas padding with `1rem` grid gap and attributes (data-theme="light", data-v-fd5224ce, data-v-211bdc1c).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"This site uses cookies."*
- Copy Excerpt 2: *"Architectural studio built on uncompromising precision and intent."*
- Copy Excerpt 3: *"Architecture Shapes Perception"*
- Copy Excerpt 4: *"Bold presence. Quiet execution."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.25,1,.5,1)`, `cubic-bezier(0.2,0.6,0.35,1)`
- **Extracted Stylesheet Rules (`santalarch-com`)**:
- `before { box-sizing:border-box;margin:0;padding:0 }`
- `video { border:0;font-size:100%;font:inherit;margin:0;padding:0;vertical-align:b... }`
- `svg { display:block }`
- `body { line-height:1 }`
- `q:before { content:"";content:none }`
- **Per-Selector Transition Rules**:
- **Selector `input:-webkit-autofill:hover`**: `transition: background-color 5000s ease-in-out 0s` extracted from `santalarch-com` stylesheet.
- **Selector `:root`**: `transition: .5s var(--ease-out)` extracted from `santalarch-com` stylesheet.
- **Selector `html`**: `transition: --c-light-primary var(--transition),--c-light-secondary var(--...` extracted from `santalarch-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.25,1,.5,1)`)**: Governs interactive state transitions across `<header.header>` and `<section.cubes-wrap>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `santalarch-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
