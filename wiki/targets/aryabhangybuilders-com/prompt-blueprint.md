---
title: "UI Prompt Blueprint: aryabhangybuilders-com"
date: 2026-11-24
captured_at: 2026-11-24
target: "aryabhangybuilders-com"
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
archetype: "Light-Substrate Editorial & Modular Grid System (`#f7f8f9` canvas, `#222222` ink, `#375efb` accent)"
---

# UI Design System & Master Generation Blueprint: aryabhangybuilders-com

> **Premium Builders In Kochi · Flats & Apartments · Arya Bhangy** (https://aryabhangybuilders.com/) — RERA-registered 2.5, 3 & 4 BHK apartments in Vyttila and Kumbalam, Kochi, from a family group building since 1969. Book a site visit.

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Premium Builders In Kochi · Flats & Apartments · Arya Bhangy** (`https://aryabhangybuilders.com/`). RERA-registered 2.5, 3 & 4 BHK apartments in Vyttila and Kumbalam, Kochi, from a family group building since 1969. Book a site visit.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#f7f8f9` canvas, `#222222` ink, `#375efb` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f7f8f9` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#222222` primary typography and `#375efb` accents.
  - **Grounded Typographic Hierarchy**: Pairs `CS Alpha` for display copy (`Premium Apartments in Kochi, by Arya`) with `Segoe UI`.
  - **Calibrated Spatial Grid & Motion**: Combines `100vw` container bounds (`gap: var(--row-gap)`, padding `20px`) with `cubic-bezier(0,0,0.25,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=8464px` / doc `9619px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `100vw` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `20px` lateral canvas padding with `var(--row-gap)` grid gap.
- **Border Radius Scale**: `3px`, `var(--border-radius)`, `2px`, `4px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 100vw`, `gap: var(--row-gap)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `20px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:768px)`, `@media (min-width:769px) and (max-width:1024px)`, `@media (min-width:1025px)`, `@media (min-width:-1)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f7f8f9` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#222222` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#a4c639` | `.elementor-social-icon-android { background-color: #a4c639 }` |
| **Interactive Accent / Highlight** | `#375efb` | `.elementor .e-button-base { background-color: #375efb }` |
| **Secondary / Muted Copy** | `#808080` | live computed `hr` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#dedfe0` | `th { border: #dedfe0 }` |
| **Variable Token (`--contrast-2`)** | `#575760` | `var(--contrast-2)` in `:root` |
| **Variable Token (`--contrast-3`)** | `#b2b2be` | `var(--contrast-3)` in `:root` |
| **Variable Token (`--base`)** | `#f0f0f0` | `var(--base)` in `:root` |
| **Variable Token (`--base-3`)** | `#ffffff` | `var(--base-3)` in `:root` |
| **Variable Token (`--accent`)** | `#1e73be` | `var(--accent)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--contrast` | `#222222` | Color / Atmospheric Token |
| `--contrast-2` | `#575760` | Color / Atmospheric Token |
| `--contrast-3` | `#b2b2be` | Color / Atmospheric Token |
| `--base` | `#f0f0f0` | Color / Atmospheric Token |
| `--base-2` | `#f7f8f9` | Color / Atmospheric Token |
| `--base-3` | `#ffffff` | Color / Atmospheric Token |
| `--accent` | `#1e73be` | Brand / Palette Token |
| `--gp-search-modal-bg-color` | `var(--base-3)` | Canvas / Surface Token |
| `--gp-search-modal-text-color` | `var(--contrast)` | Typography Ink Token |
| `--gp-search-modal-overlay-bg-color` | `rgba(0,0,0,0.2)` | Canvas / Surface Token |
| `--e-global-color-v4-white` | `var(--white)` | Canvas / Surface Token |
| `--e-global-color-v4-black` | `var(--black)` | Canvas / Surface Token |
| `--e-global-color-v4-cream-50` | `var(--cream-50)` | Brand / Palette Token |
| `--e-global-color-v4-cream-100` | `var(--cream-100)` | Brand / Palette Token |
| `--e-global-color-v4-cream-150` | `var(--cream-150)` | Brand / Palette Token |
| `--e-global-color-v4-cream-200` | `var(--cream-200)` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `CS Alpha`.
- **Primary Body Stack**: `Segoe UI`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 40px`, `line-height: 46px`, `font-weight: 400`, `letter-spacing: -0.6px`); CSS variables `--page-title-display: block`.
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 40px`, `line-height: 46px`, `font-weight: 400`, `letter-spacing: -0.6px`); rule `h2` (`font-size: 36px`).
- **Body Copy**: live computed `body` (`font-size: 17px`, `line-height: 25.5px`, `font-weight: 400`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 17px`, `line-height: 25.5px`, `font-weight: 400`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0,0,0.25,1)`, `cubic-bezier(0.22,0.61,0.36,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `input`**: `transition: color .1s ease-in-out,background-color .1s ease-in-out` extracted from `aryabhangybuilders-com` stylesheet.
- **Selector `.main-navigation ul ul`**: `transition: opacity 80ms linear` extracted from `aryabhangybuilders-com` stylesheet.
- **Selector `.main-navigation.toggled .main-na...`**: `transition: 0s` extracted from `aryabhangybuilders-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,0.25,1)`)**: Governs interactive state transitions across `<header.elementor>` and `<article.page>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Swiper Touch Carousel Engine, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `9619px`, deepest scrollY reached `8464px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: `Lenis`, `GSAP/ScrollTrigger`.
- **Hover Physics (`primary_cta` · `View Projects`)**: `color`: `rgb(30, 115, 190)` -> `rgb(34, 34, 34)`; `borderColor`: `rgb(30, 115, 190)` -> `rgb(34, 34, 34)` (`transition-duration: 0.1s, 0.1s`, `timing: ease-in-out, ease-in-out`).
- **Route Transition Architecture**: First internal navigation (`/residential_project/rhinestone/`) measured as `direct` in `4343ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Premium Builders In Kochi · Flats & Apartm │
│ ====================================================================== │
│ [ <header.elementor> (1440x0px)       | Home · Residential · Commerc ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <article.post-2414> (w=1440px)                         | │
│ | H1: Premium Apartments in Kochi, by Arya Bhangy Builders           | │
│ | Substrate: #f7f8f9 | Ink: #222222 | Accent: #375efb                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<article.page>) max-w: 100vw                        | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Years in Business            |  | sq.ft. Developed in Kochi    | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<article.type-page>) — Transparent Transacti        | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.elementor>  ) | https://aryabhangybuilders.com/      │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--ro)   │
│ ====================================================================== │
│ [ HEADER BAR (<header.elementor>      ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<article.post-2414>) — 390px Vertical Lead             | │
│ | H1: Premium Apartments in Kochi, by Arya Bhangy Builders           | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<article.page>) — 1-Col Stack                      | │
│ | [ Item 1: Years in Business                                      ] | │
│ | [ Item 2: sq.ft. Developed in Kochi                              ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<article.type-page>) — 1-Col (Transparent Transa)    | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.elementor>  ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.elementor> — `aryabhangybuilders-com`)**:
   - Landmark `<header class="elementor elementor-5070">` (`1440x0px`) hosting `Premium Builders In Kochi · Flats & ` navigation (`Home · Residential · Commercial · Our Legacy · Testimonials`), DOM attributes (`data-elementor-device-mode="desktop"`, `data-opened="1"`, `data-elementor-type="header"`, `data-elementor-id="5070"`), and stylesheet rule `main { display:block }`.
