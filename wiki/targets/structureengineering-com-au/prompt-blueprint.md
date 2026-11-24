---
title: "UI Prompt Blueprint: structureengineering-com-au"
date: 2026-11-24
captured_at: 2026-11-24
target: "structureengineering-com-au"
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
archetype: "Light-Substrate Editorial & Modular Grid System (`#f5f5f5` canvas, `#000000` ink, `#ffffff` accent)"
---

# UI Design System & Master Generation Blueprint: structureengineering-com-au

> **Structure Consulting Engineers · Structural Engineering Sydney** (https://structureengineering.com.au/) — Specialists in structural engineering in Sydney, we work across a range of industries from residential to commercial, remedial, governmen...

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Structure Consulting Engineers · Structural Engineering Sydney** (`https://structureengineering.com.au/`). Specialists in structural engineering in Sydney, we work across a range of industries from residential to commercial, remedial, governmen...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#f5f5f5` canvas, `#000000` ink, `#ffffff` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f5f5f5` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#ffffff` accents.
  - **Grounded Typographic Hierarchy**: Uses `SequelSans` across display (`A different approach to traditional `) and body copy, paired with `PPFraktionMono` for monospace/code.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 12px`, padding `0.5rem`) with `cubic-bezier(0.015,0.791,0.757,1.024)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=8979px` / doc `9912px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport).
