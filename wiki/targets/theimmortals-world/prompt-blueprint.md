---
title: "UI Prompt Blueprint: theimmortals-world"
date: 2026-11-15
target: "[[overview|theimmortals-world]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#efefef` / `#f1f1f1`)"
---

# UI Design System & Master Generation Blueprint: theimmortals-world

> **The Immortals** (https://theimmortals.world/) — An interactive journey through the history of the FIFA World Cup, celebrating every tournament from 1930 to 2022 through iconic moments,...

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/theimmortals-world/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **The Immortals** (`https://theimmortals.world/`). An interactive journey through the history of the FIFA World Cup, celebrating every tournament from 1930 to 2022 through iconic moments,...
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#efefef` / `#f1f1f1`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#efefef` (`html { background-color: #efefef }`) paired with `#000` primary typography and `#f1f1f1` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Bricolage Grotesque` for display copy (`The Immortals`) with `Bricolage Grotesque` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `91rem` container bounds (`gap: 20.5rem`, padding `.2rem`) with `cubic-bezier(0.25,0.1,0.25,1)` easing and HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/theimmortals-world/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `91rem` extracted from `theimmortals-world` stylesheet.
- **Canvas Lateral Padding & Spacing**: `.2rem` lateral canvas padding with `20.5rem` grid gap.
- **Border Radius Scale**: `5px`, `5%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 91rem`, `gap: 20.5rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `.2rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (width<=768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#efefef` | `html { background-color: #efefef }` |
| **Primary Typography Ink** | `#121212` | `body { color: #121212 }` |
| **Elevated Surface / Card Substrate** | `#1a1a1a` | `#loader { color: #1a1a1a }` |
| **Interactive Accent / Highlight** | `#f1f1f1` | `#loader { background: #f1f1f1 }` |
| **Secondary / Muted Copy** | `#004cff` | `#g_w div { background: #004cff }` |
| **Structural Hairline Border** | `#000` | `.dots { border-bottom: #000 }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--theimmortals-wor-bg` | `#efefef` | Canvas Substrate (from `html { background-color: #efefef }`) |
| `--theimmortals-wor-ink` | `#000` | Primary Typography Ink (stylesheet-derived) |
| `--theimmortals-wor-surface` | `#1a1a1a` | Surface Substrate (stylesheet-derived) |
| `--theimmortals-wor-accent` | `#f1f1f1` | Interactive Accent (stylesheet-derived) |
| `--theimmortals-wor-muted` | `#004cff` | Secondary Ink (stylesheet-derived) |
| `--theimmortals-wor-border` | `#000` | Structural Border (stylesheet-derived) |
| `--theimmortals-wor-container` | `91rem` | Container Bound (stylesheet-derived) |
| `--theimmortals-wor-gap` | `20.5rem` | Grid Gutter (stylesheet-derived) |
| `--theimmortals-wor-pad` | `.2rem` | Lateral Padding (stylesheet-derived) |
| `--theimmortals-wor-ease` | `cubic-bezier(0.25,0.1,0.25,1)` | Primary Easing Function |
| `--theimmortals-wor-radius` | `5px` | Corner Radius (stylesheet-derived) |
| `--theimmortals-wor-fs-base` | `28rem` | Observed Font Size Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Bricolage Grotesque`.
- **Primary Body Stack**: `Bricolage Grotesque`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `28rem`, `12rem`, `14rem`, `8rem`, `10rem`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `28rem`, `12rem`, `14rem`, `8rem`, `10rem`).
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `28rem`, `12rem`, `14rem`, `8rem`, `10rem`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `28rem`, `12rem`, `14rem`, `8rem`, `10rem`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.yr-item`**: `transition: opacity .4s ease-in` extracted from `theimmortals-world` stylesheet.
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in static CSS).
- **Runtime Interaction Engine**: Integrates HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — The Immortals                              │
│ ====================================================================== │
│ [ <nav.nav-w>              | The Immortals                          ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.ti>                                         |   │
│ | H1: The Immortals                                                |   │
│ | Substrate: #efefef    | Ink: #000       | Accent: #f1f1f1        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.nav-menu>        ) max-w: 91rem          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Featured Work & Interactive  |  | Technical Architecture & Nar | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 20.5re) | │
│ | [<nav.nav-w>] -> [<section.ti>] -> [<section.nav-menu>] |            │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.m-ti>         ) | https://theimmortals.world/        │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.nav-w> — `theimmortals-world`)**:
   - Landmark `<nav class="nav-w">` hosting `The Immortals` navigation (`The Immortals`), DOM attributes (`data-tr="menu"`, `data-media="https://images.prismi..."`, `data-tr="menu"`, `data-media="https://images.prismi..."`), and stylesheet rule `after { box-sizing:border-box;-webkit-user-select:none;user-select:none }`.
2. **Hero Stage & Focal Lead (<section.ti> — `The Immortals`)**:
   - Landmark `<section class="ti">` presenting display lead `The Immortals` and copy excerpt *"Designer, Developer Jason Jerez"* over `#efefef` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.nav-menu> — `Featured Work & Interactive Showca`)**:
   - Landmark `<section class="nav-menu">` rendering section `Featured Work & Interactive Showcase` with copy *"Designer, Developer"*, asset references (`theimmortals.world`, `main.css`, `favicon-96x96.png`, `favicon.svg`), and grid rule `body { -webkit-font-smoothing:antialiased;text-rendering:optimizespeed }`.
