---
title: "UI Prompt Blueprint: www-feelreformed-com"
date: 2026-11-15
target: "[[overview|www-feelreformed-com]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#FAFBFF`)"
---

# UI Design System & Master Generation Blueprint: www-feelreformed-com

> **Reformed: The biggest thing to happen to Coffee since Coffee.** (https://www.feelreformed.com/) — Reformed: Arabica coffee and ceremonial matcha, enriched with functionality: collagen or creatine, adaptogens and twenty-one vitamins.

![Desktop Viewport Capture (1440x4311)](file:///root/projects/fleet/wiki/targets/www-feelreformed-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Reformed: The biggest thing to happen to Coffee since Coffee.** (`https://www.feelreformed.com/`). Reformed: Arabica coffee and ceremonial matcha, enriched with functionality: collagen or creatine, adaptogens and twenty-one vitamins.
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#FAFBFF`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`var(--color-foreground)` in `:root`) paired with `#005BD1` primary typography and `#FAFBFF` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Chivo` for display copy (`Country/Region`) with `Hanken Grotesk` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `749px` container bounds (`gap: var(--gap-md)`, padding `var(--page-margin)`) with `cubic-bezier(.4,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/www-feelreformed-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×4311px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `749px` extracted from `www-feelreformed-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--page-margin)` lateral canvas padding with `var(--gap-md)` grid gap.
- **Border Radius Scale**: `var(--style-border-radius-inputs)`, `var(--style-border-radius-popover)`, `var(--style-border-radius-buttons-primary)`, `var(--style-border-radius-buttons-secondary)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 749px`, `gap: var(--gap-md)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--page-margin)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (any-pointer:fine)and (prefers-reduced-motion:no-preference)`, `@media (prefers-reduced-motion:no-preference)`, `@media screen and (min-width:750px)`, `@media screen and (max-width:749px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--color-foreground)` in `:root` |
| **Primary Typography Ink** | `#005BD1` | `var(--swn0j0)` in `:root` |
| **Elevated Surface / Card Substrate** | `#FFFFFF` | `var(--swn0j1)` in `:root` |
| **Interactive Accent / Highlight** | `#FAFBFF` | `var(--swn0j3)` in `:root` |
| **Secondary / Muted Copy** | `#F5F6FF` | `var(--swn0j4)` in `:root` |
| **Structural Hairline Border** | `#EBEDFF` | `var(--swn0j5)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--hover-lift-amount` | `4px` | Dimension / Scale Token |
| `--hover-scale-amount` | `1` | Design System Custom Token |
| `--hover-subtle-zoom-amount` | `1.015` | Design System Custom Token |
| `--hover-shadow-color` | `var(--color-shadow)` | Brand / Palette Token |
| `--hover-transition-duration` | `.25s` | Motion / Easing Token |
| `--hover-transition-timing` | `ease-out` | Motion / Easing Token |
| `--cursor` | `pointer` | Design System Custom Token |
| `--backdrop-color-rgb` | `var(--color-shadow-rgb)` | Brand / Palette Token |
| `--page-margin` | `16px` | Layout / Spatial Grid Token |
| `--page-content-width` | `var(--wide-page-width)` | Layout / Spatial Grid Token |
| `--page-width` | `calc(var(--page-content-width) + (var(--page-margin) * 2))` | Layout / Spatial Grid Token |
| `--full-page-grid-margin` | `minmax(var(--page-margin), 1fr)` | Layout / Spatial Grid Token |
| `--section-min-height` | `var(--section-height-small)` | Layout / Spatial Grid Token |
| `--centered-column-number` | `12` | Layout / Spatial Grid Token |
| `--full-width-column-number` | `14` | Layout / Spatial Grid Token |
| `--centered` | `column-1 / span var(--centered-column-number)` | Design System Custom Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Chivo`.
- **Primary Body Stack**: `Hanken Grotesk`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--header-logo-display: none`, `--header-logo-inverse-display: block`, `--x-shell-disclosure-display: block`; rule `h1` (`line-height: var(--line-height--di...`).
- **Section Heading (`H2`)**: CSS variables `--font-h2--spacing: 0.25em`, `--font-h2--color: var(--color-foreground-heading)`, `--font-size--h2: clamp(1.75rem, 4.8vw, 3.0rem)`; rule `h2` (`font-size: 24px!important`).
- **Body Copy**: CSS variables `--font-paragraph--line-height: 1`, `--font-body--family: Inter, sans-serif`, `--font-body--style: normal`; rule `p` (`line-height: var(--line-height--bo...`).
- **Metadata & Navigation Labels**: CSS variables `--checkbox-label-padding: 8px`, `--image-height-small: calc(var(--image-height-basis) * 2)`, `--facets-input-label-color: rgb(var(--color-input-text-rgb) / var(--opacity-60))`; rule `small` (`font-size: 80%`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.3,.5,.5,1)`, `cubic-bezier(.3,0,0,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `:root`**: `transition: .25s` extracted from `www-feelreformed-com` stylesheet.
- **Selector `.predictive-search-results__card`**: `transition: transform var(--hover-transition-duration) var(--hover-transit...` extracted from `www-feelreformed-com` stylesheet.
- **Selector `dictive-search-results__card .res...`**: `transition: none` extracted from `www-feelreformed-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.shopify-section>` and `<section.shopify-section>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Reformed: The biggest thing to happen to C │
│ ====================================================================== │
│ [ <header.shopify-section> | Black Coffee · Mocha · Matcha · Shop A ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.shopify-section>                            |   │
│ | H1: Country/Region                                               |   │
│ | Substrate: #fff       | Ink: #005BD1    | Accent: #FAFBFF        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.shopify-section> ) max-w: 749px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | All Natural, Reformed Coffee |  | Discover Our Products        | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<header.shopify-se] -> [<section.shopify-s] -> [<section.shopify-s] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.shopify-sectio) | https://www.feelreformed.com/      │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.shopify-section> — `www-feelreformed-com`)**:
   - Landmark `<header class="shopify-section shopify-section-group-header-group">` hosting `Reformed: The biggest thing to happe` navigation (`Black Coffee · Mocha · Matcha · Shop All · Mocha with Collagen`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-shopify`, `data-shop-id="81515184414"`, `data-venmo-supported="false"`), and stylesheet rule `svg { display:block;max-width:100% }`.
2. **Hero Stage & Focal Lead (<section.shopify-section> — `Country/Region`)**:
   - Landmark `<section class="shopify-section section-wrapper">` presenting display lead `Country/Region` and copy excerpt *"Get Extra 10% off with the code REFORMED10 at Checkout"* over `#fff` canvas and `#005BD1` ink.
3. **Primary Showcase & Content Grid (<section.shopify-section> — `All Natural, Reformed Coffee & Mat`)**:
   - Landmark `<section class="shopify-section hero-wrapper">` rendering section `All Natural, Reformed Coffee & Matcha` with copy *"Cart Total items in cart: 0 0"*, asset references (`storefront.js`, `page-load`, `shopify.js`, `klaviyo.js`), and grid rule `img { width:100%;height:auto }`.
4. **Interactive Detail & Feature Matrix (<section.shopify-section> — `Discover Our Products`)**:
   - Landmark `<section class="shopify-section hero-wrapper">` framing `Discover Our Products` and `Frequently Purchased With` (*"Total items in cart: 0 0"*) with `#FFFFFF` surface cards, `#FAFBFF` accents, and `select { font:inherit;border-radius:var(--style-border-radius-inputs) }`.
5. **Colophon & Global Directory Footer (<footer.shopify-section> — `https://www.feelreformed.com/`)**:
   - Landmark `<footer class="shopify-section shopify-section-group-footer-group">` anchoring `Reformed: The biggest thing to h` footer links (`Black Coffee · Mocha · Matcha · Shop All · Mocha with Collagen`), copy *"Total items in cart: 0"*, and `#EBEDFF` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-feelreformed-com (Reformed: The biggest thing to happen to Coffee since Coffee.)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-feelreformed-com` (**Reformed: The biggest thing to happen to Coffee since Coffee.** — `https://www.feelreformed.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#FAFBFF`).
- **Identity & Domain Context**: Reformed: Arabica coffee and ceremonial matcha, enriched with functionality: collagen or creatine, adaptogens and twenty-one vitamins.
- **Primary Substrate**: `#fff` (`var(--color-foreground)` in `:root`), **Primary Ink**: `#005BD1`, **Accent / Highlight**: `#FAFBFF`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`var(--color-foreground)` in `:root`) paired with `#005BD1` primary typography and `#FAFBFF` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Chivo` for display copy (`Country/Region`) with `Hanken Grotesk` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `749px` container bounds (`gap: var(--gap-md)`, padding `var(--page-margin)`) with `cubic-bezier(.4,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-feelreformed-com` in your global stylesheet:

:root {
  /* Reformed: The biggest thing to happen to Coffee since Coffee. (www-feelreformed-com) — Ground-Truth Extracted CSS Variables */
  --hover-lift-amount: 4px; /* Dimension / Scale Token (www-feelreformed-com) */
  --hover-scale-amount: 1; /* Design System Custom Token (www-feelreformed-com) */
  --hover-subtle-zoom-amount: 1.015; /* Design System Custom Token (www-feelreformed-com) */
  --hover-shadow-color: var(--color-shadow); /* Brand / Palette Token (www-feelreformed-com) */
  --hover-transition-duration: .25s; /* Motion / Easing Token (www-feelreformed-com) */
  --hover-transition-timing: ease-out; /* Motion / Easing Token (www-feelreformed-com) */
  --cursor: pointer; /* Design System Custom Token (www-feelreformed-com) */
  --backdrop-color-rgb: var(--color-shadow-rgb); /* Brand / Palette Token (www-feelreformed-com) */
  --page-margin: 16px; /* Layout / Spatial Grid Token (www-feelreformed-com) */
  --page-content-width: var(--wide-page-width); /* Layout / Spatial Grid Token (www-feelreformed-com) */
  --page-width: calc(var(--page-content-width) + (var(--page-margin) * 2)); /* Layout / Spatial Grid Token (www-feelreformed-com) */
  --full-page-grid-margin: minmax(var(--page-margin), 1fr); /* Layout / Spatial Grid Token (www-feelreformed-com) */
  --section-min-height: var(--section-height-small); /* Layout / Spatial Grid Token (www-feelreformed-com) */
  --centered-column-number: 12; /* Layout / Spatial Grid Token (www-feelreformed-com) */
  --full-width-column-number: 14; /* Layout / Spatial Grid Token (www-feelreformed-com) */
  --centered: column-1 / span var(--centered-column-number); /* Design System Custom Token (www-feelreformed-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fff` — grounded in `var(--color-foreground)` in `:root`
- **Primary Typography Ink**: `#005BD1` — grounded in `var(--swn0j0)` in `:root`
- **Elevated Surface / Card Substrate**: `#FFFFFF` — grounded in `var(--swn0j1)` in `:root`
- **Interactive Accent / Highlight**: `#FAFBFF` — grounded in `var(--swn0j3)` in `:root`
- **Secondary / Muted Copy**: `#F5F6FF` — grounded in `var(--swn0j4)` in `:root`
- **Structural Hairline Border**: `#EBEDFF` — grounded in `var(--swn0j5)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×4311px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `749px` extracted from `www-feelreformed-com` stylesheet
- **Padding & Gutters**: `var(--page-margin)` lateral canvas padding with `var(--gap-md)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 749px`, `gap: var(--gap-md)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--page-margin)` horizontal padding
- **Media Queries**: `@media (any-pointer:fine)and (prefers-reduced-motion:no-preference)`, `@media (prefers-reduced-motion:no-preference)`, `@media screen and (min-width:750px)`, `@media screen and (max-width:749px)`
- **Corner Radii**: `var(--style-border-radius-inputs)`, `var(--style-border-radius-popover)`, `var(--style-border-radius-buttons-primary)`, `var(--style-border-radius-buttons-secondary)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Chivo`
- **Body Font Stack**: `Hanken Grotesk`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--header-logo-display: none`, `--header-logo-inverse-display: block`, `--x-shell-disclosure-display: block`; rule `h1` (`line-height: var(--line-height--di...`)
- **H2 Section Rule**: CSS variables `--font-h2--spacing: 0.25em`, `--font-h2--color: var(--color-foreground-heading)`, `--font-size--h2: clamp(1.75rem, 4.8vw, 3.0rem)`; rule `h2` (`font-size: 24px!important`)
- **Body Copy Rule**: CSS variables `--font-paragraph--line-height: 1`, `--font-body--family: Inter, sans-serif`, `--font-body--style: normal`; rule `p` (`line-height: var(--line-height--bo...`)
- **Metadata & Index Rule**: CSS variables `--checkbox-label-padding: 8px`, `--image-height-small: calc(var(--image-height-basis) * 2)`, `--facets-input-label-color: rgb(var(--color-input-text-rgb) / var(--opacity-60))`; rule `small` (`font-size: 80%`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-feelreformed-com` (`Reformed: The biggest thing to happen to Coffee since Coffee.`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.shopify-section> — `www-feelreformed-com`)**:
   - DOM & Selectors: Landmark `<header class="shopify-section shopify-section-group-header-group">` hosting `Reformed: The biggest thing to happe` navigation (`Black Coffee · Mocha · Matcha · Shop All · Mocha with Collagen`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-shopify`, `data-shop-id="81515184414"`, `data-venmo-supported="false"`), and stylesheet rule `svg { display:block;max-width:100% }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.shopify-section> — `www-feelreformed-com`)` (`www-feelreformed-com`) adapts across `@media (any-pointer:fine)and (prefers-reduced-motion:no-preference)`, `@media (prefers-reduced-motion:no-preference)`, `@media screen and (min-width:750px)`, `@media screen and (max-width:749px)` with `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.3,.5,.5,1)`, `cubic-bezier(.3,0,0,1)` transitions and links `Black Coffee · Mocha · Matcha · Shop All · Mocha with Collagen`.
2. **Hero Stage & Focal Lead (<section.shopify-section> — `Country/Region`)**:
   - DOM & Selectors: Landmark `<section class="shopify-section section-wrapper">` presenting display lead `Country/Region` and copy excerpt *"Get Extra 10% off with the code REFORMED10 at Checkout"* over `#fff` canvas and `#005BD1` ink.
   - Responsive Contract: Hero stage (`1440×4311px` desktop / `390×2400px` mobile) sets `#fff` background with `#005BD1` headline `Country/Region`.
3. **Primary Showcase & Content Grid (<section.shopify-section> — `All Natural, Reformed Coffee & Mat`)**:
   - DOM & Selectors: Landmark `<section class="shopify-section hero-wrapper">` rendering section `All Natural, Reformed Coffee & Matcha` with copy *"Cart Total items in cart: 0 0"*, asset references (`storefront.js`, `page-load`, `shopify.js`, `klaviyo.js`), and grid rule `img { width:100%;height:auto }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.shopify-section> — `All Natural, Reformed Coffee & Mat`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 749px`, `gap: var(--gap-md)`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--page-margin)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.shopify-section> — `Discover Our Products`)**:
   - DOM & Selectors: Landmark `<section class="shopify-section hero-wrapper">` framing `Discover Our Products` and `Frequently Purchased With` (*"Total items in cart: 0 0"*) with `#FFFFFF` surface cards, `#FAFBFF` accents, and `select { font:inherit;border-radius:var(--style-border-radius-inputs) }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.shopify-section> — `Discover Our Products`)` uses `var(--style-border-radius-inputs)`, `var(--style-border-radius-popover)`, `var(--style-border-radius-buttons-primary)`, `var(--style-border-radius-buttons-secondary)` radii, `#FAFBFF` highlights, and assets (storefront.js, page-load, shopify.js).
