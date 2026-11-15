---
title: "UI Prompt Blueprint: www-halcyon-co-nz"
date: 2026-11-15
target: "[[overview|www-halcyon-co-nz]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#32e26e` / `#f59e0b`)"
---

# UI Design System & Master Generation Blueprint: www-halcyon-co-nz

> **Halcyon · Leading Lighting Specialists** (https://www.halcyon.co.nz/) — Driven by innovation and an unwavering commitment to quality, Halcyon works with leading architects, specifiers and electrical experts to...

![Desktop Viewport Capture (1440x6175)](file:///root/projects/fleet/wiki/targets/www-halcyon-co-nz/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Halcyon · Leading Lighting Specialists** (`https://www.halcyon.co.nz/`). Driven by innovation and an unwavering commitment to quality, Halcyon works with leading architects, specifiers and electrical experts to...
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#32e26e` / `#f59e0b`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#32e26e` (`var(--halcyon-toast-success)` in `:root`) paired with `#000` primary typography and `#f59e0b` accents.
  - **Extracted Typographic Hierarchy**: Pairs `etica-display` for display copy (`Confirmation`) with `lft-etica` and `Halcyon Monument Grotesk Semi-Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `991px` container bounds (`gap: var(--boostsd-product-list-gap-list-view-desktop)`, padding `var(--boostsd-breadcrumb-padding)`) with `cubic-bezier(0,0,.58,1)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/www-halcyon-co-nz/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×6175px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `991px` extracted from `www-halcyon-co-nz` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--boostsd-breadcrumb-padding)` lateral canvas padding with `var(--boostsd-product-list-gap-list-view-desktop)` grid gap.
- **Border Radius Scale**: `4px`, `8px`, `50%`, `var(--boostsd-bundle-style-image-border-radius)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 991px`, `gap: var(--boostsd-product-list-gap-list-view-desktop)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--boostsd-breadcrumb-padding)` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (forced-colors:active)`, `@media screen and (width<=750px)`, `@media only screen and (max-width:991px)`, `@media only screen and (min-width:992px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#32e26e` | `var(--halcyon-toast-success)` in `:root` |
| **Primary Typography Ink** | `#e75619` | `var(--halcyon-toast-error)` in `:root` |
| **Elevated Surface / Card Substrate** | `#3b82f6` | `var(--halcyon-toast-info)` in `:root` |
| **Interactive Accent / Highlight** | `#f59e0b` | `var(--halcyon-toast-warning)` in `:root` |
| **Secondary / Muted Copy** | `#000` | `var(--halcyon-toast-text)` in `:root` |
| **Structural Hairline Border** | `#222` | `var(--boostsd-general-color-primary)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--height-full` | `100vh` | Layout / Spatial Grid Token |
| `--height-fill` | `calc(100vh - var(--nav-height))` | Layout / Spatial Grid Token |
| `--font-orion` | `"Untitled", sans-serif` | Typography / Scale Token |
| `--annoucement-height` | `37px` | Layout / Spatial Grid Token |
| `--nav-main-height` | `44px` | Layout / Spatial Grid Token |
| `--nav-height` | `calc(var(--nav-main-height))` | Layout / Spatial Grid Token |
| `--halcyon-toast-success` | `#32e26e` | Color / Atmospheric Token |
| `--halcyon-toast-error` | `#e75619` | Color / Atmospheric Token |
| `--halcyon-toast-info` | `#3b82f6` | Color / Atmospheric Token |
| `--halcyon-toast-warning` | `#f59e0b` | Color / Atmospheric Token |
| `--halcyon-toast-text` | `#000` | Typography Ink Token |
| `--halcyon-toast-max-width` | `500px` | Layout / Spatial Grid Token |
| `--halcyon-toast-sweep-duration` | `5s` | Motion / Easing Token |
| `--boostsd-general-page-width-desktop` | `1216px` | Layout / Spatial Grid Token |
| `--boostsd-general-color-primary` | `#222` | Brand / Palette Token |
| `--boostsd-general-font-size-base` | `16px` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `etica-display`.
- **Primary Body Stack**: `lft-etica`.
- **Technical / Metadata Stack**: `Halcyon Monument Grotesk Semi-Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `30px`, `40px`, `var(--boostsd-filter-search-optio...`, `20px`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `30px`, `40px`, `var(--boostsd-filter-search-optio...`, `20px`).
- **Body Copy**: CSS variables `--boostsd-general-font-size-base: 16px`, `--boostsd-cart-body-padding: 16px`, `--boostsd-cart-body-padding-medium: 24px`; rule `p` (`font-size: 13px`, `line-height: 17px`, `letter-spacing: 0`, `font-weight: 500`).
- **Metadata & Navigation Labels**: CSS variables `--boostsd-product-label-padding: 2px 6px`, `--boostsd-product-label-border-radius: 2px`, `--boostsd-product-label-border-radius-capsule: 40px`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0,0,.58,1)`, `cubic-bezier(.23,1,.32,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.shopify-payment-button__button`**: `transition: background .2s ease-in-out` extracted from `www-halcyon-co-nz` stylesheet.
- **Selector `.boost-sd__filter-option-title:be...`**: `transition: none` extracted from `www-halcyon-co-nz` stylesheet.
- **Selector `d__button--show-text-on-hover:foc...`**: `transition: width .4s ease` extracted from `www-halcyon-co-nz` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.58,1)`)**: Governs interactive state transitions across `<header.js>` and `<section.featured-product>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Halcyon · Leading Lighting Specialists     │
│ ====================================================================== │
│ [ <header.js>              | Return · Products · About · Highlights ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.main-hero>                                  |   │
│ | H1: Confirmation                                                 |   │
│ | Substrate: #32e26e    | Ink: #000       | Accent: #f59e0b        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.featured-product>) max-w: 991px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Dark Art Slim Trim           |  | Trade Flex Pro               | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<header.js>] -> [<section.main-hero] -> [<section.featured-] |      │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.js-ajax-cart-e) | https://www.halcyon.co.nz/         │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.js> — `www-halcyon-co-nz`)**:
   - Landmark `<header class="js">` hosting `Halcyon · Leading Lighting Specialis` navigation (`Return · Products · About · Highlights · Stockists`), DOM attributes (`data-collection-view="grid"`, `data-source-attribution="shopify.exit_intersti..."`, `data-source-attribution="shopify.loadfeatures"`, `data-source-attribution="shopify.dynamic_check..."`), and stylesheet rule `.shopify-payment-button__button--... { visibility:hidden }`.
2. **Hero Stage & Focal Lead (<section.main-hero> — `Confirmation`)**:
   - Landmark `<section class="main-hero hero-main-section">` presenting display lead `Confirmation` and copy excerpt *"No wishlists found"* over `#32e26e` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.featured-product> — `Dark Art Slim Trim`)**:
   - Landmark `<section class="featured-product">` rendering section `Dark Art Slim Trim` with copy *"SAVE ITEM TO FAVOURITES LIST"*, asset references (`inventoryLocation.js`, `clarity.js`, `wwzwszat2d`, `gtm.js`), and grid rule `opify-payment-button__button--unb... { background-color:1990c6;padding:1em 2em }`.
4. **Interactive Detail & Feature Matrix (<section.tabbed-collection> — `Trade Flex Pro`)**:
   - Landmark `<section class="tabbed-collection">` framing `Trade Flex Pro` and `Mini Mariner` (*"Remove from this list"*) with `#3b82f6` surface cards, `#f59e0b` accents, and `ptions.shopify-payment-button__sk... { width:50%;margin-left:25%;margin-right:25%;border-radius:4px!important;h... }`.
5. **Colophon & Global Directory Footer (<footer.js-ajax-cart-empty> — `https://www.halcyon.co.nz/`)**:
   - Landmark `<footer class="js-ajax-cart-empty">` anchoring `Halcyon · Leading Lighting Speci` footer links (`Return · Products · About · Highlights · Stockists`), copy *"Create a personalised list to organise your favourite items"*, and `#222` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-halcyon-co-nz (Halcyon · Leading Lighting Specialists)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-halcyon-co-nz` (**Halcyon · Leading Lighting Specialists** — `https://www.halcyon.co.nz/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#32e26e` / `#f59e0b`).
- **Identity & Domain Context**: Driven by innovation and an unwavering commitment to quality, Halcyon works with leading architects, specifiers and electrical experts to...
- **Primary Substrate**: `#32e26e` (`var(--halcyon-toast-success)` in `:root`), **Primary Ink**: `#000`, **Accent / Highlight**: `#f59e0b`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#32e26e` (`var(--halcyon-toast-success)` in `:root`) paired with `#000` primary typography and `#f59e0b` accents.
  - **Extracted Typographic Hierarchy**: Pairs `etica-display` for display copy (`Confirmation`) with `lft-etica` and `Halcyon Monument Grotesk Semi-Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `991px` container bounds (`gap: var(--boostsd-product-list-gap-list-view-desktop)`, padding `var(--boostsd-breadcrumb-padding)`) with `cubic-bezier(0,0,.58,1)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-halcyon-co-nz` in your global stylesheet:

:root {
  /* Halcyon · Leading Lighting Specialists (www-halcyon-co-nz) — Ground-Truth Extracted CSS Variables */
  --height-full: 100vh; /* Layout / Spatial Grid Token (www-halcyon-co-nz) */
  --height-fill: calc(100vh - var(--nav-height)); /* Layout / Spatial Grid Token (www-halcyon-co-nz) */
  --font-orion: "Untitled", sans-serif; /* Typography / Scale Token (www-halcyon-co-nz) */
  --annoucement-height: 37px; /* Layout / Spatial Grid Token (www-halcyon-co-nz) */
  --nav-main-height: 44px; /* Layout / Spatial Grid Token (www-halcyon-co-nz) */
  --nav-height: calc(var(--nav-main-height)); /* Layout / Spatial Grid Token (www-halcyon-co-nz) */
  --halcyon-toast-success: #32e26e; /* Color / Atmospheric Token (www-halcyon-co-nz) */
  --halcyon-toast-error: #e75619; /* Color / Atmospheric Token (www-halcyon-co-nz) */
  --halcyon-toast-info: #3b82f6; /* Color / Atmospheric Token (www-halcyon-co-nz) */
  --halcyon-toast-warning: #f59e0b; /* Color / Atmospheric Token (www-halcyon-co-nz) */
  --halcyon-toast-text: #000; /* Typography Ink Token (www-halcyon-co-nz) */
  --halcyon-toast-max-width: 500px; /* Layout / Spatial Grid Token (www-halcyon-co-nz) */
  --halcyon-toast-sweep-duration: 5s; /* Motion / Easing Token (www-halcyon-co-nz) */
  --boostsd-general-page-width-desktop: 1216px; /* Layout / Spatial Grid Token (www-halcyon-co-nz) */
  --boostsd-general-color-primary: #222; /* Brand / Palette Token (www-halcyon-co-nz) */
  --boostsd-general-font-size-base: 16px; /* Typography / Scale Token (www-halcyon-co-nz) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#32e26e` — grounded in `var(--halcyon-toast-success)` in `:root`
- **Primary Typography Ink**: `#e75619` — grounded in `var(--halcyon-toast-error)` in `:root`
- **Elevated Surface / Card Substrate**: `#3b82f6` — grounded in `var(--halcyon-toast-info)` in `:root`
- **Interactive Accent / Highlight**: `#f59e0b` — grounded in `var(--halcyon-toast-warning)` in `:root`
- **Secondary / Muted Copy**: `#000` — grounded in `var(--halcyon-toast-text)` in `:root`
- **Structural Hairline Border**: `#222` — grounded in `var(--boostsd-general-color-primary)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×6175px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `991px` extracted from `www-halcyon-co-nz` stylesheet
- **Padding & Gutters**: `var(--boostsd-breadcrumb-padding)` lateral canvas padding with `var(--boostsd-product-list-gap-list-view-desktop)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 991px`, `gap: var(--boostsd-product-list-gap-list-view-desktop)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--boostsd-breadcrumb-padding)` horizontal padding
- **Media Queries**: `@media screen and (forced-colors:active)`, `@media screen and (width<=750px)`, `@media only screen and (max-width:991px)`, `@media only screen and (min-width:992px)`
- **Corner Radii**: `4px`, `8px`, `50%`, `var(--boostsd-bundle-style-image-border-radius)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `etica-display`
- **Body Font Stack**: `lft-etica`
- **Monospace / Technical Font Stack**: `Halcyon Monument Grotesk Semi-Mono`
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `30px`, `40px`, `var(--boostsd-filter-search-optio...`, `20px`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `30px`, `40px`, `var(--boostsd-filter-search-optio...`, `20px`)
- **Body Copy Rule**: CSS variables `--boostsd-general-font-size-base: 16px`, `--boostsd-cart-body-padding: 16px`, `--boostsd-cart-body-padding-medium: 24px`; rule `p` (`font-size: 13px`, `line-height: 17px`, `letter-spacing: 0`, `font-weight: 500`)
- **Metadata & Index Rule**: CSS variables `--boostsd-product-label-padding: 2px 6px`, `--boostsd-product-label-border-radius: 2px`, `--boostsd-product-label-border-radius-capsule: 40px`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-halcyon-co-nz` (`Halcyon · Leading Lighting Specialists`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.js> — `www-halcyon-co-nz`)**:
   - DOM & Selectors: Landmark `<header class="js">` hosting `Halcyon · Leading Lighting Specialis` navigation (`Return · Products · About · Highlights · Stockists`), DOM attributes (`data-collection-view="grid"`, `data-source-attribution="shopify.exit_intersti..."`, `data-source-attribution="shopify.loadfeatures"`, `data-source-attribution="shopify.dynamic_check..."`), and stylesheet rule `.shopify-payment-button__button--... { visibility:hidden }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.js> — `www-halcyon-co-nz`)` (`www-halcyon-co-nz`) adapts across `@media screen and (forced-colors:active)`, `@media screen and (width<=750px)`, `@media only screen and (max-width:991px)`, `@media only screen and (min-width:992px)` with `cubic-bezier(0,0,.58,1)`, `cubic-bezier(.23,1,.32,1)` transitions and links `Return · Products · About · Highlights · Stockists`.
2. **Hero Stage & Focal Lead (<section.main-hero> — `Confirmation`)**:
   - DOM & Selectors: Landmark `<section class="main-hero hero-main-section">` presenting display lead `Confirmation` and copy excerpt *"No wishlists found"* over `#32e26e` canvas and `#000` ink.
   - Responsive Contract: Hero stage (`1440×6175px` desktop / `390×2400px` mobile) sets `#32e26e` background with `#000` headline `Confirmation`.
