---
title: "UI Prompt Blueprint: explorajourneys-com_int-en-explora-journal"
date: 2026-11-23
captured_at: 2026-11-23
target: "explorajourneys-com_int-en-explora-journal"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#f4f2ef` canvas, `#222222` ink, `#9c441d` accent)"
---

# UI Design System & Master Generation Blueprint: explorajourneys-com_int-en-explora-journal

> **The Explora Journal, A Magazine by Explora Journeys** (https://explorajourneys.com/int/en/explora-journal) — Step aboard The Explora Journal for stories of ships and destinations, from wellness and dining to ports and cultures, told through the O...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **The Explora Journal, A Magazine by Explora Journeys** (`https://explorajourneys.com/int/en/explora-journal`). Step aboard The Explora Journal for stories of ships and destinations, from wellness and dining to ports and cultures, told through the O...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#f4f2ef` canvas, `#222222` ink, `#9c441d` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f4f2ef` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#222222` primary typography and `#9c441d` accents.
  - **Grounded Typographic Hierarchy**: Pairs `WT Monarch Nova` for display copy (`The Explora Journal`) with `Shapiro` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1364px` container bounds (`gap: 30px`, padding `.5rem`) with `cubic-bezier(.215,.61,.355,1)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1364px` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `.5rem` lateral canvas padding with `30px` grid gap.
- **Border Radius Scale**: `5px`, `50%`, `7px`, `3px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1364px`, `gap: 30px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `.5rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:reduce),print`, `@media only screen and (max-width:768px)`, `@media only screen and (max-width:360px)`, `@media only screen and (min-width:768px) and (max-width:1024px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f4f2ef` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#222222` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `.cmp-search__results { background: #ffffff }` |
| **Interactive Accent / Highlight** | `#9c441d` | `.cta-light-scroll:hover { color: #9c441d }` |
| **Secondary / Muted Copy** | `#866d4b` | live computed `a` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#cccccc` | `.cmp-search__loading-indicator { border: #cccccc }` |
| **Variable Token (`--swiper-theme-color`)** | `#007aff` | `var(--swiper-theme-color)` in stylesheet |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--animate-duration` | `1s` | Motion / Easing Token |
| `--animate-delay` | `1s` | Motion / Easing Token |
| `--animate-repeat` | `1` | Motion / Easing Token |
| `--alert-height` | `0px` | Layout / Spatial Grid Token |
| `--menu-height-desktop` | `95px` | Layout / Spatial Grid Token |
| `--menu-height-mobile` | `80px` | Layout / Spatial Grid Token |
| `--partner-header-height` | `0px` | Layout / Spatial Grid Token |
| `--hero-component-height` | `calc(100svh - 80px)` | Layout / Spatial Grid Token |
| `--hero-component-height-full` | `var(--hero-component-height)` | Layout / Spatial Grid Token |
| `--contact-banner-height` | `0px` | Layout / Spatial Grid Token |
| `--swiper-theme-color` | `#007aff` | Brand / Palette Token |
| `--explorajourneys--bg` | `#f4f2ef` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--explorajourneys--ink` | `#222222` | Primary Typography Ink (computed-derived) |
| `--explorajourneys--surface` | `#ffffff` | Surface Substrate (computed-derived) |
| `--explorajourneys--accent` | `#9c441d` | Interactive Accent (computed-derived) |
| `--explorajourneys--muted` | `#866d4b` | Secondary Ink (computed-derived) |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `WT Monarch Nova`.
- **Primary Body Stack**: `Shapiro`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 40.05px`, `line-height: 56.07px`, `font-weight: 400`); rule `.title` (`font-size: 24px`, `font-weight: 400`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 19.95px`, `line-height: 27.93px`, `font-weight: 400`); rule `h2` (`font-size: 1.5em`, `font-weight: bold`).
- **Body Copy**: live computed `body` (`font-size: 15px`, `line-height: 26px`, `font-weight: 400`); rule `p` (`font-size: 13px`, `line-height: 20px`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 15px`, `line-height: 26px`, `font-weight: 400`); rule `.label` (`font-size: 9pt`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.215,.61,.355,1)`, `cubic-bezier(.755,.05,.855,.06)`, `cubic-bezier(.55,.055,.675,.19)`.

### Per-Element Transition & Choreography Rules
- **Selector `print`**: `transition: 1ms!important` extracted from `explorajourneys-com_int-en-explora-journal` stylesheet.
- **Selector `80%`**: `transition: cubic-bezier(.215,.61,.355,1)` extracted from `explorajourneys-com_int-en-explora-journal` stylesheet.
- **Selector `80%`**: `transition: cubic-bezier(.215,.61,.355,1)` extracted from `explorajourneys-com_int-en-explora-journal` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.215,.61,.355,1)`)**: Governs interactive state transitions across `<header.experiencefragment>` and `<section.emag-home-grid>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — The Explora Journal, A Magazine by Explora │
│ ====================================================================== │
│ [ <header.experiencefrag (1440x0px)   | Find a journey · All Destina ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.emag-home-hero> (w=1440px)                    | │
│ | H1: The Explora Journal                                            | │
│ | Substrate: #f4f2ef | Ink: #222222 | Accent: #9c441d                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.emag-home-grid>) max-w: 1364px             | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Introducing EXPLORA III      |  | Out of Office: Jannik Sinner | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<article.article-card>) — Introducing Captain F     | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.quotesubject) | https://explorajourneys.com/int/en/  │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 30px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.experiencefragme) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.emag-home-hero>) — 390px Vertical Lead        | │
│ | H1: The Explora Journal                                            | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.emag-home-gri) — 1-Col Stack              | │
│ | [ Item 1: Introducing EXPLORA III                                ] | │
│ | [ Item 2: Out of Office: Jannik Sinner’s Way                     ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<article.article-card>) — 1-Col (Introducing Captai) | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.quotesubject) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.experiencefragment> — `explorajourneys-com_int-en-explora-journal`)**:
   - Landmark `<header class="experiencefragment header-sticky">` (`1440x0px`) hosting `The Explora Journal, A Magazine by E` navigation (`Find a journey · All Destinations · Alaska · Asia · Grand Journeys`), DOM attributes (`data-destex-discover-bound`, `data-description="Scene7DefaultCSS"`, `data-component="ScrollBar"`, `data-namespace="s7classic"`), and stylesheet rule `.cmp-accordion__button { display:block;width:100%;text-align:left }`.
