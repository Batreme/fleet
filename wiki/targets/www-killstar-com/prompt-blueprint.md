---
title: "UI Prompt Blueprint: www-killstar-com"
date: 2026-11-23
captured_at: 2026-11-23
target: "www-killstar-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#f5f5f5` canvas, `#111111` ink, `#f1c40f` accent)"
---

# UI Design System & Master Generation Blueprint: www-killstar-com

> **KILLSTAR** (https://www.killstar.com/) — Clothing & Lifestyle company with a twist of darkness, channeling emotional power and raw energy into every thread.

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **KILLSTAR** (`https://www.killstar.com/`). Clothing & Lifestyle company with a twist of darkness, channeling emotional power and raw energy into every thread.
- **Final Redirected URL**: [https://eu.killstar.com/](https://eu.killstar.com/)
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#f5f5f5` canvas, `#111111` ink, `#f1c40f` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f5f5f5` (live computed `main` `background-color` (`computed_styles.json`)) paired with `#111111` primary typography and `#f1c40f` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Inter` for display copy (`Winter's Vale Coat`) with `Inter` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 4px`, padding `.75rem`) with `cubic-bezier(0.4,0,0.2,1)` easing and Swiper Touch Carousel Engine, Barba.js Page Transition Router.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport).
- **Canvas Lateral Padding & Spacing**: `.75rem` lateral canvas padding with `4px` grid gap.
- **Border Radius Scale**: `5px`, `25px`, `6px`, `20%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 4px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `.75rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width:440px)`, `@media (max-width:1024px)`, `@media (max-width:768px)`, `@media (min-width:1220px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f5f5f5` | live computed `main` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#111111` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#faf9f8` | `var(--atlas-background-main)` in `:root` |
| **Interactive Accent / Highlight** | `#f1c40f` | `rm-box .jconfirm-buttons button... { background-color: #f1c40f }` |
| **Secondary / Muted Copy** | `#747576` | `var(--atlas-text-placeholder)` in `:root` |
| **Structural Hairline Border** | `#41a1e6` | `var(--atlas-border-focus)` in `:root` |
| **Variable Token (`--color-white`)** | `#dcdcd0` | `var(--color-white)` in `:root` |
| **Variable Token (`--color-stone`)** | `#b3ada1` | `var(--color-stone)` in `:root` |
| **Variable Token (`--color-shadow`)** | `#232323` | `var(--color-shadow)` in `:root` |
| **Variable Token (`--color-midnight-light`)** | `#3b3838` | `var(--color-midnight-light)` in `:root` |
| **Variable Token (`--color-bone`)** | `#ebebeb` | `var(--color-bone)` in `:root` |
| **Variable Token (`--color-bone-dark`)** | `#d4d4d4` | `var(--color-bone-dark)` in `:root` |
| **Variable Token (`--color-success`)** | `#32c079` | `var(--color-success)` in `:root` |
| **Variable Token (`--color-failure`)** | `#8b0910` | `var(--color-failure)` in `:root` |
| **Variable Token (`--color-warning`)** | `#ffaa33` | `var(--color-warning)` in `:root` |
| **Variable Token (`--atlas-background-content`)** | `#ffffff` | `var(--atlas-background-content)` in `:root` |
| **Variable Token (`--atlas-background-success`)** | `#518b22` | `var(--atlas-background-success)` in `:root` |
| **Variable Token (`--atlas-background-error`)** | `#be2119` | `var(--atlas-background-error)` in `:root` |
| **Variable Token (`--atlas-text-primary`)** | `#1d1e20` | `var(--atlas-text-primary)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-white` | `#DCDCD0` | Canvas / Surface Token |
| `--color-stone` | `#B3ADA1` | Brand / Palette Token |
| `--color-midnight` | `#111` | Brand / Palette Token |
| `--color-shadow` | `#232323` | Brand / Palette Token |
| `--color-midnight-light` | `#3B3838` | Canvas / Surface Token |
| `--color-bone-light` | `#f5f5f5` | Canvas / Surface Token |
| `--color-bone` | `#ebebeb` | Brand / Palette Token |
| `--color-bone-dark` | `#d4d4d4` | Canvas / Surface Token |
| `--color-success` | `#32C079` | Brand / Palette Token |
| `--color-failure` | `#8b0910` | Brand / Palette Token |
| `--color-warning` | `#FFAA33` | Brand / Palette Token |
| `--atlas-background-main` | `#faf9f8` | Canvas / Surface Token |
| `--atlas-background-content` | `#ffffff` | Canvas / Surface Token |
| `--atlas-background-success` | `#518b22` | Canvas / Surface Token |
| `--atlas-background-error` | `#be2119` | Canvas / Surface Token |
| `--atlas-text-primary` | `#1d1e20` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Inter`.
- **Primary Body Stack**: `Inter`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: CSS variables `--atlas-font-size-display: 40px`, `--atlas-line-height-display: 52px`, `--atlas-margin-display: 24px`; rule `.title` (`font-size: 13px`).
- **Section Heading (`H2`)**: CSS variables `--atlas-font-size-h2: 32px`, `--atlas-line-height-h2: 40px`, `--atlas-margin-h2: 24px`; rule `h2` (`font-size: 2.5em`, `font-weight: 900`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 20px`, `font-weight: 400`); rule `p` (`line-height: 1.6`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 20px`, `font-weight: 400`); CSS variables `--atlas-font-size-small: 14px`, `--atlas-line-height-small: 20px`, `--atlas-margin-small: 8px`; rule `.label` (`font-size: .875em`, `letter-spacing: 2.8px`, `font-weight: 500`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.4,0,0.2,1)`, `cubic-bezier(0.34,1.15,0.64,1)`, `cubic-bezier(0.6,0,0.4,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.button`**: `transition: all .3s ease-in-out` extracted from `www-killstar-com` stylesheet.
- **Selector `.button:after`**: `transition: transform .3s ease-in-out` extracted from `www-killstar-com` stylesheet.
- **Selector `button.route-continue-without-cov...`**: `transition: all .3s ease-in-out` extracted from `www-killstar-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.4,0,0.2,1)`)**: Governs interactive state transitions across `<header.shopify-section>` and `<section.section-model-image-blocks>`.
- **Runtime Interaction Engine**: Integrates Swiper Touch Carousel Engine, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — KILLSTAR                                   │
│ ====================================================================== │
│ [ <header.shopify-sectio (1440x71px)  | NEW IN · DRESSES · WOMENS ·  ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.shopify-section> (w=1440px)                   | │
│ | H1: Winter's Vale Coat                                             | │
│ | Substrate: #f5f5f5 | Ink: #111111 | Accent: #f1c40f                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.section-model-ima) max-w: 1440px           | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Skultra Cropped Cardigan     |  | Basilica Cape                | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.section-full-widt) — CRUCIFIX SLOUCH BAG   | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.shopify-sect) | https://www.killstar.com/            │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 4px)        │
│ ====================================================================== │
│ [ HEADER BAR (<header.shopify-section>) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.shopify-section) — 390px Vertical Lead        | │
│ | H1: Winter's Vale Coat                                             | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.section-model) — 1-Col Stack              | │
│ | [ Item 1: Skultra Cropped Cardigan                               ] | │
│ | [ Item 2: Basilica Cape                                          ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.section-full-wi) — 1-Col (CRUCIFIX SLOUCH BA) │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.shopify-sect) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.shopify-section> — `www-killstar-com`)**:
   - Landmark `<header class="shopify-section shopify-section-group-header-group">` (`1440x71px`) hosting `KILLSTAR` navigation (`NEW IN · DRESSES · WOMENS · PLUS · MENS`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-shop-id="53907226789"`, `data-venmo-supported="false"`, `data-environment="production"`), and stylesheet rule `button { box-sizing:border-box;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.shopify-section> — `Winter's Vale Coat`)**:
   - Landmark `<section class="shopify-section section-full-width-media">` presenting display lead `Winter's Vale Coat` and copy excerpt *"We use cookies & other technologies to provide a personalised exp"* over `#f5f5f5` canvas and `#111111` ink.
3. **Primary Showcase & Content Grid (<section.section-model-image-blocks> — `Skultra Cropped Cardigan`)**:
   - Landmark `<section class="shopify-section section-model-image-blocks">` rendering section `Skultra Cropped Cardigan` with copy *"Please select a Size"*, asset references (`reamaze-push.js`, `tp.min.js`, `37086_1783060609.js`, `init.js`), and grid rule `section { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.section-full-width-media> — `Basilica Cape`)**:
   - Landmark `<section class="shopify-section section-full-width-media">` framing `Basilica Cape` and `CRUCIFIX SLOUCH BAG` (*"Please select a Colour"*) with `#faf9f8` surface cards, `#f1c40f` accents, and `table { border-collapse:collapse;border-spacing:0 }`.
5. **Colophon & Global Directory Footer (<footer.shopify-section> — `https://www.killstar.com/`)**:
   - Landmark `<footer class="shopify-section shopify-section-group-footer-group">` anchoring `KILLSTAR` footer links (`NEW IN · DRESSES · WOMENS · PLUS · MENS`), copy *"Please select a Material Content"*, and `#41a1e6` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-killstar-com (KILLSTAR)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-killstar-com` (**KILLSTAR** — `https://www.killstar.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#f5f5f5` canvas, `#111111` ink, `#f1c40f` accent).
- **Identity & Domain Context**: Clothing & Lifestyle company with a twist of darkness, channeling emotional power and raw energy into every thread.
- **Primary Substrate**: `#f5f5f5` (live computed `main` `background-color` (`computed_styles.json`)), **Primary Ink**: `#111111`, **Accent / Highlight**: `#f1c40f`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f5f5f5` (live computed `main` `background-color` (`computed_styles.json`)) paired with `#111111` primary typography and `#f1c40f` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Inter` for display copy (`Winter's Vale Coat`) with `Inter` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 4px`, padding `.75rem`) with `cubic-bezier(0.4,0,0.2,1)` easing and Swiper Touch Carousel Engine, Barba.js Page Transition Router.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-killstar-com` in your global stylesheet:

:root {
  /* KILLSTAR (www-killstar-com) — Live-Grounded CSS Variables */
  --color-white: #DCDCD0; /* Canvas / Surface Token (www-killstar-com) */
  --color-stone: #B3ADA1; /* Brand / Palette Token (www-killstar-com) */
  --color-midnight: #111; /* Brand / Palette Token (www-killstar-com) */
  --color-shadow: #232323; /* Brand / Palette Token (www-killstar-com) */
  --color-midnight-light: #3B3838; /* Canvas / Surface Token (www-killstar-com) */
  --color-bone-light: #f5f5f5; /* Canvas / Surface Token (www-killstar-com) */
  --color-bone: #ebebeb; /* Brand / Palette Token (www-killstar-com) */
  --color-bone-dark: #d4d4d4; /* Canvas / Surface Token (www-killstar-com) */
  --color-success: #32C079; /* Brand / Palette Token (www-killstar-com) */
  --color-failure: #8b0910; /* Brand / Palette Token (www-killstar-com) */
  --color-warning: #FFAA33; /* Brand / Palette Token (www-killstar-com) */
  --atlas-background-main: #faf9f8; /* Canvas / Surface Token (www-killstar-com) */
  --atlas-background-content: #ffffff; /* Canvas / Surface Token (www-killstar-com) */
  --atlas-background-success: #518b22; /* Canvas / Surface Token (www-killstar-com) */
  --atlas-background-error: #be2119; /* Canvas / Surface Token (www-killstar-com) */
  --atlas-text-primary: #1d1e20; /* Typography Ink Token (www-killstar-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f5f5f5` — grounded in live computed `main` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#111111` — grounded in live computed `main` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#faf9f8` — grounded in `var(--atlas-background-main)` in `:root`
- **Interactive Accent / Highlight**: `#f1c40f` — grounded in `rm-box .jconfirm-buttons button... { background-color: #f1c40f }`
- **Secondary / Muted Copy**: `#747576` — grounded in `var(--atlas-text-placeholder)` in `:root`
- **Structural Hairline Border**: `#41a1e6` — grounded in `var(--atlas-border-focus)` in `:root`
- **Variable Token (`--color-white`)**: `#dcdcd0` — grounded in `var(--color-white)` in `:root`
- **Variable Token (`--color-stone`)**: `#b3ada1` — grounded in `var(--color-stone)` in `:root`
- **Variable Token (`--color-shadow`)**: `#232323` — grounded in `var(--color-shadow)` in `:root`
- **Variable Token (`--color-midnight-light`)**: `#3b3838` — grounded in `var(--color-midnight-light)` in `:root`
- **Variable Token (`--color-bone`)**: `#ebebeb` — grounded in `var(--color-bone)` in `:root`
- **Variable Token (`--color-bone-dark`)**: `#d4d4d4` — grounded in `var(--color-bone-dark)` in `:root`
- **Variable Token (`--color-success`)**: `#32c079` — grounded in `var(--color-success)` in `:root`
- **Variable Token (`--color-failure`)**: `#8b0910` — grounded in `var(--color-failure)` in `:root`
- **Variable Token (`--color-warning`)**: `#ffaa33` — grounded in `var(--color-warning)` in `:root`
- **Variable Token (`--atlas-background-content`)**: `#ffffff` — grounded in `var(--atlas-background-content)` in `:root`
- **Variable Token (`--atlas-background-success`)**: `#518b22` — grounded in `var(--atlas-background-success)` in `:root`
- **Variable Token (`--atlas-background-error`)**: `#be2119` — grounded in `var(--atlas-background-error)` in `:root`
- **Variable Token (`--atlas-text-primary`)**: `#1d1e20` — grounded in `var(--atlas-text-primary)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport)
- **Padding & Gutters**: `.75rem` lateral canvas padding with `4px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 4px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `.75rem` horizontal padding
- **Media Queries**: `@media screen and (max-width:440px)`, `@media (max-width:1024px)`, `@media (max-width:768px)`, `@media (min-width:1220px)`
- **Corner Radii**: `5px`, `25px`, `6px`, `20%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--atlas-font-size-display: 40px`, `--atlas-line-height-display: 52px`, `--atlas-margin-display: 24px`; rule `.title` (`font-size: 13px`)
- **H2 Section Rule**: CSS variables `--atlas-font-size-h2: 32px`, `--atlas-line-height-h2: 40px`, `--atlas-margin-h2: 24px`; rule `h2` (`font-size: 2.5em`, `font-weight: 900`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 20px`, `font-weight: 400`); rule `p` (`line-height: 1.6`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 20px`, `font-weight: 400`); CSS variables `--atlas-font-size-small: 14px`, `--atlas-line-height-small: 20px`, `--atlas-margin-small: 8px`; rule `.label` (`font-size: .875em`, `letter-spacing: 2.8px`, `font-weight: 500`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-killstar-com` (`KILLSTAR`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.shopify-section> — `www-killstar-com`)**:
   - DOM & Selectors: Landmark `<header class="shopify-section shopify-section-group-header-group">` (`1440x71px`) hosting `KILLSTAR` navigation (`NEW IN · DRESSES · WOMENS · PLUS · MENS`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-shop-id="53907226789"`, `data-venmo-supported="false"`, `data-environment="production"`), and stylesheet rule `button { box-sizing:border-box;margin:0;padding:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.shopify-section> — `www-killstar-com`)` (`www-killstar-com`) adapts across `@media screen and (max-width:440px)`, `@media (max-width:1024px)`, `@media (max-width:768px)`, `@media (min-width:1220px)` with `cubic-bezier(0.4,0,0.2,1)`, `cubic-bezier(0.34,1.15,0.64,1)`, `cubic-bezier(0.6,0,0.4,1)` transitions and links `NEW IN · DRESSES · WOMENS · PLUS · MENS`.
2. **Hero Stage & Focal Lead (<section.shopify-section> — `Winter's Vale Coat`)**:
   - DOM & Selectors: Landmark `<section class="shopify-section section-full-width-media">` presenting display lead `Winter's Vale Coat` and copy excerpt *"We use cookies & other technologies to provide a personalised exp"* over `#f5f5f5` canvas and `#111111` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#f5f5f5` background with `#111111` headline `Winter's Vale Coat`.
3. **Primary Showcase & Content Grid (<section.section-model-image-blocks> — `Skultra Cropped Cardigan`)**:
   - DOM & Selectors: Landmark `<section class="shopify-section section-model-image-blocks">` rendering section `Skultra Cropped Cardigan` with copy *"Please select a Size"*, asset references (`reamaze-push.js`, `tp.min.js`, `37086_1783060609.js`, `init.js`), and grid rule `section { display:block }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.section-model-image-blocks> — `Skultra Cropped Cardigan`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 4px`) on desktop and Single-column vertical stack at `390px` viewport width with `.75rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.section-full-width-media> — `Basilica Cape`)**:
   - DOM & Selectors: Landmark `<section class="shopify-section section-full-width-media">` framing `Basilica Cape` and `CRUCIFIX SLOUCH BAG` (*"Please select a Colour"*) with `#faf9f8` surface cards, `#f1c40f` accents, and `table { border-collapse:collapse;border-spacing:0 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.section-full-width-media> — `Basilica Cape`)` uses `5px`, `25px`, `6px`, `20%` radii, `#f1c40f` highlights, and assets (reamaze-push.js, tp.min.js, 37086_1783060609.js).
5. **Colophon & Global Directory Footer (<footer.shopify-section> — `https://www.killstar.com/`)**:
   - DOM & Selectors: Landmark `<footer class="shopify-section shopify-section-group-footer-group">` anchoring `KILLSTAR` footer links (`NEW IN · DRESSES · WOMENS · PLUS · MENS`), copy *"Please select a Material Content"*, and `#41a1e6` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.shopify-section> — `https://www.killstar.com/`)` aligns to `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport) with `.75rem` lateral canvas padding with `4px` grid gap and attributes (data-source-attribution="shopify.exit_intersti...", data-shop-id="53907226789", data-venmo-supported="false").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"We use cookies & other technologies to provide a personalised experience on our we..."*
