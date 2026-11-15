---
title: "UI Prompt Blueprint: douglus-co"
date: 2026-11-15
target: "[[overview|douglus-co]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#fefff8` / `#ebebeb`)"
---

# UI Design System & Master Generation Blueprint: douglus-co

> **Douglus Nguyen — Web Designer from Vietnam** (https://douglus.co) — Independent web designer based in Vietnam, focused on website design, interaction design, and front-end development.

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Douglus Nguyen — Web Designer from Vietnam** (`https://douglus.co`). Independent web designer based in Vietnam, focused on website design, interaction design, and front-end development.
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#fefff8` / `#ebebeb`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fefff8` (`var(--white-color)` in `:root`) paired with `#000` primary typography and `#ebebeb` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Neue Montreal` for display copy (`D ouglus N guyen`) with `Roxborough CF` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `var(--v-w)` container bounds (`gap: .5rem`, padding `.75rem`) with `cubic-bezier(.25,1,.5,1)` easing and Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `var(--v-w)` extracted from `douglus-co` stylesheet.
- **Canvas Lateral Padding & Spacing**: `.75rem` lateral canvas padding with `.5rem` grid gap.
- **Border Radius Scale**: `10px`, `50%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--v-w)`, `gap: .5rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `.75rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (width<=23.75rem)`, `@media screen and (width>=1025px)`, `@media (prefers-reduced-motion:no-preference)`, `@media (prefers-reduced-motion:reduce)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fefff8` | `var(--white-color)` in `:root` |
| **Primary Typography Ink** | `#1e1e1e` | `var(--black-color)` in `:root` |
| **Elevated Surface / Card Substrate** | `#292724` | `var(--neutral-color)` in `:root` |
| **Interactive Accent / Highlight** | `#ebebeb` | `var(--muted-color)` in `:root` |
| **Secondary / Muted Copy** | `#1c1d20` | `var(--nf-deep)` in `:root` |
| **Structural Hairline Border** | `#000` | `.c-scrollbar_thumb { background-color: #000 }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--page-padding` | `clamp(20px, 2.3vw, 40px)` | Layout / Spatial Grid Token |
| `--header-height` | `112px` | Layout / Spatial Grid Token |
| `--footer-right-width` | `clamp(38.75rem, 45.14vw, 48.75rem)` | Layout / Spatial Grid Token |
| `--white-color` | `#fefff8` | Canvas / Surface Token |
| `--black-color` | `#1e1e1e` | Canvas / Surface Token |
| `--neutral-color` | `#292724` | Brand / Palette Token |
| `--muted-color` | `#ebebeb` | Brand / Palette Token |
| `--default-easing` | `cubic-bezier(.25, 1, .5, 1)` | Motion / Easing Token |
| `--gw` | `4.16667vw` | Dimension / Scale Token |
| `--rv-ease` | `var(--default-easing)` | Motion / Easing Token |
| `--rv-ease-img` | `cubic-bezier(.76, 0, .24, 1)` | Motion / Easing Token |
| `--rv-d-s` | `.5s` | Motion / Timing Token |
| `--rv-d-m` | `.7s` | Motion / Timing Token |
| `--rv-d-l` | `.9s` | Motion / Timing Token |
| `--rv-step-t` | `40ms` | Motion / Timing Token |
| `--rv-step-l` | `80ms` | Motion / Timing Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Neue Montreal`.
- **Primary Body Stack**: `Roxborough CF`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `100%`, `clamp(.75rem,.81vw,.875rem)`, `clamp(.75rem,.92vw,1rem)`, `var(--menu-link-size)`, `clamp(.75rem,.59375rem + .32vw,.9...`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `100%`, `clamp(.75rem,.81vw,.875rem)`, `clamp(.75rem,.92vw,1rem)`, `var(--menu-link-size)`, `clamp(.75rem,.59375rem + .32vw,.9...`).
- **Body Copy**: rule `p` (`font-size: clamp(.875rem, var(--gw) * .2...`, `line-height: 1.2`, `letter-spacing: -.045em`, `font-weight: 400`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `100%`, `clamp(.75rem,.81vw,.875rem)`, `clamp(.75rem,.92vw,1rem)`, `var(--menu-link-size)`, `clamp(.75rem,.59375rem + .32vw,.9...`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.25,1,.5,1)`, `cubic-bezier(.76,0,.24,1)`, `cubic-bezier(.17,.67,.1,.99)`.

### Per-Element Transition & Choreography Rules
- **Selector `.c-scrollbar`**: `transition: transform .3s,opacity .3s` extracted from `douglus-co` stylesheet.
- **Selector `.is-in))~:where([data-rv=line])>:...`**: `transition: translate var(--rv-d,var(--rv-d-m)) var(--rv-e,var(--rv-ease))...` extracted from `douglus-co` stylesheet.
- **Selector `.is-in))~:where([data-rv=rise])`**: `transition: translate var(--rv-d,var(--rv-d-m)) var(--rv-e,var(--rv-ease))...` extracted from `douglus-co` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.25,1,.5,1)`)**: Governs interactive state transitions across `<header.site-header>` and `<section.home-hero>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Douglus Nguyen — Web Designer from Vietnam │
│ ====================================================================== │
│ [ <header.site-header>     | H ome · W orks · P layground · A bout  ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.home-hero>                                  |   │
│ | H1: D ouglus N guyen                                             |   │
│ | Substrate: #fefff8    | Ink: #000       | Accent: #ebebeb        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.home-hero>       ) max-w: var(--v-w)     |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Hello, Welcome to my Portfol |  | Open for collaborations      | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .5rem ) | │
│ | [<header.site-heade] -> [<section.home-hero] -> [<section.home-hero] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.preloader__sub) | https://douglus.co                 │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.site-header> — `douglus-co`)**:
   - Landmark `<header class="site-header">` hosting `Douglus Nguyen — Web Designer from V` navigation (`H ome · W orks · P layground · A bout · C ontact`), DOM attributes (`data-scroll-direction="vertical"`, `data-barba="wrapper"`, `data-preloader`, `data-fragment="1"`), and stylesheet rule `video { font-size:100%;font:inherit;vertical-align:baseline;border:0;margin:0;pa... }`.
2. **Hero Stage & Focal Lead (<section.home-hero> — `D ouglus N guyen`)**:
   - Landmark `<section class="home-hero">` presenting display lead `D ouglus N guyen` and copy excerpt *"Hello, Welcome to my Portfolio"* over `#fefff8` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.home-hero> — `Hello, Welcome to my Portfolio`)**:
   - Landmark `<section class="home-hero">` rendering section `Hello, Welcome to my Portfolio` with copy *"Open for collaborations"*, asset references (`favicon.ico`, `favicon-32x32.png`, `favicon-16x16.png`, `apple-touch-icon.png`), and grid rule `section { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.home-hero> — `Open for collaborations`)**:
   - Landmark `<section class="home-hero">` framing `Open for collaborations` and `Menu Menu Close Close` (*"Menu Menu Close Close"*) with `#292724` surface cards, `#ebebeb` accents, and `body { line-height:1 }`.
5. **Colophon & Global Directory Footer (<footer.preloader__subject> — `https://douglus.co`)**:
   - Landmark `<footer class="preloader__subject">` anchoring `Douglus Nguyen — Web Designer fr` footer links (`H ome · W orks · P layground · A bout · C ontact`), copy *"Just a designer & developer trying to make good things for t"*, and `#000` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: douglus-co (Douglus Nguyen — Web Designer from Vietnam)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `douglus-co` (**Douglus Nguyen — Web Designer from Vietnam** — `https://douglus.co`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fefff8` / `#ebebeb`).
- **Identity & Domain Context**: Independent web designer based in Vietnam, focused on website design, interaction design, and front-end development.
- **Primary Substrate**: `#fefff8` (`var(--white-color)` in `:root`), **Primary Ink**: `#000`, **Accent / Highlight**: `#ebebeb`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fefff8` (`var(--white-color)` in `:root`) paired with `#000` primary typography and `#ebebeb` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Neue Montreal` for display copy (`D ouglus N guyen`) with `Roxborough CF` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `var(--v-w)` container bounds (`gap: .5rem`, padding `.75rem`) with `cubic-bezier(.25,1,.5,1)` easing and Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `douglus-co` in your global stylesheet:

:root {
  /* Douglus Nguyen — Web Designer from Vietnam (douglus-co) — Ground-Truth Extracted CSS Variables */
  --page-padding: clamp(20px, 2.3vw, 40px); /* Layout / Spatial Grid Token (douglus-co) */
  --header-height: 112px; /* Layout / Spatial Grid Token (douglus-co) */
  --footer-right-width: clamp(38.75rem, 45.14vw, 48.75rem); /* Layout / Spatial Grid Token (douglus-co) */
  --white-color: #fefff8; /* Canvas / Surface Token (douglus-co) */
  --black-color: #1e1e1e; /* Canvas / Surface Token (douglus-co) */
  --neutral-color: #292724; /* Brand / Palette Token (douglus-co) */
  --muted-color: #ebebeb; /* Brand / Palette Token (douglus-co) */
  --default-easing: cubic-bezier(.25, 1, .5, 1); /* Motion / Easing Token (douglus-co) */
  --gw: 4.16667vw; /* Dimension / Scale Token (douglus-co) */
  --rv-ease: var(--default-easing); /* Motion / Easing Token (douglus-co) */
  --rv-ease-img: cubic-bezier(.76, 0, .24, 1); /* Motion / Easing Token (douglus-co) */
  --rv-d-s: .5s; /* Motion / Timing Token (douglus-co) */
  --rv-d-m: .7s; /* Motion / Timing Token (douglus-co) */
  --rv-d-l: .9s; /* Motion / Timing Token (douglus-co) */
  --rv-step-t: 40ms; /* Motion / Timing Token (douglus-co) */
  --rv-step-l: 80ms; /* Motion / Timing Token (douglus-co) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fefff8` — grounded in `var(--white-color)` in `:root`
- **Primary Typography Ink**: `#1e1e1e` — grounded in `var(--black-color)` in `:root`
- **Elevated Surface / Card Substrate**: `#292724` — grounded in `var(--neutral-color)` in `:root`
- **Interactive Accent / Highlight**: `#ebebeb` — grounded in `var(--muted-color)` in `:root`
- **Secondary / Muted Copy**: `#1c1d20` — grounded in `var(--nf-deep)` in `:root`
- **Structural Hairline Border**: `#000` — grounded in `.c-scrollbar_thumb { background-color: #000 }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `var(--v-w)` extracted from `douglus-co` stylesheet
- **Padding & Gutters**: `.75rem` lateral canvas padding with `.5rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--v-w)`, `gap: .5rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `.75rem` horizontal padding
- **Media Queries**: `@media (width<=23.75rem)`, `@media screen and (width>=1025px)`, `@media (prefers-reduced-motion:no-preference)`, `@media (prefers-reduced-motion:reduce)`
- **Corner Radii**: `10px`, `50%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Neue Montreal`
- **Body Font Stack**: `Roxborough CF`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `100%`, `clamp(.75rem,.81vw,.875rem)`, `clamp(.75rem,.92vw,1rem)`, `var(--menu-link-size)`, `clamp(.75rem,.59375rem + .32vw,.9...`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `100%`, `clamp(.75rem,.81vw,.875rem)`, `clamp(.75rem,.92vw,1rem)`, `var(--menu-link-size)`, `clamp(.75rem,.59375rem + .32vw,.9...`)
- **Body Copy Rule**: rule `p` (`font-size: clamp(.875rem, var(--gw) * .2...`, `line-height: 1.2`, `letter-spacing: -.045em`, `font-weight: 400`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `100%`, `clamp(.75rem,.81vw,.875rem)`, `clamp(.75rem,.92vw,1rem)`, `var(--menu-link-size)`, `clamp(.75rem,.59375rem + .32vw,.9...`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `douglus-co` (`Douglus Nguyen — Web Designer from Vietnam`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.site-header> — `douglus-co`)**:
   - DOM & Selectors: Landmark `<header class="site-header">` hosting `Douglus Nguyen — Web Designer from V` navigation (`H ome · W orks · P layground · A bout · C ontact`), DOM attributes (`data-scroll-direction="vertical"`, `data-barba="wrapper"`, `data-preloader`, `data-fragment="1"`), and stylesheet rule `video { font-size:100%;font:inherit;vertical-align:baseline;border:0;margin:0;pa... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.site-header> — `douglus-co`)` (`douglus-co`) adapts across `@media (width<=23.75rem)`, `@media screen and (width>=1025px)`, `@media (prefers-reduced-motion:no-preference)`, `@media (prefers-reduced-motion:reduce)` with `cubic-bezier(.25,1,.5,1)`, `cubic-bezier(.76,0,.24,1)`, `cubic-bezier(.17,.67,.1,.99)` transitions and links `H ome · W orks · P layground · A bout · C ontact`.
2. **Hero Stage & Focal Lead (<section.home-hero> — `D ouglus N guyen`)**:
   - DOM & Selectors: Landmark `<section class="home-hero">` presenting display lead `D ouglus N guyen` and copy excerpt *"Hello, Welcome to my Portfolio"* over `#fefff8` canvas and `#000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#fefff8` background with `#000` headline `D ouglus N guyen`.
3. **Primary Showcase & Content Grid (<section.home-hero> — `Hello, Welcome to my Portfolio`)**:
   - DOM & Selectors: Landmark `<section class="home-hero">` rendering section `Hello, Welcome to my Portfolio` with copy *"Open for collaborations"*, asset references (`favicon.ico`, `favicon-32x32.png`, `favicon-16x16.png`, `apple-touch-icon.png`), and grid rule `section { display:block }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.home-hero> — `Hello, Welcome to my Portfolio`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--v-w)`, `gap: .5rem`) on desktop and Single-column vertical stack at `390px` viewport width with `.75rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.home-hero> — `Open for collaborations`)**:
   - DOM & Selectors: Landmark `<section class="home-hero">` framing `Open for collaborations` and `Menu Menu Close Close` (*"Menu Menu Close Close"*) with `#292724` surface cards, `#ebebeb` accents, and `body { line-height:1 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.home-hero> — `Open for collaborations`)` uses `10px`, `50%` radii, `#ebebeb` highlights, and assets (favicon.ico, favicon-32x32.png, favicon-16x16.png).
5. **Colophon & Global Directory Footer (<footer.preloader__subject> — `https://douglus.co`)**:
   - DOM & Selectors: Landmark `<footer class="preloader__subject">` anchoring `Douglus Nguyen — Web Designer fr` footer links (`H ome · W orks · P layground · A bout · C ontact`), copy *"Just a designer & developer trying to make good things for t"*, and `#000` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.preloader__subject> — `https://douglus.co`)` aligns to `var(--v-w)` extracted from `douglus-co` stylesheet with `.75rem` lateral canvas padding with `.5rem` grid gap and attributes (data-scroll-direction="vertical", data-barba="wrapper", data-preloader).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Hello, Welcome to my Portfolio"*
- Copy Excerpt 2: *"Open for collaborations"*
- Copy Excerpt 3: *"Menu Menu Close Close"*
- Copy Excerpt 4: *"Just a designer & developer trying to make good things for the web."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.25,1,.5,1)`, `cubic-bezier(.76,0,.24,1)`, `cubic-bezier(.17,.67,.1,.99)`
- **Extracted Stylesheet Rules (`douglus-co`)**:
- `video { font-size:100%;font:inherit;vertical-align:baseline;border:0;margin:0;pa... }`
- `section { display:block }`
- `body { line-height:1 }`
- `q:after { content:"";content:none }`
- `table { border-collapse:collapse;border-spacing:0 }`
- **Per-Selector Transition Rules**:
- **Selector `.c-scrollbar`**: `transition: transform .3s,opacity .3s` extracted from `douglus-co` stylesheet.
- **Selector `.is-in))~:where([data-rv=line])>:...`**: `transition: translate var(--rv-d,var(--rv-d-m)) var(--rv-e,var(--rv-ease))...` extracted from `douglus-co` stylesheet.
- **Selector `.is-in))~:where([data-rv=rise])`**: `transition: translate var(--rv-d,var(--rv-d-m)) var(--rv-e,var(--rv-ease))...` extracted from `douglus-co` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.25,1,.5,1)`)**: Governs interactive state transitions across `<header.site-header>` and `<section.home-hero>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `douglus-co`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
