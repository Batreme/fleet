---
title: "UI Prompt Blueprint: myfrida-com"
date: 2026-11-23
captured_at: 2026-11-23
target: "myfrida-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#020a0a` ink, `#0d6efd` accent)"
---

# UI Design System & Master Generation Blueprint: myfrida-com

> **My Frida · Chocolate-Covered Fruit, Smoothies & Cake Bars** (https://myfrida.com/) — Discover My Frida: real fruit wrapped in chocolate, fruity Choco Smoothies, frozen treats and layered Fridika Cake Bars. Find your favour...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **My Frida · Chocolate-Covered Fruit, Smoothies & Cake Bars** (`https://myfrida.com/`). Discover My Frida: real fruit wrapped in chocolate, fruity Choco Smoothies, frozen treats and layered Fridika Cake Bars. Find your favour...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#020a0a` ink, `#0d6efd` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#020a0a` primary typography and `#0d6efd` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Source Sans Pro` for display copy (`My Frida my moment`) with `Source Sans Pro` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1320px` container bounds (`gap: 48px`, padding `2rem`) with `cubic-bezier(0.22,1,0.36,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1320px` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `2rem` lateral canvas padding with `48px` grid gap.
- **Border Radius Scale**: `0.375rem`, `.25rem`, `var(--bs-border-radius)`, `var(--bs-border-radius-sm)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1320px`, `gap: 48px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `2rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:1200px)`, `@media (min-width:576px)`, `@media (min-width:768px)`, `@media (min-width:992px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#020a0a` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f8f9fa` | `var(--bs-tertiary-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#0d6efd` | `var(--bs-primary)` in `:root` |
| **Secondary / Muted Copy** | `#6c757d` | `var(--bs-secondary)` in `:root` |
| **Structural Hairline Border** | `#9ec5fe` | `var(--bs-primary-border-subtle)` in `:root` |
| **Variable Token (`--bs-indigo`)** | `#6610f2` | `var(--bs-indigo)` in `:root` |
| **Variable Token (`--bs-purple`)** | `#6f42c1` | `var(--bs-purple)` in `:root` |
| **Variable Token (`--bs-pink`)** | `#d63384` | `var(--bs-pink)` in `:root` |
| **Variable Token (`--bs-red`)** | `#dc3545` | `var(--bs-red)` in `:root` |
| **Variable Token (`--bs-orange`)** | `#fd7e14` | `var(--bs-orange)` in `:root` |
| **Variable Token (`--bs-yellow`)** | `#ffc107` | `var(--bs-yellow)` in `:root` |
| **Variable Token (`--bs-green`)** | `#198754` | `var(--bs-green)` in `:root` |
| **Variable Token (`--bs-teal`)** | `#20c997` | `var(--bs-teal)` in `:root` |
| **Variable Token (`--bs-cyan`)** | `#0dcaf0` | `var(--bs-cyan)` in `:root` |
| **Variable Token (`--bs-black`)** | `#000000` | `var(--bs-black)` in `:root` |
| **Variable Token (`--bs-gray-dark`)** | `#343a40` | `var(--bs-gray-dark)` in `:root` |
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
- **Display Typography**: `Source Sans Pro`.
- **Primary Body Stack**: `Source Sans Pro`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 40px`, `line-height: 48px`, `font-weight: 900`); rule `,.h1` (`line-height: 1.2`, `font-weight: 500`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 110.16px`, `line-height: 92.8649px`, `font-weight: 900`); rule `,.h2` (`font-size: calc(1.325rem + 0.9vw)`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--bs-body-font-family: var(--bs-font-sans-serif)`, `--bs-body-font-size: 1rem`, `--bs-body-font-weight: 400`; rule `p` (`font-size: min(1vw,20px)`, `line-height: 1.2`, `font-weight: 400`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`).

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

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — My Frida · Chocolate-Covered Fruit, Smooth │
│ ====================================================================== │
│ [ <header.webp> (1440x114px)          | Meet Frida · Contact us      ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.tf-hero> (w=1440px)                           | │
│ | H1: My Frida my moment                                             | │
│ | Substrate: #ffffff | Ink: #020a0a | Accent: #0d6efd                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.tf-uvod>) max-w: 1320px                    | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Whatever you call her,       |  | Choco Fruits                 | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.tf-marquee>) — Choco Smoothies             | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.home>       ) | https://myfrida.com/                 │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 48px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.webp>           ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.tf-hero>) — 390px Vertical Lead               | │
│ | H1: My Frida my moment                                             | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.tf-uvod>) — 1-Col Stack                   | │
│ | [ Item 1: Whatever you call her,                                 ] | │
│ | [ Item 2: Choco Fruits                                           ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.tf-marquee>) — 1-Col (Choco Smoothies)      | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.home>       ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.webp> — `myfrida-com`)**:
   - Landmark `<header class="webp">` (`1440x114px`) hosting `My Frida · Chocolate-Covered Fruit, ` navigation (`Meet Frida · Contact us`), DOM attributes (`data-smush-preload`, `data-rocket-prefetch`, `data-rocket-preload`, `data-minify="1"`), and stylesheet rule `.fa-lg { font-size:1.33333em;line-height:.75em;vertical-align:-.0667em }`.
