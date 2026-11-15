---
title: "UI Prompt Blueprint: studyhall-design"
date: 2026-11-15
target: "[[overview|studyhall-design]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#ededed`)"
---

# UI Design System & Master Generation Blueprint: studyhall-design

> **Home · Study Hall ✶ Built to move you.** (https://studyhall.design/) — A creative agency based in Oakland and partnering globally. We craft brand, motion, and interactive to help businesses resonate now and r...

![Desktop Viewport Capture (1440x5085)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Home · Study Hall ✶ Built to move you.** (`https://studyhall.design/`). A creative agency based in Oakland and partnering globally. We craft brand, motion, and interactive to help businesses resonate now and r...
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#ededed`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--color-black)` in `:root`) paired with `#fff` primary typography and `#ededed` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Neue Montreal` for display copy (`We're in the business of making thin`) with `Kommuna` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `48.0625rem` container bounds (`gap: var(--project-image-gap)`, padding `var(--spacing-gx)`) with `cubic-bezier(0,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×5085px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `48.0625rem` extracted from `studyhall-design` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--spacing-gx)` lateral canvas padding with `var(--project-image-gap)` grid gap.
- **Border Radius Scale**: `.25rem`, `3px`, `4px`, `5rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 48.0625rem`, `gap: var(--project-image-gap)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--spacing-gx)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (width>=48.0625rem)`, `@media (width>=64rem)`, `@media (width>=80rem)`, `@media (width>=96rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fdffb6` | `var(--color-yellow)` in `:root` |
| **Interactive Accent / Highlight** | `#ededed` | `var(--color-gray)` in `:root` |
| **Secondary / Muted Copy** | `#cdcdcd` | `var(--color-form-bg)` in `:root` |
| **Structural Hairline Border** | `#b7b7b7` | `var(--color-gray-hover)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `"Neue Montreal", ui-sans-serif, system-ui, sans-serif` | Typography / Scale Token |
| `--font-serif` | `"PS Times", ui-serif, Georgia, "Times New Roman", serif` | Typography / Scale Token |
| `--color-red-500` | `oklch(63.7% .237 25.331)` | Brand / Palette Token |
| `--color-red-700` | `oklch(50.5% .213 27.518)` | Brand / Palette Token |
| `--color-blue-500` | `oklch(62.3% .214 259.815)` | Brand / Palette Token |
| `--color-gray-200` | `oklch(92.8% .006 264.531)` | Brand / Palette Token |
| `--color-gray-800` | `oklch(27.8% .033 256.848)` | Brand / Palette Token |
| `--color-neutral-800` | `oklch(26.9% 0 none)` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `calc(1 / var(--type-root-max-value) * 1rem)` | Layout / Spatial Grid Token |
| `--font-weight-medium` | `500` | Typography / Scale Token |
| `--font-weight-semibold` | `600` | Typography / Scale Token |
| `--tracking-tighter` | `-.05em` | Typography / Scale Token |
| `--leading-normal` | `1.5` | Typography / Scale Token |
| `--radius-sm` | `.25rem` | Elevation / Border Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Neue Montreal`.
- **Primary Body Stack**: `Kommuna`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--text-caption-serif-size)`, `.7em`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--text-caption-serif-size)`, `.7em`).
- **Body Copy**: CSS variables `--type-body-lg-mobile: 20`, `--type-body-lg-tablet: 20`, `--type-body-lg-desktop: 24`.
- **Metadata & Navigation Labels**: CSS variables `--default-mono-font-family: var(--font-mono)`, `--type-small-mobile: 16`, `--type-small-tablet: 16`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.45,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `studyhall-design` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `studyhall-design` stylesheet.
- **Selector `.transition-colors`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `studyhall-design` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<nav.flex>` and `<section.py-gy>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Home · Study Hall ✶ Built to move you.     │
│ ====================================================================== │
│ [ <nav.flex>               | About · Work with us                   ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.pb-gy>                                      |   │
│ | H1: We're in the business of making things move. Bran...         |   │
│ | Substrate: #000       | Ink: #fff       | Accent: #ededed        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.py-gy>           ) max-w: 48.0625rem     |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | San Francisco Running Compan |  | Recent Work                  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<nav.flex>] -> [<section.pb-gy>] -> [<section.py-gy>] |             │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.mb-18>        ) | https://studyhall.design/          │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.flex> — `studyhall-design`)**:
   - Landmark `<nav class="flex flex-col">` hosting `Home · Study Hall ✶ Built to move yo` navigation (`About · Work with us`), DOM attributes (`data-module="nav-footer-hide"`, `data-module="nav-drawer-hover"`, `data-module="nav-drawer"`, `data-media-hover-trigger`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.pb-gy> — `We're in the business of making th`)**:
   - Landmark `<section class="pb-gy">` presenting display lead `We're in the business of making things move. Bran...` and copy excerpt *"W o r k w i t h u s Work with us"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.py-gy> — `San Francisco Running Company Bran`)**:
   - Landmark `<section class="py-gy px-gx">` rendering section `San Francisco Running Company Brand Identity` with copy *"W o r k w i t h u s"*, asset references (`594ac8afc003a31c157eba4bb9a25ab65...`, `cdn.sanity.io`, `stream.mux.com`, `7198ba5e4c2149645a79f387b2a12f5ce...`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.py-gy> — `Recent Work`)**:
   - Landmark `<section class="py-gy flex">` framing `Recent Work` and `Awards & Publications` (*"San Francisco Running Company Brand Identity Motion Brand Identit"*) with `#fdffb6` surface cards, `#ededed` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.mb-18> — `https://studyhall.design/`)**:
   - Landmark `<footer class="mb-18 pt-24">` anchoring `Home · Study Hall ✶ Built to mov` footer links (`About · Work with us`), copy *"San Francisco Running Company"*, and `#b7b7b7` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: studyhall-design (Home · Study Hall ✶ Built to move you.)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `studyhall-design` (**Home · Study Hall ✶ Built to move you.** — `https://studyhall.design/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#ededed`).
