---
title: "UI Prompt Blueprint: montarville-ca"
date: 2026-11-23
captured_at: 2026-11-23
target: "montarville-ca"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#121212` canvas, `#fafafa` ink, `#d0112b` accent)"
---

# UI Design System & Master Generation Blueprint: montarville-ca

> **montarville · Une approche globale et intégrée dans la gestion de vos pr...** (https://montarville.ca/) — Un partenaire engagé. Une expertise reconnue. Une exécution maîtrisée. - Une approche globale et intégrée dans la gestion de vos projets...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **montarville · Une approche globale et intégrée dans la gestion de vos pr...** (`https://montarville.ca/`). Un partenaire engagé. Une expertise reconnue. Une exécution maîtrisée. - Une approche globale et intégrée dans la gestion de vos projets...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#121212` canvas, `#fafafa` ink, `#d0112b` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#121212` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#fafafa` primary typography and `#d0112b` accents.
  - **Grounded Typographic Hierarchy**: Pairs `General Sans` for display copy (`Un partenaire engagé. Une expertise `) with `General Sans` and `Fira Sans`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 1rem`, padding `1.5rem`) with `cubic-bezier(0.25,1,0.5,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport).
- **Canvas Lateral Padding & Spacing**: `1.5rem` lateral canvas padding with `1rem` grid gap.
- **Border Radius Scale**: `2px`, `1px`, `50%`, `var(--border-radius)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 1rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `1.5rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:1201px)`, `@media (max-width:1200px)`, `@media (max-width:750px)`, `@media (prefers-reduced-motion:reduce)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#121212` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#fafafa` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#d0112b` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#d0112b` | live computed `button` `background-color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#000000` | `var(--ff_wp_tracking_text_color)` in `:root` |
| **Structural Hairline Border** | `#090909` | `var(--ff_wp_tracking_border_color)` in `:root` (`rgb(0 0 0 / 50%)`) |
| **Variable Token (`--ff_wp_tracking_background_color`)** | `#ffffff` | `var(--ff_wp_tracking_background_color)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ff_wp_tracking_ease` | `cubic-bezier(0.25, 1, 0.5, 1)` | Typography / Scale Token |
| `--ff_wp_tracking_border_color` | `rgb(0 0 0 / 50%)` | Brand / Palette Token |
| `--ff_wp_tracking_background_color` | `#fff` | Canvas / Surface Token |
| `--ff_wp_tracking_text_color` | `#000` | Typography Ink Token |
| `--ff_wp_tracking_wrapper_padding` | `1.5rem` | Typography / Scale Token |
| `--ff_wp_tracking_dynamic-viewport-height` | `100vh` | Typography / Scale Token |
| `--fa-style-family-brands` | `"Font Awesome 6 Brands"` | Brand / Palette Token |
| `--fa-font-brands` | `normal 400 1em/1 "Font Awesome 6 Brands"` | Brand / Palette Token |
| `--fa-font-regular` | `normal 400 1em/1 "Font Awesome 6 Free"` | Typography / Scale Token |
| `--fa-style-family-classic` | `"Font Awesome 6 Free"` | Typography / Scale Token |
| `--fa-font-solid` | `normal 900 1em/1 "Font Awesome 6 Free"` | Typography / Scale Token |
| `--font-size-h1` | `calc(128 / var(--base-px, 18) * 1rem)` | Typography / Scale Token |
| `--font-size-h2-xl` | `calc(96 / var(--base-px, 18) * 1rem)` | Typography / Scale Token |
| `--font-size-h2` | `calc(72 / var(--base-px, 18) * 1rem)` | Typography / Scale Token |
| `--font-size-h3` | `calc(48 / var(--base-px, 18) * 1rem)` | Typography / Scale Token |
| `--font-size-h4` | `calc(32 / var(--base-px, 18) * 1rem)` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `General Sans`.
- **Primary Body Stack**: `General Sans`.
- **Technical / Metadata Stack**: `Fira Sans`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 36px`, `line-height: 39.6px`, `font-weight: 600`); CSS variables `--font-size-h1: calc(128 / var(--base-px, 18) * 1rem)`; rule `h1` (`font-size: var(--font-size-h1)`, `line-height: 1em`, `font-weight: 600`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 96px`, `line-height: 96px`, `font-weight: 600`); CSS variables `--font-size-h2-xl: calc(96 / var(--base-px, 18) * 1rem)`, `--font-size-h2: calc(72 / var(--base-px, 18) * 1rem)`; rule `h2` (`font-size: var(--font-size-h2-xl)`, `line-height: 1.02em`, `font-weight: 600`).
- **Body Copy**: live computed `body` (`font-size: 13.5px`, `line-height: 13.5px`, `font-weight: 400`); CSS variables `--font-size-body-lg: calc(24 / var(--base-px, 18) * 1rem)`, `--font-size-body: max(14px, calc(18 / var(--base-px, 18) * 1rem))`, `--font-size-body-sm: max(13px, calc(16 / var(--base-px, 18) * 1rem))`; rule `p` (`font-size: 1rem`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 13.5px`, `line-height: 13.5px`, `font-weight: 400`); CSS variables `--font-size-caption: max(12px, calc(14 / var(--base-px, 18) * 1rem))`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.25,1,0.5,1)`, `cubic-bezier(.28,.84,.42,1)`, `cubic-bezier(.4,0,.6,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.ff-wp-tracking__overlay`**: `transition: all .3s var(--ff_wp_tracking_ease)` extracted from `montarville-ca` stylesheet.
- **Selector `.ff-wp-tracking__ctn`**: `transition: height .3s var(--ff_wp_tracking_ease)` extracted from `montarville-ca` stylesheet.
- **Selector `.ff-wp-tracking__scroll-zone`**: `transition: height .6s var(--ff_wp_tracking_ease),visibility .6s var(--ff_...` extracted from `montarville-ca` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.25,1,0.5,1)`)**: Governs interactive state transitions across `<header.c-header>` and `<section.c-home-about>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — montarville · Une approche globale et inté │
│ ====================================================================== │
│ [ <header.c-header> (1440x0px)        | À propos · Découvrir · Proje ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.c-home-intro> (w=1440px)                      | │
│ | H1: Un partenaire engagé. Une expertise reconnue. Une...           | │
│ | Substrate: #121212 | Ink: #fafafa | Accent: #d0112b                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.c-home-about>) max-w: 1440px               | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Un partenaire engagé . Une e |  | Partenaire de vos réussites  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.c-home-target>) — Vous êtes...             | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.c-footer>   ) | https://montarville.ca/              │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 1rem)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.c-header>       ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.c-home-intro>) — 390px Vertical Lead          | │
│ | H1: Un partenaire engagé. Une expertise reconnue. Une...           | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.c-home-about>) — 1-Col Stack              | │
│ | [ Item 1: Un partenaire engagé . Une expertise reconnue. Un...   ] | │
│ | [ Item 2: Partenaire de vos réussites                            ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.c-home-target>) — 1-Col (Vous êtes...)      | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.c-footer>   ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.c-header> — `montarville-ca`)**:
   - Landmark `<header class="c-header">` (`1440x0px`) hosting `montarville · Une approche globale e` navigation (`À propos · Découvrir · Projets forfaitaires · Projets clés en main · Institutionnel`), DOM attributes (`data-browser="Chrome"`, `data-browser-version="131.0.0.0"`, `data-platform="Apple"`, `data-os="Mac OS"`), and stylesheet rule `admin-bar-ff-maintenance-mode.--a... { background-color:8b0000 }`.
