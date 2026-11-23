---
title: "UI Prompt Blueprint: sincro-es_en-us"
date: 2026-11-23
captured_at: 2026-11-23
target: "sincro-es_en-us"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#081423` ink, `#0040ff` accent)"
---

# UI Design System & Master Generation Blueprint: sincro-es_en-us

> **Us - Sincro** (https://sincro.es/en/us/) — Navigating complexity together

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Us - Sincro** (`https://sincro.es/en/us/`). Navigating complexity together
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#081423` ink, `#0040ff` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `browser-default` `background-color` (`computed_styles.json`)) paired with `#081423` primary typography and `#0040ff` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Schibsted Grotesk` for display copy (`20 years of being who we say we are`) with `Schibsted Grotesk` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `96rem` container bounds (`gap: 29.97px`, padding `var(--spacing-L)`) with `cubic-bezier(.4,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), Swiper Touch Carousel Engine.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `96rem` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `var(--spacing-L)` lateral canvas padding with `29.97px` grid gap.
- **Border Radius Scale**: `3.996px`, `.25rem`, `2147483647px`, `var(--radius-sm)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: 29.97px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--spacing-L)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (width>=40rem)`, `@media (width>=64rem)`, `@media (width>=80rem)`, `@media (width>=96rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `browser-default` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#081423` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#081423` | `:placeholder-shown { background-color: #081423 }` |
| **Interactive Accent / Highlight** | `#0040ff` | `var(--color-vividBlueHover)` in `:root` |
| **Secondary / Muted Copy** | `#ff7cc1` | `var(--color-pink)` in `:root` |
| **Structural Hairline Border** | `#808080` | `.border-gray-400 { border-color: #808080 }` |
| **Variable Token (`--color-black`)** | `#000000` | `var(--color-black)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-gray-400` | `oklch(70.7% .022 261.325)` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-md` | `28rem` | Layout / Spatial Grid Token |
| `--container-lg` | `32rem` | Layout / Spatial Grid Token |
| `--container-xl` | `36rem` | Layout / Spatial Grid Token |
| `--text-sm` | `.75rem` | Typography Ink Token |
| `--text-sm--line-height` | `1.25` | Typography Ink Token |
| `--text-base` | `100%` | Typography Ink Token |
| `--text-base--line-height` | `normal` | Typography Ink Token |
| `--font-weight-medium` | `500` | Typography / Scale Token |
| `--font-weight-semibold` | `600` | Typography / Scale Token |
| `--tracking-wide` | `.025em` | Typography / Scale Token |
| `--leading-tight` | `1.25` | Typography / Scale Token |
| `--radius-xs` | `.125rem` | Elevation / Border Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Schibsted Grotesk`.
- **Primary Body Stack**: `Schibsted Grotesk`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 143.856px`, `line-height: 129.47px`, `font-weight: 400`, `letter-spacing: -2.87712px`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 55.944px`, `line-height: 61.5384px`, `font-weight: 400`, `letter-spacing: -1.07892px`); rule `h2` (`font-size: var(--text-bodyMobM,.9375rem)`, `line-height: var(--tw-leading,var(...`, `letter-spacing: var(--tw-tracking,var...`).
- **Body Copy**: live computed `body` (`font-size: 15.984px`, `line-height: normal`, `font-weight: 400`); CSS variables `--text-base: 100%`, `--text-base--line-height: normal`, `--text-bodyTagline: 5.5rem`; rule `p` (`font-size: var(--text-bodyMobL)`, `line-height: var(--tw-leading,var(...`, `letter-spacing: var(--tw-tracking,var...`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 15.984px`, `line-height: normal`, `font-weight: 400`); CSS variables `--text-sm: .75rem`, `--text-sm--line-height: 1.25`, `--default-mono-font-family: var(--font-mono)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `sincro-es_en-us` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `sincro-es_en-us` stylesheet.
- **Selector `.transition-\[height\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `sincro-es_en-us` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.top-0>` and `<main.max-w-full>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Swiper Touch Carousel Engine, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Us - Sincro                                │
│ ====================================================================== │
│ [ <header.top-0> (1440px)             | Overview · Index · Archive · ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <main.flex-1> (w=1440px)                               | │
│ | H1: 20 years of being who we say we are                            | │
│ | Substrate: #ffffff | Ink: #081423 | Accent: #0040ff                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<main.max-w-full>) max-w: 96rem                     | │
│ | +------------------------------+  +------------------------------+ | │
│ | | UNE Standard                 |  | Driven by and for the people | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<main.relative>) — Building networks                | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.border-mediu) | https://sincro.es/en/us/             │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 29.97px)    │
│ ====================================================================== │
│ [ HEADER BAR (<header.top-0>          ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<main.flex-1>) — 390px Vertical Lead                   | │
│ | H1: 20 years of being who we say we are                            | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<main.max-w-full>) — 1-Col Stack                   | │
│ | [ Item 1: UNE Standard                                           ] | │
│ | [ Item 2: Driven by and for the people                           ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<main.relative>) — 1-Col (Building networks)         | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.border-mediu) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.top-0> — `sincro-es_en-us`)**:
   - Landmark `<header class="top-0 left-0">` (`1440px`) hosting `Us - Sincro` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-v-8de50b09`, `data-swiper-slide-index="0"`, `data-swiper-slide-index="1"`, `data-swiper-slide-index="2"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<main.flex-1> — `20 years of being who we say we ar`)**:
   - Landmark `<main class="flex-1 max-w-full">` presenting display lead `20 years of being who we say we are` and copy excerpt *"Navigating complexity together"* over `#ffffff` canvas and `#081423` ink.
3. **Primary Showcase & Content Grid (<main.max-w-full> — `UNE Standard`)**:
   - Landmark `<main class="flex-1 max-w-full">` rendering section `UNE Standard` with copy *"We aim to be the strategic partner that brings excellence, techno"*, asset references (`entry.BcfY3otZ.css`, `Media.DbUUtcYg.css`, `PageBuilder.D9iVxonM.css`, `SchibstedGrotesk-Regular.woff2`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<main.relative> — `Driven by and for the people`)**:
   - Landmark `<main class="flex-1 max-w-full">` framing `Driven by and for the people` and `Building networks` (*"To help you navigate complexity with direction and confidence."*) with `#081423` surface cards, `#0040ff` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.border-mediumGrey> — `https://sincro.es/en/us/`)**:
   - Landmark `<footer class="border-mediumGrey pt-XL">` anchoring `Us - Sincro` footer links (`Overview · Index · Archive · About · Contact`), copy *"We were born and grew faithful to a simple idea: that consul"*, and `#808080` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: sincro-es_en-us (Us - Sincro)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `sincro-es_en-us` (**Us - Sincro** — `https://sincro.es/en/us/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#081423` ink, `#0040ff` accent).
