---
title: "UI Prompt Blueprint: realevate-agency"
date: 2026-11-23
captured_at: 2026-11-23
target: "realevate-agency"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#1f2b5e` ink, `#000080` accent)"
---

# UI Design System & Master Generation Blueprint: realevate-agency

> **Realevate · Exceptional Real Estate Investments in Cyprus, Montenegro &...** (https://realevate.agency/) — Realevate is a global real estate agency specializing in unique properties and exceptional developments in high-demand markets, offering...

![Desktop Viewport Capture (1440x900)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Realevate · Exceptional Real Estate Investments in Cyprus, Montenegro &...** (`https://realevate.agency/`). Realevate is a global real estate agency specializing in unique properties and exceptional developments in high-demand markets, offering...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#1f2b5e` ink, `#000080` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#1f2b5e` primary typography and `#000080` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Google Sans` for display copy (`Invest in Exceptional Real Estate Pr`) with `Google Sans` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `100vw` container bounds (`gap: 2.601vw`, padding `4.5vw`) with `cubic-bezier(.7,.6,0,1)` easing and GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x844)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×900px` (`assets/desktop.png`, single-viewport 100vh live capture (900px)), Mobile `390×844px` (`assets/mobile.png`, single-viewport 100vh live capture (844px)).
- **Master Container Bounds**: `100vw` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `4.5vw` lateral canvas padding with `2.601vw` grid gap.
- **Border Radius Scale**: `5px`, `50%`, `999px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 100vw`, `gap: 2.601vw`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `4.5vw` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:650px)and (orientation:portrait)`, `@media (hover:none),(max-width:650px)and (orientation:portrait)`, `@media (min-width:651px)`, `@media (prefers-reduced-motion:reduce)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#1f2b5e` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#e3e5eb` | live computed `nav` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#000080` | `body.home-logo-transition.conta... { color: navy }` (`#000080`) |
| **Secondary / Muted Copy** | `#80988e` | `var(--category-evergreen-muted)` in `:root` |
| **Structural Hairline Border** | `#d7d9e2` | `.contact-form-tabs { border-bottom: #d7d9e2 }` |
| **Variable Token (`--muted`)** | `#626c95` | `var(--muted)` in `:root` |
| **Variable Token (`--category-by-the-sea-color`)** | `#222a4c` | `var(--category-by-the-sea-color)` in `:root` |
| **Variable Token (`--category-by-the-sea-muted`)** | `#5d668d` | `var(--category-by-the-sea-muted)` in `:root` |
| **Variable Token (`--category-evergreen-color`)** | `#36614d` | `var(--category-evergreen-color)` in `:root` |
| **Variable Token (`--category-urban-living-color`)** | `#2d1c2d` | `var(--category-urban-living-color)` in `:root` |
| **Variable Token (`--category-urban-living-muted`)** | `#6b5a6b` | `var(--category-urban-living-muted)` in `:root` |
| **Variable Token (`--category-rare-gems-color`)** | `#1c181d` | `var(--category-rare-gems-color)` in `:root` |
| **Variable Token (`--category-rare-gems-muted`)** | `#5c585d` | `var(--category-rare-gems-muted)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--brand-navy` | `#1F2B5E` | Brand / Palette Token |
| `--navy` | `var(--brand-navy)` | Layout / Spatial Grid Token |
| `--muted` | `#626C95` | Color / Atmospheric Token |
| `--white` | `#FFFFFF` | Canvas / Surface Token |
| `--category-color-light` | `var(--white)` | Canvas / Surface Token |
| `--category-by-the-sea-color` | `#222A4C` | Brand / Palette Token |
| `--category-by-the-sea-muted` | `#5D668D` | Color / Atmospheric Token |
| `--category-evergreen-color` | `#36614D` | Brand / Palette Token |
| `--category-evergreen-muted` | `#80988E` | Color / Atmospheric Token |
| `--category-urban-living-color` | `#2D1C2D` | Brand / Palette Token |
| `--category-urban-living-muted` | `#6B5A6B` | Color / Atmospheric Token |
| `--category-rare-gems-color` | `#1C181D` | Brand / Palette Token |
| `--category-rare-gems-muted` | `#5C585D` | Color / Atmospheric Token |
| `--custom-scrollbar-thumb-color` | `var(--muted)` | Brand / Palette Token |
| `--sans-font` | `"Google Sans", Arial, Helvetica, sans-serif` | Typography / Scale Token |
| `--display-font` | `"Roslindale Display", Georgia, "Times New Roman", serif` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Google Sans`.
- **Primary Body Stack**: `Google Sans`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 23.6827px`, `line-height: 30.7875px`, `font-weight: 500`, `letter-spacing: -0.236827px`); CSS variables `--display-font: "Roslindale Display", Georgia, "Times New Roman", serif`, `--desktop-h1-size: 16vw`, `--desktop-h1-line-height: 1`; rule `h1` (`font-size: 5.5vw`).
- **Section Heading (`H2`)**: CSS variables `--desktop-h2-size: 5.2vw`, `--desktop-h2-line-height: .94`, `--desktop-h2-letter-spacing: -.03em`; rule `h2` (`font-weight: 200`).
- **Body Copy**: live computed `body` (`font-size: 16.3705px`, `line-height: normal`, `font-weight: 500`, `letter-spacing: -0.163705px`); CSS variables `--body-leading: 1.35`; rule `,body` (`font-size: var(--text-size)`, `letter-spacing: -.01em`, `font-weight: 500`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16.3705px`, `line-height: normal`, `font-weight: 500`, `letter-spacing: -0.163705px`); CSS variables `--desktop-h1-letter-spacing: -.02em`, `--desktop-h2-letter-spacing: -.03em`, `--desktop-h3-letter-spacing: -.05em`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.7,.6,0,1)`, `cubic-bezier(.18,.13,0,.99)`, `cubic-bezier(.16,1,.3,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.custom-scrollbar`**: `transition: opacity .35s ease` extracted from `realevate-agency` stylesheet.
- **Selector `.custom-scrollbar .custom-scrollb...`**: `transition: background .15s ease` extracted from `realevate-agency` stylesheet.
- **Selector `.selection-card`**: `transition: filter var(--selection-hover-duration) var(--selection-hover-e...` extracted from `realevate-agency` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.7,.6,0,1)`)**: Governs interactive state transitions across `<header.logo>` and `<main.is-ready>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Realevate · Exceptional Real Estate Invest │
│ ====================================================================== │
│ [ <header.logo> (273x19px)            | Overview · Index · Archive · ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <main.site-preloader-counter-init> (w=1440px)          | │
│ | H1: Invest in Exceptional Real Estate Properties in C...           | │
│ | Substrate: #ffffff | Ink: #1f2b5e | Accent: #000080                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<main.is-ready>) max-w: 100vw                       | │
│ | +------------------------------+  +------------------------------+ | │
│ | | STARTING FROM 100,000€       |  | Starting from 100,000€       | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<main.rotate-phone-overlay) — Please rotate your de | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer>) | https://realevate.agency/            │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 2.601vw)    │
│ ====================================================================== │
│ [ HEADER BAR (<header.logo>           ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<main.site-preloader-cou) — 390px Vertical Lead        | │
│ | H1: Invest in Exceptional Real Estate Properties in C...           | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<main.is-ready>) — 1-Col Stack                     | │
│ | [ Item 1: STARTING FROM 100,000€                                 ] | │
│ | [ Item 2: Starting from 100,000€                                 ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<main.rotate-phone-overl) — 1-Col (Please rotate your) │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer>) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.logo> — `realevate-agency`)**:
   - Landmark `<header class="logo">` (`273x19px`) hosting `Realevate · Exceptional Real Estate ` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-category="home"`, `data-selection-cover="assets/women-monteneg..."`, `data-category="by-the-sea"`, `data-selection-cover="assets/bythesea-card-..."`), and stylesheet rule `after { box-sizing:border-box;-webkit-user-select:none;-moz-user-select:none;-ms... }`.
2. **Hero Stage & Focal Lead (<main.site-preloader-counter-init> — `Invest in Exceptional Real Estate `)**:
   - Landmark `<main class="site-preloader-counter-init">` presenting display lead `Invest in Exceptional Real Estate Properties in C...` and copy excerpt *"STARTING FROM 100,000€"* over `#ffffff` canvas and `#1f2b5e` ink.
