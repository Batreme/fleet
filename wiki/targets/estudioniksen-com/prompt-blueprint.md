---
title: "UI Prompt Blueprint: estudioniksen-com"
date: 2026-11-15
target: "estudioniksen-com"
status: analyzed
capture: specimen
capture_desktop: dom
capture_mobile: specimen
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#4f4f4f` accent)"
---

# UI Design System & Master Generation Blueprint: estudioniksen-com

> **Estudio Niksen** (https://estudioniksen.com/) — We are an independent lifestyle brand presenting elevated garments and living-space goods through a mix of influences.

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Estudio Niksen** (`https://estudioniksen.com/`). We are an independent lifestyle brand presenting elevated garments and living-space goods through a mix of influences.
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#4f4f4f` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--pswp-bg)` in `:root`) paired with `#fff` primary typography and `#4f4f4f` accents.
  - **Extracted Typographic Hierarchy**: Pairs `PP Frama` for display copy (`Cookie consent`) with `PP Neue Montreal` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `420px` container bounds (`gap: var(--spacing-gutter)`, padding `var(--button-padding)`) with `cubic-bezier(.4,0,.22,1)` easing and Lenis Smooth Scroll (`data-lenis`), Swiper Touch Carousel Engine.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Design Specimen (Offline WebGL/JS Fallback — not live site capture)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×10946px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `420px` extracted from `estudioniksen-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--button-padding)` lateral canvas padding with `var(--spacing-gutter)` grid gap.
- **Border Radius Scale**: `50%`, `var(--button-radius)`, `10px`, `.3125rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 420px`, `gap: var(--spacing-gutter)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--button-padding)` horizontal padding.
- **Extracted CSS Media Queries**: `@media not all and (width>=700px)`, `@media (width>=1000px)`, `@media not all and (width>=1000px)`, `@media (width>=420px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--pswp-bg)` in `:root` |
| **Primary Typography Ink** | `#222` | `var(--pswp-placeholder-bg)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff` | `var(--pswp-icon-color)` in `:root` |
| **Interactive Accent / Highlight** | `#4f4f4f` | `var(--pswp-icon-color-secondary)` in `:root` |
| **Secondary / Muted Copy** | `#f0f0f0` | `var(--color-gray-200)` in `:root` |
| **Structural Hairline Border** | `#a0a1a0` | `var(--color-gray-300)` in `:root` |
| **Variable Token (`--pswp-preloader-color`)** | `#4f4f4f66` | `var(--pswp-preloader-color)` in `:root` |
| **Variable Token (`--pswp-preloader-color-secondary`)** | `#ffffffe6` | `var(--pswp-preloader-color-secondary)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--pswp-bg` | `#000` | Canvas / Surface Token |
| `--pswp-placeholder-bg` | `#222` | Canvas / Surface Token |
| `--pswp-root-z-index` | `100000` | Elevation / Border Token |
| `--pswp-preloader-color` | `#4f4f4f66` | Brand / Palette Token |
| `--pswp-preloader-color-secondary` | `#ffffffe6` | Brand / Palette Token |
| `--pswp-icon-color` | `#fff` | Brand / Palette Token |
| `--pswp-icon-color-secondary` | `#4f4f4f` | Brand / Palette Token |
| `--pswp-icon-stroke-color` | `#4f4f4f` | Brand / Palette Token |
| `--pswp-icon-stroke-width` | `2px` | Layout / Spatial Grid Token |
| `--pswp-error-text-color` | `var(--pswp-icon-color)` | Typography Ink Token |
| `--color-red-500` | `oklch(63.7% .237 25.331)` | Brand / Palette Token |
| `--color-gray-200` | `#f0f0f0` | Brand / Palette Token |
| `--color-gray-300` | `#a0a1a0` | Brand / Palette Token |
| `--color-gray-600` | `oklch(44.6% .03 256.802)` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `PP Frama`.
- **Primary Body Stack**: `PP Neue Montreal`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--x-shell-disclosure-display: block`, `--x-shell-order-summary-display: none`, `--x-shell-content-display: grid`; rule `h1` (`font-size: var(--x-heading-level1-font-s...`, `line-height: var(--x-typography-li...`, `letter-spacing: var(--x-heading-level...`, `font-weight: var(--x-headi...`).
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`; rule `h2` (`font-size: var(--x-heading-level2-font-s...`, `line-height: var(--x-typography-li...`, `letter-spacing: var(--x-heading-level...`, `font-weight: var(--x-headi...`).
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`font-size: var(--text-xxs)`, `line-height: 1.1`, `font-weight: var(--font-we...`).
- **Metadata & Navigation Labels**: CSS variables `--text-xs: 12px`, `--text-xs--line-height: calc(1 / .75)`, `--default-mono-font-family: var(--font-mono)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.22,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.lenis.lenis-autoToggle`**: `transition: 1ms` extracted from `estudioniksen-com` stylesheet.
- **Selector `.swiper-wrapper`**: `transition: var(--swiper-wrapper-transition-timing-function,initial)` extracted from `estudioniksen-com` stylesheet.
- **Selector `.swiper-pagination`**: `transition: opacity .3s` extracted from `estudioniksen-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.22,1)`)**: Governs interactive state transitions across `<header.c-header_inner>` and `<section.shopify-pc__banner__dialog>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Estudio Niksen                             │
│ ====================================================================== │
│ [ <header.c-header_inner>  | Shop All · Outerwear · All Outerwear · ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.shopify-pc__banner__dialog>                 |   │
│ | H1: Cookie consent                                               |   │
│ | Substrate: #000       | Ink: #fff       | Accent: #4f4f4f        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.shopify-pc__banne) max-w: 420px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Join the family              |  | Fall Winter '26              | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<header.c-header_i] -> [<section.shopify-p] -> [<section.shopify-p] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.container>    ) | https://estudioniksen.com/         │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.c-header_inner> — `estudioniksen-com`)**:
   - Landmark `<header class="c-header_inner">` hosting `Estudio Niksen` navigation (`Shop All · Outerwear · All Outerwear · Coats · Jackets`), DOM attributes (`data-template="index"`, `data-smooth-scrolling="true"`, `data-scroll-orientation="vertical"`, `data-source-attribution="shopify.exit_intersti..."`), and stylesheet rule `html.lenis body { height:auto }`.
2. **Hero Stage & Focal Lead (<section.shopify-pc__banner__dialog> — `Cookie consent`)**:
   - Landmark `<section class="shopify-pc__banner__dialog">` presenting display lead `Cookie consent` and copy excerpt *"We use cookies and other technologies to personalize your experie"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.shopify-pc__banner__dialog> — `Join the family`)**:
   - Landmark `<section class="shopify-pc__banner__dialog">` rendering section `Join the family` with copy *"Manage preferences"*, asset references (`a2f45e7b43c941fd84b3f91a8.js`, `favicon.svg`, `site.webmanifest`, `vite-main-C-QMCZi1.css`), and grid rule `.lenis-stopped { overflow:clip }`.
4. **Interactive Detail & Feature Matrix (<section.shopify-pc__banner__dialog> — `Fall Winter '26`)**:
   - Landmark `<section class="shopify-pc__banner__dialog">` framing `Fall Winter '26` and `New arrivals` (*"Free shipping on orders over $250 CAD"*) with `#fff` surface cards, `#4f4f4f` accents, and `.lenis.lenis-smooth iframe { pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.container> — `https://estudioniksen.com/`)**:
   - Landmark `<footer class="container mt-fluid-3xl">` anchoring `Estudio Niksen` footer links (`Shop All · Outerwear · All Outerwear · Coats · Jackets`), copy *"Early-access to our drops, secret password to our only annua"*, and `#a0a1a0` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: estudioniksen-com (Estudio Niksen)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `estudioniksen-com` (**Estudio Niksen** — `https://estudioniksen.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#4f4f4f` accent).
- **Identity & Domain Context**: We are an independent lifestyle brand presenting elevated garments and living-space goods through a mix of influences.
- **Primary Substrate**: `#000` (`var(--pswp-bg)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#4f4f4f`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--pswp-bg)` in `:root`) paired with `#fff` primary typography and `#4f4f4f` accents.
  - **Extracted Typographic Hierarchy**: Pairs `PP Frama` for display copy (`Cookie consent`) with `PP Neue Montreal` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `420px` container bounds (`gap: var(--spacing-gutter)`, padding `var(--button-padding)`) with `cubic-bezier(.4,0,.22,1)` easing and Lenis Smooth Scroll (`data-lenis`), Swiper Touch Carousel Engine.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `estudioniksen-com` in your global stylesheet:

:root {
  /* Estudio Niksen (estudioniksen-com) — Ground-Truth Extracted CSS Variables */
  --pswp-bg: #000; /* Canvas / Surface Token (estudioniksen-com) */
  --pswp-placeholder-bg: #222; /* Canvas / Surface Token (estudioniksen-com) */
  --pswp-root-z-index: 100000; /* Elevation / Border Token (estudioniksen-com) */
  --pswp-preloader-color: #4f4f4f66; /* Brand / Palette Token (estudioniksen-com) */
  --pswp-preloader-color-secondary: #ffffffe6; /* Brand / Palette Token (estudioniksen-com) */
  --pswp-icon-color: #fff; /* Brand / Palette Token (estudioniksen-com) */
  --pswp-icon-color-secondary: #4f4f4f; /* Brand / Palette Token (estudioniksen-com) */
  --pswp-icon-stroke-color: #4f4f4f; /* Brand / Palette Token (estudioniksen-com) */
  --pswp-icon-stroke-width: 2px; /* Layout / Spatial Grid Token (estudioniksen-com) */
  --pswp-error-text-color: var(--pswp-icon-color); /* Typography Ink Token (estudioniksen-com) */
  --color-red-500: oklch(63.7% .237 25.331); /* Brand / Palette Token (estudioniksen-com) */
  --color-gray-200: #f0f0f0; /* Brand / Palette Token (estudioniksen-com) */
  --color-gray-300: #a0a1a0; /* Brand / Palette Token (estudioniksen-com) */
  --color-gray-600: oklch(44.6% .03 256.802); /* Brand / Palette Token (estudioniksen-com) */
  --color-black: #000; /* Canvas / Surface Token (estudioniksen-com) */
  --color-white: #fff; /* Canvas / Surface Token (estudioniksen-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000` — grounded in `var(--pswp-bg)` in `:root`
- **Primary Typography Ink**: `#222` — grounded in `var(--pswp-placeholder-bg)` in `:root`
- **Elevated Surface / Card Substrate**: `#fff` — grounded in `var(--pswp-icon-color)` in `:root`
- **Interactive Accent / Highlight**: `#4f4f4f` — grounded in `var(--pswp-icon-color-secondary)` in `:root`
- **Secondary / Muted Copy**: `#f0f0f0` — grounded in `var(--color-gray-200)` in `:root`
- **Structural Hairline Border**: `#a0a1a0` — grounded in `var(--color-gray-300)` in `:root`
- **Variable Token (`--pswp-preloader-color`)**: `#4f4f4f66` — grounded in `var(--pswp-preloader-color)` in `:root`
- **Variable Token (`--pswp-preloader-color-secondary`)**: `#ffffffe6` — grounded in `var(--pswp-preloader-color-secondary)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×10946px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `420px` extracted from `estudioniksen-com` stylesheet
- **Padding & Gutters**: `var(--button-padding)` lateral canvas padding with `var(--spacing-gutter)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 420px`, `gap: var(--spacing-gutter)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--button-padding)` horizontal padding
- **Media Queries**: `@media not all and (width>=700px)`, `@media (width>=1000px)`, `@media not all and (width>=1000px)`, `@media (width>=420px)`
- **Corner Radii**: `50%`, `var(--button-radius)`, `10px`, `.3125rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `PP Frama`
- **Body Font Stack**: `PP Neue Montreal`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--x-shell-disclosure-display: block`, `--x-shell-order-summary-display: none`, `--x-shell-content-display: grid`; rule `h1` (`font-size: var(--x-heading-level1-font-s...`, `line-height: var(--x-typography-li...`, `letter-spacing: var(--x-heading-level...`, `font-weight: var(--x-headi...`)
- **H2 Section Rule**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`; rule `h2` (`font-size: var(--x-heading-level2-font-s...`, `line-height: var(--x-typography-li...`, `letter-spacing: var(--x-heading-level...`, `font-weight: var(--x-headi...`)
- **Body Copy Rule**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`font-size: var(--text-xxs)`, `line-height: 1.1`, `font-weight: var(--font-we...`)
- **Metadata & Index Rule**: CSS variables `--text-xs: 12px`, `--text-xs--line-height: calc(1 / .75)`, `--default-mono-font-family: var(--font-mono)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `estudioniksen-com` (`Estudio Niksen`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.c-header_inner> — `estudioniksen-com`)**:
   - DOM & Selectors: Landmark `<header class="c-header_inner">` hosting `Estudio Niksen` navigation (`Shop All · Outerwear · All Outerwear · Coats · Jackets`), DOM attributes (`data-template="index"`, `data-smooth-scrolling="true"`, `data-scroll-orientation="vertical"`, `data-source-attribution="shopify.exit_intersti..."`), and stylesheet rule `html.lenis body { height:auto }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.c-header_inner> — `estudioniksen-com`)` (`estudioniksen-com`) adapts across `@media not all and (width>=700px)`, `@media (width>=1000px)`, `@media not all and (width>=1000px)`, `@media (width>=420px)` with `cubic-bezier(.4,0,.22,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.6,1)` transitions and links `Shop All · Outerwear · All Outerwear · Coats · Jackets`.
2. **Hero Stage & Focal Lead (<section.shopify-pc__banner__dialog> — `Cookie consent`)**:
   - DOM & Selectors: Landmark `<section class="shopify-pc__banner__dialog">` presenting display lead `Cookie consent` and copy excerpt *"We use cookies and other technologies to personalize your experie"* over `#000` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×10946px` desktop / `390×2400px` mobile) sets `#000` background with `#fff` headline `Cookie consent`.
3. **Primary Showcase & Content Grid (<section.shopify-pc__banner__dialog> — `Join the family`)**:
   - DOM & Selectors: Landmark `<section class="shopify-pc__banner__dialog">` rendering section `Join the family` with copy *"Manage preferences"*, asset references (`a2f45e7b43c941fd84b3f91a8.js`, `favicon.svg`, `site.webmanifest`, `vite-main-C-QMCZi1.css`), and grid rule `.lenis-stopped { overflow:clip }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.shopify-pc__banner__dialog> — `Join the family`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 420px`, `gap: var(--spacing-gutter)`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--button-padding)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.shopify-pc__banner__dialog> — `Fall Winter '26`)**:
   - DOM & Selectors: Landmark `<section class="shopify-pc__banner__dialog">` framing `Fall Winter '26` and `New arrivals` (*"Free shipping on orders over $250 CAD"*) with `#fff` surface cards, `#4f4f4f` accents, and `.lenis.lenis-smooth iframe { pointer-events:none }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.shopify-pc__banner__dialog> — `Fall Winter '26`)` uses `50%`, `var(--button-radius)`, `10px`, `.3125rem` radii, `#4f4f4f` highlights, and assets (a2f45e7b43c941fd84b3f91a8.js, favicon.svg, site.webmanifest).
5. **Colophon & Global Directory Footer (<footer.container> — `https://estudioniksen.com/`)**:
   - DOM & Selectors: Landmark `<footer class="container mt-fluid-3xl">` anchoring `Estudio Niksen` footer links (`Shop All · Outerwear · All Outerwear · Coats · Jackets`), copy *"Early-access to our drops, secret password to our only annua"*, and `#a0a1a0` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.container> — `https://estudioniksen.com/`)` aligns to `420px` extracted from `estudioniksen-com` stylesheet with `var(--button-padding)` lateral canvas padding with `var(--spacing-gutter)` grid gap and attributes (data-template="index", data-smooth-scrolling="true", data-scroll-orientation="vertical").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"We use cookies and other technologies to personalize your experience, show you ads..."*
- Copy Excerpt 2: *"Manage preferences"*
- Copy Excerpt 3: *"Free shipping on orders over $250 CAD"*
- Copy Excerpt 4: *"Early-access to our drops, secret password to our only annual sale, exclusive insi..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.22,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`
- **Extracted Stylesheet Rules (`estudioniksen-com`)**:
- `html.lenis body { height:auto }`
- `.lenis-stopped { overflow:clip }`
- `.lenis.lenis-smooth iframe { pointer-events:none }`
- `.lenis.lenis-autoToggle { transition-behavior:allow-discrete;transition-property:overflow;transiti... }`
- `root { --swiper-theme-color:007aff }`
- **Per-Selector Transition Rules**:
- **Selector `.lenis.lenis-autoToggle`**: `transition: 1ms` extracted from `estudioniksen-com` stylesheet.
- **Selector `.swiper-wrapper`**: `transition: var(--swiper-wrapper-transition-timing-function,initial)` extracted from `estudioniksen-com` stylesheet.
- **Selector `.swiper-pagination`**: `transition: opacity .3s` extracted from `estudioniksen-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.22,1)`)**: Governs interactive state transitions across `<header.c-header_inner>` and `<section.shopify-pc__banner__dialog>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `estudioniksen-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
