---
title: "UI Prompt Blueprint: davaris-gr"
date: 2026-11-24
captured_at: 2026-11-24
target: "davaris-gr"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
capture_mode: behavioral_journey_v2
asset_format: webp
scroll_driver: native
desktop_keyframes: 8
subpages_crawled: 3
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#f5f2e5` canvas, `#2e1414` ink, `#f65f00` accent)"
---

# UI Design System & Master Generation Blueprint: davaris-gr

> **Homepage - Davaris** (https://davaris.gr/) — We are a family-owned company built on heritage, excellence, and a human-centric approach. Taking all the necessary steps for the protect...

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Homepage - Davaris** (`https://davaris.gr/`). We are a family-owned company built on heritage, excellence, and a human-centric approach. Taking all the necessary steps for the protect...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#f5f2e5` canvas, `#2e1414` ink, `#f65f00` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f5f2e5` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#2e1414` primary typography and `#f65f00` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Moderat Extended` for display copy (`Fashion textiles that inspire`) with `Moderat` and `Moderat Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1340px` container bounds (`gap: 1rem`, padding `50px`) with `cubic-bezier(.7,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=9970px` / doc `10870px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `1340px` (measured `<main>` bounding box width within `1440px` desktop viewport).
- **Canvas Lateral Padding & Spacing**: `50px` lateral canvas padding with `1rem` grid gap.
- **Border Radius Scale**: `50%`, `.375rem`, `.25rem`, `var(--bs-border-radius)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1340px`, `gap: 1rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `50px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:1023.98px)`, `@media (prefers-reduced-motion:no-preference)`, `@media (min-width:1200px)`, `@media (min-width:576px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f5f2e5` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#2e1414` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#dddddd` | `var(--wp-editor-canvas-background)` in `:root` |
| **Interactive Accent / Highlight** | `#f65f00` | `var(--bs-link-color)` in `:root` |
| **Secondary / Muted Copy** | `#6c757d` | `var(--bs-secondary)` in `:root` |
| **Structural Hairline Border** | `#e9ecef` | `var(--bs-light-border-subtle)` in `:root` |
| **Variable Token (`--wp-block-synced-color`)** | `#7a00df` | `var(--wp-block-synced-color)` in `:root` |
| **Variable Token (`--wp-admin-theme-color`)** | `#007cba` | `var(--wp-admin-theme-color)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-10`)** | `#006ba1` | `var(--wp-admin-theme-color-darker-10)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-20`)** | `#005a87` | `var(--wp-admin-theme-color-darker-20)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--wp-block-synced-color` | `#7a00df` | Brand / Palette Token |
| `--wp-block-synced-color--rgb` | `122,0,223` | Brand / Palette Token |
| `--wp-bound-block-color` | `var(--wp-block-synced-color)` | Brand / Palette Token |
| `--wp-editor-canvas-background` | `#ddd` | Canvas / Surface Token |
| `--wp-admin-theme-color` | `#007cba` | Brand / Palette Token |
| `--wp-admin-theme-color--rgb` | `0,124,186` | Brand / Palette Token |
| `--wp-admin-theme-color-darker-10` | `#006ba1` | Canvas / Surface Token |
| `--wp-admin-theme-color-darker-10--rgb` | `0,107,160.5` | Canvas / Surface Token |
| `--wp-admin-theme-color-darker-20` | `#005a87` | Canvas / Surface Token |
| `--wp-admin-theme-color-darker-20--rgb` | `0,90,135` | Canvas / Surface Token |
| `--wp-admin-border-width-focus` | `2px` | Layout / Spatial Grid Token |
| `--wp-admin--admin-bar--position-offset` | `var(--wp-admin--admin-bar--height,0px)` | Dimension / Scale Token |
| `--space-xs` | `clamp(1rem, 2.2vw, 2.65rem)` | Layout / Spatial Grid Token |
| `--space-sm` | `clamp(1.875rem, 4.43vw, 5.3125rem)` | Layout / Spatial Grid Token |
| `--space-md` | `clamp(2.5rem, 6.5vw, 7.8125rem)` | Layout / Spatial Grid Token |
| `--space-lg` | `clamp(3.75rem, 8.85vw, 10.625rem)` | Layout / Spatial Grid Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Moderat Extended`.
- **Primary Body Stack**: `Moderat`.
- **Technical / Metadata Stack**: `Moderat Mono`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 90px`, `line-height: 81px`, `font-weight: 500`, `letter-spacing: -1.8px`); CSS variables `--fs-h1: clamp(3.75rem, 3.09rem + 2.817vw, 5.625rem)`, `--lh-h1: .9`; rule `,.h1` (`line-height: 1.2`, `font-weight: 500`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 45.008px`, `line-height: 45.008px`, `font-weight: 500`); CSS variables `--fs-h2: clamp(2.125rem, 1.4rem + 3.6vw, 4.688rem)`, `--lh-h2: 1`; rule `,.h2` (`font-size: calc(1.325rem + .9vw)`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 17.6px`, `font-weight: 400`); CSS variables `--bs-body-font-family: var(--bs-font-sans-serif)`, `--bs-body-font-size: 1rem`, `--bs-body-font-weight: 400`; rule `p` (`font-size: 1.125rem`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 17.6px`, `font-weight: 400`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.7,0,.2,1)`, `cubic-bezier(0,.3,.4,1)`, `cubic-bezier(.19,1,.22,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.btn`**: `transition: color .15s ease-in-out,background-color .15s ease-in-out,borde...` extracted from `davaris-gr` stylesheet.
- **Selector `media(prefers-reduced-motion:reduce)`**: `transition: none` extracted from `davaris-gr` stylesheet.
- **Selector `.form-control`**: `transition: border-color .15s ease-in-out,box-shadow .15s ease-in-out` extracted from `davaris-gr` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.7,0,.2,1)`)**: Governs interactive state transitions across `<header.site-header>` and `<section.scrolled-text>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `10870px`, deepest scrollY reached `9970px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: `Lenis`, `GSAP/ScrollTrigger`.
- **Nav / Drawer Probe (`Open menu`)**: Triggered visual change (pixel diff `81.842`, captured in `assets/state-nav.webp`); revealed links: Home, Collections, About Us, 62 ERMOU STR, 144 52..., SUPPORT@DAVARIS.GR.
- **Hover Physics (`primary_cta` · `E-SHOWROOM E-SHOWROOM`)**: Computed transition `0.4s` / `cubic-bezier(0.19, 1, 0.22, 1)` (no static color/transform shift captured at rest).
- **Route Transition Architecture**: First internal navigation (`/collections/plain/`) measured as `direct` in `1757ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Homepage - Davaris                         │
│ ====================================================================== │
│ [ <header.site-header> (1440x72px)    | Overview · Index · Archive · ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero> (w=1340px)                              | │
│ | H1: Fashion textiles that inspire                                  | │
│ | Substrate: #f5f2e5 | Ink: #2e1414 | Accent: #f65f00                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.scrolled-text>) max-w: 1340px              | │
│ | +------------------------------+  +------------------------------+ | │
│ | | We are a family-owned compan |  | Plain Collection             | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.collections-media) — Fancy Collection      | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.nav-primary_) | https://davaris.gr/                  │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 1rem)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.site-header>    ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.hero>) — 390px Vertical Lead                  | │
│ | H1: Fashion textiles that inspire                                  | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.scrolled-text) — 1-Col Stack              | │
│ | [ Item 1: We are a family-owned company built on heritage,...    ] | │
│ | [ Item 2: Plain Collection                                       ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.collections-med) — 1-Col (Fancy Collection) | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.nav-primary_) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.site-header> — `davaris-gr`)**:
   - Landmark `<header class="site-header">` (`1440x72px`) hosting `Homepage - Davaris` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-cfasync="false"`, `data-no-minify="true"`, `data-no-optimize="1"`, `data-noptimize="1"`), and stylesheet rule `.flickity-enabled { position:relative }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Fashion textiles that inspire`)**:
   - Landmark `<section class="hero hero--video">` presenting display lead `Fashion textiles that inspire` and copy excerpt *"62 Ermou Str, 144 52 Metamorfosi, Greece"* over `#f5f2e5` canvas and `#2e1414` ink.