2. **Hero Stage & Focal Lead (<section.emag-home-hero> — `The Explora Journal`)**:
   - Landmark `<section class="emag-home-hero emag-home-hero--imageBackground">` presenting display lead `The Explora Journal` and copy excerpt *"A Magazine by Explora Journeys"* over `#f4f2ef` canvas and `#222222` ink.
3. **Primary Showcase & Content Grid (<section.emag-home-grid> — `Introducing EXPLORA III`)**:
   - Landmark `<section class="emag-home-grid">` rendering section `Introducing EXPLORA III` with copy *"Wrong email address Primary Email Address* Add Another Email Addr"*, asset references (`0.8.77`, `187102487`, `adalyser.js`, `insight.min.js`), and grid rule `.cmp-accordion__panel--hidden { display:none }`.
4. **Interactive Detail & Feature Matrix (<article.article-card> — `Out of Office: Jannik Sinner’s Way`)**:
   - Landmark `<article class="article-card card--small">` framing `Out of Office: Jannik Sinner’s Way` and `Introducing Captain Francesco Russo: A Life Shape...` (*"Wrong email address"*) with `#ffffff` surface cards, `#9c441d` accents, and `.cmp-accordion__panel--expanded { display:block }`.
5. **Colophon & Global Directory Footer (<footer.quotesubject> — `https://explorajourneys.com/int/en/explora-journal`)**:
   - Landmark `<footer class="quotesubject">` anchoring `The Explora Journal, A Magazine ` footer links (`Find a journey · All Destinations · Alaska · Asia · Grand Journeys`), copy *"Primary Email Address*"*, and `#cccccc` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: explorajourneys-com_int-en-explora-journal (The Explora Journal, A Magazine by Explora Journeys)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `explorajourneys-com_int-en-explora-journal` (**The Explora Journal, A Magazine by Explora Journeys** — `https://explorajourneys.com/int/en/explora-journal`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#f4f2ef` canvas, `#222222` ink, `#9c441d` accent).
- **Identity & Domain Context**: Step aboard The Explora Journal for stories of ships and destinations, from wellness and dining to ports and cultures, told through the O...
- **Primary Substrate**: `#f4f2ef` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#222222`, **Accent / Highlight**: `#9c441d`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f4f2ef` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#222222` primary typography and `#9c441d` accents.
  - **Grounded Typographic Hierarchy**: Pairs `WT Monarch Nova` for display copy (`The Explora Journal`) with `Shapiro` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1364px` container bounds (`gap: 30px`, padding `.5rem`) with `cubic-bezier(.215,.61,.355,1)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `explorajourneys-com_int-en-explora-journal` in your global stylesheet:

:root {
  /* The Explora Journal, A Magazine by Explora Journeys (explorajourneys-com_int-en-explora-journal) — Live-Grounded CSS Variables */
  --animate-duration: 1s; /* Motion / Easing Token (explorajourneys-com_int-en-explora-journal) */
  --animate-delay: 1s; /* Motion / Easing Token (explorajourneys-com_int-en-explora-journal) */
  --animate-repeat: 1; /* Motion / Easing Token (explorajourneys-com_int-en-explora-journal) */
  --alert-height: 0px; /* Layout / Spatial Grid Token (explorajourneys-com_int-en-explora-journal) */
  --menu-height-desktop: 95px; /* Layout / Spatial Grid Token (explorajourneys-com_int-en-explora-journal) */
  --menu-height-mobile: 80px; /* Layout / Spatial Grid Token (explorajourneys-com_int-en-explora-journal) */
  --partner-header-height: 0px; /* Layout / Spatial Grid Token (explorajourneys-com_int-en-explora-journal) */
  --hero-component-height: calc(100svh - 80px); /* Layout / Spatial Grid Token (explorajourneys-com_int-en-explora-journal) */
  --hero-component-height-full: var(--hero-component-height); /* Layout / Spatial Grid Token (explorajourneys-com_int-en-explora-journal) */
  --contact-banner-height: 0px; /* Layout / Spatial Grid Token (explorajourneys-com_int-en-explora-journal) */
  --swiper-theme-color: #007aff; /* Brand / Palette Token (explorajourneys-com_int-en-explora-journal) */
  --explorajourneys--bg: #f4f2ef; /* Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) (explorajourneys-com_int-en-explora-journal) */
  --explorajourneys--ink: #222222; /* Primary Typography Ink (computed-derived) (explorajourneys-com_int-en-explora-journal) */
  --explorajourneys--surface: #ffffff; /* Surface Substrate (computed-derived) (explorajourneys-com_int-en-explora-journal) */
  --explorajourneys--accent: #9c441d; /* Interactive Accent (computed-derived) (explorajourneys-com_int-en-explora-journal) */
  --explorajourneys--muted: #866d4b; /* Secondary Ink (computed-derived) (explorajourneys-com_int-en-explora-journal) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f4f2ef` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#222222` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#ffffff` — grounded in `.cmp-search__results { background: #ffffff }`
- **Interactive Accent / Highlight**: `#9c441d` — grounded in `.cta-light-scroll:hover { color: #9c441d }`
- **Secondary / Muted Copy**: `#866d4b` — grounded in live computed `a` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#cccccc` — grounded in `.cmp-search__loading-indicator { border: #cccccc }`
- **Variable Token (`--swiper-theme-color`)**: `#007aff` — grounded in `var(--swiper-theme-color)` in stylesheet

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1364px` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `.5rem` lateral canvas padding with `30px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1364px`, `gap: 30px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `.5rem` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:reduce),print`, `@media only screen and (max-width:768px)`, `@media only screen and (max-width:360px)`, `@media only screen and (min-width:768px) and (max-width:1024px)`
- **Corner Radii**: `5px`, `50%`, `7px`, `3px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `WT Monarch Nova`
- **Body Font Stack**: `Shapiro`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 40.05px`, `line-height: 56.07px`, `font-weight: 400`); rule `.title` (`font-size: 24px`, `font-weight: 400`)
- **H2 Section Rule**: live computed `h2` (`font-size: 19.95px`, `line-height: 27.93px`, `font-weight: 400`); rule `h2` (`font-size: 1.5em`, `font-weight: bold`)
- **Body Copy Rule**: live computed `body` (`font-size: 15px`, `line-height: 26px`, `font-weight: 400`); rule `p` (`font-size: 13px`, `line-height: 20px`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 15px`, `line-height: 26px`, `font-weight: 400`); rule `.label` (`font-size: 9pt`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `explorajourneys-com_int-en-explora-journal` (`The Explora Journal, A Magazine by Explora Journeys`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.experiencefragment> — `explorajourneys-com_int-en-explora-journal`)**:
   - DOM & Selectors: Landmark `<header class="experiencefragment header-sticky">` (`1440x0px`) hosting `The Explora Journal, A Magazine by E` navigation (`Find a journey · All Destinations · Alaska · Asia · Grand Journeys`), DOM attributes (`data-destex-discover-bound`, `data-description="Scene7DefaultCSS"`, `data-component="ScrollBar"`, `data-namespace="s7classic"`), and stylesheet rule `.cmp-accordion__button { display:block;width:100%;text-align:left }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.experiencefragment> — `explorajourneys-com_int-en-explora-journal`)` (`explorajourneys-com_int-en-explora-journal`) adapts across `@media (prefers-reduced-motion:reduce),print`, `@media only screen and (max-width:768px)`, `@media only screen and (max-width:360px)`, `@media only screen and (min-width:768px) and (max-width:1024px)` with `cubic-bezier(.215,.61,.355,1)`, `cubic-bezier(.755,.05,.855,.06)`, `cubic-bezier(.55,.055,.675,.19)` transitions and links `Find a journey · All Destinations · Alaska · Asia · Grand Journeys`.
2. **Hero Stage & Focal Lead (<section.emag-home-hero> — `The Explora Journal`)**:
   - DOM & Selectors: Landmark `<section class="emag-home-hero emag-home-hero--imageBackground">` presenting display lead `The Explora Journal` and copy excerpt *"A Magazine by Explora Journeys"* over `#f4f2ef` canvas and `#222222` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#f4f2ef` background with `#222222` headline `The Explora Journal`.
3. **Primary Showcase & Content Grid (<section.emag-home-grid> — `Introducing EXPLORA III`)**:
   - DOM & Selectors: Landmark `<section class="emag-home-grid">` rendering section `Introducing EXPLORA III` with copy *"Wrong email address Primary Email Address* Add Another Email Addr"*, asset references (`0.8.77`, `187102487`, `adalyser.js`, `insight.min.js`), and grid rule `.cmp-accordion__panel--hidden { display:none }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.emag-home-grid> — `Introducing EXPLORA III`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1364px`, `gap: 30px`) on desktop and Single-column vertical stack at `390px` viewport width with `.5rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.article-card> — `Out of Office: Jannik Sinner’s Way`)**:
   - DOM & Selectors: Landmark `<article class="article-card card--small">` framing `Out of Office: Jannik Sinner’s Way` and `Introducing Captain Francesco Russo: A Life Shape...` (*"Wrong email address"*) with `#ffffff` surface cards, `#9c441d` accents, and `.cmp-accordion__panel--expanded { display:block }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.article-card> — `Out of Office: Jannik Sinner’s Way`)` uses `5px`, `50%`, `7px`, `3px` radii, `#9c441d` highlights, and assets (0.8.77, 187102487, adalyser.js).
