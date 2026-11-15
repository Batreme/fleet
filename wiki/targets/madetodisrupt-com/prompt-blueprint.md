---
title: "UI Prompt Blueprint: madetodisrupt-com"
date: 2026-11-15
target: "[[overview|madetodisrupt-com]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#6EC1E4` / `#61CE70`)"
---

# UI Design System & Master Generation Blueprint: madetodisrupt-com

> **Disrupt · Creative Brand Experience Agency** (https://madetodisrupt.com) — Disrupt is a creative brand experience agency shaping strategy, identity, events and activations into ideas people can see, feel and expe...

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/madetodisrupt-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Disrupt · Creative Brand Experience Agency** (`https://madetodisrupt.com`). Disrupt is a creative brand experience agency shaping strategy, identity, events and activations into ideas people can see, feel and expe...
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#6EC1E4` / `#61CE70`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#6EC1E4` (`var(--e-global-color-primary)` in `:root`) paired with `#54595F` primary typography and `#61CE70` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Clash Display` for display copy (`BRANDS IN SESSION`) with `Syne` and `Courier 10 Pitch`.
  - **Calibrated Spatial Grid & Motion**: Combines `200px` container bounds (`gap: var(--row-gap)`, padding `1px`) with `cubic-bezier(0,.33,.07,1.03)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/madetodisrupt-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `200px` extracted from `madetodisrupt-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `1px` lateral canvas padding with `var(--row-gap)` grid gap.
- **Border Radius Scale**: `4px`, `100%`, `var(--border-radius)`, `3px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 200px`, `gap: var(--row-gap)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `1px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:768px)`, `@media (max-width:767px)`, `@media (max-width:1024px)`, `@media (min-width:-1)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#6EC1E4` | `var(--e-global-color-primary)` in `:root` |
| **Primary Typography Ink** | `#54595F` | `var(--e-global-color-secondary)` in `:root` |
| **Elevated Surface / Card Substrate** | `#7A7A7A` | `var(--e-global-color-text)` in `:root` |
| **Interactive Accent / Highlight** | `#61CE70` | `var(--e-global-color-accent)` in `:root` |
| **Secondary / Muted Copy** | `#ECEFF3` | `var(--ast-code-block-background)` in `:root` |
| **Structural Hairline Border** | `#F9FAFB` | `var(--ast-comment-inputs-background)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--direction-multiplier` | `1` | Design System Custom Token |
| `--flex-direction` | `initial` | Design System Custom Token |
| `--flex-wrap` | `initial` | Layout / Spatial Grid Token |
| `--justify-content` | `initial` | Design System Custom Token |
| `--align-items` | `initial` | Design System Custom Token |
| `--align-content` | `initial` | Design System Custom Token |
| `--gap` | `initial` | Layout / Spatial Grid Token |
| `--flex-basis` | `initial` | Design System Custom Token |
| `--flex-grow` | `initial` | Design System Custom Token |
| `--flex-shrink` | `initial` | Typography Ink Token |
| `--order` | `initial` | Design System Custom Token |
| `--align-self` | `initial` | Design System Custom Token |
| `--page-title-display` | `block` | Design System Custom Token |
| `--border-radius` | `0` | Elevation / Border Token |
| `--border-top-width` | `0px` | Layout / Spatial Grid Token |
| `--border-right-width` | `0px` | Layout / Spatial Grid Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Clash Display`.
- **Primary Body Stack**: `Syne`.
- **Technical / Metadata Stack**: `Courier 10 Pitch`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--page-title-display: block`, `--display: flex`; rule `,h1` (`font-size: 2em`, `line-height: 1.2`).
- **Section Heading (`H2`)**: rule `,h2` (`font-size: 1.7em`, `line-height: 1.3`).
- **Body Copy**: rule `p` (`font-size: 16px`).
- **Metadata & Navigation Labels**: CSS variables `--ast-blog-meta-weight: 600`, `--srfm-color-input-label: var(--ast-global-color-2)`, `--mv-label-x: calc(var(--mv-base-x) + var(--mv-shift-x))`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0,.33,.07,1.03)`, `cubic-bezier(0.22,1,0.36,1)`, `cubic-bezier(.58,.3,.005,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.dashicons-before:before`**: `transition: color .1s ease-in` extracted from `madetodisrupt-com` stylesheet.
- **Selector `.listimage-wrap li label.nf-check...`**: `transition: all .5s` extracted from `madetodisrupt-com` stylesheet.
- **Selector `entor .elementor-background-video...`**: `transition: opacity 1s` extracted from `madetodisrupt-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,.33,.07,1.03)`)**: Governs interactive state transitions across `<header.entry-header>` and `<section.poc-tilt-section>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Lottie Vector Animation Player, Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Disrupt · Creative Brand Experience Agency │
│ ====================================================================== │
│ [ <header.entry-header>    | Home · Work · Services · Contact       ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <article.post-10>                                    |   │
│ | H1: BRANDS IN SESSION                                            |   │
│ | Substrate: #6EC1E4    | Ink: #54595F    | Accent: #61CE70        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.poc-tilt-section>) max-w: 200px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | WORK                         |  | The Story                    | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<header.entry-head] -> [<article.post-10>] -> [<section.poc-tilt-]  │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.elementor>    ) | https://madetodisrupt.com          │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.entry-header> — `madetodisrupt-com`)**:
   - Landmark `<header class="entry-header ast-no-thumbnail">` hosting `Disrupt · Creative Brand Experience ` navigation (`Home · Work · Services · Contact`), DOM attributes (`data-minify="1"`, `data-rocket-defer`, `data-rocket-prefetch`, `data-rocket-preload`), and stylesheet rule `.dashicons-admin-appearance:before { content:"\f100" }`.
2. **Hero Stage & Focal Lead (<article.post-10> — `BRANDS IN SESSION`)**:
   - Landmark `<article class="post-10 page">` presenting display lead `BRANDS IN SESSION` and copy excerpt *"Brand Therapy, Without the couch. Brand Therapy, Without the couc"* over `#6EC1E4` canvas and `#54595F` ink.
3. **Primary Showcase & Content Grid (<section.poc-tilt-section> — `WORK`)**:
   - Landmark `<section class="poc-tilt-section">` rendering section `WORK` with copy *"Brand Therapy, Without the couch."*, asset references (`recaptcha__en.js`, `script.js`, `www.gstatic.com`, `fonts.googleapis.com`), and grid rule `.dashicons-admin-collapse:before { content:"\f148" }`.
4. **Interactive Detail & Feature Matrix (<section.mxq-stage> — `The Story`)**:
   - Landmark `<section class="mxq-stage">` framing `The Story` and `Craft experiences that move people and shape how...` (*"START A SESSION START A SESSION"*) with `#7A7A7A` surface cards, `#61CE70` accents, and `.dashicons-admin-comments:before { content:"\f101" }`.
5. **Colophon & Global Directory Footer (<footer.elementor> — `https://madetodisrupt.com`)**:
   - Landmark `<footer class="elementor elementor-425">` anchoring `Disrupt · Creative Brand Experie` footer links (`Home · Work · Services · Contact`), copy *"Strategic brand therapy for identities, experiences, and act"*, and `#F9FAFB` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: madetodisrupt-com (Disrupt · Creative Brand Experience Agency)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `madetodisrupt-com` (**Disrupt · Creative Brand Experience Agency** — `https://madetodisrupt.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#6EC1E4` / `#61CE70`).
- **Identity & Domain Context**: Disrupt is a creative brand experience agency shaping strategy, identity, events and activations into ideas people can see, feel and expe...
- **Primary Substrate**: `#6EC1E4` (`var(--e-global-color-primary)` in `:root`), **Primary Ink**: `#54595F`, **Accent / Highlight**: `#61CE70`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#6EC1E4` (`var(--e-global-color-primary)` in `:root`) paired with `#54595F` primary typography and `#61CE70` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Clash Display` for display copy (`BRANDS IN SESSION`) with `Syne` and `Courier 10 Pitch`.
  - **Calibrated Spatial Grid & Motion**: Combines `200px` container bounds (`gap: var(--row-gap)`, padding `1px`) with `cubic-bezier(0,.33,.07,1.03)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `madetodisrupt-com` in your global stylesheet:

:root {
  /* Disrupt · Creative Brand Experience Agency (madetodisrupt-com) — Ground-Truth Extracted CSS Variables */
  --direction-multiplier: 1; /* Design System Custom Token (madetodisrupt-com) */
  --flex-direction: initial; /* Design System Custom Token (madetodisrupt-com) */
  --flex-wrap: initial; /* Layout / Spatial Grid Token (madetodisrupt-com) */
  --justify-content: initial; /* Design System Custom Token (madetodisrupt-com) */
  --align-items: initial; /* Design System Custom Token (madetodisrupt-com) */
  --align-content: initial; /* Design System Custom Token (madetodisrupt-com) */
  --gap: initial; /* Layout / Spatial Grid Token (madetodisrupt-com) */
  --flex-basis: initial; /* Design System Custom Token (madetodisrupt-com) */
  --flex-grow: initial; /* Design System Custom Token (madetodisrupt-com) */
  --flex-shrink: initial; /* Typography Ink Token (madetodisrupt-com) */
  --order: initial; /* Design System Custom Token (madetodisrupt-com) */
  --align-self: initial; /* Design System Custom Token (madetodisrupt-com) */
  --page-title-display: block; /* Design System Custom Token (madetodisrupt-com) */
  --border-radius: 0; /* Elevation / Border Token (madetodisrupt-com) */
  --border-top-width: 0px; /* Layout / Spatial Grid Token (madetodisrupt-com) */
  --border-right-width: 0px; /* Layout / Spatial Grid Token (madetodisrupt-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#6EC1E4` — grounded in `var(--e-global-color-primary)` in `:root`
- **Primary Typography Ink**: `#54595F` — grounded in `var(--e-global-color-secondary)` in `:root`
- **Elevated Surface / Card Substrate**: `#7A7A7A` — grounded in `var(--e-global-color-text)` in `:root`
- **Interactive Accent / Highlight**: `#61CE70` — grounded in `var(--e-global-color-accent)` in `:root`
- **Secondary / Muted Copy**: `#ECEFF3` — grounded in `var(--ast-code-block-background)` in `:root`
- **Structural Hairline Border**: `#F9FAFB` — grounded in `var(--ast-comment-inputs-background)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `200px` extracted from `madetodisrupt-com` stylesheet
- **Padding & Gutters**: `1px` lateral canvas padding with `var(--row-gap)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 200px`, `gap: var(--row-gap)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `1px` horizontal padding
- **Media Queries**: `@media (min-width:768px)`, `@media (max-width:767px)`, `@media (max-width:1024px)`, `@media (min-width:-1)`
- **Corner Radii**: `4px`, `100%`, `var(--border-radius)`, `3px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Clash Display`
- **Body Font Stack**: `Syne`
- **Monospace / Technical Font Stack**: `Courier 10 Pitch`
- **H1 Display Rule**: CSS variables `--page-title-display: block`, `--display: flex`; rule `,h1` (`font-size: 2em`, `line-height: 1.2`)
- **H2 Section Rule**: rule `,h2` (`font-size: 1.7em`, `line-height: 1.3`)
- **Body Copy Rule**: rule `p` (`font-size: 16px`)
- **Metadata & Index Rule**: CSS variables `--ast-blog-meta-weight: 600`, `--srfm-color-input-label: var(--ast-global-color-2)`, `--mv-label-x: calc(var(--mv-base-x) + var(--mv-shift-x))`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `madetodisrupt-com` (`Disrupt · Creative Brand Experience Agency`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.entry-header> — `madetodisrupt-com`)**:
   - DOM & Selectors: Landmark `<header class="entry-header ast-no-thumbnail">` hosting `Disrupt · Creative Brand Experience ` navigation (`Home · Work · Services · Contact`), DOM attributes (`data-minify="1"`, `data-rocket-defer`, `data-rocket-prefetch`, `data-rocket-preload`), and stylesheet rule `.dashicons-admin-appearance:before { content:"\f100" }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.entry-header> — `madetodisrupt-com`)` (`madetodisrupt-com`) adapts across `@media (min-width:768px)`, `@media (max-width:767px)`, `@media (max-width:1024px)`, `@media (min-width:-1)` with `cubic-bezier(0,.33,.07,1.03)`, `cubic-bezier(0.22,1,0.36,1)`, `cubic-bezier(.58,.3,.005,1)` transitions and links `Home · Work · Services · Contact`.
2. **Hero Stage & Focal Lead (<article.post-10> — `BRANDS IN SESSION`)**:
   - DOM & Selectors: Landmark `<article class="post-10 page">` presenting display lead `BRANDS IN SESSION` and copy excerpt *"Brand Therapy, Without the couch. Brand Therapy, Without the couc"* over `#6EC1E4` canvas and `#54595F` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#6EC1E4` background with `#54595F` headline `BRANDS IN SESSION`.
3. **Primary Showcase & Content Grid (<section.poc-tilt-section> — `WORK`)**:
   - DOM & Selectors: Landmark `<section class="poc-tilt-section">` rendering section `WORK` with copy *"Brand Therapy, Without the couch."*, asset references (`recaptcha__en.js`, `script.js`, `www.gstatic.com`, `fonts.googleapis.com`), and grid rule `.dashicons-admin-collapse:before { content:"\f148" }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.poc-tilt-section> — `WORK`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 200px`, `gap: var(--row-gap)`) on desktop and Single-column vertical stack at `390px` viewport width with `1px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.mxq-stage> — `The Story`)**:
   - DOM & Selectors: Landmark `<section class="mxq-stage">` framing `The Story` and `Craft experiences that move people and shape how...` (*"START A SESSION START A SESSION"*) with `#7A7A7A` surface cards, `#61CE70` accents, and `.dashicons-admin-comments:before { content:"\f101" }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.mxq-stage> — `The Story`)` uses `4px`, `100%`, `var(--border-radius)`, `3px` radii, `#61CE70` highlights, and assets (recaptcha__en.js, script.js, www.gstatic.com).
