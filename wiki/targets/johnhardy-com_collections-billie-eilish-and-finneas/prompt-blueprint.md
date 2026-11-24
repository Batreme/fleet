---
title: "UI Prompt Blueprint: johnhardy-com_collections-billie-eilish-and-finneas"
date: 2026-11-24
captured_at: 2026-11-24
target: "johnhardy-com_collections-billie-eilish-and-finneas"
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
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#ff5c1d`)"
---

# UI Design System & Master Generation Blueprint: johnhardy-com_collections-billie-eilish-and-finneas

> **Billie Eilish and FINNEAS – John Hardy** (https://johnhardy.com/collections/billie-eilish-and-finneas) — John Hardy fine luxury jewelry. Made in Bali since 1975. Enjoy complimentary shipping and returns on all orders. Bracelets, Rings, Neckla...

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Billie Eilish and FINNEAS – John Hardy** (`https://johnhardy.com/collections/billie-eilish-and-finneas`). John Hardy fine luxury jewelry. Made in Bali since 1975. Enjoy complimentary shipping and returns on all orders. Bracelets, Rings, Neckla...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#ff5c1d`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#ff5c1d` accents.
  - **Grounded Typographic Hierarchy**: Uses `General Sans` across display (`Billie Eilish & FINNEAS`) and body copy, paired with `Source Code Pro` for monospace/code.
  - **Calibrated Spatial Grid & Motion**: Combines `90rem` container bounds (`gap: 16px`, padding `var(--spacing-s)`) with `cubic-bezier(0.22,0.61,0.36,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=14400px` / doc `17026px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `90rem` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `var(--spacing-s)` lateral canvas padding with `16px` grid gap.
- **Border Radius Scale**: `4px`, `100%`, `50%`, `2px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 90rem`, `gap: 16px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--spacing-s)` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (forced-colors:active)`, `@media screen and (width<=750px)`, `@media (min-width:64em)`, `@media (max-width:63.99em)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#e5e5e5` | `var(--rb-smart-collections-reviews-background-color)` in `:root` |
| **Interactive Accent / Highlight** | `#ff5c1d` | `var(--color-brand-orange)` in `:root` |
| **Secondary / Muted Copy** | `#757575` | `var(--bonsai-agent-price-fg)` in `:root` |
| **Structural Hairline Border** | `#cccccc` | `var(--rb-widget-input-border-color)` in `:root` |
| **Variable Token (`--color-neutral-charcoal`)** | `#33383c` | `var(--color-neutral-charcoal)` in `:root` |
| **Variable Token (`--color-neutral-dark-grey`)** | `#646464` | `var(--color-neutral-dark-grey)` in `:root` |
| **Variable Token (`--color-neutral-light-grey`)** | `#e6e6e6` | `var(--color-neutral-light-grey)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--breakpoint-xs` | `0` | Design System Custom Token |
| `--breakpoint-s` | `36rem` | Dimension / Scale Token |
| `--breakpoint-m` | `48rem` | Dimension / Scale Token |
| `--breakpoint-l` | `64rem` | Dimension / Scale Token |
| `--breakpoint-xl` | `90rem` | Dimension / Scale Token |
| `--breakpoint-2xl` | `120rem` | Dimension / Scale Token |
| `--color-brand-black` | `#000` | Canvas / Surface Token |
| `--color-brand-orange` | `#ff5c1d` | Brand / Palette Token |
| `--color-neutral-black` | `#000` | Canvas / Surface Token |
| `--color-neutral-charcoal` | `#33383c` | Brand / Palette Token |
| `--color-neutral-dark-grey` | `#646464` | Canvas / Surface Token |
| `--color-neutral-light-grey` | `#e6e6e6` | Canvas / Surface Token |
| `--color-neutral-medium-grey` | `grey` | Brand / Palette Token |
| `--color-neutral-white` | `#fff` | Canvas / Surface Token |
| `--color-overlay` | `rgba(0,0,0,.3)` | Brand / Palette Token |
| `--color-overlay-background-overlay` | `rgba(0,0,0,.3)` | Canvas / Surface Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `General Sans`.
- **Primary Body Stack**: `General Sans`.
- **Technical / Metadata Stack**: `Source Code Pro`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: CSS variables `--x-shell-disclosure-display: block`, `--x-shell-order-summary-display: none`, `--x-shell-content-display: grid`; rule `h1` (`font-size: 1.5rem`, `line-height: 1.2`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 32px`, `line-height: 48px`, `font-weight: 500`, `letter-spacing: 0.5px`); rule `h2` (`font-size: var(--hero-title-size-mobile,...`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`, `letter-spacing: 0.5px`); CSS variables `--bonsai-font-body: var(--font-family-general-sans)`, `--bonsai-agent-body-bold-weight: 550`; rule `,p` (`font-size: var(--font-size-3)`, `line-height: var(--line-height-0)`, `letter-spacing: var(--letter-spacing-0)`, `font-weight: var(--font-we...`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`, `letter-spacing: 0.5px`); CSS variables `--letter-spacing-0: 0.5px`, `--letter-spacing-1: 1px`, `--letter-spacing-2: 1px`; rule `small` (`font-size: calc(var(--kl-reviews-reviews...`, `font-weight: var(--kl-revi...`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.22,0.61,0.36,1)`, `cubic-bezier(.22,.61,.36,1)`, `cubic-bezier(.65,.05,.36,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.shopify-payment-button__button`**: `transition: background .2s ease-in-out` extracted from `johnhardy-com_collections-billie-eilish-and-finneas` stylesheet.
- **Selector `.fade-leave-active`**: `transition: opacity var(--timing-normal) var(--easing-normal)` extracted from `johnhardy-com_collections-billie-eilish-and-finneas` stylesheet.
- **Selector `.fade-up-leave-active`**: `transition: opacity var(--timing-normal) var(--easing-normal),translate va...` extracted from `johnhardy-com_collections-billie-eilish-and-finneas` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.22,0.61,0.36,1)`)**: Governs interactive state transitions across `<header.site-header>` and `<section.hero-banner-section>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Barba.js Page Transition Router, Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `17026px`, deepest scrollY reached `14400px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: `WebGL/Canvas`.
- **Hover Physics (`primary_cta` · `SHOW THE SUB-MENU FOR COLLECTIONS...`)**: Computed transition `0s` / `ease` (no static color/transform shift captured at rest).
- **Route Transition Architecture**: First internal navigation (`/en-eu/pages/wishlist`) measured as `direct` in `3294ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Billie Eilish and FINNEAS – John Hardy     │
│ ====================================================================== │
│ [ <header.site-header> (1440x87px)    | Wishlist · Featured · New Ar ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.site-header-offset> (w=1440px)                | │
│ | H1: Billie Eilish & FINNEAS                                        | │
│ | Substrate: #ffffff | Ink: #000000 | Accent: #ff5c1d                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.hero-banner-secti) max-w: 90rem            | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Two Expressions of One Creat |  | “Jewelry has always been an  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.template-collecti) — Two years in the maki | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.usablenet>  ) | https://johnhardy.com/collections/b  │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.site-header>    ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.site-header-off) — 390px Vertical Lead        | │
│ | H1: Billie Eilish & FINNEAS                                        | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.hero-banner-s) — 1-Col Stack              | │
│ | [ Item 1: Two Expressions of One Creative Vision Two Expres...   ] | │
│ | [ Item 2: “Jewelry has always been an enormous part of how...    ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.template-collec) — 1-Col (Two years in the m) │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.usablenet>  ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.site-header> — `johnhardy-com_collections-billie-eilish-and-finneas`)**:
   - Landmark `<header class="site-header">` (`1440x87px`) hosting `Billie Eilish and FINNEAS – John Har` navigation (`Wishlist · Featured · New Arrivals · Best Sellers · Holiday Gifting`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-rapid="true"`, `data-shop-id="72737456428"`, `data-venmo-supported="true"`), and stylesheet rule `.shopify-payment-button__button--... { visibility:hidden }`.
2. **Hero Stage & Focal Lead (<section.site-header-offset> — `Billie Eilish & FINNEAS`)**:
   - Landmark `<section class="site-header-offset">` presenting display lead `Billie Eilish & FINNEAS` and copy excerpt *"Hard meets soft in two distinct design languages: delicate, roman"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.hero-banner-section> — `Two Expressions of One Creative Vi`)**:
   - Landmark `<section class="hero-banner-section">` rendering section `Two Expressions of One Creative Vision Two Expres...` with copy *"Billie Eilish & FINNEAS"*, asset references (`rebuy.js`, `loader.js`, `01HNXAYFWDBE125P1ZK44ZZ829`, `117791.ct.js`), and grid rule `opify-payment-button__button--unb... { background-color:1990c6;padding:1em 2em }`.
4. **Interactive Detail & Feature Matrix (<section.template-collection> — `“Jewelry has always been an enormo`)**:
   - Landmark `<section class="template-collection">` framing `“Jewelry has always been an enormous part of how...` and `Two years in the making` (*"Two Expressions of One Creative Vision"*) with `#e5e5e5` surface cards, `#ff5c1d` accents, and `ptions.shopify-payment-button__sk... { width:50%;margin-left:25%;margin-right:25%;border-radius:4px!important;h... }`.
5. **Colophon & Global Directory Footer (<footer.usablenet> — `https://johnhardy.com/collections/billie-eilish-and-finneas`)**:
   - Landmark `<footer class="usablenet">` anchoring `Billie Eilish and FINNEAS – John` footer links (`Wishlist · Featured · New Arrivals · Best Sellers · Holiday Gifting`), copy *"Wildflower Pendant Necklace, Sterling Silver, Lab Grown Diam"*, and `#cccccc` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=1px`, `0%`): Active landmark `Billie Eilish & FINNEAS` · sticky/fixed elements: `1`
- **Step 02** (`y=850px`, `5%`): Active landmark `Two Expressions of One Creative Vision` · sticky/fixed elements: `0`
- **Step 03** (`y=3400px`, `21%`): Active landmark `#site-header` · sticky/fixed elements: `0`
- **Step 04** (`y=5950px`, `37%`): Active landmark `#site-header` · sticky/fixed elements: `0`
- **Step 05** (`y=7650px`, `47%`): Active landmark `Two years in the making` · sticky/fixed elements: `0`
- **Step 06** (`y=10200px`, `63%`): Active landmark `Two years in the making` · sticky/fixed elements: `0`
- **Step 07** (`y=13600px`, `84%`): Active landmark `Two years in the making` · sticky/fixed elements: `0`
- **Step 08** (`y=14400px`, `89%`): Active landmark `Two years in the making` · sticky/fixed elements: `0`

### Multi-Page Internal Route Map
- **Detail Route (`/en-eu/pages/wishlist`)**: `https://johnhardy.com/en-eu/pages/wishlist` — H1: `Wishlist`, scrollHeight `1745px`, transition `direct` (`3294ms`)
- **Detail Route (`/collections/new-arrivals`)**: `https://johnhardy.com/collections/new-arrivals` — H1: `Women’s New Arrivals`, scrollHeight `8213px`, transition `direct` (`7301ms`)
- **Detail Route (`/en-eu/collections/womens-best-sellers`)**: `https://johnhardy.com/en-eu/collections/womens-best-sellers` — H1: `Women’s Best Sellers`, scrollHeight `7787px`, transition `direct` (`5838ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: johnhardy-com_collections-billie-eilish-and-finneas (Billie Eilish and FINNEAS – John Hardy)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `johnhardy-com_collections-billie-eilish-and-finneas` (**Billie Eilish and FINNEAS – John Hardy** — `https://johnhardy.com/collections/billie-eilish-and-finneas`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#ff5c1d`).
- **Identity & Domain Context**: John Hardy fine luxury jewelry. Made in Bali since 1975. Enjoy complimentary shipping and returns on all orders. Bracelets, Rings, Neckla...
- **Primary Substrate**: `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#000000`, **Accent / Highlight**: `#ff5c1d`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#ff5c1d` accents.
  - **Grounded Typographic Hierarchy**: Uses `General Sans` across display (`Billie Eilish & FINNEAS`) and body copy, paired with `Source Code Pro` for monospace/code.
  - **Calibrated Spatial Grid & Motion**: Combines `90rem` container bounds (`gap: 16px`, padding `var(--spacing-s)`) with `cubic-bezier(0.22,0.61,0.36,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `johnhardy-com_collections-billie-eilish-and-finneas` in your global stylesheet:

:root {
  /* Billie Eilish and FINNEAS – John Hardy (johnhardy-com_collections-billie-eilish-and-finneas) — Live-Grounded CSS Variables */
  --breakpoint-xs: 0; /* Design System Custom Token (johnhardy-com_collections-billie-eilish-and-finneas) */
  --breakpoint-s: 36rem; /* Dimension / Scale Token (johnhardy-com_collections-billie-eilish-and-finneas) */
  --breakpoint-m: 48rem; /* Dimension / Scale Token (johnhardy-com_collections-billie-eilish-and-finneas) */
  --breakpoint-l: 64rem; /* Dimension / Scale Token (johnhardy-com_collections-billie-eilish-and-finneas) */
  --breakpoint-xl: 90rem; /* Dimension / Scale Token (johnhardy-com_collections-billie-eilish-and-finneas) */
  --breakpoint-2xl: 120rem; /* Dimension / Scale Token (johnhardy-com_collections-billie-eilish-and-finneas) */
  --color-brand-black: #000; /* Canvas / Surface Token (johnhardy-com_collections-billie-eilish-and-finneas) */
  --color-brand-orange: #ff5c1d; /* Brand / Palette Token (johnhardy-com_collections-billie-eilish-and-finneas) */
  --color-neutral-black: #000; /* Canvas / Surface Token (johnhardy-com_collections-billie-eilish-and-finneas) */
  --color-neutral-charcoal: #33383c; /* Brand / Palette Token (johnhardy-com_collections-billie-eilish-and-finneas) */
  --color-neutral-dark-grey: #646464; /* Canvas / Surface Token (johnhardy-com_collections-billie-eilish-and-finneas) */
  --color-neutral-light-grey: #e6e6e6; /* Canvas / Surface Token (johnhardy-com_collections-billie-eilish-and-finneas) */
  --color-neutral-medium-grey: grey; /* Brand / Palette Token (johnhardy-com_collections-billie-eilish-and-finneas) */
  --color-neutral-white: #fff; /* Canvas / Surface Token (johnhardy-com_collections-billie-eilish-and-finneas) */
  --color-overlay: rgba(0,0,0,.3); /* Brand / Palette Token (johnhardy-com_collections-billie-eilish-and-finneas) */
  --color-overlay-background-overlay: rgba(0,0,0,.3); /* Canvas / Surface Token (johnhardy-com_collections-billie-eilish-and-finneas) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#000000` — grounded in live computed `main` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#e5e5e5` — grounded in `var(--rb-smart-collections-reviews-background-color)` in `:root`
- **Interactive Accent / Highlight**: `#ff5c1d` — grounded in `var(--color-brand-orange)` in `:root`
- **Secondary / Muted Copy**: `#757575` — grounded in `var(--bonsai-agent-price-fg)` in `:root`
- **Structural Hairline Border**: `#cccccc` — grounded in `var(--rb-widget-input-border-color)` in `:root`
- **Variable Token (`--color-neutral-charcoal`)**: `#33383c` — grounded in `var(--color-neutral-charcoal)` in `:root`
- **Variable Token (`--color-neutral-dark-grey`)**: `#646464` — grounded in `var(--color-neutral-dark-grey)` in `:root`
- **Variable Token (`--color-neutral-light-grey`)**: `#e6e6e6` — grounded in `var(--color-neutral-light-grey)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `90rem` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `var(--spacing-s)` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 90rem`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--spacing-s)` horizontal padding
- **Media Queries**: `@media screen and (forced-colors:active)`, `@media screen and (width<=750px)`, `@media (min-width:64em)`, `@media (max-width:63.99em)`
- **Corner Radii**: `4px`, `100%`, `50%`, `2px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `General Sans`
- **Body Font Stack**: `General Sans`
- **Monospace / Technical Font Stack**: `Source Code Pro`
- **H1 Display Rule**: CSS variables `--x-shell-disclosure-display: block`, `--x-shell-order-summary-display: none`, `--x-shell-content-display: grid`; rule `h1` (`font-size: 1.5rem`, `line-height: 1.2`)
- **H2 Section Rule**: live computed `h2` (`font-size: 32px`, `line-height: 48px`, `font-weight: 500`, `letter-spacing: 0.5px`); rule `h2` (`font-size: var(--hero-title-size-mobile,...`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`, `letter-spacing: 0.5px`); CSS variables `--bonsai-font-body: var(--font-family-general-sans)`, `--bonsai-agent-body-bold-weight: 550`; rule `,p` (`font-size: var(--font-size-3)`, `line-height: var(--line-height-0)`, `letter-spacing: var(--letter-spacing-0)`, `font-weight: var(--font-we...`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`, `letter-spacing: 0.5px`); CSS variables `--letter-spacing-0: 0.5px`, `--letter-spacing-1: 1px`, `--letter-spacing-2: 1px`; rule `small` (`font-size: calc(var(--kl-reviews-reviews...`, `font-weight: var(--kl-revi...`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `johnhardy-com_collections-billie-eilish-and-finneas` (`Billie Eilish and FINNEAS – John Hardy`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.site-header> — `johnhardy-com_collections-billie-eilish-and-finneas`)**:
   - DOM & Selectors: Landmark `<header class="site-header">` (`1440x87px`) hosting `Billie Eilish and FINNEAS – John Har` navigation (`Wishlist · Featured · New Arrivals · Best Sellers · Holiday Gifting`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-rapid="true"`, `data-shop-id="72737456428"`, `data-venmo-supported="true"`), and stylesheet rule `.shopify-payment-button__button--... { visibility:hidden }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.site-header> — `johnhardy-com_collections-billie-eilish-and-finneas`)` (`johnhardy-com_collections-billie-eilish-and-finneas`) adapts across `@media screen and (forced-colors:active)`, `@media screen and (width<=750px)`, `@media (min-width:64em)`, `@media (max-width:63.99em)` with `cubic-bezier(0.22,0.61,0.36,1)`, `cubic-bezier(.22,.61,.36,1)`, `cubic-bezier(.65,.05,.36,1)` transitions and links `Wishlist · Featured · New Arrivals · Best Sellers · Holiday Gifting`.
2. **Hero Stage & Focal Lead (<section.site-header-offset> — `Billie Eilish & FINNEAS`)**:
   - DOM & Selectors: Landmark `<section class="site-header-offset">` presenting display lead `Billie Eilish & FINNEAS` and copy excerpt *"Hard meets soft in two distinct design languages: delicate, roman"* over `#ffffff` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×2616px` mobile) sets `#ffffff` background with `#000000` headline `Billie Eilish & FINNEAS`.
3. **Primary Showcase & Content Grid (<section.hero-banner-section> — `Two Expressions of One Creative Vi`)**:
   - DOM & Selectors: Landmark `<section class="hero-banner-section">` rendering section `Two Expressions of One Creative Vision Two Expres...` with copy *"Billie Eilish & FINNEAS"*, asset references (`rebuy.js`, `loader.js`, `01HNXAYFWDBE125P1ZK44ZZ829`, `117791.ct.js`), and grid rule `opify-payment-button__button--unb... { background-color:1990c6;padding:1em 2em }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.hero-banner-section> — `Two Expressions of One Creative Vi`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 90rem`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--spacing-s)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.template-collection> — `“Jewelry has always been an enormo`)**:
   - DOM & Selectors: Landmark `<section class="template-collection">` framing `“Jewelry has always been an enormous part of how...` and `Two years in the making` (*"Two Expressions of One Creative Vision"*) with `#e5e5e5` surface cards, `#ff5c1d` accents, and `ptions.shopify-payment-button__sk... { width:50%;margin-left:25%;margin-right:25%;border-radius:4px!important;h... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.template-collection> — `“Jewelry has always been an enormo`)` uses `4px`, `100%`, `50%`, `2px` radii, `#ff5c1d` highlights, and assets (rebuy.js, loader.js, 01HNXAYFWDBE125P1ZK44ZZ829).
5. **Colophon & Global Directory Footer (<footer.usablenet> — `https://johnhardy.com/collections/billie-eilish-and-finneas`)**:
   - DOM & Selectors: Landmark `<footer class="usablenet">` anchoring `Billie Eilish and FINNEAS – John` footer links (`Wishlist · Featured · New Arrivals · Best Sellers · Holiday Gifting`), copy *"Wildflower Pendant Necklace, Sterling Silver, Lab Grown Diam"*, and `#cccccc` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.usablenet> — `https://johnhardy.com/collections/billie-eilish-and-finneas`)` aligns to `90rem` (non-`@media` desktop container stylesheet rule) with `var(--spacing-s)` lateral canvas padding with `16px` grid gap and attributes (data-source-attribution="shopify.exit_intersti...", data-rapid="true", data-shop-id="72737456428").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Hard meets soft in two distinct design languages: delicate, romantic Wildflower an..."*
- Copy Excerpt 2: *"Billie Eilish & FINNEAS"*
- Copy Excerpt 3: *"Two Expressions of One Creative Vision"*
- Copy Excerpt 4: *"Wildflower Pendant Necklace, Sterling Silver, Lab Grown Diamond, 0.1TCW"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.22,0.61,0.36,1)`, `cubic-bezier(.22,.61,.36,1)`, `cubic-bezier(.65,.05,.36,1)`
- **Extracted Stylesheet Rules (`johnhardy-com_collections-billie-eilish-and-finneas`)**:
- `.shopify-payment-button__button--... { visibility:hidden }`
- `opify-payment-button__button--unb... { background-color:1990c6;padding:1em 2em }`
- `ptions.shopify-payment-button__sk... { width:50%;margin-left:25%;margin-right:25%;border-radius:4px!important;h... }`
- `shopify-payment-button__button--b... { z-index:1;flex-direction:column;display:flex;position:relative }`
- `on__button--branded .shopify-clea... { flex-direction:column!important;flex:1!important;display:flex!important }`
- **Per-Selector Transition Rules**:
- **Selector `.shopify-payment-button__button`**: `transition: background .2s ease-in-out` extracted from `johnhardy-com_collections-billie-eilish-and-finneas` stylesheet.
- **Selector `.fade-leave-active`**: `transition: opacity var(--timing-normal) var(--easing-normal)` extracted from `johnhardy-com_collections-billie-eilish-and-finneas` stylesheet.
- **Selector `.fade-up-leave-active`**: `transition: opacity var(--timing-normal) var(--easing-normal),translate va...` extracted from `johnhardy-com_collections-billie-eilish-and-finneas` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.22,0.61,0.36,1)`)**: Governs interactive state transitions across `<header.site-header>` and `<section.hero-banner-section>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Barba.js Page Transition Router, Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `17026px` across 8 distinct viewport chapters using WebGL/Canvas.
- **Vertical Chapter Sequence**: Billie Eilish & FINNEAS (0%) -> Two Expressions of One Crea... (5%) -> #site-header (21%) -> #site-header (37%) -> Two years in the making (47%) -> Two years in the making (63%) -> Two years in the making (84%) -> Two years in the making (89%).
- **Multi-Page Routes**: Scaffold internal routes `/en-eu/pages/wishlist` (detail, direct), `/collections/new-arrivals` (detail, direct), `/en-eu/collections/womens-best-sellers` (detail, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `johnhardy-com_collections-billie-eilish-and-finneas`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `1px` | `0%` | Billie Eilish & FINNEAS | `1` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `5%` | Two Expressions of One Creative Vision | `0` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `3400px` | `21%` | #site-header | `0` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `5950px` | `37%` | #site-header | `0` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `7650px` | `47%` | Two years in the making | `0` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `10200px` | `63%` | Two years in the making | `0` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `13600px` | `84%` | Two years in the making | `0` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `14400px` | `89%` | Two years in the making | `0` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `1px` | `0%` | Billie Eilish & FINNEAS | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `7070px` | `50%` | Two years in the making | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `14140px` | `100%` | Two years in the making | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `detail` | `https://johnhardy.com/en-eu/pages/wishlist` | Wishlist | `1745px` | `direct` (`3294ms`) | [subpage-01-en-eu-pages-wishlist.webp](assets/subpage-01-en-eu-pages-wishlist.webp) |
| `2` | `detail` | `https://johnhardy.com/collections/new-arrivals` | Women’s New Arrivals | `8213px` | `direct` (`7301ms`) | [subpage-02-collections-new-arrivals.webp](assets/subpage-02-collections-new-arrivals.webp) |
| `3` | `detail` | `https://johnhardy.com/en-eu/collections/womens-best-sellers` | Women’s Best Sellers | `7787px` | `direct` (`5838ms`) | [subpage-03-en-eu-collections-womens-best-seller.webp](assets/subpage-03-en-eu-collections-womens-best-seller.webp) |