- **Identity & Domain Context**: Navigating complexity together
- **Primary Substrate**: `#ffffff` (live computed `browser-default` `background-color` (`computed_styles.json`)), **Primary Ink**: `#081423`, **Accent / Highlight**: `#0040ff`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `browser-default` `background-color` (`computed_styles.json`)) paired with `#081423` primary typography and `#0040ff` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Schibsted Grotesk` for display copy (`20 years of being who we say we are`) with `Schibsted Grotesk` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `96rem` container bounds (`gap: 29.97px`, padding `var(--spacing-L)`) with `cubic-bezier(.4,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), Swiper Touch Carousel Engine.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `sincro-es_en-us` in your global stylesheet:

:root {
  /* Us - Sincro (sincro-es_en-us) — Live-Grounded CSS Variables */
  --color-gray-400: oklch(70.7% .022 261.325); /* Brand / Palette Token (sincro-es_en-us) */
  --color-black: #000; /* Canvas / Surface Token (sincro-es_en-us) */
  --color-white: #fff; /* Canvas / Surface Token (sincro-es_en-us) */
  --spacing: .25rem; /* Layout / Spatial Grid Token (sincro-es_en-us) */
  --container-md: 28rem; /* Layout / Spatial Grid Token (sincro-es_en-us) */
  --container-lg: 32rem; /* Layout / Spatial Grid Token (sincro-es_en-us) */
  --container-xl: 36rem; /* Layout / Spatial Grid Token (sincro-es_en-us) */
  --text-sm: .75rem; /* Typography Ink Token (sincro-es_en-us) */
  --text-sm--line-height: 1.25; /* Typography Ink Token (sincro-es_en-us) */
  --text-base: 100%; /* Typography Ink Token (sincro-es_en-us) */
  --text-base--line-height: normal; /* Typography Ink Token (sincro-es_en-us) */
  --font-weight-medium: 500; /* Typography / Scale Token (sincro-es_en-us) */
  --font-weight-semibold: 600; /* Typography / Scale Token (sincro-es_en-us) */
  --tracking-wide: .025em; /* Typography / Scale Token (sincro-es_en-us) */
  --leading-tight: 1.25; /* Typography / Scale Token (sincro-es_en-us) */
  --radius-xs: .125rem; /* Elevation / Border Token (sincro-es_en-us) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `browser-default` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#081423` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#081423` — grounded in `:placeholder-shown { background-color: #081423 }`
- **Interactive Accent / Highlight**: `#0040ff` — grounded in `var(--color-vividBlueHover)` in `:root`
- **Secondary / Muted Copy**: `#ff7cc1` — grounded in `var(--color-pink)` in `:root`
- **Structural Hairline Border**: `#808080` — grounded in `.border-gray-400 { border-color: #808080 }`
- **Variable Token (`--color-black`)**: `#000000` — grounded in `var(--color-black)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `96rem` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `var(--spacing-L)` lateral canvas padding with `29.97px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: 29.97px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--spacing-L)` horizontal padding
- **Media Queries**: `@media (width>=40rem)`, `@media (width>=64rem)`, `@media (width>=80rem)`, `@media (width>=96rem)`
- **Corner Radii**: `3.996px`, `.25rem`, `2147483647px`, `var(--radius-sm)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Schibsted Grotesk`
- **Body Font Stack**: `Schibsted Grotesk`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 143.856px`, `line-height: 129.47px`, `font-weight: 400`, `letter-spacing: -2.87712px`)
- **H2 Section Rule**: live computed `h2` (`font-size: 55.944px`, `line-height: 61.5384px`, `font-weight: 400`, `letter-spacing: -1.07892px`); rule `h2` (`font-size: var(--text-bodyMobM,.9375rem)`, `line-height: var(--tw-leading,var(...`, `letter-spacing: var(--tw-tracking,var...`)
- **Body Copy Rule**: live computed `body` (`font-size: 15.984px`, `line-height: normal`, `font-weight: 400`); CSS variables `--text-base: 100%`, `--text-base--line-height: normal`, `--text-bodyTagline: 5.5rem`; rule `p` (`font-size: var(--text-bodyMobL)`, `line-height: var(--tw-leading,var(...`, `letter-spacing: var(--tw-tracking,var...`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 15.984px`, `line-height: normal`, `font-weight: 400`); CSS variables `--text-sm: .75rem`, `--text-sm--line-height: 1.25`, `--default-mono-font-family: var(--font-mono)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `sincro-es_en-us` (`Us - Sincro`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.top-0> — `sincro-es_en-us`)**:
   - DOM & Selectors: Landmark `<header class="top-0 left-0">` (`1440px`) hosting `Us - Sincro` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-v-8de50b09`, `data-swiper-slide-index="0"`, `data-swiper-slide-index="1"`, `data-swiper-slide-index="2"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.top-0> — `sincro-es_en-us`)` (`sincro-es_en-us`) adapts across `@media (width>=40rem)`, `@media (width>=64rem)`, `@media (width>=80rem)`, `@media (width>=96rem)` with `cubic-bezier(.4,0,.2,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<main.flex-1> — `20 years of being who we say we ar`)**:
   - DOM & Selectors: Landmark `<main class="flex-1 max-w-full">` presenting display lead `20 years of being who we say we are` and copy excerpt *"Navigating complexity together"* over `#ffffff` canvas and `#081423` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#ffffff` background with `#081423` headline `20 years of being who we say we are`.
3. **Primary Showcase & Content Grid (<main.max-w-full> — `UNE Standard`)**:
   - DOM & Selectors: Landmark `<main class="flex-1 max-w-full">` rendering section `UNE Standard` with copy *"We aim to be the strategic partner that brings excellence, techno"*, asset references (`entry.BcfY3otZ.css`, `Media.DbUUtcYg.css`, `PageBuilder.D9iVxonM.css`, `SchibstedGrotesk-Regular.woff2`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<main.max-w-full> — `UNE Standard`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: 29.97px`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--spacing-L)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<main.relative> — `Driven by and for the people`)**:
   - DOM & Selectors: Landmark `<main class="flex-1 max-w-full">` framing `Driven by and for the people` and `Building networks` (*"To help you navigate complexity with direction and confidence."*) with `#081423` surface cards, `#0040ff` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<main.relative> — `Driven by and for the people`)` uses `3.996px`, `.25rem`, `2147483647px`, `var(--radius-sm)` radii, `#0040ff` highlights, and assets (entry.BcfY3otZ.css, Media.DbUUtcYg.css, PageBuilder.D9iVxonM.css).
5. **Colophon & Global Directory Footer (<footer.border-mediumGrey> — `https://sincro.es/en/us/`)**:
   - DOM & Selectors: Landmark `<footer class="border-mediumGrey pt-XL">` anchoring `Us - Sincro` footer links (`Overview · Index · Archive · About · Contact`), copy *"We were born and grew faithful to a simple idea: that consul"*, and `#808080` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.border-mediumGrey> — `https://sincro.es/en/us/`)` aligns to `96rem` (non-`@media` desktop container stylesheet rule) with `var(--spacing-L)` lateral canvas padding with `29.97px` grid gap and attributes (data-v-8de50b09, data-swiper-slide-index="0", data-swiper-slide-index="1").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Navigating complexity together"*
- Copy Excerpt 2: *"We aim to be the strategic partner that brings excellence, technology, and securit..."*
- Copy Excerpt 3: *"To help you navigate complexity with direction and confidence."*
- Copy Excerpt 4: *"We were born and grew faithful to a simple idea: that consulting can also be human..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`sincro-es_en-us`)**:
- `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- `sup { vertical-align:baseline;font-size:75%;line-height:0;position:relative }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `sincro-es_en-us` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `sincro-es_en-us` stylesheet.
- **Selector `.transition-\[height\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `sincro-es_en-us` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.top-0>` and `<main.max-w-full>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Swiper Touch Carousel Engine, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `sincro-es_en-us`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
