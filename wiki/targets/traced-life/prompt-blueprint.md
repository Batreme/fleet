---
title: "UI Prompt Blueprint: traced-life"
date: 2026-11-15
target: "[[overview|traced-life]]"
status: analyzed
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#f5f5f5` accent)"
---

# UI Design System & Master Generation Blueprint: traced-life

> **At-Home Environmental Exposure Test · Traced** (https://traced.life/) — Trace 15 environmental elements from one strand of hair. A personal 30-day timeline, percentile rankings against a global database, and g...

![Desktop Viewport Capture (1440x12284)](file:///root/projects/fleet/wiki/targets/traced-life/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **At-Home Environmental Exposure Test · Traced** (`https://traced.life/`). Trace 15 environmental elements from one strand of hair. A personal 30-day timeline, percentile rankings against a global database, and g...
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#f5f5f5` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--color-black)` in `:root`) paired with `#fff` primary typography and `#f5f5f5` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Saans` for display copy (`Time leaves traces. Now you can read`) with `Saans Semi Mono` and `Saans Semi Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `30rem` container bounds (`gap: .375rem`, padding `.5rem`) with `cubic-bezier(.4,0,1,1)` easing and Swiper Touch Carousel Engine.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/traced-life/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×12284px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `30rem` extracted from `traced-life` stylesheet.
- **Canvas Lateral Padding & Spacing**: `.5rem` lateral canvas padding with `.375rem` grid gap.
- **Border Radius Scale**: `var(--radius-xl)`, `1rem`, `50%`, `var(--radius-full)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 30rem`, `gap: .375rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `.5rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:no-preference)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (prefers-reduced-motion:reduce)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#d9d9d9` | `var(--color-grey)` in `:root` |
| **Interactive Accent / Highlight** | `#f5f5f5` | `var(--color-light)` in `:root` |
| **Secondary / Muted Copy** | `#f8f8f8` | `var(--color-light-70)` in `:root` |
| **Structural Hairline Border** | `#fafafa` | `var(--color-light-50)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `"Saans",sans-serif` | Typography / Scale Token |
| `--font-serif` | `"Serrif",serif` | Typography / Scale Token |
| `--font-mono` | `"Saans Semi Mono",monospace` | Typography / Scale Token |
| `--spacing` | `0.063rem` | Layout / Spatial Grid Token |
| `--font-weight-light` | `300` | Canvas / Surface Token |
| `--font-weight-normal` | `400` | Typography / Scale Token |
| `--font-weight-bold` | `700` | Typography / Scale Token |
| `--radius-lg` | `1.5rem` | Elevation / Border Token |
| `--radius-xl` | `2rem` | Elevation / Border Token |
| `--ease-in` | `cubic-bezier(.4,0,1,1)` | Motion / Easing Token |
| `--ease-out` | `cubic-bezier(0,0,.2,1)` | Motion / Easing Token |
| `--ease-in-out` | `cubic-bezier(.4,0,.2,1)` | Motion / Easing Token |
| `--aspect-video` | `16/9` | Design System Custom Token |
| `--default-transition-duration` | `.15s` | Motion / Easing Token |
| `--default-transition-timing-function` | `cubic-bezier(.4,0,.2,1)` | Motion / Easing Token |
| `--default-font-family` | `var(--font-sans)` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Saans`.
- **Primary Body Stack**: `Saans Semi Mono`.
- **Technical / Metadata Stack**: `Saans Semi Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 2.5rem`, `line-height: 100%`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 1.5rem`, `line-height: 110%`).
- **Body Copy**: CSS variables `--oke-bodyText-fontWeight: 400`, `--oke-bodyText-fontSize: var(--oke-text-regular,14px)`, `--oke-bodyText-fontFamily: inherit`; rule `p` (`font-size: 1rem`, `line-height: 120%`).
- **Metadata & Navigation Labels**: CSS variables `--font-mono: "Saans Semi Mono",monospace`, `--default-mono-font-family: var(--font-mono)`, `--oke-text-small: 0.75rem`; rule `small` (`font-size: calc(var(--kl-reviews-reviews...`, `font-weight: var(--kl-revi...`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `traced-life` stylesheet.
- **Selector `dialog::backdrop`**: `transition: opacity .35s` extracted from `traced-life` stylesheet.
- **Selector `.swiper-wrapper`**: `transition: var(--swiper-wrapper-transition-timing-function,initial)` extracted from `traced-life` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.contents>` and `<section.w-full>`.
- **Runtime Interaction Engine**: Integrates Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — At-Home Environmental Exposure Test · Trac │
│ ====================================================================== │
│ [ <header.contents>        | Shop · What we test · Report · Science ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.relative>                                   |   │
│ | H1: Time leaves traces. Now you can read them.                   |   │
│ | Substrate: #000       | Ink: #fff       | Accent: #f5f5f5        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.w-full>          ) max-w: 30rem          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Why Traced?                  |  | The difference               | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .375re) | │
│ | [<header.contents>] -> [<section.relative>] -> [<section.w-full>] |  │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.contents>     ) | https://traced.life/               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.contents> — `traced-life`)**:
   - Landmark `<header class="contents">` hosting `At-Home Environmental Exposure Test ` navigation (`Shop · What we test · Report · Science · Our story`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-shop-id="70566805578"`, `data-venmo-supported="false"`, `data-environment="production"`), and stylesheet rule `before { border:0 solid;box-sizing:border-box;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.relative> — `Time leaves traces. Now you can re`)**:
   - Landmark `<section class="relative w-full">` presenting display lead `Time leaves traces. Now you can read them.` and copy excerpt *"Learn What we test Report Science Our story Journal FAQs"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.w-full> — `Why Traced?`)**:
   - Landmark `<section class="w-full relative">` rendering section `Why Traced?` with copy *"Traced™ Environmental Exposure Test"*, asset references (`awin-shopify-integration-code.js`, `loader.js`, `sealsubscriptions.js`, `990232790301153`), and grid rule `webkit-file-upload-button { border:0 solid;box-sizing:border-box;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.w-full> — `The difference`)**:
   - Landmark `<section class="w-full relative">` framing `The difference` and `How It Works` (*"Nickel contaminants"*) with `#d9d9d9` surface cards, `#f5f5f5` accents, and `file-selector-button { border:0 solid;box-sizing:border-box;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.contents> — `https://traced.life/`)**:
   - Landmark `<footer class="contents">` anchoring `At-Home Environmental Exposure T` footer links (`Shop · What we test · Report · Science · Our story`), copy *"Trace your exposures"*, and `#fafafa` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: traced-life (At-Home Environmental Exposure Test · Traced)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `traced-life` (**At-Home Environmental Exposure Test · Traced** — `https://traced.life/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#f5f5f5` accent).
- **Identity & Domain Context**: Trace 15 environmental elements from one strand of hair. A personal 30-day timeline, percentile rankings against a global database, and g...
- **Primary Substrate**: `#000` (`var(--color-black)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#f5f5f5`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--color-black)` in `:root`) paired with `#fff` primary typography and `#f5f5f5` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Saans` for display copy (`Time leaves traces. Now you can read`) with `Saans Semi Mono` and `Saans Semi Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `30rem` container bounds (`gap: .375rem`, padding `.5rem`) with `cubic-bezier(.4,0,1,1)` easing and Swiper Touch Carousel Engine.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `traced-life` in your global stylesheet:

:root {
  /* At-Home Environmental Exposure Test · Traced (traced-life) — Ground-Truth Extracted CSS Variables */
  --font-sans: "Saans",sans-serif; /* Typography / Scale Token (traced-life) */
  --font-serif: "Serrif",serif; /* Typography / Scale Token (traced-life) */
  --font-mono: "Saans Semi Mono",monospace; /* Typography / Scale Token (traced-life) */
  --spacing: 0.063rem; /* Layout / Spatial Grid Token (traced-life) */
  --font-weight-light: 300; /* Canvas / Surface Token (traced-life) */
  --font-weight-normal: 400; /* Typography / Scale Token (traced-life) */
  --font-weight-bold: 700; /* Typography / Scale Token (traced-life) */
  --radius-lg: 1.5rem; /* Elevation / Border Token (traced-life) */
  --radius-xl: 2rem; /* Elevation / Border Token (traced-life) */
  --ease-in: cubic-bezier(.4,0,1,1); /* Motion / Easing Token (traced-life) */
  --ease-out: cubic-bezier(0,0,.2,1); /* Motion / Easing Token (traced-life) */
  --ease-in-out: cubic-bezier(.4,0,.2,1); /* Motion / Easing Token (traced-life) */
  --aspect-video: 16/9; /* Design System Custom Token (traced-life) */
  --default-transition-duration: .15s; /* Motion / Easing Token (traced-life) */
  --default-transition-timing-function: cubic-bezier(.4,0,.2,1); /* Motion / Easing Token (traced-life) */
  --default-font-family: var(--font-sans); /* Typography / Scale Token (traced-life) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000` — grounded in `var(--color-black)` in `:root`
- **Primary Typography Ink**: `#fff` — grounded in `var(--color-white)` in `:root`
- **Elevated Surface / Card Substrate**: `#d9d9d9` — grounded in `var(--color-grey)` in `:root`
- **Interactive Accent / Highlight**: `#f5f5f5` — grounded in `var(--color-light)` in `:root`
- **Secondary / Muted Copy**: `#f8f8f8` — grounded in `var(--color-light-70)` in `:root`
- **Structural Hairline Border**: `#fafafa` — grounded in `var(--color-light-50)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×12284px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `30rem` extracted from `traced-life` stylesheet
- **Padding & Gutters**: `.5rem` lateral canvas padding with `.375rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 30rem`, `gap: .375rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `.5rem` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:no-preference)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (prefers-reduced-motion:reduce)`
- **Corner Radii**: `var(--radius-xl)`, `1rem`, `50%`, `var(--radius-full)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Saans`
- **Body Font Stack**: `Saans Semi Mono`
- **Monospace / Technical Font Stack**: `Saans Semi Mono`
- **H1 Display Rule**: rule `h1` (`font-size: 2.5rem`, `line-height: 100%`)
- **H2 Section Rule**: rule `h2` (`font-size: 1.5rem`, `line-height: 110%`)
- **Body Copy Rule**: CSS variables `--oke-bodyText-fontWeight: 400`, `--oke-bodyText-fontSize: var(--oke-text-regular,14px)`, `--oke-bodyText-fontFamily: inherit`; rule `p` (`font-size: 1rem`, `line-height: 120%`)
- **Metadata & Index Rule**: CSS variables `--font-mono: "Saans Semi Mono",monospace`, `--default-mono-font-family: var(--font-mono)`, `--oke-text-small: 0.75rem`; rule `small` (`font-size: calc(var(--kl-reviews-reviews...`, `font-weight: var(--kl-revi...`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `traced-life` (`At-Home Environmental Exposure Test · Traced`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.contents> — `traced-life`)**:
   - DOM & Selectors: Landmark `<header class="contents">` hosting `At-Home Environmental Exposure Test ` navigation (`Shop · What we test · Report · Science · Our story`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-shop-id="70566805578"`, `data-venmo-supported="false"`, `data-environment="production"`), and stylesheet rule `before { border:0 solid;box-sizing:border-box;margin:0;padding:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.contents> — `traced-life`)` (`traced-life`) adapts across `@media (prefers-reduced-motion:no-preference)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (prefers-reduced-motion:reduce)` with `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `Shop · What we test · Report · Science · Our story`.
2. **Hero Stage & Focal Lead (<section.relative> — `Time leaves traces. Now you can re`)**:
   - DOM & Selectors: Landmark `<section class="relative w-full">` presenting display lead `Time leaves traces. Now you can read them.` and copy excerpt *"Learn What we test Report Science Our story Journal FAQs"* over `#000` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×12284px` desktop / `390×2400px` mobile) sets `#000` background with `#fff` headline `Time leaves traces. Now you can read them.`.
3. **Primary Showcase & Content Grid (<section.w-full> — `Why Traced?`)**:
   - DOM & Selectors: Landmark `<section class="w-full relative">` rendering section `Why Traced?` with copy *"Traced™ Environmental Exposure Test"*, asset references (`awin-shopify-integration-code.js`, `loader.js`, `sealsubscriptions.js`, `990232790301153`), and grid rule `webkit-file-upload-button { border:0 solid;box-sizing:border-box;margin:0;padding:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.w-full> — `Why Traced?`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 30rem`, `gap: .375rem`) on desktop and Single-column vertical stack at `390px` viewport width with `.5rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.w-full> — `The difference`)**:
   - DOM & Selectors: Landmark `<section class="w-full relative">` framing `The difference` and `How It Works` (*"Nickel contaminants"*) with `#d9d9d9` surface cards, `#f5f5f5` accents, and `file-selector-button { border:0 solid;box-sizing:border-box;margin:0;padding:0 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.w-full> — `The difference`)` uses `var(--radius-xl)`, `1rem`, `50%`, `var(--radius-full)` radii, `#f5f5f5` highlights, and assets (awin-shopify-integration-code.js, loader.js, sealsubscriptions.js).
5. **Colophon & Global Directory Footer (<footer.contents> — `https://traced.life/`)**:
   - DOM & Selectors: Landmark `<footer class="contents">` anchoring `At-Home Environmental Exposure T` footer links (`Shop · What we test · Report · Science · Our story`), copy *"Trace your exposures"*, and `#fafafa` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.contents> — `https://traced.life/`)` aligns to `30rem` extracted from `traced-life` stylesheet with `.5rem` lateral canvas padding with `.375rem` grid gap and attributes (data-source-attribution="shopify.exit_intersti...", data-shop-id="70566805578", data-venmo-supported="false").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Learn What we test Report Science Our story Journal FAQs"*
- Copy Excerpt 2: *"Traced™ Environmental Exposure Test"*
- Copy Excerpt 3: *"Nickel contaminants"*
- Copy Excerpt 4: *"Trace your exposures"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`traced-life`)**:
- `before { border:0 solid;box-sizing:border-box;margin:0;padding:0 }`
- `webkit-file-upload-button { border:0 solid;box-sizing:border-box;margin:0;padding:0 }`
- `file-selector-button { border:0 solid;box-sizing:border-box;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `traced-life` stylesheet.
- **Selector `dialog::backdrop`**: `transition: opacity .35s` extracted from `traced-life` stylesheet.
- **Selector `.swiper-wrapper`**: `transition: var(--swiper-wrapper-transition-timing-function,initial)` extracted from `traced-life` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.contents>` and `<section.w-full>`.
- **Runtime Interaction Engine**: Integrates Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `traced-life`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
