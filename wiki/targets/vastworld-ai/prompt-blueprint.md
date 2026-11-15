---
title: "UI Prompt Blueprint: vastworld-ai"
date: 2026-11-15
target: "[[overview|vastworld-ai]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#7a5a12`)"
---

# UI Design System & Master Generation Blueprint: vastworld-ai

> **VAST-A global Leading AI Company** (https://vastworld.ai/) — VAST-A global Leading AI Company

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/vastworld-ai/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **VAST-A global Leading AI Company** (`https://vastworld.ai/`). VAST-A global Leading AI Company
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#7a5a12`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--color-black)` in `:root`) paired with `#fff` primary typography and `#7a5a12` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Instrument Sans` for display copy (`B u i l d Y o u r W o r l d s`) with `Saans VF` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: var(--spacing)`, padding `var(--padding-vast)`) with `cubic-bezier(0,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/vastworld-ai/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `40rem` extracted from `vastworld-ai` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--padding-vast)` lateral canvas padding with `var(--spacing)` grid gap.
- **Border Radius Scale**: `.25rem`, `1px`, `2147483647px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--spacing)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--padding-vast)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (width>=40rem)`, `@media (width>=48rem)`, `@media (width>=64rem)`, `@media (width>=80rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#0006` | `var(--ds-dim)` in `:root` |
| **Interactive Accent / Highlight** | `#7a5a12` | `var(--ds-accent-gold)` in `:root` |
| **Secondary / Muted Copy** | `#FFFFFF` | `var(--navbar-ink-light)` in `:root` |
| **Structural Hairline Border** | `#000000` | `var(--navbar-ink-dark)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-red-400` | `oklch(70.4% .191 22.216)` | Brand / Palette Token |
| `--color-neutral-400` | `oklch(70.8% 0 none)` | Brand / Palette Token |
| `--color-neutral-900` | `oklch(20.5% 0 none)` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `calc(4 * var(--u))` | Layout / Spatial Grid Token |
| `--container-sm` | `24rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |
| `--text-xs--line-height` | `calc(1 / .75)` | Typography Ink Token |
| `--text-sm` | `.875rem` | Typography Ink Token |
| `--text-sm--line-height` | `calc(1.25 / .875)` | Typography Ink Token |
| `--text-base` | `1rem` | Typography Ink Token |
| `--text-base--line-height` | `calc(1.5 / 1)` | Typography Ink Token |
| `--text-lg` | `1.125rem` | Typography Ink Token |
| `--text-lg--line-height` | `calc(1.75 / 1.125)` | Typography Ink Token |
| `--text-xl` | `1.25rem` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Instrument Sans`.
- **Primary Body Stack**: `Saans VF`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--text-4xl: calc(var(--txt-4xl) * var(--u))`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: calc(var(--txt-5xl) * var(--u))`.
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: calc(var(--txt-3xl) * var(--u))`.
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`, `--lh-body: 1.35`.
- **Metadata & Navigation Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.33,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `vastworld-ai` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `vastworld-ai` stylesheet.
- **Selector `border-color\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `vastworld-ai` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.fixed>` and `<article.group>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — VAST-A global Leading AI Company           │
│ ====================================================================== │
│ [ <header.fixed>           | Home · Research · Universe · Product · ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.pb-16>                                      |   │
│ | H1: B u i l d Y o u r W o r l d s                                |   │
│ | Substrate: #000       | Ink: #fff       | Accent: #7a5a12        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<article.group>           ) max-w: 40rem          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | V A S T - A G l o b a l L e  |  | B u i l t o n R e s e a r c  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<header.fixed>] -> [<section.pb-16>] -> [<article.group>] |         │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.pointer-events) | https://vastworld.ai/              │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.fixed> — `vastworld-ai`)**:
   - Landmark `<header class="fixed z-30">` hosting `VAST-A global Leading AI Company` navigation (`Home · Research · Universe · Product · About`), DOM attributes (`data-barba="wrapper"`, `data-root`, `data-stats-panels-wrapper`, `data-barba="container"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.pb-16> — `B u i l d Y o u r W o r l d s`)**:
   - Landmark `<section class="pb-16 relative">` presenting display lead `B u i l d Y o u r W o r l d s` and copy excerpt *"Try Tripo Try Tripo Try Tripo"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<article.group> — `V A S T - A G l o b a l L e a d i `)**:
   - Landmark `<article class="group flex">` rendering section `V A S T - A G l o b a l L e a d i n g A I C o m p...` with copy *"V A S T - A G l o b a l"*, asset references (`InstrumentSans-variable-latin.woff2`, `favicon.ico`, `apple-touch-icon.png`, `page-wrapper.BKmYtgLc.css`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<article.group> — `B u i l t o n R e s e a r c h`)**:
   - Landmark `<article class="group flex">` framing `B u i l t o n R e s e a r c h` and `F r o m A s s e t s t o W o r l d s` (*"L e a d i n g A I C o m p a n y"*) with `#0006` surface cards, `#7a5a12` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.pointer-events-none> — `https://vastworld.ai/`)**:
   - Landmark `<footer class="pointer-events-none w-full">` anchoring `VAST-A global Leading AI Company` footer links (`Home · Research · Universe · Product · About`), copy *"Believing that 3D is the native form of the world, VAST turn"*, and `#000000` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: vastworld-ai (VAST-A global Leading AI Company)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `vastworld-ai` (**VAST-A global Leading AI Company** — `https://vastworld.ai/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#7a5a12`).
