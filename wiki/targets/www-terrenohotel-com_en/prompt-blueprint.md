---
title: "UI Prompt Blueprint: www-terrenohotel-com_en"
date: 2026-11-23
captured_at: 2026-11-23
target: "www-terrenohotel-com_en"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#ecffb3` canvas, `#570007` ink, `#cc3224` accent)"
---

# UI Design System & Master Generation Blueprint: www-terrenohotel-com_en

> **Terreno Barrio Hotel · Boutique hotel in Palma de Mallorca** (https://www.terrenohotel.com/en/) — Boutique hotel in Palma de Mallorca with Mediterranean design, local character, rooftop moments and direct booking benefits on the offici...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Terreno Barrio Hotel · Boutique hotel in Palma de Mallorca** (`https://www.terrenohotel.com/en/`). Boutique hotel in Palma de Mallorca with Mediterranean design, local character, rooftop moments and direct booking benefits on the offici...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#ecffb3` canvas, `#570007` ink, `#cc3224` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ecffb3` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#570007` primary typography and `#cc3224` accents.
  - **Grounded Typographic Hierarchy**: Pairs `WT Central Avenue` for display copy (`A HOTEL WITH A NEIGHBORHOOD SOUL`) with `Tiempos Text` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1026px` container bounds (`gap: 10px`, padding `100px`) with `cubic-bezier(.68,-.55,.27,1.55)` easing and Swiper Touch Carousel Engine.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1026px` (measured widest bounded `<section>` landmark width on `1440px` desktop).
- **Canvas Lateral Padding & Spacing**: `100px` lateral canvas padding with `10px` grid gap.
- **Border Radius Scale**: `0px`, `var(--mirai-ui-checkbox-border-radius)`, `var(--mirai-ui-input-text-radius)`, `50%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1026px`, `gap: 10px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `100px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width: 767px)`, `@media only screen and (max-width:480px)`, `@media only screen and (min-width:481px)`, `@media only screen and (min-width:481px) and (max-width:1179px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ecffb3` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#570007` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f6f6f6` | `var(--mirai-ui-content-background)` in `:root` |
| **Interactive Accent / Highlight** | `#cc3224` | `.cookiescript_vendor_name a:hover { color: #cc3224 }` |
| **Secondary / Muted Copy** | `#7d7e81` | `#capacalendario .cabeceracal .n... { color: #7d7e81 }` |
| **Structural Hairline Border** | `#dddddd` | `var(--mirai-ui-content-border)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--mirai-ui-font-weight` | `400` | Typography / Scale Token |
| `--mirai-ui-font-medium` | `var(--mirai-ui-font)` | Typography / Scale Token |
| `--mirai-ui-font-medium-weight` | `500` | Typography / Scale Token |
| `--mirai-ui-font-bold` | `var(--mirai-ui-font)` | Typography / Scale Token |
| `--mirai-ui-font-bold-weight` | `700` | Typography / Scale Token |
| `--mirai-ui-font-size-headline-1` | `32px` | Typography / Scale Token |
| `--mirai-ui-line-height-headline-1` | `40px` | Typography / Scale Token |
| `--mirai-ui-font-size-headline-2` | `24px` | Typography / Scale Token |
| `--mirai-ui-line-height-headline-2` | `32px` | Typography / Scale Token |
| `--mirai-ui-font-size-headline-3` | `20px` | Typography / Scale Token |
| `--mirai-ui-line-height-headline-3` | `24px` | Typography / Scale Token |
| `--mirai-ui-font-size-paragraph` | `16px` | Typography / Scale Token |
| `--mirai-ui-line-height-paragraph` | `20px` | Typography / Scale Token |
| `--mirai-ui-font-size-action` | `14px` | Typography / Scale Token |
| `--mirai-ui-line-height-action` | `18px` | Typography / Scale Token |
| `--mirai-ui-font-size-small` | `12px` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `WT Central Avenue`.
- **Primary Body Stack**: `Tiempos Text`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 68px`, `line-height: 60px`, `font-weight: 700`); rule `.title` (`font-size: 3.6rem`, `line-height: 3.6rem`, `letter-spacing: 2.4%`, `font-weight: 700`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 68px`, `line-height: 60px`, `font-weight: 700`); CSS variables `--subtitle-fs: 1.8rem`, `--subtitle-lh: 2.6rem`, `--subtitle-g: 0.8rem`.
- **Body Copy**: live computed `body` (`font-size: 10px`, `line-height: normal`, `font-weight: 400`); CSS variables `--mirai-ui-font-size-paragraph: 16px`, `--mirai-ui-line-height-paragraph: 20px`; rule `body` (`font-weight: 400`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 10px`, `line-height: normal`, `font-weight: 400`); CSS variables `--mirai-ui-font-size-small: 12px`, `--mirai-ui-line-height-small: 16px`, `--mirai-ui-button-small-height: calc(var(--mirai-ui-space-XL) - var(--mirai-ui-space-M))`; rule `small` (`font-size: 12px`, `line-height: 14px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.68,-.55,.27,1.55)`, `cubic-bezier(.1,.1,.25,.9)`, `cubic-bezier(0.4,0,0.22,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `._3qK-PW_checkbox input`**: `transition: background-color var(--mirai-ui-motion-collapse)var(--mirai-ui...` extracted from `www-terrenohotel-com_en` stylesheet.
- **Selector `t.I2Uiuq_input:focus:required:inv...`**: `transition: none` extracted from `www-terrenohotel-com_en` stylesheet.
- **Selector `input.I2Uiuq_input:-webkit-autofill`**: `transition: none` extracted from `www-terrenohotel-com_en` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.68,-.55,.27,1.55)`)**: Governs interactive state transitions across `<header.mdl-header>` and `<article.e-slide>`.
- **Runtime Interaction Engine**: Integrates Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Terreno Barrio Hotel · Boutique hotel in P │
│ ====================================================================== │
│ [ <header.mdl-header> (1440x90px)     | Overview · Index · Archive · ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.m-experiencias> (w=1440px)                    | │
│ | H1: A HOTEL WITH A NEIGHBORHOOD SOUL                               | │
│ | Substrate: #ecffb3 | Ink: #570007 | Accent: #cc3224                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<article.e-slide>) max-w: 1026px                    | │
│ | +------------------------------+  +------------------------------+ | │
│ | | a hotel with a neighborhood  |  | TERRENO IS PART OF THE NEIGH | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<article.swiper-slide>) — THE PLACE TO STAY         | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.module-foote) | https://www.terrenohotel.com/en/     │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 10px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.mdl-header>     ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.m-experiencias>) — 390px Vertical Lead        | │
│ | H1: A HOTEL WITH A NEIGHBORHOOD SOUL                               | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<article.e-slide>) — 1-Col Stack                   | │
│ | [ Item 1: a hotel with a neighborhood soul                       ] | │
│ | [ Item 2: TERRENO IS PART OF THE NEIGHBOURHOOD. THE NEIGHBO...   ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<article.swiper-slide>) — 1-Col (THE PLACE TO STAY)  | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.module-foote) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.mdl-header> — `www-terrenohotel-com_en`)**:
   - Landmark `<header class="mdl-header color-scheme-burgundy">` (`1440x90px`) hosting `Terreno Barrio Hotel · Boutique hote` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-ueto="ueto_c4cc3437ae"`, `data-thn-current="1"`, `data-mirai-id="100380929"`, `data-type="hotel"`), and stylesheet rule `.mdl-hero .search-form { position: relative; z-index: 5; }`.
