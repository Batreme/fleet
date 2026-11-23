---
title: "UI Prompt Blueprint: milledollars-fr"
date: 2026-11-23
captured_at: 2026-11-23
target: "milledollars-fr"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier2_webgl
http_status: 200
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#e0dee1` / `#c2a1c7`)"
---

# UI Design System & Master Generation Blueprint: milledollars-fr

> **MilleDollars** (https://milledollars.fr/) — Creative bureau focused on high-end video production. Working worldwide.

![Desktop Viewport Capture (1440x900)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **MilleDollars** (`https://milledollars.fr/`). Creative bureau focused on high-end video production. Working worldwide.
- **Capture Provenance**: Live browser capture (`tier2_webgl`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#e0dee1` / `#c2a1c7`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#e0dee1` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#c2a1c7` accents.
  - **Grounded Typographic Hierarchy**: Pairs `ABCDiatype` for display copy (`MilleDollars`) with `ABCDiatype` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1200px` container bounds (`gap: 4px`, padding `var(--header-spacing-y)`) with `cubic-bezier(.55,.085,.68,.53)` easing and Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x844)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×900px` (`assets/desktop.png`, single-viewport 100vh live capture (900px)), Mobile `390×844px` (`assets/mobile.png`, single-viewport 100vh live capture (844px)).
- **Master Container Bounds**: `1200px` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `var(--header-spacing-y)` lateral canvas padding with `4px` grid gap.
- **Border Radius Scale**: `50%`, `.5rem`, `.4rem`, `1rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1200px`, `gap: 4px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--header-spacing-y)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:768px)`, `@media (min-width:768px)`, `@media (pointer:fine)and (min-width:768px)`, `@media (max-width:768px)and (max-width:768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#e0dee1` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `header` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `var(--cc-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#c2a1c7` | `#cc-main .cm__btn:before { background: #c2a1c7 }` |
| **Secondary / Muted Copy** | `#5e6266` | `var(--cc-secondary-color)` in `:root` |
| **Structural Hairline Border** | `#ffffff` | `var(--accent-border-color)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ease-in-quad` | `cubic-bezier(.55,.085,.68,.53)` | Motion / Easing Token |
| `--ease-in-cubic` | `cubic-bezier(.55,.055,.675,.19)` | Motion / Easing Token |
| `--ease-in-quart` | `cubic-bezier(.895,.03,.685,.22)` | Motion / Easing Token |
| `--ease-in-quint` | `cubic-bezier(.755,.05,.855,.06)` | Motion / Easing Token |
| `--ease-in-expo` | `cubic-bezier(.95,.05,.795,.035)` | Motion / Easing Token |
| `--ease-in-circ` | `cubic-bezier(.6,.04,.98,.335)` | Motion / Easing Token |
| `--ease-out-quad` | `cubic-bezier(.25,.46,.45,.94)` | Motion / Easing Token |
| `--ease-out-cubic` | `cubic-bezier(.215,.61,.355,1)` | Motion / Easing Token |
| `--ease-out-quart` | `cubic-bezier(.165,.84,.44,1)` | Motion / Easing Token |
| `--ease-out-quint` | `cubic-bezier(.23,1,.32,1)` | Motion / Easing Token |
| `--ease-out-expo` | `cubic-bezier(.19,1,.22,1)` | Motion / Easing Token |
| `--ease-out-circ` | `cubic-bezier(.075,.82,.165,1)` | Motion / Easing Token |
| `--ease-in-out-quad` | `cubic-bezier(.455,.03,.515,.955)` | Motion / Easing Token |
| `--ease-in-out-cubic` | `cubic-bezier(.645,.045,.355,1)` | Motion / Easing Token |
| `--ease-in-out-quart` | `cubic-bezier(.77,0,.175,1)` | Motion / Easing Token |
| `--ease-in-out-quint` | `cubic-bezier(.86,0,.07,1)` | Motion / Easing Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `ABCDiatype`.
- **Primary Body Stack**: `ABCDiatype`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 18px`, `line-height: 18px`, `font-weight: 400`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.55,.085,.68,.53)`, `cubic-bezier(.19,1,.22,1)`, `cubic-bezier(.55,.055,.675,.19)`.

### Per-Element Transition & Choreography Rules
- **Selector `.o-header-top-item`**: `transition: color .2s linear` extracted from `milledollars-fr` stylesheet.
- **Selector `.a-lines_inner`**: `transition: transform .26s cubic-bezier(.55,.085,.68,.53) var(--delay-out,0s)` extracted from `milledollars-fr` stylesheet.
- **Selector `.a-lines.-instant .a-lines_inner`**: `transition: 0s` extracted from `milledollars-fr` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.55,.085,.68,.53)`)**: Governs interactive state transitions across `<header.c-header>` and `<section.sr-only:nth(2)>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — MilleDollars                               │
│ ====================================================================== │
│ [ <header.c-header> (1440x64px)       | Home · Works · Info · Contac ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.sr-only> (w=1440px)                           | │
│ | H1: MilleDollars                                                   | │
│ | Substrate: #e0dee1 | Ink: #000000 | Accent: #c2a1c7                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.sr-only:nth(2)>) max-w: 1200px             | │
│ | +------------------------------+  +------------------------------+ | │
│ | | The Dazzling Division        |  | Ultimate Shield              | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.sr-only:nth(3)>) — Eternal Snow            | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.c-preloader-) | https://milledollars.fr/             │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 4px)        │
│ ====================================================================== │
│ [ HEADER BAR (<header.c-header>       ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.sr-only>) — 390px Vertical Lead               | │
│ | H1: MilleDollars                                                   | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.sr-only:nth(2) — 1-Col Stack              | │
│ | [ Item 1: The Dazzling Division                                  ] | │
│ | [ Item 2: Ultimate Shield                                        ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.sr-only:nth(3)>) — 1-Col (Eternal Snow)     | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.c-preloader-) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.c-header> — `milledollars-fr`)**:
   - Landmark `<header class="c-header">` (`1440x64px`) hosting `MilleDollars` navigation (`Home · Works · Info · Contact`), DOM attributes (`data-hid="prismic-preview"`, `data-hid="jsonld-seo"`, `data-symbol="logo"`, `data-symbol="logo-mille"`), and stylesheet rule `.o-header-top-item { display:none }`.
