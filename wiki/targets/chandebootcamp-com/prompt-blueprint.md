---
title: "UI Prompt Blueprint: chandebootcamp-com"
date: 2026-11-24
captured_at: 2026-11-24
target: "chandebootcamp-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
capture_mode: behavioral_journey_v2
asset_format: webp
scroll_driver: native
desktop_keyframes: 8
subpages_crawled: 3
http_status: 200
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#f4f3eb` / `#236c3c`)"
---

# UI Design System & Master Generation Blueprint: chandebootcamp-com

> **Chande Bootcamp 2026 by Mingg Patreon - Design Community in Vietnam** (http://chandebootcamp.com/) — Chande Bootcamp by Mingg is a retreat that connects Vietnamese designers: three days to listen, share and show the love at Ke Retreat, Ha...

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Chande Bootcamp 2026 by Mingg Patreon - Design Community in Vietnam** (`http://chandebootcamp.com/`). Chande Bootcamp by Mingg is a retreat that connects Vietnamese designers: three days to listen, share and show the love at Ke Retreat, Ha...
- **Final Redirected URL**: [https://www.chandebootcamp.com/](https://www.chandebootcamp.com/)
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#f4f3eb` / `#236c3c`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f4f3eb` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#236c3c` accents.
  - **Grounded Typographic Hierarchy**: Uses `Phudu` across display (`CHANDE BOOTCAMP BY. MINGG`) and body copy, paired with `Geist Mono` for monospace/code.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 2px`, padding `var(--g3-gutter)`) with `cubic-bezier(.65,0,.25,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=14400px` / doc `15611px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport).
- **Canvas Lateral Padding & Spacing**: `var(--g3-gutter)` lateral canvas padding with `2px` grid gap.
- **Border Radius Scale**: `999px`, `10px`, `4px`, `99px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 2px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--g3-gutter)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:44em), (max-height:680px)`, `@media (max-width:44em)`, `@media (max-width:599px)`, `@media (prefers-reduced-motion:reduce)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f4f3eb` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f5f0e3` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#236c3c` | `.hs-foot__cta1 { background: #236c3c }` |
| **Secondary / Muted Copy** | `#838b89` | live computed `footer` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#cbcbc4` | `var(--line)` in `:root` (`rgba(15,21,19,.18)`) |
| **Variable Token (`--panel`)** | `#1b2625` | `var(--panel)` in `:root` |
| **Variable Token (`--green`)** | `#245535` | `var(--green)` in `:root` |
| **Variable Token (`--lime`)** | `#68f12b` | `var(--lime)` in `:root` |
| **Variable Token (`--ink`)** | `#0f1513` | `var(--ink)` in `:root` |
| **Variable Token (`--g3-floor`)** | `#f7f3ed` | `var(--g3-floor)` in `:root` |
| **Variable Token (`--g3-danger`)** | `#c4372b` | `var(--g3-danger)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--cream` | `#f4f3eb` | Color / Atmospheric Token |
| `--panel` | `#1b2625` | Color / Atmospheric Token |
| `--green` | `#245535` | Color / Atmospheric Token |
| `--lime` | `#68f12b` | Color / Atmospheric Token |
| `--ink` | `#0f1513` | Typography Ink Token |
| `--bar` | `5rem` | Dimension / Scale Token |
| `--g3-floor` | `#F7F3ED` | Color / Atmospheric Token |
| `--g3-ink` | `#0f1513` | Typography Ink Token |
| `--g3-green` | `#236c3c` | Color / Atmospheric Token |
| `--g3-lime` | `#68f12b` | Color / Atmospheric Token |
| `--g3-cream` | `#f4f3eb` | Color / Atmospheric Token |
| `--g3-danger` | `#c4372b` | Color / Atmospheric Token |
| `--g3-hair` | `rgba(15, 21, 19, .18)` | Color / Atmospheric Token |
| `--g3-mute` | `rgba(15, 21, 19, .55)` | Color / Atmospheric Token |
| `--g3-mono` | `'Geist Mono', ui-monospace, 'SFMono-Regular', Consolas, monospace` | Typography / Scale Token |
| `--g3-display` | `'Phudu', ui-sans-serif, system-ui, sans-serif` | Dimension / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Phudu`.
- **Primary Body Stack**: `Phudu`.
- **Technical / Metadata Stack**: `Geist Mono`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 80.0244px`, `line-height: 57.6176px`, `font-weight: 700`, `letter-spacing: -3.20098px`); CSS variables `--g3-display: 'Phudu', ui-sans-serif, system-ui, sans-serif`.
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 79.5px`, `line-height: 62.01px`, `font-weight: 700`, `letter-spacing: -3.18px`); rule `h2` (`letter-spacing: -.04em`).
- **Body Copy**: live computed `body` (`font-size: 12px`, `line-height: normal`, `font-weight: 600`); rule `body` (`font-weight: 600`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: 11.52px`, `font-weight: 500`, `letter-spacing: -0.24px`); CSS variables `--g3-mono: 'Geist Mono', ui-monospace, 'SFMono-Regular', Consolas, monospace`, `--mono: max(11px, calc(14 * var(--fu)))`; rule `.mono` (`line-height: .96`, `letter-spacing: -.02em`, `font-weight: 500`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.65,0,.25,1)`, `cubic-bezier(.65,0,.35,1)`, `cubic-bezier(.16,1,.3,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.g3-lb::before`**: `transition: opacity var(--lb-ms) ease` extracted from `chandebootcamp-com` stylesheet.
- **Selector `.g3-lb__frame`**: `transition: width .75s cubic-bezier(.65,0,.25,1), height .75s cubic-bez...` extracted from `chandebootcamp-com` stylesheet.
- **Selector `.g3-bar`**: `transition: opacity .3s ease, transform .3s ease` extracted from `chandebootcamp-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.65,0,.25,1)`)**: Governs interactive state transitions across `<nav.abs>` and `<section.hs>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `15611px`, deepest scrollY reached `14400px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: `Lenis`, `GSAP/ScrollTrigger`, `WebGL/Canvas`.
- **Nav / Drawer Probe (`Menu`)**: Triggered visual change (pixel diff `128.436`, captured in `assets/state-nav.webp`); revealed links: BECOME A PARTNER BECO..., REGISTER FOR THE NEXT..., FACEBOOK, YOUTUBE, INSTAGRAM, LINKEDIN.
- **Hover Physics (`first_card` · `05 TRONG MOTION`)**: Computed transition `0s` / `ease` (no static color/transform shift captured at rest).
- **Route Transition Architecture**: First internal navigation (`/about`) measured as `direct` in `3598ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Chande Bootcamp 2026 by Mingg Patreon - De │
│ ====================================================================== │
│ [ <nav.abs> (320x56px)                | Explore Gallery · About us   ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero> (w=1440px)                              | │
│ | H1: CHANDE BOOTCAMP BY. MINGG                                      | │
│ | Substrate: #f4f3eb | Ink: #000000 | Accent: #236c3c                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.hs>) max-w: 1440px                         | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Chande Bootcamp By. Mingg    |  | An event for all designers t | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.hs-story>) — (12) Events at bootca         | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.hs>         ) | http://chandebootcamp.com/           │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 2px)        │
│ ====================================================================== │
│ [ HEADER BAR (<nav.abs>               ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.hero>) — 390px Vertical Lead                  | │
│ | H1: CHANDE BOOTCAMP BY. MINGG                                      | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.hs>) — 1-Col Stack                        | │
│ | [ Item 1: Chande Bootcamp By. Mingg                              ] | │
│ | [ Item 2: An event for all designers to connect. Listen & s...   ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.hs-story>) — 1-Col ((12) Events at boo)     | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.hs>         ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.abs> — `chandebootcamp-com`)**:
   - Landmark `<nav class="abs pills">` (`320x56px`) hosting `Chande Bootcamp 2026 by Mingg Patreo` navigation (`Explore Gallery · About us`), DOM attributes (`data-chande-loading`, `data-chande-transition`, `data-barba="wrapper"`, `data-transition-wrap`), and stylesheet rule `.page--gallery { height:100vh; min-height:0; padding:0; overflow:hidden }`.