- **Canvas Lateral Padding & Spacing**: `0.5rem` lateral canvas padding with `12px` grid gap.
- **Border Radius Scale**: `1.04px`, `0px`, `100%`, `50%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 12px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `0.5rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width: 479px)`, `@media (min-width: 375px)`, `@media (min-width: 769px)`, `@media (min-width: 1200px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f5f5f5` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `.background-color-white { background-color: white }` (`#ffffff`) |
| **Interactive Accent / Highlight** | `#ffffff` | `ackground-color-gold .block-hea... { color: #ffffff }` |
| **Secondary / Muted Copy** | `#777777` | `form-wrap .dropdown-menu>.disab... { color: #777777 }` |
| **Structural Hairline Border** | `#ffffff` | `a.btn-with-arrow:hover { border-color: #ffffff }` |
| **Variable Token (`--color-gold`)** | `#b9b36d` | `var(--color-gold)` in `:root` |
| **Variable Token (`--color-grey`)** | `#bebebe` | `var(--color-grey)` in `:root` |
| **Variable Token (`--wp--preset--color--cyan-bluish-gray`)** | `#abb8c3` | `var(--wp--preset--color--cyan-bluish-gray)` in stylesheet |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#ffffff` | Canvas / Surface Token |
| `--color-gold` | `#B9B36D` | Brand / Palette Token |
| `--color-background-grey` | `#F5F5F5` | Canvas / Surface Token |
| `--color-grey` | `#BEBEBE` | Brand / Palette Token |
| `--wp--preset--aspect-ratio--square` | `1` | Design System Custom Token |
| `--wp--preset--aspect-ratio--4-3` | `4/3` | Design System Custom Token |
| `--wp--preset--aspect-ratio--3-4` | `3/4` | Design System Custom Token |
| `--wp--preset--aspect-ratio--3-2` | `3/2` | Design System Custom Token |
| `--wp--preset--aspect-ratio--2-3` | `2/3` | Design System Custom Token |
| `--wp--preset--aspect-ratio--16-9` | `16/9` | Design System Custom Token |
| `--wp--preset--aspect-ratio--9-16` | `9/16` | Design System Custom Token |
| `--wp--preset--color--black` | `#000000` | Canvas / Surface Token |
| `--wp--preset--color--cyan-bluish-gray` | `#abb8c3` | Brand / Palette Token |
| `--structureenginee-bg` | `#f5f5f5` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--structureenginee-ink` | `#000000` | Primary Typography Ink (computed-derived) |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `SequelSans`.
- **Primary Body Stack**: `SequelSans`.
- **Technical / Metadata Stack**: `PPFraktionMono`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 81.6px`, `line-height: 81.6px`, `font-weight: 400`); rule `h1` (`font-size: 2em`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 81.6px`, `line-height: 81.6px`, `font-weight: 400`); rule `.h2` (`font-size: 3.7em`, `line-height: 1`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 20.8px`, `font-weight: 400`); rule `p` (`font-size: 0.8em`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 20.8px`, `font-weight: 400`); rule `small` (`font-size: 80%`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.015,0.791,0.757,1.024)`, `cubic-bezier(0.76,0,0.24,1)`, `cubic-bezier(0.66,0,0.34,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.preload *`**: `transition: none !important` extracted from `structureengineering-com-au` stylesheet.
- **Selector `.rocket-lazyload`**: `transition: opacity 1s` extracted from `structureengineering-com-au` stylesheet.
- **Selector `.media-link .media`**: `transition: ease-in-out 0.5s` extracted from `structureengineering-com-au` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.015,0.791,0.757,1.024)`)**: Governs interactive state transitions across `<nav.top-nav>` and `<section.section-intro>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `9912px`, deepest scrollY reached `8979px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: Native browser scroll / standard CSS transitions.
- **Hover Physics (`primary_cta` · `PUBLIC ART`)**: `color`: `rgb(255, 255, 255)` -> `rgb(0, 0, 0)`; `backgroundColor`: `rgba(0, 0, 0, 0)` -> `rgb(255, 255, 255)` (`transition-duration: 0.25s`, `timing: ease`).
- **Route Transition Architecture**: First internal navigation (`/journal/`) measured as `MPA` in `1663ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Structure Consulting Engineers · Structura │
│ ====================================================================== │
│ [ <nav.top-nav> (878x93px)            | About · Company · Careers ·  ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.section> (w=1425px)                           | │
│ | H1: A different approach to traditional structural en...           | │
│ | Substrate: #f5f5f5 | Ink: #000000 | Accent: #ffffff                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.section-intro>) max-w: 1440px              | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Northbridge House II         |  | Castlecrag House             | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.section-spread>) — Marrickville House      | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.preloadergon) | https://structureengineering.com.au  │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 12px)       │
│ ====================================================================== │
│ [ HEADER BAR (<nav.top-nav>           ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.section>) — 390px Vertical Lead               | │
│ | H1: A different approach to traditional structural en...           | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.section-intro) — 1-Col Stack              | │
│ | [ Item 1: Northbridge House II                                   ] | │
│ | [ Item 2: Castlecrag House                                       ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.section-spread>) — 1-Col (Marrickville House) │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.preloadergon) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.top-nav> — `structureengineering-com-au`)**:
   - Landmark `<nav class="top-nav font-PPFraktionMono">` (`878x93px`) hosting `Structure Consulting Engineers · Str` navigation (`About · Company · Careers · People · Sectors`), DOM attributes (`data-section-background-color="background-color-black"`, `data-rocket-prefetch`, `data-rocket-preload`, `data-rocket-async="style"`), and stylesheet rule `html { scrollbar-gutter: stable; }`.
2. **Hero Stage & Focal Lead (<section.section> — `A different approach to traditiona`)**:
   - Landmark `<section class="section section-topbannerhome">` presenting display lead `A different approach to traditional structural en...` and copy excerpt *"Residential Northbridge House II"* over `#f5f5f5` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.section-intro> — `Northbridge House II`)**:
   - Landmark `<section class="section section-intro">` rendering section `Northbridge House II` with copy *"Residential Castlecrag House"*, asset references (`gtm.js`, `www.googletagmanager.com`, `SequelSans-Medium.woff2`, `PPFraktionMono-Regular.woff2`), and grid rule `figure { border: none; padding: 0; display: inline-block; margin: 1em 0; }`.
4. **Interactive Detail & Feature Matrix (<section.section-spread> — `Castlecrag House`)**:
   - Landmark `<section class="section section-spread">` framing `Castlecrag House` and `Marrickville House` (*"Residential Marrickville House"*) with `#ffffff` surface cards, `#ffffff` accents, and `img { pointer-events: none; }`.
5. **Colophon & Global Directory Footer (<footer.preloadergone> — `https://structureengineering.com.au/`)**:
   - Landmark `<footer class="preloadergone">` anchoring `Structure Consulting Engineers ·` footer links (`About · Company · Careers · People · Sectors`), copy *"Through thoughtful design, clear communication and lateral t"*, and `#ffffff` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `A different approach to traditional structural en...` · sticky/fixed elements: `1`
