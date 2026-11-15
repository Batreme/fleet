---
title: "UI Prompt Blueprint: delice-ca"
date: 2026-11-15
target: "[[overview|delice-ca]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#f5dbca` / `#f8efdc`)"
---

# UI Design System & Master Generation Blueprint: delice-ca

> **Accueil - Délice** (https://delice.ca/) — Pizza Délice depuis 1970 Au cœur de Lévis, alliant chaleur, grandeur et convivialité dans une ambiance vibrante et accueillante.

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/delice-ca/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Accueil - Délice** (`https://delice.ca/`). Pizza Délice depuis 1970 Au cœur de Lévis, alliant chaleur, grandeur et convivialité dans une ambiance vibrante et accueillante.
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#f5dbca` / `#f8efdc`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#f5dbca` (`var(--primary-300)` in `:root`) paired with `#273e2a` primary typography and `#f8efdc` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Filson Soft` for display copy (`Pizza Délice depuis 1970 Au cœur de `) with `Ivy Mode` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `767px` container bounds (`gap: 32px`, padding `3px`) with `cubic-bezier(.4,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/delice-ca/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `767px` extracted from `delice-ca` stylesheet.
- **Canvas Lateral Padding & Spacing**: `3px` lateral canvas padding with `32px` grid gap.
- **Border Radius Scale**: `50%`, `2px`, `4px`, `8px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 767px`, `gap: 32px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `3px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:480px)`, `@media (min-width:768px)`, `@media (max-width:767px)`, `@media (min-width:1024px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f5dbca` | `var(--primary-300)` in `:root` |
| **Primary Typography Ink** | `#de2b2b` | `var(--on-primary-300)` in `:root` |
| **Elevated Surface / Card Substrate** | `#7c2627` | `var(--on-primary-300-alt)` in `:root` |
| **Interactive Accent / Highlight** | `#f8efdc` | `var(--on-primary-500)` in `:root` |
| **Secondary / Muted Copy** | `#91964f` | `var(--secondary-500)` in `:root` |
| **Structural Hairline Border** | `#273e2a` | `var(--secondary-700)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--header-banner-height` | `2.75rem` | Layout / Spatial Grid Token |
| `--header-inner-height` | `clamp(64px, 47.0986px + 4.50704vw, 7rem)` | Layout / Spatial Grid Token |
| `--header-height` | `calc(var(--header-banner-height) + var(--header-inner-height))` | Layout / Spatial Grid Token |
| `--menu-banner-height` | `2.5rem` | Layout / Spatial Grid Token |
| `--menu-nav-height` | `6rem` | Layout / Spatial Grid Token |
| `--promotion-media-size` | `min(34rem, 55vh)` | Layout / Spatial Grid Token |
| `--section-spacing-top-default` | `clamp(64px, 41.4648px + 6.00939vw, 8rem)` | Layout / Spatial Grid Token |
| `--section-spacing-bottom-default` | `clamp(64px, 41.4648px + 6.00939vw, 8rem)` | Layout / Spatial Grid Token |
| `--section-spacing-top-compact` | `clamp(64px, 64px + 0vw, 4rem)` | Layout / Spatial Grid Token |
| `--section-spacing-bottom-compact` | `clamp(64px, 64px + 0vw, 4rem)` | Layout / Spatial Grid Token |
| `--container-spacing-md` | `clamp(32px, 20.7324px + 3.0047vw, 4rem)` | Layout / Spatial Grid Token |
| `--primary-300` | `#f5dbca` | Brand / Palette Token |
| `--primary-300-rgb` | `245, 219, 202` | Brand / Palette Token |
| `--on-primary-300` | `#de2b2b` | Brand / Palette Token |
| `--on-primary-300-rgb` | `222, 43, 43` | Brand / Palette Token |
| `--on-primary-300-alt` | `#7c2627` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Filson Soft`.
- **Primary Body Stack**: `Ivy Mode`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `9px`, `13px`, `15px`, `18px`, `21px`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `9px`, `13px`, `15px`, `18px`, `21px`).
- **Body Copy**: rule `p` (`font-size: max(14px,min(14px,.875rem))`, `line-height: 1.4`, `letter-spacing: 0`, `font-weight: 400`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `9px`, `13px`, `15px`, `18px`, `21px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.23,1,.32,1)`, `cubic-bezier(.215,.61,.355,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.plyr`**: `transition: box-shadow .3s` extracted from `delice-ca` stylesheet.
- **Selector `.plyr__captions`**: `transition: transform .4s ease-in-out` extracted from `delice-ca` stylesheet.
- **Selector `.plyr__control`**: `transition: all .1s ease-in-out` extracted from `delice-ca` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.c-header>` and `<section.o-section>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Accueil - Délice                           │
│ ====================================================================== │
│ [ <header.c-header>        | Les menus · Le restaurant              ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.c-hero>                                     |   │
│ | H1: Pizza Délice depuis 1970 Au cœur de Lévis, allian...         |   │
│ | Substrate: #f5dbca    | Ink: #273e2a    | Accent: #f8efdc        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.o-section>       ) max-w: 767px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Un choix pour tous les goûts |  | Plaisirs du jour             | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 32px  ) | │
│ | [<header.c-header>] -> [<section.c-hero>] -> [<section.o-section] |  │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.c-footer>     ) | https://delice.ca/                 │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.c-header> — `delice-ca`)**:
   - Landmark `<header class="c-header">` hosting `Accueil - Délice` navigation (`Les menus · Le restaurant`), DOM attributes (`data-module-swup="m1"`, `data-module-scroll="m2"`, `data-module-effects="m3"`, `data-module-dev-utils="m4"`), and stylesheet rule `.flickity-enabled { position:relative }`.
2. **Hero Stage & Focal Lead (<section.c-hero> — `Pizza Délice depuis 1970 Au cœur d`)**:
   - Landmark `<section class="c-hero">` presenting display lead `Pizza Délice depuis 1970 Au cœur de Lévis, allian...` and copy excerpt *"Tous les jours de 14 h à 18 h."* over `#f5dbca` canvas and `#273e2a` ink.
3. **Primary Showcase & Content Grid (<section.o-section> — `Un choix pour tous les goûts`)**:
   - Landmark `<section class="o-section u-relative">` rendering section `Un choix pour tous les goûts` with copy *"Tous les jours de 11 h à 15 h."*, asset references (`recaptcha__en.js`, `script.js`, `www.googletagmanager.com`, `mainCss.css`), and grid rule `.flickity-viewport { touch-action:pan-y;height:100%;position:relative;overflow:hidden }`.
4. **Interactive Detail & Feature Matrix (<section.o-section> — `Plaisirs du jour`)**:
   - Landmark `<section class="o-section">` framing `Plaisirs du jour` and `Happy Hour` (*"Tous les mardis de 11 h à 22 h."*) with `#7c2627` surface cards, `#f8efdc` accents, and `.flickity-slider { width:100%;height:100%;position:absolute;left:0 }`.
5. **Colophon & Global Directory Footer (<footer.c-footer> — `https://delice.ca/`)**:
   - Landmark `<footer class="c-footer">` anchoring `Accueil - Délice` footer links (`Les menus · Le restaurant`), copy *"20 % de rabais en livraison et pour emporter."*, and `#273e2a` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: delice-ca (Accueil - Délice)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `delice-ca` (**Accueil - Délice** — `https://delice.ca/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f5dbca` / `#f8efdc`).
- **Identity & Domain Context**: Pizza Délice depuis 1970 Au cœur de Lévis, alliant chaleur, grandeur et convivialité dans une ambiance vibrante et accueillante.
- **Primary Substrate**: `#f5dbca` (`var(--primary-300)` in `:root`), **Primary Ink**: `#273e2a`, **Accent / Highlight**: `#f8efdc`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#f5dbca` (`var(--primary-300)` in `:root`) paired with `#273e2a` primary typography and `#f8efdc` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Filson Soft` for display copy (`Pizza Délice depuis 1970 Au cœur de `) with `Ivy Mode` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `767px` container bounds (`gap: 32px`, padding `3px`) with `cubic-bezier(.4,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `delice-ca` in your global stylesheet:

:root {
  /* Accueil - Délice (delice-ca) — Ground-Truth Extracted CSS Variables */
  --header-banner-height: 2.75rem; /* Layout / Spatial Grid Token (delice-ca) */
  --header-inner-height: clamp(64px, 47.0986px + 4.50704vw, 7rem); /* Layout / Spatial Grid Token (delice-ca) */
  --header-height: calc(var(--header-banner-height) + var(--header-inner-height)); /* Layout / Spatial Grid Token (delice-ca) */
  --menu-banner-height: 2.5rem; /* Layout / Spatial Grid Token (delice-ca) */
  --menu-nav-height: 6rem; /* Layout / Spatial Grid Token (delice-ca) */
  --promotion-media-size: min(34rem, 55vh); /* Layout / Spatial Grid Token (delice-ca) */
  --section-spacing-top-default: clamp(64px, 41.4648px + 6.00939vw, 8rem); /* Layout / Spatial Grid Token (delice-ca) */
  --section-spacing-bottom-default: clamp(64px, 41.4648px + 6.00939vw, 8rem); /* Layout / Spatial Grid Token (delice-ca) */
  --section-spacing-top-compact: clamp(64px, 64px + 0vw, 4rem); /* Layout / Spatial Grid Token (delice-ca) */
  --section-spacing-bottom-compact: clamp(64px, 64px + 0vw, 4rem); /* Layout / Spatial Grid Token (delice-ca) */
  --container-spacing-md: clamp(32px, 20.7324px + 3.0047vw, 4rem); /* Layout / Spatial Grid Token (delice-ca) */
  --primary-300: #f5dbca; /* Brand / Palette Token (delice-ca) */
  --primary-300-rgb: 245, 219, 202; /* Brand / Palette Token (delice-ca) */
  --on-primary-300: #de2b2b; /* Brand / Palette Token (delice-ca) */
  --on-primary-300-rgb: 222, 43, 43; /* Brand / Palette Token (delice-ca) */
  --on-primary-300-alt: #7c2627; /* Brand / Palette Token (delice-ca) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f5dbca` — grounded in `var(--primary-300)` in `:root`
- **Primary Typography Ink**: `#de2b2b` — grounded in `var(--on-primary-300)` in `:root`
- **Elevated Surface / Card Substrate**: `#7c2627` — grounded in `var(--on-primary-300-alt)` in `:root`
- **Interactive Accent / Highlight**: `#f8efdc` — grounded in `var(--on-primary-500)` in `:root`
- **Secondary / Muted Copy**: `#91964f` — grounded in `var(--secondary-500)` in `:root`
- **Structural Hairline Border**: `#273e2a` — grounded in `var(--secondary-700)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `767px` extracted from `delice-ca` stylesheet
- **Padding & Gutters**: `3px` lateral canvas padding with `32px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 767px`, `gap: 32px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `3px` horizontal padding
- **Media Queries**: `@media (min-width:480px)`, `@media (min-width:768px)`, `@media (max-width:767px)`, `@media (min-width:1024px)`
- **Corner Radii**: `50%`, `2px`, `4px`, `8px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Filson Soft`
- **Body Font Stack**: `Ivy Mode`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `9px`, `13px`, `15px`, `18px`, `21px`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `9px`, `13px`, `15px`, `18px`, `21px`)
- **Body Copy Rule**: rule `p` (`font-size: max(14px,min(14px,.875rem))`, `line-height: 1.4`, `letter-spacing: 0`, `font-weight: 400`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `9px`, `13px`, `15px`, `18px`, `21px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `delice-ca` (`Accueil - Délice`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.c-header> — `delice-ca`)**:
   - DOM & Selectors: Landmark `<header class="c-header">` hosting `Accueil - Délice` navigation (`Les menus · Le restaurant`), DOM attributes (`data-module-swup="m1"`, `data-module-scroll="m2"`, `data-module-effects="m3"`, `data-module-dev-utils="m4"`), and stylesheet rule `.flickity-enabled { position:relative }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.c-header> — `delice-ca`)` (`delice-ca`) adapts across `@media (min-width:480px)`, `@media (min-width:768px)`, `@media (max-width:767px)`, `@media (min-width:1024px)` with `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.23,1,.32,1)`, `cubic-bezier(.215,.61,.355,1)` transitions and links `Les menus · Le restaurant`.
2. **Hero Stage & Focal Lead (<section.c-hero> — `Pizza Délice depuis 1970 Au cœur d`)**:
   - DOM & Selectors: Landmark `<section class="c-hero">` presenting display lead `Pizza Délice depuis 1970 Au cœur de Lévis, allian...` and copy excerpt *"Tous les jours de 14 h à 18 h."* over `#f5dbca` canvas and `#273e2a` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#f5dbca` background with `#273e2a` headline `Pizza Délice depuis 1970 Au cœur de Lévis, allian...`.