2. **Hero Stage & Focal Lead (<section.hero> — `CHANDE BOOTCAMP BY. MINGG`)**:
   - Landmark `<section class="hero">` presenting display lead `CHANDE BOOTCAMP BY. MINGG` and copy excerpt *"Special event organized by Mingg Patreon - Design community"* over `#f4f3eb` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.hs> — `Chande Bootcamp By. Mingg`)**:
   - Landmark `<section class="hs hs-intro">` rendering section `Chande Bootcamp By. Mingg` with copy *"2-4 October Ke Retreat - Hanoi, VN"*, asset references (`favicon.ico`, `favicon.svg`, `favicon-32.png`, `apple-touch-icon.png`), and grid rule `html.g3-on body { overflow:hidden; overscroll-behavior:none }`.
4. **Interactive Detail & Feature Matrix (<section.hs-story> — `An event for all designers to conn`)**:
   - Landmark `<section class="hs hs-story">` framing `An event for all designers to connect. Listen & s...` and `(12) Events at bootcamp` (*"A community connecting event for Vietnamese designers. In the mos"*) with `#f5f0e3` surface cards, `#236c3c` accents, and `after { box-sizing:border-box }`.
5. **Colophon & Global Directory Footer (<footer.hs> — `http://chandebootcamp.com/`)**:
   - Landmark `<footer class="hs hs-foot">` anchoring `Chande Bootcamp 2026 by Mingg Pa` footer links (`Explore Gallery · About us`), copy *"[ UIUX design community ]"*, and `#cbcbc4` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `CHANDE BOOTCAMP BY. MINGG` · sticky/fixed elements: `3`
