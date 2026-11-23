---
title: "UI Prompt Blueprint: almadalabel-com"
date: 2026-11-23
captured_at: 2026-11-23
target: "almadalabel-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#0000ee` accent)"
---

# UI Design System & Master Generation Blueprint: almadalabel-com

> **ALMADA LABEL - A modern take on a seasonless wardrobe** (https://almadalabel.com/) — Seasonless modern wardrobe staples designed with Scandinavian minimalism, resonating beyond trends. Responsibly crafted from high-quality...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **ALMADA LABEL - A modern take on a seasonless wardrobe** (`https://almadalabel.com/`). Seasonless modern wardrobe staples designed with Scandinavian minimalism, resonating beyond trends. Responsibly crafted from high-quality...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#0000ee` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `browser-default` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#0000ee` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Paragraph Primary Font` for display copy (`ALMADA`) with `Paragraph Primary Font` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 16px`, padding `32px`) with `cubic-bezier(0.25,0.1,0.25,1)` easing and Swiper Touch Carousel Engine, Barba.js Page Transition Router.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport).
- **Canvas Lateral Padding & Spacing**: `32px` lateral canvas padding with `16px` grid gap.
- **Border Radius Scale**: `50%`, `4px`, `5px`, `8px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 16px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `32px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (min-width:1025px)`, `@media (min-width:1025px)`, `@media screen and (max-width:1024px)`, `@media (prefers-reduced-motion:reduce)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `browser-default` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f3f2f2` | `var(--background_color_2)` in `:root` |
| **Interactive Accent / Highlight** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#88847c` | `var(--secondary_gray)` in `:root` |
| **Structural Hairline Border** | `#a6a6a5` | `var(--button-border)` in `:root` |
| **Variable Token (`--primary_text`)** | `#17140f` | `var(--primary_text)` in `:root` |
| **Variable Token (`--secondary_accent`)** | `#38302e` | `var(--secondary_accent)` in `:root` |
| **Variable Token (`--primary_gray`)** | `#55534e` | `var(--primary_gray)` in `:root` |
| **Variable Token (`--loader_color`)** | `#1e242a` | `var(--loader_color)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--background_color` | `#ffffff` | Canvas / Surface Token |
| `--background_color_2` | `#f3f2f2` | Canvas / Surface Token |
| `--primary_text` | `#17140f` | Typography Ink Token |
| `--secondary_text` | `#ffffff` | Typography Ink Token |
| `--primary_accent` | `#a6a6a5` | Brand / Palette Token |
| `--secondary_accent` | `#38302e` | Brand / Palette Token |
| `--primary_gray` | `#55534e` | Brand / Palette Token |
| `--secondary_gray` | `#88847c` | Brand / Palette Token |
| `--tertiary_gray` | `#f3f2f2` | Color / Atmospheric Token |
| `--button-bg` | `#a6a6a5` | Canvas / Surface Token |
| `--button-content` | `#ffffff` | Color / Atmospheric Token |
| `--button-border` | `#a6a6a5` | Elevation / Border Token |
| `--body_color` | `#FFF` | Brand / Palette Token |
| `--loader_color` | `#1e242a` | Brand / Palette Token |
| `--submenu-position` | `54px` | Dimension / Scale Token |
| `--header-height` | `54px` | Layout / Spatial Grid Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Paragraph Primary Font`.
- **Primary Body Stack**: `Paragraph Primary Font`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 14px`, `line-height: 18.2px`, `font-weight: 400`); rule `h1` (`font-size: 32px`, `line-height: normal`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 18px`, `line-height: 24px`, `font-weight: 400`); rule `h2` (`font-size: .875rem`, `line-height: 1.125rem`, `letter-spacing: 0`, `font-weight: 400`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 20.8px`, `font-weight: 400`); CSS variables `--type_primary_paragraph_font: 'Paragraph Primary Font'`, `--weight_paragraph_font: 400`; rule `p` (`font-size: .75rem`, `line-height: 1.125rem`, `letter-spacing: 0`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 14px`, `line-height: 18.2px`, `font-weight: 400`); CSS variables `--mobile-menu-label-gap: .375rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.product-card__media`**: `transition: opacity .15s ease-out` extracted from `almadalabel-com` stylesheet.
- **Selector `.product-card__image`**: `transition: opacity .35s ease` extracted from `almadalabel-com` stylesheet.
- **Selector `duct-card[data-slider] .product-c...`**: `transition: transform .35s ease` extracted from `almadalabel-com` stylesheet.
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in captured CSS).
- **Runtime Interaction Engine**: Integrates Swiper Touch Carousel Engine, Barba.js Page Transition Router, Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — ALMADA LABEL - A modern take on a seasonle │
│ ====================================================================== │
│ [ <header.Drawer__header (1440px)     | Journal · New Arrivals · Com ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <article.favorites-drawer__item> (w=1425px)            | │
│ | H1: ALMADA                                                         | │
│ | Substrate: #ffffff | Ink: #000000 | Accent: #0000ee                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<article.favorites-drawer_) max-w: 1440px           | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Silk, lustrous satin and del |  | Search                       | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<article.favorites-drawer_) — Search Wishlist Cart  | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>     ) | https://almadalabel.com/             │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.Drawer__header> ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<article.favorites-drawe) — 390px Vertical Lead        | │
│ | H1: ALMADA                                                         | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<article.favorites-dra) — 1-Col Stack              | │
│ | [ Item 1: Silk, lustrous satin and delicate sheer layers         ] | │
│ | [ Item 2: Search                                                 ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<article.favorites-drawe) — 1-Col (Search Wishlist Ca) │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>     ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.Drawer__header> — `almadalabel-com`)**:
   - Landmark `<header class="Drawer__header">` (`1440px`) hosting `ALMADA LABEL - A modern take on a se` navigation (`Journal · New Arrivals · Coming Soon · Gift Edit New · Occasion Edit New`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-shop-id="25465225306"`, `data-venmo-supported="false"`, `data-environment="production"`), and stylesheet rule `.form-checkbox__label { display:flex;flex-direction:row;align-items:center;gap:.5rem;width:100%;... }`.
