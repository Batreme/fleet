---
title: "UI Prompt Blueprint: andreas-vision"
date: 2026-11-23
captured_at: 2026-11-23
target: "andreas-vision"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#f8f8fa` / `#00aaff`)"
---

# UI Design System & Master Generation Blueprint: andreas-vision

> **Andreas Kruszakin, growth-focused design engineer in Europe** (https://andreas.vision) — I'm Andreas, a growth-focused design engineer who is design first and builds the system underneath. I make founders' products easy to get...

![Desktop Viewport Capture (1440x900)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Andreas Kruszakin, growth-focused design engineer in Europe** (`https://andreas.vision`). I'm Andreas, a growth-focused design engineer who is design first and builds the system underneath. I make founders' products easy to get...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#f8f8fa` / `#00aaff`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f8f8fa` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#00aaff` accents.
  - **Grounded Typographic Hierarchy**: Pairs `TRJN DaVinci` for display copy (`Designer who ships with vision Desig`) with `Geist Variable` and `Geist Mono Variable`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 15px`, padding `15px`) with `cubic-bezier(0.25,0.1,0.25,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x844)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×900px` (`assets/desktop.png`, single-viewport 100vh live capture (900px)), Mobile `390×844px` (`assets/mobile.png`, single-viewport 100vh live capture (844px)).
- **Master Container Bounds**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport).
- **Canvas Lateral Padding & Spacing**: `15px` lateral canvas padding with `15px` grid gap.
- **Border Radius Scale**: `0px` (sharp unrounded corners).

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 15px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `15px` horizontal padding.
- **Extracted CSS Media Queries**: no `@media` queries in captured stylesheet (fluid viewport scaling).

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f8f8fa` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | live computed `footer` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#00aaff` | `var(--link-visited)` in `:root` |
| **Secondary / Muted Copy** | `#ff44aa` | `var(--palette-pink)` in `:root` |
| **Structural Hairline Border** | `#e2e2e4` | `var(--line-hover)` in `:root` (`rgba(0, 0, 0, 0.09)`) |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `"Geist Variable", -apple-system, system-ui, sans-serif` | Typography / Scale Token |
| `--font-brand` | `"Geist Variable", -apple-system, system-ui, sans-serif` | Brand / Palette Token |
| `--font-brand-serif` | `"Newsreader Variable", Georgia, serif` | Brand / Palette Token |
| `--font-brand-mono` | `"Geist Mono Variable", ui-monospace, monospace` | Brand / Palette Token |
| `--font-site` | `"Geist Variable", -apple-system, system-ui, sans-serif` | Typography / Scale Token |
| `--font-site-highlight` | `"TRJN DaVinci", "Newsreader Variable", Georgia, serif` | Canvas / Surface Token |
| `--control-2xs` | `20px` | Dimension / Scale Token |
| `--control-xs` | `24px` | Dimension / Scale Token |
| `--control-sm` | `28px` | Dimension / Scale Token |
| `--control-md` | `32px` | Dimension / Scale Token |
| `--control-lg` | `36px` | Dimension / Scale Token |
| `--radius-control-sm` | `4px` | Elevation / Border Token |
| `--radius-control` | `8px` | Elevation / Border Token |
| `--radius-surface` | `12px` | Canvas / Surface Token |
| `--radius-card` | `16px` | Elevation / Border Token |
| `--focus-ring-width` | `1.5px` | Layout / Spatial Grid Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `TRJN DaVinci`.
- **Primary Body Stack**: `Geist Variable`.
- **Technical / Metadata Stack**: `Geist Mono Variable`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 132px`, `line-height: 147.84px`, `font-weight: 400`, `letter-spacing: -5.28px`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 32px`, `line-height: 38.4px`, `font-weight: 500`, `letter-spacing: -0.32px`).
- **Body Copy**: live computed `body` (`font-size: 14px`, `line-height: 21px`, `font-weight: 400`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: 16.2px`, `font-weight: 500`); CSS variables `--font-brand-mono: "Geist Mono Variable", ui-monospace, monospace`, `--label-icon-selected: inherit`, `--labels: 0`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `style]`**: `transition: none` extracted from `andreas-vision` stylesheet.
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in captured CSS).
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Andreas Kruszakin, growth-focused design e │
│ ====================================================================== │
│ [ <header.top> (686x26px)             | Overview · Index · Archive · ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.e5sioty0> (w=1440px)                          | │
│ | H1: Designer who ships with vision Design Engineer wh...           | │
│ | Substrate: #f8f8fa | Ink: #000000 | Accent: #00aaff                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.swap>) max-w: 1440px                       | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Work                         |  | Designer who ships with visi | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.css-1yyyvev>) — Design Engineer who s      | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.css-za9d9j> ) | https://andreas.vision               │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 15px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.top>            ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.e5sioty0>) — 390px Vertical Lead              | │
│ | H1: Designer who ships with vision Design Engineer wh...           | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.swap>) — 1-Col Stack                      | │
│ | [ Item 1: Work                                                   ] | │
│ | [ Item 2: Designer who ships with vision                         ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.css-1yyyvev>) — 1-Col (Design Engineer wh)  | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.css-za9d9j> ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.top> — `andreas-vision`)**:
   - Landmark `<header class="top">` (`686x26px`) hosting `Andreas Kruszakin, growth-focused de` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-selection-ink`, `data-emotion="css-global"`, `data-s`, `data-emotion="css-global"`), and stylesheet rule `root { height: 100%; margin: 0; }`.
