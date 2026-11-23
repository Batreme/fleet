---
title: "UI Prompt Blueprint: www-tokonoma-xyz"
date: 2026-11-23
captured_at: 2026-11-23
target: "www-tokonoma-xyz"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#baff00`)"
---

# UI Design System & Master Generation Blueprint: www-tokonoma-xyz

> **Tokonoma Studio — Image Making, Art, AI & Creative Direction** (https://www.tokonoma.xyz/) — Tokonoma is an image-making studio working across analogue and AI photography, animation, creative coding, art and digital experiences. C...

![Desktop Viewport Capture (1440x900)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Tokonoma Studio — Image Making, Art, AI & Creative Direction** (`https://www.tokonoma.xyz/`). Tokonoma is an image-making studio working across analogue and AI photography, animation, creative coding, art and digital experiences. C...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#baff00`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#000000` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#baff00` accents.
  - **Grounded Typographic Hierarchy**: Pairs `EurostileMNExtendedBold` for display copy (`Tokonoma Studio — Image Making, Art,`) with `EurostileMNExtendedBold` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 32px`, padding `20px`) with `cubic-bezier(.22,1,.36,1)` easing and HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x844)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×900px` (`assets/desktop.png`, single-viewport 100vh live capture (900px)), Mobile `390×844px` (`assets/mobile.png`, single-viewport 100vh live capture (844px)).
- **Master Container Bounds**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport).
- **Canvas Lateral Padding & Spacing**: `20px` lateral canvas padding with `32px` grid gap.
- **Border Radius Scale**: `999px`, `50%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 32px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `20px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width: 700px), (hover: none) and (pointer: coarse) a...`, `@media (max-width: 1100px), (hover: none) and (pointer: coarse)`, `@media (prefers-reduced-motion: reduce) and (min-width: 1101px)...`, `@media (prefers-reduced-motion: reduce)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#141414` | `var(--color-panel)` in `:root` |
| **Interactive Accent / Highlight** | `#baff00` | `var(--cursor-color)` in `:root` |
| **Secondary / Muted Copy** | `#5f5f5f` | `var(--color-muted)` in `:root` |
| **Structural Hairline Border** | `#767676` | `.points-border .ants-white { stroke: #767676 }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--cursor-color` | `#baff00` | Brand / Palette Token |
| `--color-muted` | `#5f5f5f` | Brand / Palette Token |
| `--color-panel` | `#141414` | Brand / Palette Token |
| `--www-tokonoma-xyz-bg` | `#000000` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--www-tokonoma-xyz-ink` | `#ffffff` | Primary Typography Ink (computed-derived) |
| `--www-tokonoma-xyz-surface` | `#141414` | Surface Substrate (computed-derived) |
| `--www-tokonoma-xyz-accent` | `#baff00` | Interactive Accent (computed-derived) |
| `--www-tokonoma-xyz-muted` | `#5f5f5f` | Secondary Ink (computed-derived) |
| `--www-tokonoma-xyz-border` | `#767676` | Structural Border (computed-derived) |
| `--www-tokonoma-xyz-container` | `1440px` | Container Bound (computed-derived) |
| `--www-tokonoma-xyz-gap` | `32px` | Grid Gutter (computed-derived) |
| `--www-tokonoma-xyz-pad` | `20px` | Lateral Padding (computed-derived) |
| `--www-tokonoma-xyz-ease` | `cubic-bezier(.22,1,.36,1)` | Primary Easing Function |
| `--www-tokonoma-xyz-radius` | `999px` | Corner Radius (computed-derived) |
| `--www-tokonoma-xyz-fs-base` | `16px` | Observed Font Size Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `EurostileMNExtendedBold`.
- **Primary Body Stack**: `EurostileMNExtendedBold`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: rule `h1` (`letter-spacing: .02em`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 24px`, `line-height: 1.05`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 700`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.65,0,.35,1)`, `cubic-bezier(.55,0,.15,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.mobile-wheel-thumb-track`**: `transition: transform .34s cubic-bezier(.22,1,.36,1)` extracted from `www-tokonoma-xyz` stylesheet.
- **Selector `.mobile-wheel-thumb-frame`**: `transition: opacity .22s ease` extracted from `www-tokonoma-xyz` stylesheet.
- **Selector `bile-project-wheel .mobile-wheel-...`**: `transition: background-color .3s linear` extracted from `www-tokonoma-xyz` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,1,.36,1)`)**: Governs interactive state transitions across `<nav.interface>` and `<main.entry-main:nth(2)>`.
- **Runtime Interaction Engine**: Integrates HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Tokonoma Studio — Image Making, Art, AI &  │
│ ====================================================================== │
│ [ <nav.interface> (1440x900px)        | ABOUT · SHOWS                ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <main.entry-main> (w=1440px)                           | │
│ | H1: Tokonoma Studio — Image Making, Art, AI & Creati               | │
│ | Substrate: #000000 | Ink: #ffffff | Accent: #baff00                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<main.entry-main:nth(2)>) max-w: 1440px             | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Featured Work & Interactive  |  | Technical Architecture & Nar | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<main.entry-main:nth(3)>) — Global Directory & Co   | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.tokonoma-log) | https://www.tokonoma.xyz/            │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 32px)       │
│ ====================================================================== │
│ [ HEADER BAR (<nav.interface>         ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<main.entry-main>) — 390px Vertical Lead               | │
│ | H1: Tokonoma Studio — Image Making, Art, AI & Creati               | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<main.entry-main:nth(2) — 1-Col Stack              | │
│ | [ Item 1: Featured Work & Interactive Showcase                   ] | │
│ | [ Item 2: Technical Architecture & Narrative                     ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<main.entry-main:nth(3)>) — 1-Col (Global Directory &) │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.tokonoma-log) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.interface> — `www-tokonoma-xyz`)**:
   - Landmark `<nav class="interface">` (`1440x900px`) hosting `Tokonoma Studio — Image Making, Art,` navigation (`ABOUT · SHOWS`), DOM attributes (`data-target="www-tokonoma-xyz"`), and stylesheet rule `property --angle-1 { syntax: "<angle>"; inherits: false; initial-value: -75deg; }`.