- **Step 02** (`y=850px`, `6%`): Active landmark `AN EVENT FOR ALL DESIGNERS TO CONNECT. LISTEN & S...` · sticky/fixed elements: `3`
- **Step 03** (`y=3400px`, `23%`): Active landmark `Section @ 23%` · sticky/fixed elements: `4`
- **Step 04** (`y=5950px`, `40%`): Active landmark `Section @ 40%` · sticky/fixed elements: `3`
- **Step 05** (`y=8500px`, `58%`): Active landmark `(12) EVENTS AT BOOTCAMP` · sticky/fixed elements: `3`
- **Step 06** (`y=11050px`, `75%`): Active landmark `WAKE UP JOIN ME IN NATURE WORKSHOP-002: AI ERA BY...` · sticky/fixed elements: `4`
- **Step 07** (`y=13600px`, `92%`): Active landmark `Section @ 92%` · sticky/fixed elements: `2`
- **Step 08** (`y=14400px`, `98%`): Active landmark `Footer` · sticky/fixed elements: `2`

### Multi-Page Internal Route Map
- **About Route (`/about`)**: `https://www.chandebootcamp.com/about` — H1: `A DESIGN COMMUNITY THAT STANDS APART`, scrollHeight `10049px`, transition `direct` (`3598ms`)
- **Other Route (`/gallery`)**: `https://www.chandebootcamp.com/gallery` — H1: `GALLERY — PHOTOS FROM CHANDE BOOTCAMP`, scrollHeight `900px`, transition `direct` (`7032ms`)
- **Other Route (`/partner`)**: `https://www.chandebootcamp.com/partner` — H1: `BECOME A PARTNER`, scrollHeight `900px`, transition `direct` (`2635ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: chandebootcamp-com (Chande Bootcamp 2026 by Mingg Patreon - Design Community in Vietnam)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `chandebootcamp-com` (**Chande Bootcamp 2026 by Mingg Patreon - Design Community in Vietnam** — `http://chandebootcamp.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f4f3eb` / `#236c3c`).
- **Identity & Domain Context**: Chande Bootcamp by Mingg is a retreat that connects Vietnamese designers: three days to listen, share and show the love at Ke Retreat, Ha...
- **Primary Substrate**: `#f4f3eb` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#000000`, **Accent / Highlight**: `#236c3c`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f4f3eb` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#236c3c` accents.
  - **Grounded Typographic Hierarchy**: Uses `Phudu` across display (`CHANDE BOOTCAMP BY. MINGG`) and body copy, paired with `Geist Mono` for monospace/code.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 2px`, padding `var(--g3-gutter)`) with `cubic-bezier(.65,0,.25,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `chandebootcamp-com` in your global stylesheet:

:root {
  /* Chande Bootcamp 2026 by Mingg Patreon - Design Community in Vietnam (chandebootcamp-com) — Live-Grounded CSS Variables */
  --cream: #f4f3eb; /* Color / Atmospheric Token (chandebootcamp-com) */
  --panel: #1b2625; /* Color / Atmospheric Token (chandebootcamp-com) */
  --green: #245535; /* Color / Atmospheric Token (chandebootcamp-com) */
  --lime: #68f12b; /* Color / Atmospheric Token (chandebootcamp-com) */
  --ink: #0f1513; /* Typography Ink Token (chandebootcamp-com) */
  --bar: 5rem; /* Dimension / Scale Token (chandebootcamp-com) */
  --g3-floor: #F7F3ED; /* Color / Atmospheric Token (chandebootcamp-com) */
  --g3-ink: #0f1513; /* Typography Ink Token (chandebootcamp-com) */
  --g3-green: #236c3c; /* Color / Atmospheric Token (chandebootcamp-com) */
  --g3-lime: #68f12b; /* Color / Atmospheric Token (chandebootcamp-com) */
  --g3-cream: #f4f3eb; /* Color / Atmospheric Token (chandebootcamp-com) */
  --g3-danger: #c4372b; /* Color / Atmospheric Token (chandebootcamp-com) */
  --g3-hair: rgba(15, 21, 19, .18); /* Color / Atmospheric Token (chandebootcamp-com) */
  --g3-mute: rgba(15, 21, 19, .55); /* Color / Atmospheric Token (chandebootcamp-com) */
  --g3-mono: 'Geist Mono', ui-monospace, 'SFMono-Regular', Consolas, monospace; /* Typography / Scale Token (chandebootcamp-com) */
  --g3-display: 'Phudu', ui-sans-serif, system-ui, sans-serif; /* Dimension / Scale Token (chandebootcamp-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f4f3eb` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#000000` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#f5f0e3` — grounded in live computed `button` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#236c3c` — grounded in `.hs-foot__cta1 { background: #236c3c }`
- **Secondary / Muted Copy**: `#838b89` — grounded in live computed `footer` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#cbcbc4` — grounded in `var(--line)` in `:root` (`rgba(15,21,19,.18)`)
- **Variable Token (`--panel`)**: `#1b2625` — grounded in `var(--panel)` in `:root`
- **Variable Token (`--green`)**: `#245535` — grounded in `var(--green)` in `:root`
- **Variable Token (`--lime`)**: `#68f12b` — grounded in `var(--lime)` in `:root`
- **Variable Token (`--ink`)**: `#0f1513` — grounded in `var(--ink)` in `:root`
- **Variable Token (`--g3-floor`)**: `#f7f3ed` — grounded in `var(--g3-floor)` in `:root`
- **Variable Token (`--g3-danger`)**: `#c4372b` — grounded in `var(--g3-danger)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport)
- **Padding & Gutters**: `var(--g3-gutter)` lateral canvas padding with `2px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 2px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--g3-gutter)` horizontal padding
- **Media Queries**: `@media (max-width:44em), (max-height:680px)`, `@media (max-width:44em)`, `@media (max-width:599px)`, `@media (prefers-reduced-motion:reduce)`
- **Corner Radii**: `999px`, `10px`, `4px`, `99px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Phudu`
- **Body Font Stack**: `Phudu`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **H1 Display Rule**: live computed `h1` (`font-size: 80.0244px`, `line-height: 57.6176px`, `font-weight: 700`, `letter-spacing: -3.20098px`); CSS variables `--g3-display: 'Phudu', ui-sans-serif, system-ui, sans-serif`
- **H2 Section Rule**: live computed `h2` (`font-size: 79.5px`, `line-height: 62.01px`, `font-weight: 700`, `letter-spacing: -3.18px`); rule `h2` (`letter-spacing: -.04em`)
- **Body Copy Rule**: live computed `body` (`font-size: 12px`, `line-height: normal`, `font-weight: 600`); rule `body` (`font-weight: 600`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 12px`, `line-height: 11.52px`, `font-weight: 500`, `letter-spacing: -0.24px`); CSS variables `--g3-mono: 'Geist Mono', ui-monospace, 'SFMono-Regular', Consolas, monospace`, `--mono: max(11px, calc(14 * var(--fu)))`; rule `.mono` (`line-height: .96`, `letter-spacing: -.02em`, `font-weight: 500`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `chandebootcamp-com` (`Chande Bootcamp 2026 by Mingg Patreon - Design Community in Vietnam`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.abs> — `chandebootcamp-com`)**:
   - DOM & Selectors: Landmark `<nav class="abs pills">` (`320x56px`) hosting `Chande Bootcamp 2026 by Mingg Patreo` navigation (`Explore Gallery · About us`), DOM attributes (`data-chande-loading`, `data-chande-transition`, `data-barba="wrapper"`, `data-transition-wrap`), and stylesheet rule `.page--gallery { height:100vh; min-height:0; padding:0; overflow:hidden }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.abs> — `chandebootcamp-com`)` (`chandebootcamp-com`) adapts across `@media (max-width:44em), (max-height:680px)`, `@media (max-width:44em)`, `@media (max-width:599px)`, `@media (prefers-reduced-motion:reduce)` with `cubic-bezier(.65,0,.25,1)`, `cubic-bezier(.65,0,.35,1)`, `cubic-bezier(.16,1,.3,1)` transitions and links `Explore Gallery · About us`.
2. **Hero Stage & Focal Lead (<section.hero> — `CHANDE BOOTCAMP BY. MINGG`)**:
   - DOM & Selectors: Landmark `<section class="hero">` presenting display lead `CHANDE BOOTCAMP BY. MINGG` and copy excerpt *"Special event organized by Mingg Patreon - Design community"* over `#f4f3eb` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×2616px` mobile) sets `#f4f3eb` background with `#000000` headline `CHANDE BOOTCAMP BY. MINGG`.
3. **Primary Showcase & Content Grid (<section.hs> — `Chande Bootcamp By. Mingg`)**:
   - DOM & Selectors: Landmark `<section class="hs hs-intro">` rendering section `Chande Bootcamp By. Mingg` with copy *"2-4 October Ke Retreat - Hanoi, VN"*, asset references (`favicon.ico`, `favicon.svg`, `favicon-32.png`, `apple-touch-icon.png`), and grid rule `html.g3-on body { overflow:hidden; overscroll-behavior:none }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.hs> — `Chande Bootcamp By. Mingg`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 2px`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--g3-gutter)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.hs-story> — `An event for all designers to conn`)**:
   - DOM & Selectors: Landmark `<section class="hs hs-story">` framing `An event for all designers to connect. Listen & s...` and `(12) Events at bootcamp` (*"A community connecting event for Vietnamese designers. In the mos"*) with `#f5f0e3` surface cards, `#236c3c` accents, and `after { box-sizing:border-box }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.hs-story> — `An event for all designers to conn`)` uses `999px`, `10px`, `4px`, `99px` radii, `#236c3c` highlights, and assets (favicon.ico, favicon.svg, favicon-32.png).
5. **Colophon & Global Directory Footer (<footer.hs> — `http://chandebootcamp.com/`)**:
   - DOM & Selectors: Landmark `<footer class="hs hs-foot">` anchoring `Chande Bootcamp 2026 by Mingg Pa` footer links (`Explore Gallery · About us`), copy *"[ UIUX design community ]"*, and `#cbcbc4` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.hs> — `http://chandebootcamp.com/`)` aligns to `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport) with `var(--g3-gutter)` lateral canvas padding with `2px` grid gap and attributes (data-chande-loading, data-chande-transition, data-barba="wrapper").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Special event organized by Mingg Patreon - Design community"*
- Copy Excerpt 2: *"2-4 October Ke Retreat - Hanoi, VN"*
- Copy Excerpt 3: *"A community connecting event for Vietnamese designers. In the most peaceful way."*
- Copy Excerpt 4: *"[ UIUX design community ]"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.65,0,.25,1)`, `cubic-bezier(.65,0,.35,1)`, `cubic-bezier(.16,1,.3,1)`
- **Extracted Stylesheet Rules (`chandebootcamp-com`)**:
- `.page--gallery { height:100vh; min-height:0; padding:0; overflow:hidden }`
- `html.g3-on body { overflow:hidden; overscroll-behavior:none }`
- `after { box-sizing:border-box }`
- `.g3-stage canvas { display:block; width:100%; height:100%; touch-action:none; cursor:grab }`
- `.g3-card { position:absolute; inset:0; transform-style:preserve-3d }`
- **Per-Selector Transition Rules**:
- **Selector `.g3-lb::before`**: `transition: opacity var(--lb-ms) ease` extracted from `chandebootcamp-com` stylesheet.
- **Selector `.g3-lb__frame`**: `transition: width .75s cubic-bezier(.65,0,.25,1), height .75s cubic-bez...` extracted from `chandebootcamp-com` stylesheet.
- **Selector `.g3-bar`**: `transition: opacity .3s ease, transform .3s ease` extracted from `chandebootcamp-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.65,0,.25,1)`)**: Governs interactive state transitions across `<nav.abs>` and `<section.hs>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `15611px` across 8 distinct viewport chapters using Lenis, GSAP/ScrollTrigger, WebGL/Canvas.
- **Vertical Chapter Sequence**: CHANDE BOOTCAMP BY. MINGG (0%) -> AN EVENT FOR ALL DESIGNERS... (6%) -> Section @ 23% (23%) -> Section @ 40% (40%) -> (12) EVENTS AT BOOTCAMP (58%) -> WAKE UP JOIN ME IN NATURE W... (75%) -> Section @ 92% (92%) -> Footer (98%).
- **Navigation Drawer / Menu State**: Replicate interactive menu toggle (`Menu`) with Escape-to-close keyboard handling.
- **Multi-Page Routes**: Scaffold internal routes `/about` (about, direct), `/gallery` (other, direct), `/partner` (other, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `chandebootcamp-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | CHANDE BOOTCAMP BY. MINGG | `3` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `6%` | AN EVENT FOR ALL DESIGNERS TO CONNECT. LISTEN... | `3` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `3400px` | `23%` | Section @ 23% | `4` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `5950px` | `40%` | Section @ 40% | `3` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `8500px` | `58%` | (12) EVENTS AT BOOTCAMP | `3` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `11050px` | `75%` | WAKE UP JOIN ME IN NATURE WORKSHOP-002: AI ER... | `4` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `13600px` | `92%` | Section @ 92% | `2` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `14400px` | `98%` | Footer | `2` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | CHANDE BOOTCAMP BY. MINGG | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `7200px` | `50%` | Section @ 38% | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `14400px` | `100%` | EXCHANGE MEMORY GIFTS FAREWELL GET BACK -... | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Interactive UI State Captures (`1440×900` WebP)
| State Type | Trigger / Observation | Visual Asset |
| :--- | :--- | :--- |
| `nav_menu` | Nav/Menu opened (`Menu`, diff `128.436`) | [state-nav.webp](assets/state-nav.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `about` | `https://www.chandebootcamp.com/about` | A DESIGN COMMUNITY THAT STANDS APART | `10049px` | `direct` (`3598ms`) | [subpage-01-about.webp](assets/subpage-01-about.webp) |
| `2` | `other` | `https://www.chandebootcamp.com/gallery` | GALLERY — PHOTOS FROM CHANDE BOOTCAMP | `900px` | `direct` (`7032ms`) | [subpage-02-gallery.webp](assets/subpage-02-gallery.webp) |
| `3` | `other` | `https://www.chandebootcamp.com/partner` | BECOME A PARTNER | `900px` | `direct` (`2635ms`) | [subpage-03-partner.webp](assets/subpage-03-partner.webp) |

