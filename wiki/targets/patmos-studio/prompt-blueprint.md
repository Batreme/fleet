---
title: "UI Prompt Blueprint: patmos-studio"
date: 2026-11-15
target: "[[overview|patmos-studio]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#000` ink, `#8f8f8f` accent)"
---

# UI Design System & Master Generation Blueprint: patmos-studio

> **Patmos · Wahr, Gut, Schön** (https://patmos.studio/) — A Gestalting™ practice at the intersection of business and art. Across strategy, organization, branding, design, marketing, product, arch...

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/patmos-studio/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Patmos · Wahr, Gut, Schön** (`https://patmos.studio/`). A Gestalting™ practice at the intersection of business and art. Across strategy, organization, branding, design, marketing, product, arch...
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#000` ink, `#8f8f8f` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`var(--color-bg)` in `:root`) paired with `#000` primary typography and `#8f8f8f` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Patmos Serif` for display copy (`( Patmos ) Wahr, Gut, Schön`) with `Noto Sans JP` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `999px` container bounds (`gap: var(--spacing-20-24)`, padding `var(--spacing-30-40)`) with `cubic-bezier(.55,.085,.68,.53)` easing and Lenis Smooth Scroll (`data-lenis`).

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/patmos-studio/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `999px` extracted from `patmos-studio` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--spacing-30-40)` lateral canvas padding with `var(--spacing-20-24)` grid gap.
- **Border Radius Scale**: `0px` (sharp unrounded corners).

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 999px`, `gap: var(--spacing-20-24)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--spacing-30-40)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:25em)`, `@media (min-width:37.5em)`, `@media (min-width:50em)`, `@media (min-width:62.5em)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--color-bg)` in `:root` |
| **Primary Typography Ink** | `#f5f5f5` | `var(--color-bg-muted)` in `:root` |
| **Elevated Surface / Card Substrate** | `#000` | `var(--color-fg)` in `:root` |
| **Interactive Accent / Highlight** | `#8f8f8f` | `var(--color-fg-muted)` in `:root` |
| **Secondary / Muted Copy** | `#ddd` | `var(--color-fg-muted-strong)` in `:root` |
| **Structural Hairline Border** | `#787878` | `var(--color-neutral)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--cols` | `var(--_cols)` | Layout / Spatial Grid Token |
| `--header-height` | `18rem` | Layout / Spatial Grid Token |
| `--mt` | `var(--_mt)` | Design System Custom Token |
| `--span` | `var(--_span)` | Design System Custom Token |
| `--start` | `var(--_start)` | Design System Custom Token |
| `--spacing` | `.0625rem` | Layout / Spatial Grid Token |
| `--spacing-base` | `.9375rem` | Layout / Spatial Grid Token |
| `--spacing-10-11` | `clamp(.625rem,.6016rem + .0935vw,.6875rem)` | Layout / Spatial Grid Token |
| `--spacing-12-13` | `clamp(.75rem,.7266rem + .0935vw,.8125rem)` | Layout / Spatial Grid Token |
| `--spacing-14-16` | `clamp(.875rem,.8283rem + .1869vw,1rem)` | Layout / Spatial Grid Token |
| `--spacing-14-17` | `clamp(.875rem,.8049rem + .2831vw,1.0625rem)` | Layout / Spatial Grid Token |
| `--spacing-15-16` | `clamp(.9375rem,.9141rem + .0935vw,1rem)` | Layout / Spatial Grid Token |
| `--spacing-16-17` | `clamp(1rem,.9765rem + .0935vw,1.0625rem)` | Layout / Spatial Grid Token |
| `--spacing-16-18` | `clamp(1rem,.9533rem + .1869vw,1.125rem)` | Layout / Spatial Grid Token |
| `--spacing-16-19` | `clamp(1rem,.9299rem + .2804vw,1.1875rem)` | Layout / Spatial Grid Token |
| `--spacing-16-20` | `clamp(1rem,.374vw + .907rem,1.25rem)` | Layout / Spatial Grid Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Patmos Serif`.
- **Primary Body Stack**: `Noto Sans JP`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`font-weight: 300`).
- **Section Heading (`H2`)**: rule `h2` (`line-height: 1.6!important`).
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--spacing-14-16)`, `var(--spacing-16-20)`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--spacing-14-16)`, `var(--spacing-16-20)`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.55,.085,.68,.53)`, `cubic-bezier(.165,.84,.44,1)`, `cubic-bezier(.455,.03,.515,.955)`.

