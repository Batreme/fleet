---
title: "UI Prompt Blueprint: morphowater-com"
date: 2026-11-15
target: "[[overview|morphowater-com]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#d0edff` canvas, `#101820` ink, `#ffffff` accent)"
---

# UI Design System & Master Generation Blueprint: morphowater-com

> **MORPHO · Natural Spring Water from Costa Rica** (https://morphowater.com) — Discover MORPHO natural spring water from Costa Rica. Explore our source, still water in 12 oz aluminum cans, and our upcoming sparkling...

![Desktop Viewport Capture (1440x24479)](file:///root/projects/fleet/wiki/targets/morphowater-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **MORPHO · Natural Spring Water from Costa Rica** (`https://morphowater.com`). Discover MORPHO natural spring water from Costa Rica. Explore our source, still water in 12 oz aluminum cans, and our upcoming sparkling...
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#d0edff` canvas, `#101820` ink, `#ffffff` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#d0edff` (`var(--brand-flight)` in `:root`) paired with `#101820` primary typography and `#ffffff` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Publico Headline` for display copy (`A world within.`) with `Gotham` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `700px` container bounds (`gap: 7px`, padding `8px`) with `cubic-bezier(.2,.7,.2,1)` easing.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/morphowater-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×24479px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `700px` extracted from `morphowater-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `8px` lateral canvas padding with `7px` grid gap.
- **Border Radius Scale**: `50%`, `30px`, `40px`, `20px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 700px`, `gap: 7px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `8px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (prefers-reduced-motion:no-preference)`, `@media (max-width:700px)`, `@media (max-height:650px) and (min-width:701px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#d0edff` | `var(--brand-flight)` in `:root` |
| **Primary Typography Ink** | `#0a127b` | `var(--brand-reserve)` in `:root` |
| **Elevated Surface / Card Substrate** | `#0056d4` | `var(--brand-blue)` in `:root` |
| **Interactive Accent / Highlight** | `#ffffff` | `var(--brand-purity)` in `:root` |
| **Secondary / Muted Copy** | `#101820` | `var(--brand-premium)` in `:root` |
| **Structural Hairline Border** | `#6b7080` | `var(--muted)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--brand-flight` | `#d0edff` | Canvas / Surface Token |
| `--brand-reserve` | `#0a127b` | Brand / Palette Token |
| `--brand-blue` | `#0056d4` | Brand / Palette Token |
| `--brand-purity` | `#ffffff` | Brand / Palette Token |
| `--brand-premium` | `#101820` | Brand / Palette Token |
| `--ink` | `var(--brand-premium)` | Typography Ink Token |
| `--paper` | `var(--brand-purity)` | Canvas / Surface Token |
| `--flow-serif` | `"Publico Headline",Georgia,serif` | Typography / Scale Token |
| `--brand-secondary` | `color-mix(in srgb,var(--brand-premium) 68%,white)` | Brand / Palette Token |
| `--brand-rule` | `color-mix(in srgb,var(--brand-premium) 20%,transparent)` | Brand / Palette Token |
| `--read-progress` | `0` | Design System Custom Token |
| `--read-rest-opacity` | `.34` | Design System Custom Token |
| `--word-on` | `clamp(0,calc((var(--read-progress) - var(--word-start))*40),1)` | Design System Custom Token |
| `--flow-surface` | `#101820` | Canvas / Surface Token |
| `--panel-opacity` | `1` | Design System Custom Token |
| `--copy-opacity` | `1` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Publico Headline`.
- **Primary Body Stack**: `Gotham`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`font-size: clamp(46px,6.1vw,94px)`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 44px`).
- **Body Copy**: CSS variables `--body-reveal: 1`; rule `p` (`font-size: 12px`).
- **Metadata & Navigation Labels**: rule `small` (`font-size: 8px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.2,.7,.2,1)`, `cubic-bezier(.18,.55,.3,1)`, `cubic-bezier(.16,1,.3,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.scroll-reading-word`**: `transition: color .1s linear` extracted from `morphowater-com` stylesheet.
- **Selector `.flow-page>.flow-header`**: `transition: color 1s ease` extracted from `morphowater-com` stylesheet.
- **Selector `.flow-page>.flow-header:before`**: `transition: background 1s ease,opacity 1s ease` extracted from `morphowater-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.2,.7,.2,1)`)**: Governs interactive state transitions across `<header.morpho-header>` and `<section.territory-journey>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.flow-journey>` and `<section.territory-journey>` interactive targets.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — MORPHO · Natural Spring Water from Costa R │
│ ====================================================================== │
│ [ <header.morpho-header>   | The beginning · The MORPHO life · Loca ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.flow-journey>                               |   │
│ | H1: A world within.                                              |   │
│ | Substrate: #d0edff    | Ink: #101820    | Accent: #ffffff        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.territory-journey) max-w: 700px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | A small click. A world opens |  | Let the outside in.          | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 7px   ) | │
│ | [<header.morpho-hea] -> [<section.flow-jour] -> [<section.territory] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.flow-footer>  ) | https://morphowater.com            │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.morpho-header> — `morphowater-com`)**:
   - Landmark `<header class="morpho-header">` hosting `MORPHO · Natural Spring Water from C` navigation (`The beginning · The MORPHO life · Location · The Nicoya way · Inside MORPHO`), DOM attributes (`data-journey-critical`, `data-journey-styles`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.flow-page em { font-family:var(--flow-serif);font-style:italic;font-weight:300;font-syn... }`.
2. **Hero Stage & Focal Lead (<section.flow-journey> — `A world within.`)**:
   - Landmark `<section class="flow-journey">` presenting display lead `A world within.` and copy excerpt *"Skip the introduction"* over `#d0edff` canvas and `#101820` ink.
3. **Primary Showcase & Content Grid (<section.territory-journey> — `A small click. A world opens.`)**:
   - Landmark `<section class="territory-journey coastal-story">` rendering section `A small click. A world opens.` with copy *"NATURAL COSTA RICAN SPRING WATER"*, asset references (`gotham-light-common.woff2`, `gotham-book-common.woff2`, `publico-headline-light-italic-com...`, `wordmark-white.webp`), and grid rule `.flow-page .flow-header img { filter:none }`.
4. **Interactive Detail & Feature Matrix (<article.territory-panel> — `Let the outside in.`)**:
   - Landmark `<article class="territory-panel">` framing `Let the outside in.` and `Back to what matters.` (*"Natural spring water from Costa Rica."*) with `#0056d4` surface cards, `#ffffff` accents, and `.flow-page .flow-skip { color:var(--brand-premium) }`.
5. **Colophon & Global Directory Footer (<footer.flow-footer> — `https://morphowater.com`)**:
   - Landmark `<footer class="flow-footer morpho-footer">` anchoring `MORPHO · Natural Spring Water fr` footer links (`The beginning · The MORPHO life · Location · The Nicoya way · Inside MORPHO`), copy *"Still and sparkling. In aluminum cans."*, and `#6b7080` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: morphowater-com (MORPHO · Natural Spring Water from Costa Rica)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `morphowater-com` (**MORPHO · Natural Spring Water from Costa Rica** — `https://morphowater.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#d0edff` canvas, `#101820` ink, `#ffffff` accent).
- **Identity & Domain Context**: Discover MORPHO natural spring water from Costa Rica. Explore our source, still water in 12 oz aluminum cans, and our upcoming sparkling...
- **Primary Substrate**: `#d0edff` (`var(--brand-flight)` in `:root`), **Primary Ink**: `#101820`, **Accent / Highlight**: `#ffffff`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#d0edff` (`var(--brand-flight)` in `:root`) paired with `#101820` primary typography and `#ffffff` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Publico Headline` for display copy (`A world within.`) with `Gotham` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `700px` container bounds (`gap: 7px`, padding `8px`) with `cubic-bezier(.2,.7,.2,1)` easing.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `morphowater-com` in your global stylesheet:

:root {
  /* MORPHO · Natural Spring Water from Costa Rica (morphowater-com) — Ground-Truth Extracted CSS Variables */
  --brand-flight: #d0edff; /* Canvas / Surface Token (morphowater-com) */
  --brand-reserve: #0a127b; /* Brand / Palette Token (morphowater-com) */
  --brand-blue: #0056d4; /* Brand / Palette Token (morphowater-com) */
  --brand-purity: #ffffff; /* Brand / Palette Token (morphowater-com) */
  --brand-premium: #101820; /* Brand / Palette Token (morphowater-com) */
  --ink: var(--brand-premium); /* Typography Ink Token (morphowater-com) */
  --paper: var(--brand-purity); /* Canvas / Surface Token (morphowater-com) */
  --flow-serif: "Publico Headline",Georgia,serif; /* Typography / Scale Token (morphowater-com) */
  --brand-secondary: color-mix(in srgb,var(--brand-premium) 68%,white); /* Brand / Palette Token (morphowater-com) */
  --brand-rule: color-mix(in srgb,var(--brand-premium) 20%,transparent); /* Brand / Palette Token (morphowater-com) */
  --read-progress: 0; /* Design System Custom Token (morphowater-com) */
  --read-rest-opacity: .34; /* Design System Custom Token (morphowater-com) */
  --word-on: clamp(0,calc((var(--read-progress) - var(--word-start))*40),1); /* Design System Custom Token (morphowater-com) */
  --flow-surface: #101820; /* Canvas / Surface Token (morphowater-com) */
  --panel-opacity: 1; /* Design System Custom Token (morphowater-com) */
  --copy-opacity: 1; /* Typography Ink Token (morphowater-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#d0edff` — grounded in `var(--brand-flight)` in `:root`
- **Primary Typography Ink**: `#0a127b` — grounded in `var(--brand-reserve)` in `:root`
- **Elevated Surface / Card Substrate**: `#0056d4` — grounded in `var(--brand-blue)` in `:root`
- **Interactive Accent / Highlight**: `#ffffff` — grounded in `var(--brand-purity)` in `:root`
- **Secondary / Muted Copy**: `#101820` — grounded in `var(--brand-premium)` in `:root`
- **Structural Hairline Border**: `#6b7080` — grounded in `var(--muted)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×24479px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `700px` extracted from `morphowater-com` stylesheet
- **Padding & Gutters**: `8px` lateral canvas padding with `7px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 700px`, `gap: 7px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `8px` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (prefers-reduced-motion:no-preference)`, `@media (max-width:700px)`, `@media (max-height:650px) and (min-width:701px)`
- **Corner Radii**: `50%`, `30px`, `40px`, `20px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Publico Headline`
- **Body Font Stack**: `Gotham`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: rule `h1` (`font-size: clamp(46px,6.1vw,94px)`)
- **H2 Section Rule**: rule `h2` (`font-size: 44px`)
- **Body Copy Rule**: CSS variables `--body-reveal: 1`; rule `p` (`font-size: 12px`)
- **Metadata & Index Rule**: rule `small` (`font-size: 8px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `morphowater-com` (`MORPHO · Natural Spring Water from Costa Rica`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.morpho-header> — `morphowater-com`)**:
   - DOM & Selectors: Landmark `<header class="morpho-header">` hosting `MORPHO · Natural Spring Water from C` navigation (`The beginning · The MORPHO life · Location · The Nicoya way · Inside MORPHO`), DOM attributes (`data-journey-critical`, `data-journey-styles`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.flow-page em { font-family:var(--flow-serif);font-style:italic;font-weight:300;font-syn... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.morpho-header> — `morphowater-com`)` (`morphowater-com`) adapts across `@media (prefers-reduced-motion:reduce)`, `@media (prefers-reduced-motion:no-preference)`, `@media (max-width:700px)`, `@media (max-height:650px) and (min-width:701px)` with `cubic-bezier(.2,.7,.2,1)`, `cubic-bezier(.18,.55,.3,1)`, `cubic-bezier(.16,1,.3,1)` transitions and links `The beginning · The MORPHO life · Location · The Nicoya way · Inside MORPHO`.
2. **Hero Stage & Focal Lead (<section.flow-journey> — `A world within.`)**:
   - DOM & Selectors: Landmark `<section class="flow-journey">` presenting display lead `A world within.` and copy excerpt *"Skip the introduction"* over `#d0edff` canvas and `#101820` ink.
   - Responsive Contract: Hero stage (`1440×24479px` desktop / `390×2400px` mobile) sets `#d0edff` background with `#101820` headline `A world within.`.
3. **Primary Showcase & Content Grid (<section.territory-journey> — `A small click. A world opens.`)**:
   - DOM & Selectors: Landmark `<section class="territory-journey coastal-story">` rendering section `A small click. A world opens.` with copy *"NATURAL COSTA RICAN SPRING WATER"*, asset references (`gotham-light-common.woff2`, `gotham-book-common.woff2`, `publico-headline-light-italic-com...`, `wordmark-white.webp`), and grid rule `.flow-page .flow-header img { filter:none }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.territory-journey> — `A small click. A world opens.`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 700px`, `gap: 7px`) on desktop and Single-column vertical stack at `390px` viewport width with `8px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.territory-panel> — `Let the outside in.`)**:
   - DOM & Selectors: Landmark `<article class="territory-panel">` framing `Let the outside in.` and `Back to what matters.` (*"Natural spring water from Costa Rica."*) with `#0056d4` surface cards, `#ffffff` accents, and `.flow-page .flow-skip { color:var(--brand-premium) }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.territory-panel> — `Let the outside in.`)` uses `50%`, `30px`, `40px`, `20px` radii, `#ffffff` highlights, and assets (gotham-light-common.woff2, gotham-book-common.woff2, publico-headline-light-italic-com...).
5. **Colophon & Global Directory Footer (<footer.flow-footer> — `https://morphowater.com`)**:
   - DOM & Selectors: Landmark `<footer class="flow-footer morpho-footer">` anchoring `MORPHO · Natural Spring Water fr` footer links (`The beginning · The MORPHO life · Location · The Nicoya way · Inside MORPHO`), copy *"Still and sparkling. In aluminum cans."*, and `#6b7080` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.flow-footer> — `https://morphowater.com`)` aligns to `700px` extracted from `morphowater-com` stylesheet with `8px` lateral canvas padding with `7px` grid gap and attributes (data-journey-critical, data-journey-styles, data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Skip the introduction"*
- Copy Excerpt 2: *"NATURAL COSTA RICAN SPRING WATER"*
- Copy Excerpt 3: *"Natural spring water from Costa Rica."*
- Copy Excerpt 4: *"Still and sparkling. In aluminum cans."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.2,.7,.2,1)`, `cubic-bezier(.18,.55,.3,1)`, `cubic-bezier(.16,1,.3,1)`
- **Extracted Stylesheet Rules (`morphowater-com`)**:
- `.flow-page em { font-family:var(--flow-serif);font-style:italic;font-weight:300;font-syn... }`
- `.flow-page .flow-header img { filter:none }`
- `.flow-page .flow-skip { color:var(--brand-premium) }`
- `.flow-page .flow-eyebrow { color:var(--brand-reserve);font-weight:500 }`
- `.flow-page .flow-shop { border-bottom-color:ffffff60 }`
- **Per-Selector Transition Rules**:
- **Selector `.scroll-reading-word`**: `transition: color .1s linear` extracted from `morphowater-com` stylesheet.
- **Selector `.flow-page>.flow-header`**: `transition: color 1s ease` extracted from `morphowater-com` stylesheet.
- **Selector `.flow-page>.flow-header:before`**: `transition: background 1s ease,opacity 1s ease` extracted from `morphowater-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.2,.7,.2,1)`)**: Governs interactive state transitions across `<header.morpho-header>` and `<section.territory-journey>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.flow-journey>` and `<section.territory-journey>` interactive targets.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `morphowater-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