5. **Colophon & Global Directory Footer (<footer.quotesubject> — `https://explorajourneys.com/int/en/explora-journal`)**:
   - DOM & Selectors: Landmark `<footer class="quotesubject">` anchoring `The Explora Journal, A Magazine ` footer links (`Find a journey · All Destinations · Alaska · Asia · Grand Journeys`), copy *"Primary Email Address*"*, and `#cccccc` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.quotesubject> — `https://explorajourneys.com/int/en/explora-journal`)` aligns to `1364px` (non-`@media` desktop container stylesheet rule) with `.5rem` lateral canvas padding with `30px` grid gap and attributes (data-destex-discover-bound, data-description="Scene7DefaultCSS", data-component="ScrollBar").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"A Magazine by Explora Journeys"*
- Copy Excerpt 2: *"Wrong email address Primary Email Address* Add Another Email Address Wrong email a..."*
- Copy Excerpt 3: *"Wrong email address"*
- Copy Excerpt 4: *"Primary Email Address*"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.215,.61,.355,1)`, `cubic-bezier(.755,.05,.855,.06)`, `cubic-bezier(.55,.055,.675,.19)`
- **Extracted Stylesheet Rules (`explorajourneys-com_int-en-explora-journal`)**:
- `.cmp-accordion__button { display:block;width:100%;text-align:left }`
- `.cmp-accordion__panel--hidden { display:none }`
- `.cmp-accordion__panel--expanded { display:block }`
- `.cmp-tabs__tablist { display:flex;flex-wrap:wrap;padding-left:0;list-style:none }`
- `.cmp-tabs__tab { box-sizing:border-box;border-bottom:1px solid transparent;padding:.5rem... }`
- **Per-Selector Transition Rules**:
- **Selector `print`**: `transition: 1ms!important` extracted from `explorajourneys-com_int-en-explora-journal` stylesheet.
- **Selector `80%`**: `transition: cubic-bezier(.215,.61,.355,1)` extracted from `explorajourneys-com_int-en-explora-journal` stylesheet.
- **Selector `80%`**: `transition: cubic-bezier(.215,.61,.355,1)` extracted from `explorajourneys-com_int-en-explora-journal` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.215,.61,.355,1)`)**: Governs interactive state transitions across `<header.experiencefragment>` and `<section.emag-home-grid>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `explorajourneys-com_int-en-explora-journal`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
