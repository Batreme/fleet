---
title: "UI Prompt Blueprint: perappelgren-de"
date: 2026-11-23
captured_at: 2026-11-23
target: "perappelgren-de"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#213547`)"
---

# UI Design System & Master Generation Blueprint: perappelgren-de

> **Per Appelgren** (https://perappelgren.de/) — Per Appelgren is a Paris and Berlin based photographer working across fashion, beauty, editorial, and commercial image-making.

![Desktop Viewport Capture (1440x900)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Per Appelgren** (`https://perappelgren.de/`). Per Appelgren is a Paris and Berlin based photographer working across fashion, beauty, editorial, and commercial image-making.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#213547`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#0f0f15` primary typography and `#213547` accents.
  - **Grounded Typographic Hierarchy**: Pairs `neueMontreal` for display copy (`Per Appelgren`) with `neueMontreal` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `96rem` container bounds (`gap: 2px`, padding `216px`) with `cubic-bezier(0,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×900px` (`assets/desktop.png`, single-viewport 100vh live capture (900px)), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `96rem` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `216px` lateral canvas padding with `2px` grid gap.
- **Border Radius Scale**: `4px`, `32px`, `var(--radius-lg)`, `999px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: 2px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `216px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0f0f15` | live computed `a` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#1f1f2b` | `:hover { background-color: #1f1f2b }` |
| **Interactive Accent / Highlight** | `#213547` | live computed `button` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#33333d` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#33333d` | hairline divider derived from live computed `p` `color` (`computed_styles.json`) |
| **Variable Token (`--color-black`)** | `#000000` | `var(--color-black)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-neue-montreal` | `"neueMontreal", "neueMontreal Fallback"` | Typography / Scale Token |
| `--font-vemior` | `"vemior", "vemior Fallback"` | Typography / Scale Token |
| `--font-sans` | `var(--font-neue-montreal)` | Typography / Scale Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |
| `--text-xs--line-height` | `calc(1 / .75)` | Typography Ink Token |
| `--text-sm` | `.875rem` | Typography Ink Token |
| `--text-sm--line-height` | `calc(1.25 / .875)` | Typography Ink Token |
| `--font-weight-normal` | `400` | Typography / Scale Token |
| `--font-weight-medium` | `500` | Typography / Scale Token |
| `--font-weight-semibold` | `600` | Typography / Scale Token |
| `--tracking-normal` | `0em` | Typography / Scale Token |
| `--radius-lg` | `.5rem` | Elevation / Border Token |
| `--ease-out` | `cubic-bezier(0, 0, .2, 1)` | Motion / Easing Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `neueMontreal`.
- **Primary Body Stack**: `neueMontreal`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: observed font-size ladder: `22px`, `16px`, `29px`, `10px`, `1em`.
- **Section Heading (`H2`)**: live computed `h3 (primary section heading)` (`font-size: 22px`, `line-height: 28px`, `font-weight: 400`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.16,1,.3,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `perappelgren-de` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `perappelgren-de` stylesheet.
- **Selector `transform\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `perappelgren-de` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<nav.home-nav>` and `<section.w-full>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Per Appelgren                              │
│ ====================================================================== │
│ [ <nav.home-nav> (1440x40px)          | Overview · Index · Archive · ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.relative> (w=1440px)                          | │
│ | H1: Per Appelgren                                                  | │
│ | Substrate: #ffffff | Ink: #0f0f15 | Accent: #213547                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.w-full>) max-w: 96rem                      | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Featured Work & Interactive  |  | Technical Architecture & Nar | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.h-auto>) — Global Directory & Co           | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.z-42>       ) | https://perappelgren.de/             │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 2px)        │
│ ====================================================================== │
│ [ HEADER BAR (<nav.home-nav>          ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.relative>) — 390px Vertical Lead              | │
│ | H1: Per Appelgren                                                  | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.w-full>) — 1-Col Stack                    | │
│ | [ Item 1: Featured Work & Interactive Showcase                   ] | │
│ | [ Item 2: Technical Architecture & Narrative                     ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.h-auto>) — 1-Col (Global Directory &)       | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.z-42>       ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.home-nav> — `perappelgren-de`)**:
   - Landmark `<nav class="home-nav top-0">` (`1440x40px`) hosting `Per Appelgren` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-engine="three.js r182"`, `data-gallery-title-track="true"`, `data-cursor="arrow"`), and stylesheet rule `real_94799760-module__C5EBEW__cla... { font-family:neueMontreal,neueMontreal Fallback }`.
2. **Hero Stage & Focal Lead (<section.relative> — `Per Appelgren`)**:
   - Landmark `<section class="relative w-full">` presenting display lead `Per Appelgren` and copy excerpt *"Hi! I am Per! I'm a German-Swedish photographer based between Par"* over `#ffffff` canvas and `#0f0f15` ink.
3. **Primary Showcase & Content Grid (<section.w-full> — `Featured Work & Interactive Showca`)**:
   - Landmark `<section class="relative w-full">` rendering section `Featured Work & Interactive Showcase` with copy *"CASABLANCA PRE-FALL ´26 CAMPAIGN"*, asset references (`vemior-s.p.0loat6znd6m5-.otf`, `12mrv9~q-_9yg.css`, `0wjx1qarcnur7.js`, `14x4ulv7j4.e5.js`), and grid rule `treal_94799760-module__C5EBEW__va... { --font-neue-montreal:"neueMontreal", "neueMontreal Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.h-auto> — `Technical Architecture & Narrative`)**:
   - Landmark `<section class="h-auto relative">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"ARCHIVE A R C H I V E"*) with `#1f1f2b` surface cards, `#213547` accents, and `mior_bd07f20d-module__cotiFq__cla... { font-family:vemior,vemior Fallback;font-style:normal;font-weight:400 }`.
5. **Colophon & Global Directory Footer (<footer.z-42> — `https://perappelgren.de/`)**:
   - Landmark `<footer class="z-42 relative">` anchoring `Per Appelgren` footer links (`Overview · Index · Archive · About · Contact`), copy *"CONTACT C O N T A C T"*, and `#33333d` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: perappelgren-de (Per Appelgren)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `perappelgren-de` (**Per Appelgren** — `https://perappelgren.de/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#213547`).
- **Identity & Domain Context**: Per Appelgren is a Paris and Berlin based photographer working across fashion, beauty, editorial, and commercial image-making.
- **Primary Substrate**: `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#0f0f15`, **Accent / Highlight**: `#213547`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#0f0f15` primary typography and `#213547` accents.
  - **Grounded Typographic Hierarchy**: Pairs `neueMontreal` for display copy (`Per Appelgren`) with `neueMontreal` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `96rem` container bounds (`gap: 2px`, padding `216px`) with `cubic-bezier(0,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `perappelgren-de` in your global stylesheet:

:root {
  /* Per Appelgren (perappelgren-de) — Live-Grounded CSS Variables */
  --font-neue-montreal: "neueMontreal", "neueMontreal Fallback"; /* Typography / Scale Token (perappelgren-de) */
  --font-vemior: "vemior", "vemior Fallback"; /* Typography / Scale Token (perappelgren-de) */
  --font-sans: var(--font-neue-montreal); /* Typography / Scale Token (perappelgren-de) */
  --color-black: #000; /* Canvas / Surface Token (perappelgren-de) */
  --color-white: #fff; /* Canvas / Surface Token (perappelgren-de) */
  --spacing: .25rem; /* Layout / Spatial Grid Token (perappelgren-de) */
  --text-xs: .75rem; /* Typography Ink Token (perappelgren-de) */
  --text-xs--line-height: calc(1 / .75); /* Typography Ink Token (perappelgren-de) */
  --text-sm: .875rem; /* Typography Ink Token (perappelgren-de) */
  --text-sm--line-height: calc(1.25 / .875); /* Typography Ink Token (perappelgren-de) */
  --font-weight-normal: 400; /* Typography / Scale Token (perappelgren-de) */
  --font-weight-medium: 500; /* Typography / Scale Token (perappelgren-de) */
  --font-weight-semibold: 600; /* Typography / Scale Token (perappelgren-de) */
  --tracking-normal: 0em; /* Typography / Scale Token (perappelgren-de) */
  --radius-lg: .5rem; /* Elevation / Border Token (perappelgren-de) */
  --ease-out: cubic-bezier(0, 0, .2, 1); /* Motion / Easing Token (perappelgren-de) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#0f0f15` — grounded in live computed `a` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#1f1f2b` — grounded in `:hover { background-color: #1f1f2b }`
- **Interactive Accent / Highlight**: `#213547` — grounded in live computed `button` `color` (`computed_styles.json`)
- **Secondary / Muted Copy**: `#33333d` — grounded in live computed `p` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#33333d` — grounded in hairline divider derived from live computed `p` `color` (`computed_styles.json`)
- **Variable Token (`--color-black`)**: `#000000` — grounded in `var(--color-black)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×900px` (single-viewport 100vh live capture (900px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `96rem` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `216px` lateral canvas padding with `2px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: 2px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `216px` horizontal padding
- **Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`
- **Corner Radii**: `4px`, `32px`, `var(--radius-lg)`, `999px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `neueMontreal`
- **Body Font Stack**: `neueMontreal`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: observed font-size ladder: `22px`, `16px`, `29px`, `10px`, `1em`
- **H2 Section Rule**: live computed `h3 (primary section heading)` (`font-size: 22px`, `line-height: 28px`, `font-weight: 400`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `perappelgren-de` (`Per Appelgren`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.home-nav> — `perappelgren-de`)**:
   - DOM & Selectors: Landmark `<nav class="home-nav top-0">` (`1440x40px`) hosting `Per Appelgren` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-engine="three.js r182"`, `data-gallery-title-track="true"`, `data-cursor="arrow"`), and stylesheet rule `real_94799760-module__C5EBEW__cla... { font-family:neueMontreal,neueMontreal Fallback }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.home-nav> — `perappelgren-de`)` (`perappelgren-de`) adapts across `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)` with `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.16,1,.3,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<section.relative> — `Per Appelgren`)**:
   - DOM & Selectors: Landmark `<section class="relative w-full">` presenting display lead `Per Appelgren` and copy excerpt *"Hi! I am Per! I'm a German-Swedish photographer based between Par"* over `#ffffff` canvas and `#0f0f15` ink.
   - Responsive Contract: Hero stage (`1440×900px` desktop / `390×2400px` mobile) sets `#ffffff` background with `#0f0f15` headline `Per Appelgren`.
3. **Primary Showcase & Content Grid (<section.w-full> — `Featured Work & Interactive Showca`)**:
   - DOM & Selectors: Landmark `<section class="relative w-full">` rendering section `Featured Work & Interactive Showcase` with copy *"CASABLANCA PRE-FALL ´26 CAMPAIGN"*, asset references (`vemior-s.p.0loat6znd6m5-.otf`, `12mrv9~q-_9yg.css`, `0wjx1qarcnur7.js`, `14x4ulv7j4.e5.js`), and grid rule `treal_94799760-module__C5EBEW__va... { --font-neue-montreal:"neueMontreal", "neueMontreal Fallback" }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.w-full> — `Featured Work & Interactive Showca`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: 2px`) on desktop and Single-column vertical stack at `390px` viewport width with `216px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.h-auto> — `Technical Architecture & Narrative`)**:
   - DOM & Selectors: Landmark `<section class="h-auto relative">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"ARCHIVE A R C H I V E"*) with `#1f1f2b` surface cards, `#213547` accents, and `mior_bd07f20d-module__cotiFq__cla... { font-family:vemior,vemior Fallback;font-style:normal;font-weight:400 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.h-auto> — `Technical Architecture & Narrative`)` uses `4px`, `32px`, `var(--radius-lg)`, `999px` radii, `#213547` highlights, and assets (vemior-s.p.0loat6znd6m5-.otf, 12mrv9~q-_9yg.css, 0wjx1qarcnur7.js).