- **Identity & Domain Context**: VAST-A global Leading AI Company
- **Primary Substrate**: `#000` (`var(--color-black)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#7a5a12`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--color-black)` in `:root`) paired with `#fff` primary typography and `#7a5a12` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Instrument Sans` for display copy (`B u i l d Y o u r W o r l d s`) with `Saans VF` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: var(--spacing)`, padding `var(--padding-vast)`) with `cubic-bezier(0,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `vastworld-ai` in your global stylesheet:

:root {
  /* VAST-A global Leading AI Company (vastworld-ai) — Ground-Truth Extracted CSS Variables */
  --color-red-400: oklch(70.4% .191 22.216); /* Brand / Palette Token (vastworld-ai) */
  --color-neutral-400: oklch(70.8% 0 none); /* Brand / Palette Token (vastworld-ai) */
  --color-neutral-900: oklch(20.5% 0 none); /* Brand / Palette Token (vastworld-ai) */
  --color-black: #000; /* Canvas / Surface Token (vastworld-ai) */
  --color-white: #fff; /* Canvas / Surface Token (vastworld-ai) */
  --spacing: calc(4 * var(--u)); /* Layout / Spatial Grid Token (vastworld-ai) */
  --container-sm: 24rem; /* Layout / Spatial Grid Token (vastworld-ai) */
  --text-xs: .75rem; /* Typography Ink Token (vastworld-ai) */
  --text-xs--line-height: calc(1 / .75); /* Typography Ink Token (vastworld-ai) */
  --text-sm: .875rem; /* Typography Ink Token (vastworld-ai) */
  --text-sm--line-height: calc(1.25 / .875); /* Typography Ink Token (vastworld-ai) */
  --text-base: 1rem; /* Typography Ink Token (vastworld-ai) */
  --text-base--line-height: calc(1.5 / 1); /* Typography Ink Token (vastworld-ai) */
  --text-lg: 1.125rem; /* Typography Ink Token (vastworld-ai) */
  --text-lg--line-height: calc(1.75 / 1.125); /* Typography Ink Token (vastworld-ai) */
  --text-xl: 1.25rem; /* Typography Ink Token (vastworld-ai) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000` — grounded in `var(--color-black)` in `:root`
- **Primary Typography Ink**: `#fff` — grounded in `var(--color-white)` in `:root`
- **Elevated Surface / Card Substrate**: `#0006` — grounded in `var(--ds-dim)` in `:root`
- **Interactive Accent / Highlight**: `#7a5a12` — grounded in `var(--ds-accent-gold)` in `:root`
- **Secondary / Muted Copy**: `#FFFFFF` — grounded in `var(--navbar-ink-light)` in `:root`
- **Structural Hairline Border**: `#000000` — grounded in `var(--navbar-ink-dark)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `40rem` extracted from `vastworld-ai` stylesheet
- **Padding & Gutters**: `var(--padding-vast)` lateral canvas padding with `var(--spacing)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--spacing)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--padding-vast)` horizontal padding
- **Media Queries**: `@media (width>=40rem)`, `@media (width>=48rem)`, `@media (width>=64rem)`, `@media (width>=80rem)`
- **Corner Radii**: `.25rem`, `1px`, `2147483647px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Instrument Sans`
- **Body Font Stack**: `Saans VF`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: CSS variables `--text-4xl: calc(var(--txt-4xl) * var(--u))`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: calc(var(--txt-5xl) * var(--u))`
- **H2 Section Rule**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: calc(var(--txt-3xl) * var(--u))`
- **Body Copy Rule**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`, `--lh-body: 1.35`
- **Metadata & Index Rule**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `vastworld-ai` (`VAST-A global Leading AI Company`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.fixed> — `vastworld-ai`)**:
   - DOM & Selectors: Landmark `<header class="fixed z-30">` hosting `VAST-A global Leading AI Company` navigation (`Home · Research · Universe · Product · About`), DOM attributes (`data-barba="wrapper"`, `data-root`, `data-stats-panels-wrapper`, `data-barba="container"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.fixed> — `vastworld-ai`)` (`vastworld-ai`) adapts across `@media (width>=40rem)`, `@media (width>=48rem)`, `@media (width>=64rem)`, `@media (width>=80rem)` with `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.33,0,.2,1)` transitions and links `Home · Research · Universe · Product · About`.
2. **Hero Stage & Focal Lead (<section.pb-16> — `B u i l d Y o u r W o r l d s`)**:
   - DOM & Selectors: Landmark `<section class="pb-16 relative">` presenting display lead `B u i l d Y o u r W o r l d s` and copy excerpt *"Try Tripo Try Tripo Try Tripo"* over `#000` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#000` background with `#fff` headline `B u i l d Y o u r W o r l d s`.
3. **Primary Showcase & Content Grid (<article.group> — `V A S T - A G l o b a l L e a d i `)**:
   - DOM & Selectors: Landmark `<article class="group flex">` rendering section `V A S T - A G l o b a l L e a d i n g A I C o m p...` with copy *"V A S T - A G l o b a l"*, asset references (`InstrumentSans-variable-latin.woff2`, `favicon.ico`, `apple-touch-icon.png`, `page-wrapper.BKmYtgLc.css`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<article.group> — `V A S T - A G l o b a l L e a d i `)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--spacing)`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--padding-vast)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.group> — `B u i l t o n R e s e a r c h`)**:
   - DOM & Selectors: Landmark `<article class="group flex">` framing `B u i l t o n R e s e a r c h` and `F r o m A s s e t s t o W o r l d s` (*"L e a d i n g A I C o m p a n y"*) with `#0006` surface cards, `#7a5a12` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.group> — `B u i l t o n R e s e a r c h`)` uses `.25rem`, `1px`, `2147483647px` radii, `#7a5a12` highlights, and assets (InstrumentSans-variable-latin.woff2, favicon.ico, apple-touch-icon.png).
5. **Colophon & Global Directory Footer (<footer.pointer-events-none> — `https://vastworld.ai/`)**:
   - DOM & Selectors: Landmark `<footer class="pointer-events-none w-full">` anchoring `VAST-A global Leading AI Company` footer links (`Home · Research · Universe · Product · About`), copy *"Believing that 3D is the native form of the world, VAST turn"*, and `#000000` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.pointer-events-none> — `https://vastworld.ai/`)` aligns to `40rem` extracted from `vastworld-ai` stylesheet with `var(--padding-vast)` lateral canvas padding with `var(--spacing)` grid gap and attributes (data-barba="wrapper", data-root, data-stats-panels-wrapper).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Try Tripo Try Tripo Try Tripo"*
- Copy Excerpt 2: *"V A S T - A G l o b a l"*
- Copy Excerpt 3: *"L e a d i n g A I C o m p a n y"*
- Copy Excerpt 4: *"Believing that 3D is the native form of the world, VAST turns ideas into immersive..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.33,0,.2,1)`
- **Extracted Stylesheet Rules (`vastworld-ai`)**:
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- `sup { vertical-align:baseline;font-size:75%;line-height:0;position:relative }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `vastworld-ai` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `vastworld-ai` stylesheet.
- **Selector `border-color\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `vastworld-ai` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.fixed>` and `<article.group>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `vastworld-ai`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