- Copy Excerpt 2: *"Please select a Size"*
- Copy Excerpt 3: *"Please select a Colour"*
- Copy Excerpt 4: *"Please select a Material Content"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.4,0,0.2,1)`, `cubic-bezier(0.34,1.15,0.64,1)`, `cubic-bezier(0.6,0,0.4,1)`
- **Extracted Stylesheet Rules (`www-killstar-com`)**:
- `button { box-sizing:border-box;margin:0;padding:0 }`
- `section { display:block }`
- `table { border-collapse:collapse;border-spacing:0 }`
- `mark { font-weight:600;font-style:inherit }`
- `var { font-style:italic;font-weight:inherit }`
- **Per-Selector Transition Rules**:
- **Selector `.button`**: `transition: all .3s ease-in-out` extracted from `www-killstar-com` stylesheet.
- **Selector `.button:after`**: `transition: transform .3s ease-in-out` extracted from `www-killstar-com` stylesheet.
- **Selector `button.route-continue-without-cov...`**: `transition: all .3s ease-in-out` extracted from `www-killstar-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.4,0,0.2,1)`)**: Governs interactive state transitions across `<header.shopify-section>` and `<section.section-model-image-blocks>`.
- **Runtime Interaction Engine**: Integrates Swiper Touch Carousel Engine, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-killstar-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