- **Identity & Domain Context**: A creative agency based in Oakland and partnering globally. We craft brand, motion, and interactive to help businesses resonate now and r...
- **Primary Substrate**: `#000` (`var(--color-black)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#ededed`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--color-black)` in `:root`) paired with `#fff` primary typography and `#ededed` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Neue Montreal` for display copy (`We're in the business of making thin`) with `Kommuna` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `48.0625rem` container bounds (`gap: var(--project-image-gap)`, padding `var(--spacing-gx)`) with `cubic-bezier(0,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `studyhall-design` in your global stylesheet:

:root {
  /* Home · Study Hall ✶ Built to move you. (studyhall-design) — Ground-Truth Extracted CSS Variables */
  --font-sans: "Neue Montreal", ui-sans-serif, system-ui, sans-serif; /* Typography / Scale Token (studyhall-design) */
  --font-serif: "PS Times", ui-serif, Georgia, "Times New Roman", serif; /* Typography / Scale Token (studyhall-design) */
  --color-red-500: oklch(63.7% .237 25.331); /* Brand / Palette Token (studyhall-design) */
  --color-red-700: oklch(50.5% .213 27.518); /* Brand / Palette Token (studyhall-design) */
  --color-blue-500: oklch(62.3% .214 259.815); /* Brand / Palette Token (studyhall-design) */
  --color-gray-200: oklch(92.8% .006 264.531); /* Brand / Palette Token (studyhall-design) */
  --color-gray-800: oklch(27.8% .033 256.848); /* Brand / Palette Token (studyhall-design) */
  --color-neutral-800: oklch(26.9% 0 none); /* Brand / Palette Token (studyhall-design) */
  --color-black: #000; /* Canvas / Surface Token (studyhall-design) */
  --color-white: #fff; /* Canvas / Surface Token (studyhall-design) */
  --spacing: calc(1 / var(--type-root-max-value) * 1rem); /* Layout / Spatial Grid Token (studyhall-design) */
  --font-weight-medium: 500; /* Typography / Scale Token (studyhall-design) */
  --font-weight-semibold: 600; /* Typography / Scale Token (studyhall-design) */
  --tracking-tighter: -.05em; /* Typography / Scale Token (studyhall-design) */
  --leading-normal: 1.5; /* Typography / Scale Token (studyhall-design) */
  --radius-sm: .25rem; /* Elevation / Border Token (studyhall-design) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000` — grounded in `var(--color-black)` in `:root`
- **Primary Typography Ink**: `#fff` — grounded in `var(--color-white)` in `:root`
- **Elevated Surface / Card Substrate**: `#fdffb6` — grounded in `var(--color-yellow)` in `:root`
- **Interactive Accent / Highlight**: `#ededed` — grounded in `var(--color-gray)` in `:root`
- **Secondary / Muted Copy**: `#cdcdcd` — grounded in `var(--color-form-bg)` in `:root`
- **Structural Hairline Border**: `#b7b7b7` — grounded in `var(--color-gray-hover)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×5085px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `48.0625rem` extracted from `studyhall-design` stylesheet
- **Padding & Gutters**: `var(--spacing-gx)` lateral canvas padding with `var(--project-image-gap)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 48.0625rem`, `gap: var(--project-image-gap)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--spacing-gx)` horizontal padding
- **Media Queries**: `@media (width>=48.0625rem)`, `@media (width>=64rem)`, `@media (width>=80rem)`, `@media (width>=96rem)`
- **Corner Radii**: `.25rem`, `3px`, `4px`, `5rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Neue Montreal`
- **Body Font Stack**: `Kommuna`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--text-caption-serif-size)`, `.7em`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--text-caption-serif-size)`, `.7em`)
- **Body Copy Rule**: CSS variables `--type-body-lg-mobile: 20`, `--type-body-lg-tablet: 20`, `--type-body-lg-desktop: 24`
- **Metadata & Index Rule**: CSS variables `--default-mono-font-family: var(--font-mono)`, `--type-small-mobile: 16`, `--type-small-tablet: 16`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `studyhall-design` (`Home · Study Hall ✶ Built to move you.`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.flex> — `studyhall-design`)**:
   - DOM & Selectors: Landmark `<nav class="flex flex-col">` hosting `Home · Study Hall ✶ Built to move yo` navigation (`About · Work with us`), DOM attributes (`data-module="nav-footer-hide"`, `data-module="nav-drawer-hover"`, `data-module="nav-drawer"`, `data-media-hover-trigger`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.flex> — `studyhall-design`)` (`studyhall-design`) adapts across `@media (width>=48.0625rem)`, `@media (width>=64rem)`, `@media (width>=80rem)`, `@media (width>=96rem)` with `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.45,0,.2,1)` transitions and links `About · Work with us`.
2. **Hero Stage & Focal Lead (<section.pb-gy> — `We're in the business of making th`)**:
   - DOM & Selectors: Landmark `<section class="pb-gy">` presenting display lead `We're in the business of making things move. Bran...` and copy excerpt *"W o r k w i t h u s Work with us"* over `#000` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×5085px` desktop / `390×2400px` mobile) sets `#000` background with `#fff` headline `We're in the business of making things move. Bran...`.
3. **Primary Showcase & Content Grid (<section.py-gy> — `San Francisco Running Company Bran`)**:
   - DOM & Selectors: Landmark `<section class="py-gy px-gx">` rendering section `San Francisco Running Company Brand Identity` with copy *"W o r k w i t h u s"*, asset references (`594ac8afc003a31c157eba4bb9a25ab65...`, `cdn.sanity.io`, `stream.mux.com`, `7198ba5e4c2149645a79f387b2a12f5ce...`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.py-gy> — `San Francisco Running Company Bran`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 48.0625rem`, `gap: var(--project-image-gap)`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--spacing-gx)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.py-gy> — `Recent Work`)**:
   - DOM & Selectors: Landmark `<section class="py-gy flex">` framing `Recent Work` and `Awards & Publications` (*"San Francisco Running Company Brand Identity Motion Brand Identit"*) with `#fdffb6` surface cards, `#ededed` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.py-gy> — `Recent Work`)` uses `.25rem`, `3px`, `4px`, `5rem` radii, `#ededed` highlights, and assets (594ac8afc003a31c157eba4bb9a25ab65..., cdn.sanity.io, stream.mux.com).
5. **Colophon & Global Directory Footer (<footer.mb-18> — `https://studyhall.design/`)**:
   - DOM & Selectors: Landmark `<footer class="mb-18 pt-24">` anchoring `Home · Study Hall ✶ Built to mov` footer links (`About · Work with us`), copy *"San Francisco Running Company"*, and `#b7b7b7` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.mb-18> — `https://studyhall.design/`)` aligns to `48.0625rem` extracted from `studyhall-design` stylesheet with `var(--spacing-gx)` lateral canvas padding with `var(--project-image-gap)` grid gap and attributes (data-module="nav-footer-hide", data-module="nav-drawer-hover", data-module="nav-drawer").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"W o r k w i t h u s Work with us"*
- Copy Excerpt 2: *"W o r k w i t h u s"*
- Copy Excerpt 3: *"San Francisco Running Company Brand Identity Motion Brand Identity Mt. Tamalpais i..."*
- Copy Excerpt 4: *"San Francisco Running Company"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.45,0,.2,1)`
- **Extracted Stylesheet Rules (`studyhall-design`)**:
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- `sup { vertical-align:baseline;font-size:75%;line-height:0;position:relative }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `studyhall-design` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `studyhall-design` stylesheet.
- **Selector `.transition-colors`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `studyhall-design` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<nav.flex>` and `<section.py-gy>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `studyhall-design`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
