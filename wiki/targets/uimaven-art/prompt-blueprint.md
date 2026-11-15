---
title: "UI Prompt Blueprint: uimaven-art"
date: 2026-11-15
target: "[[overview|uimaven-art]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#fb3748` / `#ffdb43`)"
---

# UI Design System & Master Generation Blueprint: uimaven-art

> **uimaven.art** (https://uimaven.art) — UI/UX design portfolio of Leila Abbassova.

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/uimaven-art/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **uimaven.art** (`https://uimaven.art`). UI/UX design portfolio of Leila Abbassova.
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#fb3748` / `#ffdb43`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fb3748` (`var(--color-red-100)` in `:root`) paired with `#ffdb43` primary typography and `#ffdb43` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Jost` for display copy (`uimaven.art`) with `Jost Fallback` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: 2.63px`, padding `2px`) with `cubic-bezier(.4,0,1,1)` easing and HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/uimaven-art/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `40rem` extracted from `uimaven-art` stylesheet.
- **Canvas Lateral Padding & Spacing**: `2px` lateral canvas padding with `2.63px` grid gap.
- **Border Radius Scale**: `.25rem`, `1px`, `2px`, `3.5px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: 2.63px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `2px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fb3748` | `var(--color-red-100)` in `:root` |
| **Primary Typography Ink** | `#fb2c36` | `var(--color-red-500)` in `:root` |
| **Elevated Surface / Card Substrate** | `#9f0712` | `var(--color-red-800)` in `:root` |
| **Interactive Accent / Highlight** | `#ffdb43` | `var(--color-yellow-100)` in `:root` |
| **Secondary / Muted Copy** | `#dfb400` | `var(--color-yellow-200)` in `:root` |
| **Structural Hairline Border** | `#edb200` | `var(--color-yellow-500)` in `:root` |
| **Variable Token (`--color-green-200`)** | `#1fc16b` | `var(--color-green-200)` in `:root` |
| **Variable Token (`--color-neutral-100`)** | `#fff` | `var(--color-neutral-100)` in `:root` |
| **Variable Token (`--color-neutral-200`)** | `#e8e8e8` | `var(--color-neutral-200)` in `:root` |
| **Variable Token (`--color-neutral-300`)** | `#d2d2d2` | `var(--color-neutral-300)` in `:root` |
| **Variable Token (`--color-black`)** | `#000` | `var(--color-black)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-jost` | `"Jost","Jost Fallback"` | Typography / Scale Token |
| `--type-weight` | `initial` | Typography / Scale Token |
| `--color-red-100` | `#fb3748` | Brand / Palette Token |
| `--color-red-500` | `#fb2c36` | Brand / Palette Token |
| `--color-red-800` | `#9f0712` | Brand / Palette Token |
| `--color-yellow-100` | `#ffdb43` | Brand / Palette Token |
| `--color-yellow-200` | `#dfb400` | Brand / Palette Token |
| `--color-yellow-500` | `#edb200` | Brand / Palette Token |
| `--color-green-200` | `#1fc16b` | Brand / Palette Token |
| `--color-neutral-100` | `#fff` | Brand / Palette Token |
| `--color-neutral-200` | `#e8e8e8` | Brand / Palette Token |
| `--color-neutral-300` | `#d2d2d2` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Jost`.
- **Primary Body Stack**: `Jost Fallback`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--text-display: 64px`, `--text-display--line-height: .95`, `--text-display-phone: 40px`.
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--text-heading)`, `var(--text-heading-phone)`).
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`, `--text-body: 16px`.
- **Metadata & Navigation Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1/.75)`, `--text-sm: .875rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `uimaven-art` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `uimaven-art` stylesheet.
- **Selector `translate\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `uimaven-art` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.relative>` and `<main.mobile-stripes>`.
- **Runtime Interaction Engine**: Integrates HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — uimaven.art                                │
│ ====================================================================== │
│ [ <header.relative>        | Overview · Index · Archive · About · C ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <main.mobile-stripes>                                |   │
│ | H1: uimaven.art                                                  |   │
│ | Substrate: #fb3748    | Ink: #ffdb43    | Accent: #ffdb43        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<main.mobile-stripes>     ) max-w: 40rem          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Featured Work & Interactive  |  | Technical Architecture & Nar | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 2.63px) | │
│ | [<header.relative>] -> [<main.mobile-strip] -> [<main.mobile-strip]  │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.bg-primary-300) | https://uimaven.art                │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.relative> — `uimaven-art`)**:
   - Landmark `<header class="relative shrink-0">` hosting `uimaven.art` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-home`), and stylesheet rule `jost_bd43172b-module__QzW_JW__cla... { font-family:Jost,Jost Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<main.mobile-stripes> — `uimaven.art`)**:
   - Landmark `<main class="mobile-stripes bg-primary-300">` presenting display lead `uimaven.art` and copy excerpt *"UI/UX design portfolio of Leila Abbassova."* over `#fb3748` canvas and `#ffdb43` ink.
