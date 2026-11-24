---
title: "UI Prompt Blueprint: seedjewelry-com"
date: 2026-11-24
captured_at: 2026-11-24
target: "seedjewelry-com"
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
archetype: "Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#1990c6` accent)"
---

# UI Design System & Master Generation Blueprint: seedjewelry-com

> **Seed Jewelry · Lab-Grown Diamond High Jewelry, Dubai** (https://seedjewelry.com/) — Lab-grown diamond jewelry and transformable designs, crafted in the UAE. Explore Be Free, Kohana, Be True and Always Be, with a tree plan...

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Seed Jewelry · Lab-Grown Diamond High Jewelry, Dubai** (`https://seedjewelry.com/`). Lab-grown diamond jewelry and transformable designs, crafted in the UAE. Explore Be Free, Kohana, Be True and Always Be, with a tree plan...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#1990c6` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#1990c6` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Aire Pro` for display copy (`Born from the earth, refined by art`) with `Poppins` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1536px` container bounds (`gap: 10px 40px`, padding `1.5rem`) with `cubic-bezier(.785,.135,.15,.86)` easing and Barba.js Page Transition Router.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=6902px` / doc `7802px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `1536px` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `1.5rem` lateral canvas padding with `10px 40px` grid gap.
- **Border Radius Scale**: `var(--button-border-radius)`, `var(--rounded-full)`, `var(--input-border-radius)`, `2px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1536px`, `gap: 10px 40px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `1.5rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:767px)`, `@media (max-width:700px)`, `@media (prefers-reduced-motion:reduce)`, `@media screen and (min-width:1000px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f3f0eb` | `var(--seed-pdp-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#1990c6` | `.shopify-payment-button__button... { background-color: #1990c6 }` |
| **Secondary / Muted Copy** | `#808080` | live computed `hr` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e3e0d8` | `var(--seed-pdp-border)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--container-max-width` | `100%` | Layout / Spatial Grid Token |
| `--container-xxs-max-width` | `27.5rem` | Layout / Spatial Grid Token |
| `--container-xs-max-width` | `42.5rem` | Layout / Spatial Grid Token |
| `--container-sm-max-width` | `61.25rem` | Layout / Spatial Grid Token |
| `--container-md-max-width` | `71.875rem` | Layout / Spatial Grid Token |
| `--container-lg-max-width` | `90rem` | Layout / Spatial Grid Token |
| `--container-xl-max-width` | `1920px` | Layout / Spatial Grid Token |
| `--container-gutter` | `1.25rem` | Layout / Spatial Grid Token |
| `--section-vertical-spacing` | `2.5rem` | Layout / Spatial Grid Token |
| `--section-vertical-spacing-tight` | `2.5rem` | Layout / Spatial Grid Token |
| `--section-stack-gap` | `2.25rem` | Layout / Spatial Grid Token |
| `--section-stack-gap-tight` | `2.25rem` | Layout / Spatial Grid Token |
| `--form-gap` | `1.25rem` | Layout / Spatial Grid Token |
| `--fieldset-gap` | `1rem` | Layout / Spatial Grid Token |
| `--form-control-gap` | `0.625rem` | Layout / Spatial Grid Token |
| `--checkbox-control-gap` | `0.75rem` | Layout / Spatial Grid Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Aire Pro`.
- **Primary Body Stack**: `Poppins`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 60px`, `line-height: 60px`, `font-weight: 400`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 77.23px`, `line-height: 94px`, `font-weight: 400`); rule `h2` (`font-size: 120%`, `font-weight: bold`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 26.4px`, `font-weight: 400`); CSS variables `--text-base: 1.0rem`, `--modal-body-padding-block: 1.25rem`, `--modal-body-padding-inline: 1.25rem`; rule `,body` (`line-height: 1.5rem`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 26.4px`, `font-weight: 400`); CSS variables `--heading-letter-spacing: 0.0em`, `--text-letter-spacing: 0.0em`, `--button-letter-spacing: 0.0em`; rule `.label` (`font-size: 14px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.785,.135,.15,.86)`, `cubic-bezier(.4,0,.22,1)`, `cubic-bezier(.45,0,.55,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.accordion :is(svg)`**: `transition: transform .2s` extracted from `seedjewelry-com` stylesheet.
- **Selector `.shopify-payment-button__button--...`**: `transition: background-size .45s cubic-bezier(.785,.135,.15,.86),backgroun...` extracted from `seedjewelry-com` stylesheet.
- **Selector `.shopify-payment-button__button--...`**: `transition: background-size .45s cubic-bezier(.785,.135,.15,.86),backgroun...` extracted from `seedjewelry-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.785,.135,.15,.86)`)**: Governs interactive state transitions across `<header.analytics>` and `<section.seed-hero>`.
- **Runtime Interaction Engine**: Integrates Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `7802px`, deepest scrollY reached `6902px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: Native browser scroll / standard CSS transitions.
- **Hover Physics (`primary_cta` · `EXPLORE OUR COLLECTIONS`)**: `color`: `rgb(255, 255, 255)` -> `rgb(0, 0, 0)` (`transition-duration: 0.45s, 0.45s, 0.45s, 0.45s`, `timing: cubic-bezier(0.785, 0.135, 0.15, 0.86), steps(1), cubic-bezier(0.785, 0.135, 0.15, 0.86), cubic-bezier(0.785, 0.135, 0.15, 0.86)`).
- **Route Transition Architecture**: First internal navigation (`/collections`) measured as `direct` in `2249ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Seed Jewelry · Lab-Grown Diamond High Jewe │
│ ====================================================================== │
│ [ <header.analytics> (1440x91px)      | Search Search                ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.shopify-section> (w=1440px)                   | │
│ | H1: Born from the earth, refined by art                            | │
│ | Substrate: #ffffff | Ink: #000000 | Accent: #1990c6                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.seed-hero>) max-w: 1536px                  | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Best Sellers                 |  | Kohana Ring , Big Size, Reve | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.seed-product-grid) — Always Be Round Cut E | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.color-scheme) | https://seedjewelry.com/             │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 10px 40p)   │
│ ====================================================================== │
│ [ HEADER BAR (<header.analytics>      ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.shopify-section) — 390px Vertical Lead        | │
│ | H1: Born from the earth, refined by art                            | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.seed-hero>) — 1-Col Stack                 | │
│ | [ Item 1: Best Sellers                                           ] | │
│ | [ Item 2: Kohana Ring , Big Size, Reverse                        ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.seed-product-gr) — 1-Col (Always Be Round Cu) │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.color-scheme) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.analytics> — `seedjewelry-com`)**:
   - Landmark `<header class="analytics">` (`1440x91px`) hosting `Seed Jewelry · Lab-Grown Diamond Hig` navigation (`Search Search`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-source-attribution="shopify.loadfeatures"`, `data-source-attribution="shopify.dynamic_check..."`, `data-source-attribution="shopify.dynamic_check..."`), and stylesheet rule `.page-width { max-width:var(--container-xl-max-width);margin:0 auto;padding:0 25px }`.
2. **Hero Stage & Focal Lead (<section.shopify-section> — `Born from the earth, refined by ar`)**:
   - Landmark `<section class="shopify-section seed-hero-section">` presenting display lead `Born from the earth, refined by art` and copy excerpt *"Celebrating our launch: 20% off every piece until 30 November."* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.seed-hero> — `Best Sellers`)**:
   - Landmark `<section class="seed-hero">` rendering section `Best Sellers` with copy *"Lab-grown diamonds, transformable designs, and sustainable luxury"*, asset references (`2113812439524310`, `fbevents.js`, `clarity.js`, `zcz4nln3tx`), and grid rule `.page-width-lg { max-width:var(--container-lg-max-width);margin:0 auto;padding:0 25px }`.
4. **Interactive Detail & Feature Matrix (<section.seed-product-grid-section> — `Kohana Ring , Big Size, Reverse`)**:
   - Landmark `<section class="shopify-section seed-product-grid-section">` framing `Kohana Ring , Big Size, Reverse` and `Always Be Round Cut Earrings with Removable Halo` (*"Kohana Ring , Big Size, Reverse 18K (750) White Gold · 1 total ca"*) with `#f3f0eb` surface cards, `#1990c6` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.color-scheme--scheme-1> — `https://seedjewelry.com/`)**:
   - Landmark `<footer class="color-scheme--scheme-1">` anchoring `Seed Jewelry · Lab-Grown Diamond` footer links (`Search Search`), copy *"18K (750) White Gold · 1 total carat weight ·..."*, and `#e3e0d8` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `Seed Jewelry` · sticky/fixed elements: `1`
- **Step 02** (`y=850px`, `12%`): Active landmark `Best Sellers` · sticky/fixed elements: `1`
- **Step 03** (`y=1700px`, `25%`): Active landmark `Seed Jewelry` · sticky/fixed elements: `1`
- **Step 04** (`y=3400px`, `49%`): Active landmark `Seed Jewelry` · sticky/fixed elements: `1`
- **Step 05** (`y=4250px`, `62%`): Active landmark `Seed Jewelry` · sticky/fixed elements: `1`
- **Step 06** (`y=5950px`, `86%`): Active landmark `Seed Jewelry` · sticky/fixed elements: `1`
- **Step 07** (`y=6800px`, `99%`): Active landmark `Seed Jewelry` · sticky/fixed elements: `1`
- **Step 08** (`y=6902px`, `100%`): Active landmark `Seed Jewelry` · sticky/fixed elements: `1`

### Multi-Page Internal Route Map
- **Listing Route (`/collections`)**: `https://seedjewelry.com/collections` — H1: `Discover all collections`, scrollHeight `7959px`, transition `direct` (`2249ms`)
- **Detail Route (`/pages/wishlist`)**: `https://seedjewelry.com/pages/wishlist` — H1: `Wishlist`, scrollHeight `1280px`, transition `direct` (`1423ms`)
- **Detail Route (`/collections/be-free`)**: `https://seedjewelry.com/collections/be-free` — H1: `Be Free`, scrollHeight `2587px`, transition `direct` (`2141ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: seedjewelry-com (Seed Jewelry · Lab-Grown Diamond High Jewelry, Dubai)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `seedjewelry-com` (**Seed Jewelry · Lab-Grown Diamond High Jewelry, Dubai** — `https://seedjewelry.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#1990c6` accent).
- **Identity & Domain Context**: Lab-grown diamond jewelry and transformable designs, crafted in the UAE. Explore Be Free, Kohana, Be True and Always Be, with a tree plan...
- **Primary Substrate**: `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#000000`, **Accent / Highlight**: `#1990c6`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#1990c6` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Aire Pro` for display copy (`Born from the earth, refined by art`) with `Poppins` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1536px` container bounds (`gap: 10px 40px`, padding `1.5rem`) with `cubic-bezier(.785,.135,.15,.86)` easing and Barba.js Page Transition Router.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `seedjewelry-com` in your global stylesheet:

:root {
  /* Seed Jewelry · Lab-Grown Diamond High Jewelry, Dubai (seedjewelry-com) — Live-Grounded CSS Variables */
  --container-max-width: 100%; /* Layout / Spatial Grid Token (seedjewelry-com) */
  --container-xxs-max-width: 27.5rem; /* Layout / Spatial Grid Token (seedjewelry-com) */
  --container-xs-max-width: 42.5rem; /* Layout / Spatial Grid Token (seedjewelry-com) */
  --container-sm-max-width: 61.25rem; /* Layout / Spatial Grid Token (seedjewelry-com) */
  --container-md-max-width: 71.875rem; /* Layout / Spatial Grid Token (seedjewelry-com) */
  --container-lg-max-width: 90rem; /* Layout / Spatial Grid Token (seedjewelry-com) */
  --container-xl-max-width: 1920px; /* Layout / Spatial Grid Token (seedjewelry-com) */
  --container-gutter: 1.25rem; /* Layout / Spatial Grid Token (seedjewelry-com) */
  --section-vertical-spacing: 2.5rem; /* Layout / Spatial Grid Token (seedjewelry-com) */
  --section-vertical-spacing-tight: 2.5rem; /* Layout / Spatial Grid Token (seedjewelry-com) */
  --section-stack-gap: 2.25rem; /* Layout / Spatial Grid Token (seedjewelry-com) */
  --section-stack-gap-tight: 2.25rem; /* Layout / Spatial Grid Token (seedjewelry-com) */
  --form-gap: 1.25rem; /* Layout / Spatial Grid Token (seedjewelry-com) */
  --fieldset-gap: 1rem; /* Layout / Spatial Grid Token (seedjewelry-com) */
  --form-control-gap: 0.625rem; /* Layout / Spatial Grid Token (seedjewelry-com) */
  --checkbox-control-gap: 0.75rem; /* Layout / Spatial Grid Token (seedjewelry-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#000000` — grounded in live computed `main` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#f3f0eb` — grounded in `var(--seed-pdp-bg)` in `:root`
- **Interactive Accent / Highlight**: `#1990c6` — grounded in `.shopify-payment-button__button... { background-color: #1990c6 }`
- **Secondary / Muted Copy**: `#808080` — grounded in live computed `hr` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#e3e0d8` — grounded in `var(--seed-pdp-border)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `1536px` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `1.5rem` lateral canvas padding with `10px 40px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1536px`, `gap: 10px 40px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `1.5rem` horizontal padding
- **Media Queries**: `@media (min-width:767px)`, `@media (max-width:700px)`, `@media (prefers-reduced-motion:reduce)`, `@media screen and (min-width:1000px)`
- **Corner Radii**: `var(--button-border-radius)`, `var(--rounded-full)`, `var(--input-border-radius)`, `2px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Aire Pro`
- **Body Font Stack**: `Poppins`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: live computed `h1` (`font-size: 60px`, `line-height: 60px`, `font-weight: 400`)
- **H2 Section Rule**: live computed `h2` (`font-size: 77.23px`, `line-height: 94px`, `font-weight: 400`); rule `h2` (`font-size: 120%`, `font-weight: bold`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 26.4px`, `font-weight: 400`); CSS variables `--text-base: 1.0rem`, `--modal-body-padding-block: 1.25rem`, `--modal-body-padding-inline: 1.25rem`; rule `,body` (`line-height: 1.5rem`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 26.4px`, `font-weight: 400`); CSS variables `--heading-letter-spacing: 0.0em`, `--text-letter-spacing: 0.0em`, `--button-letter-spacing: 0.0em`; rule `.label` (`font-size: 14px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `seedjewelry-com` (`Seed Jewelry · Lab-Grown Diamond High Jewelry, Dubai`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.analytics> — `seedjewelry-com`)**:
   - DOM & Selectors: Landmark `<header class="analytics">` (`1440x91px`) hosting `Seed Jewelry · Lab-Grown Diamond Hig` navigation (`Search Search`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-source-attribution="shopify.loadfeatures"`, `data-source-attribution="shopify.dynamic_check..."`, `data-source-attribution="shopify.dynamic_check..."`), and stylesheet rule `.page-width { max-width:var(--container-xl-max-width);margin:0 auto;padding:0 25px }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.analytics> — `seedjewelry-com`)` (`seedjewelry-com`) adapts across `@media (min-width:767px)`, `@media (max-width:700px)`, `@media (prefers-reduced-motion:reduce)`, `@media screen and (min-width:1000px)` with `cubic-bezier(.785,.135,.15,.86)`, `cubic-bezier(.4,0,.22,1)`, `cubic-bezier(.45,0,.55,1)` transitions and links `Search Search`.
2. **Hero Stage & Focal Lead (<section.shopify-section> — `Born from the earth, refined by ar`)**:
   - DOM & Selectors: Landmark `<section class="shopify-section seed-hero-section">` presenting display lead `Born from the earth, refined by art` and copy excerpt *"Celebrating our launch: 20% off every piece until 30 November."* over `#ffffff` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×2616px` mobile) sets `#ffffff` background with `#000000` headline `Born from the earth, refined by art`.
3. **Primary Showcase & Content Grid (<section.seed-hero> — `Best Sellers`)**:
   - DOM & Selectors: Landmark `<section class="seed-hero">` rendering section `Best Sellers` with copy *"Lab-grown diamonds, transformable designs, and sustainable luxury"*, asset references (`2113812439524310`, `fbevents.js`, `clarity.js`, `zcz4nln3tx`), and grid rule `.page-width-lg { max-width:var(--container-lg-max-width);margin:0 auto;padding:0 25px }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.seed-hero> — `Best Sellers`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1536px`, `gap: 10px 40px`) on desktop and Single-column vertical stack at `390px` viewport width with `1.5rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.seed-product-grid-section> — `Kohana Ring , Big Size, Reverse`)**:
   - DOM & Selectors: Landmark `<section class="shopify-section seed-product-grid-section">` framing `Kohana Ring , Big Size, Reverse` and `Always Be Round Cut Earrings with Removable Halo` (*"Kohana Ring , Big Size, Reverse 18K (750) White Gold · 1 total ca"*) with `#f3f0eb` surface cards, `#1990c6` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.seed-product-grid-section> — `Kohana Ring , Big Size, Reverse`)` uses `var(--button-border-radius)`, `var(--rounded-full)`, `var(--input-border-radius)`, `2px` radii, `#1990c6` highlights, and assets (2113812439524310, fbevents.js, clarity.js).
5. **Colophon & Global Directory Footer (<footer.color-scheme--scheme-1> — `https://seedjewelry.com/`)**:
   - DOM & Selectors: Landmark `<footer class="color-scheme--scheme-1">` anchoring `Seed Jewelry · Lab-Grown Diamond` footer links (`Search Search`), copy *"18K (750) White Gold · 1 total carat weight ·..."*, and `#e3e0d8` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.color-scheme--scheme-1> — `https://seedjewelry.com/`)` aligns to `1536px` (non-`@media` desktop container stylesheet rule) with `1.5rem` lateral canvas padding with `10px 40px` grid gap and attributes (data-source-attribution="shopify.exit_intersti...", data-source-attribution="shopify.loadfeatures", data-source-attribution="shopify.dynamic_check...").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Celebrating our launch: 20% off every piece until 30 November."*
- Copy Excerpt 2: *"Lab-grown diamonds, transformable designs, and sustainable luxury. Each piece tell..."*
- Copy Excerpt 3: *"Kohana Ring , Big Size, Reverse 18K (750) White Gold · 1 total carat weight ·... €..."*
- Copy Excerpt 4: *"18K (750) White Gold · 1 total carat weight ·..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.785,.135,.15,.86)`, `cubic-bezier(.4,0,.22,1)`, `cubic-bezier(.45,0,.55,1)`
- **Extracted Stylesheet Rules (`seedjewelry-com`)**:
- `.page-width { max-width:var(--container-xl-max-width);margin:0 auto;padding:0 25px }`
- `.page-width-lg { max-width:var(--container-lg-max-width);margin:0 auto;padding:0 25px }`
- `strong { font-weight:bolder }`
- `pre { font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,Liberation... }`
- `table { text-indent:0;border-color:inherit;border-collapse:collapse }`
- **Per-Selector Transition Rules**:
- **Selector `.accordion :is(svg)`**: `transition: transform .2s` extracted from `seedjewelry-com` stylesheet.
- **Selector `.shopify-payment-button__button--...`**: `transition: background-size .45s cubic-bezier(.785,.135,.15,.86),backgroun...` extracted from `seedjewelry-com` stylesheet.
- **Selector `.shopify-payment-button__button--...`**: `transition: background-size .45s cubic-bezier(.785,.135,.15,.86),backgroun...` extracted from `seedjewelry-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.785,.135,.15,.86)`)**: Governs interactive state transitions across `<header.analytics>` and `<section.seed-hero>`.
- **Runtime Interaction Engine**: Integrates Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `7802px` across 8 distinct viewport chapters.
- **Vertical Chapter Sequence**: Seed Jewelry (0%) -> Best Sellers (12%) -> Seed Jewelry (25%) -> Seed Jewelry (49%) -> Seed Jewelry (62%) -> Seed Jewelry (86%) -> Seed Jewelry (99%) -> Seed Jewelry (100%).
- **Hover Micro-Interaction (`primary_cta`)**: Animate `color` with `0.45s, 0.45s, 0.45s, 0.45s cubic-bezier(0.785, 0.135, 0.15, 0.86), steps(1), cubic-bezier(0.785, 0.135, 0.15, 0.86), cubic-bezier(0.785, 0.135, 0.15, 0.86)`.
- **Multi-Page Routes**: Scaffold internal routes `/collections` (listing, direct), `/pages/wishlist` (detail, direct), `/collections/be-free` (detail, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `seedjewelry-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | Seed Jewelry | `1` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `12%` | Best Sellers | `1` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `1700px` | `25%` | Seed Jewelry | `1` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `3400px` | `49%` | Seed Jewelry | `1` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `4250px` | `62%` | Seed Jewelry | `1` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `5950px` | `86%` | Seed Jewelry | `1` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `6800px` | `99%` | Seed Jewelry | `1` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `6902px` | `100%` | Seed Jewelry | `1` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | Seed Jewelry | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `3127px` | `50%` | Seed Jewelry | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `6254px` | `100%` | Seed Jewelry | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `listing` | `https://seedjewelry.com/collections` | Discover all collections | `7959px` | `direct` (`2249ms`) | [subpage-01-collections.webp](assets/subpage-01-collections.webp) |
| `2` | `detail` | `https://seedjewelry.com/pages/wishlist` | Wishlist | `1280px` | `direct` (`1423ms`) | [subpage-02-pages-wishlist.webp](assets/subpage-02-pages-wishlist.webp) |
| `3` | `detail` | `https://seedjewelry.com/collections/be-free` | Be Free | `2587px` | `direct` (`2141ms`) | [subpage-03-collections-be-free.webp](assets/subpage-03-collections-be-free.webp) |

