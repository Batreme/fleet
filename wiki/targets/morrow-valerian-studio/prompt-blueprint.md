---
title: "UI Prompt Blueprint: morrow-valerian-studio"
date: 2026-11-23
captured_at: 2026-11-23
target: "morrow-valerian-studio"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#c4c4c4` accent)"
---

# UI Design System & Master Generation Blueprint: morrow-valerian-studio

> **MORROW** (https://morrow.valerian.studio) — FALL26’ KNITWEAR PORCELAIN

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **MORROW** (`https://morrow.valerian.studio`). FALL26’ KNITWEAR PORCELAIN
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#c4c4c4` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#c4c4c4` accents.
  - **Grounded Typographic Hierarchy**: Pairs `editorialNew` for display copy (`Pace Base Layer`) with `ppNeueMontreal` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `96rem` container bounds (`gap: normal 10px`, padding `15px`) with `cubic-bezier(.22,1,.36,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `96rem` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `15px` lateral canvas padding with `normal 10px` grid gap.
- **Border Radius Scale**: `4px`, `.25rem`, `var(--radius-sm)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: normal 10px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `15px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:no-preference)`, `@media (max-width:400px)`, `@media (prefers-reduced-motion:reduce)`, `@media (min-width:40rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | `.text-black { color: black }` (`#000000`) |
| **Elevated Surface / Card Substrate** | `#f5f5f5` | `.cart-item-image { background: #f5f5f5 }` |
| **Interactive Accent / Highlight** | `#c4c4c4` | `.cart-quantity button:disabled { color: #c4c4c4 }` |
| **Secondary / Muted Copy** | `#737373` | `.cart-item-size { color: #737373 }` |
| **Structural Hairline Border** | `#e5e5e5` | `.cart-header { border-bottom: #e5e5e5 }` |
| **Variable Token (`--color-red-800`)** | `#9f0712` | `var(--color-red-800)` in `:root` |
| **Variable Token (`--color-rose-500`)** | `#ff2357` | `var(--color-rose-500)` in `:root` |
| **Variable Token (`--color-neutral-50`)** | `#fafafa` | `var(--color-neutral-50)` in `:root` |
| **Variable Token (`--color-neutral-300`)** | `#d4d4d4` | `var(--color-neutral-300)` in `:root` |
| **Variable Token (`--color-neutral-400`)** | `#a1a1a1` | `var(--color-neutral-400)` in `:root` |
| **Variable Token (`--color-neutral-600`)** | `#525252` | `var(--color-neutral-600)` in `:root` |
| **Variable Token (`--color-neutral-900`)** | `#171717` | `var(--color-neutral-900)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `var(--font-pp-neue-montreal), Arial, sans-serif` | Typography / Scale Token |
| `--color-red-800` | `#9f0712` | Brand / Palette Token |
| `--color-rose-500` | `#ff2357` | Brand / Palette Token |
| `--color-neutral-50` | `#fafafa` | Brand / Palette Token |
| `--color-neutral-100` | `#f5f5f5` | Brand / Palette Token |
| `--color-neutral-200` | `#e5e5e5` | Brand / Palette Token |
| `--color-neutral-300` | `#d4d4d4` | Brand / Palette Token |
| `--color-neutral-400` | `#a1a1a1` | Brand / Palette Token |
| `--color-neutral-500` | `#737373` | Brand / Palette Token |
| `--color-neutral-600` | `#525252` | Brand / Palette Token |
| `--color-neutral-900` | `#171717` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-xs` | `20rem` | Layout / Spatial Grid Token |
| `--container-3xl` | `48rem` | Layout / Spatial Grid Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `editorialNew`.
- **Primary Body Stack**: `ppNeueMontreal`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: CSS variables `--text-display: clamp(1.75rem, 3vw, 3rem)`, `--text-display--line-height: 1.2`.
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 24px`, `line-height: 32px`, `font-weight: 500`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`.
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-body: 14px`, `--text-body--line-height: calc(1.25 / .875)`.
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--default-mono-font-family: var(--font-mono)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.lenis.lenis-autoToggle`**: `transition: 1ms` extracted from `morrow-valerian-studio` stylesheet.
- **Selector `layer theme`**: `transition: .15s` extracted from `morrow-valerian-studio` stylesheet.
- **Selector `.transition-colors`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `morrow-valerian-studio` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,1,.36,1)`)**: Governs interactive state transitions across `<header.site-nav>` and `<section.grid-cols-12>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — MORROW                                     │
│ ====================================================================== │
│ [ <header.site-nav> (1440x68px)       | MORROW · Shop · All products ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.h-svh> (w=1440px)                             | │
│ | H1: Pace Base Layer                                                | │
│ | Substrate: #ffffff | Ink: #000000 | Accent: #c4c4c4                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.grid-cols-12>) max-w: 96rem                | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Everyday Long Sleeve         |  | Tempo Running Shorts         | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<article.group>) — Stride Windbreaker               | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.px-page>    ) | https://morrow.valerian.studio       │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: normal 1)   │
│ ====================================================================== │
│ [ HEADER BAR (<header.site-nav>       ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.h-svh>) — 390px Vertical Lead                 | │
│ | H1: Pace Base Layer                                                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.grid-cols-12>) — 1-Col Stack              | │
│ | [ Item 1: Everyday Long Sleeve                                   ] | │
│ | [ Item 2: Tempo Running Shorts                                   ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<article.group>) — 1-Col (Stride Windbreaker)        | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.px-page>    ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.site-nav> — `morrow-valerian-studio`)**:
   - Landmark `<header class="site-nav col-start-1">` (`1440x68px`) hosting `MORROW` navigation (`MORROW · Shop · All products · Clothes · Accessories`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.cart-dialog::backdrop { background:0 0 }`.
