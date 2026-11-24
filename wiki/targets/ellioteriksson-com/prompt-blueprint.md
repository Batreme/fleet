---
title: "UI Prompt Blueprint: ellioteriksson-com"
date: 2026-11-24
captured_at: 2026-11-24
target: "ellioteriksson-com"
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
archetype: "Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#0c0c0c` ink, `#c6f432` accent)"
---

# UI Design System & Master Generation Blueprint: ellioteriksson-com

> **Elliot Eriksson — UI/UX, web & brand design, Stockholm & Åland** (https://ellioteriksson.com/) — Elliot Eriksson is a design technologist in Stockholm, designing clear, accessible websites and interfaces from first sketch to final pol...

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x1744)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Elliot Eriksson — UI/UX, web & brand design, Stockholm & Åland** (`https://ellioteriksson.com/`). Elliot Eriksson is a design technologist in Stockholm, designing clear, accessible websites and interfaces from first sketch to final pol...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#0c0c0c` ink, `#c6f432` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#0c0c0c` primary typography and `#c6f432` accents.
  - **Grounded Typographic Hierarchy**: Uses `Geist` across display (`I’m elliot, an award winning design `) and body copy, paired with `Geist Mono` for monospace/code.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 6px`, padding `5px`) with `cubic-bezier(.19,1,.22,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=6522px` / doc `7424px`), Mobile `390×1744px` (`assets/mobile-journey.webp`, `2` keyframes).
- **Master Container Bounds**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport).
- **Canvas Lateral Padding & Spacing**: `5px` lateral canvas padding with `6px` grid gap.
- **Border Radius Scale**: `999px`, `0px 0px 12px 12px`, `6px`, `var(--radius-img)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 6px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `5px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (prefers-reduced-motion:no-preference)`, `@media (max-width:767px)`, `@media (min-width:1024px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0c0c0c` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f3f3f3` | `var(--surface)` in `:root` |
| **Interactive Accent / Highlight** | `#c6f432` | `var(--accent)` in `:root` |
| **Secondary / Muted Copy** | `#6b6b6b` | `var(--muted)` in `:root` |
| **Structural Hairline Border** | `#e1e1e1` | `var(--rule)` in `:root` (`0c0c0c1f`) |
| **Variable Token (`--kind-client`)** | `#ff6fae` | `var(--kind-client)` in `:root` |
| **Variable Token (`--kind-personal`)** | `#ff5a36` | `var(--kind-personal)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--accent` | `#c6f432` | Brand / Palette Token |
| `--on-accent` | `#0c0c0c` | Brand / Palette Token |
| `--highlight` | `#c6f432` | Canvas / Surface Token |
| `--on-highlight` | `#0c0c0c` | Canvas / Surface Token |
| `--kind-agency` | `var(--highlight)` | Design System Custom Token |
| `--kind-client` | `#ff6fae` | Color / Atmospheric Token |
| `--kind-personal` | `#ff5a36` | Color / Atmospheric Token |
| `--font-wordmark` | `var(--font-wordmark-face,"Gossip"), Georgia, serif` | Typography / Scale Token |
| `--font-mono` | `var(--font-mono-face,"Geist Mono"), ui-monospace, Menlo, monospace` | Typography / Scale Token |
| `--gutter` | `3vw` | Layout / Spatial Grid Token |
| `--gap` | `11px` | Layout / Spatial Grid Token |
| `--header-h` | `52px` | Layout / Spatial Grid Token |
| `--section` | `clamp(96px, 11vw, 180px)` | Dimension / Scale Token |
| `--fs-body` | `16px` | Dimension / Scale Token |
| `--fs-md` | `clamp(20px, 1.8vw, 30px)` | Dimension / Scale Token |
| `--fs-lg` | `clamp(24px, 2.4vw, 40px)` | Dimension / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Geist`.
- **Primary Body Stack**: `Geist`.
- **Technical / Metadata Stack**: `Geist Mono`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 37.44px`, `line-height: 38.9376px`, `font-weight: 400`, `letter-spacing: -1.3104px`); CSS variables `--fs-display: clamp(36px, 4vw, 72px)`.
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 57.6px`, `line-height: 59.904px`, `font-weight: 400`, `letter-spacing: -2.592px`); CSS variables `--fs-lg: clamp(24px, 2.4vw, 40px)`.
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 23.2px`, `font-weight: 400`, `letter-spacing: -0.16px`); CSS variables `--fs-body: 16px`.
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 23.2px`, `font-weight: 400`, `letter-spacing: -0.16px`); CSS variables `--font-mono: var(--font-mono-face,"Geist Mono"), ui-monospace, Menlo, monospace`, `--font-mono-face: "Geist Mono", "Geist Mono Fallback"`; rule `,.mono` (`font-size: 12px`, `line-height: 1.4`, `letter-spacing: .02em`, `font-weight: 400`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.19,1,.22,1)`, `cubic-bezier(.76,0,.24,1)`, `cubic-bezier(.16,1,.3,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.arrow-link`**: `transition: color .3s` extracted from `ellioteriksson-com` stylesheet.
- **Selector `.icon`**: `transition: transform .4s var(--ease-out)` extracted from `ellioteriksson-com` stylesheet.
- **Selector `.skip-link`**: `transition: transform .2s` extracted from `ellioteriksson-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.19,1,.22,1)`)**: Governs interactive state transitions across `<header.site-header>` and `<section.showcase>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `7424px`, deepest scrollY reached `6522px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: Native browser scroll / standard CSS transitions.
- **Hover Physics (`primary_cta` · `elliot eriksson elliot eriksson`)**: Computed transition `0s` / `ease` (no static color/transform shift captured at rest).
- **Hover Physics (`first_card` · `iris-card`)**: `transform`: `matrix(0.89094, 0, 0, 0...` -> `matrix(0.929883, 0, 0,...`; `opacity`: `0.795074` -> `0.868254` (`transition-duration: 0s`, `timing: ease`).
- **Route Transition Architecture**: First internal navigation (`/cases`) measured as `SPA` in `1663ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Elliot Eriksson — UI/UX, web & brand desig │
│ ====================================================================== │
│ [ <header.site-header> (1440x53px)    | Home H o m e · Cases C a s e ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero> (w=1440px)                              | │
│ | H1: I’m elliot, an award winning design technologist...            | │
│ | Substrate: #ffffff | Ink: #0c0c0c | Accent: #c6f432                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.showcase>) max-w: 1440px                   | │
│ | +------------------------------+  +------------------------------+ | │
│ | | I’m Elliot , an award winnin |  | Selected work Selected work  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.projects>) — More projects                 | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer>) | https://ellioteriksson.com/          │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 6px)        │
│ ====================================================================== │
│ [ HEADER BAR (<header.site-header>    ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.hero>) — 390px Vertical Lead                  | │
│ | H1: I’m elliot, an award winning design technologist...            | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.showcase>) — 1-Col Stack                  | │
│ | [ Item 1: I’m Elliot , an award winning design technologist...   ] | │
│ | [ Item 2: Selected work Selected work                            ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.projects>) — 1-Col (More projects)          | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer>) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.site-header> — `ellioteriksson-com`)**:
   - Landmark `<header class="site-header">` (`1440x53px`) hosting `Elliot Eriksson — UI/UX, web & brand` navigation (`Home H o m e · Cases C a s e s · EN E N – English · SV S V – Svenska`), DOM attributes (`data-precedence="next"`, `data-href="/_next/static/immutab..."`, `data-sdkn="@vercel/analytics/next"`, `data-sdkv="2.0.1"`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.hero> — `I’m elliot, an award winning desig`)**:
   - Landmark `<section class="hero">` presenting display lead `I’m elliot, an award winning design technologist...` and copy excerpt *"CURRENTLY IN STOCKHOLM14:22"* over `#ffffff` canvas and `#0c0c0c` ink.
