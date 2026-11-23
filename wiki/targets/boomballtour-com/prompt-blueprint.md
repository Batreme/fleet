---
title: "UI Prompt Blueprint: boomballtour-com"
date: 2026-11-23
captured_at: 2026-11-23
target: "boomballtour-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#f4eddf` canvas, `#1f335e` ink, `#ff0000` accent)"
---

# UI Design System & Master Generation Blueprint: boomballtour-com

> **Boom Ball Baseball · The Ultimate Family Sports Experience** (https://boomballtour.com/) — Discover Boom Ball — the interactive, family-friendly baseball show packed with energy, music, and nonstop fun for all ages.

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Boom Ball Baseball · The Ultimate Family Sports Experience** (`https://boomballtour.com/`). Discover Boom Ball — the interactive, family-friendly baseball show packed with energy, music, and nonstop fun for all ages.
- **Final Redirected URL**: [https://boomball.com/](https://boomball.com/)
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#f4eddf` canvas, `#1f335e` ink, `#ff0000` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f4eddf` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#1f335e` primary typography and `#ff0000` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Groundout` for display copy (`Bigger Than Baseball`) with `Inter-400` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1320px` container bounds (`gap: 8px`, padding `40px`) with `cubic-bezier(0.22,1,0.36,1)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1320px` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `40px` lateral canvas padding with `8px` grid gap.
- **Border Radius Scale**: `290486px`, `50%`, `5px`, `100%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1320px`, `gap: 8px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `40px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (min-width:1000px)`, `@media screen and (max-width:1000px)`, `@media screen and (max-width:768px)`, `@media screen and (max-width:480px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f4eddf` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#1f335e` | live computed `a` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f3ebdc` | `var(--bb-color-paper)` in `:root` |
| **Interactive Accent / Highlight** | `#ff0000` | `.woocommerce a.remove { color: red }` (`#ff0000`) |
| **Secondary / Muted Copy** | `#5ba238` | `var(--fkcart-saving-text-price-color)` in `:root` |
| **Structural Hairline Border** | `#b8b3a8` | `var(--bb-color-divider)` in `:root` |
| **Variable Token (`--bb-color-pink`)** | `#ff1e96` | `var(--bb-color-pink)` in `:root` |
| **Variable Token (`--bb-color-gold`)** | `#c2a155` | `var(--bb-color-gold)` in `:root` |
| **Variable Token (`--bb-color-ink`)** | `#43433d` | `var(--bb-color-ink)` in `:root` |
| **Variable Token (`--bb-color-white`)** | `#ffffff` | `var(--bb-color-white)` in `:root` |
| **Variable Token (`--bb-color-slate`)** | `#79859f` | `var(--bb-color-slate)` in `:root` |
| **Variable Token (`--bb-color-inactive`)** | `#f894c5` | `var(--bb-color-inactive)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bb-color-pink` | `#ff1e96` | Typography Ink Token |
| `--bb-color-blue` | `#1f335e` | Brand / Palette Token |
| `--bb-color-gold` | `#c2a155` | Brand / Palette Token |
| `--bb-color-ink` | `#43433d` | Typography Ink Token |
| `--bb-color-paper` | `#f3ebdc` | Canvas / Surface Token |
| `--bb-color-white` | `#ffffff` | Canvas / Surface Token |
| `--bb-color-slate` | `#79859f` | Brand / Palette Token |
| `--bb-color-frame` | `rgb(255 255 255 / 35%)` | Brand / Palette Token |
| `--bb-color-divider` | `#B8B3A8` | Brand / Palette Token |
| `--bb-color-inactive` | `#f894c5` | Brand / Palette Token |
| `--bb-font-body` | `"Inter-400", Arial, Helvetica, sans-serif` | Typography / Scale Token |
| `--bb-font-body-medium` | `"Inter-500", Arial, Helvetica, sans-serif` | Typography / Scale Token |
| `--bb-font-heading` | `"Hamburg-700", Arial, Helvetica, sans-serif` | Typography Ink Token |
| `--bb-font-display` | `"Groundout", Georgia, serif` | Typography / Scale Token |
| `--bb-font-script` | `"Brooklyn-700", Georgia, serif` | Typography / Scale Token |
| `--bb-font-mono` | `"Roboto-600", "Courier New", monospace` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Groundout`.
- **Primary Body Stack**: `Inter-400`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 96px`, `line-height: 76.8px`, `font-weight: 500`); CSS variables `--bb-font-display: "Groundout", Georgia, serif`, `--bbc-font-display: var(--bb-font-display, Georgia, serif)`; rule `,h1` (`font-size: calc(1.375rem + 1.5vw)`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 32px`, `line-height: 35.84px`, `font-weight: 700`); rule `,h2` (`font-size: calc(1.325rem + .9vw)`).
- **Body Copy**: live computed `body` (`font-size: 18px`, `line-height: 23.4px`, `font-weight: 400`); CSS variables `--bb-font-body: "Inter-400", Arial, Helvetica, sans-serif`, `--bb-font-body-medium: "Inter-500", Arial, Helvetica, sans-serif`, `--bs-body-bg-rgb: 255,255,255`; rule `p` (`font-weight: 400`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 18px`, `line-height: 23.4px`, `font-weight: 400`); CSS variables `--bb-font-mono: "Roboto-600", "Courier New", monospace`, `--bbc-font-label: var(--bb-font-heading, Arial, Helvetica, sans-serif)`, `--wpforms-field-size-sublabel-spacing: 5px`; rule `small` (`font-size: 15px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.22,1,0.36,1)`, `cubic-bezier(.28,.84,.42,1)`, `cubic-bezier(.4,0,.6,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `#fkcart-floating-toggler`**: `transition: box-shadow .25s ease 0s,opacity .4s ease 0s,scale 1s ease-in-o...` extracted from `boomballtour-com` stylesheet.
- **Selector `cart-floating-toggler .fkcart-flo...`**: `transition: opacity 80ms linear 0s,transform .16s linear 0s` extracted from `boomballtour-com` stylesheet.
- **Selector `#fkcart-modal .fkcart-preview-ui`**: `transition: transform var(--fkcart-animation-duration,.4s) ease-out` extracted from `boomballtour-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.22,1,0.36,1)`)**: Governs interactive state transitions across `<nav.footer-nav>` and `<section.bb-feature>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Boom Ball Baseball · The Ultimate Family S │
│ ====================================================================== │
│ [ <nav.footer-nav> (273x144px)        | What’s Boom Ball · Teams · A ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero-banner> (w=1440px)                       | │
│ | H1: Bigger Than Baseball                                           | │
│ | Substrate: #f4eddf | Ink: #1f335e | Accent: #ff0000                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.bb-feature>) max-w: 1320px                 | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Boom Ball is baseball reimag |  | EVERY INNING BRINGS          | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<article.bb-feature__item>) — Babe Ruth Hologram    | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer>) | https://boomballtour.com/            │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 8px)        │
│ ====================================================================== │
│ [ HEADER BAR (<nav.footer-nav>        ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.hero-banner>) — 390px Vertical Lead           | │
│ | H1: Bigger Than Baseball                                           | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.bb-feature>) — 1-Col Stack                | │
│ | [ Item 1: Boom Ball is baseball reimagined for families—a        ] | │
│ | [ Item 2: EVERY INNING BRINGS                                    ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<article.bb-feature__ite) — 1-Col (Babe Ruth Hologram) │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer>) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.footer-nav> — `boomballtour-com`)**:
   - Landmark `<nav class="footer-nav">` (`273x144px`) hosting `Boom Ball Baseball · The Ultimate Fa` navigation (`What’s Boom Ball · Teams · About · Tickets · Merch`), DOM attributes (`data-id="D8BJ15BC77UDFA3HME2G"`, `data-wp-strategy="defer"`, `data-wp-strategy="defer"`, `data-wp-strategy="defer"`), and stylesheet rule `fkcart-modal { font-size:16px;color:var(--fkcart-primary-text-color);line-height:1.3;fo... }`.
2. **Hero Stage & Focal Lead (<section.hero-banner> — `Bigger Than Baseball`)**:
   - Landmark `<section class="hero-banner">` presenting display lead `Bigger Than Baseball` and copy excerpt *"Boom Ball is baseball reimagined for families—a fast-paced, high-"* over `#f4eddf` canvas and `#1f335e` ink.
3. **Primary Showcase & Content Grid (<section.bb-feature> — `Boom Ball is baseball reimagined f`)**:
   - Landmark `<section class="bb-feature is-enhanced">` rendering section `Boom Ball is baseball reimagined for families—a ` with copy *"EVERY INNING BRINGS"*, asset references (`favicon-96x96.png`, `favicon.svg`, `favicon.ico`, `apple-touch-icon.png`), and grid rule `webkit-scrollbar { width:6px;height:5px }`.
4. **Interactive Detail & Feature Matrix (<article.bb-feature__item> — `EVERY INNING BRINGS`)**:
   - Landmark `<article class="bb-feature__item reveal-slide">` framing `EVERY INNING BRINGS` and `Babe Ruth Hologram` (*"Babe Ruth Hologram"*) with `#f3ebdc` surface cards, `#ff0000` accents, and `webkit-scrollbar-thumb { background:666 }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://boomballtour.com/`)**:
   - Landmark `<footer class="site-footer">` anchoring `Boom Ball Baseball · The Ultimat` footer links (`What’s Boom Ball · Teams · About · Tickets · Merch`), copy *"See The Great Bambino take the field and re-create his legen"*, and `#b8b3a8` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: boomballtour-com (Boom Ball Baseball · The Ultimate Family Sports Experience)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `boomballtour-com` (**Boom Ball Baseball · The Ultimate Family Sports Experience** — `https://boomballtour.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#f4eddf` canvas, `#1f335e` ink, `#ff0000` accent).
- **Identity & Domain Context**: Discover Boom Ball — the interactive, family-friendly baseball show packed with energy, music, and nonstop fun for all ages.
- **Primary Substrate**: `#f4eddf` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#1f335e`, **Accent / Highlight**: `#ff0000`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f4eddf` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#1f335e` primary typography and `#ff0000` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Groundout` for display copy (`Bigger Than Baseball`) with `Inter-400` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1320px` container bounds (`gap: 8px`, padding `40px`) with `cubic-bezier(0.22,1,0.36,1)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `boomballtour-com` in your global stylesheet:

:root {
  /* Boom Ball Baseball · The Ultimate Family Sports Experience (boomballtour-com) — Live-Grounded CSS Variables */
  --bb-color-pink: #ff1e96; /* Typography Ink Token (boomballtour-com) */
  --bb-color-blue: #1f335e; /* Brand / Palette Token (boomballtour-com) */
  --bb-color-gold: #c2a155; /* Brand / Palette Token (boomballtour-com) */
  --bb-color-ink: #43433d; /* Typography Ink Token (boomballtour-com) */
  --bb-color-paper: #f3ebdc; /* Canvas / Surface Token (boomballtour-com) */
  --bb-color-white: #ffffff; /* Canvas / Surface Token (boomballtour-com) */
  --bb-color-slate: #79859f; /* Brand / Palette Token (boomballtour-com) */
  --bb-color-frame: rgb(255 255 255 / 35%); /* Brand / Palette Token (boomballtour-com) */
  --bb-color-divider: #B8B3A8; /* Brand / Palette Token (boomballtour-com) */
  --bb-color-inactive: #f894c5; /* Brand / Palette Token (boomballtour-com) */
  --bb-font-body: "Inter-400", Arial, Helvetica, sans-serif; /* Typography / Scale Token (boomballtour-com) */
  --bb-font-body-medium: "Inter-500", Arial, Helvetica, sans-serif; /* Typography / Scale Token (boomballtour-com) */
  --bb-font-heading: "Hamburg-700", Arial, Helvetica, sans-serif; /* Typography Ink Token (boomballtour-com) */
  --bb-font-display: "Groundout", Georgia, serif; /* Typography / Scale Token (boomballtour-com) */
  --bb-font-script: "Brooklyn-700", Georgia, serif; /* Typography / Scale Token (boomballtour-com) */
  --bb-font-mono: "Roboto-600", "Courier New", monospace; /* Typography / Scale Token (boomballtour-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f4eddf` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#1f335e` — grounded in live computed `a` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#f3ebdc` — grounded in `var(--bb-color-paper)` in `:root`
- **Interactive Accent / Highlight**: `#ff0000` — grounded in `.woocommerce a.remove { color: red }` (`#ff0000`)
- **Secondary / Muted Copy**: `#5ba238` — grounded in `var(--fkcart-saving-text-price-color)` in `:root`
- **Structural Hairline Border**: `#b8b3a8` — grounded in `var(--bb-color-divider)` in `:root`
- **Variable Token (`--bb-color-pink`)**: `#ff1e96` — grounded in `var(--bb-color-pink)` in `:root`
- **Variable Token (`--bb-color-gold`)**: `#c2a155` — grounded in `var(--bb-color-gold)` in `:root`
- **Variable Token (`--bb-color-ink`)**: `#43433d` — grounded in `var(--bb-color-ink)` in `:root`
- **Variable Token (`--bb-color-white`)**: `#ffffff` — grounded in `var(--bb-color-white)` in `:root`
- **Variable Token (`--bb-color-slate`)**: `#79859f` — grounded in `var(--bb-color-slate)` in `:root`
- **Variable Token (`--bb-color-inactive`)**: `#f894c5` — grounded in `var(--bb-color-inactive)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1320px` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `40px` lateral canvas padding with `8px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1320px`, `gap: 8px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `40px` horizontal padding
- **Media Queries**: `@media screen and (min-width:1000px)`, `@media screen and (max-width:1000px)`, `@media screen and (max-width:768px)`, `@media screen and (max-width:480px)`
- **Corner Radii**: `290486px`, `50%`, `5px`, `100%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Groundout`
- **Body Font Stack**: `Inter-400`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 96px`, `line-height: 76.8px`, `font-weight: 500`); CSS variables `--bb-font-display: "Groundout", Georgia, serif`, `--bbc-font-display: var(--bb-font-display, Georgia, serif)`; rule `,h1` (`font-size: calc(1.375rem + 1.5vw)`)
- **H2 Section Rule**: live computed `h2` (`font-size: 32px`, `line-height: 35.84px`, `font-weight: 700`); rule `,h2` (`font-size: calc(1.325rem + .9vw)`)
- **Body Copy Rule**: live computed `body` (`font-size: 18px`, `line-height: 23.4px`, `font-weight: 400`); CSS variables `--bb-font-body: "Inter-400", Arial, Helvetica, sans-serif`, `--bb-font-body-medium: "Inter-500", Arial, Helvetica, sans-serif`, `--bs-body-bg-rgb: 255,255,255`; rule `p` (`font-weight: 400`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 18px`, `line-height: 23.4px`, `font-weight: 400`); CSS variables `--bb-font-mono: "Roboto-600", "Courier New", monospace`, `--bbc-font-label: var(--bb-font-heading, Arial, Helvetica, sans-serif)`, `--wpforms-field-size-sublabel-spacing: 5px`; rule `small` (`font-size: 15px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `boomballtour-com` (`Boom Ball Baseball · The Ultimate Family Sports Experience`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.footer-nav> — `boomballtour-com`)**:
   - DOM & Selectors: Landmark `<nav class="footer-nav">` (`273x144px`) hosting `Boom Ball Baseball · The Ultimate Fa` navigation (`What’s Boom Ball · Teams · About · Tickets · Merch`), DOM attributes (`data-id="D8BJ15BC77UDFA3HME2G"`, `data-wp-strategy="defer"`, `data-wp-strategy="defer"`, `data-wp-strategy="defer"`), and stylesheet rule `fkcart-modal { font-size:16px;color:var(--fkcart-primary-text-color);line-height:1.3;fo... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.footer-nav> — `boomballtour-com`)` (`boomballtour-com`) adapts across `@media screen and (min-width:1000px)`, `@media screen and (max-width:1000px)`, `@media screen and (max-width:768px)`, `@media screen and (max-width:480px)` with `cubic-bezier(0.22,1,0.36,1)`, `cubic-bezier(.28,.84,.42,1)`, `cubic-bezier(.4,0,.6,1)` transitions and links `What’s Boom Ball · Teams · About · Tickets · Merch`.
2. **Hero Stage & Focal Lead (<section.hero-banner> — `Bigger Than Baseball`)**:
   - DOM & Selectors: Landmark `<section class="hero-banner">` presenting display lead `Bigger Than Baseball` and copy excerpt *"Boom Ball is baseball reimagined for families—a fast-paced, high-"* over `#f4eddf` canvas and `#1f335e` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#f4eddf` background with `#1f335e` headline `Bigger Than Baseball`.
3. **Primary Showcase & Content Grid (<section.bb-feature> — `Boom Ball is baseball reimagined f`)**:
   - DOM & Selectors: Landmark `<section class="bb-feature is-enhanced">` rendering section `Boom Ball is baseball reimagined for families—a ` with copy *"EVERY INNING BRINGS"*, asset references (`favicon-96x96.png`, `favicon.svg`, `favicon.ico`, `apple-touch-icon.png`), and grid rule `webkit-scrollbar { width:6px;height:5px }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.bb-feature> — `Boom Ball is baseball reimagined f`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1320px`, `gap: 8px`) on desktop and Single-column vertical stack at `390px` viewport width with `40px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.bb-feature__item> — `EVERY INNING BRINGS`)**:
   - DOM & Selectors: Landmark `<article class="bb-feature__item reveal-slide">` framing `EVERY INNING BRINGS` and `Babe Ruth Hologram` (*"Babe Ruth Hologram"*) with `#f3ebdc` surface cards, `#ff0000` accents, and `webkit-scrollbar-thumb { background:666 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.bb-feature__item> — `EVERY INNING BRINGS`)` uses `290486px`, `50%`, `5px`, `100%` radii, `#ff0000` highlights, and assets (favicon-96x96.png, favicon.svg, favicon.ico).
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://boomballtour.com/`)**:
   - DOM & Selectors: Landmark `<footer class="site-footer">` anchoring `Boom Ball Baseball · The Ultimat` footer links (`What’s Boom Ball · Teams · About · Tickets · Merch`), copy *"See The Great Bambino take the field and re-create his legen"*, and `#b8b3a8` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.site-footer> — `https://boomballtour.com/`)` aligns to `1320px` (non-`@media` desktop container stylesheet rule) with `40px` lateral canvas padding with `8px` grid gap and attributes (data-id="D8BJ15BC77UDFA3HME2G", data-wp-strategy="defer", data-wp-strategy="defer").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Boom Ball is baseball reimagined for families—a fast-paced, high-energy show packe..."*
- Copy Excerpt 2: *"EVERY INNING BRINGS"*
- Copy Excerpt 3: *"Babe Ruth Hologram"*
- Copy Excerpt 4: *"See The Great Bambino take the field and re-create his legendary Called Shot momen..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.22,1,0.36,1)`, `cubic-bezier(.28,.84,.42,1)`, `cubic-bezier(.4,0,.6,1)`
- **Extracted Stylesheet Rules (`boomballtour-com`)**:
- `fkcart-modal { font-size:16px;color:var(--fkcart-primary-text-color);line-height:1.3;fo... }`
- `webkit-scrollbar { width:6px;height:5px }`
- `webkit-scrollbar-thumb { background:666 }`
- `webkit-scrollbar-track { background:dedede }`
- `fkcart-modal .fkcart-hide { display:none!important }`
- **Per-Selector Transition Rules**:
- **Selector `#fkcart-floating-toggler`**: `transition: box-shadow .25s ease 0s,opacity .4s ease 0s,scale 1s ease-in-o...` extracted from `boomballtour-com` stylesheet.
- **Selector `cart-floating-toggler .fkcart-flo...`**: `transition: opacity 80ms linear 0s,transform .16s linear 0s` extracted from `boomballtour-com` stylesheet.
- **Selector `#fkcart-modal .fkcart-preview-ui`**: `transition: transform var(--fkcart-animation-duration,.4s) ease-out` extracted from `boomballtour-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.22,1,0.36,1)`)**: Governs interactive state transitions across `<nav.footer-nav>` and `<section.bb-feature>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `boomballtour-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