3. **Primary Showcase & Content Grid (<main.is-ready> — `STARTING FROM 100,000€`)**:
   - Landmark `<main class="is-ready">` rendering section `STARTING FROM 100,000€` with copy *"Starting from 100,000€"*, asset references (`4532996743652549`, `fbevents.js`, `compat-bootstrap.js`, `favicon.png`), and grid rule `root { --category-hero-scroll-grow-scale: 1.2 }`.
4. **Interactive Detail & Feature Matrix (<main.rotate-phone-overlay> — `Starting from 100,000€`)**:
   - Landmark `<main class="rotate-phone-overlay">` framing `Starting from 100,000€` and `Please rotate your device` (*"Please rotate your device"*) with `#e3e5eb` surface cards, `#000080` accents, and `html { scrollbar-width:none;width:100%;height:100svh }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://realevate.agency/`)**:
   - Landmark `<footer class="site-footer">` anchoring `Realevate · Exceptional Real Est` footer links (`Overview · Index · Archive · About · Contact`), copy *"Homepage Invest in Cyprus, Montenegro and Georgia"*, and `#d7d9e2` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: realevate-agency (Realevate · Exceptional Real Estate Investments in Cyprus, Montenegro &...)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `realevate-agency` (**Realevate · Exceptional Real Estate Investments in Cyprus, Montenegro &...** — `https://realevate.agency/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#1f2b5e` ink, `#000080` accent).
