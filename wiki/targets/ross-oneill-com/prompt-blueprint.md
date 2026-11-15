---
title: "UI Prompt Blueprint: ross-oneill-com"
date: 2026-11-15
target: "ross-oneill-com"
status: analyzed
capture: dom
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#f5f5f7` accent)"
---

# UI Design System & Master Generation Blueprint: ross-oneill-com

> **Ross O'Neill · Freelance Web Developer and Designer in Perth** (https://ross-oneill.com/) — Freelance web developer and designer in North Beach, Perth. Fast custom websites for WA businesses, built and looked after by the person...

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Ross O'Neill · Freelance Web Developer and Designer in Perth** (`https://ross-oneill.com/`). Freelance web developer and designer in North Beach, Perth. Fast custom websites for WA businesses, built and looked after by the person...
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#f5f5f7` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--color-black)` in `:root`) paired with `#fff` primary typography and `#f5f5f7` accents.
  - **Extracted Typographic Hierarchy**: Pairs `DM Sans` for display copy (`Ross O'Neill, a Perth-based web deve`) with `Segoe UI` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: 1rem`, padding `.5rem`) with `cubic-bezier(.4,0,1,1)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×3718px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `40rem` extracted from `ross-oneill-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `.5rem` lateral canvas padding with `1rem` grid gap.
- **Border Radius Scale**: `100%`, `9999px`, `var(--radius-base)`, `8px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: 1rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `.5rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (width>=640px)`, `@media (width>=40rem)`, `@media (width>=48rem)`, `@media (width>=64rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#da0a2c` | `var(--color-accent)` in `:root` |
| **Interactive Accent / Highlight** | `#f5f5f7` | `var(--color-offwhite)` in `:root` |
| **Secondary / Muted Copy** | `#0000` | `textarea { background-color: #0000 }` |
| **Structural Hairline Border** | `#ffffff` | `:disabled:checked:after { background-color: white }` (`#ffffff`) |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-red-50` | `oklch(97.1% .013 17.38)` | Brand / Palette Token |
| `--color-red-100` | `oklch(93.6% .032 17.717)` | Brand / Palette Token |
| `--color-red-200` | `oklch(88.5% .062 18.334)` | Brand / Palette Token |
| `--color-red-300` | `oklch(80.8% .114 19.571)` | Brand / Palette Token |
| `--color-red-400` | `oklch(70.4% .191 22.216)` | Brand / Palette Token |
| `--color-red-500` | `oklch(63.7% .237 25.331)` | Brand / Palette Token |
| `--color-red-600` | `oklch(57.7% .245 27.325)` | Brand / Palette Token |
| `--color-red-700` | `oklch(50.5% .213 27.518)` | Brand / Palette Token |
| `--color-red-800` | `oklch(44.4% .177 26.899)` | Brand / Palette Token |
| `--color-red-900` | `oklch(39.6% .141 25.723)` | Brand / Palette Token |
| `--color-red-950` | `oklch(25.8% .092 26.042)` | Brand / Palette Token |
| `--color-orange-50` | `oklch(98% .016 73.684)` | Brand / Palette Token |
| `--color-orange-100` | `oklch(95.4% .038 75.164)` | Brand / Palette Token |
| `--color-orange-200` | `oklch(90.1% .076 70.697)` | Brand / Palette Token |
| `--color-orange-300` | `oklch(83.7% .128 66.29)` | Brand / Palette Token |
| `--color-orange-400` | `oklch(75% .183 55.934)` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `DM Sans`.
- **Primary Body Stack**: `Segoe UI`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`.
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`.
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`, `--color-body: var(--color-gray-600)`.
- **Metadata & Navigation Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `ross-oneill-com` stylesheet.
- **Selector `.toggle-bg:after`**: `transition: .15s` extracted from `ross-oneill-com` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `ross-oneill-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.header-content>` and `<section.bg-white>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Ross O'Neill · Freelance Web Developer and │
│ ====================================================================== │
│ [ <header.header-content>  | About Me · Plans · Work · Blog · Get i ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.bg-white>                                   |   │
│ | H1: Ross O'Neill, a Perth-based web developer who tra...         |   │
│ | Substrate: #000       | Ink: #fff       | Accent: #f5f5f7        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.bg-white>        ) max-w: 40rem          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Margaret River Region        |  | Capes Foundation             | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 1rem  ) | │
│ | [<header.header-con] -> [<section.bg-white>] -> [<section.bg-white>] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.relative>     ) | https://ross-oneill.com/           │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.header-content> — `ross-oneill-com`)**:
   - Landmark `<header class="header-content fixed">` hosting `Ross O'Neill · Freelance Web Develop` navigation (`About Me · Plans · Work · Blog · Get in Touch`), DOM attributes (`data-astro-exec`, `data-cfasync="false"`, `data-icon="carbon:arrow-right"`, `data-icon="carbon:arrow-right"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.bg-white> — `Ross O'Neill, a Perth-based web de`)**:
   - Landmark `<section class="bg-white py-28">` presenting display lead `Ross O'Neill, a Perth-based web developer who tra...` and copy excerpt *"Ross O'Neill, a Perth-based web developer who transforms designs "* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.bg-white> — `Margaret River Region`)**:
   - Landmark `<section class="bg-white pb-12">` rendering section `Margaret River Region` with copy *"Swipe to See Full Portfolio"*, asset references (`favicon.ico`, `favicon.svg`, `sitemap-index.xml`, `static.cloudflareinsights.com`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.relative> — `Capes Foundation`)**:
   - Landmark `<section class="relative py-12">` framing `Capes Foundation` and `CMEWA` (*"See Full Portfolio"*) with `#da0a2c` surface cards, `#f5f5f7` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://ross-oneill.com/`)**:
   - Landmark `<footer class="relative text-white">` anchoring `Ross O'Neill · Freelance Web Dev` footer links (`About Me · Plans · Work · Blog · Get in Touch`), copy *"Margaret River Region"*, and `#ffffff` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: ross-oneill-com (Ross O'Neill · Freelance Web Developer and Designer in Perth)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `ross-oneill-com` (**Ross O'Neill · Freelance Web Developer and Designer in Perth** — `https://ross-oneill.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#f5f5f7` accent).