2. **Hero Stage & Focal Lead (<section.c-home-intro> — `Un partenaire engagé. Une expertis`)**:
   - Landmark `<section class="c-home-intro">` presenting display lead `Un partenaire engagé. Une expertise reconnue. Une...` and copy excerpt *"Une approche globale et intégrée dans la gestion de vos projets d"* over `#121212` canvas and `#fafafa` ink.
3. **Primary Showcase & Content Grid (<section.c-home-about> — `Un partenaire engagé . Une experti`)**:
   - Landmark `<section class="c-home-about">` rendering section `Un partenaire engagé . Une expertise reconnue. Un...` with copy *"Que vous soyez au stade de la planification, à la recherche d’un "*, asset references (`orphisme_photographie_20210816-_2...`, `favicon.ico`, `FiraSans-Bold.woff2`, `GeneralSans-Variable.woff2`), and grid rule `.ff-wp-maintenance-page { color:00f!important }`.
4. **Interactive Detail & Feature Matrix (<section.c-home-target> — `Partenaire de vos réussites`)**:
   - Landmark `<section class="c-home-target">` framing `Partenaire de vos réussites` and `Vous êtes...` (*"montarville . se distingue par sa capacité à offrir un service in"*) with `#d0112b` surface cards, `#d0112b` accents, and `.ff-wp-tracking h3 { font-size:1.6rem }`.
