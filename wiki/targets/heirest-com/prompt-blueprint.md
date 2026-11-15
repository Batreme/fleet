---
title: "UI Prompt Blueprint: heirest-com"
date: 2026-11-15
target: "[[overview|heirest-com]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#DFDFDF` canvas, `#000000` ink, `#ffffff` accent)"
---

# UI Design System & Master Generation Blueprint: heirest-com

> **HEIREST · Fine Jewellery, Authored By You** (https://heirest.com/) — Fine jewellery for those who choose to author what others inherit. Configured by you and crafted to last.

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **HEIREST · Fine Jewellery, Authored By You** (`https://heirest.com/`). Fine jewellery for those who choose to author what others inherit. Configured by you and crafted to last.
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#DFDFDF` canvas, `#000000` ink, `#ffffff` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#DFDFDF` (`var(--accordion-border-color)` in `:root`) paired with `#000000` primary typography and `#ffffff` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Inter` for display copy (`Cookie consent`) with `Moderat-Regular` and `ModeratMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `767.98px` container bounds (`gap: var(--gap)`, padding `var(--page-margin)`) with `cubic-bezier(.25,.1,.25,1)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `767.98px` extracted from `heirest-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--page-margin)` lateral canvas padding with `var(--gap)` grid gap.
- **Border Radius Scale**: `var(--style-border-radius-inputs)`, `var(--border-radius)`, `var(--style-border-radius-popover)`, `var(--style-border-radius-buttons-primary)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 767.98px`, `gap: var(--gap)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--page-margin)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:767.98px)`, `@media (any-pointer:fine)and (prefers-reduced-motion:no-preference)`, `@media (prefers-reduced-motion:no-preference)`, `@media screen and (min-width:768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#DFDFDF` | `var(--accordion-border-color)` in `:root` |
| **Primary Typography Ink** | `#f9f8f6` | `var(--product-image-tint)` in `:root` |
| **Elevated Surface / Card Substrate** | `#000000` | `var(--bundle-component-title-color)` in `:root` |
| **Interactive Accent / Highlight** | `#ffffff` | `var(--bundle-component-background)` in `:root` |
| **Secondary / Muted Copy** | `#cccccc` | `var(--bundle-option-border-color)` in `:root` |
| **Structural Hairline Border** | `#202020` | `var(--paragraph-color)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--hover-lift-amount` | `4px` | Dimension / Scale Token |
| `--hover-scale-amount` | `1.03` | Design System Custom Token |
| `--hover-subtle-zoom-amount` | `1.015` | Design System Custom Token |
| `--hover-shadow-color` | `var(--color-shadow)` | Brand / Palette Token |
| `--hover-transition-duration` | `var(--global-transition-duration)` | Motion / Easing Token |
| `--hover-transition-timing` | `var(--global-transition-timing-function)` | Motion / Easing Token |
| `--surface-transition-duration` | `var(--global-transition-duration)` | Canvas / Surface Token |
| `--surface-transition-timing` | `var(--global-transition-timing-function)` | Canvas / Surface Token |
| `--submenu-animation-speed` | `.36s` | Motion / Easing Token |
| `--submenu-animation-easing` | `cubic-bezier(.25, .1, .25, 1)` | Motion / Easing Token |
| `--icon-stroke-width` | `1px` | Layout / Spatial Grid Token |
| `--backdrop-color-rgb` | `var(--color-shadow-rgb)` | Brand / Palette Token |
| `--page-margin` | `16px` | Layout / Spatial Grid Token |
| `--full-page-grid-margin` | `minmax(var(--page-margin), 1fr)` | Layout / Spatial Grid Token |
| `--full-page-margin-inline-offset` | `calc(((100vw - var(--full-page-grid-central-column-width)) / 2) * -1)` | Layout / Spatial Grid Token |
| `--dot-size` | `var(--section-dot-size, 1.5px)` | Layout / Spatial Grid Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Inter`.
- **Primary Body Stack**: `Moderat-Regular`.
- **Technical / Metadata Stack**: `ModeratMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--loyalty-shimmer-display: none`, `--font-h1--spacing: var(--font-heading--spacing)`, `--font-h1--color: var(--color-foreground-heading)`; rule `h1` (`line-height: var(--line-height--di...`).
- **Section Heading (`H2`)**: CSS variables `--loyalty-banner-subtitle-size: 14px`, `--font-h2--spacing: var(--font-heading--spacing)`, `--font-h2--color: var(--color-foreground-heading)`; rule `h2` (`font-size: var(--heading-font-size)`, `font-weight: var(--heading...`).
- **Body Copy**: CSS variables `--paragraph-color: #202020`, `--paragraph-font-size: 16px`, `--paragraph-font-weight: 400`; rule `p` (`line-height: var(--line-height--bo...`).
- **Metadata & Navigation Labels**: CSS variables `--default-mono-font-family: var(--font-mono)`, `--bundle-product-label-color: #000000`, `--bundle-product-label-size: 16px`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.25,.1,.25,1)`, `cubic-bezier(.7,-5,.98,.5)`, `cubic-bezier(.15,.57,.9,1.05)`.

### Per-Element Transition & Choreography Rules
- **Selector `:root`**: `transition: var(--global-transition-duration)` extracted from `heirest-com` stylesheet.
- **Selector `.predictive-search-results__card`**: `transition: transform var(--hover-transition-duration) var(--hover-transit...` extracted from `heirest-com` stylesheet.
- **Selector `ver-effect-subtle-zoom .product-c...`**: `transition: transform var(--hover-transition-duration) var(--hover-transit...` extracted from `heirest-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.25,.1,.25,1)`)**: Governs interactive state transitions across `<header.shopify-section>` and `<section.shopify-section>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — HEIREST · Fine Jewellery, Authored By You  │
│ ====================================================================== │
│ [ <header.shopify-section> | Bespoke · Our Standards · Sizing Kits  ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.shopify-pc__banner__dialog>                 |   │
│ | H1: Cookie consent                                               |   │
│ | Substrate: #DFDFDF    | Ink: #000000    | Accent: #ffffff        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.shopify-section> ) max-w: 767.98px       |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Your Cart Your cart is empty |  | Subscribe to our newsletter  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<header.shopify-se] -> [<section.shopify-p] -> [<section.shopify-s] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.announcement-b) | https://heirest.com/               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.shopify-section> — `heirest-com`)**:
   - Landmark `<header class="shopify-section shopify-section-group-header-group">` hosting `HEIREST · Fine Jewellery, Authored B` navigation (`Bespoke · Our Standards · Sizing Kits`), DOM attributes (`data-swym-guest-login-bound="1"`, `data-source-attribution="shopify.exit_intersti..."`, `data-source-attribution="shopify.event_observe..."`, `data-shopify`), and stylesheet rule `body { scrollbar-width:none;-ms-overflow-style:none }`.
2. **Hero Stage & Focal Lead (<section.shopify-pc__banner__dialog> — `Cookie consent`)**:
   - Landmark `<section class="shopify-pc__banner__dialog">` presenting display lead `Cookie consent` and copy excerpt *"cookies are used on this site. Privacy Policy"* over `#DFDFDF` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.shopify-section> — `Your Cart Your cart is empty`)**:
   - Landmark `<section class="shopify-section shopify-section-group-header-group">` rendering section `Your Cart Your cart is empty` with copy *"SHOP THE HEIREST SIZING KIT · ONLY $19 + FREE SHIPPING SHOP THE H"*, asset references (`clarity.js`, `y0e70x819z`, `gtm.js`, `cdn.shopify.com`), and grid rule `body::-webkit-scrollbar { width:0;height:0;display:none }`.
4. **Interactive Detail & Feature Matrix (<section.shopify-section> — `Subscribe to our newsletter`)**:
   - Landmark `<section class="shopify-section shopify-section-group-header-group">` framing `Subscribe to our newsletter` and `Slideshow` (*"SHOP THE HEIREST SIZING KIT · ONLY $19 + FREE SHIPPING"*) with `#000000` surface cards, `#ffffff` accents, and `svg { display:block;max-width:100% }`.
5. **Colophon & Global Directory Footer (<footer.announcement-bar--show> — `https://heirest.com/`)**:
   - Landmark `<footer class="announcement-bar--show">` anchoring `HEIREST · Fine Jewellery, Author` footer links (`Bespoke · Our Standards · Sizing Kits`), copy *"Translation missing: en.localization.currency_label AED AUD "*, and `#202020` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: heirest-com (HEIREST · Fine Jewellery, Authored By You)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `heirest-com` (**HEIREST · Fine Jewellery, Authored By You** — `https://heirest.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#DFDFDF` canvas, `#000000` ink, `#ffffff` accent).
- **Identity & Domain Context**: Fine jewellery for those who choose to author what others inherit. Configured by you and crafted to last.
- **Primary Substrate**: `#DFDFDF` (`var(--accordion-border-color)` in `:root`), **Primary Ink**: `#000000`, **Accent / Highlight**: `#ffffff`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#DFDFDF` (`var(--accordion-border-color)` in `:root`) paired with `#000000` primary typography and `#ffffff` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Inter` for display copy (`Cookie consent`) with `Moderat-Regular` and `ModeratMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `767.98px` container bounds (`gap: var(--gap)`, padding `var(--page-margin)`) with `cubic-bezier(.25,.1,.25,1)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `heirest-com` in your global stylesheet:

:root {
  /* HEIREST · Fine Jewellery, Authored By You (heirest-com) — Ground-Truth Extracted CSS Variables */
  --hover-lift-amount: 4px; /* Dimension / Scale Token (heirest-com) */
  --hover-scale-amount: 1.03; /* Design System Custom Token (heirest-com) */
  --hover-subtle-zoom-amount: 1.015; /* Design System Custom Token (heirest-com) */
  --hover-shadow-color: var(--color-shadow); /* Brand / Palette Token (heirest-com) */
  --hover-transition-duration: var(--global-transition-duration); /* Motion / Easing Token (heirest-com) */
  --hover-transition-timing: var(--global-transition-timing-function); /* Motion / Easing Token (heirest-com) */
  --surface-transition-duration: var(--global-transition-duration); /* Canvas / Surface Token (heirest-com) */
  --surface-transition-timing: var(--global-transition-timing-function); /* Canvas / Surface Token (heirest-com) */
  --submenu-animation-speed: .36s; /* Motion / Easing Token (heirest-com) */
  --submenu-animation-easing: cubic-bezier(.25, .1, .25, 1); /* Motion / Easing Token (heirest-com) */
  --icon-stroke-width: 1px; /* Layout / Spatial Grid Token (heirest-com) */
  --backdrop-color-rgb: var(--color-shadow-rgb); /* Brand / Palette Token (heirest-com) */
  --page-margin: 16px; /* Layout / Spatial Grid Token (heirest-com) */
  --full-page-grid-margin: minmax(var(--page-margin), 1fr); /* Layout / Spatial Grid Token (heirest-com) */
  --full-page-margin-inline-offset: calc(((100vw - var(--full-page-grid-central-column-width)) / 2) * -1); /* Layout / Spatial Grid Token (heirest-com) */
  --dot-size: var(--section-dot-size, 1.5px); /* Layout / Spatial Grid Token (heirest-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#DFDFDF` — grounded in `var(--accordion-border-color)` in `:root`
- **Primary Typography Ink**: `#f9f8f6` — grounded in `var(--product-image-tint)` in `:root`
- **Elevated Surface / Card Substrate**: `#000000` — grounded in `var(--bundle-component-title-color)` in `:root`
- **Interactive Accent / Highlight**: `#ffffff` — grounded in `var(--bundle-component-background)` in `:root`
- **Secondary / Muted Copy**: `#cccccc` — grounded in `var(--bundle-option-border-color)` in `:root`
- **Structural Hairline Border**: `#202020` — grounded in `var(--paragraph-color)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `767.98px` extracted from `heirest-com` stylesheet
- **Padding & Gutters**: `var(--page-margin)` lateral canvas padding with `var(--gap)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 767.98px`, `gap: var(--gap)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--page-margin)` horizontal padding
- **Media Queries**: `@media (max-width:767.98px)`, `@media (any-pointer:fine)and (prefers-reduced-motion:no-preference)`, `@media (prefers-reduced-motion:no-preference)`, `@media screen and (min-width:768px)`
- **Corner Radii**: `var(--style-border-radius-inputs)`, `var(--border-radius)`, `var(--style-border-radius-popover)`, `var(--style-border-radius-buttons-primary)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Moderat-Regular`
- **Monospace / Technical Font Stack**: `ModeratMono-Regular`
- **H1 Display Rule**: CSS variables `--loyalty-shimmer-display: none`, `--font-h1--spacing: var(--font-heading--spacing)`, `--font-h1--color: var(--color-foreground-heading)`; rule `h1` (`line-height: var(--line-height--di...`)
- **H2 Section Rule**: CSS variables `--loyalty-banner-subtitle-size: 14px`, `--font-h2--spacing: var(--font-heading--spacing)`, `--font-h2--color: var(--color-foreground-heading)`; rule `h2` (`font-size: var(--heading-font-size)`, `font-weight: var(--heading...`)
- **Body Copy Rule**: CSS variables `--paragraph-color: #202020`, `--paragraph-font-size: 16px`, `--paragraph-font-weight: 400`; rule `p` (`line-height: var(--line-height--bo...`)
- **Metadata & Index Rule**: CSS variables `--default-mono-font-family: var(--font-mono)`, `--bundle-product-label-color: #000000`, `--bundle-product-label-size: 16px`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `heirest-com` (`HEIREST · Fine Jewellery, Authored By You`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.shopify-section> — `heirest-com`)**:
   - DOM & Selectors: Landmark `<header class="shopify-section shopify-section-group-header-group">` hosting `HEIREST · Fine Jewellery, Authored B` navigation (`Bespoke · Our Standards · Sizing Kits`), DOM attributes (`data-swym-guest-login-bound="1"`, `data-source-attribution="shopify.exit_intersti..."`, `data-source-attribution="shopify.event_observe..."`, `data-shopify`), and stylesheet rule `body { scrollbar-width:none;-ms-overflow-style:none }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.shopify-section> — `heirest-com`)` (`heirest-com`) adapts across `@media (max-width:767.98px)`, `@media (any-pointer:fine)and (prefers-reduced-motion:no-preference)`, `@media (prefers-reduced-motion:no-preference)`, `@media screen and (min-width:768px)` with `cubic-bezier(.25,.1,.25,1)`, `cubic-bezier(.7,-5,.98,.5)`, `cubic-bezier(.15,.57,.9,1.05)` transitions and links `Bespoke · Our Standards · Sizing Kits`.
2. **Hero Stage & Focal Lead (<section.shopify-pc__banner__dialog> — `Cookie consent`)**:
   - DOM & Selectors: Landmark `<section class="shopify-pc__banner__dialog">` presenting display lead `Cookie consent` and copy excerpt *"cookies are used on this site. Privacy Policy"* over `#DFDFDF` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#DFDFDF` background with `#000000` headline `Cookie consent`.
3. **Primary Showcase & Content Grid (<section.shopify-section> — `Your Cart Your cart is empty`)**:
   - DOM & Selectors: Landmark `<section class="shopify-section shopify-section-group-header-group">` rendering section `Your Cart Your cart is empty` with copy *"SHOP THE HEIREST SIZING KIT · ONLY $19 + FREE SHIPPING SHOP THE H"*, asset references (`clarity.js`, `y0e70x819z`, `gtm.js`, `cdn.shopify.com`), and grid rule `body::-webkit-scrollbar { width:0;height:0;display:none }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.shopify-section> — `Your Cart Your cart is empty`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 767.98px`, `gap: var(--gap)`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--page-margin)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.shopify-section> — `Subscribe to our newsletter`)**:
   - DOM & Selectors: Landmark `<section class="shopify-section shopify-section-group-header-group">` framing `Subscribe to our newsletter` and `Slideshow` (*"SHOP THE HEIREST SIZING KIT · ONLY $19 + FREE SHIPPING"*) with `#000000` surface cards, `#ffffff` accents, and `svg { display:block;max-width:100% }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.shopify-section> — `Subscribe to our newsletter`)` uses `var(--style-border-radius-inputs)`, `var(--border-radius)`, `var(--style-border-radius-popover)`, `var(--style-border-radius-buttons-primary)` radii, `#ffffff` highlights, and assets (clarity.js, y0e70x819z, gtm.js).
5. **Colophon & Global Directory Footer (<footer.announcement-bar--show> — `https://heirest.com/`)**:
   - DOM & Selectors: Landmark `<footer class="announcement-bar--show">` anchoring `HEIREST · Fine Jewellery, Author` footer links (`Bespoke · Our Standards · Sizing Kits`), copy *"Translation missing: en.localization.currency_label AED AUD "*, and `#202020` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.announcement-bar--show> — `https://heirest.com/`)` aligns to `767.98px` extracted from `heirest-com` stylesheet with `var(--page-margin)` lateral canvas padding with `var(--gap)` grid gap and attributes (data-swym-guest-login-bound="1", data-source-attribution="shopify.exit_intersti...", data-source-attribution="shopify.event_observe...").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"cookies are used on this site. Privacy Policy"*
- Copy Excerpt 2: *"SHOP THE HEIREST SIZING KIT · ONLY $19 + FREE SHIPPING SHOP THE HEIREST SIZING KIT..."*
- Copy Excerpt 3: *"SHOP THE HEIREST SIZING KIT · ONLY $19 + FREE SHIPPING"*
- Copy Excerpt 4: *"Translation missing: en.localization.currency_label AED AUD CAD CHF CZK DKK EUR GB..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.25,.1,.25,1)`, `cubic-bezier(.7,-5,.98,.5)`, `cubic-bezier(.15,.57,.9,1.05)`
- **Extracted Stylesheet Rules (`heirest-com`)**:
- `body { scrollbar-width:none;-ms-overflow-style:none }`
- `body::-webkit-scrollbar { width:0;height:0;display:none }`
- `svg { display:block;max-width:100% }`
- `img { width:100%;height:auto }`
- `select { font:inherit;border-radius:var(--style-border-radius-inputs) }`
- **Per-Selector Transition Rules**:
- **Selector `:root`**: `transition: var(--global-transition-duration)` extracted from `heirest-com` stylesheet.
- **Selector `.predictive-search-results__card`**: `transition: transform var(--hover-transition-duration) var(--hover-transit...` extracted from `heirest-com` stylesheet.
- **Selector `ver-effect-subtle-zoom .product-c...`**: `transition: transform var(--hover-transition-duration) var(--hover-transit...` extracted from `heirest-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.25,.1,.25,1)`)**: Governs interactive state transitions across `<header.shopify-section>` and `<section.shopify-section>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `heirest-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