- **Step 02** (`y=850px`, `9%`): Active landmark `Northbridge House II` · sticky/fixed elements: `2`
- **Step 03** (`y=2550px`, `28%`): Active landmark `Section @ 28%` · sticky/fixed elements: `2`
- **Step 04** (`y=4250px`, `47%`): Active landmark `Do it once. Do it right.` · sticky/fixed elements: `1`
- **Step 05** (`y=5100px`, `57%`): Active landmark `TAHMOOR SPORTS COMPLEX` · sticky/fixed elements: `1`
- **Step 06** (`y=6800px`, `75%`): Active landmark `SPIN` · sticky/fixed elements: `1`
- **Step 07** (`y=8500px`, `95%`): Active landmark `NORTHBRIDGE HOUSE II` · sticky/fixed elements: `1`
- **Step 08** (`y=8979px`, `100%`): Active landmark `BONDI HOUSE II` · sticky/fixed elements: `1`

### Multi-Page Internal Route Map
- **Listing Route (`/journal/`)**: `https://structureengineering.com.au/journal/` — H1: `Journal`, scrollHeight `3573px`, transition `MPA` (`1663ms`)
- **Detail Route (`/sectors/residential-structural-engineers/`)**: `https://structureengineering.com.au/sectors/residential-structural-engineers/` — H1: `Most residentialstructural engineers focus on num...`, scrollHeight `5843px`, transition `direct` (`1122ms`)
- **About Route (`/people/`)**: `https://structureengineering.com.au/people/` — H1: `People`, scrollHeight `3432px`, transition `direct` (`735ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: structureengineering-com-au (Structure Consulting Engineers · Structural Engineering Sydney)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `structureengineering-com-au` (**Structure Consulting Engineers · Structural Engineering Sydney** — `https://structureengineering.com.au/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#f5f5f5` canvas, `#000000` ink, `#ffffff` accent).
- **Identity & Domain Context**: Specialists in structural engineering in Sydney, we work across a range of industries from residential to commercial, remedial, governmen...
- **Primary Substrate**: `#f5f5f5` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#000000`, **Accent / Highlight**: `#ffffff`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f5f5f5` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#ffffff` accents.
  - **Grounded Typographic Hierarchy**: Uses `SequelSans` across display (`A different approach to traditional `) and body copy, paired with `PPFraktionMono` for monospace/code.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 12px`, padding `0.5rem`) with `cubic-bezier(0.015,0.791,0.757,1.024)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `structureengineering-com-au` in your global stylesheet:

:root {
  /* Structure Consulting Engineers · Structural Engineering Sydney (structureengineering-com-au) — Live-Grounded CSS Variables */
  --color-black: #000; /* Canvas / Surface Token (structureengineering-com-au) */
  --color-white: #ffffff; /* Canvas / Surface Token (structureengineering-com-au) */
  --color-gold: #B9B36D; /* Brand / Palette Token (structureengineering-com-au) */
  --color-background-grey: #F5F5F5; /* Canvas / Surface Token (structureengineering-com-au) */
  --color-grey: #BEBEBE; /* Brand / Palette Token (structureengineering-com-au) */
  --wp--preset--aspect-ratio--square: 1; /* Design System Custom Token (structureengineering-com-au) */
  --wp--preset--aspect-ratio--4-3: 4/3; /* Design System Custom Token (structureengineering-com-au) */
  --wp--preset--aspect-ratio--3-4: 3/4; /* Design System Custom Token (structureengineering-com-au) */
  --wp--preset--aspect-ratio--3-2: 3/2; /* Design System Custom Token (structureengineering-com-au) */
  --wp--preset--aspect-ratio--2-3: 2/3; /* Design System Custom Token (structureengineering-com-au) */
  --wp--preset--aspect-ratio--16-9: 16/9; /* Design System Custom Token (structureengineering-com-au) */
  --wp--preset--aspect-ratio--9-16: 9/16; /* Design System Custom Token (structureengineering-com-au) */
  --wp--preset--color--black: #000000; /* Canvas / Surface Token (structureengineering-com-au) */
  --wp--preset--color--cyan-bluish-gray: #abb8c3; /* Brand / Palette Token (structureengineering-com-au) */
  --structureenginee-bg: #f5f5f5; /* Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) (structureengineering-com-au) */
  --structureenginee-ink: #000000; /* Primary Typography Ink (computed-derived) (structureengineering-com-au) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f5f5f5` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#000000` — grounded in live computed `main` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#ffffff` — grounded in `.background-color-white { background-color: white }` (`#ffffff`)
- **Interactive Accent / Highlight**: `#ffffff` — grounded in `ackground-color-gold .block-hea... { color: #ffffff }`
- **Secondary / Muted Copy**: `#777777` — grounded in `form-wrap .dropdown-menu>.disab... { color: #777777 }`
- **Structural Hairline Border**: `#ffffff` — grounded in `a.btn-with-arrow:hover { border-color: #ffffff }`
- **Variable Token (`--color-gold`)**: `#b9b36d` — grounded in `var(--color-gold)` in `:root`
- **Variable Token (`--color-grey`)**: `#bebebe` — grounded in `var(--color-grey)` in `:root`
- **Variable Token (`--wp--preset--color--cyan-bluish-gray`)**: `#abb8c3` — grounded in `var(--wp--preset--color--cyan-bluish-gray)` in stylesheet

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport)
- **Padding & Gutters**: `0.5rem` lateral canvas padding with `12px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 12px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `0.5rem` horizontal padding
- **Media Queries**: `@media (max-width: 479px)`, `@media (min-width: 375px)`, `@media (min-width: 769px)`, `@media (min-width: 1200px)`
- **Corner Radii**: `1.04px`, `0px`, `100%`, `50%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `SequelSans`
- **Body Font Stack**: `SequelSans`
- **Monospace / Technical Font Stack**: `PPFraktionMono`
- **H1 Display Rule**: live computed `h1` (`font-size: 81.6px`, `line-height: 81.6px`, `font-weight: 400`); rule `h1` (`font-size: 2em`)
- **H2 Section Rule**: live computed `h2` (`font-size: 81.6px`, `line-height: 81.6px`, `font-weight: 400`); rule `.h2` (`font-size: 3.7em`, `line-height: 1`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 20.8px`, `font-weight: 400`); rule `p` (`font-size: 0.8em`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 20.8px`, `font-weight: 400`); rule `small` (`font-size: 80%`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `structureengineering-com-au` (`Structure Consulting Engineers · Structural Engineering Sydney`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.top-nav> — `structureengineering-com-au`)**:
   - DOM & Selectors: Landmark `<nav class="top-nav font-PPFraktionMono">` (`878x93px`) hosting `Structure Consulting Engineers · Str` navigation (`About · Company · Careers · People · Sectors`), DOM attributes (`data-section-background-color="background-color-black"`, `data-rocket-prefetch`, `data-rocket-preload`, `data-rocket-async="style"`), and stylesheet rule `html { scrollbar-gutter: stable; }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.top-nav> — `structureengineering-com-au`)` (`structureengineering-com-au`) adapts across `@media (max-width: 479px)`, `@media (min-width: 375px)`, `@media (min-width: 769px)`, `@media (min-width: 1200px)` with `cubic-bezier(0.015,0.791,0.757,1.024)`, `cubic-bezier(0.76,0,0.24,1)`, `cubic-bezier(0.66,0,0.34,1)` transitions and links `About · Company · Careers · People · Sectors`.
2. **Hero Stage & Focal Lead (<section.section> — `A different approach to traditiona`)**:
   - DOM & Selectors: Landmark `<section class="section section-topbannerhome">` presenting display lead `A different approach to traditional structural en...` and copy excerpt *"Residential Northbridge House II"* over `#f5f5f5` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×2616px` mobile) sets `#f5f5f5` background with `#000000` headline `A different approach to traditional structural en...`.
3. **Primary Showcase & Content Grid (<section.section-intro> — `Northbridge House II`)**:
   - DOM & Selectors: Landmark `<section class="section section-intro">` rendering section `Northbridge House II` with copy *"Residential Castlecrag House"*, asset references (`gtm.js`, `www.googletagmanager.com`, `SequelSans-Medium.woff2`, `PPFraktionMono-Regular.woff2`), and grid rule `figure { border: none; padding: 0; display: inline-block; margin: 1em 0; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.section-intro> — `Northbridge House II`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 12px`) on desktop and Single-column vertical stack at `390px` viewport width with `0.5rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.section-spread> — `Castlecrag House`)**:
   - DOM & Selectors: Landmark `<section class="section section-spread">` framing `Castlecrag House` and `Marrickville House` (*"Residential Marrickville House"*) with `#ffffff` surface cards, `#ffffff` accents, and `img { pointer-events: none; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.section-spread> — `Castlecrag House`)` uses `1.04px`, `0px`, `100%`, `50%` radii, `#ffffff` highlights, and assets (gtm.js, www.googletagmanager.com, SequelSans-Medium.woff2).
5. **Colophon & Global Directory Footer (<footer.preloadergone> — `https://structureengineering.com.au/`)**:
   - DOM & Selectors: Landmark `<footer class="preloadergone">` anchoring `Structure Consulting Engineers ·` footer links (`About · Company · Careers · People · Sectors`), copy *"Through thoughtful design, clear communication and lateral t"*, and `#ffffff` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.preloadergone> — `https://structureengineering.com.au/`)` aligns to `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport) with `0.5rem` lateral canvas padding with `12px` grid gap and attributes (data-section-background-color="background-color-black", data-rocket-prefetch, data-rocket-preload).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Residential Northbridge House II"*
