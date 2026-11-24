---
title: "UI Prompt Blueprint: thecassandravale-com"
date: 2026-11-24
captured_at: 2026-11-24
target: "thecassandravale-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
capture_mode: behavioral_journey_v2
asset_format: webp
scroll_driver: native
desktop_keyframes: 8
subpages_crawled: 0
http_status: 200
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#131313` canvas, `#ffffff` ink, `#ff1053` accent)"
---

# UI Design System & Master Generation Blueprint: thecassandravale-com

> **Cassandra Vale · Fashion, Stories & Branded Content** (https://thecassandravale.com/) — Cassandra Vale brings together fashion, short-form stories, editorial imagery and branded collaborations.

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Cassandra Vale · Fashion, Stories & Branded Content** (`https://thecassandravale.com/`). Cassandra Vale brings together fashion, short-form stories, editorial imagery and branded collaborations.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#131313` canvas, `#ffffff` ink, `#ff1053` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#131313` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#ff1053` accents.
  - **Grounded Typographic Hierarchy**: Uses `Monument` across display (`TOO LOUD`) and body copy, paired with `Andale Mono` for monospace/code.
  - **Calibrated Spatial Grid & Motion**: Combines `1280px` container bounds (`gap: 6px`, padding `25px`) with `cubic-bezier(.15,.75,.4,1)` easing and Lenis Smooth Scroll (`data-lenis`), Swiper Touch Carousel Engine.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=13095px` / doc `14247px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `1280px` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `25px` lateral canvas padding with `6px` grid gap.
- **Border Radius Scale**: `2px`, `10px`, `50%`, `4px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1280px`, `gap: 6px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `25px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:691px)`, `@media only screen and (min-width:1000px)`, `@media only screen and (max-width:999px) and (min-width:691px)`, `@media only screen and (max-width:690px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#131313` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#2c3338` | `#wpadminbar .shortlink-input { background: #2c3338 }` |
| **Interactive Accent / Highlight** | `#ff1053` | `var(--nectar-extra-color-gradient-1)` in `:root` |
| **Secondary / Muted Copy** | `#888888` | `gle #single-meta ul .meta-share... { color: #888888 }` |
| **Structural Hairline Border** | `#2c353b` | `#wp-admin-bar-my-account.with-a... { border: #2c353b }` |
| **Variable Token (`--nectar-extra-color-gradient-1`)** | `#3452ff` | `var(--nectar-extra-color-gradient-1)` in `:root` |
| **Variable Token (`--nectar-extra-color-gradient-2`)** | `#32d6ff` | `var(--nectar-extra-color-gradient-2)` in `:root` |
| **Variable Token (`--nectar-extra-color-gradient-2`)** | `#2ac4ea` | `var(--nectar-extra-color-gradient-2)` in `:root` |
| **Variable Token (`--nectar-extra-color-2`)** | `#bf7741` | `var(--nectar-extra-color-2)` in `:root` |
| **Variable Token (`--nectar-extra-color-3`)** | `#bb3a4e` | `var(--nectar-extra-color-3)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--wp--style--global--content-size` | `1300px` | Layout / Spatial Grid Token |
| `--wp--style--global--wide-size` | `1300px` | Layout / Spatial Grid Token |
| `--wp-admin--admin-bar--height` | `32px` | Layout / Spatial Grid Token |
| `--scroll-bar-w` | `-2px` | Dimension / Scale Token |
| `--nectar-font-light-color` | `#ffffff` | Canvas / Surface Token |
| `--page-color-change-section-transition-time` | `0.8s` | Brand / Palette Token |
| `--nectar-cubic-bezier-out` | `cubic-bezier(0.3, 1, 0.3, 1)` | Brand / Palette Token |
| `--nectar-cubic-bezier-in-out` | `cubic-bezier(0.76, 0, 0.24, 1)` | Brand / Palette Token |
| `--nectar-header-hover-timing` | `0.65s` | Brand / Palette Token |
| `--mobile-container-width` | `88%` | Layout / Spatial Grid Token |
| `--nectar-extra-color-gradient-1` | `linear-gradient(to right,#ff1053,#3452ff)` | Brand / Palette Token |
| `--nectar-extra-color-gradient-2` | `linear-gradient(to right,#32d6ff,#2AC4EA)` | Brand / Palette Token |
| `--nectar-accent-color` | `#ffffff` | Brand / Palette Token |
| `--nectar-extra-color-1` | `#131313` | Brand / Palette Token |
| `--nectar-extra-color-2` | `#bf7741` | Brand / Palette Token |
| `--nectar-extra-color-3` | `#bb3a4e` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Monument`.
- **Primary Body Stack**: `Monument`.
- **Technical / Metadata Stack**: `Andale Mono`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 201.6px`, `line-height: 161.28px`, `font-weight: 700`, `letter-spacing: -10.08px`); rule `h1` (`font-size: 44px`, `line-height: 54px`, `font-weight: 600`).
- **Section Heading (`H2`)**: live computed `h3 (primary section heading)` (`font-size: 26px`, `line-height: 26px`, `font-weight: 700`, `letter-spacing: -0.26px`); rule `h2` (`font-weight: 600`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 29px`, `font-weight: 400`); CSS variables `--nectar-body-line-height: 29px`, `--nectar-body-font-size: 16px`; rule `p` (`font-size: 1em`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 29px`, `font-weight: 400`); rule `.label` (`font-size: 14px`, `line-height: 1`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.15,.75,.4,1)`, `cubic-bezier(.19,1,.22,1)`, `cubic-bezier(0.3,1,0.3,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.wpb_column.boxed>.vc_column-inner`**: `transition: transform .2s ease,box-shadow .2s ease` extracted from `thecassandravale-com` stylesheet.
- **Selector `#wpadminbar *`**: `transition: none` extracted from `thecassandravale-com` stylesheet.
- **Selector `#wpadminbar .ab-item:before`**: `transition: color .1s ease-in-out` extracted from `thecassandravale-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.15,.75,.4,1)`)**: Governs interactive state transitions across `<header.js>` and `<div.home>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `14247px`, deepest scrollY reached `13095px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: `Lenis`.
- **Hover Physics (`primary_cta` · `INSTAGRAM`)**: Computed transition `0.2s, 0.2s` / `ease, ease` (no static color/transform shift captured at rest).

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Cassandra Vale · Fashion, Stories & Brande │
│ ====================================================================== │
│ [ <header.js> (1440x49px)             | Overview · Index · Archive · ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <div.lenis> (w=1440px)                                 | │
│ | H1: TOO LOUD                                                       | │
│ | Substrate: #131313 | Ink: #ffffff | Accent: #ff1053                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<div.home>) max-w: 1280px                           | │
│ | +------------------------------+  +------------------------------+ | │
│ | | SHE TAKES THE LONG WAY, THE  |  | TO MAKE IT WORTH SHOWING UP  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<div.wp-singular>) — ARTEM MARKOVSKY / ARC          | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.page-templat) | https://thecassandravale.com/        │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 6px)        │
│ ====================================================================== │
│ [ HEADER BAR (<header.js>             ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<div.lenis>) — 390px Vertical Lead                     | │
│ | H1: TOO LOUD                                                       | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<div.home>) — 1-Col Stack                          | │
│ | [ Item 1: SHE TAKES THE LONG WAY, THE FAST LANE, OR WHATEV       ] | │
│ | [ Item 2: TO MAKE IT WORTH SHOWING UP FOR.                       ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<div.wp-singular>) — 1-Col (ARTEM MARKOVSKY / )      | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.page-templat) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.js> — `thecassandravale-com`)**:
   - Landmark `<header class="js">` (`1440x49px`) hosting `Cassandra Vale · Fashion, Stories & ` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-pagespeed-no-defer`, `data-nowprocket`, `data-wpacu-skip`, `data-no-optimize`), and stylesheet rule `.col { position:relative;display:block;width:100% }`.
2. **Hero Stage & Focal Lead (<div.lenis> — `TOO LOUD`)**:
   - Landmark `<div class="lenis">` presenting display lead `TOO LOUD` and copy excerpt *"SHE TAKES THE LONG WAY, THE FAST LANE, OR WHATEVER MAKES A BETTER"* over `#131313` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<div.home> — `SHE TAKES THE LONG WAY, THE FAST L`)**:
   - Landmark `<div class="home">` rendering section `SHE TAKES THE LONG WAY, THE FAST LANE, OR WHATEV` with copy *"TO MAKE IT WORTH SHOWING UP FOR."*, asset references (`embed`, `icomoon.woff`, `HERO5_OPT-1024x768.jpg`, `HERO5_OPT.jpg`), and grid rule `html body .vc_row-fluid>.span_12 { display:flex;display:-ms-flexbox;-ms-flex-wrap:wrap;flex-wrap:wrap;float... }`.