5. **Colophon & Global Directory Footer (<footer.shopify-section> — `https://www.feelreformed.com/`)**:
   - DOM & Selectors: Landmark `<footer class="shopify-section shopify-section-group-footer-group">` anchoring `Reformed: The biggest thing to h` footer links (`Black Coffee · Mocha · Matcha · Shop All · Mocha with Collagen`), copy *"Total items in cart: 0"*, and `#EBEDFF` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.shopify-section> — `https://www.feelreformed.com/`)` aligns to `749px` extracted from `www-feelreformed-com` stylesheet with `var(--page-margin)` lateral canvas padding with `var(--gap-md)` grid gap and attributes (data-source-attribution="shopify.exit_intersti...", data-shopify, data-shop-id="81515184414").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Get Extra 10% off with the code REFORMED10 at Checkout"*
- Copy Excerpt 2: *"Cart Total items in cart: 0 0"*
- Copy Excerpt 3: *"Total items in cart: 0 0"*
- Copy Excerpt 4: *"Total items in cart: 0"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.3,.5,.5,1)`, `cubic-bezier(.3,0,0,1)`
- **Extracted Stylesheet Rules (`www-feelreformed-com`)**:
- `svg { display:block;max-width:100% }`
- `img { width:100%;height:auto }`
- `select { font:inherit;border-radius:var(--style-border-radius-inputs) }`
- `input:hover { background-color:var(--color-input-hover-background) }`
- `.product-card__link { position:absolute;top:0;right:0;bottom:0;left:0 }`
- **Per-Selector Transition Rules**:
- **Selector `:root`**: `transition: .25s` extracted from `www-feelreformed-com` stylesheet.
- **Selector `.predictive-search-results__card`**: `transition: transform var(--hover-transition-duration) var(--hover-transit...` extracted from `www-feelreformed-com` stylesheet.
- **Selector `dictive-search-results__card .res...`**: `transition: none` extracted from `www-feelreformed-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.shopify-section>` and `<section.shopify-section>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-feelreformed-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