2. **Hero Stage & Focal Lead (<section.e5sioty0> — `Designer who ships with vision Des`)**:
   - Landmark `<section class="e5sioty0 css-8jf4oe">` presenting display lead `Designer who ships with vision Design Engineer wh...` and copy excerpt *"I'm Andreas, making precise, joyful interfaces and the tools to b"* over `#f8f8fa` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.swap> — `Work`)**:
   - Landmark `<section class="swap css-1eowax1">` rendering section `Work` with copy *"Designer who ships with vision"*, asset references (`llms.txt`, `icon-192.png`, `favicon.ico`, `favicon.svg`), and grid rule `html { background: fff; }`.
4. **Interactive Detail & Feature Matrix (<section.css-1yyyvev> — `Designer who ships with vision`)**:
   - Landmark `<section class="swap css-1yyyvev">` framing `Designer who ships with vision` and `Design Engineer who ships growth` (*"Design Engineer who ships growth"*) with `#ffffff` surface cards, `#00aaff` accents, and `header { border-color: #e2e2e4; }`.
5. **Colophon & Global Directory Footer (<footer.css-za9d9j> — `https://andreas.vision`)**:
   - Landmark `<footer class="css-za9d9j e154gxt60">` anchoring `Andreas Kruszakin, growth-focuse` footer links (`Overview · Index · Archive · About · Contact`), copy *"Cheval Inbox Canvas Arrange Share 2. Inbox: crit and variant"*, and `#e2e2e4` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: andreas-vision (Andreas Kruszakin, growth-focused design engineer in Europe)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `andreas-vision` (**Andreas Kruszakin, growth-focused design engineer in Europe** — `https://andreas.vision`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f8f8fa` / `#00aaff`).
- **Identity & Domain Context**: I'm Andreas, a growth-focused design engineer who is design first and builds the system underneath. I make founders' products easy to get...
- **Primary Substrate**: `#f8f8fa` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#000000`, **Accent / Highlight**: `#00aaff`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f8f8fa` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#00aaff` accents.
  - **Grounded Typographic Hierarchy**: Pairs `TRJN DaVinci` for display copy (`Designer who ships with vision Desig`) with `Geist Variable` and `Geist Mono Variable`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 15px`, padding `15px`) with `cubic-bezier(0.25,0.1,0.25,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `andreas-vision` in your global stylesheet:

:root {
  /* Andreas Kruszakin, growth-focused design engineer in Europe (andreas-vision) — Live-Grounded CSS Variables */
  --font-sans: "Geist Variable", -apple-system, system-ui, sans-serif; /* Typography / Scale Token (andreas-vision) */
  --font-brand: "Geist Variable", -apple-system, system-ui, sans-serif; /* Brand / Palette Token (andreas-vision) */
  --font-brand-serif: "Newsreader Variable", Georgia, serif; /* Brand / Palette Token (andreas-vision) */
  --font-brand-mono: "Geist Mono Variable", ui-monospace, monospace; /* Brand / Palette Token (andreas-vision) */
  --font-site: "Geist Variable", -apple-system, system-ui, sans-serif; /* Typography / Scale Token (andreas-vision) */
  --font-site-highlight: "TRJN DaVinci", "Newsreader Variable", Georgia, serif; /* Canvas / Surface Token (andreas-vision) */
  --control-2xs: 20px; /* Dimension / Scale Token (andreas-vision) */
  --control-xs: 24px; /* Dimension / Scale Token (andreas-vision) */
  --control-sm: 28px; /* Dimension / Scale Token (andreas-vision) */
  --control-md: 32px; /* Dimension / Scale Token (andreas-vision) */
  --control-lg: 36px; /* Dimension / Scale Token (andreas-vision) */
  --radius-control-sm: 4px; /* Elevation / Border Token (andreas-vision) */
  --radius-control: 8px; /* Elevation / Border Token (andreas-vision) */
  --radius-surface: 12px; /* Canvas / Surface Token (andreas-vision) */
  --radius-card: 16px; /* Elevation / Border Token (andreas-vision) */
  --focus-ring-width: 1.5px; /* Layout / Spatial Grid Token (andreas-vision) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f8f8fa` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#000000` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#ffffff` — grounded in live computed `footer` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#00aaff` — grounded in `var(--link-visited)` in `:root`
- **Secondary / Muted Copy**: `#ff44aa` — grounded in `var(--palette-pink)` in `:root`
- **Structural Hairline Border**: `#e2e2e4` — grounded in `var(--line-hover)` in `:root` (`rgba(0, 0, 0, 0.09)`)

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×900px` (single-viewport 100vh live capture (900px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×844px` (single-viewport 100vh live capture (844px), `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport)
- **Padding & Gutters**: `15px` lateral canvas padding with `15px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 15px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `15px` horizontal padding
- **Media Queries**: no `@media` queries in captured stylesheet (fluid viewport scaling)
- **Corner Radii**: `0px` (sharp unrounded corners)

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `TRJN DaVinci`
- **Body Font Stack**: `Geist Variable`
- **Monospace / Technical Font Stack**: `Geist Mono Variable`
- **H1 Display Rule**: live computed `h1` (`font-size: 132px`, `line-height: 147.84px`, `font-weight: 400`, `letter-spacing: -5.28px`)
- **H2 Section Rule**: live computed `h2` (`font-size: 32px`, `line-height: 38.4px`, `font-weight: 500`, `letter-spacing: -0.32px`)
- **Body Copy Rule**: live computed `body` (`font-size: 14px`, `line-height: 21px`, `font-weight: 400`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 12px`, `line-height: 16.2px`, `font-weight: 500`); CSS variables `--font-brand-mono: "Geist Mono Variable", ui-monospace, monospace`, `--label-icon-selected: inherit`, `--labels: 0`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `andreas-vision` (`Andreas Kruszakin, growth-focused design engineer in Europe`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.top> — `andreas-vision`)**:
   - DOM & Selectors: Landmark `<header class="top">` (`686x26px`) hosting `Andreas Kruszakin, growth-focused de` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-selection-ink`, `data-emotion="css-global"`, `data-s`, `data-emotion="css-global"`), and stylesheet rule `root { height: 100%; margin: 0; }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.top> — `andreas-vision`)` (`andreas-vision`) adapts across no `@media` queries in captured stylesheet (fluid viewport scaling) with `cubic-bezier(0.25,0.1,0.25,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<section.e5sioty0> — `Designer who ships with vision Des`)**:
   - DOM & Selectors: Landmark `<section class="e5sioty0 css-8jf4oe">` presenting display lead `Designer who ships with vision Design Engineer wh...` and copy excerpt *"I'm Andreas, making precise, joyful interfaces and the tools to b"* over `#f8f8fa` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1440×900px` desktop / `390×844px` mobile) sets `#f8f8fa` background with `#000000` headline `Designer who ships with vision Design Engineer wh...`.
3. **Primary Showcase & Content Grid (<section.swap> — `Work`)**:
   - DOM & Selectors: Landmark `<section class="swap css-1eowax1">` rendering section `Work` with copy *"Designer who ships with vision"*, asset references (`llms.txt`, `icon-192.png`, `favicon.ico`, `favicon.svg`), and grid rule `html { background: fff; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.swap> — `Work`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 15px`) on desktop and Single-column vertical stack at `390px` viewport width with `15px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.css-1yyyvev> — `Designer who ships with vision`)**:
   - DOM & Selectors: Landmark `<section class="swap css-1yyyvev">` framing `Designer who ships with vision` and `Design Engineer who ships growth` (*"Design Engineer who ships growth"*) with `#ffffff` surface cards, `#00aaff` accents, and `header { border-color: #e2e2e4; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.css-1yyyvev> — `Designer who ships with vision`)` uses `0px` (sharp unrounded corners) radii, `#00aaff` highlights, and assets (llms.txt, icon-192.png, favicon.ico).
5. **Colophon & Global Directory Footer (<footer.css-za9d9j> — `https://andreas.vision`)**:
   - DOM & Selectors: Landmark `<footer class="css-za9d9j e154gxt60">` anchoring `Andreas Kruszakin, growth-focuse` footer links (`Overview · Index · Archive · About · Contact`), copy *"Cheval Inbox Canvas Arrange Share 2. Inbox: crit and variant"*, and `#e2e2e4` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.css-za9d9j> — `https://andreas.vision`)` aligns to `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport) with `15px` lateral canvas padding with `15px` grid gap and attributes (data-selection-ink, data-emotion="css-global", data-s).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"I'm Andreas, making precise, joyful interfaces and the tools to build them, from f..."*
- Copy Excerpt 2: *"Designer who ships with vision"*
- Copy Excerpt 3: *"Design Engineer who ships growth"*
- Copy Excerpt 4: *"Cheval Inbox Canvas Arrange Share 2. Inbox: crit and variants Inbox Brief A Cheval..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`
- **Extracted Stylesheet Rules (`andreas-vision`)**:
- `root { height: 100%; margin: 0; }`
- `html { background: fff; }`
- **Per-Selector Transition Rules**:
- **Selector `style]`**: `transition: none` extracted from `andreas-vision` stylesheet.
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in captured CSS).
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `andreas-vision`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