5. **Colophon & Global Directory Footer (<footer.c-footer> — `https://montarville.ca/`)**:
   - Landmark `<footer class="c-footer">` anchoring `montarville · Une approche globa` footer links (`À propos · Découvrir · Projets forfaitaires · Projets clés en main · Institutionnel`), copy *"Ce qui nous différencie, c’est aussi la qualité des relation"*, and `#090909` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: montarville-ca (montarville · Une approche globale et intégrée dans la gestion de vos pr...)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `montarville-ca` (**montarville · Une approche globale et intégrée dans la gestion de vos pr...** — `https://montarville.ca/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#121212` canvas, `#fafafa` ink, `#d0112b` accent).
- **Identity & Domain Context**: Un partenaire engagé. Une expertise reconnue. Une exécution maîtrisée. - Une approche globale et intégrée dans la gestion de vos projets...
- **Primary Substrate**: `#121212` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#fafafa`, **Accent / Highlight**: `#d0112b`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#121212` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#fafafa` primary typography and `#d0112b` accents.
  - **Grounded Typographic Hierarchy**: Pairs `General Sans` for display copy (`Un partenaire engagé. Une expertise `) with `General Sans` and `Fira Sans`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 1rem`, padding `1.5rem`) with `cubic-bezier(0.25,1,0.5,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `montarville-ca` in your global stylesheet:

:root {
  /* montarville · Une approche globale et intégrée dans la gestion de vos pr... (montarville-ca) — Live-Grounded CSS Variables */
  --ff_wp_tracking_ease: cubic-bezier(0.25, 1, 0.5, 1); /* Typography / Scale Token (montarville-ca) */
  --ff_wp_tracking_border_color: rgb(0 0 0 / 50%); /* Brand / Palette Token (montarville-ca) */
  --ff_wp_tracking_background_color: #fff; /* Canvas / Surface Token (montarville-ca) */
  --ff_wp_tracking_text_color: #000; /* Typography Ink Token (montarville-ca) */
  --ff_wp_tracking_wrapper_padding: 1.5rem; /* Typography / Scale Token (montarville-ca) */
  --ff_wp_tracking_dynamic-viewport-height: 100vh; /* Typography / Scale Token (montarville-ca) */
  --fa-style-family-brands: "Font Awesome 6 Brands"; /* Brand / Palette Token (montarville-ca) */
  --fa-font-brands: normal 400 1em/1 "Font Awesome 6 Brands"; /* Brand / Palette Token (montarville-ca) */
  --fa-font-regular: normal 400 1em/1 "Font Awesome 6 Free"; /* Typography / Scale Token (montarville-ca) */
  --fa-style-family-classic: "Font Awesome 6 Free"; /* Typography / Scale Token (montarville-ca) */
  --fa-font-solid: normal 900 1em/1 "Font Awesome 6 Free"; /* Typography / Scale Token (montarville-ca) */
  --font-size-h1: calc(128 / var(--base-px, 18) * 1rem); /* Typography / Scale Token (montarville-ca) */
  --font-size-h2-xl: calc(96 / var(--base-px, 18) * 1rem); /* Typography / Scale Token (montarville-ca) */
  --font-size-h2: calc(72 / var(--base-px, 18) * 1rem); /* Typography / Scale Token (montarville-ca) */
  --font-size-h3: calc(48 / var(--base-px, 18) * 1rem); /* Typography / Scale Token (montarville-ca) */
  --font-size-h4: calc(32 / var(--base-px, 18) * 1rem); /* Typography / Scale Token (montarville-ca) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#121212` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#fafafa` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#d0112b` — grounded in live computed `button` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#d0112b` — grounded in live computed `button` `background-color` (`computed_styles.json`)
- **Secondary / Muted Copy**: `#000000` — grounded in `var(--ff_wp_tracking_text_color)` in `:root`
- **Structural Hairline Border**: `#090909` — grounded in `var(--ff_wp_tracking_border_color)` in `:root` (`rgb(0 0 0 / 50%)`)
- **Variable Token (`--ff_wp_tracking_background_color`)**: `#ffffff` — grounded in `var(--ff_wp_tracking_background_color)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport)
- **Padding & Gutters**: `1.5rem` lateral canvas padding with `1rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 1rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `1.5rem` horizontal padding
- **Media Queries**: `@media (min-width:1201px)`, `@media (max-width:1200px)`, `@media (max-width:750px)`, `@media (prefers-reduced-motion:reduce)`
- **Corner Radii**: `2px`, `1px`, `50%`, `var(--border-radius)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `General Sans`
- **Body Font Stack**: `General Sans`
- **Monospace / Technical Font Stack**: `Fira Sans`
- **H1 Display Rule**: live computed `h1` (`font-size: 36px`, `line-height: 39.6px`, `font-weight: 600`); CSS variables `--font-size-h1: calc(128 / var(--base-px, 18) * 1rem)`; rule `h1` (`font-size: var(--font-size-h1)`, `line-height: 1em`, `font-weight: 600`)
- **H2 Section Rule**: live computed `h2` (`font-size: 96px`, `line-height: 96px`, `font-weight: 600`); CSS variables `--font-size-h2-xl: calc(96 / var(--base-px, 18) * 1rem)`, `--font-size-h2: calc(72 / var(--base-px, 18) * 1rem)`; rule `h2` (`font-size: var(--font-size-h2-xl)`, `line-height: 1.02em`, `font-weight: 600`)
- **Body Copy Rule**: live computed `body` (`font-size: 13.5px`, `line-height: 13.5px`, `font-weight: 400`); CSS variables `--font-size-body-lg: calc(24 / var(--base-px, 18) * 1rem)`, `--font-size-body: max(14px, calc(18 / var(--base-px, 18) * 1rem))`, `--font-size-body-sm: max(13px, calc(16 / var(--base-px, 18) * 1rem))`; rule `p` (`font-size: 1rem`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 13.5px`, `line-height: 13.5px`, `font-weight: 400`); CSS variables `--font-size-caption: max(12px, calc(14 / var(--base-px, 18) * 1rem))`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `montarville-ca` (`montarville · Une approche globale et intégrée dans la gestion de vos pr...`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.c-header> — `montarville-ca`)**:
   - DOM & Selectors: Landmark `<header class="c-header">` (`1440x0px`) hosting `montarville · Une approche globale e` navigation (`À propos · Découvrir · Projets forfaitaires · Projets clés en main · Institutionnel`), DOM attributes (`data-browser="Chrome"`, `data-browser-version="131.0.0.0"`, `data-platform="Apple"`, `data-os="Mac OS"`), and stylesheet rule `admin-bar-ff-maintenance-mode.--a... { background-color:8b0000 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.c-header> — `montarville-ca`)` (`montarville-ca`) adapts across `@media (min-width:1201px)`, `@media (max-width:1200px)`, `@media (max-width:750px)`, `@media (prefers-reduced-motion:reduce)` with `cubic-bezier(0.25,1,0.5,1)`, `cubic-bezier(.28,.84,.42,1)`, `cubic-bezier(.4,0,.6,1)` transitions and links `À propos · Découvrir · Projets forfaitaires · Projets clés en main · Institutionnel`.
2. **Hero Stage & Focal Lead (<section.c-home-intro> — `Un partenaire engagé. Une expertis`)**:
   - DOM & Selectors: Landmark `<section class="c-home-intro">` presenting display lead `Un partenaire engagé. Une expertise reconnue. Une...` and copy excerpt *"Une approche globale et intégrée dans la gestion de vos projets d"* over `#121212` canvas and `#fafafa` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#121212` background with `#fafafa` headline `Un partenaire engagé. Une expertise reconnue. Une...`.
3. **Primary Showcase & Content Grid (<section.c-home-about> — `Un partenaire engagé . Une experti`)**:
   - DOM & Selectors: Landmark `<section class="c-home-about">` rendering section `Un partenaire engagé . Une expertise reconnue. Un...` with copy *"Que vous soyez au stade de la planification, à la recherche d’un "*, asset references (`orphisme_photographie_20210816-_2...`, `favicon.ico`, `FiraSans-Bold.woff2`, `GeneralSans-Variable.woff2`), and grid rule `.ff-wp-maintenance-page { color:00f!important }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.c-home-about> — `Un partenaire engagé . Une experti`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 1rem`) on desktop and Single-column vertical stack at `390px` viewport width with `1.5rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.c-home-target> — `Partenaire de vos réussites`)**:
   - DOM & Selectors: Landmark `<section class="c-home-target">` framing `Partenaire de vos réussites` and `Vous êtes...` (*"montarville . se distingue par sa capacité à offrir un service in"*) with `#d0112b` surface cards, `#d0112b` accents, and `.ff-wp-tracking h3 { font-size:1.6rem }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.c-home-target> — `Partenaire de vos réussites`)` uses `2px`, `1px`, `50%`, `var(--border-radius)` radii, `#d0112b` highlights, and assets (orphisme_photographie_20210816-_2..., favicon.ico, FiraSans-Bold.woff2).
5. **Colophon & Global Directory Footer (<footer.c-footer> — `https://montarville.ca/`)**:
   - DOM & Selectors: Landmark `<footer class="c-footer">` anchoring `montarville · Une approche globa` footer links (`À propos · Découvrir · Projets forfaitaires · Projets clés en main · Institutionnel`), copy *"Ce qui nous différencie, c’est aussi la qualité des relation"*, and `#090909` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.c-footer> — `https://montarville.ca/`)` aligns to `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport) with `1.5rem` lateral canvas padding with `1rem` grid gap and attributes (data-browser="Chrome", data-browser-version="131.0.0.0", data-platform="Apple").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Une approche globale et intégrée dans la gestion de vos projets de construction."*
- Copy Excerpt 2: *"Que vous soyez au stade de la planification, à la recherche d’un gestionnaire pour..."*
- Copy Excerpt 3: *"montarville . se distingue par sa capacité à offrir un service intégré, structuré..."*
- Copy Excerpt 4: *"Ce qui nous différencie, c’est aussi la qualité des relations que nous cultivons...."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.25,1,0.5,1)`, `cubic-bezier(.28,.84,.42,1)`, `cubic-bezier(.4,0,.6,1)`
- **Extracted Stylesheet Rules (`montarville-ca`)**:
- `admin-bar-ff-maintenance-mode.--a... { background-color:8b0000 }`
- `.ff-wp-maintenance-page { color:00f!important }`
- `.ff-wp-tracking h3 { font-size:1.6rem }`
- `.ff-wp-tracking h4 { font-size:1.3rem }`
- `.ff-wp-tracking p { font-size:1rem;margin-top:1em }`
- **Per-Selector Transition Rules**:
- **Selector `.ff-wp-tracking__overlay`**: `transition: all .3s var(--ff_wp_tracking_ease)` extracted from `montarville-ca` stylesheet.
- **Selector `.ff-wp-tracking__ctn`**: `transition: height .3s var(--ff_wp_tracking_ease)` extracted from `montarville-ca` stylesheet.
- **Selector `.ff-wp-tracking__scroll-zone`**: `transition: height .6s var(--ff_wp_tracking_ease),visibility .6s var(--ff_...` extracted from `montarville-ca` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.25,1,0.5,1)`)**: Governs interactive state transitions across `<header.c-header>` and `<section.c-home-about>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `montarville-ca`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