- **Identity & Domain Context**: Freelance web developer and designer in North Beach, Perth. Fast custom websites for WA businesses, built and looked after by the person...
- **Primary Substrate**: `#000` (`var(--color-black)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#f5f5f7`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--color-black)` in `:root`) paired with `#fff` primary typography and `#f5f5f7` accents.
  - **Extracted Typographic Hierarchy**: Pairs `DM Sans` for display copy (`Ross O'Neill, a Perth-based web deve`) with `Segoe UI` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: 1rem`, padding `.5rem`) with `cubic-bezier(.4,0,1,1)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `ross-oneill-com` in your global stylesheet:

:root {
  /* Ross O'Neill · Freelance Web Developer and Designer in Perth (ross-oneill-com) — Ground-Truth Extracted CSS Variables */
  --color-red-50: oklch(97.1% .013 17.38); /* Brand / Palette Token (ross-oneill-com) */
  --color-red-100: oklch(93.6% .032 17.717); /* Brand / Palette Token (ross-oneill-com) */
  --color-red-200: oklch(88.5% .062 18.334); /* Brand / Palette Token (ross-oneill-com) */
  --color-red-300: oklch(80.8% .114 19.571); /* Brand / Palette Token (ross-oneill-com) */
  --color-red-400: oklch(70.4% .191 22.216); /* Brand / Palette Token (ross-oneill-com) */
  --color-red-500: oklch(63.7% .237 25.331); /* Brand / Palette Token (ross-oneill-com) */
  --color-red-600: oklch(57.7% .245 27.325); /* Brand / Palette Token (ross-oneill-com) */
  --color-red-700: oklch(50.5% .213 27.518); /* Brand / Palette Token (ross-oneill-com) */
  --color-red-800: oklch(44.4% .177 26.899); /* Brand / Palette Token (ross-oneill-com) */
  --color-red-900: oklch(39.6% .141 25.723); /* Brand / Palette Token (ross-oneill-com) */
  --color-red-950: oklch(25.8% .092 26.042); /* Brand / Palette Token (ross-oneill-com) */
  --color-orange-50: oklch(98% .016 73.684); /* Brand / Palette Token (ross-oneill-com) */
  --color-orange-100: oklch(95.4% .038 75.164); /* Brand / Palette Token (ross-oneill-com) */
  --color-orange-200: oklch(90.1% .076 70.697); /* Brand / Palette Token (ross-oneill-com) */
  --color-orange-300: oklch(83.7% .128 66.29); /* Brand / Palette Token (ross-oneill-com) */
  --color-orange-400: oklch(75% .183 55.934); /* Brand / Palette Token (ross-oneill-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000` — grounded in `var(--color-black)` in `:root`
- **Primary Typography Ink**: `#fff` — grounded in `var(--color-white)` in `:root`
- **Elevated Surface / Card Substrate**: `#da0a2c` — grounded in `var(--color-accent)` in `:root`
- **Interactive Accent / Highlight**: `#f5f5f7` — grounded in `var(--color-offwhite)` in `:root`
- **Secondary / Muted Copy**: `#0000` — grounded in `textarea { background-color: #0000 }`
- **Structural Hairline Border**: `#ffffff` — grounded in `:disabled:checked:after { background-color: white }` (`#ffffff`)

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×3718px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `40rem` extracted from `ross-oneill-com` stylesheet
- **Padding & Gutters**: `.5rem` lateral canvas padding with `1rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: 1rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `.5rem` horizontal padding
- **Media Queries**: `@media (width>=640px)`, `@media (width>=40rem)`, `@media (width>=48rem)`, `@media (width>=64rem)`
- **Corner Radii**: `100%`, `9999px`, `var(--radius-base)`, `8px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `DM Sans`
- **Body Font Stack**: `Segoe UI`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **H2 Section Rule**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`
- **Body Copy Rule**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`, `--color-body: var(--color-gray-600)`
- **Metadata & Index Rule**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `ross-oneill-com` (`Ross O'Neill · Freelance Web Developer and Designer in Perth`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.header-content> — `ross-oneill-com`)**:
   - DOM & Selectors: Landmark `<header class="header-content fixed">` hosting `Ross O'Neill · Freelance Web Develop` navigation (`About Me · Plans · Work · Blog · Get in Touch`), DOM attributes (`data-astro-exec`, `data-cfasync="false"`, `data-icon="carbon:arrow-right"`, `data-icon="carbon:arrow-right"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.header-content> — `ross-oneill-com`)` (`ross-oneill-com`) adapts across `@media (width>=640px)`, `@media (width>=40rem)`, `@media (width>=48rem)`, `@media (width>=64rem)` with `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `About Me · Plans · Work · Blog · Get in Touch`.
2. **Hero Stage & Focal Lead (<section.bg-white> — `Ross O'Neill, a Perth-based web de`)**:
   - DOM & Selectors: Landmark `<section class="bg-white py-28">` presenting display lead `Ross O'Neill, a Perth-based web developer who tra...` and copy excerpt *"Ross O'Neill, a Perth-based web developer who transforms designs "* over `#000` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×3718px` desktop / `390×2400px` mobile) sets `#000` background with `#fff` headline `Ross O'Neill, a Perth-based web developer who tra...`.
3. **Primary Showcase & Content Grid (<section.bg-white> — `Margaret River Region`)**:
   - DOM & Selectors: Landmark `<section class="bg-white pb-12">` rendering section `Margaret River Region` with copy *"Swipe to See Full Portfolio"*, asset references (`favicon.ico`, `favicon.svg`, `sitemap-index.xml`, `static.cloudflareinsights.com`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.bg-white> — `Margaret River Region`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: 1rem`) on desktop and Single-column vertical stack at `390px` viewport width with `.5rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.relative> — `Capes Foundation`)**:
   - DOM & Selectors: Landmark `<section class="relative py-12">` framing `Capes Foundation` and `CMEWA` (*"See Full Portfolio"*) with `#da0a2c` surface cards, `#f5f5f7` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.relative> — `Capes Foundation`)` uses `100%`, `9999px`, `var(--radius-base)`, `8px` radii, `#f5f5f7` highlights, and assets (favicon.ico, favicon.svg, sitemap-index.xml).
5. **Colophon & Global Directory Footer (<footer.relative> — `https://ross-oneill.com/`)**:
   - DOM & Selectors: Landmark `<footer class="relative text-white">` anchoring `Ross O'Neill · Freelance Web Dev` footer links (`About Me · Plans · Work · Blog · Get in Touch`), copy *"Margaret River Region"*, and `#ffffff` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.relative> — `https://ross-oneill.com/`)` aligns to `40rem` extracted from `ross-oneill-com` stylesheet with `.5rem` lateral canvas padding with `1rem` grid gap and attributes (data-astro-exec, data-cfasync="false", data-icon="carbon:arrow-right").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Ross O'Neill, a Perth-based web developer who transforms designs into lightning-fa..."*
- Copy Excerpt 2: *"Swipe to See Full Portfolio"*
- Copy Excerpt 3: *"See Full Portfolio"*
- Copy Excerpt 4: *"Margaret River Region"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`ross-oneill-com`)**:
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- `sup { vertical-align:baseline;font-size:75%;line-height:0;position:relative }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `ross-oneill-com` stylesheet.
- **Selector `.toggle-bg:after`**: `transition: .15s` extracted from `ross-oneill-com` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `ross-oneill-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.header-content>` and `<section.bg-white>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `ross-oneill-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