- **Identity & Domain Context**: Realevate is a global real estate agency specializing in unique properties and exceptional developments in high-demand markets, offering...
- **Primary Substrate**: `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#1f2b5e`, **Accent / Highlight**: `#000080`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#1f2b5e` primary typography and `#000080` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Google Sans` for display copy (`Invest in Exceptional Real Estate Pr`) with `Google Sans` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `100vw` container bounds (`gap: 2.601vw`, padding `4.5vw`) with `cubic-bezier(.7,.6,0,1)` easing and GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `realevate-agency` in your global stylesheet:

:root {
  /* Realevate · Exceptional Real Estate Investments in Cyprus, Montenegro &... (realevate-agency) — Live-Grounded CSS Variables */
  --brand-navy: #1F2B5E; /* Brand / Palette Token (realevate-agency) */
  --navy: var(--brand-navy); /* Layout / Spatial Grid Token (realevate-agency) */
  --muted: #626C95; /* Color / Atmospheric Token (realevate-agency) */
  --white: #FFFFFF; /* Canvas / Surface Token (realevate-agency) */
  --category-color-light: var(--white); /* Canvas / Surface Token (realevate-agency) */
  --category-by-the-sea-color: #222A4C; /* Brand / Palette Token (realevate-agency) */
  --category-by-the-sea-muted: #5D668D; /* Color / Atmospheric Token (realevate-agency) */
  --category-evergreen-color: #36614D; /* Brand / Palette Token (realevate-agency) */
  --category-evergreen-muted: #80988E; /* Color / Atmospheric Token (realevate-agency) */
  --category-urban-living-color: #2D1C2D; /* Brand / Palette Token (realevate-agency) */
  --category-urban-living-muted: #6B5A6B; /* Color / Atmospheric Token (realevate-agency) */
  --category-rare-gems-color: #1C181D; /* Brand / Palette Token (realevate-agency) */
  --category-rare-gems-muted: #5C585D; /* Color / Atmospheric Token (realevate-agency) */
  --custom-scrollbar-thumb-color: var(--muted); /* Brand / Palette Token (realevate-agency) */
  --sans-font: "Google Sans", Arial, Helvetica, sans-serif; /* Typography / Scale Token (realevate-agency) */
  --display-font: "Roslindale Display", Georgia, "Times New Roman", serif; /* Typography / Scale Token (realevate-agency) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#1f2b5e` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#e3e5eb` — grounded in live computed `nav` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#000080` — grounded in `body.home-logo-transition.conta... { color: navy }` (`#000080`)
- **Secondary / Muted Copy**: `#80988e` — grounded in `var(--category-evergreen-muted)` in `:root`
- **Structural Hairline Border**: `#d7d9e2` — grounded in `.contact-form-tabs { border-bottom: #d7d9e2 }`
- **Variable Token (`--muted`)**: `#626c95` — grounded in `var(--muted)` in `:root`
- **Variable Token (`--category-by-the-sea-color`)**: `#222a4c` — grounded in `var(--category-by-the-sea-color)` in `:root`
- **Variable Token (`--category-by-the-sea-muted`)**: `#5d668d` — grounded in `var(--category-by-the-sea-muted)` in `:root`
- **Variable Token (`--category-evergreen-color`)**: `#36614d` — grounded in `var(--category-evergreen-color)` in `:root`
- **Variable Token (`--category-urban-living-color`)**: `#2d1c2d` — grounded in `var(--category-urban-living-color)` in `:root`
- **Variable Token (`--category-urban-living-muted`)**: `#6b5a6b` — grounded in `var(--category-urban-living-muted)` in `:root`
- **Variable Token (`--category-rare-gems-color`)**: `#1c181d` — grounded in `var(--category-rare-gems-color)` in `:root`
- **Variable Token (`--category-rare-gems-muted`)**: `#5c585d` — grounded in `var(--category-rare-gems-muted)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×900px` (single-viewport 100vh live capture (900px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×844px` (single-viewport 100vh live capture (844px), `390px` standard mobile width).
- **Container Max-Width**: `100vw` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `4.5vw` lateral canvas padding with `2.601vw` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 100vw`, `gap: 2.601vw`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `4.5vw` horizontal padding
- **Media Queries**: `@media (max-width:650px)and (orientation:portrait)`, `@media (hover:none),(max-width:650px)and (orientation:portrait)`, `@media (min-width:651px)`, `@media (prefers-reduced-motion:reduce)`
- **Corner Radii**: `5px`, `50%`, `999px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Google Sans`
- **Body Font Stack**: `Google Sans`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 23.6827px`, `line-height: 30.7875px`, `font-weight: 500`, `letter-spacing: -0.236827px`); CSS variables `--display-font: "Roslindale Display", Georgia, "Times New Roman", serif`, `--desktop-h1-size: 16vw`, `--desktop-h1-line-height: 1`; rule `h1` (`font-size: 5.5vw`)
- **H2 Section Rule**: CSS variables `--desktop-h2-size: 5.2vw`, `--desktop-h2-line-height: .94`, `--desktop-h2-letter-spacing: -.03em`; rule `h2` (`font-weight: 200`)
- **Body Copy Rule**: live computed `body` (`font-size: 16.3705px`, `line-height: normal`, `font-weight: 500`, `letter-spacing: -0.163705px`); CSS variables `--body-leading: 1.35`; rule `,body` (`font-size: var(--text-size)`, `letter-spacing: -.01em`, `font-weight: 500`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16.3705px`, `line-height: normal`, `font-weight: 500`, `letter-spacing: -0.163705px`); CSS variables `--desktop-h1-letter-spacing: -.02em`, `--desktop-h2-letter-spacing: -.03em`, `--desktop-h3-letter-spacing: -.05em`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `realevate-agency` (`Realevate · Exceptional Real Estate Investments in Cyprus, Montenegro &...`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.logo> — `realevate-agency`)**:
   - DOM & Selectors: Landmark `<header class="logo">` (`273x19px`) hosting `Realevate · Exceptional Real Estate ` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-category="home"`, `data-selection-cover="assets/women-monteneg..."`, `data-category="by-the-sea"`, `data-selection-cover="assets/bythesea-card-..."`), and stylesheet rule `after { box-sizing:border-box;-webkit-user-select:none;-moz-user-select:none;-ms... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.logo> — `realevate-agency`)` (`realevate-agency`) adapts across `@media (max-width:650px)and (orientation:portrait)`, `@media (hover:none),(max-width:650px)and (orientation:portrait)`, `@media (min-width:651px)`, `@media (prefers-reduced-motion:reduce)` with `cubic-bezier(.7,.6,0,1)`, `cubic-bezier(.18,.13,0,.99)`, `cubic-bezier(.16,1,.3,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<main.site-preloader-counter-init> — `Invest in Exceptional Real Estate `)**:
   - DOM & Selectors: Landmark `<main class="site-preloader-counter-init">` presenting display lead `Invest in Exceptional Real Estate Properties in C...` and copy excerpt *"STARTING FROM 100,000€"* over `#ffffff` canvas and `#1f2b5e` ink.
   - Responsive Contract: Hero stage (`1440×900px` desktop / `390×844px` mobile) sets `#ffffff` background with `#1f2b5e` headline `Invest in Exceptional Real Estate Properties in C...`.
3. **Primary Showcase & Content Grid (<main.is-ready> — `STARTING FROM 100,000€`)**:
   - DOM & Selectors: Landmark `<main class="is-ready">` rendering section `STARTING FROM 100,000€` with copy *"Starting from 100,000€"*, asset references (`4532996743652549`, `fbevents.js`, `compat-bootstrap.js`, `favicon.png`), and grid rule `root { --category-hero-scroll-grow-scale: 1.2 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<main.is-ready> — `STARTING FROM 100,000€`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 100vw`, `gap: 2.601vw`) on desktop and Single-column vertical stack at `390px` viewport width with `4.5vw` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<main.rotate-phone-overlay> — `Starting from 100,000€`)**:
   - DOM & Selectors: Landmark `<main class="rotate-phone-overlay">` framing `Starting from 100,000€` and `Please rotate your device` (*"Please rotate your device"*) with `#e3e5eb` surface cards, `#000080` accents, and `html { scrollbar-width:none;width:100%;height:100svh }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<main.rotate-phone-overlay> — `Starting from 100,000€`)` uses `5px`, `50%`, `999px` radii, `#000080` highlights, and assets (4532996743652549, fbevents.js, compat-bootstrap.js).
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://realevate.agency/`)**:
   - DOM & Selectors: Landmark `<footer class="site-footer">` anchoring `Realevate · Exceptional Real Est` footer links (`Overview · Index · Archive · About · Contact`), copy *"Homepage Invest in Cyprus, Montenegro and Georgia"*, and `#d7d9e2` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.site-footer> — `https://realevate.agency/`)` aligns to `100vw` (non-`@media` desktop container stylesheet rule) with `4.5vw` lateral canvas padding with `2.601vw` grid gap and attributes (data-category="home", data-selection-cover="assets/women-monteneg...", data-category="by-the-sea").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"STARTING FROM 100,000€"*
- Copy Excerpt 2: *"Starting from 100,000€"*
- Copy Excerpt 3: *"Please rotate your device"*
- Copy Excerpt 4: *"Homepage Invest in Cyprus, Montenegro and Georgia"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.7,.6,0,1)`, `cubic-bezier(.18,.13,0,.99)`, `cubic-bezier(.16,1,.3,1)`
- **Extracted Stylesheet Rules (`realevate-agency`)**:
- `after { box-sizing:border-box;-webkit-user-select:none;-moz-user-select:none;-ms... }`
- `root { --category-hero-scroll-grow-scale: 1.2 }`
- `html { scrollbar-width:none;width:100%;height:100svh }`
- `body::-webkit-scrollbar { display:none }`
- `body { -ms-overflow-style:none }`
- **Per-Selector Transition Rules**:
- **Selector `.custom-scrollbar`**: `transition: opacity .35s ease` extracted from `realevate-agency` stylesheet.
- **Selector `.custom-scrollbar .custom-scrollb...`**: `transition: background .15s ease` extracted from `realevate-agency` stylesheet.
- **Selector `.selection-card`**: `transition: filter var(--selection-hover-duration) var(--selection-hover-e...` extracted from `realevate-agency` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.7,.6,0,1)`)**: Governs interactive state transitions across `<header.logo>` and `<main.is-ready>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `realevate-agency`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
