---
title: "UI Prompt Blueprint: www-unimaticwatches-com"
date: 2026-11-24
captured_at: 2026-11-24
target: "www-unimaticwatches-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
capture_mode: behavioral_journey_v2
asset_format: webp
scroll_driver: native
desktop_keyframes: 6
subpages_crawled: 3
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#f6f6f6` canvas, `#000000` ink, `#afff00` accent)"
---

# UI Design System & Master Generation Blueprint: www-unimaticwatches-com

> **UNIMATIC Watches** (https://www.unimaticwatches.com/?srsltid=AfmBOor1S-k1GXW2WUlgmQd-YbKuDQWHeKBxyRjTFNyURmTvXoeNJXHD) — Discover UNIMATIC watches, an independent Italian watch brand creating minimalist, functional watches made in Italy. Explore our Classic...

![Desktop Journey Filmstrip (1280x4968)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **UNIMATIC Watches** (`https://www.unimaticwatches.com/?srsltid=AfmBOor1S-k1GXW2WUlgmQd-YbKuDQWHeKBxyRjTFNyURmTvXoeNJXHD`). Discover UNIMATIC watches, an independent Italian watch brand creating minimalist, functional watches made in Italy. Explore our Classic...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#f6f6f6` canvas, `#000000` ink, `#afff00` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f6f6f6` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#afff00` accents.
  - **Grounded Typographic Hierarchy**: Uses `Helvetica Neue` across display (`New Langhe Collection`) and body copy, paired with `JetBrains Mono` for monospace/code.
  - **Calibrated Spatial Grid & Motion**: Combines `1200px` container bounds (`gap: 24px`, padding `var(--page-margin)`) with `cubic-bezier(.4,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×4968px` (`assets/desktop-journey.webp`, `6` keyframes up to `y=3941px` / doc `4841px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `1200px` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `var(--page-margin)` lateral canvas padding with `24px` grid gap.
- **Border Radius Scale**: `var(--radius-sm)`, `var(--radius-lg)`, `var(--radius-md)`, `.6rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1200px`, `gap: 24px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--page-margin)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:768px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:767px)`, `@media (max-width:1099px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f6f6f6` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `.b2b-terms { background-color: white }` (`#ffffff`) |
| **Interactive Accent / Highlight** | `#afff00` | `var(--color-accent)` in `:root` |
| **Secondary / Muted Copy** | `#808080` | live computed `hr` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#ffffff` | `.filter-opt__box:after { border: #ffffff }` |
| **Variable Token (`--color-tag-ink`)** | `#222222` | `var(--color-tag-ink)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--space-1` | `.4rem` | Layout / Spatial Grid Token |
| `--space-2` | `.8rem` | Layout / Spatial Grid Token |
| `--space-2-5` | `1rem` | Layout / Spatial Grid Token |
| `--space-3` | `1.2rem` | Layout / Spatial Grid Token |
| `--space-4` | `1.6rem` | Layout / Spatial Grid Token |
| `--space-5` | `2.4rem` | Layout / Spatial Grid Token |
| `--space-6` | `3.2rem` | Layout / Spatial Grid Token |
| `--color-tag-ink` | `#222` | Typography Ink Token |
| `--editorial-sticky-top` | `6.4rem` | Dimension / Scale Token |
| `--drawer-top-base` | `calc(var(--space-4) + var(--space-2-5) * 2 + 1.6rem + var(--space-2))` | Dimension / Scale Token |
| `--drawer-top` | `var(--drawer-top-base)` | Design System Custom Token |
| `--drawer-width` | `33rem` | Layout / Spatial Grid Token |
| `--sticky-top` | `calc(var(--drawer-top-base) + var(--space-6))` | Design System Custom Token |
| `--color-bg` | `#F6F6F6` | Canvas / Surface Token |
| `--color-ink` | `#000000` | Typography Ink Token |
| `--color-accent` | `#AFFF00` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Helvetica Neue`.
- **Primary Body Stack**: `Helvetica Neue`.
- **Technical / Metadata Stack**: `JetBrains Mono`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 24px`, `line-height: 29.304px`, `font-weight: 700`, `letter-spacing: -0.48px`).
- **Section Heading (`H2`)**: live computed `h3 (primary section heading)` (`font-size: 28.08px`, `line-height: 34.2857px`, `font-weight: 700`, `letter-spacing: -0.48px`); CSS variables `--fs-subtitle: 1.6rem`; rule `h2` (`font-size: 120%`, `font-weight: bold`).
- **Body Copy**: live computed `body` (`font-size: 12px`, `line-height: 14.652px`, `font-weight: 400`); CSS variables `--fs-body: 1.2rem`; rule `p` (`line-height: 2.8rem`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: 14.652px`, `font-weight: 400`); CSS variables `--font-mono: "JetBrains Mono", ui-monospace, "SFMono-Regular", Menlo, monospace`, `--fs-mono: 1.2rem`, `--lh-mono: 1.32`; rule `small` (`font-size: var(--fs-eyebrow)`, `line-height: var(--lh-mono)`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(1,0,0,1)`, `cubic-bezier(0.64,0,0.78,0)`.

### Per-Element Transition & Choreography Rules
- **Selector `.slider__ctrl`**: `transition: background-color var(--transition),color var(--transition)` extracted from `www-unimaticwatches-com` stylesheet.
- **Selector `.drawer`**: `transition: opacity var(--transition),transform var(--transition),display...` extracted from `www-unimaticwatches-com` stylesheet.
- **Selector `body:after`**: `transition: opacity var(--transition)` extracted from `www-unimaticwatches-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.shopify-section>` and `<section.product-carousel-section>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `4841px`, deepest scrollY reached `3941px` across `6` desktop keyframes).
- **Detected Scroll / Motion Libraries**: Native browser scroll / standard CSS transitions.
- **Hover Physics (`primary_cta` · `Meet The Collection`)**: Computed transition `0.22s, 0.22s` / `ease, ease` (no static color/transform shift captured at rest).
- **Hover Physics (`first_card` · `TRUFFLE, MOSS, FOG DIALS SWISS MO...`)**: Computed transition `0s` / `ease` (no static color/transform shift captured at rest).
- **Route Transition Architecture**: First internal navigation (`/collections/new-in`) measured as `MPA` in `1514ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — UNIMATIC Watches                           │
│ ====================================================================== │
│ [ <header.shopify-sectio (1440x0px)   | New in · Bracelets           ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.shopify-section> (w=1440px)                   | │
│ | H1: New Langhe Collection                                          | │
│ | Substrate: #f6f6f6 | Ink: #000000 | Accent: #afff00                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.product-carousel-) max-w: 1200px           | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Some landscapes are defined  |  | The ICON collection          | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<article.product-card>) — Waterproof checked        | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.shopify-sect) | https://www.unimaticwatches.com/?sr  │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 24px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.shopify-section>) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.shopify-section) — 390px Vertical Lead        | │
│ | H1: New Langhe Collection                                          | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.product-carou) — 1-Col Stack              | │
│ | [ Item 1: Some landscapes are defined less by what can be s...   ] | │
│ | [ Item 2: The ICON collection                                    ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<article.product-card>) — 1-Col (Waterproof checked) | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.shopify-sect) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.shopify-section> — `www-unimaticwatches-com`)**:
   - Landmark `<header class="shopify-section shopify-section-group-header-group">` (`1440x0px`) hosting `UNIMATIC Watches` navigation (`New in · Bracelets`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-shopify`, `data-shop-id="104415822154"`, `data-venmo-supported="false"`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.shopify-section> — `New Langhe Collection`)**:
   - Landmark `<section class="shopify-section hero">` presenting display lead `New Langhe Collection` and copy excerpt *"Weather: partly cloudy"* over `#f6f6f6` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.product-carousel-section> — `Some landscapes are defined less b`)**:
   - Landmark `<section class="shopify-section product-carousel-section">` rendering section `Some landscapes are defined less by what can be s...` with copy *"Truffle, Moss, Fog Dials"*, asset references (`596128728859448`, `fbevents.js`, `clarity.js`, `zg18q6f8jj`), and grid rule `html { font-size:10px;-webkit-text-size-adjust:100%;text-size-adjust:100% }`.
4. **Interactive Detail & Feature Matrix (<article.product-card> — `The ICON collection`)**:
   - Landmark `<article class="product-card">` framing `The ICON collection` and `Waterproof checked` (*"A landscape interpreted through colour and texture."*) with `#ffffff` surface cards, `#afff00` accents, and `button { font:inherit;color:inherit;background:none;border:0;padding:0;cursor:poi... }`.
5. **Colophon & Global Directory Footer (<footer.shopify-section> — `https://www.unimaticwatches.com/?srsltid=AfmBOor1S-k1GXW2WUlgmQd-YbKuDQWHeKBxyRjTFNyURmTvXoeNJXHD`)**:
   - Landmark `<footer class="shopify-section shopify-section-group-footer-group">` anchoring `UNIMATIC Watches` footer links (`New in · Bracelets`), copy *"Meet The Collection"*, and `#ffffff` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `New Langhe Collection` · sticky/fixed elements: `1`
- **Step 02** (`y=850px`, `22%`): Active landmark `The ICON collection` · sticky/fixed elements: `1`
- **Step 03** (`y=1700px`, `43%`): Active landmark `#shopify-section-template--30951437730122__editorial` · sticky/fixed elements: `1`
- **Step 04** (`y=2550px`, `65%`): Active landmark `#shopify-section-template--30951437730122__produc...` · sticky/fixed elements: `1`
- **Step 05** (`y=3400px`, `86%`): Active landmark `Waterproof checked` · sticky/fixed elements: `1`
- **Step 06** (`y=3941px`, `100%`): Active landmark `Waterproof checked` · sticky/fixed elements: `1`

### Multi-Page Internal Route Map
- **Detail Route (`/collections/new-in`)**: `https://www.unimaticwatches.com/collections/new-in` — H1: `Crafting modern timepieces that merge iconic desi...`, scrollHeight `4609px`, transition `MPA` (`1514ms`)
- **Detail Route (`/collections/bracelets`)**: `https://www.unimaticwatches.com/collections/bracelets` — H1: `Crafting modern timepieces that merge iconic desi...`, scrollHeight `2566px`, transition `direct` (`3335ms`)
- **Detail Route (`/apps/wishlist-1`)**: `https://www.unimaticwatches.com/apps/wishlist-1` — H1: `My wishlist`, scrollHeight `923px`, transition `direct` (`4381ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-unimaticwatches-com (UNIMATIC Watches)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-unimaticwatches-com` (**UNIMATIC Watches** — `https://www.unimaticwatches.com/?srsltid=AfmBOor1S-k1GXW2WUlgmQd-YbKuDQWHeKBxyRjTFNyURmTvXoeNJXHD`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#f6f6f6` canvas, `#000000` ink, `#afff00` accent).
- **Identity & Domain Context**: Discover UNIMATIC watches, an independent Italian watch brand creating minimalist, functional watches made in Italy. Explore our Classic...
- **Primary Substrate**: `#f6f6f6` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#000000`, **Accent / Highlight**: `#afff00`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f6f6f6` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#afff00` accents.
  - **Grounded Typographic Hierarchy**: Uses `Helvetica Neue` across display (`New Langhe Collection`) and body copy, paired with `JetBrains Mono` for monospace/code.
  - **Calibrated Spatial Grid & Motion**: Combines `1200px` container bounds (`gap: 24px`, padding `var(--page-margin)`) with `cubic-bezier(.4,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-unimaticwatches-com` in your global stylesheet:

:root {
  /* UNIMATIC Watches (www-unimaticwatches-com) — Live-Grounded CSS Variables */
  --space-1: .4rem; /* Layout / Spatial Grid Token (www-unimaticwatches-com) */
  --space-2: .8rem; /* Layout / Spatial Grid Token (www-unimaticwatches-com) */
  --space-2-5: 1rem; /* Layout / Spatial Grid Token (www-unimaticwatches-com) */
  --space-3: 1.2rem; /* Layout / Spatial Grid Token (www-unimaticwatches-com) */
  --space-4: 1.6rem; /* Layout / Spatial Grid Token (www-unimaticwatches-com) */
  --space-5: 2.4rem; /* Layout / Spatial Grid Token (www-unimaticwatches-com) */
  --space-6: 3.2rem; /* Layout / Spatial Grid Token (www-unimaticwatches-com) */
  --color-tag-ink: #222; /* Typography Ink Token (www-unimaticwatches-com) */
  --editorial-sticky-top: 6.4rem; /* Dimension / Scale Token (www-unimaticwatches-com) */
  --drawer-top-base: calc(var(--space-4) + var(--space-2-5) * 2 + 1.6rem + var(--space-2)); /* Dimension / Scale Token (www-unimaticwatches-com) */
  --drawer-top: var(--drawer-top-base); /* Design System Custom Token (www-unimaticwatches-com) */
  --drawer-width: 33rem; /* Layout / Spatial Grid Token (www-unimaticwatches-com) */
  --sticky-top: calc(var(--drawer-top-base) + var(--space-6)); /* Design System Custom Token (www-unimaticwatches-com) */
  --color-bg: #F6F6F6; /* Canvas / Surface Token (www-unimaticwatches-com) */
  --color-ink: #000000; /* Typography Ink Token (www-unimaticwatches-com) */
  --color-accent: #AFFF00; /* Brand / Palette Token (www-unimaticwatches-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f6f6f6` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#000000` — grounded in live computed `main` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#ffffff` — grounded in `.b2b-terms { background-color: white }` (`#ffffff`)
- **Interactive Accent / Highlight**: `#afff00` — grounded in `var(--color-accent)` in `:root`
- **Secondary / Muted Copy**: `#808080` — grounded in live computed `hr` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#ffffff` — grounded in `.filter-opt__box:after { border: #ffffff }`
- **Variable Token (`--color-tag-ink`)**: `#222222` — grounded in `var(--color-tag-ink)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×4968px` (multi-frame vertical journey filmstrip (4968px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `1200px` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `var(--page-margin)` lateral canvas padding with `24px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1200px`, `gap: 24px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--page-margin)` horizontal padding
- **Media Queries**: `@media (min-width:768px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:767px)`, `@media (max-width:1099px)`
- **Corner Radii**: `var(--radius-sm)`, `var(--radius-lg)`, `var(--radius-md)`, `.6rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Helvetica Neue`
- **Body Font Stack**: `Helvetica Neue`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **H1 Display Rule**: live computed `h1` (`font-size: 24px`, `line-height: 29.304px`, `font-weight: 700`, `letter-spacing: -0.48px`)
- **H2 Section Rule**: live computed `h3 (primary section heading)` (`font-size: 28.08px`, `line-height: 34.2857px`, `font-weight: 700`, `letter-spacing: -0.48px`); CSS variables `--fs-subtitle: 1.6rem`; rule `h2` (`font-size: 120%`, `font-weight: bold`)
- **Body Copy Rule**: live computed `body` (`font-size: 12px`, `line-height: 14.652px`, `font-weight: 400`); CSS variables `--fs-body: 1.2rem`; rule `p` (`line-height: 2.8rem`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 12px`, `line-height: 14.652px`, `font-weight: 400`); CSS variables `--font-mono: "JetBrains Mono", ui-monospace, "SFMono-Regular", Menlo, monospace`, `--fs-mono: 1.2rem`, `--lh-mono: 1.32`; rule `small` (`font-size: var(--fs-eyebrow)`, `line-height: var(--lh-mono)`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-unimaticwatches-com` (`UNIMATIC Watches`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.shopify-section> — `www-unimaticwatches-com`)**:
   - DOM & Selectors: Landmark `<header class="shopify-section shopify-section-group-header-group">` (`1440x0px`) hosting `UNIMATIC Watches` navigation (`New in · Bracelets`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-shopify`, `data-shop-id="104415822154"`, `data-venmo-supported="false"`), and stylesheet rule `after { box-sizing:border-box }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.shopify-section> — `www-unimaticwatches-com`)` (`www-unimaticwatches-com`) adapts across `@media (min-width:768px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:767px)`, `@media (max-width:1099px)` with `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(1,0,0,1)`, `cubic-bezier(0.64,0,0.78,0)` transitions and links `New in · Bracelets`.
2. **Hero Stage & Focal Lead (<section.shopify-section> — `New Langhe Collection`)**:
   - DOM & Selectors: Landmark `<section class="shopify-section hero">` presenting display lead `New Langhe Collection` and copy excerpt *"Weather: partly cloudy"* over `#f6f6f6` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1280×4968px` desktop / `390×2616px` mobile) sets `#f6f6f6` background with `#000000` headline `New Langhe Collection`.
3. **Primary Showcase & Content Grid (<section.product-carousel-section> — `Some landscapes are defined less b`)**:
   - DOM & Selectors: Landmark `<section class="shopify-section product-carousel-section">` rendering section `Some landscapes are defined less by what can be s...` with copy *"Truffle, Moss, Fog Dials"*, asset references (`596128728859448`, `fbevents.js`, `clarity.js`, `zg18q6f8jj`), and grid rule `html { font-size:10px;-webkit-text-size-adjust:100%;text-size-adjust:100% }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.product-carousel-section> — `Some landscapes are defined less b`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1200px`, `gap: 24px`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--page-margin)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.product-card> — `The ICON collection`)**:
   - DOM & Selectors: Landmark `<article class="product-card">` framing `The ICON collection` and `Waterproof checked` (*"A landscape interpreted through colour and texture."*) with `#ffffff` surface cards, `#afff00` accents, and `button { font:inherit;color:inherit;background:none;border:0;padding:0;cursor:poi... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.product-card> — `The ICON collection`)` uses `var(--radius-sm)`, `var(--radius-lg)`, `var(--radius-md)`, `.6rem` radii, `#afff00` highlights, and assets (596128728859448, fbevents.js, clarity.js).
5. **Colophon & Global Directory Footer (<footer.shopify-section> — `https://www.unimaticwatches.com/?srsltid=AfmBOor1S-k1GXW2WUlgmQd-YbKuDQWHeKBxyRjTFNyURmTvXoeNJXHD`)**:
   - DOM & Selectors: Landmark `<footer class="shopify-section shopify-section-group-footer-group">` anchoring `UNIMATIC Watches` footer links (`New in · Bracelets`), copy *"Meet The Collection"*, and `#ffffff` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.shopify-section> — `https://www.unimaticwatches.com/?srsltid=AfmBOor1S-k1GXW2WUlgmQd-YbKuDQWHeKBxyRjTFNyURmTvXoeNJXHD`)` aligns to `1200px` (non-`@media` desktop container stylesheet rule) with `var(--page-margin)` lateral canvas padding with `24px` grid gap and attributes (data-source-attribution="shopify.exit_intersti...", data-shopify, data-shop-id="104415822154").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Weather: partly cloudy"*
- Copy Excerpt 2: *"Truffle, Moss, Fog Dials"*
- Copy Excerpt 3: *"A landscape interpreted through colour and texture."*
- Copy Excerpt 4: *"Meet The Collection"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(1,0,0,1)`, `cubic-bezier(0.64,0,0.78,0)`
- **Extracted Stylesheet Rules (`www-unimaticwatches-com`)**:
- `after { box-sizing:border-box }`
- `html { font-size:10px;-webkit-text-size-adjust:100%;text-size-adjust:100% }`
- `button { font:inherit;color:inherit;background:none;border:0;padding:0;cursor:poi... }`
- `svg { display:block;max-width:100% }`
- `video-background { display:block }`
- **Per-Selector Transition Rules**:
- **Selector `.slider__ctrl`**: `transition: background-color var(--transition),color var(--transition)` extracted from `www-unimaticwatches-com` stylesheet.
- **Selector `.drawer`**: `transition: opacity var(--transition),transform var(--transition),display...` extracted from `www-unimaticwatches-com` stylesheet.
- **Selector `body:after`**: `transition: opacity var(--transition)` extracted from `www-unimaticwatches-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.shopify-section>` and `<section.product-carousel-section>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `4841px` across 6 distinct viewport chapters.
- **Vertical Chapter Sequence**: New Langhe Collection (0%) -> The ICON collection (22%) -> #shopify-section-template--... (43%) -> #shopify-section-template--... (65%) -> Waterproof checked (86%) -> Waterproof checked (100%).
- **Multi-Page Routes**: Scaffold internal routes `/collections/new-in` (detail, MPA), `/collections/bracelets` (detail, direct), `/apps/wishlist-1` (detail, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-unimaticwatches-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | New Langhe Collection | `1` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `22%` | The ICON collection | `1` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `1700px` | `43%` | #shopify-section-template--30951437730122__ed... | `1` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `2550px` | `65%` | #shopify-section-template--30951437730122__pr... | `1` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `3400px` | `86%` | Waterproof checked | `1` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `3941px` | `100%` | Waterproof checked | `1` | [desktop-step-06.webp](assets/desktop-step-06.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | New Langhe Collection | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `2629px` | `50%` | #shopify-section-template--30951437730122... | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `5259px` | `100%` | Watches | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `detail` | `https://www.unimaticwatches.com/collections/new-in` | Crafting modern timepieces that merge... | `4609px` | `MPA` (`1514ms`) | [subpage-01-collections-new-in.webp](assets/subpage-01-collections-new-in.webp) |
| `2` | `detail` | `https://www.unimaticwatches.com/collections/bracelets` | Crafting modern timepieces that merge... | `2566px` | `direct` (`3335ms`) | [subpage-02-collections-bracelets.webp](assets/subpage-02-collections-bracelets.webp) |
| `3` | `detail` | `https://www.unimaticwatches.com/apps/wishlist-1` | My wishlist | `923px` | `direct` (`4381ms`) | [subpage-03-apps-wishlist-1.webp](assets/subpage-03-apps-wishlist-1.webp) |

