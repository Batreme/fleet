---
title: "UI Prompt Blueprint: seedrouter-ai"
date: 2026-11-15
target: "[[overview|seedrouter-ai]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#fef2f2` canvas, `#e40014` ink, `#ff6568` accent)"
---

# UI Design System & Master Generation Blueprint: seedrouter-ai

> **SeedRouter · One API for Image, Video, LLM and Audio Models** (https://seedrouter.ai) — SeedRouter puts image, video, language and audio models behind one API key with pay-per-request billing. Failed requests cost nothing. Ge...

![Desktop Viewport Capture (1440x10504)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **SeedRouter · One API for Image, Video, LLM and Audio Models** (`https://seedrouter.ai`). SeedRouter puts image, video, language and audio models behind one API key with pay-per-request billing. Failed requests cost nothing. Ge...
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#fef2f2` canvas, `#e40014` ink, `#ff6568` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fef2f2` (`var(--color-red-50)` in `:root`) paired with `#e40014` primary typography and `#ff6568` accents.
  - **Extracted Typographic Hierarchy**: Pairs `JetBrains Mono` for display copy (`SeedRouter: one API for every model `) with `JetBrains Mono Fallback` and `JetBrains Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: var(--gap)`, padding `var(--card-spacing)`) with `cubic-bezier(0,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×10504px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `40rem` extracted from `seedrouter-ai` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--card-spacing)` lateral canvas padding with `var(--gap)` grid gap.
- **Border Radius Scale**: `var(--radius)`, `.25rem`, `var(--cell-radius)`, `2px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--gap)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--card-spacing)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fef2f2` | `var(--color-red-50)` in `:root` |
| **Primary Typography Ink** | `#ffe2e2` | `var(--color-red-100)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ffa3a3` | `var(--color-red-300)` in `:root` |
| **Interactive Accent / Highlight** | `#ff6568` | `var(--color-red-400)` in `:root` |
| **Secondary / Muted Copy** | `#fb2c36` | `var(--color-red-500)` in `:root` |
| **Structural Hairline Border** | `#e40014` | `var(--color-red-600)` in `:root` |
| **Variable Token (`--color-red-700`)** | `#bf000f` | `var(--color-red-700)` in `:root` |
| **Variable Token (`--color-red-950`)** | `#460809` | `var(--color-red-950)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--shimmer-angle` | `20deg` | Design System Custom Token |
| `--scroll-fade-t` | `0px` | Dimension / Scale Token |
| `--scroll-fade-b` | `0px` | Dimension / Scale Token |
| `--scroll-fade-s` | `0px` | Dimension / Scale Token |
| `--scroll-fade-e` | `0px` | Dimension / Scale Token |
| `--scroll-fade-mask` | `initial` | Design System Custom Token |
| `--shimmer-image` | `initial` | Design System Custom Token |
| `--shimmer-text-fill` | `initial` | Typography Ink Token |
| `--color-red-50` | `#fef2f2` | Brand / Palette Token |
| `--color-red-100` | `#ffe2e2` | Brand / Palette Token |
| `--color-red-300` | `#ffa3a3` | Brand / Palette Token |
| `--color-red-400` | `#ff6568` | Brand / Palette Token |
| `--color-red-500` | `#fb2c36` | Brand / Palette Token |
| `--color-red-600` | `#e40014` | Brand / Palette Token |
| `--color-red-700` | `#bf000f` | Brand / Palette Token |
| `--color-red-950` | `#460809` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `JetBrains Mono`.
- **Primary Body Stack**: `JetBrains Mono Fallback`.
- **Technical / Metadata Stack**: `JetBrains Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`; rule `h1` (`letter-spacing: -.025em`, `font-weight: 500`).
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `,h2` (`letter-spacing: -.02em`, `font-weight: 400`).
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`, `--font-body-ext: "Nunito Sans", "Nunito Sans Fallback"`.
- **Metadata & Navigation Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.22,1,.36,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `seedrouter-ai` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `seedrouter-ai` stylesheet.
- **Selector `transform\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `seedrouter-ai` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.sr-chrome>` and `<section.pb-16>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — SeedRouter · One API for Image, Video, LLM │
│ ====================================================================== │
│ [ <header.sr-chrome>       | SeedRouter · Models · Pricing · Docs · ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.sr-hero>                                    |   │
│ | H1: SeedRouter: one API for every model your product...          |   │
│ | Substrate: #fef2f2    | Ink: #e40014    | Accent: #ff6568        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.pb-16>           ) max-w: 40rem          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Models you can call on SeedR |  | Integration in 4 steps       | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<header.sr-chrome>] -> [<section.sr-hero>] -> [<section.pb-16>] |   │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.sr-chrome-dark) | https://seedrouter.ai              │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.sr-chrome> — `seedrouter-ai`)**:
   - Landmark `<header class="sr-chrome sticky">` hosting `SeedRouter · One API for Image, Vide` navigation (`SeedRouter · Models · Pricing · Docs · Sign up`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-testid="announcement-dismiss"`, `data-nimg="1"`), and stylesheet rule `host { --shimmer-angle:20deg }`.
2. **Hero Stage & Focal Lead (<section.sr-hero> — `SeedRouter: one API for every mode`)**:
   - Landmark `<section class="sr-hero sr-chrome-dark">` presenting display lead `SeedRouter: one API for every model your product...` and copy excerpt *"Seedance 2.5 is live on SeedRouter Try Seedance 2.5"* over `#fef2f2` canvas and `#e40014` ink.
3. **Primary Showcase & Content Grid (<section.pb-16> — `Models you can call on SeedRouter `)**:
   - Landmark `<section class="pb-16 pt-10">` rendering section `Models you can call on SeedRouter today` with copy *"Seedance 2.5 is live on SeedRouter"*, asset references (`0c8c4ded07fff55c-s.p.2tcyrya9o07v...`, `1b99372b3eaef0c8-s.p.1gsd1jahc5dg...`, `70bc3e132a0a741e-s.p.3t6q91iet4ns...`, `bytedance.svg`), and grid rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.py-16> — `Integration in 4 steps`)**:
   - Landmark `<section class="py-16">` framing `Integration in 4 steps` and `Sign up` (*"01 · Image, video, language and audio · one key"*) with `#ffa3a3` surface cards, `#ff6568` accents, and `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.sr-chrome-dark> — `https://seedrouter.ai`)**:
   - Landmark `<footer class="sr-chrome-dark relative">` anchoring `SeedRouter · One API for Image, ` footer links (`SeedRouter · Models · Pricing · Docs · Sign up`), copy *"one API for every model your product needs"*, and `#e40014` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: seedrouter-ai (SeedRouter · One API for Image, Video, LLM and Audio Models)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `seedrouter-ai` (**SeedRouter · One API for Image, Video, LLM and Audio Models** — `https://seedrouter.ai`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#fef2f2` canvas, `#e40014` ink, `#ff6568` accent).
- **Identity & Domain Context**: SeedRouter puts image, video, language and audio models behind one API key with pay-per-request billing. Failed requests cost nothing. Ge...
- **Primary Substrate**: `#fef2f2` (`var(--color-red-50)` in `:root`), **Primary Ink**: `#e40014`, **Accent / Highlight**: `#ff6568`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fef2f2` (`var(--color-red-50)` in `:root`) paired with `#e40014` primary typography and `#ff6568` accents.
  - **Extracted Typographic Hierarchy**: Pairs `JetBrains Mono` for display copy (`SeedRouter: one API for every model `) with `JetBrains Mono Fallback` and `JetBrains Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: var(--gap)`, padding `var(--card-spacing)`) with `cubic-bezier(0,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `seedrouter-ai` in your global stylesheet:

:root {
  /* SeedRouter · One API for Image, Video, LLM and Audio Models (seedrouter-ai) — Ground-Truth Extracted CSS Variables */
  --shimmer-angle: 20deg; /* Design System Custom Token (seedrouter-ai) */
  --scroll-fade-t: 0px; /* Dimension / Scale Token (seedrouter-ai) */
  --scroll-fade-b: 0px; /* Dimension / Scale Token (seedrouter-ai) */
  --scroll-fade-s: 0px; /* Dimension / Scale Token (seedrouter-ai) */
  --scroll-fade-e: 0px; /* Dimension / Scale Token (seedrouter-ai) */
  --scroll-fade-mask: initial; /* Design System Custom Token (seedrouter-ai) */
  --shimmer-image: initial; /* Design System Custom Token (seedrouter-ai) */
  --shimmer-text-fill: initial; /* Typography Ink Token (seedrouter-ai) */
  --color-red-50: #fef2f2; /* Brand / Palette Token (seedrouter-ai) */
  --color-red-100: #ffe2e2; /* Brand / Palette Token (seedrouter-ai) */
  --color-red-300: #ffa3a3; /* Brand / Palette Token (seedrouter-ai) */
  --color-red-400: #ff6568; /* Brand / Palette Token (seedrouter-ai) */
  --color-red-500: #fb2c36; /* Brand / Palette Token (seedrouter-ai) */
  --color-red-600: #e40014; /* Brand / Palette Token (seedrouter-ai) */
  --color-red-700: #bf000f; /* Brand / Palette Token (seedrouter-ai) */
  --color-red-950: #460809; /* Brand / Palette Token (seedrouter-ai) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fef2f2` — grounded in `var(--color-red-50)` in `:root`
- **Primary Typography Ink**: `#ffe2e2` — grounded in `var(--color-red-100)` in `:root`
- **Elevated Surface / Card Substrate**: `#ffa3a3` — grounded in `var(--color-red-300)` in `:root`
- **Interactive Accent / Highlight**: `#ff6568` — grounded in `var(--color-red-400)` in `:root`
- **Secondary / Muted Copy**: `#fb2c36` — grounded in `var(--color-red-500)` in `:root`
- **Structural Hairline Border**: `#e40014` — grounded in `var(--color-red-600)` in `:root`
- **Variable Token (`--color-red-700`)**: `#bf000f` — grounded in `var(--color-red-700)` in `:root`
- **Variable Token (`--color-red-950`)**: `#460809` — grounded in `var(--color-red-950)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×10504px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `40rem` extracted from `seedrouter-ai` stylesheet
- **Padding & Gutters**: `var(--card-spacing)` lateral canvas padding with `var(--gap)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--gap)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--card-spacing)` horizontal padding
- **Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`
- **Corner Radii**: `var(--radius)`, `.25rem`, `var(--cell-radius)`, `2px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `JetBrains Mono`
- **Body Font Stack**: `JetBrains Mono Fallback`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **H1 Display Rule**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`; rule `h1` (`letter-spacing: -.025em`, `font-weight: 500`)
- **H2 Section Rule**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `,h2` (`letter-spacing: -.02em`, `font-weight: 400`)
- **Body Copy Rule**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`, `--font-body-ext: "Nunito Sans", "Nunito Sans Fallback"`
- **Metadata & Index Rule**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `seedrouter-ai` (`SeedRouter · One API for Image, Video, LLM and Audio Models`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.sr-chrome> — `seedrouter-ai`)**:
   - DOM & Selectors: Landmark `<header class="sr-chrome sticky">` hosting `SeedRouter · One API for Image, Vide` navigation (`SeedRouter · Models · Pricing · Docs · Sign up`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-testid="announcement-dismiss"`, `data-nimg="1"`), and stylesheet rule `host { --shimmer-angle:20deg }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.sr-chrome> — `seedrouter-ai`)` (`seedrouter-ai`) adapts across `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)` with `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.22,1,.36,1)` transitions and links `SeedRouter · Models · Pricing · Docs · Sign up`.