4. **Interactive Detail & Feature Matrix (<div.wp-singular> — `TO MAKE IT WORTH SHOWING UP FOR.`)**:
   - Landmark `<div class="wp-singular">` framing `TO MAKE IT WORTH SHOWING UP FOR.` and `ARTEM MARKOVSKY / ARCR` (*"ARTEM MARKOVSKY / ARCR"*) with `#2c3338` surface cards, `#ff1053` accents, and `.col:last-child { margin-right:0 }`.
5. **Colophon & Global Directory Footer (<footer.page-template-default> — `https://thecassandravale.com/`)**:
   - Landmark `<footer class="page-template-default">` anchoring `Cassandra Vale · Fashion, Storie` footer links (`Overview · Index · Archive · About · Contact`), copy *"TO MAKE IT WORTH SHOWING UP FOR."*, and `#2c353b` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `Hero` · sticky/fixed elements: `1`
- **Step 02** (`y=850px`, `6%`): Active landmark `INSTAGRAM` · sticky/fixed elements: `1`
- **Step 03** (`y=3400px`, `26%`): Active landmark `SHE MOVES FIRST` · sticky/fixed elements: `1`
- **Step 04** (`y=5950px`, `45%`): Active landmark `SHE CUTS` · sticky/fixed elements: `1`
- **Step 05** (`y=7650px`, `57%`): Active landmark `IRON WILL` · sticky/fixed elements: `1`
- **Step 06** (`y=10200px`, `76%`): Active landmark `NOT EVERYTHING` · sticky/fixed elements: `1`
- **Step 07** (`y=12750px`, `96%`): Active landmark `EMAIL` · sticky/fixed elements: `1`
- **Step 08** (`y=13095px`, `98%`): Active landmark `EMAIL` · sticky/fixed elements: `1`

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: thecassandravale-com (Cassandra Vale · Fashion, Stories & Branded Content)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `thecassandravale-com` (**Cassandra Vale · Fashion, Stories & Branded Content** — `https://thecassandravale.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#131313` canvas, `#ffffff` ink, `#ff1053` accent).
- **Identity & Domain Context**: Cassandra Vale brings together fashion, short-form stories, editorial imagery and branded collaborations.
- **Primary Substrate**: `#131313` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#ffffff`, **Accent / Highlight**: `#ff1053`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#131313` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#ff1053` accents.
  - **Grounded Typographic Hierarchy**: Uses `Monument` across display (`TOO LOUD`) and body copy, paired with `Andale Mono` for monospace/code.
  - **Calibrated Spatial Grid & Motion**: Combines `1280px` container bounds (`gap: 6px`, padding `25px`) with `cubic-bezier(.15,.75,.4,1)` easing and Lenis Smooth Scroll (`data-lenis`), Swiper Touch Carousel Engine.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `thecassandravale-com` in your global stylesheet:

:root {
  /* Cassandra Vale · Fashion, Stories & Branded Content (thecassandravale-com) — Live-Grounded CSS Variables */
  --wp--style--global--content-size: 1300px; /* Layout / Spatial Grid Token (thecassandravale-com) */
  --wp--style--global--wide-size: 1300px; /* Layout / Spatial Grid Token (thecassandravale-com) */
  --wp-admin--admin-bar--height: 32px; /* Layout / Spatial Grid Token (thecassandravale-com) */
  --scroll-bar-w: -2px; /* Dimension / Scale Token (thecassandravale-com) */
  --nectar-font-light-color: #ffffff; /* Canvas / Surface Token (thecassandravale-com) */
  --page-color-change-section-transition-time: 0.8s; /* Brand / Palette Token (thecassandravale-com) */
  --nectar-cubic-bezier-out: cubic-bezier(0.3, 1, 0.3, 1); /* Brand / Palette Token (thecassandravale-com) */
  --nectar-cubic-bezier-in-out: cubic-bezier(0.76, 0, 0.24, 1); /* Brand / Palette Token (thecassandravale-com) */
  --nectar-header-hover-timing: 0.65s; /* Brand / Palette Token (thecassandravale-com) */
  --mobile-container-width: 88%; /* Layout / Spatial Grid Token (thecassandravale-com) */
  --nectar-extra-color-gradient-1: linear-gradient(to right,#ff1053,#3452ff); /* Brand / Palette Token (thecassandravale-com) */
  --nectar-extra-color-gradient-2: linear-gradient(to right,#32d6ff,#2AC4EA); /* Brand / Palette Token (thecassandravale-com) */
  --nectar-accent-color: #ffffff; /* Brand / Palette Token (thecassandravale-com) */
  --nectar-extra-color-1: #131313; /* Brand / Palette Token (thecassandravale-com) */
  --nectar-extra-color-2: #bf7741; /* Brand / Palette Token (thecassandravale-com) */
  --nectar-extra-color-3: #bb3a4e; /* Brand / Palette Token (thecassandravale-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#131313` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#ffffff` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#2c3338` — grounded in `#wpadminbar .shortlink-input { background: #2c3338 }`
- **Interactive Accent / Highlight**: `#ff1053` — grounded in `var(--nectar-extra-color-gradient-1)` in `:root`
- **Secondary / Muted Copy**: `#888888` — grounded in `gle #single-meta ul .meta-share... { color: #888888 }`
- **Structural Hairline Border**: `#2c353b` — grounded in `#wp-admin-bar-my-account.with-a... { border: #2c353b }`
- **Variable Token (`--nectar-extra-color-gradient-1`)**: `#3452ff` — grounded in `var(--nectar-extra-color-gradient-1)` in `:root`
- **Variable Token (`--nectar-extra-color-gradient-2`)**: `#32d6ff` — grounded in `var(--nectar-extra-color-gradient-2)` in `:root`
- **Variable Token (`--nectar-extra-color-gradient-2`)**: `#2ac4ea` — grounded in `var(--nectar-extra-color-gradient-2)` in `:root`
- **Variable Token (`--nectar-extra-color-2`)**: `#bf7741` — grounded in `var(--nectar-extra-color-2)` in `:root`
- **Variable Token (`--nectar-extra-color-3`)**: `#bb3a4e` — grounded in `var(--nectar-extra-color-3)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `1280px` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `25px` lateral canvas padding with `6px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1280px`, `gap: 6px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `25px` horizontal padding
- **Media Queries**: `@media (min-width:691px)`, `@media only screen and (min-width:1000px)`, `@media only screen and (max-width:999px) and (min-width:691px)`, `@media only screen and (max-width:690px)`
- **Corner Radii**: `2px`, `10px`, `50%`, `4px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Monument`
- **Body Font Stack**: `Monument`
- **Monospace / Technical Font Stack**: `Andale Mono`
- **H1 Display Rule**: live computed `h1` (`font-size: 201.6px`, `line-height: 161.28px`, `font-weight: 700`, `letter-spacing: -10.08px`); rule `h1` (`font-size: 44px`, `line-height: 54px`, `font-weight: 600`)
- **H2 Section Rule**: live computed `h3 (primary section heading)` (`font-size: 26px`, `line-height: 26px`, `font-weight: 700`, `letter-spacing: -0.26px`); rule `h2` (`font-weight: 600`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 29px`, `font-weight: 400`); CSS variables `--nectar-body-line-height: 29px`, `--nectar-body-font-size: 16px`; rule `p` (`font-size: 1em`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 29px`, `font-weight: 400`); rule `.label` (`font-size: 14px`, `line-height: 1`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `thecassandravale-com` (`Cassandra Vale · Fashion, Stories & Branded Content`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.js> — `thecassandravale-com`)**:
   - DOM & Selectors: Landmark `<header class="js">` (`1440x49px`) hosting `Cassandra Vale · Fashion, Stories & ` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-pagespeed-no-defer`, `data-nowprocket`, `data-wpacu-skip`, `data-no-optimize`), and stylesheet rule `.col { position:relative;display:block;width:100% }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.js> — `thecassandravale-com`)` (`thecassandravale-com`) adapts across `@media (min-width:691px)`, `@media only screen and (min-width:1000px)`, `@media only screen and (max-width:999px) and (min-width:691px)`, `@media only screen and (max-width:690px)` with `cubic-bezier(.15,.75,.4,1)`, `cubic-bezier(.19,1,.22,1)`, `cubic-bezier(0.3,1,0.3,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<div.lenis> — `TOO LOUD`)**:
   - DOM & Selectors: Landmark `<div class="lenis">` presenting display lead `TOO LOUD` and copy excerpt *"SHE TAKES THE LONG WAY, THE FAST LANE, OR WHATEVER MAKES A BETTER"* over `#131313` canvas and `#ffffff` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×2616px` mobile) sets `#131313` background with `#ffffff` headline `TOO LOUD`.
3. **Primary Showcase & Content Grid (<div.home> — `SHE TAKES THE LONG WAY, THE FAST L`)**:
   - DOM & Selectors: Landmark `<div class="home">` rendering section `SHE TAKES THE LONG WAY, THE FAST LANE, OR WHATEV` with copy *"TO MAKE IT WORTH SHOWING UP FOR."*, asset references (`embed`, `icomoon.woff`, `HERO5_OPT-1024x768.jpg`, `HERO5_OPT.jpg`), and grid rule `html body .vc_row-fluid>.span_12 { display:flex;display:-ms-flexbox;-ms-flex-wrap:wrap;flex-wrap:wrap;float... }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<div.home> — `SHE TAKES THE LONG WAY, THE FAST L`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1280px`, `gap: 6px`) on desktop and Single-column vertical stack at `390px` viewport width with `25px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<div.wp-singular> — `TO MAKE IT WORTH SHOWING UP FOR.`)**:
   - DOM & Selectors: Landmark `<div class="wp-singular">` framing `TO MAKE IT WORTH SHOWING UP FOR.` and `ARTEM MARKOVSKY / ARCR` (*"ARTEM MARKOVSKY / ARCR"*) with `#2c3338` surface cards, `#ff1053` accents, and `.col:last-child { margin-right:0 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<div.wp-singular> — `TO MAKE IT WORTH SHOWING UP FOR.`)` uses `2px`, `10px`, `50%`, `4px` radii, `#ff1053` highlights, and assets (embed, icomoon.woff, HERO5_OPT-1024x768.jpg).
5. **Colophon & Global Directory Footer (<footer.page-template-default> — `https://thecassandravale.com/`)**:
   - DOM & Selectors: Landmark `<footer class="page-template-default">` anchoring `Cassandra Vale · Fashion, Storie` footer links (`Overview · Index · Archive · About · Contact`), copy *"TO MAKE IT WORTH SHOWING UP FOR."*, and `#2c353b` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.page-template-default> — `https://thecassandravale.com/`)` aligns to `1280px` (non-`@media` desktop container stylesheet rule) with `25px` lateral canvas padding with `6px` grid gap and attributes (data-pagespeed-no-defer, data-nowprocket, data-wpacu-skip).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"SHE TAKES THE LONG WAY, THE FAST LANE, OR WHATEVER MAKES A BETTER STORY."*
- Copy Excerpt 2: *"TO MAKE IT WORTH SHOWING UP FOR."*
- Copy Excerpt 3: *"ARTEM MARKOVSKY / ARCR"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.15,.75,.4,1)`, `cubic-bezier(.19,1,.22,1)`, `cubic-bezier(0.3,1,0.3,1)`
- **Extracted Stylesheet Rules (`thecassandravale-com`)**:
- `.col { position:relative;display:block;width:100% }`
- `html body .vc_row-fluid>.span_12 { display:flex;display:-ms-flexbox;-ms-flex-wrap:wrap;flex-wrap:wrap;float... }`
- `.col:last-child { margin-right:0 }`
- `.col.col_last { margin-right:0 }`
- `body .vc_row-fluid>.span_12>.wpb_... { float:none;margin-right:0 }`
- **Per-Selector Transition Rules**:
- **Selector `.wpb_column.boxed>.vc_column-inner`**: `transition: transform .2s ease,box-shadow .2s ease` extracted from `thecassandravale-com` stylesheet.
- **Selector `#wpadminbar *`**: `transition: none` extracted from `thecassandravale-com` stylesheet.
- **Selector `#wpadminbar .ab-item:before`**: `transition: color .1s ease-in-out` extracted from `thecassandravale-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.15,.75,.4,1)`)**: Governs interactive state transitions across `<header.js>` and `<div.home>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `14247px` across 8 distinct viewport chapters using Lenis.
- **Vertical Chapter Sequence**: Hero (0%) -> INSTAGRAM (6%) -> SHE MOVES FIRST (26%) -> SHE CUTS (45%) -> IRON WILL (57%) -> NOT EVERYTHING (76%) -> EMAIL (96%) -> EMAIL (98%).

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `thecassandravale-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | Hero | `1` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `6%` | INSTAGRAM | `1` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `3400px` | `26%` | SHE MOVES FIRST | `1` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `5950px` | `45%` | SHE CUTS | `1` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `7650px` | `57%` | IRON WILL | `1` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `10200px` | `76%` | NOT EVERYTHING | `1` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `12750px` | `96%` | EMAIL | `1` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `13095px` | `98%` | EMAIL | `1` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | Hero | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `4504px` | `50%` | Section @ 50% | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `8851px` | `100%` | INSTAGRAM | [mobile-step-03.webp](assets/mobile-step-03.webp) |

