---
title: "UI Prompt Blueprint: kissbranding-co-uk"
date: 2026-11-23
captured_at: 2026-11-23
target: "kissbranding-co-uk"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#008300`)"
---

# UI Design System & Master Generation Blueprint: kissbranding-co-uk

> **Kiss · Brands that Kiss** (https://kissbranding.co.uk/) — Brand strategy and identity for founder-led and investor-backed businesses at the moments that matter. Transform Award-winning studio in...

![Desktop Viewport Capture (1440x900)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Kiss · Brands that Kiss** (`https://kissbranding.co.uk/`). Brand strategy and identity for founder-led and investor-backed businesses at the moments that matter. Transform Award-winning studio in...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#008300`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#000000` (live computed `html` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#008300` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Apple Color Emoji` for display copy (`Kiss · Brands that Kiss`) with `Apple Color Emoji` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1920px` container bounds (`gap: var(--spacing-grid)`, padding `var(--spacing-container)`) with `cubic-bezier(.23,1,.32,1)` easing and Lenis Smooth Scroll (`data-lenis`), Lottie Vector Animation Player.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x844)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×900px` (`assets/desktop.png`, single-viewport 100vh live capture (900px)), Mobile `390×844px` (`assets/mobile.png`, single-viewport 100vh live capture (844px)).
- **Master Container Bounds**: `1920px` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `var(--spacing-container)` lateral canvas padding with `var(--spacing-grid)` grid gap.
- **Border Radius Scale**: `var(--tac-border-radius)`, `var(--tac-btn-border-radius)`, `8px`, `5px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1920px`, `gap: var(--spacing-grid)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--spacing-container)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:375px)`, `@media (min-width:768px)`, `@media (min-width:1024px)`, `@media (min-width:1200px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `a` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ff0000` | `.bg-red { background-color: red }` (`#ff0000`) |
| **Interactive Accent / Highlight** | `#008300` | `.tarteaucitronCTAButton { background: #008300 }` |
| **Secondary / Muted Copy** | `#333333` | live computed `button` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#333333` | `#tarteaucitron .tarteaucitronBo... { border: #333333 }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--size` | `375` | Layout / Spatial Grid Token |
| `--padding-container` | `2rem` | Layout / Spatial Grid Token |
| `--vw` | `100vw` | Layout / Spatial Grid Token |
| `--vh` | `calc(var(--vh-initial,1vh)*100)` | Layout / Spatial Grid Token |
| `--spacing-container` | `var(--padding-container)` | Layout / Spatial Grid Token |
| `--spacing-grid` | `1rem` | Layout / Spatial Grid Token |
| `--spacing-0` | `0` | Layout / Spatial Grid Token |
| `--spacing` | `.1rem` | Layout / Spatial Grid Token |
| `--font-body` | `"tt-commons-pro","TT Commons Pro",sans-serif` | Typography / Scale Token |
| `--font-body-condensed` | `"tt-commons-pro-condensed","TT Commons Pro Condensed",sans-serif` | Typography / Scale Token |
| `--font-heading` | `"PP Migra",serif` | Typography Ink Token |
| `--font-weight-normal` | `400` | Typography / Scale Token |
| `--font-weight-bold` | `700` | Typography / Scale Token |
| `--font-weight-extrabold` | `800` | Typography / Scale Token |
| `--text-10` | `1rem` | Typography Ink Token |
| `--text-12` | `1.2rem` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Apple Color Emoji`.
- **Primary Body Stack**: `Apple Color Emoji`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: observed font-size ladder: `10px`, `72px`, `14px`, `1em`, `80%`.
- **Section Heading (`H2`)**: CSS variables `--tac-subtitle-font-family: "PP Migra",serif`, `--tac-subtitle-font-size: 3.2rem`, `--tac-subtitle-font-weight: var(--tac-font-weight)`; rule `h2` (`font-size: var(--text-24)`, `line-height: 120%`, `letter-spacing: 0`, `font-weight: var(--font-we...`).
- **Body Copy**: live computed `body` (`font-size: 10px`, `line-height: normal`, `font-weight: 400`); CSS variables `--font-body: "tt-commons-pro","TT Commons Pro",sans-serif`, `--font-body-condensed: "tt-commons-pro-condensed","TT Commons Pro Condensed",sans-serif`; rule `p` (`font-size: var(--text-14)`, `line-height: 140%`, `letter-spacing: 0`, `font-weight: var(--font-we...`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 72px`, `line-height: 72px`, `font-weight: 400`, `letter-spacing: -1px`); CSS variables `--tac-letter-spacing: .04rem`, `--tac-btn-letter-spacing: var(--tac-letter-spacing)`, `--tac-close-btn-letter-spacing: var(--tac-letter-spacing)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.23,1,.32,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: 15` extracted from `kissbranding-co-uk` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,ease)` extracted from `kissbranding-co-uk` stylesheet.
- **Selector `.transition-all`**: `transition: var(--tw-ease,ease)` extracted from `kissbranding-co-uk` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.23,1,.32,1)`)**: Governs interactive state transitions across `<header.pointer-events-none>` and `<div.bg-white>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Lottie Vector Animation Player, HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Kiss · Brands that Kiss                    │
│ ====================================================================== │
│ [ <header.pointer-events (1440x131px) | Overview · Index · Archive · ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <div.mobile-wrapper> (w=1440px)                        | │
│ | H1: Kiss · Brands that Kiss                                        | │
│ | Substrate: #000000 | Ink: #ffffff | Accent: #008300                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<div.bg-white>) max-w: 1920px                       | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Featured Work & Interactive  |  | Technical Architecture & Nar | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<div.mobile-wrapper:nth(2)) — Global Directory & Co | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.yoast-schema) | https://kissbranding.co.uk/          │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--sp)   │
│ ====================================================================== │
│ [ HEADER BAR (<header.pointer-events-n) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<div.mobile-wrapper>) — 390px Vertical Lead            | │
│ | H1: Kiss · Brands that Kiss                                        | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<div.bg-white>) — 1-Col Stack                      | │
│ | [ Item 1: Featured Work & Interactive Showcase                   ] | │
│ | [ Item 2: Technical Architecture & Narrative                     ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<div.mobile-wrapper:nth() — 1-Col (Global Directory &) │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.yoast-schema) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.pointer-events-none> — `kissbranding-co-uk`)**:
   - Landmark `<header class="pointer-events-none fixed">` (`1440x131px`) hosting `Kiss · Brands that Kiss` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-taxi-reload`, `data-frames-count="22"`, `data-frames-directory-uri="https://kissbranding...."`, `data-clone="true"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<div.mobile-wrapper> — `Kiss · Brands that Kiss`)**:
   - Landmark `<div class="mobile-wrapper bg-white">` presenting display lead `Kiss · Brands that Kiss` and copy excerpt *"Cookie preferences"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<div.bg-white> — `Featured Work & Interactive Showca`)**:
   - Landmark `<div class="mobile-wrapper bg-white">` rendering section `Featured Work & Interactive Showcase` with copy *"Preference for all services"*, asset references (`tarteaucitron.min.js`, `apple-touch-icon-57x57.png`, `apple-touch-icon-60x60.png`, `apple-touch-icon-72x72.png`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<div.mobile-wrapper:nth(2)> — `Technical Architecture & Narrative`)**:
   - Landmark `<div class="mobile-wrapper bg-white">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Mandatory cookies This site uses cookies necessary for its proper"*) with `#ff0000` surface cards, `#008300` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.yoast-schema-graph> — `https://kissbranding.co.uk/`)**:
   - Landmark `<footer class="yoast-schema-graph">` anchoring `Kiss · Brands that Kiss` footer links (`Overview · Index · Archive · About · Contact`), copy *"This site uses cookies necessary for its proper functioning "*, and `#333333` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: kissbranding-co-uk (Kiss · Brands that Kiss)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `kissbranding-co-uk` (**Kiss · Brands that Kiss** — `https://kissbranding.co.uk/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#008300`).
- **Identity & Domain Context**: Brand strategy and identity for founder-led and investor-backed businesses at the moments that matter. Transform Award-winning studio in...
- **Primary Substrate**: `#000000` (live computed `html` `background-color` (`computed_styles.json`)), **Primary Ink**: `#ffffff`, **Accent / Highlight**: `#008300`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#000000` (live computed `html` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#008300` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Apple Color Emoji` for display copy (`Kiss · Brands that Kiss`) with `Apple Color Emoji` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1920px` container bounds (`gap: var(--spacing-grid)`, padding `var(--spacing-container)`) with `cubic-bezier(.23,1,.32,1)` easing and Lenis Smooth Scroll (`data-lenis`), Lottie Vector Animation Player.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `kissbranding-co-uk` in your global stylesheet:

:root {
  /* Kiss · Brands that Kiss (kissbranding-co-uk) — Live-Grounded CSS Variables */
  --size: 375; /* Layout / Spatial Grid Token (kissbranding-co-uk) */
  --padding-container: 2rem; /* Layout / Spatial Grid Token (kissbranding-co-uk) */
  --vw: 100vw; /* Layout / Spatial Grid Token (kissbranding-co-uk) */
  --vh: calc(var(--vh-initial,1vh)*100); /* Layout / Spatial Grid Token (kissbranding-co-uk) */
  --spacing-container: var(--padding-container); /* Layout / Spatial Grid Token (kissbranding-co-uk) */
  --spacing-grid: 1rem; /* Layout / Spatial Grid Token (kissbranding-co-uk) */
  --spacing-0: 0; /* Layout / Spatial Grid Token (kissbranding-co-uk) */
  --spacing: .1rem; /* Layout / Spatial Grid Token (kissbranding-co-uk) */
  --font-body: "tt-commons-pro","TT Commons Pro",sans-serif; /* Typography / Scale Token (kissbranding-co-uk) */
  --font-body-condensed: "tt-commons-pro-condensed","TT Commons Pro Condensed",sans-serif; /* Typography / Scale Token (kissbranding-co-uk) */
  --font-heading: "PP Migra",serif; /* Typography Ink Token (kissbranding-co-uk) */
  --font-weight-normal: 400; /* Typography / Scale Token (kissbranding-co-uk) */
  --font-weight-bold: 700; /* Typography / Scale Token (kissbranding-co-uk) */
  --font-weight-extrabold: 800; /* Typography / Scale Token (kissbranding-co-uk) */
  --text-10: 1rem; /* Typography Ink Token (kissbranding-co-uk) */
  --text-12: 1.2rem; /* Typography Ink Token (kissbranding-co-uk) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000000` — grounded in live computed `html` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#ffffff` — grounded in live computed `a` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#ff0000` — grounded in `.bg-red { background-color: red }` (`#ff0000`)
- **Interactive Accent / Highlight**: `#008300` — grounded in `.tarteaucitronCTAButton { background: #008300 }`
- **Secondary / Muted Copy**: `#333333` — grounded in live computed `button` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#333333` — grounded in `#tarteaucitron .tarteaucitronBo... { border: #333333 }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×900px` (single-viewport 100vh live capture (900px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×844px` (single-viewport 100vh live capture (844px), `390px` standard mobile width).
- **Container Max-Width**: `1920px` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `var(--spacing-container)` lateral canvas padding with `var(--spacing-grid)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1920px`, `gap: var(--spacing-grid)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--spacing-container)` horizontal padding
- **Media Queries**: `@media (min-width:375px)`, `@media (min-width:768px)`, `@media (min-width:1024px)`, `@media (min-width:1200px)`
- **Corner Radii**: `var(--tac-border-radius)`, `var(--tac-btn-border-radius)`, `8px`, `5px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Apple Color Emoji`
- **Body Font Stack**: `Apple Color Emoji`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: observed font-size ladder: `10px`, `72px`, `14px`, `1em`, `80%`
- **H2 Section Rule**: CSS variables `--tac-subtitle-font-family: "PP Migra",serif`, `--tac-subtitle-font-size: 3.2rem`, `--tac-subtitle-font-weight: var(--tac-font-weight)`; rule `h2` (`font-size: var(--text-24)`, `line-height: 120%`, `letter-spacing: 0`, `font-weight: var(--font-we...`)
- **Body Copy Rule**: live computed `body` (`font-size: 10px`, `line-height: normal`, `font-weight: 400`); CSS variables `--font-body: "tt-commons-pro","TT Commons Pro",sans-serif`, `--font-body-condensed: "tt-commons-pro-condensed","TT Commons Pro Condensed",sans-serif`; rule `p` (`font-size: var(--text-14)`, `line-height: 140%`, `letter-spacing: 0`, `font-weight: var(--font-we...`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 72px`, `line-height: 72px`, `font-weight: 400`, `letter-spacing: -1px`); CSS variables `--tac-letter-spacing: .04rem`, `--tac-btn-letter-spacing: var(--tac-letter-spacing)`, `--tac-close-btn-letter-spacing: var(--tac-letter-spacing)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `kissbranding-co-uk` (`Kiss · Brands that Kiss`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.pointer-events-none> — `kissbranding-co-uk`)**:
   - DOM & Selectors: Landmark `<header class="pointer-events-none fixed">` (`1440x131px`) hosting `Kiss · Brands that Kiss` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-taxi-reload`, `data-frames-count="22"`, `data-frames-directory-uri="https://kissbranding...."`, `data-clone="true"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.pointer-events-none> — `kissbranding-co-uk`)` (`kissbranding-co-uk`) adapts across `@media (min-width:375px)`, `@media (min-width:768px)`, `@media (min-width:1024px)`, `@media (min-width:1200px)` with `cubic-bezier(.23,1,.32,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<div.mobile-wrapper> — `Kiss · Brands that Kiss`)**:
   - DOM & Selectors: Landmark `<div class="mobile-wrapper bg-white">` presenting display lead `Kiss · Brands that Kiss` and copy excerpt *"Cookie preferences"* over `#000000` canvas and `#ffffff` ink.
   - Responsive Contract: Hero stage (`1440×900px` desktop / `390×844px` mobile) sets `#000000` background with `#ffffff` headline `Kiss · Brands that Kiss`.
3. **Primary Showcase & Content Grid (<div.bg-white> — `Featured Work & Interactive Showca`)**:
   - DOM & Selectors: Landmark `<div class="mobile-wrapper bg-white">` rendering section `Featured Work & Interactive Showcase` with copy *"Preference for all services"*, asset references (`tarteaucitron.min.js`, `apple-touch-icon-57x57.png`, `apple-touch-icon-60x60.png`, `apple-touch-icon-72x72.png`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<div.bg-white> — `Featured Work & Interactive Showca`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1920px`, `gap: var(--spacing-grid)`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--spacing-container)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<div.mobile-wrapper:nth(2)> — `Technical Architecture & Narrative`)**:
   - DOM & Selectors: Landmark `<div class="mobile-wrapper bg-white">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Mandatory cookies This site uses cookies necessary for its proper"*) with `#ff0000` surface cards, `#008300` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<div.mobile-wrapper:nth(2)> — `Technical Architecture & Narrative`)` uses `var(--tac-border-radius)`, `var(--tac-btn-border-radius)`, `8px`, `5px` radii, `#008300` highlights, and assets (tarteaucitron.min.js, apple-touch-icon-57x57.png, apple-touch-icon-60x60.png).
5. **Colophon & Global Directory Footer (<footer.yoast-schema-graph> — `https://kissbranding.co.uk/`)**:
   - DOM & Selectors: Landmark `<footer class="yoast-schema-graph">` anchoring `Kiss · Brands that Kiss` footer links (`Overview · Index · Archive · About · Contact`), copy *"This site uses cookies necessary for its proper functioning "*, and `#333333` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.yoast-schema-graph> — `https://kissbranding.co.uk/`)` aligns to `1920px` (non-`@media` desktop container stylesheet rule) with `var(--spacing-container)` lateral canvas padding with `var(--spacing-grid)` grid gap and attributes (data-taxi-reload, data-frames-count="22", data-frames-directory-uri="https://kissbranding....").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Cookie preferences"*
- Copy Excerpt 2: *"Preference for all services"*
- Copy Excerpt 3: *"Mandatory cookies This site uses cookies necessary for its proper functioning whic..."*
- Copy Excerpt 4: *"This site uses cookies necessary for its proper functioning which cannot be deacti..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.23,1,.32,1)`
- **Extracted Stylesheet Rules (`kissbranding-co-uk`)**:
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- `sup { vertical-align:baseline;font-size:75%;line-height:0;position:relative }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: 15` extracted from `kissbranding-co-uk` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,ease)` extracted from `kissbranding-co-uk` stylesheet.
- **Selector `.transition-all`**: `transition: var(--tw-ease,ease)` extracted from `kissbranding-co-uk` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.23,1,.32,1)`)**: Governs interactive state transitions across `<header.pointer-events-none>` and `<div.bg-white>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Lottie Vector Animation Player, HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `kissbranding-co-uk`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