2. **Hero Stage & Focal Lead (<article.favorites-drawer__item> — `ALMADA`)**:
   - Landmark `<article class="favorites-drawer__item">` presenting display lead `ALMADA` and copy excerpt *"Free shipping to Germany on orders over 300€"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<article.favorites-drawer__item:nth(2)> — `Silk, lustrous satin and delicate `)**:
   - Landmark `<article class="favorites-drawer__item">` rendering section `Silk, lustrous satin and delicate sheer layers` with copy *"Shop occasion edit"*, asset references (`script.js`, `weglot_script_tag.js`, `storefrontattributes`, `trsdk`), and grid rule `.form-checkbox__label-text p { display:inline }`.
4. **Interactive Detail & Feature Matrix (<article.favorites-drawer__item:nth(3)> — `Search`)**:
   - Landmark `<article class="favorites-drawer__item">` framing `Search` and `Search Wishlist Cart 0` (*"Search Wishlist Cart 0"*) with `#f3f2f2` surface cards, `#0000ee` accents, and `.form-checkbox { width:100% }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://almadalabel.com/`)**:
   - Landmark `<footer class="footer colorGroup--primary">` anchoring `ALMADA LABEL - A modern take on ` footer links (`Journal · New Arrivals · Coming Soon · Gift Edit New · Occasion Edit New`), copy *"Autumn / Winter 26"*, and `#a6a6a5` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: almadalabel-com (ALMADA LABEL - A modern take on a seasonless wardrobe)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `almadalabel-com` (**ALMADA LABEL - A modern take on a seasonless wardrobe** — `https://almadalabel.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#0000ee` accent).
- **Identity & Domain Context**: Seasonless modern wardrobe staples designed with Scandinavian minimalism, resonating beyond trends. Responsibly crafted from high-quality...
- **Primary Substrate**: `#ffffff` (live computed `browser-default` `background-color` (`computed_styles.json`)), **Primary Ink**: `#000000`, **Accent / Highlight**: `#0000ee`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `browser-default` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#0000ee` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Paragraph Primary Font` for display copy (`ALMADA`) with `Paragraph Primary Font` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 16px`, padding `32px`) with `cubic-bezier(0.25,0.1,0.25,1)` easing and Swiper Touch Carousel Engine, Barba.js Page Transition Router.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `almadalabel-com` in your global stylesheet:

:root {
  /* ALMADA LABEL - A modern take on a seasonless wardrobe (almadalabel-com) — Live-Grounded CSS Variables */
  --background_color: #ffffff; /* Canvas / Surface Token (almadalabel-com) */
  --background_color_2: #f3f2f2; /* Canvas / Surface Token (almadalabel-com) */
  --primary_text: #17140f; /* Typography Ink Token (almadalabel-com) */
  --secondary_text: #ffffff; /* Typography Ink Token (almadalabel-com) */
  --primary_accent: #a6a6a5; /* Brand / Palette Token (almadalabel-com) */
  --secondary_accent: #38302e; /* Brand / Palette Token (almadalabel-com) */
  --primary_gray: #55534e; /* Brand / Palette Token (almadalabel-com) */
  --secondary_gray: #88847c; /* Brand / Palette Token (almadalabel-com) */
  --tertiary_gray: #f3f2f2; /* Color / Atmospheric Token (almadalabel-com) */
  --button-bg: #a6a6a5; /* Canvas / Surface Token (almadalabel-com) */
  --button-content: #ffffff; /* Color / Atmospheric Token (almadalabel-com) */
  --button-border: #a6a6a5; /* Elevation / Border Token (almadalabel-com) */
  --body_color: #FFF; /* Brand / Palette Token (almadalabel-com) */
  --loader_color: #1e242a; /* Brand / Palette Token (almadalabel-com) */
  --submenu-position: 54px; /* Dimension / Scale Token (almadalabel-com) */
  --header-height: 54px; /* Layout / Spatial Grid Token (almadalabel-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `browser-default` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#000000` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#f3f2f2` — grounded in `var(--background_color_2)` in `:root`
- **Interactive Accent / Highlight**: `#0000ee` — grounded in live computed `a` `color` (`computed_styles.json`)
- **Secondary / Muted Copy**: `#88847c` — grounded in `var(--secondary_gray)` in `:root`
- **Structural Hairline Border**: `#a6a6a5` — grounded in `var(--button-border)` in `:root`
- **Variable Token (`--primary_text`)**: `#17140f` — grounded in `var(--primary_text)` in `:root`
- **Variable Token (`--secondary_accent`)**: `#38302e` — grounded in `var(--secondary_accent)` in `:root`
- **Variable Token (`--primary_gray`)**: `#55534e` — grounded in `var(--primary_gray)` in `:root`
- **Variable Token (`--loader_color`)**: `#1e242a` — grounded in `var(--loader_color)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport)
- **Padding & Gutters**: `32px` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `32px` horizontal padding
- **Media Queries**: `@media screen and (min-width:1025px)`, `@media (min-width:1025px)`, `@media screen and (max-width:1024px)`, `@media (prefers-reduced-motion:reduce)`
- **Corner Radii**: `50%`, `4px`, `5px`, `8px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Paragraph Primary Font`
- **Body Font Stack**: `Paragraph Primary Font`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 14px`, `line-height: 18.2px`, `font-weight: 400`); rule `h1` (`font-size: 32px`, `line-height: normal`)
- **H2 Section Rule**: live computed `h2` (`font-size: 18px`, `line-height: 24px`, `font-weight: 400`); rule `h2` (`font-size: .875rem`, `line-height: 1.125rem`, `letter-spacing: 0`, `font-weight: 400`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 20.8px`, `font-weight: 400`); CSS variables `--type_primary_paragraph_font: 'Paragraph Primary Font'`, `--weight_paragraph_font: 400`; rule `p` (`font-size: .75rem`, `line-height: 1.125rem`, `letter-spacing: 0`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 14px`, `line-height: 18.2px`, `font-weight: 400`); CSS variables `--mobile-menu-label-gap: .375rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `almadalabel-com` (`ALMADA LABEL - A modern take on a seasonless wardrobe`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.Drawer__header> — `almadalabel-com`)**:
   - DOM & Selectors: Landmark `<header class="Drawer__header">` (`1440px`) hosting `ALMADA LABEL - A modern take on a se` navigation (`Journal · New Arrivals · Coming Soon · Gift Edit New · Occasion Edit New`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-shop-id="25465225306"`, `data-venmo-supported="false"`, `data-environment="production"`), and stylesheet rule `.form-checkbox__label { display:flex;flex-direction:row;align-items:center;gap:.5rem;width:100%;... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.Drawer__header> — `almadalabel-com`)` (`almadalabel-com`) adapts across `@media screen and (min-width:1025px)`, `@media (min-width:1025px)`, `@media screen and (max-width:1024px)`, `@media (prefers-reduced-motion:reduce)` with `cubic-bezier(0.25,0.1,0.25,1)` transitions and links `Journal · New Arrivals · Coming Soon · Gift Edit New · Occasion Edit New`.
2. **Hero Stage & Focal Lead (<article.favorites-drawer__item> — `ALMADA`)**:
   - DOM & Selectors: Landmark `<article class="favorites-drawer__item">` presenting display lead `ALMADA` and copy excerpt *"Free shipping to Germany on orders over 300€"* over `#ffffff` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#ffffff` background with `#000000` headline `ALMADA`.
3. **Primary Showcase & Content Grid (<article.favorites-drawer__item:nth(2)> — `Silk, lustrous satin and delicate `)**:
   - DOM & Selectors: Landmark `<article class="favorites-drawer__item">` rendering section `Silk, lustrous satin and delicate sheer layers` with copy *"Shop occasion edit"*, asset references (`script.js`, `weglot_script_tag.js`, `storefrontattributes`, `trsdk`), and grid rule `.form-checkbox__label-text p { display:inline }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<article.favorites-drawer__item:nth(2)> — `Silk, lustrous satin and delicate `)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `32px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.favorites-drawer__item:nth(3)> — `Search`)**:
   - DOM & Selectors: Landmark `<article class="favorites-drawer__item">` framing `Search` and `Search Wishlist Cart 0` (*"Search Wishlist Cart 0"*) with `#f3f2f2` surface cards, `#0000ee` accents, and `.form-checkbox { width:100% }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.favorites-drawer__item:nth(3)> — `Search`)` uses `50%`, `4px`, `5px`, `8px` radii, `#0000ee` highlights, and assets (script.js, weglot_script_tag.js, storefrontattributes).
5. **Colophon & Global Directory Footer (<footer.footer> — `https://almadalabel.com/`)**:
   - DOM & Selectors: Landmark `<footer class="footer colorGroup--primary">` anchoring `ALMADA LABEL - A modern take on ` footer links (`Journal · New Arrivals · Coming Soon · Gift Edit New · Occasion Edit New`), copy *"Autumn / Winter 26"*, and `#a6a6a5` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer> — `https://almadalabel.com/`)` aligns to `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport) with `32px` lateral canvas padding with `16px` grid gap and attributes (data-source-attribution="shopify.exit_intersti...", data-shop-id="25465225306", data-venmo-supported="false").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Free shipping to Germany on orders over 300€"*
- Copy Excerpt 2: *"Shop occasion edit"*
- Copy Excerpt 3: *"Search Wishlist Cart 0"*
- Copy Excerpt 4: *"Autumn / Winter 26"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`
- **Extracted Stylesheet Rules (`almadalabel-com`)**:
- `.form-checkbox__label { display:flex;flex-direction:row;align-items:center;gap:.5rem;width:100%;... }`
- `.form-checkbox__label-text p { display:inline }`
- `.form-checkbox { width:100% }`
- `label .svg-checkbox__square-solid { display:flex;align-items:center;justify-content:center }`
- `.icon-text-block { display:flex;align-items:center }`
- **Per-Selector Transition Rules**:
- **Selector `.product-card__media`**: `transition: opacity .15s ease-out` extracted from `almadalabel-com` stylesheet.
- **Selector `.product-card__image`**: `transition: opacity .35s ease` extracted from `almadalabel-com` stylesheet.
- **Selector `duct-card[data-slider] .product-c...`**: `transition: transform .35s ease` extracted from `almadalabel-com` stylesheet.
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in captured CSS).
- **Runtime Interaction Engine**: Integrates Swiper Touch Carousel Engine, Barba.js Page Transition Router, Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `almadalabel-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