2. **Hero Stage & Focal Lead (<section.h-svh> — `Pace Base Layer`)**:
   - Landmark `<section class="h-svh grid-cols-12">` presenting display lead `Pace Base Layer` and copy excerpt *"KNITWEAR PORCELAIN"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.grid-cols-12> — `Everyday Long Sleeve`)**:
   - Landmark `<section class="grid-cols-12 gap-x-gutter">` rendering section `Everyday Long Sleeve` with copy *"Built for the changing rhythm of the season, Fall 2026 introduces"*, asset references (`3p45zkgyngvyk.css`, `19h1-_j7inwm4.css`, `376za7hcbsln-.css`, `2x1xg-ar74jvz.css`), and grid rule `.cart-scrim { pointer-events:none;background:00000047;position:absolute;inset:0 }`.
4. **Interactive Detail & Feature Matrix (<article.group> — `Tempo Running Shorts`)**:
   - Landmark `<article class="group font-sans">` framing `Tempo Running Shorts` and `Stride Windbreaker` (*"Explore the collection"*) with `#f5f5f5` surface cards, `#c4c4c4` accents, and `.cart-panel { background:fff;flex-direction:column;width:min(100%,480px);height:100%;m... }`.
5. **Colophon & Global Directory Footer (<footer.px-page> — `https://morrow.valerian.studio`)**:
   - Landmark `<footer class="px-page font-sans">` anchoring `MORROW` footer links (`MORROW · Shop · All products · Clothes · Accessories`), copy *"Stories of people, places and the details that shape the way"*, and `#e5e5e5` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: morrow-valerian-studio (MORROW)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `morrow-valerian-studio` (**MORROW** — `https://morrow.valerian.studio`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#c4c4c4` accent).
- **Identity & Domain Context**: FALL26’ KNITWEAR PORCELAIN
- **Primary Substrate**: `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#000000`, **Accent / Highlight**: `#c4c4c4`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#c4c4c4` accents.
  - **Grounded Typographic Hierarchy**: Pairs `editorialNew` for display copy (`Pace Base Layer`) with `ppNeueMontreal` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `96rem` container bounds (`gap: normal 10px`, padding `15px`) with `cubic-bezier(.22,1,.36,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `morrow-valerian-studio` in your global stylesheet:

:root {
  /* MORROW (morrow-valerian-studio) — Live-Grounded CSS Variables */
  --font-sans: var(--font-pp-neue-montreal), Arial, sans-serif; /* Typography / Scale Token (morrow-valerian-studio) */
  --color-red-800: #9f0712; /* Brand / Palette Token (morrow-valerian-studio) */
  --color-rose-500: #ff2357; /* Brand / Palette Token (morrow-valerian-studio) */
  --color-neutral-50: #fafafa; /* Brand / Palette Token (morrow-valerian-studio) */
  --color-neutral-100: #f5f5f5; /* Brand / Palette Token (morrow-valerian-studio) */
  --color-neutral-200: #e5e5e5; /* Brand / Palette Token (morrow-valerian-studio) */
  --color-neutral-300: #d4d4d4; /* Brand / Palette Token (morrow-valerian-studio) */
  --color-neutral-400: #a1a1a1; /* Brand / Palette Token (morrow-valerian-studio) */
  --color-neutral-500: #737373; /* Brand / Palette Token (morrow-valerian-studio) */
  --color-neutral-600: #525252; /* Brand / Palette Token (morrow-valerian-studio) */
  --color-neutral-900: #171717; /* Brand / Palette Token (morrow-valerian-studio) */
  --color-black: #000; /* Canvas / Surface Token (morrow-valerian-studio) */
  --color-white: #fff; /* Canvas / Surface Token (morrow-valerian-studio) */
  --spacing: .25rem; /* Layout / Spatial Grid Token (morrow-valerian-studio) */
  --container-xs: 20rem; /* Layout / Spatial Grid Token (morrow-valerian-studio) */
  --container-3xl: 48rem; /* Layout / Spatial Grid Token (morrow-valerian-studio) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#000000` — grounded in `.text-black { color: black }` (`#000000`)
- **Elevated Surface / Card Substrate**: `#f5f5f5` — grounded in `.cart-item-image { background: #f5f5f5 }`
- **Interactive Accent / Highlight**: `#c4c4c4` — grounded in `.cart-quantity button:disabled { color: #c4c4c4 }`
- **Secondary / Muted Copy**: `#737373` — grounded in `.cart-item-size { color: #737373 }`
- **Structural Hairline Border**: `#e5e5e5` — grounded in `.cart-header { border-bottom: #e5e5e5 }`
- **Variable Token (`--color-red-800`)**: `#9f0712` — grounded in `var(--color-red-800)` in `:root`
- **Variable Token (`--color-rose-500`)**: `#ff2357` — grounded in `var(--color-rose-500)` in `:root`
- **Variable Token (`--color-neutral-50`)**: `#fafafa` — grounded in `var(--color-neutral-50)` in `:root`
- **Variable Token (`--color-neutral-300`)**: `#d4d4d4` — grounded in `var(--color-neutral-300)` in `:root`
- **Variable Token (`--color-neutral-400`)**: `#a1a1a1` — grounded in `var(--color-neutral-400)` in `:root`
- **Variable Token (`--color-neutral-600`)**: `#525252` — grounded in `var(--color-neutral-600)` in `:root`
- **Variable Token (`--color-neutral-900`)**: `#171717` — grounded in `var(--color-neutral-900)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `96rem` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `15px` lateral canvas padding with `normal 10px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: normal 10px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `15px` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:no-preference)`, `@media (max-width:400px)`, `@media (prefers-reduced-motion:reduce)`, `@media (min-width:40rem)`
- **Corner Radii**: `4px`, `.25rem`, `var(--radius-sm)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `editorialNew`
- **Body Font Stack**: `ppNeueMontreal`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: CSS variables `--text-display: clamp(1.75rem, 3vw, 3rem)`, `--text-display--line-height: 1.2`
- **H2 Section Rule**: live computed `h2` (`font-size: 24px`, `line-height: 32px`, `font-weight: 500`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-body: 14px`, `--text-body--line-height: calc(1.25 / .875)`
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--default-mono-font-family: var(--font-mono)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `morrow-valerian-studio` (`MORROW`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.site-nav> — `morrow-valerian-studio`)**:
   - DOM & Selectors: Landmark `<header class="site-nav col-start-1">` (`1440x68px`) hosting `MORROW` navigation (`MORROW · Shop · All products · Clothes · Accessories`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.cart-dialog::backdrop { background:0 0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.site-nav> — `morrow-valerian-studio`)` (`morrow-valerian-studio`) adapts across `@media (prefers-reduced-motion:no-preference)`, `@media (max-width:400px)`, `@media (prefers-reduced-motion:reduce)`, `@media (min-width:40rem)` with `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)` transitions and links `MORROW · Shop · All products · Clothes · Accessories`.
2. **Hero Stage & Focal Lead (<section.h-svh> — `Pace Base Layer`)**:
   - DOM & Selectors: Landmark `<section class="h-svh grid-cols-12">` presenting display lead `Pace Base Layer` and copy excerpt *"KNITWEAR PORCELAIN"* over `#ffffff` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#ffffff` background with `#000000` headline `Pace Base Layer`.
3. **Primary Showcase & Content Grid (<section.grid-cols-12> — `Everyday Long Sleeve`)**:
   - DOM & Selectors: Landmark `<section class="grid-cols-12 gap-x-gutter">` rendering section `Everyday Long Sleeve` with copy *"Built for the changing rhythm of the season, Fall 2026 introduces"*, asset references (`3p45zkgyngvyk.css`, `19h1-_j7inwm4.css`, `376za7hcbsln-.css`, `2x1xg-ar74jvz.css`), and grid rule `.cart-scrim { pointer-events:none;background:00000047;position:absolute;inset:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.grid-cols-12> — `Everyday Long Sleeve`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: normal 10px`) on desktop and Single-column vertical stack at `390px` viewport width with `15px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.group> — `Tempo Running Shorts`)**:
   - DOM & Selectors: Landmark `<article class="group font-sans">` framing `Tempo Running Shorts` and `Stride Windbreaker` (*"Explore the collection"*) with `#f5f5f5` surface cards, `#c4c4c4` accents, and `.cart-panel { background:fff;flex-direction:column;width:min(100%,480px);height:100%;m... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.group> — `Tempo Running Shorts`)` uses `4px`, `.25rem`, `var(--radius-sm)` radii, `#c4c4c4` highlights, and assets (3p45zkgyngvyk.css, 19h1-_j7inwm4.css, 376za7hcbsln-.css).