- Copy Excerpt 2: *"Residential Castlecrag House"*
- Copy Excerpt 3: *"Residential Marrickville House"*
- Copy Excerpt 4: *"Through thoughtful design, clear communication and lateral thinking, we turn compl..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.015,0.791,0.757,1.024)`, `cubic-bezier(0.76,0,0.24,1)`, `cubic-bezier(0.66,0,0.34,1)`
- **Extracted Stylesheet Rules (`structureengineering-com-au`)**:
- `html { scrollbar-gutter: stable; }`
- `figure { border: none; padding: 0; display: inline-block; margin: 1em 0; }`
- `img { pointer-events: none; }`
- `.rocket-lazyload { opacity: 0; transition: opacity 1s; }`
- `.rocket-lazyload.lazyloaded { opacity: 1; }`
- **Per-Selector Transition Rules**:
- **Selector `.preload *`**: `transition: none !important` extracted from `structureengineering-com-au` stylesheet.
- **Selector `.rocket-lazyload`**: `transition: opacity 1s` extracted from `structureengineering-com-au` stylesheet.
- **Selector `.media-link .media`**: `transition: ease-in-out 0.5s` extracted from `structureengineering-com-au` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.015,0.791,0.757,1.024)`)**: Governs interactive state transitions across `<nav.top-nav>` and `<section.section-intro>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `9912px` across 8 distinct viewport chapters.
- **Vertical Chapter Sequence**: A different approach to tra... (0%) -> Northbridge House II (9%) -> Section @ 28% (28%) -> Do it once. Do it right. (47%) -> TAHMOOR SPORTS COMPLEX (57%) -> SPIN (75%) -> NORTHBRIDGE HOUSE II (95%) -> BONDI HOUSE II (100%).
- **Hover Micro-Interaction (`primary_cta`)**: Animate `color, backgroundColor` with `0.25s ease`.
- **Multi-Page Routes**: Scaffold internal routes `/journal/` (listing, MPA), `/sectors/residential-structural-engineers/` (detail, direct), `/people/` (about, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `structureengineering-com-au`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | A different approach to traditional structura... | `1` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `9%` | Northbridge House II | `2` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `2550px` | `28%` | Section @ 28% | `2` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `4250px` | `47%` | Do it once. Do it right. | `1` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `5100px` | `57%` | TAHMOOR SPORTS COMPLEX | `1` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `6800px` | `75%` | SPIN | `1` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `8500px` | `95%` | NORTHBRIDGE HOUSE II | `1` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `8979px` | `100%` | BONDI HOUSE II | `1` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | A different approach to traditional struc... | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `4166px` | `50%` | Not all structural engineering businesses... | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `8311px` | `100%` | Let's collaborate | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `listing` | `https://structureengineering.com.au/journal/` | Journal | `3573px` | `MPA` (`1663ms`) | [subpage-01-journal.webp](assets/subpage-01-journal.webp) |
| `2` | `detail` | `https://structureengineering.com.au/sectors/residential-structural-engineers/` | Most residentialstructural engineers... | `5843px` | `direct` (`1122ms`) | [subpage-02-sectors-residential-structural-engin.webp](assets/subpage-02-sectors-residential-structural-engin.webp) |
| `3` | `about` | `https://structureengineering.com.au/people/` | People | `3432px` | `direct` (`735ms`) | [subpage-03-people.webp](assets/subpage-03-people.webp) |