3. **Primary Showcase & Content Grid (<section.showcase> — `I’m Elliot , an award winning desi`)**:
   - Landmark `<section class="showcase showcase--roomy">` rendering section `I’m Elliot , an award winning design technologist...` with copy *"Design technologist"*, asset references (`1dm-4pi_h5ujm.js`, `41lrt_djk18al.js`, `1x62cbew_54xo.js`, `2jqd0dpb7brv_.js`), and grid rule `img { max-width:100%;height:auto;display:block }`.
4. **Interactive Detail & Feature Matrix (<section.projects> — `Selected work Selected work`)**:
   - Landmark `<section class="projects">` framing `Selected work Selected work` and `More projects` (*"Based in Stockholm B a s e d i n S t o c k h o l m"*) with `#f3f3f3` surface cards, `#c6f432` accents, and `button { font:inherit;letter-spacing:inherit;color:inherit;cursor:pointer;backgro... }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://ellioteriksson.com/`)**:
   - Landmark `<footer class="site-footer">` anchoring `Elliot Eriksson — UI/UX, web & b` footer links (`Home H o m e · Cases C a s e s · EN E N – English · SV S V – Svenska`), copy *"Based in Stockholm"*, and `#e1e1e1` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `I’m elliot, an award winning design technologist...` · sticky/fixed elements: `1`