3. **Primary Showcase & Content Grid (<section.scrolled-text> — `We are a family-owned company buil`)**:
   - Landmark `<section class="scrolled-text u-escape-container">` rendering section `We are a family-owned company built on heritage,...` with copy *"TEXTILE EXCELLENCE"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `.flickity-enabled:focus { outline:none }`.
4. **Interactive Detail & Feature Matrix (<section.collections-media> — `Plain Collection`)**:
   - Landmark `<section class="collections-media u-escape-container">` framing `Plain Collection` and `Fancy Collection` (*"We are a family-owned company built on heritage, excellence, and "*) with `#dddddd` surface cards, `#f65f00` accents, and `.flickity-viewport { overflow:hidden;position:relative;height:100%;touch-action:pan-y }`.
5. **Colophon & Global Directory Footer (<footer.nav-primary__footer> — `https://davaris.gr/`)**:
   - Landmark `<footer class="nav-primary__footer">` anchoring `Homepage - Davaris` footer links (`Overview · Index · Archive · About · Contact`), copy *"Premium fabrics crafted for elegance, versatility, and super"*, and `#e9ecef` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `MENU` · sticky/fixed elements: `3`
- **Step 02** (`y=850px`, `9%`): Active landmark `We are a family-owned company built on heritage,...` · sticky/fixed elements: `3`
- **Step 03** (`y=2550px`, `26%`): Active landmark `MENU` · sticky/fixed elements: `3`
- **Step 04** (`y=4250px`, `43%`): Active landmark `A leading creative partner of the women's fashion...` · sticky/fixed elements: `2`
- **Step 05** (`y=5950px`, `60%`): Active landmark `MENU` · sticky/fixed elements: `3`
- **Step 06** (`y=7650px`, `77%`): Active landmark `We are committed to creating high-quality textile...` · sticky/fixed elements: `2`
- **Step 07** (`y=9350px`, `94%`): Active landmark `MENU` · sticky/fixed elements: `2`
- **Step 08** (`y=9970px`, `100%`): Active landmark `MENU` · sticky/fixed elements: `2`