5. **Colophon & Global Directory Footer (<footer.px-page> — `https://morrow.valerian.studio`)**:
   - DOM & Selectors: Landmark `<footer class="px-page font-sans">` anchoring `MORROW` footer links (`MORROW · Shop · All products · Clothes · Accessories`), copy *"Stories of people, places and the details that shape the way"*, and `#e5e5e5` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.px-page> — `https://morrow.valerian.studio`)` aligns to `96rem` (non-`@media` desktop container stylesheet rule) with `15px` lateral canvas padding with `normal 10px` grid gap and attributes (data-precedence="next", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"KNITWEAR PORCELAIN"*
- Copy Excerpt 2: *"Built for the changing rhythm of the season, Fall 2026 introduces a considered bal..."*
- Copy Excerpt 3: *"Explore the collection"*
- Copy Excerpt 4: *"Stories of people, places and the details that shape the way we move. From the fir..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`
- **Extracted Stylesheet Rules (`morrow-valerian-studio`)**:
- `.cart-dialog::backdrop { background:0 0 }`
- `.cart-scrim { pointer-events:none;background:00000047;position:absolute;inset:0 }`
- `.cart-panel { background:fff;flex-direction:column;width:min(100%,480px);height:100%;m... }`
- `.cart-count { vertical-align:middle;margin-left:4px;font-size:12px }`
- `.cart-close { cursor:pointer;place-items:center;width:40px;height:40px;display:grid }`
- **Per-Selector Transition Rules**:
- **Selector `.lenis.lenis-autoToggle`**: `transition: 1ms` extracted from `morrow-valerian-studio` stylesheet.
- **Selector `layer theme`**: `transition: .15s` extracted from `morrow-valerian-studio` stylesheet.
- **Selector `.transition-colors`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `morrow-valerian-studio` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,1,.36,1)`)**: Governs interactive state transitions across `<header.site-nav>` and `<section.grid-cols-12>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `morrow-valerian-studio`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