2. **Hero Stage & Focal Lead (<section.sr-hero> — `SeedRouter: one API for every mode`)**:
   - DOM & Selectors: Landmark `<section class="sr-hero sr-chrome-dark">` presenting display lead `SeedRouter: one API for every model your product...` and copy excerpt *"Seedance 2.5 is live on SeedRouter Try Seedance 2.5"* over `#fef2f2` canvas and `#e40014` ink.
   - Responsive Contract: Hero stage (`1440×10504px` desktop / `390×2400px` mobile) sets `#fef2f2` background with `#e40014` headline `SeedRouter: one API for every model your product...`.
3. **Primary Showcase & Content Grid (<section.pb-16> — `Models you can call on SeedRouter `)**:
   - DOM & Selectors: Landmark `<section class="pb-16 pt-10">` rendering section `Models you can call on SeedRouter today` with copy *"Seedance 2.5 is live on SeedRouter"*, asset references (`0c8c4ded07fff55c-s.p.2tcyrya9o07v...`, `1b99372b3eaef0c8-s.p.1gsd1jahc5dg...`, `70bc3e132a0a741e-s.p.3t6q91iet4ns...`, `bytedance.svg`), and grid rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.pb-16> — `Models you can call on SeedRouter `)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--gap)`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--card-spacing)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.py-16> — `Integration in 4 steps`)**:
   - DOM & Selectors: Landmark `<section class="py-16">` framing `Integration in 4 steps` and `Sign up` (*"01 · Image, video, language and audio · one key"*) with `#ffa3a3` surface cards, `#ff6568` accents, and `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.py-16> — `Integration in 4 steps`)` uses `var(--radius)`, `.25rem`, `var(--cell-radius)`, `2px` radii, `#ff6568` highlights, and assets (0c8c4ded07fff55c-s.p.2tcyrya9o07v..., 1b99372b3eaef0c8-s.p.1gsd1jahc5dg..., 70bc3e132a0a741e-s.p.3t6q91iet4ns...).