5. **Colophon & Global Directory Footer (<footer.z-42> — `https://perappelgren.de/`)**:
   - DOM & Selectors: Landmark `<footer class="z-42 relative">` anchoring `Per Appelgren` footer links (`Overview · Index · Archive · About · Contact`), copy *"CONTACT C O N T A C T"*, and `#33333d` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.z-42> — `https://perappelgren.de/`)` aligns to `96rem` (non-`@media` desktop container stylesheet rule) with `216px` lateral canvas padding with `2px` grid gap and attributes (data-precedence="next", data-engine="three.js r182", data-gallery-title-track="true").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Hi! I am Per! I'm a German-Swedish photographer based between Paris and Berlin, wi..."*
- Copy Excerpt 2: *"CASABLANCA PRE-FALL ´26 CAMPAIGN"*
- Copy Excerpt 3: *"ARCHIVE A R C H I V E"*
- Copy Excerpt 4: *"CONTACT C O N T A C T"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.16,1,.3,1)`
- **Extracted Stylesheet Rules (`perappelgren-de`)**:
- `real_94799760-module__C5EBEW__cla... { font-family:neueMontreal,neueMontreal Fallback }`
- `treal_94799760-module__C5EBEW__va... { --font-neue-montreal:"neueMontreal", "neueMontreal Fallback" }`
- `mior_bd07f20d-module__cotiFq__cla... { font-family:vemior,vemior Fallback;font-style:normal;font-weight:400 }`
- `emior_bd07f20d-module__cotiFq__va... { --font-vemior:"vemior", "vemior Fallback" }`
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `perappelgren-de` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `perappelgren-de` stylesheet.
- **Selector `transform\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `perappelgren-de` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<nav.home-nav>` and `<section.w-full>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `perappelgren-de`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