3. **Primary Showcase & Content Grid (<section.featured-product> — `Dark Art Slim Trim`)**:
   - DOM & Selectors: Landmark `<section class="featured-product">` rendering section `Dark Art Slim Trim` with copy *"SAVE ITEM TO FAVOURITES LIST"*, asset references (`inventoryLocation.js`, `clarity.js`, `wwzwszat2d`, `gtm.js`), and grid rule `opify-payment-button__button--unb... { background-color:1990c6;padding:1em 2em }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.featured-product> — `Dark Art Slim Trim`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 991px`, `gap: var(--boostsd-product-list-gap-list-view-desktop)`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--boostsd-breadcrumb-padding)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.tabbed-collection> — `Trade Flex Pro`)**:
   - DOM & Selectors: Landmark `<section class="tabbed-collection">` framing `Trade Flex Pro` and `Mini Mariner` (*"Remove from this list"*) with `#3b82f6` surface cards, `#f59e0b` accents, and `ptions.shopify-payment-button__sk... { width:50%;margin-left:25%;margin-right:25%;border-radius:4px!important;h... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.tabbed-collection> — `Trade Flex Pro`)` uses `4px`, `8px`, `50%`, `var(--boostsd-bundle-style-image-border-radius)` radii, `#f59e0b` highlights, and assets (inventoryLocation.js, clarity.js, wwzwszat2d).