5. **Colophon & Global Directory Footer (<footer.sr-chrome-dark> — `https://seedrouter.ai`)**:
   - DOM & Selectors: Landmark `<footer class="sr-chrome-dark relative">` anchoring `SeedRouter · One API for Image, ` footer links (`SeedRouter · Models · Pricing · Docs · Sign up`), copy *"one API for every model your product needs"*, and `#e40014` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.sr-chrome-dark> — `https://seedrouter.ai`)` aligns to `40rem` extracted from `seedrouter-ai` stylesheet with `var(--card-spacing)` lateral canvas padding with `var(--gap)` grid gap and attributes (data-precedence="next", data-precedence="next", data-testid="announcement-dismiss").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Seedance 2.5 is live on SeedRouter Try Seedance 2.5"*
- Copy Excerpt 2: *"Seedance 2.5 is live on SeedRouter"*
- Copy Excerpt 3: *"01 · Image, video, language and audio · one key"*
- Copy Excerpt 4: *"one API for every model your product needs"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.22,1,.36,1)`
- **Extracted Stylesheet Rules (`seedrouter-ai`)**:
- `host { --shimmer-angle:20deg }`
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `seedrouter-ai` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `seedrouter-ai` stylesheet.
- **Selector `transform\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `seedrouter-ai` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.sr-chrome>` and `<section.pb-16>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `seedrouter-ai`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