3. **Primary Showcase & Content Grid (<section.o-section> — `Un choix pour tous les goûts`)**:
   - DOM & Selectors: Landmark `<section class="o-section u-relative">` rendering section `Un choix pour tous les goûts` with copy *"Tous les jours de 11 h à 15 h."*, asset references (`recaptcha__en.js`, `script.js`, `www.googletagmanager.com`, `mainCss.css`), and grid rule `.flickity-viewport { touch-action:pan-y;height:100%;position:relative;overflow:hidden }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.o-section> — `Un choix pour tous les goûts`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 767px`, `gap: 32px`) on desktop and Single-column vertical stack at `390px` viewport width with `3px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.o-section> — `Plaisirs du jour`)**:
   - DOM & Selectors: Landmark `<section class="o-section">` framing `Plaisirs du jour` and `Happy Hour` (*"Tous les mardis de 11 h à 22 h."*) with `#7c2627` surface cards, `#f8efdc` accents, and `.flickity-slider { width:100%;height:100%;position:absolute;left:0 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.o-section> — `Plaisirs du jour`)` uses `50%`, `2px`, `4px`, `8px` radii, `#f8efdc` highlights, and assets (recaptcha__en.js, script.js, www.googletagmanager.com).
5. **Colophon & Global Directory Footer (<footer.c-footer> — `https://delice.ca/`)**:
   - DOM & Selectors: Landmark `<footer class="c-footer">` anchoring `Accueil - Délice` footer links (`Les menus · Le restaurant`), copy *"20 % de rabais en livraison et pour emporter."*, and `#273e2a` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.c-footer> — `https://delice.ca/`)` aligns to `767px` extracted from `delice-ca` stylesheet with `3px` lateral canvas padding with `32px` grid gap and attributes (data-module-swup="m1", data-module-scroll="m2", data-module-effects="m3").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Tous les jours de 14 h à 18 h."*
- Copy Excerpt 2: *"Tous les jours de 11 h à 15 h."*
- Copy Excerpt 3: *"Tous les mardis de 11 h à 22 h."*
- Copy Excerpt 4: *"20 % de rabais en livraison et pour emporter."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.23,1,.32,1)`, `cubic-bezier(.215,.61,.355,1)`
- **Extracted Stylesheet Rules (`delice-ca`)**:
- `.flickity-enabled { position:relative }`
- `.flickity-viewport { touch-action:pan-y;height:100%;position:relative;overflow:hidden }`
- `.flickity-slider { width:100%;height:100%;position:absolute;left:0 }`
- `.flickity-rtl .flickity-slider { left:unset;right:0 }`
- `.flickity-enabled.is-draggable { -webkit-tap-highlight-color:transparent;-webkit-user-select:none;-ms-use... }`
- **Per-Selector Transition Rules**:
- **Selector `.plyr`**: `transition: box-shadow .3s` extracted from `delice-ca` stylesheet.
- **Selector `.plyr__captions`**: `transition: transform .4s ease-in-out` extracted from `delice-ca` stylesheet.
- **Selector `.plyr__control`**: `transition: all .1s ease-in-out` extracted from `delice-ca` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.c-header>` and `<section.o-section>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `delice-ca`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
