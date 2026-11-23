---
title: "UI Prompt Blueprint: www-feelreformed-com"
date: 2026-11-23
captured_at: 2026-11-23
target: "www-feelreformed-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#f9f8f6` canvas, `#000000` ink, `#ff0000` accent)"
---

# UI Design System & Master Generation Blueprint: www-feelreformed-com

> **Reformed: The biggest thing to happen to Coffee since Coffee.** (https://www.feelreformed.com/) — Reformed: Arabica coffee and ceremonial matcha, enriched with functionality: collagen or creatine, adaptogens and twenty-one vitamins.

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Reformed: The biggest thing to happen to Coffee since Coffee.** (`https://www.feelreformed.com/`). Reformed: Arabica coffee and ceremonial matcha, enriched with functionality: collagen or creatine, adaptogens and twenty-one vitamins.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#f9f8f6` canvas, `#000000` ink, `#ff0000` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f9f8f6` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#ff0000` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Optima` for display copy (`Black Coffee with Collagen`) with `Inter` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1920px` container bounds (`gap: var(--gap-md)`, padding `var(--page-margin)`) with `cubic-bezier(.4,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1920px` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `var(--page-margin)` lateral canvas padding with `var(--gap-md)` grid gap.
- **Border Radius Scale**: `var(--style-border-radius-inputs)`, `var(--style-border-radius-popover)`, `var(--style-border-radius-buttons-primary)`, `var(--style-border-radius-buttons-secondary)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1920px`, `gap: var(--gap-md)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--page-margin)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (any-pointer:fine)and (prefers-reduced-motion:no-preference)`, `@media (prefers-reduced-motion:no-preference)`, `@media screen and (min-width:750px)`, `@media screen and (max-width:749px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f9f8f6` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `a` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#e5e5eb` | `var(--oke-avatar-backgroundColor)` in `:root` |
| **Interactive Accent / Highlight** | `#ff0000` | `.octane-popup__optin-channel-error { color: red }` (`#ff0000`) |
| **Secondary / Muted Copy** | `#7b6f65` | `var(--oke-stars-foregroundColor)` in `:root` |
| **Structural Hairline Border** | `#b3b3b1` | `var(--color-border)` in `:root` (`rgb(0 0 0 / 0.28)`) |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--hover-lift-amount` | `4px` | Dimension / Scale Token |
| `--hover-scale-amount` | `1` | Design System Custom Token |
| `--hover-subtle-zoom-amount` | `1.015` | Design System Custom Token |
| `--hover-shadow-color` | `var(--color-shadow)` | Brand / Palette Token |
| `--hover-transition-duration` | `.25s` | Motion / Easing Token |
| `--hover-transition-timing` | `ease-out` | Motion / Easing Token |
| `--sidebar-width` | `25rem` | Layout / Spatial Grid Token |
| `--narrow-content-width` | `36rem` | Layout / Spatial Grid Token |
| `--normal-content-width` | `42rem` | Layout / Spatial Grid Token |
| `--wide-content-width` | `46rem` | Layout / Spatial Grid Token |
| `--narrow-page-width` | `90rem` | Layout / Spatial Grid Token |
| `--normal-page-width` | `120rem` | Layout / Spatial Grid Token |
| `--wide-page-width` | `150rem` | Layout / Spatial Grid Token |
| `--section-height-small` | `15rem` | Layout / Spatial Grid Token |
| `--section-height-medium` | `25rem` | Layout / Spatial Grid Token |
| `--section-height-large` | `35rem` | Layout / Spatial Grid Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Optima`.
- **Primary Body Stack**: `Inter`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 24px`, `line-height: 27.6px`, `font-weight: 400`); CSS variables `--header-logo-display: none`, `--header-logo-inverse-display: block`, `--font-h1--spacing: 0.25em`; rule `h1` (`line-height: var(--line-height--di...`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 48px`, `line-height: 52.8px`, `font-weight: 400`); CSS variables `--font-h2--spacing: 0.25em`, `--font-size--h2: clamp(1.75rem, 4.8vw, 3.0rem)`, `--font-h2--weight: var(--font-heading--weight)`; rule `h2` (`font-size: 24px`).
- **Body Copy**: live computed `body` (`font-size: 14px`, `line-height: 22.4px`, `font-weight: 400`); CSS variables `--font-paragraph--line-height: 1`, `--font-body--family: Inter, sans-serif`, `--font-body--style: normal`; rule `p` (`line-height: var(--line-height--bo...`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 14px`, `line-height: 22.4px`, `font-weight: 400`); CSS variables `--section-height-small: 15rem`, `--oke-text-small: 14px`, `--checkbox-label-padding: 8px`; rule `small` (`font-size: 80%`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(0.33,1,0.68,1)`, `cubic-bezier(0.32,0.72,0,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `:root`**: `transition: .25s` extracted from `www-feelreformed-com` stylesheet.
- **Selector `.predictive-search-results__card`**: `transition: transform var(--hover-transition-duration) var(--hover-transit...` extracted from `www-feelreformed-com` stylesheet.
- **Selector `dictive-search-results__card .res...`**: `transition: none` extracted from `www-feelreformed-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.shopify-section>` and `<section.hero-wrapper>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Reformed: The biggest thing to happen to C │
│ ====================================================================== │
│ [ <header.shopify-sectio (1440x0px)   | Black Coffee · Mocha · Match ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.shopify-section> (w=1440px)                   | │
│ | H1: Black Coffee with Collagen                                     | │
│ | Substrate: #f9f8f6 | Ink: #000000 | Accent: #ff0000                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.hero-wrapper>) max-w: 1920px               | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Matcha with Collagen         |  | Mocha with Collagen          | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.section-wrapper>) — FAQ                    | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.shopify-sect) | https://www.feelreformed.com/        │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--ga)   │
│ ====================================================================== │
│ [ HEADER BAR (<header.shopify-section>) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.shopify-section) — 390px Vertical Lead        | │
│ | H1: Black Coffee with Collagen                                     | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.hero-wrapper>) — 1-Col Stack              | │
│ | [ Item 1: Matcha with Collagen                                   ] | │
│ | [ Item 2: Mocha with Collagen                                    ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.section-wrapper) — 1-Col (FAQ)              | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.shopify-sect) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.shopify-section> — `www-feelreformed-com`)**:
   - Landmark `<header class="shopify-section shopify-section-group-header-group">` (`1440x0px`) hosting `Reformed: The biggest thing to happe` navigation (`Black Coffee · Mocha · Matcha · Shop All · Mocha with Collagen`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-shopify`, `data-shop-id="81515184414"`, `data-venmo-supported="false"`), and stylesheet rule `svg { display:block;max-width:100% }`.
2. **Hero Stage & Focal Lead (<section.shopify-section> — `Black Coffee with Collagen`)**:
   - Landmark `<section class="shopify-section section-wrapper">` presenting display lead `Black Coffee with Collagen` and copy excerpt *"Our lowest prices of the year."* over `#f9f8f6` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.hero-wrapper> — `Matcha with Collagen`)**:
   - Landmark `<section class="shopify-section hero-wrapper">` rendering section `Matcha with Collagen` with copy *"Experience the next era of Coffee & Matcha"*, asset references (`storefront.js`, `page-load`, `shopify.js`, `klaviyo.js`), and grid rule `img { width:100%;height:auto }`.
4. **Interactive Detail & Feature Matrix (<section.section-wrapper> — `Mocha with Collagen`)**:
   - Landmark `<section class="shopify-section hero-wrapper">` framing `Mocha with Collagen` and `FAQ` (*"Made in the United Kingdom"*) with `#e5e5eb` surface cards, `#ff0000` accents, and `select { font:inherit;border-radius:var(--style-border-radius-inputs) }`.
5. **Colophon & Global Directory Footer (<footer.shopify-section> — `https://www.feelreformed.com/`)**:
   - Landmark `<footer class="shopify-section shopify-section-group-footer-group">` anchoring `Reformed: The biggest thing to h` footer links (`Black Coffee · Mocha · Matcha · Shop All · Mocha with Collagen`), copy *"Reformed blends the finest coffee beans or ceremonial-grade "*, and `#b3b3b1` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-feelreformed-com (Reformed: The biggest thing to happen to Coffee since Coffee.)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-feelreformed-com` (**Reformed: The biggest thing to happen to Coffee since Coffee.** — `https://www.feelreformed.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#f9f8f6` canvas, `#000000` ink, `#ff0000` accent).
- **Identity & Domain Context**: Reformed: Arabica coffee and ceremonial matcha, enriched with functionality: collagen or creatine, adaptogens and twenty-one vitamins.
- **Primary Substrate**: `#f9f8f6` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#000000`, **Accent / Highlight**: `#ff0000`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f9f8f6` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#ff0000` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Optima` for display copy (`Black Coffee with Collagen`) with `Inter` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1920px` container bounds (`gap: var(--gap-md)`, padding `var(--page-margin)`) with `cubic-bezier(.4,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-feelreformed-com` in your global stylesheet:

:root {
  /* Reformed: The biggest thing to happen to Coffee since Coffee. (www-feelreformed-com) — Live-Grounded CSS Variables */
  --hover-lift-amount: 4px; /* Dimension / Scale Token (www-feelreformed-com) */
  --hover-scale-amount: 1; /* Design System Custom Token (www-feelreformed-com) */
  --hover-subtle-zoom-amount: 1.015; /* Design System Custom Token (www-feelreformed-com) */
  --hover-shadow-color: var(--color-shadow); /* Brand / Palette Token (www-feelreformed-com) */
  --hover-transition-duration: .25s; /* Motion / Easing Token (www-feelreformed-com) */
  --hover-transition-timing: ease-out; /* Motion / Easing Token (www-feelreformed-com) */
  --sidebar-width: 25rem; /* Layout / Spatial Grid Token (www-feelreformed-com) */
  --narrow-content-width: 36rem; /* Layout / Spatial Grid Token (www-feelreformed-com) */
  --normal-content-width: 42rem; /* Layout / Spatial Grid Token (www-feelreformed-com) */
  --wide-content-width: 46rem; /* Layout / Spatial Grid Token (www-feelreformed-com) */
  --narrow-page-width: 90rem; /* Layout / Spatial Grid Token (www-feelreformed-com) */
  --normal-page-width: 120rem; /* Layout / Spatial Grid Token (www-feelreformed-com) */
  --wide-page-width: 150rem; /* Layout / Spatial Grid Token (www-feelreformed-com) */
  --section-height-small: 15rem; /* Layout / Spatial Grid Token (www-feelreformed-com) */
  --section-height-medium: 25rem; /* Layout / Spatial Grid Token (www-feelreformed-com) */
  --section-height-large: 35rem; /* Layout / Spatial Grid Token (www-feelreformed-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f9f8f6` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#000000` — grounded in live computed `a` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#e5e5eb` — grounded in `var(--oke-avatar-backgroundColor)` in `:root`
- **Interactive Accent / Highlight**: `#ff0000` — grounded in `.octane-popup__optin-channel-error { color: red }` (`#ff0000`)
- **Secondary / Muted Copy**: `#7b6f65` — grounded in `var(--oke-stars-foregroundColor)` in `:root`
- **Structural Hairline Border**: `#b3b3b1` — grounded in `var(--color-border)` in `:root` (`rgb(0 0 0 / 0.28)`)

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1920px` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `var(--page-margin)` lateral canvas padding with `var(--gap-md)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1920px`, `gap: var(--gap-md)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--page-margin)` horizontal padding
- **Media Queries**: `@media (any-pointer:fine)and (prefers-reduced-motion:no-preference)`, `@media (prefers-reduced-motion:no-preference)`, `@media screen and (min-width:750px)`, `@media screen and (max-width:749px)`
- **Corner Radii**: `var(--style-border-radius-inputs)`, `var(--style-border-radius-popover)`, `var(--style-border-radius-buttons-primary)`, `var(--style-border-radius-buttons-secondary)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Optima`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 24px`, `line-height: 27.6px`, `font-weight: 400`); CSS variables `--header-logo-display: none`, `--header-logo-inverse-display: block`, `--font-h1--spacing: 0.25em`; rule `h1` (`line-height: var(--line-height--di...`)
- **H2 Section Rule**: live computed `h2` (`font-size: 48px`, `line-height: 52.8px`, `font-weight: 400`); CSS variables `--font-h2--spacing: 0.25em`, `--font-size--h2: clamp(1.75rem, 4.8vw, 3.0rem)`, `--font-h2--weight: var(--font-heading--weight)`; rule `h2` (`font-size: 24px`)
- **Body Copy Rule**: live computed `body` (`font-size: 14px`, `line-height: 22.4px`, `font-weight: 400`); CSS variables `--font-paragraph--line-height: 1`, `--font-body--family: Inter, sans-serif`, `--font-body--style: normal`; rule `p` (`line-height: var(--line-height--bo...`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 14px`, `line-height: 22.4px`, `font-weight: 400`); CSS variables `--section-height-small: 15rem`, `--oke-text-small: 14px`, `--checkbox-label-padding: 8px`; rule `small` (`font-size: 80%`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-feelreformed-com` (`Reformed: The biggest thing to happen to Coffee since Coffee.`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.shopify-section> — `www-feelreformed-com`)**:
   - DOM & Selectors: Landmark `<header class="shopify-section shopify-section-group-header-group">` (`1440x0px`) hosting `Reformed: The biggest thing to happe` navigation (`Black Coffee · Mocha · Matcha · Shop All · Mocha with Collagen`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-shopify`, `data-shop-id="81515184414"`, `data-venmo-supported="false"`), and stylesheet rule `svg { display:block;max-width:100% }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.shopify-section> — `www-feelreformed-com`)` (`www-feelreformed-com`) adapts across `@media (any-pointer:fine)and (prefers-reduced-motion:no-preference)`, `@media (prefers-reduced-motion:no-preference)`, `@media screen and (min-width:750px)`, `@media screen and (max-width:749px)` with `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(0.33,1,0.68,1)`, `cubic-bezier(0.32,0.72,0,1)` transitions and links `Black Coffee · Mocha · Matcha · Shop All · Mocha with Collagen`.
2. **Hero Stage & Focal Lead (<section.shopify-section> — `Black Coffee with Collagen`)**:
   - DOM & Selectors: Landmark `<section class="shopify-section section-wrapper">` presenting display lead `Black Coffee with Collagen` and copy excerpt *"Our lowest prices of the year."* over `#f9f8f6` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#f9f8f6` background with `#000000` headline `Black Coffee with Collagen`.
3. **Primary Showcase & Content Grid (<section.hero-wrapper> — `Matcha with Collagen`)**:
   - DOM & Selectors: Landmark `<section class="shopify-section hero-wrapper">` rendering section `Matcha with Collagen` with copy *"Experience the next era of Coffee & Matcha"*, asset references (`storefront.js`, `page-load`, `shopify.js`, `klaviyo.js`), and grid rule `img { width:100%;height:auto }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.hero-wrapper> — `Matcha with Collagen`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1920px`, `gap: var(--gap-md)`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--page-margin)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.section-wrapper> — `Mocha with Collagen`)**:
   - DOM & Selectors: Landmark `<section class="shopify-section hero-wrapper">` framing `Mocha with Collagen` and `FAQ` (*"Made in the United Kingdom"*) with `#e5e5eb` surface cards, `#ff0000` accents, and `select { font:inherit;border-radius:var(--style-border-radius-inputs) }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.section-wrapper> — `Mocha with Collagen`)` uses `var(--style-border-radius-inputs)`, `var(--style-border-radius-popover)`, `var(--style-border-radius-buttons-primary)`, `var(--style-border-radius-buttons-secondary)` radii, `#ff0000` highlights, and assets (storefront.js, page-load, shopify.js).
5. **Colophon & Global Directory Footer (<footer.shopify-section> — `https://www.feelreformed.com/`)**:
   - DOM & Selectors: Landmark `<footer class="shopify-section shopify-section-group-footer-group">` anchoring `Reformed: The biggest thing to h` footer links (`Black Coffee · Mocha · Matcha · Shop All · Mocha with Collagen`), copy *"Reformed blends the finest coffee beans or ceremonial-grade "*, and `#b3b3b1` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.shopify-section> — `https://www.feelreformed.com/`)` aligns to `1920px` (non-`@media` desktop container stylesheet rule) with `var(--page-margin)` lateral canvas padding with `var(--gap-md)` grid gap and attributes (data-source-attribution="shopify.exit_intersti...", data-shopify, data-shop-id="81515184414").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Our lowest prices of the year."*
- Copy Excerpt 2: *"Experience the next era of Coffee & Matcha"*
- Copy Excerpt 3: *"Made in the United Kingdom"*
- Copy Excerpt 4: *"Reformed blends the finest coffee beans or ceremonial-grade matcha with collagen p..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(0.33,1,0.68,1)`, `cubic-bezier(0.32,0.72,0,1)`
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
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.shopify-section>` and `<section.hero-wrapper>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-feelreformed-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