### Per-Element Transition & Choreography Rules
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `patmos-studio` stylesheet.
- **Selector `.transition-\[gap\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `patmos-studio` stylesheet.
- **Selector `opacity\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `patmos-studio` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.55,.085,.68,.53)`)**: Governs interactive state transitions across `<nav.visible>` and `<main.row-span-full>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`) with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Patmos · Wahr, Gut, Schön                  │
│ ====================================================================== │
│ [ <nav.visible>            | Home · Prologue · Episode · Scene · Ep ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <main.row-span-full>                                 |   │
│ | H1: ( Patmos ) Wahr, Gut, Schön                                  |   │
│ | Substrate: #fff       | Ink: #000       | Accent: #8f8f8f        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<main.row-span-full>      ) max-w: 999px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Loading complete. Choose whe |  | Praksis of Gestalting        | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<nav.visible>] -> [<main.row-span-ful] -> [<main.row-span-ful] |    │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.swup-enabled> ) | https://patmos.studio/             │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.visible> — `patmos-studio`)**:
   - Landmark `<nav class="visible fixed">` hosting `Patmos · Wahr, Gut, Schön` navigation (`Home · Prologue · Episode · Scene · Epilogue`), DOM attributes (`data-typeface="serif"`, `data-path="/contact/"`, `data-path="/"`, `data-path="/prologue/"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<main.row-span-full> — `( Patmos ) Wahr, Gut, Schön`)**:
   - Landmark `<main class="row-span-full">` presenting display lead `( Patmos ) Wahr, Gut, Schön` and copy excerpt *"Loading complete. Choose whether to play sound."* over `#fff` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<main.row-span-full> — `Loading complete. Choose whether t`)**:
   - Landmark `<main class="row-span-full">` rendering section `Loading complete. Choose whether to play sound.` with copy *"Praksis of Gestalting"*, asset references (`dlr2ezd.js`, `favicon.svg`, `apple-touch-icon.png`, `fonts.googleapis.com`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<main.row-span-full> — `Praksis of Gestalting`)**:
   - Landmark `<main class="row-span-full">` framing `Praksis of Gestalting` and `( Das Wahre, Gute, Schöne )` (*"( Das Wahre, Gute, Schöne )"*) with `#000` surface cards, `#8f8f8f` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.swup-enabled> — `https://patmos.studio/`)**:
   - Landmark `<footer class="swup-enabled">` anchoring `Patmos · Wahr, Gut, Schön` footer links (`Home · Prologue · Episode · Scene · Epilogue`), copy *"Praksis of Gestalting"*, and `#787878` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: patmos-studio (Patmos · Wahr, Gut, Schön)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `patmos-studio` (**Patmos · Wahr, Gut, Schön** — `https://patmos.studio/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#000` ink, `#8f8f8f` accent).