2. **Hero Stage & Focal Lead (<section.m-experiencias> — `A HOTEL WITH A NEIGHBORHOOD SOUL`)**:
   - Landmark `<section class="m-experiencias color-scheme-burgundy">` presenting display lead `A HOTEL WITH A NEIGHBORHOOD SOUL` and copy excerpt *"Some neighbourhoods have something you can’t quite put your finge"* over `#ecffb3` canvas and `#570007` ink.
3. **Primary Showcase & Content Grid (<article.e-slide> — `a hotel with a neighborhood soul`)**:
   - Landmark `<article class="e-slide swiper-slide">` rendering section `a hotel with a neighborhood soul` with copy *"LIVE BARRIO AGENDA SPA"*, asset references (`favicon-ios-7f1277496f8279e6f805a...`, `favicon-ios-3a0235b9e158e0432cb3d...`, `0.8.77`, `clientParamBuilder.bundle.js`), and grid rule `.module-content { overflow: visible !important; }`.
4. **Interactive Detail & Feature Matrix (<article.swiper-slide> — `TERRENO IS PART OF THE NEIGHBOURHO`)**:
   - Landmark `<article class="e-slide swiper-slide">` framing `TERRENO IS PART OF THE NEIGHBOURHOOD. THE NEIGHBO...` and `THE PLACE TO STAY` (*"DRINK EL TERRADO Club"*) with `#f6f6f6` surface cards, `#cc3224` accents, and `.mdl-header { z-index: 900; }`.