5. **Colophon & Global Directory Footer (<footer.elementor> — `https://madetodisrupt.com`)**:
   - DOM & Selectors: Landmark `<footer class="elementor elementor-425">` anchoring `Disrupt · Creative Brand Experie` footer links (`Home · Work · Services · Contact`), copy *"Strategic brand therapy for identities, experiences, and act"*, and `#F9FAFB` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.elementor> — `https://madetodisrupt.com`)` aligns to `200px` extracted from `madetodisrupt-com` stylesheet with `1px` lateral canvas padding with `var(--row-gap)` grid gap and attributes (data-minify="1", data-rocket-defer, data-rocket-prefetch).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Brand Therapy, Without the couch. Brand Therapy, Without the couch."*
- Copy Excerpt 2: *"Brand Therapy, Without the couch."*
- Copy Excerpt 3: *"START A SESSION START A SESSION"*
- Copy Excerpt 4: *"Strategic brand therapy for identities, experiences, and activations that stay wit..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0,.33,.07,1.03)`, `cubic-bezier(0.22,1,0.36,1)`, `cubic-bezier(.58,.3,.005,1)`
- **Extracted Stylesheet Rules (`madetodisrupt-com`)**:
- `.dashicons-admin-appearance:before { content:"\f100" }`
- `.dashicons-admin-collapse:before { content:"\f148" }`
- `.dashicons-admin-comments:before { content:"\f101" }`
- `.dashicons-admin-customizer:before { content:"\f540" }`
- `.dashicons-admin-generic:before { content:"\f111" }`
- **Per-Selector Transition Rules**:
- **Selector `.dashicons-before:before`**: `transition: color .1s ease-in` extracted from `madetodisrupt-com` stylesheet.
- **Selector `.listimage-wrap li label.nf-check...`**: `transition: all .5s` extracted from `madetodisrupt-com` stylesheet.
- **Selector `entor .elementor-background-video...`**: `transition: opacity 1s` extracted from `madetodisrupt-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,.33,.07,1.03)`)**: Governs interactive state transitions across `<header.entry-header>` and `<section.poc-tilt-section>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Lottie Vector Animation Player, Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `madetodisrupt-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