2. **Hero Stage & Focal Lead (<article.post-2414> — `Premium Apartments in Kochi, by Ar`)**:
   - Landmark `<article class="post-2414 page">` presenting display lead `Premium Apartments in Kochi, by Arya Bhangy Builders` and copy excerpt *"Est. 1969 · Kochi, Kerala"* over `#f7f8f9` canvas and `#222222` ink.
3. **Primary Showcase & Content Grid (<article.page> — `Years in Business`)**:
   - Landmark `<article class="post-2414 page">` rendering section `Years in Business` with copy *"F o r u s , r e a l e s t a t e i s m o r e t h a n c o n s t r u"*, asset references (`1806948866520083`, `fbevents.js`, `gtm.js`, `embed`), and grid rule `progress { vertical-align:baseline }`.
4. **Interactive Detail & Feature Matrix (<article.type-page> — `sq.ft. Developed in Kochi`)**:
   - Landmark `<article class="post-2414 page">` framing `sq.ft. Developed in Kochi` and `Transparent Transactions` (*"Apartments across Kochi, in the areas people are actually looking"*) with `#a4c639` surface cards, `#375efb` accents, and `html { box-sizing:border-box }`.
5. **Colophon & Global Directory Footer (<footer.elementor> — `https://aryabhangybuilders.com/`)**:
   - Landmark `<footer class="elementor elementor-6448">` anchoring `Premium Builders In Kochi · Flat` footer links (`Home · Residential · Commercial · Our Legacy · Testimonials`), copy *"Commercial spaces built for the businesses inside them. Prac"*, and `#dedfe0` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `Premium Apartments in Kochi, by Arya Bhangy Builders` · sticky/fixed elements: `4`