2. **Hero Stage & Focal Lead (<main.entry-main> — `Tokonoma Studio — Image Making, Ar`)**:
   - Landmark `<main class="entry-main">` presenting display lead `Tokonoma Studio — Image Making, Art, AI & Creati` and copy excerpt *"Tokonoma is an image-making studio working across analogue and AI"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<main.entry-main:nth(2)> — `Featured Work & Interactive Showca`)**:
   - Landmark `<main class="entry-main">` rendering section `Featured Work & Interactive Showcase` with copy *"Tokonoma Studio — Image Making, Art, AI & Creati"*, asset references (`EurostileMNExtendedBold.ttf`, `favicon-32x32-dm.png`, `styles.css`, `tokonoma_logo.png (Tokonoma)`), and grid rule `property --angle-2 { syntax: "<angle>"; inherits: false; initial-value: -45deg; }`.
4. **Interactive Detail & Feature Matrix (<main.entry-main:nth(3)> — `Technical Architecture & Narrative`)**:
   - Landmark `<main class="entry-main">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Work & Interactive Showcase"*) with `#141414` surface cards, `#baff00` accents, and `html.mobile-project-wheel .viewer... { inset: 160px 0 64px 0; }`.
5. **Colophon & Global Directory Footer (<footer.tokonoma-logo-frame> — `https://www.tokonoma.xyz/`)**:
   - Landmark `<footer class="tokonoma-logo-frame">` anchoring `Tokonoma Studio — Image Making, ` footer links (`ABOUT · SHOWS`), copy *"Technical Architecture & Narrative"*, and `#767676` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-tokonoma-xyz (Tokonoma Studio — Image Making, Art, AI & Creative Direction)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-tokonoma-xyz` (**Tokonoma Studio — Image Making, Art, AI & Creative Direction** — `https://www.tokonoma.xyz/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#baff00`).
- **Identity & Domain Context**: Tokonoma is an image-making studio working across analogue and AI photography, animation, creative coding, art and digital experiences. C...
- **Primary Substrate**: `#000000` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#ffffff`, **Accent / Highlight**: `#baff00`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#000000` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#baff00` accents.
  - **Grounded Typographic Hierarchy**: Pairs `EurostileMNExtendedBold` for display copy (`Tokonoma Studio — Image Making, Art,`) with `EurostileMNExtendedBold` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 32px`, padding `20px`) with `cubic-bezier(.22,1,.36,1)` easing and HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-tokonoma-xyz` in your global stylesheet:

:root {
  /* Tokonoma Studio — Image Making, Art, AI & Creative Direction (www-tokonoma-xyz) — Live-Grounded CSS Variables */
  --cursor-color: #baff00; /* Brand / Palette Token (www-tokonoma-xyz) */
  --color-muted: #5f5f5f; /* Brand / Palette Token (www-tokonoma-xyz) */
  --color-panel: #141414; /* Brand / Palette Token (www-tokonoma-xyz) */
  --www-tokonoma-xyz-bg: #000000; /* Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) (www-tokonoma-xyz) */
  --www-tokonoma-xyz-ink: #ffffff; /* Primary Typography Ink (computed-derived) (www-tokonoma-xyz) */
  --www-tokonoma-xyz-surface: #141414; /* Surface Substrate (computed-derived) (www-tokonoma-xyz) */
  --www-tokonoma-xyz-accent: #baff00; /* Interactive Accent (computed-derived) (www-tokonoma-xyz) */
  --www-tokonoma-xyz-muted: #5f5f5f; /* Secondary Ink (computed-derived) (www-tokonoma-xyz) */
  --www-tokonoma-xyz-border: #767676; /* Structural Border (computed-derived) (www-tokonoma-xyz) */
  --www-tokonoma-xyz-container: 1440px; /* Container Bound (computed-derived) (www-tokonoma-xyz) */
  --www-tokonoma-xyz-gap: 32px; /* Grid Gutter (computed-derived) (www-tokonoma-xyz) */
  --www-tokonoma-xyz-pad: 20px; /* Lateral Padding (computed-derived) (www-tokonoma-xyz) */
  --www-tokonoma-xyz-ease: cubic-bezier(.22,1,.36,1); /* Primary Easing Function (www-tokonoma-xyz) */
  --www-tokonoma-xyz-radius: 999px; /* Corner Radius (computed-derived) (www-tokonoma-xyz) */
  --www-tokonoma-xyz-fs-base: 16px; /* Observed Font Size Token (www-tokonoma-xyz) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000000` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#ffffff` — grounded in live computed `main` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#141414` — grounded in `var(--color-panel)` in `:root`
- **Interactive Accent / Highlight**: `#baff00` — grounded in `var(--cursor-color)` in `:root`
- **Secondary / Muted Copy**: `#5f5f5f` — grounded in `var(--color-muted)` in `:root`
- **Structural Hairline Border**: `#767676` — grounded in `.points-border .ants-white { stroke: #767676 }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×900px` (single-viewport 100vh live capture (900px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×844px` (single-viewport 100vh live capture (844px), `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport)
- **Padding & Gutters**: `20px` lateral canvas padding with `32px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 32px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `20px` horizontal padding
- **Media Queries**: `@media (max-width: 700px), (hover: none) and (pointer: coarse) a...`, `@media (max-width: 1100px), (hover: none) and (pointer: coarse)`, `@media (prefers-reduced-motion: reduce) and (min-width: 1101px)...`, `@media (prefers-reduced-motion: reduce)`
- **Corner Radii**: `999px`, `50%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `EurostileMNExtendedBold`
- **Body Font Stack**: `EurostileMNExtendedBold`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: rule `h1` (`letter-spacing: .02em`)
- **H2 Section Rule**: rule `h2` (`font-size: 24px`, `line-height: 1.05`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 700`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-tokonoma-xyz` (`Tokonoma Studio — Image Making, Art, AI & Creative Direction`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.interface> — `www-tokonoma-xyz`)**:
   - DOM & Selectors: Landmark `<nav class="interface">` (`1440x900px`) hosting `Tokonoma Studio — Image Making, Art,` navigation (`ABOUT · SHOWS`), DOM attributes (`data-target="www-tokonoma-xyz"`), and stylesheet rule `property --angle-1 { syntax: "<angle>"; inherits: false; initial-value: -75deg; }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.interface> — `www-tokonoma-xyz`)` (`www-tokonoma-xyz`) adapts across `@media (max-width: 700px), (hover: none) and (pointer: coarse) a...`, `@media (max-width: 1100px), (hover: none) and (pointer: coarse)`, `@media (prefers-reduced-motion: reduce) and (min-width: 1101px)...`, `@media (prefers-reduced-motion: reduce)` with `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.65,0,.35,1)`, `cubic-bezier(.55,0,.15,1)` transitions and links `ABOUT · SHOWS`.
2. **Hero Stage & Focal Lead (<main.entry-main> — `Tokonoma Studio — Image Making, Ar`)**:
   - DOM & Selectors: Landmark `<main class="entry-main">` presenting display lead `Tokonoma Studio — Image Making, Art, AI & Creati` and copy excerpt *"Tokonoma is an image-making studio working across analogue and AI"* over `#000000` canvas and `#ffffff` ink.
   - Responsive Contract: Hero stage (`1440×900px` desktop / `390×844px` mobile) sets `#000000` background with `#ffffff` headline `Tokonoma Studio — Image Making, Art, AI & Creati`.
3. **Primary Showcase & Content Grid (<main.entry-main:nth(2)> — `Featured Work & Interactive Showca`)**:
   - DOM & Selectors: Landmark `<main class="entry-main">` rendering section `Featured Work & Interactive Showcase` with copy *"Tokonoma Studio — Image Making, Art, AI & Creati"*, asset references (`EurostileMNExtendedBold.ttf`, `favicon-32x32-dm.png`, `styles.css`, `tokonoma_logo.png (Tokonoma)`), and grid rule `property --angle-2 { syntax: "<angle>"; inherits: false; initial-value: -45deg; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<main.entry-main:nth(2)> — `Featured Work & Interactive Showca`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 32px`) on desktop and Single-column vertical stack at `390px` viewport width with `20px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<main.entry-main:nth(3)> — `Technical Architecture & Narrative`)**:
   - DOM & Selectors: Landmark `<main class="entry-main">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Work & Interactive Showcase"*) with `#141414` surface cards, `#baff00` accents, and `html.mobile-project-wheel .viewer... { inset: 160px 0 64px 0; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<main.entry-main:nth(3)> — `Technical Architecture & Narrative`)` uses `999px`, `50%` radii, `#baff00` highlights, and assets (EurostileMNExtendedBold.ttf, favicon-32x32-dm.png, styles.css).
5. **Colophon & Global Directory Footer (<footer.tokonoma-logo-frame> — `https://www.tokonoma.xyz/`)**:
   - DOM & Selectors: Landmark `<footer class="tokonoma-logo-frame">` anchoring `Tokonoma Studio — Image Making, ` footer links (`ABOUT · SHOWS`), copy *"Technical Architecture & Narrative"*, and `#767676` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.tokonoma-logo-frame> — `https://www.tokonoma.xyz/`)` aligns to `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport) with `20px` lateral canvas padding with `32px` grid gap and attributes (www-tokonoma-xyz).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Lead Copy: *"Tokonoma is an image-making studio working across analogue and AI photography, animation, creative coding, art and digital experiences. C..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.65,0,.35,1)`, `cubic-bezier(.55,0,.15,1)`
- **Extracted Stylesheet Rules (`www-tokonoma-xyz`)**:
- `property --angle-1 { syntax: "<angle>"; inherits: false; initial-value: -75deg; }`
- `property --angle-2 { syntax: "<angle>"; inherits: false; initial-value: -45deg; }`
- `html.mobile-project-wheel .viewer... { inset: 160px 0 64px 0; }`
- `project-wheel .viewer-menu-list.c... { padding-top: calc((100dvh - 224px) / 2 - 34px); padding-bottom: calc((10... }`
- `.mobile-wheel-thumb-row { display: none; }`
- **Per-Selector Transition Rules**:
- **Selector `.mobile-wheel-thumb-track`**: `transition: transform .34s cubic-bezier(.22,1,.36,1)` extracted from `www-tokonoma-xyz` stylesheet.
- **Selector `.mobile-wheel-thumb-frame`**: `transition: opacity .22s ease` extracted from `www-tokonoma-xyz` stylesheet.
- **Selector `bile-project-wheel .mobile-wheel-...`**: `transition: background-color .3s linear` extracted from `www-tokonoma-xyz` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,1,.36,1)`)**: Governs interactive state transitions across `<nav.interface>` and `<main.entry-main:nth(2)>`.
- **Runtime Interaction Engine**: Integrates HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-tokonoma-xyz`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