### Multi-Page Internal Route Map
- **Detail Route (`/collections/plain/`)**: `https://davaris.gr/collections/plain/` — H1: `Plain - Davaris`, scrollHeight `7142px`, transition `direct` (`1757ms`)
- **About Route (`/company/`)**: `https://davaris.gr/company/` — H1: `Company - Davaris`, scrollHeight `10691px`, transition `direct` (`903ms`)
- **Detail Route (`/collections/fancy/`)**: `https://davaris.gr/collections/fancy/` — H1: `Fancy - Davaris`, scrollHeight `6585px`, transition `direct` (`347ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: davaris-gr (Homepage - Davaris)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `davaris-gr` (**Homepage - Davaris** — `https://davaris.gr/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#f5f2e5` canvas, `#2e1414` ink, `#f65f00` accent).
- **Identity & Domain Context**: We are a family-owned company built on heritage, excellence, and a human-centric approach. Taking all the necessary steps for the protect...
- **Primary Substrate**: `#f5f2e5` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#2e1414`, **Accent / Highlight**: `#f65f00`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f5f2e5` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#2e1414` primary typography and `#f65f00` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Moderat Extended` for display copy (`Fashion textiles that inspire`) with `Moderat` and `Moderat Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1340px` container bounds (`gap: 1rem`, padding `50px`) with `cubic-bezier(.7,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `davaris-gr` in your global stylesheet:

:root {
  /* Homepage - Davaris (davaris-gr) — Live-Grounded CSS Variables */
  --wp-block-synced-color: #7a00df; /* Brand / Palette Token (davaris-gr) */
  --wp-block-synced-color--rgb: 122,0,223; /* Brand / Palette Token (davaris-gr) */
  --wp-bound-block-color: var(--wp-block-synced-color); /* Brand / Palette Token (davaris-gr) */
  --wp-editor-canvas-background: #ddd; /* Canvas / Surface Token (davaris-gr) */
  --wp-admin-theme-color: #007cba; /* Brand / Palette Token (davaris-gr) */
  --wp-admin-theme-color--rgb: 0,124,186; /* Brand / Palette Token (davaris-gr) */
  --wp-admin-theme-color-darker-10: #006ba1; /* Canvas / Surface Token (davaris-gr) */
  --wp-admin-theme-color-darker-10--rgb: 0,107,160.5; /* Canvas / Surface Token (davaris-gr) */
  --wp-admin-theme-color-darker-20: #005a87; /* Canvas / Surface Token (davaris-gr) */
  --wp-admin-theme-color-darker-20--rgb: 0,90,135; /* Canvas / Surface Token (davaris-gr) */
  --wp-admin-border-width-focus: 2px; /* Layout / Spatial Grid Token (davaris-gr) */
  --wp-admin--admin-bar--position-offset: var(--wp-admin--admin-bar--height,0px); /* Dimension / Scale Token (davaris-gr) */
  --space-xs: clamp(1rem, 2.2vw, 2.65rem); /* Layout / Spatial Grid Token (davaris-gr) */
  --space-sm: clamp(1.875rem, 4.43vw, 5.3125rem); /* Layout / Spatial Grid Token (davaris-gr) */
  --space-md: clamp(2.5rem, 6.5vw, 7.8125rem); /* Layout / Spatial Grid Token (davaris-gr) */
  --space-lg: clamp(3.75rem, 8.85vw, 10.625rem); /* Layout / Spatial Grid Token (davaris-gr) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f5f2e5` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#2e1414` — grounded in live computed `main` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#dddddd` — grounded in `var(--wp-editor-canvas-background)` in `:root`
- **Interactive Accent / Highlight**: `#f65f00` — grounded in `var(--bs-link-color)` in `:root`
- **Secondary / Muted Copy**: `#6c757d` — grounded in `var(--bs-secondary)` in `:root`
- **Structural Hairline Border**: `#e9ecef` — grounded in `var(--bs-light-border-subtle)` in `:root`
- **Variable Token (`--wp-block-synced-color`)**: `#7a00df` — grounded in `var(--wp-block-synced-color)` in `:root`
- **Variable Token (`--wp-admin-theme-color`)**: `#007cba` — grounded in `var(--wp-admin-theme-color)` in `:root`
- **Variable Token (`--wp-admin-theme-color-darker-10`)**: `#006ba1` — grounded in `var(--wp-admin-theme-color-darker-10)` in `:root`
- **Variable Token (`--wp-admin-theme-color-darker-20`)**: `#005a87` — grounded in `var(--wp-admin-theme-color-darker-20)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `1340px` (measured `<main>` bounding box width within `1440px` desktop viewport)
- **Padding & Gutters**: `50px` lateral canvas padding with `1rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1340px`, `gap: 1rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `50px` horizontal padding
- **Media Queries**: `@media (max-width:1023.98px)`, `@media (prefers-reduced-motion:no-preference)`, `@media (min-width:1200px)`, `@media (min-width:576px)`
- **Corner Radii**: `50%`, `.375rem`, `.25rem`, `var(--bs-border-radius)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Moderat Extended`
- **Body Font Stack**: `Moderat`
- **Monospace / Technical Font Stack**: `Moderat Mono`
- **H1 Display Rule**: live computed `h1` (`font-size: 90px`, `line-height: 81px`, `font-weight: 500`, `letter-spacing: -1.8px`); CSS variables `--fs-h1: clamp(3.75rem, 3.09rem + 2.817vw, 5.625rem)`, `--lh-h1: .9`; rule `,.h1` (`line-height: 1.2`, `font-weight: 500`)
- **H2 Section Rule**: live computed `h2` (`font-size: 45.008px`, `line-height: 45.008px`, `font-weight: 500`); CSS variables `--fs-h2: clamp(2.125rem, 1.4rem + 3.6vw, 4.688rem)`, `--lh-h2: 1`; rule `,.h2` (`font-size: calc(1.325rem + .9vw)`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 17.6px`, `font-weight: 400`); CSS variables `--bs-body-font-family: var(--bs-font-sans-serif)`, `--bs-body-font-size: 1rem`, `--bs-body-font-weight: 400`; rule `p` (`font-size: 1.125rem`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 17.6px`, `font-weight: 400`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `davaris-gr` (`Homepage - Davaris`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.site-header> — `davaris-gr`)**:
   - DOM & Selectors: Landmark `<header class="site-header">` (`1440x72px`) hosting `Homepage - Davaris` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-cfasync="false"`, `data-no-minify="true"`, `data-no-optimize="1"`, `data-noptimize="1"`), and stylesheet rule `.flickity-enabled { position:relative }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.site-header> — `davaris-gr`)` (`davaris-gr`) adapts across `@media (max-width:1023.98px)`, `@media (prefers-reduced-motion:no-preference)`, `@media (min-width:1200px)`, `@media (min-width:576px)` with `cubic-bezier(.7,0,.2,1)`, `cubic-bezier(0,.3,.4,1)`, `cubic-bezier(.19,1,.22,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<section.hero> — `Fashion textiles that inspire`)**:
   - DOM & Selectors: Landmark `<section class="hero hero--video">` presenting display lead `Fashion textiles that inspire` and copy excerpt *"62 Ermou Str, 144 52 Metamorfosi, Greece"* over `#f5f2e5` canvas and `#2e1414` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×2616px` mobile) sets `#f5f2e5` background with `#2e1414` headline `Fashion textiles that inspire`.
3. **Primary Showcase & Content Grid (<section.scrolled-text> — `We are a family-owned company buil`)**:
   - DOM & Selectors: Landmark `<section class="scrolled-text u-escape-container">` rendering section `We are a family-owned company built on heritage,...` with copy *"TEXTILE EXCELLENCE"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `.flickity-enabled:focus { outline:none }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.scrolled-text> — `We are a family-owned company buil`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1340px`, `gap: 1rem`) on desktop and Single-column vertical stack at `390px` viewport width with `50px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.collections-media> — `Plain Collection`)**:
   - DOM & Selectors: Landmark `<section class="collections-media u-escape-container">` framing `Plain Collection` and `Fancy Collection` (*"We are a family-owned company built on heritage, excellence, and "*) with `#dddddd` surface cards, `#f65f00` accents, and `.flickity-viewport { overflow:hidden;position:relative;height:100%;touch-action:pan-y }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.collections-media> — `Plain Collection`)` uses `50%`, `.375rem`, `.25rem`, `var(--bs-border-radius)` radii, `#f65f00` highlights, and assets (favicon.ico, favicon.svg, apple-touch-icon.png).
5. **Colophon & Global Directory Footer (<footer.nav-primary__footer> — `https://davaris.gr/`)**:
   - DOM & Selectors: Landmark `<footer class="nav-primary__footer">` anchoring `Homepage - Davaris` footer links (`Overview · Index · Archive · About · Contact`), copy *"Premium fabrics crafted for elegance, versatility, and super"*, and `#e9ecef` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.nav-primary__footer> — `https://davaris.gr/`)` aligns to `1340px` (measured `<main>` bounding box width within `1440px` desktop viewport) with `50px` lateral canvas padding with `1rem` grid gap and attributes (data-cfasync="false", data-no-minify="true", data-no-optimize="1").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"62 Ermou Str, 144 52 Metamorfosi, Greece"*
- Copy Excerpt 2: *"TEXTILE EXCELLENCE"*
- Copy Excerpt 3: *"We are a family-owned company built on heritage, excellence, and a human-centric a..."*
- Copy Excerpt 4: *"Premium fabrics crafted for elegance, versatility, and superior quality."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.7,0,.2,1)`, `cubic-bezier(0,.3,.4,1)`, `cubic-bezier(.19,1,.22,1)`
- **Extracted Stylesheet Rules (`davaris-gr`)**:
- `.flickity-enabled { position:relative }`
- `.flickity-enabled:focus { outline:none }`
- `.flickity-viewport { overflow:hidden;position:relative;height:100%;touch-action:pan-y }`
- `.flickity-slider { position:absolute;width:100%;height:100%;left:0 }`
- `.flickity-rtl .flickity-slider { left:unset;right:0 }`
- **Per-Selector Transition Rules**:
- **Selector `.btn`**: `transition: color .15s ease-in-out,background-color .15s ease-in-out,borde...` extracted from `davaris-gr` stylesheet.
- **Selector `media(prefers-reduced-motion:reduce)`**: `transition: none` extracted from `davaris-gr` stylesheet.
- **Selector `.form-control`**: `transition: border-color .15s ease-in-out,box-shadow .15s ease-in-out` extracted from `davaris-gr` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.7,0,.2,1)`)**: Governs interactive state transitions across `<header.site-header>` and `<section.scrolled-text>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `10870px` across 8 distinct viewport chapters using Lenis, GSAP/ScrollTrigger.
- **Vertical Chapter Sequence**: MENU (0%) -> We are a family-owned compa... (9%) -> MENU (26%) -> A leading creative partner... (43%) -> MENU (60%) -> We are committed to creatin... (77%) -> MENU (94%) -> MENU (100%).
- **Navigation Drawer / Menu State**: Replicate interactive menu toggle (`Open menu`) with Escape-to-close keyboard handling.
- **Multi-Page Routes**: Scaffold internal routes `/collections/plain/` (detail, direct), `/company/` (about, direct), `/collections/fancy/` (detail, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `davaris-gr`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | MENU | `3` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `9%` | We are a family-owned company built on herita... | `3` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `2550px` | `26%` | MENU | `3` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `4250px` | `43%` | A leading creative partner of the women's fas... | `2` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `5950px` | `60%` | MENU | `3` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `7650px` | `77%` | We are committed to creating high-quality tex... | `2` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `9350px` | `94%` | MENU | `2` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `9970px` | `100%` | MENU | `2` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | MENU | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `4436px` | `50%` | MENU | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `8873px` | `100%` | MENU | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Interactive UI State Captures (`1440×900` WebP)
| State Type | Trigger / Observation | Visual Asset |
| :--- | :--- | :--- |
| `nav_menu` | Nav/Menu opened (`Open menu`, diff `81.842`) | [state-nav.webp](assets/state-nav.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `detail` | `https://davaris.gr/collections/plain/` | Plain - Davaris | `7142px` | `direct` (`1757ms`) | [subpage-01-collections-plain.webp](assets/subpage-01-collections-plain.webp) |
| `2` | `about` | `https://davaris.gr/company/` | Company - Davaris | `10691px` | `direct` (`903ms`) | [subpage-02-company.webp](assets/subpage-02-company.webp) |
| `3` | `detail` | `https://davaris.gr/collections/fancy/` | Fancy - Davaris | `6585px` | `direct` (`347ms`) | [subpage-03-collections-fancy.webp](assets/subpage-03-collections-fancy.webp) |