- **Step 02** (`y=850px`, `10%`): Active landmark `Years in Business` · sticky/fixed elements: `3`
- **Step 03** (`y=2550px`, `30%`): Active landmark `Section @ 30%` · sticky/fixed elements: `3`
- **Step 04** (`y=3400px`, `40%`): Active landmark `Section @ 40%` · sticky/fixed elements: `3`
- **Step 05** (`y=5100px`, `59%`): Active landmark `Section @ 59%` · sticky/fixed elements: `3`
- **Step 06** (`y=5950px`, `68%`): Active landmark `Section @ 68%` · sticky/fixed elements: `3`
- **Step 07** (`y=7650px`, `88%`): Active landmark `Curated Insights from Experts` · sticky/fixed elements: `3`
- **Step 08** (`y=8464px`, `97%`): Active landmark `Why we build fewer projects than we could` · sticky/fixed elements: `3`

### Multi-Page Internal Route Map
- **Detail Route (`/residential_project/rhinestone/`)**: `https://aryabhangybuilders.com/residential_project/rhinestone/` — H1: `Rhinestone: Completed Apartments in Panampilly Na...`, scrollHeight `6615px`, transition `direct` (`4343ms`)
- **About Route (`/about-us/`)**: `https://aryabhangybuilders.com/about-us/` — H1: `Premium Residential & Commercial Spaces Across Ko...`, scrollHeight `9853px`, transition `direct` (`5159ms`)
- **Other Route (`/residential/`)**: `https://aryabhangybuilders.com/residential/` — H1: `Apartments & Flats in Kochi, Ernakulam`, scrollHeight `2720px`, transition `direct` (`1744ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: aryabhangybuilders-com (Premium Builders In Kochi · Flats & Apartments · Arya Bhangy)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `aryabhangybuilders-com` (**Premium Builders In Kochi · Flats & Apartments · Arya Bhangy** — `https://aryabhangybuilders.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#f7f8f9` canvas, `#222222` ink, `#375efb` accent).
- **Identity & Domain Context**: RERA-registered 2.5, 3 & 4 BHK apartments in Vyttila and Kumbalam, Kochi, from a family group building since 1969. Book a site visit.
- **Primary Substrate**: `#f7f8f9` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#222222`, **Accent / Highlight**: `#375efb`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f7f8f9` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#222222` primary typography and `#375efb` accents.
  - **Grounded Typographic Hierarchy**: Pairs `CS Alpha` for display copy (`Premium Apartments in Kochi, by Arya`) with `Segoe UI`.
  - **Calibrated Spatial Grid & Motion**: Combines `100vw` container bounds (`gap: var(--row-gap)`, padding `20px`) with `cubic-bezier(0,0,0.25,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `aryabhangybuilders-com` in your global stylesheet:

:root {
  /* Premium Builders In Kochi · Flats & Apartments · Arya Bhangy (aryabhangybuilders-com) — Live-Grounded CSS Variables */
  --contrast: #222222; /* Color / Atmospheric Token (aryabhangybuilders-com) */
  --contrast-2: #575760; /* Color / Atmospheric Token (aryabhangybuilders-com) */
  --contrast-3: #b2b2be; /* Color / Atmospheric Token (aryabhangybuilders-com) */
  --base: #f0f0f0; /* Color / Atmospheric Token (aryabhangybuilders-com) */
  --base-2: #f7f8f9; /* Color / Atmospheric Token (aryabhangybuilders-com) */
  --base-3: #ffffff; /* Color / Atmospheric Token (aryabhangybuilders-com) */
  --accent: #1e73be; /* Brand / Palette Token (aryabhangybuilders-com) */
  --gp-search-modal-bg-color: var(--base-3); /* Canvas / Surface Token (aryabhangybuilders-com) */
  --gp-search-modal-text-color: var(--contrast); /* Typography Ink Token (aryabhangybuilders-com) */
  --gp-search-modal-overlay-bg-color: rgba(0,0,0,0.2); /* Canvas / Surface Token (aryabhangybuilders-com) */
  --e-global-color-v4-white: var(--white); /* Canvas / Surface Token (aryabhangybuilders-com) */
  --e-global-color-v4-black: var(--black); /* Canvas / Surface Token (aryabhangybuilders-com) */
  --e-global-color-v4-cream-50: var(--cream-50); /* Brand / Palette Token (aryabhangybuilders-com) */
  --e-global-color-v4-cream-100: var(--cream-100); /* Brand / Palette Token (aryabhangybuilders-com) */
  --e-global-color-v4-cream-150: var(--cream-150); /* Brand / Palette Token (aryabhangybuilders-com) */
  --e-global-color-v4-cream-200: var(--cream-200); /* Brand / Palette Token (aryabhangybuilders-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f7f8f9` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#222222` — grounded in live computed `main` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#a4c639` — grounded in `.elementor-social-icon-android { background-color: #a4c639 }`
- **Interactive Accent / Highlight**: `#375efb` — grounded in `.elementor .e-button-base { background-color: #375efb }`
- **Secondary / Muted Copy**: `#808080` — grounded in live computed `hr` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#dedfe0` — grounded in `th { border: #dedfe0 }`
- **Variable Token (`--contrast-2`)**: `#575760` — grounded in `var(--contrast-2)` in `:root`
- **Variable Token (`--contrast-3`)**: `#b2b2be` — grounded in `var(--contrast-3)` in `:root`
- **Variable Token (`--base`)**: `#f0f0f0` — grounded in `var(--base)` in `:root`
- **Variable Token (`--base-3`)**: `#ffffff` — grounded in `var(--base-3)` in `:root`
- **Variable Token (`--accent`)**: `#1e73be` — grounded in `var(--accent)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `100vw` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `20px` lateral canvas padding with `var(--row-gap)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 100vw`, `gap: var(--row-gap)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `20px` horizontal padding
- **Media Queries**: `@media (max-width:768px)`, `@media (min-width:769px) and (max-width:1024px)`, `@media (min-width:1025px)`, `@media (min-width:-1)`
- **Corner Radii**: `3px`, `var(--border-radius)`, `2px`, `4px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `CS Alpha`
- **Body Font Stack**: `Segoe UI`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 40px`, `line-height: 46px`, `font-weight: 400`, `letter-spacing: -0.6px`); CSS variables `--page-title-display: block`
- **H2 Section Rule**: live computed `h2` (`font-size: 40px`, `line-height: 46px`, `font-weight: 400`, `letter-spacing: -0.6px`); rule `h2` (`font-size: 36px`)
- **Body Copy Rule**: live computed `body` (`font-size: 17px`, `line-height: 25.5px`, `font-weight: 400`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 17px`, `line-height: 25.5px`, `font-weight: 400`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `aryabhangybuilders-com` (`Premium Builders In Kochi · Flats & Apartments · Arya Bhangy`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.elementor> — `aryabhangybuilders-com`)**:
   - DOM & Selectors: Landmark `<header class="elementor elementor-5070">` (`1440x0px`) hosting `Premium Builders In Kochi · Flats & ` navigation (`Home · Residential · Commercial · Our Legacy · Testimonials`), DOM attributes (`data-elementor-device-mode="desktop"`, `data-opened="1"`, `data-elementor-type="header"`, `data-elementor-id="5070"`), and stylesheet rule `main { display:block }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.elementor> — `aryabhangybuilders-com`)` (`aryabhangybuilders-com`) adapts across `@media (max-width:768px)`, `@media (min-width:769px) and (max-width:1024px)`, `@media (min-width:1025px)`, `@media (min-width:-1)` with `cubic-bezier(0,0,0.25,1)`, `cubic-bezier(0.22,0.61,0.36,1)` transitions and links `Home · Residential · Commercial · Our Legacy · Testimonials`.
2. **Hero Stage & Focal Lead (<article.post-2414> — `Premium Apartments in Kochi, by Ar`)**:
   - DOM & Selectors: Landmark `<article class="post-2414 page">` presenting display lead `Premium Apartments in Kochi, by Arya Bhangy Builders` and copy excerpt *"Est. 1969 · Kochi, Kerala"* over `#f7f8f9` canvas and `#222222` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×2616px` mobile) sets `#f7f8f9` background with `#222222` headline `Premium Apartments in Kochi, by Arya Bhangy Builders`.