4. **Interactive Detail & Feature Matrix (<section.menu-wr> — `Technical Architecture & Narrative`)**:
   - Landmark `<section class="menu-wr">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"The story continues"*) with `#1a1a1a` surface cards, `#f1f1f1` accents, and `svg { max-width:100%;display:block }`.
5. **Colophon & Global Directory Footer (<footer.m-ti> — `https://theimmortals.world/`)**:
   - Landmark `<footer class="m-ti">` anchoring `The Immortals` footer links (`The Immortals`), copy *"The Return of La Roja"*, and `#000` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: theimmortals-world (The Immortals)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `theimmortals-world` (**The Immortals** — `https://theimmortals.world/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#efefef` / `#f1f1f1`).
- **Identity & Domain Context**: An interactive journey through the history of the FIFA World Cup, celebrating every tournament from 1930 to 2022 through iconic moments,...
- **Primary Substrate**: `#efefef` (`html { background-color: #efefef }`), **Primary Ink**: `#000`, **Accent / Highlight**: `#f1f1f1`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#efefef` (`html { background-color: #efefef }`) paired with `#000` primary typography and `#f1f1f1` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Bricolage Grotesque` for display copy (`The Immortals`) with `Bricolage Grotesque` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `91rem` container bounds (`gap: 20.5rem`, padding `.2rem`) with `cubic-bezier(0.25,0.1,0.25,1)` easing and HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `theimmortals-world` in your global stylesheet:

:root {
  /* The Immortals (theimmortals-world) — Ground-Truth Extracted CSS Variables */
  --theimmortals-wor-bg: #efefef; /* Canvas Substrate (from `html { background-color: #efefef }`) (theimmortals-world) */
  --theimmortals-wor-ink: #000; /* Primary Typography Ink (stylesheet-derived) (theimmortals-world) */
  --theimmortals-wor-surface: #1a1a1a; /* Surface Substrate (stylesheet-derived) (theimmortals-world) */
  --theimmortals-wor-accent: #f1f1f1; /* Interactive Accent (stylesheet-derived) (theimmortals-world) */
  --theimmortals-wor-muted: #004cff; /* Secondary Ink (stylesheet-derived) (theimmortals-world) */
  --theimmortals-wor-border: #000; /* Structural Border (stylesheet-derived) (theimmortals-world) */
  --theimmortals-wor-container: 91rem; /* Container Bound (stylesheet-derived) (theimmortals-world) */
  --theimmortals-wor-gap: 20.5rem; /* Grid Gutter (stylesheet-derived) (theimmortals-world) */
  --theimmortals-wor-pad: .2rem; /* Lateral Padding (stylesheet-derived) (theimmortals-world) */
  --theimmortals-wor-ease: cubic-bezier(0.25,0.1,0.25,1); /* Primary Easing Function (theimmortals-world) */
  --theimmortals-wor-radius: 5px; /* Corner Radius (stylesheet-derived) (theimmortals-world) */
  --theimmortals-wor-fs-base: 28rem; /* Observed Font Size Token (theimmortals-world) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#efefef` — grounded in `html { background-color: #efefef }`
- **Primary Typography Ink**: `#121212` — grounded in `body { color: #121212 }`
- **Elevated Surface / Card Substrate**: `#1a1a1a` — grounded in `#loader { color: #1a1a1a }`
- **Interactive Accent / Highlight**: `#f1f1f1` — grounded in `#loader { background: #f1f1f1 }`
- **Secondary / Muted Copy**: `#004cff` — grounded in `#g_w div { background: #004cff }`
- **Structural Hairline Border**: `#000` — grounded in `.dots { border-bottom: #000 }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `91rem` extracted from `theimmortals-world` stylesheet
- **Padding & Gutters**: `.2rem` lateral canvas padding with `20.5rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 91rem`, `gap: 20.5rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `.2rem` horizontal padding
- **Media Queries**: `@media (width<=768px)`
- **Corner Radii**: `5px`, `5%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Bricolage Grotesque`
- **Body Font Stack**: `Bricolage Grotesque`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `28rem`, `12rem`, `14rem`, `8rem`, `10rem`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `28rem`, `12rem`, `14rem`, `8rem`, `10rem`)
- **Body Copy Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `28rem`, `12rem`, `14rem`, `8rem`, `10rem`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `28rem`, `12rem`, `14rem`, `8rem`, `10rem`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `theimmortals-world` (`The Immortals`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.nav-w> — `theimmortals-world`)**:
   - DOM & Selectors: Landmark `<nav class="nav-w">` hosting `The Immortals` navigation (`The Immortals`), DOM attributes (`data-tr="menu"`, `data-media="https://images.prismi..."`, `data-tr="menu"`, `data-media="https://images.prismi..."`), and stylesheet rule `after { box-sizing:border-box;-webkit-user-select:none;user-select:none }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.nav-w> — `theimmortals-world`)` (`theimmortals-world`) adapts across `@media (width<=768px)` with `cubic-bezier(0.25,0.1,0.25,1)` transitions and links `The Immortals`.
2. **Hero Stage & Focal Lead (<section.ti> — `The Immortals`)**:
   - DOM & Selectors: Landmark `<section class="ti">` presenting display lead `The Immortals` and copy excerpt *"Designer, Developer Jason Jerez"* over `#efefef` canvas and `#000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#efefef` background with `#000` headline `The Immortals`.
3. **Primary Showcase & Content Grid (<section.nav-menu> — `Featured Work & Interactive Showca`)**:
   - DOM & Selectors: Landmark `<section class="nav-menu">` rendering section `Featured Work & Interactive Showcase` with copy *"Designer, Developer"*, asset references (`theimmortals.world`, `main.css`, `favicon-96x96.png`, `favicon.svg`), and grid rule `body { -webkit-font-smoothing:antialiased;text-rendering:optimizespeed }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.nav-menu> — `Featured Work & Interactive Showca`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 91rem`, `gap: 20.5rem`) on desktop and Single-column vertical stack at `390px` viewport width with `.2rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.menu-wr> — `Technical Architecture & Narrative`)**:
   - DOM & Selectors: Landmark `<section class="menu-wr">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"The story continues"*) with `#1a1a1a` surface cards, `#f1f1f1` accents, and `svg { max-width:100%;display:block }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.menu-wr> — `Technical Architecture & Narrative`)` uses `5px`, `5%` radii, `#f1f1f1` highlights, and assets (theimmortals.world, main.css, favicon-96x96.png).
5. **Colophon & Global Directory Footer (<footer.m-ti> — `https://theimmortals.world/`)**:
   - DOM & Selectors: Landmark `<footer class="m-ti">` anchoring `The Immortals` footer links (`The Immortals`), copy *"The Return of La Roja"*, and `#000` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.m-ti> — `https://theimmortals.world/`)` aligns to `91rem` extracted from `theimmortals-world` stylesheet with `.2rem` lateral canvas padding with `20.5rem` grid gap and attributes (data-tr="menu", data-media="https://images.prismi...", data-tr="menu").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Designer, Developer Jason Jerez"*
- Copy Excerpt 2: *"Designer, Developer"*
- Copy Excerpt 3: *"The story continues"*
- Copy Excerpt 4: *"The Return of La Roja"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`
- **Extracted Stylesheet Rules (`theimmortals-world`)**:
- `after { box-sizing:border-box;-webkit-user-select:none;user-select:none }`
- `body { -webkit-font-smoothing:antialiased;text-rendering:optimizespeed }`
- `svg { max-width:100%;display:block }`
- `select { font:inherit }`
- `img { -webkit-user-drag:none;-khtml-user-drag:none;-moz-user-drag:none;-o-user... }`
- **Per-Selector Transition Rules**:
- **Selector `.yr-item`**: `transition: opacity .4s ease-in` extracted from `theimmortals-world` stylesheet.
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in static CSS).
- **Runtime Interaction Engine**: Integrates HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `theimmortals-world`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