3. **Primary Showcase & Content Grid (<main.mobile-stripes> — `Featured Work & Interactive Showca`)**:
   - Landmark `<main class="mobile-stripes bg-primary-300">` rendering section `Featured Work & Interactive Showcase` with copy *"uimaven.art"*, asset references (`81cef6a21128489e-s.p.6cf41120.woff2`, `d7f27077a988d3d1.css`, `e48a17b7f69aeb46.js`, `2677990b2b1206f6.js`), and grid rule `.jost_bd43172b-module__QzW_JW__va... { --font-jost:"Jost","Jost Fallback" }`.
4. **Interactive Detail & Feature Matrix (<main.mobile-stripes> — `Technical Architecture & Narrative`)**:
   - Landmark `<main class="mobile-stripes bg-primary-300">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Work & Interactive Showcase"*) with `#9f0712` surface cards, `#ffdb43` accents, and `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.bg-primary-300> — `https://uimaven.art`)**:
   - Landmark `<footer class="bg-primary-300">` anchoring `uimaven.art` footer links (`Overview · Index · Archive · About · Contact`), copy *"Technical Architecture & Narrative"*, and `#edb200` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: uimaven-art (uimaven.art)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `uimaven-art` (**uimaven.art** — `https://uimaven.art`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#fb3748` / `#ffdb43`).
- **Identity & Domain Context**: UI/UX design portfolio of Leila Abbassova.
- **Primary Substrate**: `#fb3748` (`var(--color-red-100)` in `:root`), **Primary Ink**: `#ffdb43`, **Accent / Highlight**: `#ffdb43`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fb3748` (`var(--color-red-100)` in `:root`) paired with `#ffdb43` primary typography and `#ffdb43` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Jost` for display copy (`uimaven.art`) with `Jost Fallback` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: 2.63px`, padding `2px`) with `cubic-bezier(.4,0,1,1)` easing and HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `uimaven-art` in your global stylesheet:

:root {
  /* uimaven.art (uimaven-art) — Ground-Truth Extracted CSS Variables */
  --font-jost: "Jost","Jost Fallback"; /* Typography / Scale Token (uimaven-art) */
  --type-weight: initial; /* Typography / Scale Token (uimaven-art) */
  --color-red-100: #fb3748; /* Brand / Palette Token (uimaven-art) */
  --color-red-500: #fb2c36; /* Brand / Palette Token (uimaven-art) */
  --color-red-800: #9f0712; /* Brand / Palette Token (uimaven-art) */
  --color-yellow-100: #ffdb43; /* Brand / Palette Token (uimaven-art) */
  --color-yellow-200: #dfb400; /* Brand / Palette Token (uimaven-art) */
  --color-yellow-500: #edb200; /* Brand / Palette Token (uimaven-art) */
  --color-green-200: #1fc16b; /* Brand / Palette Token (uimaven-art) */
  --color-neutral-100: #fff; /* Brand / Palette Token (uimaven-art) */
  --color-neutral-200: #e8e8e8; /* Brand / Palette Token (uimaven-art) */
  --color-neutral-300: #d2d2d2; /* Brand / Palette Token (uimaven-art) */
  --color-black: #000; /* Canvas / Surface Token (uimaven-art) */
  --color-white: #fff; /* Canvas / Surface Token (uimaven-art) */
  --spacing: .25rem; /* Layout / Spatial Grid Token (uimaven-art) */
  --text-xs: .75rem; /* Typography Ink Token (uimaven-art) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fb3748` — grounded in `var(--color-red-100)` in `:root`
- **Primary Typography Ink**: `#fb2c36` — grounded in `var(--color-red-500)` in `:root`
- **Elevated Surface / Card Substrate**: `#9f0712` — grounded in `var(--color-red-800)` in `:root`
- **Interactive Accent / Highlight**: `#ffdb43` — grounded in `var(--color-yellow-100)` in `:root`
- **Secondary / Muted Copy**: `#dfb400` — grounded in `var(--color-yellow-200)` in `:root`
- **Structural Hairline Border**: `#edb200` — grounded in `var(--color-yellow-500)` in `:root`
- **Variable Token (`--color-green-200`)**: `#1fc16b` — grounded in `var(--color-green-200)` in `:root`
- **Variable Token (`--color-neutral-100`)**: `#fff` — grounded in `var(--color-neutral-100)` in `:root`
- **Variable Token (`--color-neutral-200`)**: `#e8e8e8` — grounded in `var(--color-neutral-200)` in `:root`
- **Variable Token (`--color-neutral-300`)**: `#d2d2d2` — grounded in `var(--color-neutral-300)` in `:root`
- **Variable Token (`--color-black`)**: `#000` — grounded in `var(--color-black)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `40rem` extracted from `uimaven-art` stylesheet
- **Padding & Gutters**: `2px` lateral canvas padding with `2.63px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: 2.63px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `2px` horizontal padding
- **Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`
- **Corner Radii**: `.25rem`, `1px`, `2px`, `3.5px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Jost`
- **Body Font Stack**: `Jost Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: CSS variables `--text-display: 64px`, `--text-display--line-height: .95`, `--text-display-phone: 40px`
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--text-heading)`, `var(--text-heading-phone)`)
- **Body Copy Rule**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`, `--text-body: 16px`
- **Metadata & Index Rule**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1/.75)`, `--text-sm: .875rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `uimaven-art` (`uimaven.art`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.relative> — `uimaven-art`)**:
   - DOM & Selectors: Landmark `<header class="relative shrink-0">` hosting `uimaven.art` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-home`), and stylesheet rule `jost_bd43172b-module__QzW_JW__cla... { font-family:Jost,Jost Fallback;font-style:normal }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.relative> — `uimaven-art`)` (`uimaven-art`) adapts across `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)` with `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<main.mobile-stripes> — `uimaven.art`)**:
   - DOM & Selectors: Landmark `<main class="mobile-stripes bg-primary-300">` presenting display lead `uimaven.art` and copy excerpt *"UI/UX design portfolio of Leila Abbassova."* over `#fb3748` canvas and `#ffdb43` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#fb3748` background with `#ffdb43` headline `uimaven.art`.
3. **Primary Showcase & Content Grid (<main.mobile-stripes> — `Featured Work & Interactive Showca`)**:
   - DOM & Selectors: Landmark `<main class="mobile-stripes bg-primary-300">` rendering section `Featured Work & Interactive Showcase` with copy *"uimaven.art"*, asset references (`81cef6a21128489e-s.p.6cf41120.woff2`, `d7f27077a988d3d1.css`, `e48a17b7f69aeb46.js`, `2677990b2b1206f6.js`), and grid rule `.jost_bd43172b-module__QzW_JW__va... { --font-jost:"Jost","Jost Fallback" }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<main.mobile-stripes> — `Featured Work & Interactive Showca`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: 2.63px`) on desktop and Single-column vertical stack at `390px` viewport width with `2px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<main.mobile-stripes> — `Technical Architecture & Narrative`)**:
   - DOM & Selectors: Landmark `<main class="mobile-stripes bg-primary-300">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Work & Interactive Showcase"*) with `#9f0712` surface cards, `#ffdb43` accents, and `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<main.mobile-stripes> — `Technical Architecture & Narrative`)` uses `.25rem`, `1px`, `2px`, `3.5px` radii, `#ffdb43` highlights, and assets (81cef6a21128489e-s.p.6cf41120.woff2, d7f27077a988d3d1.css, e48a17b7f69aeb46.js).
5. **Colophon & Global Directory Footer (<footer.bg-primary-300> — `https://uimaven.art`)**:
   - DOM & Selectors: Landmark `<footer class="bg-primary-300">` anchoring `uimaven.art` footer links (`Overview · Index · Archive · About · Contact`), copy *"Technical Architecture & Narrative"*, and `#edb200` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.bg-primary-300> — `https://uimaven.art`)` aligns to `40rem` extracted from `uimaven-art` stylesheet with `2px` lateral canvas padding with `2.63px` grid gap and attributes (data-precedence="next", data-home).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Lead Copy: *"UI/UX design portfolio of Leila Abbassova."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`uimaven-art`)**:
- `jost_bd43172b-module__QzW_JW__cla... { font-family:Jost,Jost Fallback;font-style:normal }`
- `.jost_bd43172b-module__QzW_JW__va... { --font-jost:"Jost","Jost Fallback" }`
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `uimaven-art` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `uimaven-art` stylesheet.
- **Selector `translate\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `uimaven-art` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.relative>` and `<main.mobile-stripes>`.
- **Runtime Interaction Engine**: Integrates HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `uimaven-art`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