2. **Hero Stage & Focal Lead (<section.sr-only> — `MilleDollars`)**:
   - Landmark `<section class="sr-only">` presenting display lead `MilleDollars` and copy excerpt *"Creative bureau focused on high-end video production. Working wor"* over `#e0dee1` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.sr-only:nth(2)> — `The Dazzling Division`)**:
   - Landmark `<section class="sr-only">` rendering section `The Dazzling Division` with copy *"The Dazzling Division — Richard Mille (2026)"*, asset references (`fonts.googleapis.com`, `fonts.gstatic.com`, `prismic.min.js`, `css2`), and grid rule `.a-mask-lines_inner-mask { margin-bottom:-.2lh }`.
4. **Interactive Detail & Feature Matrix (<section.sr-only:nth(3)> — `Ultimate Shield`)**:
   - Landmark `<section class="sr-only">` framing `Ultimate Shield` and `Eternal Snow` (*"Ultimate Shield — EviDenS de Beauté (2026)"*) with `#ffffff` surface cards, `#c2a1c7` accents, and `.a-lines { --appear-y:var(--y,120%) }`.
5. **Colophon & Global Directory Footer (<footer.c-preloader-logo-loop> — `https://milledollars.fr/`)**:
   - Landmark `<footer class="c-preloader-logo-loop">` anchoring `MilleDollars` footer links (`Home · Works · Info · Contact`), copy *"Eternal Snow — Richard Mille (2026)"*, and `#ffffff` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: milledollars-fr (MilleDollars)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `milledollars-fr` (**MilleDollars** — `https://milledollars.fr/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#e0dee1` / `#c2a1c7`).