5. **Colophon & Global Directory Footer (<footer.module-footer> — `https://www.terrenohotel.com/en/`)**:
   - Landmark `<footer class="module-footer">` anchoring `Terreno Barrio Hotel · Boutique ` footer links (`Overview · Index · Archive · About · Contact`), copy *"24 HOURS IN TERRENO"*, and `#dddddd` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-terrenohotel-com_en (Terreno Barrio Hotel · Boutique hotel in Palma de Mallorca)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-terrenohotel-com_en` (**Terreno Barrio Hotel · Boutique hotel in Palma de Mallorca** — `https://www.terrenohotel.com/en/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#ecffb3` canvas, `#570007` ink, `#cc3224` accent).
- **Identity & Domain Context**: Boutique hotel in Palma de Mallorca with Mediterranean design, local character, rooftop moments and direct booking benefits on the offici...
- **Primary Substrate**: `#ecffb3` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#570007`, **Accent / Highlight**: `#cc3224`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ecffb3` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#570007` primary typography and `#cc3224` accents.
  - **Grounded Typographic Hierarchy**: Pairs `WT Central Avenue` for display copy (`A HOTEL WITH A NEIGHBORHOOD SOUL`) with `Tiempos Text` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1026px` container bounds (`gap: 10px`, padding `100px`) with `cubic-bezier(.68,-.55,.27,1.55)` easing and Swiper Touch Carousel Engine.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-terrenohotel-com_en` in your global stylesheet:

:root {
  /* Terreno Barrio Hotel · Boutique hotel in Palma de Mallorca (www-terrenohotel-com_en) — Live-Grounded CSS Variables */
  --mirai-ui-font-weight: 400; /* Typography / Scale Token (www-terrenohotel-com_en) */
  --mirai-ui-font-medium: var(--mirai-ui-font); /* Typography / Scale Token (www-terrenohotel-com_en) */
  --mirai-ui-font-medium-weight: 500; /* Typography / Scale Token (www-terrenohotel-com_en) */
  --mirai-ui-font-bold: var(--mirai-ui-font); /* Typography / Scale Token (www-terrenohotel-com_en) */
  --mirai-ui-font-bold-weight: 700; /* Typography / Scale Token (www-terrenohotel-com_en) */
  --mirai-ui-font-size-headline-1: 32px; /* Typography / Scale Token (www-terrenohotel-com_en) */
  --mirai-ui-line-height-headline-1: 40px; /* Typography / Scale Token (www-terrenohotel-com_en) */
  --mirai-ui-font-size-headline-2: 24px; /* Typography / Scale Token (www-terrenohotel-com_en) */
  --mirai-ui-line-height-headline-2: 32px; /* Typography / Scale Token (www-terrenohotel-com_en) */
  --mirai-ui-font-size-headline-3: 20px; /* Typography / Scale Token (www-terrenohotel-com_en) */
  --mirai-ui-line-height-headline-3: 24px; /* Typography / Scale Token (www-terrenohotel-com_en) */
  --mirai-ui-font-size-paragraph: 16px; /* Typography / Scale Token (www-terrenohotel-com_en) */
  --mirai-ui-line-height-paragraph: 20px; /* Typography / Scale Token (www-terrenohotel-com_en) */
  --mirai-ui-font-size-action: 14px; /* Typography / Scale Token (www-terrenohotel-com_en) */
  --mirai-ui-line-height-action: 18px; /* Typography / Scale Token (www-terrenohotel-com_en) */
  --mirai-ui-font-size-small: 12px; /* Typography / Scale Token (www-terrenohotel-com_en) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ecffb3` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#570007` — grounded in live computed `main` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#f6f6f6` — grounded in `var(--mirai-ui-content-background)` in `:root`
- **Interactive Accent / Highlight**: `#cc3224` — grounded in `.cookiescript_vendor_name a:hover { color: #cc3224 }`
- **Secondary / Muted Copy**: `#7d7e81` — grounded in `#capacalendario .cabeceracal .n... { color: #7d7e81 }`
- **Structural Hairline Border**: `#dddddd` — grounded in `var(--mirai-ui-content-border)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1026px` (measured widest bounded `<section>` landmark width on `1440px` desktop)
- **Padding & Gutters**: `100px` lateral canvas padding with `10px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1026px`, `gap: 10px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `100px` horizontal padding
- **Media Queries**: `@media (max-width: 767px)`, `@media only screen and (max-width:480px)`, `@media only screen and (min-width:481px)`, `@media only screen and (min-width:481px) and (max-width:1179px)`
- **Corner Radii**: `0px`, `var(--mirai-ui-checkbox-border-radius)`, `var(--mirai-ui-input-text-radius)`, `50%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `WT Central Avenue`
- **Body Font Stack**: `Tiempos Text`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 68px`, `line-height: 60px`, `font-weight: 700`); rule `.title` (`font-size: 3.6rem`, `line-height: 3.6rem`, `letter-spacing: 2.4%`, `font-weight: 700`)
- **H2 Section Rule**: live computed `h2` (`font-size: 68px`, `line-height: 60px`, `font-weight: 700`); CSS variables `--subtitle-fs: 1.8rem`, `--subtitle-lh: 2.6rem`, `--subtitle-g: 0.8rem`
- **Body Copy Rule**: live computed `body` (`font-size: 10px`, `line-height: normal`, `font-weight: 400`); CSS variables `--mirai-ui-font-size-paragraph: 16px`, `--mirai-ui-line-height-paragraph: 20px`; rule `body` (`font-weight: 400`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 10px`, `line-height: normal`, `font-weight: 400`); CSS variables `--mirai-ui-font-size-small: 12px`, `--mirai-ui-line-height-small: 16px`, `--mirai-ui-button-small-height: calc(var(--mirai-ui-space-XL) - var(--mirai-ui-space-M))`; rule `small` (`font-size: 12px`, `line-height: 14px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-terrenohotel-com_en` (`Terreno Barrio Hotel · Boutique hotel in Palma de Mallorca`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.mdl-header> — `www-terrenohotel-com_en`)**:
   - DOM & Selectors: Landmark `<header class="mdl-header color-scheme-burgundy">` (`1440x90px`) hosting `Terreno Barrio Hotel · Boutique hote` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-ueto="ueto_c4cc3437ae"`, `data-thn-current="1"`, `data-mirai-id="100380929"`, `data-type="hotel"`), and stylesheet rule `.mdl-hero .search-form { position: relative; z-index: 5; }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.mdl-header> — `www-terrenohotel-com_en`)` (`www-terrenohotel-com_en`) adapts across `@media (max-width: 767px)`, `@media only screen and (max-width:480px)`, `@media only screen and (min-width:481px)`, `@media only screen and (min-width:481px) and (max-width:1179px)` with `cubic-bezier(.68,-.55,.27,1.55)`, `cubic-bezier(.1,.1,.25,.9)`, `cubic-bezier(0.4,0,0.22,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<section.m-experiencias> — `A HOTEL WITH A NEIGHBORHOOD SOUL`)**:
   - DOM & Selectors: Landmark `<section class="m-experiencias color-scheme-burgundy">` presenting display lead `A HOTEL WITH A NEIGHBORHOOD SOUL` and copy excerpt *"Some neighbourhoods have something you can’t quite put your finge"* over `#ecffb3` canvas and `#570007` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#ecffb3` background with `#570007` headline `A HOTEL WITH A NEIGHBORHOOD SOUL`.
3. **Primary Showcase & Content Grid (<article.e-slide> — `a hotel with a neighborhood soul`)**:
   - DOM & Selectors: Landmark `<article class="e-slide swiper-slide">` rendering section `a hotel with a neighborhood soul` with copy *"LIVE BARRIO AGENDA SPA"*, asset references (`favicon-ios-7f1277496f8279e6f805a...`, `favicon-ios-3a0235b9e158e0432cb3d...`, `0.8.77`, `clientParamBuilder.bundle.js`), and grid rule `.module-content { overflow: visible !important; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<article.e-slide> — `a hotel with a neighborhood soul`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1026px`, `gap: 10px`) on desktop and Single-column vertical stack at `390px` viewport width with `100px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.swiper-slide> — `TERRENO IS PART OF THE NEIGHBOURHO`)**:
   - DOM & Selectors: Landmark `<article class="e-slide swiper-slide">` framing `TERRENO IS PART OF THE NEIGHBOURHOOD. THE NEIGHBO...` and `THE PLACE TO STAY` (*"DRINK EL TERRADO Club"*) with `#f6f6f6` surface cards, `#cc3224` accents, and `.mdl-header { z-index: 900; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.swiper-slide> — `TERRENO IS PART OF THE NEIGHBOURHO`)` uses `0px`, `var(--mirai-ui-checkbox-border-radius)`, `var(--mirai-ui-input-text-radius)`, `50%` radii, `#cc3224` highlights, and assets (favicon-ios-7f1277496f8279e6f805a..., favicon-ios-3a0235b9e158e0432cb3d..., 0.8.77).
5. **Colophon & Global Directory Footer (<footer.module-footer> — `https://www.terrenohotel.com/en/`)**:
   - DOM & Selectors: Landmark `<footer class="module-footer">` anchoring `Terreno Barrio Hotel · Boutique ` footer links (`Overview · Index · Archive · About · Contact`), copy *"24 HOURS IN TERRENO"*, and `#dddddd` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.module-footer> — `https://www.terrenohotel.com/en/`)` aligns to `1026px` (measured widest bounded `<section>` landmark width on `1440px` desktop) with `100px` lateral canvas padding with `10px` grid gap and attributes (data-ueto="ueto_c4cc3437ae", data-thn-current="1", data-mirai-id="100380929").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Some neighbourhoods have something you can’t quite put your finger on. You just fe..."*
- Copy Excerpt 2: *"LIVE BARRIO AGENDA SPA"*
- Copy Excerpt 3: *"DRINK EL TERRADO Club"*
- Copy Excerpt 4: *"24 HOURS IN TERRENO"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.68,-.55,.27,1.55)`, `cubic-bezier(.1,.1,.25,.9)`, `cubic-bezier(0.4,0,0.22,1)`
- **Extracted Stylesheet Rules (`www-terrenohotel-com_en`)**:
- `.mdl-hero .search-form { position: relative; z-index: 5; }`
- `.module-content { overflow: visible !important; }`
- `.mdl-header { z-index: 900; }`
- `._3qK-PW_checkbox { position:relative }`
- `._3qK-PW_checkbox input:disabled { border-color:var(--mirai-ui-checkbox-background-disabled) }`
- **Per-Selector Transition Rules**:
- **Selector `._3qK-PW_checkbox input`**: `transition: background-color var(--mirai-ui-motion-collapse)var(--mirai-ui...` extracted from `www-terrenohotel-com_en` stylesheet.
- **Selector `t.I2Uiuq_input:focus:required:inv...`**: `transition: none` extracted from `www-terrenohotel-com_en` stylesheet.
- **Selector `input.I2Uiuq_input:-webkit-autofill`**: `transition: none` extracted from `www-terrenohotel-com_en` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.68,-.55,.27,1.55)`)**: Governs interactive state transitions across `<header.mdl-header>` and `<article.e-slide>`.
- **Runtime Interaction Engine**: Integrates Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-terrenohotel-com_en`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