- **Step 02** (`y=850px`, `13%`): Active landmark `Selected work Selected work` · sticky/fixed elements: `1`
- **Step 03** (`y=1700px`, `26%`): Active landmark `MORE PROJECTS` · sticky/fixed elements: `1`
- **Step 04** (`y=2550px`, `39%`): Active landmark `Pilates Plus` · sticky/fixed elements: `1`
- **Step 05** (`y=4250px`, `65%`): Active landmark `Brand & identity` · sticky/fixed elements: `1`
- **Step 06** (`y=5100px`, `78%`): Active landmark `Portfolio` · sticky/fixed elements: `1`
- **Step 07** (`y=5950px`, `91%`): Active landmark `LET’S TALK LET’S TALK` · sticky/fixed elements: `1`
- **Step 08** (`y=6522px`, `100%`): Active landmark `Footer` · sticky/fixed elements: `1`

### Multi-Page Internal Route Map
- **Listing Route (`/cases`)**: `https://ellioteriksson.com/cases` — H1: `Case studies Case staxkgs`, scrollHeight `3495px`, transition `SPA` (`1663ms`)
- **Detail Route (`/case/the-stash`)**: `https://ellioteriksson.com/case/the-stash` — H1: `Everything the team knows, one search away. Every...`, scrollHeight `8510px`, transition `direct` (`598ms`)
- **About Route (`/contact`)**: `https://ellioteriksson.com/contact` — H1: `Let’s talk Let’s talk`, scrollHeight `1877px`, transition `direct` (`341ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: ellioteriksson-com (Elliot Eriksson — UI/UX, web & brand design, Stockholm & Åland)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `ellioteriksson-com` (**Elliot Eriksson — UI/UX, web & brand design, Stockholm & Åland** — `https://ellioteriksson.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#0c0c0c` ink, `#c6f432` accent).
- **Identity & Domain Context**: Elliot Eriksson is a design technologist in Stockholm, designing clear, accessible websites and interfaces from first sketch to final pol...
- **Primary Substrate**: `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#0c0c0c`, **Accent / Highlight**: `#c6f432`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#0c0c0c` primary typography and `#c6f432` accents.
  - **Grounded Typographic Hierarchy**: Uses `Geist` across display (`I’m elliot, an award winning design `) and body copy, paired with `Geist Mono` for monospace/code.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 6px`, padding `5px`) with `cubic-bezier(.19,1,.22,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `ellioteriksson-com` in your global stylesheet:

:root {
  /* Elliot Eriksson — UI/UX, web & brand design, Stockholm & Åland (ellioteriksson-com) — Live-Grounded CSS Variables */
  --accent: #c6f432; /* Brand / Palette Token (ellioteriksson-com) */
  --on-accent: #0c0c0c; /* Brand / Palette Token (ellioteriksson-com) */
  --highlight: #c6f432; /* Canvas / Surface Token (ellioteriksson-com) */
  --on-highlight: #0c0c0c; /* Canvas / Surface Token (ellioteriksson-com) */
  --kind-agency: var(--highlight); /* Design System Custom Token (ellioteriksson-com) */
  --kind-client: #ff6fae; /* Color / Atmospheric Token (ellioteriksson-com) */
  --kind-personal: #ff5a36; /* Color / Atmospheric Token (ellioteriksson-com) */
  --font-wordmark: var(--font-wordmark-face,"Gossip"), Georgia, serif; /* Typography / Scale Token (ellioteriksson-com) */
  --font-mono: var(--font-mono-face,"Geist Mono"), ui-monospace, Menlo, monospace; /* Typography / Scale Token (ellioteriksson-com) */
  --gutter: 3vw; /* Layout / Spatial Grid Token (ellioteriksson-com) */
  --gap: 11px; /* Layout / Spatial Grid Token (ellioteriksson-com) */
  --header-h: 52px; /* Layout / Spatial Grid Token (ellioteriksson-com) */
  --section: clamp(96px, 11vw, 180px); /* Dimension / Scale Token (ellioteriksson-com) */
  --fs-body: 16px; /* Dimension / Scale Token (ellioteriksson-com) */
  --fs-md: clamp(20px, 1.8vw, 30px); /* Dimension / Scale Token (ellioteriksson-com) */
  --fs-lg: clamp(24px, 2.4vw, 40px); /* Dimension / Scale Token (ellioteriksson-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#0c0c0c` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#f3f3f3` — grounded in `var(--surface)` in `:root`
- **Interactive Accent / Highlight**: `#c6f432` — grounded in `var(--accent)` in `:root`
- **Secondary / Muted Copy**: `#6b6b6b` — grounded in `var(--muted)` in `:root`
- **Structural Hairline Border**: `#e1e1e1` — grounded in `var(--rule)` in `:root` (`0c0c0c1f`)
- **Variable Token (`--kind-client`)**: `#ff6fae` — grounded in `var(--kind-client)` in `:root`
- **Variable Token (`--kind-personal`)**: `#ff5a36` — grounded in `var(--kind-personal)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×1744px` (full-page live capture (1744px), `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport)
- **Padding & Gutters**: `5px` lateral canvas padding with `6px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 6px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `5px` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (prefers-reduced-motion:no-preference)`, `@media (max-width:767px)`, `@media (min-width:1024px)`
- **Corner Radii**: `999px`, `0px 0px 12px 12px`, `6px`, `var(--radius-img)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Geist`
- **Body Font Stack**: `Geist`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **H1 Display Rule**: live computed `h1` (`font-size: 37.44px`, `line-height: 38.9376px`, `font-weight: 400`, `letter-spacing: -1.3104px`); CSS variables `--fs-display: clamp(36px, 4vw, 72px)`
- **H2 Section Rule**: live computed `h2` (`font-size: 57.6px`, `line-height: 59.904px`, `font-weight: 400`, `letter-spacing: -2.592px`); CSS variables `--fs-lg: clamp(24px, 2.4vw, 40px)`
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 23.2px`, `font-weight: 400`, `letter-spacing: -0.16px`); CSS variables `--fs-body: 16px`
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 23.2px`, `font-weight: 400`, `letter-spacing: -0.16px`); CSS variables `--font-mono: var(--font-mono-face,"Geist Mono"), ui-monospace, Menlo, monospace`, `--font-mono-face: "Geist Mono", "Geist Mono Fallback"`; rule `,.mono` (`font-size: 12px`, `line-height: 1.4`, `letter-spacing: .02em`, `font-weight: 400`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `ellioteriksson-com` (`Elliot Eriksson — UI/UX, web & brand design, Stockholm & Åland`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.site-header> — `ellioteriksson-com`)**:
   - DOM & Selectors: Landmark `<header class="site-header">` (`1440x53px`) hosting `Elliot Eriksson — UI/UX, web & brand` navigation (`Home H o m e · Cases C a s e s · EN E N – English · SV S V – Svenska`), DOM attributes (`data-precedence="next"`, `data-href="/_next/static/immutab..."`, `data-sdkn="@vercel/analytics/next"`, `data-sdkv="2.0.1"`), and stylesheet rule `after { box-sizing:border-box }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.site-header> — `ellioteriksson-com`)` (`ellioteriksson-com`) adapts across `@media (prefers-reduced-motion:reduce)`, `@media (prefers-reduced-motion:no-preference)`, `@media (max-width:767px)`, `@media (min-width:1024px)` with `cubic-bezier(.19,1,.22,1)`, `cubic-bezier(.76,0,.24,1)`, `cubic-bezier(.16,1,.3,1)` transitions and links `Home H o m e · Cases C a s e s · EN E N – English · SV S V – Svenska`.
2. **Hero Stage & Focal Lead (<section.hero> — `I’m elliot, an award winning desig`)**:
   - DOM & Selectors: Landmark `<section class="hero">` presenting display lead `I’m elliot, an award winning design technologist...` and copy excerpt *"CURRENTLY IN STOCKHOLM14:22"* over `#ffffff` canvas and `#0c0c0c` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×1744px` mobile) sets `#ffffff` background with `#0c0c0c` headline `I’m elliot, an award winning design technologist...`.
3. **Primary Showcase & Content Grid (<section.showcase> — `I’m Elliot , an award winning desi`)**:
   - DOM & Selectors: Landmark `<section class="showcase showcase--roomy">` rendering section `I’m Elliot , an award winning design technologist...` with copy *"Design technologist"*, asset references (`1dm-4pi_h5ujm.js`, `41lrt_djk18al.js`, `1x62cbew_54xo.js`, `2jqd0dpb7brv_.js`), and grid rule `img { max-width:100%;height:auto;display:block }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.showcase> — `I’m Elliot , an award winning desi`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 6px`) on desktop and Single-column vertical stack at `390px` viewport width with `5px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.projects> — `Selected work Selected work`)**:
   - DOM & Selectors: Landmark `<section class="projects">` framing `Selected work Selected work` and `More projects` (*"Based in Stockholm B a s e d i n S t o c k h o l m"*) with `#f3f3f3` surface cards, `#c6f432` accents, and `button { font:inherit;letter-spacing:inherit;color:inherit;cursor:pointer;backgro... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.projects> — `Selected work Selected work`)` uses `999px`, `0px 0px 12px 12px`, `6px`, `var(--radius-img)` radii, `#c6f432` highlights, and assets (1dm-4pi_h5ujm.js, 41lrt_djk18al.js, 1x62cbew_54xo.js).
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://ellioteriksson.com/`)**:
   - DOM & Selectors: Landmark `<footer class="site-footer">` anchoring `Elliot Eriksson — UI/UX, web & b` footer links (`Home H o m e · Cases C a s e s · EN E N – English · SV S V – Svenska`), copy *"Based in Stockholm"*, and `#e1e1e1` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.site-footer> — `https://ellioteriksson.com/`)` aligns to `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport) with `5px` lateral canvas padding with `6px` grid gap and attributes (data-precedence="next", data-href="/_next/static/immutab...", data-sdkn="@vercel/analytics/next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"CURRENTLY IN STOCKHOLM14:22"*
- Copy Excerpt 2: *"Design technologist"*
- Copy Excerpt 3: *"Based in Stockholm B a s e d i n S t o c k h o l m"*
- Copy Excerpt 4: *"Based in Stockholm"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.19,1,.22,1)`, `cubic-bezier(.76,0,.24,1)`, `cubic-bezier(.16,1,.3,1)`
- **Extracted Stylesheet Rules (`ellioteriksson-com`)**:
- `after { box-sizing:border-box }`
- `img { max-width:100%;height:auto;display:block }`
- `button { font:inherit;letter-spacing:inherit;color:inherit;cursor:pointer;backgro... }`
- `selection { background:var(--highlight);color:var(--on-highlight) }`
- `focus-visible { outline:2px solid var(--fg);outline-offset:3px }`
- **Per-Selector Transition Rules**:
- **Selector `.arrow-link`**: `transition: color .3s` extracted from `ellioteriksson-com` stylesheet.
- **Selector `.icon`**: `transition: transform .4s var(--ease-out)` extracted from `ellioteriksson-com` stylesheet.
- **Selector `.skip-link`**: `transition: transform .2s` extracted from `ellioteriksson-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.19,1,.22,1)`)**: Governs interactive state transitions across `<header.site-header>` and `<section.showcase>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `7424px` across 8 distinct viewport chapters.
- **Vertical Chapter Sequence**: I’m elliot, an award winnin... (0%) -> Selected work Selected work (13%) -> MORE PROJECTS (26%) -> Pilates Plus (39%) -> Brand & identity (65%) -> Portfolio (78%) -> LET’S TALK LET’S TALK (91%) -> Footer (100%).
- **Hover Micro-Interaction (`first_card`)**: Animate `transform, opacity` with `0s ease`.
- **Multi-Page Routes**: Scaffold internal routes `/cases` (listing, SPA), `/case/the-stash` (detail, direct), `/contact` (about, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `ellioteriksson-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | I’m elliot, an award winning design technolog... | `1` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `13%` | Selected work Selected work | `1` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `1700px` | `26%` | MORE PROJECTS | `1` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `2550px` | `39%` | Pilates Plus | `1` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `4250px` | `65%` | Brand & identity | `1` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `5100px` | `78%` | Portfolio | `1` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `5950px` | `91%` | LET’S TALK LET’S TALK | `1` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `6522px` | `100%` | Footer | `1` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | #home | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `7742px` | `100%` | Footer | [mobile-step-02.webp](assets/mobile-step-02.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `listing` | `https://ellioteriksson.com/cases` | Case studies Case staxkgs | `3495px` | `SPA` (`1663ms`) | [subpage-01-cases.webp](assets/subpage-01-cases.webp) |
| `2` | `detail` | `https://ellioteriksson.com/case/the-stash` | Everything the team knows, one search... | `8510px` | `direct` (`598ms`) | [subpage-02-case-the-stash.webp](assets/subpage-02-case-the-stash.webp) |
| `3` | `about` | `https://ellioteriksson.com/contact` | Let’s talk Let’s talk | `1877px` | `direct` (`341ms`) | [subpage-03-contact.webp](assets/subpage-03-contact.webp) |