3. **Primary Showcase & Content Grid (<article.page> — `Years in Business`)**:
   - DOM & Selectors: Landmark `<article class="post-2414 page">` rendering section `Years in Business` with copy *"F o r u s , r e a l e s t a t e i s m o r e t h a n c o n s t r u"*, asset references (`1806948866520083`, `fbevents.js`, `gtm.js`, `embed`), and grid rule `progress { vertical-align:baseline }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<article.page> — `Years in Business`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 100vw`, `gap: var(--row-gap)`) on desktop and Single-column vertical stack at `390px` viewport width with `20px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.type-page> — `sq.ft. Developed in Kochi`)**:
   - DOM & Selectors: Landmark `<article class="post-2414 page">` framing `sq.ft. Developed in Kochi` and `Transparent Transactions` (*"Apartments across Kochi, in the areas people are actually looking"*) with `#a4c639` surface cards, `#375efb` accents, and `html { box-sizing:border-box }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.type-page> — `sq.ft. Developed in Kochi`)` uses `3px`, `var(--border-radius)`, `2px`, `4px` radii, `#375efb` highlights, and assets (1806948866520083, fbevents.js, gtm.js).
5. **Colophon & Global Directory Footer (<footer.elementor> — `https://aryabhangybuilders.com/`)**:
   - DOM & Selectors: Landmark `<footer class="elementor elementor-6448">` anchoring `Premium Builders In Kochi · Flat` footer links (`Home · Residential · Commercial · Our Legacy · Testimonials`), copy *"Commercial spaces built for the businesses inside them. Prac"*, and `#dedfe0` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.elementor> — `https://aryabhangybuilders.com/`)` aligns to `100vw` (non-`@media` desktop container stylesheet rule) with `20px` lateral canvas padding with `var(--row-gap)` grid gap and attributes (data-elementor-device-mode="desktop", data-opened="1", data-elementor-type="header").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Est. 1969 · Kochi, Kerala"*
- Copy Excerpt 2: *"F o r u s , r e a l e s t a t e i s m o r e t h a n c o n s t r u c t i o n . I t..."*
- Copy Excerpt 3: *"Apartments across Kochi, in the areas people are actually looking to live. Well-bu..."*
- Copy Excerpt 4: *"Commercial spaces built for the businesses inside them. Practical layouts, solid c..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0,0,0.25,1)`, `cubic-bezier(0.22,0.61,0.36,1)`
- **Extracted Stylesheet Rules (`aryabhangybuilders-com`)**:
- `main { display:block }`
- `progress { vertical-align:baseline }`
- `html { box-sizing:border-box }`
- `before { box-sizing:inherit }`
- `textarea { font-family:inherit;font-size:100%;margin:0 }`
- **Per-Selector Transition Rules**:
- **Selector `input`**: `transition: color .1s ease-in-out,background-color .1s ease-in-out` extracted from `aryabhangybuilders-com` stylesheet.
- **Selector `.main-navigation ul ul`**: `transition: opacity 80ms linear` extracted from `aryabhangybuilders-com` stylesheet.
- **Selector `.main-navigation.toggled .main-na...`**: `transition: 0s` extracted from `aryabhangybuilders-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,0.25,1)`)**: Governs interactive state transitions across `<header.elementor>` and `<article.page>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Swiper Touch Carousel Engine, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `9619px` across 8 distinct viewport chapters using Lenis, GSAP/ScrollTrigger.
- **Vertical Chapter Sequence**: Premium Apartments in Kochi... (0%) -> Years in Business (10%) -> Section @ 30% (30%) -> Section @ 40% (40%) -> Section @ 59% (59%) -> Section @ 68% (68%) -> Curated Insights from Experts (88%) -> Why we build fewer projects... (97%).
- **Hover Micro-Interaction (`primary_cta`)**: Animate `color, borderColor` with `0.1s, 0.1s ease-in-out, ease-in-out`.
- **Multi-Page Routes**: Scaffold internal routes `/residential_project/rhinestone/` (detail, direct), `/about-us/` (about, direct), `/residential/` (other, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `aryabhangybuilders-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | Premium Apartments in Kochi, by Arya Bhangy B... | `4` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `10%` | Years in Business | `3` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `2550px` | `30%` | Section @ 30% | `3` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `3400px` | `40%` | Section @ 40% | `3` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `5100px` | `59%` | Section @ 59% | `3` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `5950px` | `68%` | Section @ 68% | `3` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `7650px` | `88%` | Curated Insights from Experts | `3` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `8464px` | `97%` | Why we build fewer projects than we could | `3` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | Premium Apartments in Kochi, by Arya Bhan... | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `3116px` | `50%` | Section @ 48% | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `6233px` | `100%` | Quick Links | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `detail` | `https://aryabhangybuilders.com/residential_project/rhinestone/` | Rhinestone: Completed Apartments in P... | `6615px` | `direct` (`4343ms`) | [subpage-01-residential-project-rhinestone.webp](assets/subpage-01-residential-project-rhinestone.webp) |
| `2` | `about` | `https://aryabhangybuilders.com/about-us/` | Premium Residential & Commercial Spac... | `9853px` | `direct` (`5159ms`) | [subpage-02-about-us.webp](assets/subpage-02-about-us.webp) |
| `3` | `other` | `https://aryabhangybuilders.com/residential/` | Apartments & Flats in Kochi, Ernakulam | `2720px` | `direct` (`1744ms`) | [subpage-03-residential.webp](assets/subpage-03-residential.webp) |