- **Identity & Domain Context**: Creative bureau focused on high-end video production. Working worldwide.
- **Primary Substrate**: `#e0dee1` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#000000`, **Accent / Highlight**: `#c2a1c7`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#e0dee1` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#c2a1c7` accents.
  - **Grounded Typographic Hierarchy**: Pairs `ABCDiatype` for display copy (`MilleDollars`) with `ABCDiatype` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1200px` container bounds (`gap: 4px`, padding `var(--header-spacing-y)`) with `cubic-bezier(.55,.085,.68,.53)` easing and Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `milledollars-fr` in your global stylesheet:

:root {
  /* MilleDollars (milledollars-fr) — Live-Grounded CSS Variables */
  --ease-in-quad: cubic-bezier(.55,.085,.68,.53); /* Motion / Easing Token (milledollars-fr) */
  --ease-in-cubic: cubic-bezier(.55,.055,.675,.19); /* Motion / Easing Token (milledollars-fr) */
  --ease-in-quart: cubic-bezier(.895,.03,.685,.22); /* Motion / Easing Token (milledollars-fr) */
  --ease-in-quint: cubic-bezier(.755,.05,.855,.06); /* Motion / Easing Token (milledollars-fr) */
  --ease-in-expo: cubic-bezier(.95,.05,.795,.035); /* Motion / Easing Token (milledollars-fr) */
  --ease-in-circ: cubic-bezier(.6,.04,.98,.335); /* Motion / Easing Token (milledollars-fr) */
  --ease-out-quad: cubic-bezier(.25,.46,.45,.94); /* Motion / Easing Token (milledollars-fr) */
  --ease-out-cubic: cubic-bezier(.215,.61,.355,1); /* Motion / Easing Token (milledollars-fr) */
  --ease-out-quart: cubic-bezier(.165,.84,.44,1); /* Motion / Easing Token (milledollars-fr) */
  --ease-out-quint: cubic-bezier(.23,1,.32,1); /* Motion / Easing Token (milledollars-fr) */
  --ease-out-expo: cubic-bezier(.19,1,.22,1); /* Motion / Easing Token (milledollars-fr) */
  --ease-out-circ: cubic-bezier(.075,.82,.165,1); /* Motion / Easing Token (milledollars-fr) */
  --ease-in-out-quad: cubic-bezier(.455,.03,.515,.955); /* Motion / Easing Token (milledollars-fr) */
  --ease-in-out-cubic: cubic-bezier(.645,.045,.355,1); /* Motion / Easing Token (milledollars-fr) */
  --ease-in-out-quart: cubic-bezier(.77,0,.175,1); /* Motion / Easing Token (milledollars-fr) */
  --ease-in-out-quint: cubic-bezier(.86,0,.07,1); /* Motion / Easing Token (milledollars-fr) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#e0dee1` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#000000` — grounded in live computed `header` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#ffffff` — grounded in `var(--cc-bg)` in `:root`