2. **Hero Stage & Focal Lead (<section.tf-hero> — `My Frida my moment`)**:
   - Landmark `<section class="tf-hero">` presenting display lead `My Frida my moment` and copy excerpt *"Frida always had a way of making moments a little sweeter."* over `#ffffff` canvas and `#020a0a` ink.
3. **Primary Showcase & Content Grid (<section.tf-uvod> — `Whatever you call her,`)**:
   - Landmark `<section class="tf-uvod container-fluid">` rendering section `Whatever you call her,` with copy *"Choco Fruits Frozen ›"*, asset references (`myfrida-hero-frozen-1200.webp`, `b4751355.assetcdn.net`, `www.googletagmanager.com`, `myfrida-source-sans-pro-400-latin...`), and grid rule `.fa-xs { font-size:.75em }`.
4. **Interactive Detail & Feature Matrix (<section.tf-marquee> — `Choco Fruits`)**:
   - Landmark `<section class="tf-marquee container-fluid">` framing `Choco Fruits` and `Choco Smoothies` (*"Frida always had a way of"*) with `#f8f9fa` surface cards, `#0d6efd` accents, and `.fa-sm { font-size:.875em }`.
5. **Colophon & Global Directory Footer (<footer.home> — `https://myfrida.com/`)**:
   - Landmark `<footer class="home">` anchoring `My Frida · Chocolate-Covered Fru` footer links (`Meet Frida · Contact us`), copy *"making moments a little sweeter."*, and `#9ec5fe` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: myfrida-com (My Frida · Chocolate-Covered Fruit, Smoothies & Cake Bars)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `myfrida-com` (**My Frida · Chocolate-Covered Fruit, Smoothies & Cake Bars** — `https://myfrida.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#020a0a` ink, `#0d6efd` accent).
- **Identity & Domain Context**: Discover My Frida: real fruit wrapped in chocolate, fruity Choco Smoothies, frozen treats and layered Fridika Cake Bars. Find your favour...
- **Primary Substrate**: `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#020a0a`, **Accent / Highlight**: `#0d6efd`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#020a0a` primary typography and `#0d6efd` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Source Sans Pro` for display copy (`My Frida my moment`) with `Source Sans Pro` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1320px` container bounds (`gap: 48px`, padding `2rem`) with `cubic-bezier(0.22,1,0.36,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `myfrida-com` in your global stylesheet:

:root {
  /* My Frida · Chocolate-Covered Fruit, Smoothies & Cake Bars (myfrida-com) — Live-Grounded CSS Variables */
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
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#020a0a` — grounded in live computed `main` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#f8f9fa` — grounded in `var(--bs-tertiary-bg)` in `:root`
- **Interactive Accent / Highlight**: `#0d6efd` — grounded in `var(--bs-primary)` in `:root`
- **Secondary / Muted Copy**: `#6c757d` — grounded in `var(--bs-secondary)` in `:root`
- **Structural Hairline Border**: `#9ec5fe` — grounded in `var(--bs-primary-border-subtle)` in `:root`
- **Variable Token (`--bs-indigo`)**: `#6610f2` — grounded in `var(--bs-indigo)` in `:root`
- **Variable Token (`--bs-purple`)**: `#6f42c1` — grounded in `var(--bs-purple)` in `:root`
- **Variable Token (`--bs-pink`)**: `#d63384` — grounded in `var(--bs-pink)` in `:root`
- **Variable Token (`--bs-red`)**: `#dc3545` — grounded in `var(--bs-red)` in `:root`
- **Variable Token (`--bs-orange`)**: `#fd7e14` — grounded in `var(--bs-orange)` in `:root`
- **Variable Token (`--bs-yellow`)**: `#ffc107` — grounded in `var(--bs-yellow)` in `:root`
- **Variable Token (`--bs-green`)**: `#198754` — grounded in `var(--bs-green)` in `:root`
- **Variable Token (`--bs-teal`)**: `#20c997` — grounded in `var(--bs-teal)` in `:root`
- **Variable Token (`--bs-cyan`)**: `#0dcaf0` — grounded in `var(--bs-cyan)` in `:root`
- **Variable Token (`--bs-black`)**: `#000000` — grounded in `var(--bs-black)` in `:root`
- **Variable Token (`--bs-gray-dark`)**: `#343a40` — grounded in `var(--bs-gray-dark)` in `:root`
- **Variable Token (`--bs-gray-200`)**: `#e9ecef` — grounded in `var(--bs-gray-200)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1320px` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `2rem` lateral canvas padding with `48px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1320px`, `gap: 48px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `2rem` horizontal padding
- **Media Queries**: `@media (min-width:1200px)`, `@media (min-width:576px)`, `@media (min-width:768px)`, `@media (min-width:992px)`
- **Corner Radii**: `0.375rem`, `.25rem`, `var(--bs-border-radius)`, `var(--bs-border-radius-sm)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Source Sans Pro`
- **Body Font Stack**: `Source Sans Pro`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: live computed `h1` (`font-size: 40px`, `line-height: 48px`, `font-weight: 900`); rule `,.h1` (`line-height: 1.2`, `font-weight: 500`)
- **H2 Section Rule**: live computed `h2` (`font-size: 110.16px`, `line-height: 92.8649px`, `font-weight: 900`); rule `,.h2` (`font-size: calc(1.325rem + 0.9vw)`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--bs-body-font-family: var(--bs-font-sans-serif)`, `--bs-body-font-size: 1rem`, `--bs-body-font-weight: 400`; rule `p` (`font-size: min(1vw,20px)`, `line-height: 1.2`, `font-weight: 400`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `myfrida-com` (`My Frida · Chocolate-Covered Fruit, Smoothies & Cake Bars`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.webp> — `myfrida-com`)**:
   - DOM & Selectors: Landmark `<header class="webp">` (`1440x114px`) hosting `My Frida · Chocolate-Covered Fruit, ` navigation (`Meet Frida · Contact us`), DOM attributes (`data-smush-preload`, `data-rocket-prefetch`, `data-rocket-preload`, `data-minify="1"`), and stylesheet rule `.fa-lg { font-size:1.33333em;line-height:.75em;vertical-align:-.0667em }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.webp> — `myfrida-com`)` (`myfrida-com`) adapts across `@media (min-width:1200px)`, `@media (min-width:576px)`, `@media (min-width:768px)`, `@media (min-width:992px)` with `cubic-bezier(0.22,1,0.36,1)`, `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(0,0,0.2,1)` transitions and links `Meet Frida · Contact us`.
2. **Hero Stage & Focal Lead (<section.tf-hero> — `My Frida my moment`)**:
   - DOM & Selectors: Landmark `<section class="tf-hero">` presenting display lead `My Frida my moment` and copy excerpt *"Frida always had a way of making moments a little sweeter."* over `#ffffff` canvas and `#020a0a` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#ffffff` background with `#020a0a` headline `My Frida my moment`.
3. **Primary Showcase & Content Grid (<section.tf-uvod> — `Whatever you call her,`)**:
   - DOM & Selectors: Landmark `<section class="tf-uvod container-fluid">` rendering section `Whatever you call her,` with copy *"Choco Fruits Frozen ›"*, asset references (`myfrida-hero-frozen-1200.webp`, `b4751355.assetcdn.net`, `www.googletagmanager.com`, `myfrida-source-sans-pro-400-latin...`), and grid rule `.fa-xs { font-size:.75em }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.tf-uvod> — `Whatever you call her,`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1320px`, `gap: 48px`) on desktop and Single-column vertical stack at `390px` viewport width with `2rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.tf-marquee> — `Choco Fruits`)**:
   - DOM & Selectors: Landmark `<section class="tf-marquee container-fluid">` framing `Choco Fruits` and `Choco Smoothies` (*"Frida always had a way of"*) with `#f8f9fa` surface cards, `#0d6efd` accents, and `.fa-sm { font-size:.875em }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.tf-marquee> — `Choco Fruits`)` uses `0.375rem`, `.25rem`, `var(--bs-border-radius)`, `var(--bs-border-radius-sm)` radii, `#0d6efd` highlights, and assets (myfrida-hero-frozen-1200.webp, b4751355.assetcdn.net, www.googletagmanager.com).
5. **Colophon & Global Directory Footer (<footer.home> — `https://myfrida.com/`)**:
   - DOM & Selectors: Landmark `<footer class="home">` anchoring `My Frida · Chocolate-Covered Fru` footer links (`Meet Frida · Contact us`), copy *"making moments a little sweeter."*, and `#9ec5fe` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.home> — `https://myfrida.com/`)` aligns to `1320px` (non-`@media` desktop container stylesheet rule) with `2rem` lateral canvas padding with `48px` grid gap and attributes (data-smush-preload, data-rocket-prefetch, data-rocket-preload).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Frida always had a way of making moments a little sweeter."*
- Copy Excerpt 2: *"Choco Fruits Frozen ›"*
- Copy Excerpt 3: *"Frida always had a way of"*
- Copy Excerpt 4: *"making moments a little sweeter."*

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
