---
title: "UI Prompt Blueprint: myfrida-com"
date: 2026-11-15
target: "[[overview|myfrida-com]]"
status: analyzed
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#0d6efd` canvas, `#6610f2` ink, `#d63384` accent)"
---

# UI Design System & Master Generation Blueprint: myfrida-com

> **My Frida · Chocolate-Covered Fruit, Smoothies & Cake Bars** (https://myfrida.com/) — Discover My Frida: real fruit wrapped in chocolate, fruity Choco Smoothies, frozen treats and layered Fridika Cake Bars. Find your favour...

![Desktop Viewport Capture (1440x7118)](file:///root/projects/fleet/wiki/targets/myfrida-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **My Frida · Chocolate-Covered Fruit, Smoothies & Cake Bars** (`https://myfrida.com/`). Discover My Frida: real fruit wrapped in chocolate, fruity Choco Smoothies, frozen treats and layered Fridika Cake Bars. Find your favour...
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#0d6efd` canvas, `#6610f2` ink, `#d63384` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#0d6efd` (`var(--bs-blue)` in `:root`) paired with `#6610f2` primary typography and `#d63384` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Josefin Sans` for display copy (`Fresh fruit covered in chocolate`) with `Source Sans Pro` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `540px` container bounds (`gap: 1rem`, padding `2rem`) with `cubic-bezier(0.22,1,0.36,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/myfrida-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×7118px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `540px` extracted from `myfrida-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `2rem` lateral canvas padding with `1rem` grid gap.
- **Border Radius Scale**: `0.375rem`, `.25rem`, `var(--bs-border-radius)`, `var(--bs-border-radius-sm)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 540px`, `gap: 1rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `2rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:1200px)`, `@media (min-width:576px)`, `@media (min-width:768px)`, `@media (min-width:992px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0d6efd` | `var(--bs-blue)` in `:root` |
| **Primary Typography Ink** | `#6610f2` | `var(--bs-indigo)` in `:root` |
| **Elevated Surface / Card Substrate** | `#6f42c1` | `var(--bs-purple)` in `:root` |
| **Interactive Accent / Highlight** | `#d63384` | `var(--bs-pink)` in `:root` |
| **Secondary / Muted Copy** | `#dc3545` | `var(--bs-red)` in `:root` |
| **Structural Hairline Border** | `#fd7e14` | `var(--bs-orange)` in `:root` |
| **Variable Token (`--bs-yellow`)** | `#ffc107` | `var(--bs-yellow)` in `:root` |
| **Variable Token (`--bs-green`)** | `#198754` | `var(--bs-green)` in `:root` |
| **Variable Token (`--bs-teal`)** | `#20c997` | `var(--bs-teal)` in `:root` |
| **Variable Token (`--bs-cyan`)** | `#0dcaf0` | `var(--bs-cyan)` in `:root` |
| **Variable Token (`--bs-black`)** | `#000` | `var(--bs-black)` in `:root` |
| **Variable Token (`--bs-white`)** | `#fff` | `var(--bs-white)` in `:root` |
| **Variable Token (`--bs-gray`)** | `#6c757d` | `var(--bs-gray)` in `:root` |
| **Variable Token (`--bs-gray-dark`)** | `#343a40` | `var(--bs-gray-dark)` in `:root` |
| **Variable Token (`--bs-gray-100`)** | `#f8f9fa` | `var(--bs-gray-100)` in `:root` |
| **Variable Token (`--bs-gray-200`)** | `#e9ecef` | `var(--bs-gray-200)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bs-blue` | `#0d6efd` | Color / Atmospheric Token |
| `--bs-indigo` | `#6610f2` | Color / Atmospheric Token |
| `--bs-purple` | `#6f42c1` | Color / Atmospheric Token |
| `--bs-pink` | `#d63384` | Typography Ink Token |
| `--bs-red` | `#dc3545` | Color / Atmospheric Token |
| `--bs-orange` | `#fd7e14` | Color / Atmospheric Token |
| `--bs-yellow` | `#ffc107` | Color / Atmospheric Token |
| `--bs-green` | `#198754` | Color / Atmospheric Token |
| `--bs-teal` | `#20c997` | Color / Atmospheric Token |
| `--bs-cyan` | `#0dcaf0` | Color / Atmospheric Token |
| `--bs-black` | `#000` | Canvas / Surface Token |
| `--bs-white` | `#fff` | Canvas / Surface Token |
| `--bs-gray` | `#6c757d` | Color / Atmospheric Token |
| `--bs-gray-dark` | `#343a40` | Canvas / Surface Token |
| `--bs-gray-100` | `#f8f9fa` | Color / Atmospheric Token |
| `--bs-gray-200` | `#e9ecef` | Color / Atmospheric Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Josefin Sans`.
- **Primary Body Stack**: `Source Sans Pro`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `,.h1` (`line-height: 1.2`, `font-weight: 500`).
- **Section Heading (`H2`)**: rule `,.h2` (`font-size: calc(1.325rem + 0.9vw)`).
- **Body Copy**: CSS variables `--bs-body-font-family: var(--bs-font-sans-serif)`, `--bs-body-font-size: 1rem`, `--bs-body-font-weight: 400`; rule `p` (`font-size: min(1vw,20px)`, `line-height: 1.2`, `font-weight: 400`).
- **Metadata & Navigation Labels**: CSS variables `--bs-carousel-caption-color: #000`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.22,1,0.36,1)`, `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(0,0,0.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.widget_archive select`**: `transition: border-color .15s ease-in-out,box-shadow .15s ease-in-out` extracted from `myfrida-com` stylesheet.
- **Selector `widget_archive select::file-selec...`**: `transition: color .15s ease-in-out,background-color .15s ease-in-out,borde...` extracted from `myfrida-com` stylesheet.
- **Selector `.select2-selection`**: `transition: border-color .15s ease-in-out,box-shadow .15s ease-in-out` extracted from `myfrida-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.22,1,0.36,1)`)**: Governs interactive state transitions across `<header.webp>` and `<section.tf-uvod>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — My Frida · Chocolate-Covered Fruit, Smooth │
│ ====================================================================== │
│ [ <header.webp>            | Meet Frida · Contact us                ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.tf-hero>                                    |   │
│ | H1: Fresh fruit covered in chocolate                             |   │
│ | Substrate: #0d6efd    | Ink: #6610f2    | Accent: #d63384        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.tf-uvod>         ) max-w: 540px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | My Frida my moment           |  | Whatever you call her,       | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 1rem  ) | │
│ | [<header.webp>] -> [<section.tf-hero>] -> [<section.tf-uvod>] |      │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.wp-singular>  ) | https://myfrida.com/               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.webp> — `myfrida-com`)**:
   - Landmark `<header class="webp">` hosting `My Frida · Chocolate-Covered Fruit, ` navigation (`Meet Frida · Contact us`), DOM attributes (`data-smush-preload`, `data-rocket-prefetch`, `data-rocket-preload`, `data-minify="1"`), and stylesheet rule `.fa-lg { font-size:1.33333em;line-height:.75em;vertical-align:-.0667em }`.
2. **Hero Stage & Focal Lead (<section.tf-hero> — `Fresh fruit covered in chocolate`)**:
   - Landmark `<section class="tf-hero">` presenting display lead `Fresh fruit covered in chocolate` and copy excerpt *"Choco Fruits Frozen"* over `#0d6efd` canvas and `#6610f2` ink.
3. **Primary Showcase & Content Grid (<section.tf-uvod> — `My Frida my moment`)**:
   - Landmark `<section class="tf-uvod container-fluid">` rendering section `My Frida my moment` with copy *"Choco Fruits Frozen ›"*, asset references (`myfrida-hero-frozen-1200.webp`, `b4751355.assetcdn.net`, `myfrida-source-sans-pro-400-latin...`, `myfrida-josefin-sans-700-latin.woff2`), and grid rule `.fa-xs { font-size:.75em }`.
4. **Interactive Detail & Feature Matrix (<section.tf-marquee> — `Whatever you call her,`)**:
   - Landmark `<section class="tf-marquee container-fluid">` framing `Whatever you call her,` and `Choco Fruits` (*"Frida always had a way of making moments a little sweeter."*) with `#6f42c1` surface cards, `#d63384` accents, and `.fa-sm { font-size:.875em }`.
5. **Colophon & Global Directory Footer (<footer.wp-singular> — `https://myfrida.com/`)**:
   - Landmark `<footer class="wp-singular">` anchoring `My Frida · Chocolate-Covered Fru` footer links (`Meet Frida · Contact us`), copy *"Frida always had a way of"*, and `#fd7e14` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: myfrida-com (My Frida · Chocolate-Covered Fruit, Smoothies & Cake Bars)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `myfrida-com` (**My Frida · Chocolate-Covered Fruit, Smoothies & Cake Bars** — `https://myfrida.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#0d6efd` canvas, `#6610f2` ink, `#d63384` accent).
- **Identity & Domain Context**: Discover My Frida: real fruit wrapped in chocolate, fruity Choco Smoothies, frozen treats and layered Fridika Cake Bars. Find your favour...
- **Primary Substrate**: `#0d6efd` (`var(--bs-blue)` in `:root`), **Primary Ink**: `#6610f2`, **Accent / Highlight**: `#d63384`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#0d6efd` (`var(--bs-blue)` in `:root`) paired with `#6610f2` primary typography and `#d63384` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Josefin Sans` for display copy (`Fresh fruit covered in chocolate`) with `Source Sans Pro` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `540px` container bounds (`gap: 1rem`, padding `2rem`) with `cubic-bezier(0.22,1,0.36,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `myfrida-com` in your global stylesheet:

:root {
  /* My Frida · Chocolate-Covered Fruit, Smoothies & Cake Bars (myfrida-com) — Ground-Truth Extracted CSS Variables */
  --bs-blue: #0d6efd; /* Color / Atmospheric Token (myfrida-com) */
  --bs-indigo: #6610f2; /* Color / Atmospheric Token (myfrida-com) */
  --bs-purple: #6f42c1; /* Color / Atmospheric Token (myfrida-com) */
  --bs-pink: #d63384; /* Typography Ink Token (myfrida-com) */
  --bs-red: #dc3545; /* Color / Atmospheric Token (myfrida-com) */
  --bs-orange: #fd7e14; /* Color / Atmospheric Token (myfrida-com) */
  --bs-yellow: #ffc107; /* Color / Atmospheric Token (myfrida-com) */
  --bs-green: #198754; /* Color / Atmospheric Token (myfrida-com) */
  --bs-teal: #20c997; /* Color / Atmospheric Token (myfrida-com) */
  --bs-cyan: #0dcaf0; /* Color / Atmospheric Token (myfrida-com) */
  --bs-black: #000; /* Canvas / Surface Token (myfrida-com) */
  --bs-white: #fff; /* Canvas / Surface Token (myfrida-com) */
  --bs-gray: #6c757d; /* Color / Atmospheric Token (myfrida-com) */
  --bs-gray-dark: #343a40; /* Canvas / Surface Token (myfrida-com) */
  --bs-gray-100: #f8f9fa; /* Color / Atmospheric Token (myfrida-com) */
  --bs-gray-200: #e9ecef; /* Color / Atmospheric Token (myfrida-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#0d6efd` — grounded in `var(--bs-blue)` in `:root`
- **Primary Typography Ink**: `#6610f2` — grounded in `var(--bs-indigo)` in `:root`
- **Elevated Surface / Card Substrate**: `#6f42c1` — grounded in `var(--bs-purple)` in `:root`
- **Interactive Accent / Highlight**: `#d63384` — grounded in `var(--bs-pink)` in `:root`
- **Secondary / Muted Copy**: `#dc3545` — grounded in `var(--bs-red)` in `:root`
- **Structural Hairline Border**: `#fd7e14` — grounded in `var(--bs-orange)` in `:root`
- **Variable Token (`--bs-yellow`)**: `#ffc107` — grounded in `var(--bs-yellow)` in `:root`
- **Variable Token (`--bs-green`)**: `#198754` — grounded in `var(--bs-green)` in `:root`
- **Variable Token (`--bs-teal`)**: `#20c997` — grounded in `var(--bs-teal)` in `:root`
- **Variable Token (`--bs-cyan`)**: `#0dcaf0` — grounded in `var(--bs-cyan)` in `:root`
- **Variable Token (`--bs-black`)**: `#000` — grounded in `var(--bs-black)` in `:root`
- **Variable Token (`--bs-white`)**: `#fff` — grounded in `var(--bs-white)` in `:root`
- **Variable Token (`--bs-gray`)**: `#6c757d` — grounded in `var(--bs-gray)` in `:root`
- **Variable Token (`--bs-gray-dark`)**: `#343a40` — grounded in `var(--bs-gray-dark)` in `:root`
- **Variable Token (`--bs-gray-100`)**: `#f8f9fa` — grounded in `var(--bs-gray-100)` in `:root`
- **Variable Token (`--bs-gray-200`)**: `#e9ecef` — grounded in `var(--bs-gray-200)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×7118px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `540px` extracted from `myfrida-com` stylesheet
- **Padding & Gutters**: `2rem` lateral canvas padding with `1rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 540px`, `gap: 1rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `2rem` horizontal padding
- **Media Queries**: `@media (min-width:1200px)`, `@media (min-width:576px)`, `@media (min-width:768px)`, `@media (min-width:992px)`
- **Corner Radii**: `0.375rem`, `.25rem`, `var(--bs-border-radius)`, `var(--bs-border-radius-sm)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Josefin Sans`
- **Body Font Stack**: `Source Sans Pro`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: rule `,.h1` (`line-height: 1.2`, `font-weight: 500`)
- **H2 Section Rule**: rule `,.h2` (`font-size: calc(1.325rem + 0.9vw)`)
- **Body Copy Rule**: CSS variables `--bs-body-font-family: var(--bs-font-sans-serif)`, `--bs-body-font-size: 1rem`, `--bs-body-font-weight: 400`; rule `p` (`font-size: min(1vw,20px)`, `line-height: 1.2`, `font-weight: 400`)
- **Metadata & Index Rule**: CSS variables `--bs-carousel-caption-color: #000`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `myfrida-com` (`My Frida · Chocolate-Covered Fruit, Smoothies & Cake Bars`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.webp> — `myfrida-com`)**:
   - DOM & Selectors: Landmark `<header class="webp">` hosting `My Frida · Chocolate-Covered Fruit, ` navigation (`Meet Frida · Contact us`), DOM attributes (`data-smush-preload`, `data-rocket-prefetch`, `data-rocket-preload`, `data-minify="1"`), and stylesheet rule `.fa-lg { font-size:1.33333em;line-height:.75em;vertical-align:-.0667em }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.webp> — `myfrida-com`)` (`myfrida-com`) adapts across `@media (min-width:1200px)`, `@media (min-width:576px)`, `@media (min-width:768px)`, `@media (min-width:992px)` with `cubic-bezier(0.22,1,0.36,1)`, `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(0,0,0.2,1)` transitions and links `Meet Frida · Contact us`.
2. **Hero Stage & Focal Lead (<section.tf-hero> — `Fresh fruit covered in chocolate`)**:
   - DOM & Selectors: Landmark `<section class="tf-hero">` presenting display lead `Fresh fruit covered in chocolate` and copy excerpt *"Choco Fruits Frozen"* over `#0d6efd` canvas and `#6610f2` ink.
   - Responsive Contract: Hero stage (`1440×7118px` desktop / `390×2400px` mobile) sets `#0d6efd` background with `#6610f2` headline `Fresh fruit covered in chocolate`.
3. **Primary Showcase & Content Grid (<section.tf-uvod> — `My Frida my moment`)**:
   - DOM & Selectors: Landmark `<section class="tf-uvod container-fluid">` rendering section `My Frida my moment` with copy *"Choco Fruits Frozen ›"*, asset references (`myfrida-hero-frozen-1200.webp`, `b4751355.assetcdn.net`, `myfrida-source-sans-pro-400-latin...`, `myfrida-josefin-sans-700-latin.woff2`), and grid rule `.fa-xs { font-size:.75em }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.tf-uvod> — `My Frida my moment`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 540px`, `gap: 1rem`) on desktop and Single-column vertical stack at `390px` viewport width with `2rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.tf-marquee> — `Whatever you call her,`)**:
   - DOM & Selectors: Landmark `<section class="tf-marquee container-fluid">` framing `Whatever you call her,` and `Choco Fruits` (*"Frida always had a way of making moments a little sweeter."*) with `#6f42c1` surface cards, `#d63384` accents, and `.fa-sm { font-size:.875em }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.tf-marquee> — `Whatever you call her,`)` uses `0.375rem`, `.25rem`, `var(--bs-border-radius)`, `var(--bs-border-radius-sm)` radii, `#d63384` highlights, and assets (myfrida-hero-frozen-1200.webp, b4751355.assetcdn.net, myfrida-source-sans-pro-400-latin...).
5. **Colophon & Global Directory Footer (<footer.wp-singular> — `https://myfrida.com/`)**:
   - DOM & Selectors: Landmark `<footer class="wp-singular">` anchoring `My Frida · Chocolate-Covered Fru` footer links (`Meet Frida · Contact us`), copy *"Frida always had a way of"*, and `#fd7e14` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.wp-singular> — `https://myfrida.com/`)` aligns to `540px` extracted from `myfrida-com` stylesheet with `2rem` lateral canvas padding with `1rem` grid gap and attributes (data-smush-preload, data-rocket-prefetch, data-rocket-preload).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Choco Fruits Frozen"*
- Copy Excerpt 2: *"Choco Fruits Frozen ›"*
- Copy Excerpt 3: *"Frida always had a way of making moments a little sweeter."*
- Copy Excerpt 4: *"Frida always had a way of"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.22,1,0.36,1)`, `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(0,0,0.2,1)`
- **Extracted Stylesheet Rules (`myfrida-com`)**:
- `.fa-lg { font-size:1.33333em;line-height:.75em;vertical-align:-.0667em }`
- `.fa-xs { font-size:.75em }`
- `.fa-sm { font-size:.875em }`
- `.fa-1x { font-size:1em }`
- `.fa-2x { font-size:2em }`
- **Per-Selector Transition Rules**:
- **Selector `.widget_archive select`**: `transition: border-color .15s ease-in-out,box-shadow .15s ease-in-out` extracted from `myfrida-com` stylesheet.
- **Selector `widget_archive select::file-selec...`**: `transition: color .15s ease-in-out,background-color .15s ease-in-out,borde...` extracted from `myfrida-com` stylesheet.
- **Selector `.select2-selection`**: `transition: border-color .15s ease-in-out,box-shadow .15s ease-in-out` extracted from `myfrida-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.22,1,0.36,1)`)**: Governs interactive state transitions across `<header.webp>` and `<section.tf-uvod>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `myfrida-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