- **Identity & Domain Context**: A Gestalting™ practice at the intersection of business and art. Across strategy, organization, branding, design, marketing, product, arch...
- **Primary Substrate**: `#fff` (`var(--color-bg)` in `:root`), **Primary Ink**: `#000`, **Accent / Highlight**: `#8f8f8f`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`var(--color-bg)` in `:root`) paired with `#000` primary typography and `#8f8f8f` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Patmos Serif` for display copy (`( Patmos ) Wahr, Gut, Schön`) with `Noto Sans JP` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `999px` container bounds (`gap: var(--spacing-20-24)`, padding `var(--spacing-30-40)`) with `cubic-bezier(.55,.085,.68,.53)` easing and Lenis Smooth Scroll (`data-lenis`).

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `patmos-studio` in your global stylesheet:

:root {
  /* Patmos · Wahr, Gut, Schön (patmos-studio) — Ground-Truth Extracted CSS Variables */
  --cols: var(--_cols); /* Layout / Spatial Grid Token (patmos-studio) */
  --header-height: 18rem; /* Layout / Spatial Grid Token (patmos-studio) */
  --mt: var(--_mt); /* Design System Custom Token (patmos-studio) */
  --span: var(--_span); /* Design System Custom Token (patmos-studio) */
  --start: var(--_start); /* Design System Custom Token (patmos-studio) */
  --spacing: .0625rem; /* Layout / Spatial Grid Token (patmos-studio) */
  --spacing-base: .9375rem; /* Layout / Spatial Grid Token (patmos-studio) */
  --spacing-10-11: clamp(.625rem,.6016rem + .0935vw,.6875rem); /* Layout / Spatial Grid Token (patmos-studio) */
  --spacing-12-13: clamp(.75rem,.7266rem + .0935vw,.8125rem); /* Layout / Spatial Grid Token (patmos-studio) */
  --spacing-14-16: clamp(.875rem,.8283rem + .1869vw,1rem); /* Layout / Spatial Grid Token (patmos-studio) */
  --spacing-14-17: clamp(.875rem,.8049rem + .2831vw,1.0625rem); /* Layout / Spatial Grid Token (patmos-studio) */
  --spacing-15-16: clamp(.9375rem,.9141rem + .0935vw,1rem); /* Layout / Spatial Grid Token (patmos-studio) */
  --spacing-16-17: clamp(1rem,.9765rem + .0935vw,1.0625rem); /* Layout / Spatial Grid Token (patmos-studio) */
  --spacing-16-18: clamp(1rem,.9533rem + .1869vw,1.125rem); /* Layout / Spatial Grid Token (patmos-studio) */
  --spacing-16-19: clamp(1rem,.9299rem + .2804vw,1.1875rem); /* Layout / Spatial Grid Token (patmos-studio) */
  --spacing-16-20: clamp(1rem,.374vw + .907rem,1.25rem); /* Layout / Spatial Grid Token (patmos-studio) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fff` — grounded in `var(--color-bg)` in `:root`
