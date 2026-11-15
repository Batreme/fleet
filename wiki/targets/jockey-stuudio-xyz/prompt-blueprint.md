---
title: "UI Prompt Blueprint: jockey-stuudio-xyz"
date: 2026-11-15
target: "[[overview|jockey-stuudio-xyz]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#a3a3a3` / `#000`)"
---

# UI Design System & Master Generation Blueprint: jockey-stuudio-xyz

> **Jockey by TwelveLabs: The Video Intelligence Agent** (https://jockey.stuudio.xyz/) — The TwelveLabs agent that organizes, searches, and assembles across your entire video library. Built on Pegasus and Marengo. Now in resea...

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/jockey-stuudio-xyz/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Jockey by TwelveLabs: The Video Intelligence Agent** (`https://jockey.stuudio.xyz/`). The TwelveLabs agent that organizes, searches, and assembles across your entire video library. Built on Pegasus and Marengo. Now in resea...
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#a3a3a3` / `#000`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#a3a3a3` (`var(--color-neutral-400)` in `:root`) paired with `#000` primary typography and `#000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Milling` for display copy (`The agent layer for video understand`) with `Milling Triplex` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: var(--spacing)`, padding `var(--spacing)`) with `cubic-bezier(.4,0,1,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/jockey-stuudio-xyz/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `40rem` extracted from `jockey-stuudio-xyz` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--spacing)` lateral canvas padding with `var(--spacing)` grid gap.
- **Border Radius Scale**: `.25rem`, `var(--radius-2xl)`, `var(--radius-3xl)`, `1.4rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--spacing)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--spacing)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#a3a3a3` | `var(--color-neutral-400)` in `:root` |
| **Primary Typography Ink** | `#737373` | `var(--color-neutral-500)` in `:root` |
| **Elevated Surface / Card Substrate** | `#404040` | `var(--color-neutral-700)` in `:root` |
| **Interactive Accent / Highlight** | `#000` | `var(--color-black)` in `:root` |
| **Secondary / Muted Copy** | `#fff` | `var(--color-white)` in `:root` |
| **Structural Hairline Border** | `#f4f3f3` | `var(--color-tag)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--rim-angle` | `0deg` | Design System Custom Token |
| `--font-sans` | `"Milling","Suisse Intl",ui-sans-serif,system-ui,sans-serif` | Typography / Scale Token |
| `--color-neutral-400` | `#a3a3a3` | Brand / Palette Token |
| `--color-neutral-500` | `#737373` | Brand / Palette Token |
| `--color-neutral-700` | `#404040` | Brand / Palette Token |
| `--color-neutral-900` | `oklch(20.5% 0 0)` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--text-sm` | `.875rem` | Typography Ink Token |
| `--text-sm--line-height` | `1.45` | Typography Ink Token |
| `--text-lg` | `1.125rem` | Typography Ink Token |
| `--text-lg--line-height` | `1.5` | Typography Ink Token |
| `--text-xl` | `1.5rem` | Typography Ink Token |
| `--text-xl--line-height` | `1.25` | Typography Ink Token |
| `--text-2xl` | `1.875rem` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Milling`.
- **Primary Body Stack**: `Milling Triplex`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--font-display: "Milling Triplex","Milling","Suisse Intl",sans-serif`, `--text-display: 3rem`, `--text-display--line-height: 1.17`.
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.875rem`, `--text-2xl--line-height: 1.15`, `--text-3xl: 3rem`.
- **Body Copy**: CSS variables `--text-body: 1rem`, `--text-body--line-height: 1.5`, `--text-body--letter-spacing: .01em`.
- **Metadata & Navigation Labels**: CSS variables `--text-sm: .875rem`, `--text-sm--line-height: 1.45`, `--default-mono-font-family: var(--font-mono)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `jockey-stuudio-xyz` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `jockey-stuudio-xyz` stylesheet.
- **Selector `border-color\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `jockey-stuudio-xyz` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<nav.flex>` and `<section.relative>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Jockey by TwelveLabs: The Video Intelligen │
│ ====================================================================== │
│ [ <nav.flex>               | Use Cases · Integration · Models · FAQ ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.relative>                                   |   │
│ | H1: The agent layer for video understanding                      |   │
│ | Substrate: #a3a3a3    | Ink: #000       | Accent: #000           |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.relative>        ) max-w: 40rem          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Know every ad you've ever ru |  | Automatic Ad Tagging         | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<nav.flex>] -> [<section.relative>] -> [<section.relative>] |       │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.relative>     ) | https://jockey.stuudio.xyz/        │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.flex> — `jockey-stuudio-xyz`)**:
   - Landmark `<nav class="flex flex-col">` hosting `Jockey by TwelveLabs: The Video Inte` navigation (`Use Cases · Integration · Models · FAQ · Get started`), DOM attributes (`data-precedence="next"`, `data-nav="dark"`, `data-engine="three.js r183"`, `data-nav="dark"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.relative> — `The agent layer for video understa`)**:
   - Landmark `<section class="relative w-full">` presenting display lead `The agent layer for video understanding` and copy excerpt *"Jockey by TwelveLabs"* over `#a3a3a3` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `Know every ad you've ever run.`)**:
   - Landmark `<section class="relative w-full">` rendering section `Know every ad you've ever run.` with copy *"Available in the Claude Connectors Directory"*, asset references (`c9ea9b6355867f69.css`, `webpack-3e3201efe76e74c7.js`, `uwt.js`, `1867067050739407`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.light> — `Automatic Ad Tagging`)**:
   - Landmark `<section class="light relative">` framing `Automatic Ad Tagging` and `Winning Hook Detection` (*"The same intelligence, pointed at your creative library."*) with `#404040` surface cards, `#000` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://jockey.stuudio.xyz/`)**:
   - Landmark `<footer class="relative flex">` anchoring `Jockey by TwelveLabs: The Video ` footer links (`Use Cases · Integration · Models · FAQ · Get started`), copy *"Automatic Ad Tagging"*, and `#f4f3f3` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: jockey-stuudio-xyz (Jockey by TwelveLabs: The Video Intelligence Agent)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `jockey-stuudio-xyz` (**Jockey by TwelveLabs: The Video Intelligence Agent** — `https://jockey.stuudio.xyz/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#a3a3a3` / `#000`).
- **Identity & Domain Context**: The TwelveLabs agent that organizes, searches, and assembles across your entire video library. Built on Pegasus and Marengo. Now in resea...
- **Primary Substrate**: `#a3a3a3` (`var(--color-neutral-400)` in `:root`), **Primary Ink**: `#000`, **Accent / Highlight**: `#000`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#a3a3a3` (`var(--color-neutral-400)` in `:root`) paired with `#000` primary typography and `#000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Milling` for display copy (`The agent layer for video understand`) with `Milling Triplex` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: var(--spacing)`, padding `var(--spacing)`) with `cubic-bezier(.4,0,1,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `jockey-stuudio-xyz` in your global stylesheet:

:root {
  /* Jockey by TwelveLabs: The Video Intelligence Agent (jockey-stuudio-xyz) — Ground-Truth Extracted CSS Variables */
  --rim-angle: 0deg; /* Design System Custom Token (jockey-stuudio-xyz) */
  --font-sans: "Milling","Suisse Intl",ui-sans-serif,system-ui,sans-serif; /* Typography / Scale Token (jockey-stuudio-xyz) */
  --color-neutral-400: #a3a3a3; /* Brand / Palette Token (jockey-stuudio-xyz) */
  --color-neutral-500: #737373; /* Brand / Palette Token (jockey-stuudio-xyz) */
  --color-neutral-700: #404040; /* Brand / Palette Token (jockey-stuudio-xyz) */
  --color-neutral-900: oklch(20.5% 0 0); /* Brand / Palette Token (jockey-stuudio-xyz) */
  --color-black: #000; /* Canvas / Surface Token (jockey-stuudio-xyz) */
  --color-white: #fff; /* Canvas / Surface Token (jockey-stuudio-xyz) */
  --spacing: .25rem; /* Layout / Spatial Grid Token (jockey-stuudio-xyz) */
  --text-sm: .875rem; /* Typography Ink Token (jockey-stuudio-xyz) */
  --text-sm--line-height: 1.45; /* Typography Ink Token (jockey-stuudio-xyz) */
  --text-lg: 1.125rem; /* Typography Ink Token (jockey-stuudio-xyz) */
  --text-lg--line-height: 1.5; /* Typography Ink Token (jockey-stuudio-xyz) */
  --text-xl: 1.5rem; /* Typography Ink Token (jockey-stuudio-xyz) */
  --text-xl--line-height: 1.25; /* Typography Ink Token (jockey-stuudio-xyz) */
  --text-2xl: 1.875rem; /* Typography Ink Token (jockey-stuudio-xyz) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#a3a3a3` — grounded in `var(--color-neutral-400)` in `:root`
- **Primary Typography Ink**: `#737373` — grounded in `var(--color-neutral-500)` in `:root`
- **Elevated Surface / Card Substrate**: `#404040` — grounded in `var(--color-neutral-700)` in `:root`
- **Interactive Accent / Highlight**: `#000` — grounded in `var(--color-black)` in `:root`
- **Secondary / Muted Copy**: `#fff` — grounded in `var(--color-white)` in `:root`
- **Structural Hairline Border**: `#f4f3f3` — grounded in `var(--color-tag)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `40rem` extracted from `jockey-stuudio-xyz` stylesheet
- **Padding & Gutters**: `var(--spacing)` lateral canvas padding with `var(--spacing)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--spacing)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--spacing)` horizontal padding
- **Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`
- **Corner Radii**: `.25rem`, `var(--radius-2xl)`, `var(--radius-3xl)`, `1.4rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Milling`
- **Body Font Stack**: `Milling Triplex`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: CSS variables `--font-display: "Milling Triplex","Milling","Suisse Intl",sans-serif`, `--text-display: 3rem`, `--text-display--line-height: 1.17`
- **H2 Section Rule**: CSS variables `--text-2xl: 1.875rem`, `--text-2xl--line-height: 1.15`, `--text-3xl: 3rem`
- **Body Copy Rule**: CSS variables `--text-body: 1rem`, `--text-body--line-height: 1.5`, `--text-body--letter-spacing: .01em`
- **Metadata & Index Rule**: CSS variables `--text-sm: .875rem`, `--text-sm--line-height: 1.45`, `--default-mono-font-family: var(--font-mono)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `jockey-stuudio-xyz` (`Jockey by TwelveLabs: The Video Intelligence Agent`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.flex> — `jockey-stuudio-xyz`)**:
   - DOM & Selectors: Landmark `<nav class="flex flex-col">` hosting `Jockey by TwelveLabs: The Video Inte` navigation (`Use Cases · Integration · Models · FAQ · Get started`), DOM attributes (`data-precedence="next"`, `data-nav="dark"`, `data-engine="three.js r183"`, `data-nav="dark"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.flex> — `jockey-stuudio-xyz`)` (`jockey-stuudio-xyz`) adapts across `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)` with `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `Use Cases · Integration · Models · FAQ · Get started`.
2. **Hero Stage & Focal Lead (<section.relative> — `The agent layer for video understa`)**:
   - DOM & Selectors: Landmark `<section class="relative w-full">` presenting display lead `The agent layer for video understanding` and copy excerpt *"Jockey by TwelveLabs"* over `#a3a3a3` canvas and `#000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#a3a3a3` background with `#000` headline `The agent layer for video understanding`.
3. **Primary Showcase & Content Grid (<section.relative> — `Know every ad you've ever run.`)**:
   - DOM & Selectors: Landmark `<section class="relative w-full">` rendering section `Know every ad you've ever run.` with copy *"Available in the Claude Connectors Directory"*, asset references (`c9ea9b6355867f69.css`, `webpack-3e3201efe76e74c7.js`, `uwt.js`, `1867067050739407`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.relative> — `Know every ad you've ever run.`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--spacing)`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--spacing)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.light> — `Automatic Ad Tagging`)**:
   - DOM & Selectors: Landmark `<section class="light relative">` framing `Automatic Ad Tagging` and `Winning Hook Detection` (*"The same intelligence, pointed at your creative library."*) with `#404040` surface cards, `#000` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.light> — `Automatic Ad Tagging`)` uses `.25rem`, `var(--radius-2xl)`, `var(--radius-3xl)`, `1.4rem` radii, `#000` highlights, and assets (c9ea9b6355867f69.css, webpack-3e3201efe76e74c7.js, uwt.js).
5. **Colophon & Global Directory Footer (<footer.relative> — `https://jockey.stuudio.xyz/`)**:
   - DOM & Selectors: Landmark `<footer class="relative flex">` anchoring `Jockey by TwelveLabs: The Video ` footer links (`Use Cases · Integration · Models · FAQ · Get started`), copy *"Automatic Ad Tagging"*, and `#f4f3f3` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.relative> — `https://jockey.stuudio.xyz/`)` aligns to `40rem` extracted from `jockey-stuudio-xyz` stylesheet with `var(--spacing)` lateral canvas padding with `var(--spacing)` grid gap and attributes (data-precedence="next", data-nav="dark", data-engine="three.js r183").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Jockey by TwelveLabs"*
- Copy Excerpt 2: *"Available in the Claude Connectors Directory"*
- Copy Excerpt 3: *"The same intelligence, pointed at your creative library."*
- Copy Excerpt 4: *"Automatic Ad Tagging"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`jockey-stuudio-xyz`)**:
- `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- `sup { vertical-align:baseline;font-size:75%;line-height:0;position:relative }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `jockey-stuudio-xyz` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `jockey-stuudio-xyz` stylesheet.
- **Selector `border-color\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `jockey-stuudio-xyz` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<nav.flex>` and `<section.relative>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `jockey-stuudio-xyz`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