5. **Colophon & Global Directory Footer (<footer.js-ajax-cart-empty> — `https://www.halcyon.co.nz/`)**:
   - DOM & Selectors: Landmark `<footer class="js-ajax-cart-empty">` anchoring `Halcyon · Leading Lighting Speci` footer links (`Return · Products · About · Highlights · Stockists`), copy *"Create a personalised list to organise your favourite items"*, and `#222` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.js-ajax-cart-empty> — `https://www.halcyon.co.nz/`)` aligns to `991px` extracted from `www-halcyon-co-nz` stylesheet with `var(--boostsd-breadcrumb-padding)` lateral canvas padding with `var(--boostsd-product-list-gap-list-view-desktop)` grid gap and attributes (data-collection-view="grid", data-source-attribution="shopify.exit_intersti...", data-source-attribution="shopify.loadfeatures").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"No wishlists found"*
- Copy Excerpt 2: *"SAVE ITEM TO FAVOURITES LIST"*
- Copy Excerpt 3: *"Remove from this list"*
- Copy Excerpt 4: *"Create a personalised list to organise your favourite items"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0,0,.58,1)`, `cubic-bezier(.23,1,.32,1)`
- **Extracted Stylesheet Rules (`www-halcyon-co-nz`)**:
- `.shopify-payment-button__button--... { visibility:hidden }`
- `opify-payment-button__button--unb... { background-color:1990c6;padding:1em 2em }`
- `ptions.shopify-payment-button__sk... { width:50%;margin-left:25%;margin-right:25%;border-radius:4px!important;h... }`
- `shopify-payment-button__button--b... { z-index:1;flex-direction:column;display:flex;position:relative }`
- `on__button--branded .shopify-clea... { flex-direction:column!important;flex:1!important;display:flex!important }`
- **Per-Selector Transition Rules**:
- **Selector `.shopify-payment-button__button`**: `transition: background .2s ease-in-out` extracted from `www-halcyon-co-nz` stylesheet.
- **Selector `.boost-sd__filter-option-title:be...`**: `transition: none` extracted from `www-halcyon-co-nz` stylesheet.
- **Selector `d__button--show-text-on-hover:foc...`**: `transition: width .4s ease` extracted from `www-halcyon-co-nz` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.58,1)`)**: Governs interactive state transitions across `<header.js>` and `<section.featured-product>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-halcyon-co-nz`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