- **Primary Typography Ink**: `#f5f5f5` — grounded in `var(--color-bg-muted)` in `:root`
- **Elevated Surface / Card Substrate**: `#000` — grounded in `var(--color-fg)` in `:root`
- **Interactive Accent / Highlight**: `#8f8f8f` — grounded in `var(--color-fg-muted)` in `:root`
- **Secondary / Muted Copy**: `#ddd` — grounded in `var(--color-fg-muted-strong)` in `:root`
- **Structural Hairline Border**: `#787878` — grounded in `var(--color-neutral)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `999px` extracted from `patmos-studio` stylesheet
- **Padding & Gutters**: `var(--spacing-30-40)` lateral canvas padding with `var(--spacing-20-24)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 999px`, `gap: var(--spacing-20-24)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--spacing-30-40)` horizontal padding
- **Media Queries**: `@media (min-width:25em)`, `@media (min-width:37.5em)`, `@media (min-width:50em)`, `@media (min-width:62.5em)`
- **Corner Radii**: `0px` (sharp unrounded corners)

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Patmos Serif`
- **Body Font Stack**: `Noto Sans JP`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: rule `h1` (`font-weight: 300`)
- **H2 Section Rule**: rule `h2` (`line-height: 1.6!important`)
- **Body Copy Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--spacing-14-16)`, `var(--spacing-16-20)`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--spacing-14-16)`, `var(--spacing-16-20)`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `patmos-studio` (`Patmos · Wahr, Gut, Schön`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.visible> — `patmos-studio`)**:
   - DOM & Selectors: Landmark `<nav class="visible fixed">` hosting `Patmos · Wahr, Gut, Schön` navigation (`Home · Prologue · Episode · Scene · Epilogue`), DOM attributes (`data-typeface="serif"`, `data-path="/contact/"`, `data-path="/"`, `data-path="/prologue/"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.visible> — `patmos-studio`)` (`patmos-studio`) adapts across `@media (min-width:25em)`, `@media (min-width:37.5em)`, `@media (min-width:50em)`, `@media (min-width:62.5em)` with `cubic-bezier(.55,.085,.68,.53)`, `cubic-bezier(.165,.84,.44,1)`, `cubic-bezier(.455,.03,.515,.955)` transitions and links `Home · Prologue · Episode · Scene · Epilogue`.
2. **Hero Stage & Focal Lead (<main.row-span-full> — `( Patmos ) Wahr, Gut, Schön`)**:
   - DOM & Selectors: Landmark `<main class="row-span-full">` presenting display lead `( Patmos ) Wahr, Gut, Schön` and copy excerpt *"Loading complete. Choose whether to play sound."* over `#fff` canvas and `#000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#fff` background with `#000` headline `( Patmos ) Wahr, Gut, Schön`.
3. **Primary Showcase & Content Grid (<main.row-span-full> — `Loading complete. Choose whether t`)**:
   - DOM & Selectors: Landmark `<main class="row-span-full">` rendering section `Loading complete. Choose whether to play sound.` with copy *"Praksis of Gestalting"*, asset references (`dlr2ezd.js`, `favicon.svg`, `apple-touch-icon.png`, `fonts.googleapis.com`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<main.row-span-full> — `Loading complete. Choose whether t`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 999px`, `gap: var(--spacing-20-24)`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--spacing-30-40)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<main.row-span-full> — `Praksis of Gestalting`)**:
   - DOM & Selectors: Landmark `<main class="row-span-full">` framing `Praksis of Gestalting` and `( Das Wahre, Gute, Schöne )` (*"( Das Wahre, Gute, Schöne )"*) with `#000` surface cards, `#8f8f8f` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<main.row-span-full> — `Praksis of Gestalting`)` uses `0px` (sharp unrounded corners) radii, `#8f8f8f` highlights, and assets (dlr2ezd.js, favicon.svg, apple-touch-icon.png).
5. **Colophon & Global Directory Footer (<footer.swup-enabled> — `https://patmos.studio/`)**:
   - DOM & Selectors: Landmark `<footer class="swup-enabled">` anchoring `Patmos · Wahr, Gut, Schön` footer links (`Home · Prologue · Episode · Scene · Epilogue`), copy *"Praksis of Gestalting"*, and `#787878` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.swup-enabled> — `https://patmos.studio/`)` aligns to `999px` extracted from `patmos-studio` stylesheet with `var(--spacing-30-40)` lateral canvas padding with `var(--spacing-20-24)` grid gap and attributes (data-typeface="serif", data-path="/contact/", data-path="/").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Loading complete. Choose whether to play sound."*
- Copy Excerpt 2: *"Praksis of Gestalting"*
- Copy Excerpt 3: *"( Das Wahre, Gute, Schöne )"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.55,.085,.68,.53)`, `cubic-bezier(.165,.84,.44,1)`, `cubic-bezier(.455,.03,.515,.955)`
- **Extracted Stylesheet Rules (`patmos-studio`)**:
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- `sup { vertical-align:baseline;font-size:75%;line-height:0;position:relative }`
- **Per-Selector Transition Rules**:
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `patmos-studio` stylesheet.
- **Selector `.transition-\[gap\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `patmos-studio` stylesheet.
- **Selector `opacity\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `patmos-studio` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.55,.085,.68,.53)`)**: Governs interactive state transitions across `<nav.visible>` and `<main.row-span-full>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`) with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `patmos-studio`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
