---
title: "UI Prompt Blueprint: www-killstar-com"
date: 2026-11-15
target: "[[overview|www-killstar-com]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#e9e9eb` canvas, `#1d1e20` ink, `#518b22` accent)"
---

# UI Design System & Master Generation Blueprint: www-killstar-com

> **KILLSTAR** (https://www.killstar.com/) — Clothing & Lifestyle company with a twist of darkness, channeling emotional power and raw energy into every thread.

![Desktop Viewport Capture (1440x4583)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **KILLSTAR** (`https://www.killstar.com/`). Clothing & Lifestyle company with a twist of darkness, channeling emotional power and raw energy into every thread.
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#e9e9eb` canvas, `#1d1e20` ink, `#518b22` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#e9e9eb` (`var(--kl-reviews-color-light-gray)` in `:root`) paired with `#1d1e20` primary typography and `#518b22` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Inter` for display copy (`HOW WE USE YOUR DATA`) with `PPPlayground` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `440px` container bounds (`gap: 4px`, padding `.75rem`) with `cubic-bezier(0.5,0,0.5,1)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×4583px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `440px` extracted from `www-killstar-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `.75rem` lateral canvas padding with `4px` grid gap.
- **Border Radius Scale**: `50%`, `5px`, `25px`, `6px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 440px`, `gap: 4px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `.75rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width:440px)`, `@media (max-width:1024px)`, `@media (max-width:768px)`, `@media (min-width:1220px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#e9e9eb` | `var(--kl-reviews-color-light-gray)` in `:root` |
| **Primary Typography Ink** | `#faf9f8` | `var(--atlas-background-main)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ffffff` | `var(--atlas-background-content)` in `:root` |
| **Interactive Accent / Highlight** | `#518b22` | `var(--atlas-background-success)` in `:root` |
| **Secondary / Muted Copy** | `#be2119` | `var(--atlas-background-error)` in `:root` |
| **Structural Hairline Border** | `#1d1e20` | `var(--atlas-text-primary)` in `:root` |
| **Variable Token (`--atlas-text-secondary`)** | `#4b4d4e` | `var(--atlas-text-secondary)` in `:root` |
| **Variable Token (`--atlas-text-positive`)** | `#366d12` | `var(--atlas-text-positive)` in `:root` |
| **Variable Token (`--atlas-text-placeholder`)** | `#747576` | `var(--atlas-text-placeholder)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--kl-reviews-color-light-gray` | `#e9e9eb` | Canvas / Surface Token |
| `--kl-local-border-radius` | `var(--atlas-button-border-radius-normal)` | Elevation / Border Token |
| `--kl-local-button-color` | `var(--atlas-text-primary-inverse)` | Brand / Palette Token |
| `--kl-local-button-background` | `var(--atlas-button-primary)` | Canvas / Surface Token |
| `--kl-local-icon-size` | `var(--atlas-icon-size-medium)` | Layout / Spatial Grid Token |
| `--kl-local-border-color` | `var(--atlas-button-primary)` | Brand / Palette Token |
| `--atlas-background-main` | `#faf9f8` | Canvas / Surface Token |
| `--atlas-background-content` | `#ffffff` | Canvas / Surface Token |
| `--atlas-background-success` | `#518b22` | Canvas / Surface Token |
| `--atlas-background-error` | `#be2119` | Canvas / Surface Token |
| `--atlas-text-primary` | `#1d1e20` | Typography Ink Token |
| `--atlas-text-secondary` | `#4b4d4e` | Typography Ink Token |
| `--atlas-text-negative` | `#be2119` | Typography Ink Token |
| `--atlas-text-positive` | `#366d12` | Typography Ink Token |
| `--atlas-text-placeholder` | `#747576` | Typography Ink Token |
| `--atlas-text-primary-inverse` | `#ffffff` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Inter`.
- **Primary Body Stack**: `PPPlayground`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--atlas-font-size-display: 40px`, `--atlas-line-height-display: 52px`, `--atlas-margin-display: 24px`; rule `.title` (`font-size: 13px`).
- **Section Heading (`H2`)**: CSS variables `--atlas-font-size-h2: 32px`, `--atlas-line-height-h2: 40px`, `--atlas-margin-h2: 24px`; rule `h2` (`font-size: 2.5em`, `font-weight: 900`).
- **Body Copy**: rule `p` (`line-height: 1.6`).
- **Metadata & Navigation Labels**: CSS variables `--atlas-font-size-small: 14px`, `--atlas-line-height-small: 20px`, `--atlas-margin-small: 8px`; rule `.label` (`font-size: .875em`, `letter-spacing: 2.8px`, `font-weight: 500`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.5,0,0.5,1)`, `cubic-bezier(0.4,0,0.2,1)`, `cubic-bezier(0.34,1.15,0.64,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.swiper-pagination`**: `transition: opacity .3s` extracted from `www-killstar-com` stylesheet.
- **Selector `n-bullets-dynamic .swiper-paginat...`**: `transition: transform .2s,top .2s` extracted from `www-killstar-com` stylesheet.
- **Selector `n-bullets-dynamic .swiper-paginat...`**: `transition: transform .2s,left .2s` extracted from `www-killstar-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.5,0,0.5,1)`)**: Governs interactive state transitions across `<header.shopify-section>` and `<section.shopify-section>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — KILLSTAR                                   │
│ ====================================================================== │
│ [ <header.shopify-section> | NEW IN · DRESSES · WOMENS · PLUS · MEN ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.shopify-pc__banner__dialog>                 |   │
│ | H1: HOW WE USE YOUR DATA                                         |   │
│ | Substrate: #e9e9eb    | Ink: #1d1e20    | Accent: #518b22        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.shopify-section> ) max-w: 440px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Winter's Vale Coat           |  | Skultra Cropped Cardigan     | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 4px   ) | │
│ | [<header.shopify-se] -> [<section.shopify-p] -> [<section.shopify-s] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.shopify-sectio) | https://www.killstar.com/          │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.shopify-section> — `www-killstar-com`)**:
   - Landmark `<header class="shopify-section shopify-section-group-header-group">` hosting `KILLSTAR` navigation (`NEW IN · DRESSES · WOMENS · PLUS · MENS`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-shop-id="53907226789"`, `data-venmo-supported="false"`, `data-environment="production"`), and stylesheet rule `root { --swiper-navigation-size:44px }`.
2. **Hero Stage & Focal Lead (<section.shopify-pc__banner__dialog> — `HOW WE USE YOUR DATA`)**:
   - Landmark `<section class="shopify-pc__banner__dialog">` presenting display lead `HOW WE USE YOUR DATA` and copy excerpt *"We use cookies & other technologies to provide a personalised exp"* over `#e9e9eb` canvas and `#1d1e20` ink.
3. **Primary Showcase & Content Grid (<section.shopify-section> — `Winter's Vale Coat`)**:
   - Landmark `<section class="shopify-section shopify-section-group-header-group">` rendering section `Winter's Vale Coat` with copy *"Manage preferences"*, asset references (`reamaze-push.js`, `tp.min.js`, `37086_1783060609.js`, `init.js`), and grid rule `iper-button-next.swiper-button-di... { opacity:.35;cursor:auto;pointer-events:none }`.
4. **Interactive Detail & Feature Matrix (<section.shopify-section> — `Skultra Cropped Cardigan`)**:
   - Landmark `<section class="shopify-section shopify-section-group-header-group">` framing `Skultra Cropped Cardigan` and `Basilica Cape` (*"Black Friday 13th Sale - Shop Now Black Friday 13th Sale - Shop N"*) with `#ffffff` surface cards, `#518b22` accents, and `swiper-button-next.swiper-button-... { opacity:0;cursor:auto;pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.shopify-section> — `https://www.killstar.com/`)**:
   - Landmark `<footer class="shopify-section shopify-section-group-footer-group">` anchoring `KILLSTAR` footer links (`NEW IN · DRESSES · WOMENS · PLUS · MENS`), copy *"Black Friday 13th Sale - Shop Now"*, and `#1d1e20` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-killstar-com (KILLSTAR)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-killstar-com` (**KILLSTAR** — `https://www.killstar.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#e9e9eb` canvas, `#1d1e20` ink, `#518b22` accent).
- **Identity & Domain Context**: Clothing & Lifestyle company with a twist of darkness, channeling emotional power and raw energy into every thread.
- **Primary Substrate**: `#e9e9eb` (`var(--kl-reviews-color-light-gray)` in `:root`), **Primary Ink**: `#1d1e20`, **Accent / Highlight**: `#518b22`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#e9e9eb` (`var(--kl-reviews-color-light-gray)` in `:root`) paired with `#1d1e20` primary typography and `#518b22` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Inter` for display copy (`HOW WE USE YOUR DATA`) with `PPPlayground` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `440px` container bounds (`gap: 4px`, padding `.75rem`) with `cubic-bezier(0.5,0,0.5,1)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-killstar-com` in your global stylesheet:

:root {
  /* KILLSTAR (www-killstar-com) — Ground-Truth Extracted CSS Variables */
  --kl-reviews-color-light-gray: #e9e9eb; /* Canvas / Surface Token (www-killstar-com) */
  --kl-local-border-radius: var(--atlas-button-border-radius-normal); /* Elevation / Border Token (www-killstar-com) */
  --kl-local-button-color: var(--atlas-text-primary-inverse); /* Brand / Palette Token (www-killstar-com) */
  --kl-local-button-background: var(--atlas-button-primary); /* Canvas / Surface Token (www-killstar-com) */
  --kl-local-icon-size: var(--atlas-icon-size-medium); /* Layout / Spatial Grid Token (www-killstar-com) */
  --kl-local-border-color: var(--atlas-button-primary); /* Brand / Palette Token (www-killstar-com) */
  --atlas-background-main: #faf9f8; /* Canvas / Surface Token (www-killstar-com) */
  --atlas-background-content: #ffffff; /* Canvas / Surface Token (www-killstar-com) */
  --atlas-background-success: #518b22; /* Canvas / Surface Token (www-killstar-com) */
  --atlas-background-error: #be2119; /* Canvas / Surface Token (www-killstar-com) */
  --atlas-text-primary: #1d1e20; /* Typography Ink Token (www-killstar-com) */
  --atlas-text-secondary: #4b4d4e; /* Typography Ink Token (www-killstar-com) */
  --atlas-text-negative: #be2119; /* Typography Ink Token (www-killstar-com) */
  --atlas-text-positive: #366d12; /* Typography Ink Token (www-killstar-com) */
  --atlas-text-placeholder: #747576; /* Typography Ink Token (www-killstar-com) */
  --atlas-text-primary-inverse: #ffffff; /* Typography Ink Token (www-killstar-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#e9e9eb` — grounded in `var(--kl-reviews-color-light-gray)` in `:root`
- **Primary Typography Ink**: `#faf9f8` — grounded in `var(--atlas-background-main)` in `:root`
- **Elevated Surface / Card Substrate**: `#ffffff` — grounded in `var(--atlas-background-content)` in `:root`
- **Interactive Accent / Highlight**: `#518b22` — grounded in `var(--atlas-background-success)` in `:root`
- **Secondary / Muted Copy**: `#be2119` — grounded in `var(--atlas-background-error)` in `:root`
- **Structural Hairline Border**: `#1d1e20` — grounded in `var(--atlas-text-primary)` in `:root`
- **Variable Token (`--atlas-text-secondary`)**: `#4b4d4e` — grounded in `var(--atlas-text-secondary)` in `:root`
- **Variable Token (`--atlas-text-positive`)**: `#366d12` — grounded in `var(--atlas-text-positive)` in `:root`
- **Variable Token (`--atlas-text-placeholder`)**: `#747576` — grounded in `var(--atlas-text-placeholder)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×4583px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `440px` extracted from `www-killstar-com` stylesheet
- **Padding & Gutters**: `.75rem` lateral canvas padding with `4px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 440px`, `gap: 4px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `.75rem` horizontal padding
- **Media Queries**: `@media screen and (max-width:440px)`, `@media (max-width:1024px)`, `@media (max-width:768px)`, `@media (min-width:1220px)`
- **Corner Radii**: `50%`, `5px`, `25px`, `6px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `PPPlayground`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--atlas-font-size-display: 40px`, `--atlas-line-height-display: 52px`, `--atlas-margin-display: 24px`; rule `.title` (`font-size: 13px`)
- **H2 Section Rule**: CSS variables `--atlas-font-size-h2: 32px`, `--atlas-line-height-h2: 40px`, `--atlas-margin-h2: 24px`; rule `h2` (`font-size: 2.5em`, `font-weight: 900`)
- **Body Copy Rule**: rule `p` (`line-height: 1.6`)
- **Metadata & Index Rule**: CSS variables `--atlas-font-size-small: 14px`, `--atlas-line-height-small: 20px`, `--atlas-margin-small: 8px`; rule `.label` (`font-size: .875em`, `letter-spacing: 2.8px`, `font-weight: 500`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-killstar-com` (`KILLSTAR`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.shopify-section> — `www-killstar-com`)**:
   - DOM & Selectors: Landmark `<header class="shopify-section shopify-section-group-header-group">` hosting `KILLSTAR` navigation (`NEW IN · DRESSES · WOMENS · PLUS · MENS`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-shop-id="53907226789"`, `data-venmo-supported="false"`, `data-environment="production"`), and stylesheet rule `root { --swiper-navigation-size:44px }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.shopify-section> — `www-killstar-com`)` (`www-killstar-com`) adapts across `@media screen and (max-width:440px)`, `@media (max-width:1024px)`, `@media (max-width:768px)`, `@media (min-width:1220px)` with `cubic-bezier(0.5,0,0.5,1)`, `cubic-bezier(0.4,0,0.2,1)`, `cubic-bezier(0.34,1.15,0.64,1)` transitions and links `NEW IN · DRESSES · WOMENS · PLUS · MENS`.
2. **Hero Stage & Focal Lead (<section.shopify-pc__banner__dialog> — `HOW WE USE YOUR DATA`)**:
   - DOM & Selectors: Landmark `<section class="shopify-pc__banner__dialog">` presenting display lead `HOW WE USE YOUR DATA` and copy excerpt *"We use cookies & other technologies to provide a personalised exp"* over `#e9e9eb` canvas and `#1d1e20` ink.
   - Responsive Contract: Hero stage (`1440×4583px` desktop / `390×2400px` mobile) sets `#e9e9eb` background with `#1d1e20` headline `HOW WE USE YOUR DATA`.
3. **Primary Showcase & Content Grid (<section.shopify-section> — `Winter's Vale Coat`)**:
   - DOM & Selectors: Landmark `<section class="shopify-section shopify-section-group-header-group">` rendering section `Winter's Vale Coat` with copy *"Manage preferences"*, asset references (`reamaze-push.js`, `tp.min.js`, `37086_1783060609.js`, `init.js`), and grid rule `iper-button-next.swiper-button-di... { opacity:.35;cursor:auto;pointer-events:none }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.shopify-section> — `Winter's Vale Coat`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 440px`, `gap: 4px`) on desktop and Single-column vertical stack at `390px` viewport width with `.75rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.shopify-section> — `Skultra Cropped Cardigan`)**:
   - DOM & Selectors: Landmark `<section class="shopify-section shopify-section-group-header-group">` framing `Skultra Cropped Cardigan` and `Basilica Cape` (*"Black Friday 13th Sale - Shop Now Black Friday 13th Sale - Shop N"*) with `#ffffff` surface cards, `#518b22` accents, and `swiper-button-next.swiper-button-... { opacity:0;cursor:auto;pointer-events:none }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.shopify-section> — `Skultra Cropped Cardigan`)` uses `50%`, `5px`, `25px`, `6px` radii, `#518b22` highlights, and assets (reamaze-push.js, tp.min.js, 37086_1783060609.js).
5. **Colophon & Global Directory Footer (<footer.shopify-section> — `https://www.killstar.com/`)**:
   - DOM & Selectors: Landmark `<footer class="shopify-section shopify-section-group-footer-group">` anchoring `KILLSTAR` footer links (`NEW IN · DRESSES · WOMENS · PLUS · MENS`), copy *"Black Friday 13th Sale - Shop Now"*, and `#1d1e20` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.shopify-section> — `https://www.killstar.com/`)` aligns to `440px` extracted from `www-killstar-com` stylesheet with `.75rem` lateral canvas padding with `4px` grid gap and attributes (data-source-attribution="shopify.exit_intersti...", data-shop-id="53907226789", data-venmo-supported="false").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"We use cookies & other technologies to provide a personalised experience on our we..."*
- Copy Excerpt 2: *"Manage preferences"*
- Copy Excerpt 3: *"Black Friday 13th Sale - Shop Now Black Friday 13th Sale - Shop Now"*
- Copy Excerpt 4: *"Black Friday 13th Sale - Shop Now"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.5,0,0.5,1)`, `cubic-bezier(0.4,0,0.2,1)`, `cubic-bezier(0.34,1.15,0.64,1)`
- **Extracted Stylesheet Rules (`www-killstar-com`)**:
- `root { --swiper-navigation-size:44px }`
- `iper-button-next.swiper-button-di... { opacity:.35;cursor:auto;pointer-events:none }`
- `swiper-button-next.swiper-button-... { opacity:0;cursor:auto;pointer-events:none }`
- `navigation-disabled .swiper-butto... { display:none!important }`
- `.swiper-button-next svg { object-fit:contain;transform-origin:50%;width:100%;height:100% }`
- **Per-Selector Transition Rules**:
- **Selector `.swiper-pagination`**: `transition: opacity .3s` extracted from `www-killstar-com` stylesheet.
- **Selector `n-bullets-dynamic .swiper-paginat...`**: `transition: transform .2s,top .2s` extracted from `www-killstar-com` stylesheet.
- **Selector `n-bullets-dynamic .swiper-paginat...`**: `transition: transform .2s,left .2s` extracted from `www-killstar-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.5,0,0.5,1)`)**: Governs interactive state transitions across `<header.shopify-section>` and `<section.shopify-section>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-killstar-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