- **Interactive Accent / Highlight**: `#c2a1c7` — grounded in `#cc-main .cm__btn:before { background: #c2a1c7 }`
- **Secondary / Muted Copy**: `#5e6266` — grounded in `var(--cc-secondary-color)` in `:root`
- **Structural Hairline Border**: `#ffffff` — grounded in `var(--accent-border-color)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×900px` (single-viewport 100vh live capture (900px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×844px` (single-viewport 100vh live capture (844px), `390px` standard mobile width).
- **Container Max-Width**: `1200px` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `var(--header-spacing-y)` lateral canvas padding with `4px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1200px`, `gap: 4px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--header-spacing-y)` horizontal padding
- **Media Queries**: `@media (max-width:768px)`, `@media (min-width:768px)`, `@media (pointer:fine)and (min-width:768px)`, `@media (max-width:768px)and (max-width:768px)`
- **Corner Radii**: `50%`, `.5rem`, `.4rem`, `1rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `ABCDiatype`
- **Body Font Stack**: `ABCDiatype`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: live computed `h1` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)
- **H2 Section Rule**: live computed `h2` (`font-size: 18px`, `line-height: 18px`, `font-weight: 400`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `milledollars-fr` (`MilleDollars`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.c-header> — `milledollars-fr`)**:
   - DOM & Selectors: Landmark `<header class="c-header">` (`1440x64px`) hosting `MilleDollars` navigation (`Home · Works · Info · Contact`), DOM attributes (`data-hid="prismic-preview"`, `data-hid="jsonld-seo"`, `data-symbol="logo"`, `data-symbol="logo-mille"`), and stylesheet rule `.o-header-top-item { display:none }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.c-header> — `milledollars-fr`)` (`milledollars-fr`) adapts across `@media (max-width:768px)`, `@media (min-width:768px)`, `@media (pointer:fine)and (min-width:768px)`, `@media (max-width:768px)and (max-width:768px)` with `cubic-bezier(.55,.085,.68,.53)`, `cubic-bezier(.19,1,.22,1)`, `cubic-bezier(.55,.055,.675,.19)` transitions and links `Home · Works · Info · Contact`.
2. **Hero Stage & Focal Lead (<section.sr-only> — `MilleDollars`)**:
   - DOM & Selectors: Landmark `<section class="sr-only">` presenting display lead `MilleDollars` and copy excerpt *"Creative bureau focused on high-end video production. Working wor"* over `#e0dee1` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1440×900px` desktop / `390×844px` mobile) sets `#e0dee1` background with `#000000` headline `MilleDollars`.
3. **Primary Showcase & Content Grid (<section.sr-only:nth(2)> — `The Dazzling Division`)**:
   - DOM & Selectors: Landmark `<section class="sr-only">` rendering section `The Dazzling Division` with copy *"The Dazzling Division — Richard Mille (2026)"*, asset references (`fonts.googleapis.com`, `fonts.gstatic.com`, `prismic.min.js`, `css2`), and grid rule `.a-mask-lines_inner-mask { margin-bottom:-.2lh }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.sr-only:nth(2)> — `The Dazzling Division`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1200px`, `gap: 4px`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--header-spacing-y)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.sr-only:nth(3)> — `Ultimate Shield`)**:
   - DOM & Selectors: Landmark `<section class="sr-only">` framing `Ultimate Shield` and `Eternal Snow` (*"Ultimate Shield — EviDenS de Beauté (2026)"*) with `#ffffff` surface cards, `#c2a1c7` accents, and `.a-lines { --appear-y:var(--y,120%) }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.sr-only:nth(3)> — `Ultimate Shield`)` uses `50%`, `.5rem`, `.4rem`, `1rem` radii, `#c2a1c7` highlights, and assets (fonts.googleapis.com, fonts.gstatic.com, prismic.min.js).
5. **Colophon & Global Directory Footer (<footer.c-preloader-logo-loop> — `https://milledollars.fr/`)**:
   - DOM & Selectors: Landmark `<footer class="c-preloader-logo-loop">` anchoring `MilleDollars` footer links (`Home · Works · Info · Contact`), copy *"Eternal Snow — Richard Mille (2026)"*, and `#ffffff` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.c-preloader-logo-loop> — `https://milledollars.fr/`)` aligns to `1200px` (non-`@media` desktop container stylesheet rule) with `var(--header-spacing-y)` lateral canvas padding with `4px` grid gap and attributes (data-hid="prismic-preview", data-hid="jsonld-seo", data-symbol="logo").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Creative bureau focused on high-end video production. Working worldwide."*
- Copy Excerpt 2: *"The Dazzling Division — Richard Mille (2026)"*
- Copy Excerpt 3: *"Ultimate Shield — EviDenS de Beauté (2026)"*
- Copy Excerpt 4: *"Eternal Snow — Richard Mille (2026)"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.55,.085,.68,.53)`, `cubic-bezier(.19,1,.22,1)`, `cubic-bezier(.55,.055,.675,.19)`
- **Extracted Stylesheet Rules (`milledollars-fr`)**:
- `.o-header-top-item { display:none }`
- `.a-mask-lines_inner-mask { margin-bottom:-.2lh }`
- `.a-lines { --appear-y:var(--y,120%) }`
- `.u-anim.is-inview .a-lines.-contr... { --appear-y:0 }`
- `.a-lines.-instant .a-lines_inner { transition-duration:0s }`
- **Per-Selector Transition Rules**:
- **Selector `.o-header-top-item`**: `transition: color .2s linear` extracted from `milledollars-fr` stylesheet.
- **Selector `.a-lines_inner`**: `transition: transform .26s cubic-bezier(.55,.085,.68,.53) var(--delay-out,0s)` extracted from `milledollars-fr` stylesheet.
- **Selector `.a-lines.-instant .a-lines_inner`**: `transition: 0s` extracted from `milledollars-fr` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.55,.085,.68,.53)`)**: Governs interactive state transitions across `<header.c-header>` and `<section.sr-only:nth(2)>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `milledollars-fr`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
