---
title: "UI Prompt Blueprint: ofrenda-davidlangarica-dev"
date: 2026-11-15
target: "[[overview|ofrenda-davidlangarica-dev]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#ef893b`)"
---

# UI Design System & Master Generation Blueprint: ofrenda-davidlangarica-dev

> **OFRENDA — Create a personal Día de Muertos altar** (https://ofrenda.davidlangarica.dev) — Create a personal Día de Muertos ofrenda with a photograph, flowers, candles, and meaningful offerings. A quiet place to remember someone...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **OFRENDA — Create a personal Día de Muertos altar** (`https://ofrenda.davidlangarica.dev`). Create a personal Día de Muertos ofrenda with a photograph, flowers, candles, and meaningful offerings. A quiet place to remember someone...
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#ef893b`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--ui-backdrop)` in `:root`) paired with `#f4e6cf` primary typography and `#ef893b` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Marqen` for display copy (`OFRENDA`) with `Macario` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `600px` container bounds (`gap: 8px`, padding `6px`) with `cubic-bezier(.22,.68,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `600px` extracted from `ofrenda-davidlangarica-dev` stylesheet.
- **Canvas Lateral Padding & Spacing**: `6px` lateral canvas padding with `8px` grid gap.
- **Border Radius Scale**: `50%`, `4px`, `5px`, `2px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 600px`, `gap: 8px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `6px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:600px)`, `@media (max-height:500px)and (min-aspect-ratio:1.15/1)`, `@media (max-height:700px)`, `@media (prefers-reduced-motion:reduce)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--ui-backdrop)` in `:root` |
| **Primary Typography Ink** | `#f4e6cf` | `var(--ui-text)` in `:root` |
| **Elevated Surface / Card Substrate** | `#d5c4a9` | `var(--ui-muted)` in `:root` |
| **Interactive Accent / Highlight** | `#ef893b` | `var(--ui-heading)` in `:root` |
| **Secondary / Muted Copy** | `#f3e3c7` | `var(--ui-home-heading)` in `:root` |
| **Structural Hairline Border** | `#efd6a4` | `var(--ui-focus)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ui-font-heading` | `"Marqen", Georgia, "Times New Roman", serif` | Typography Ink Token |
| `--ui-font-body` | `Georgia, "Times New Roman", serif` | Typography / Scale Token |
| `--ui-text-shadow` | `0 2px 14px #000` | Typography Ink Token |
| `--ui-backdrop` | `#000` | Color / Atmospheric Token |
| `--ui-text` | `#f4e6cf` | Typography Ink Token |
| `--ui-muted` | `#d5c4a9` | Color / Atmospheric Token |
| `--ui-heading` | `#ef893b` | Typography Ink Token |
| `--ui-home-heading` | `#f3e3c7` | Typography Ink Token |
| `--ui-amber-rgb` | `189 149 91` | Design System Custom Token |
| `--ui-amber` | `rgb(var(--ui-amber-rgb))` | Color / Atmospheric Token |
| `--ui-surface-rgb` | `70 39 17` | Canvas / Surface Token |
| `--ui-surface` | `rgb(var(--ui-surface-rgb) / .18)` | Canvas / Surface Token |
| `--ui-surface-hover` | `rgb(160 110 49 / .2)` | Canvas / Surface Token |
| `--ui-surface-pressed` | `rgb(184 133 67 / .28)` | Canvas / Surface Token |
| `--ui-border` | `rgb(var(--ui-amber-rgb) / .74)` | Elevation / Border Token |
| `--ui-focus` | `#efd6a4` | Color / Atmospheric Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Marqen`.
- **Primary Body Stack**: `Macario`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`font-size: clamp(44px,12vw,72px)`, `line-height: 1.08`, `font-weight: 400`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 30px`, `line-height: 1.1`).
- **Body Copy**: CSS variables `--ui-font-body: Georgia, "Times New Roman", serif`, `--ui-body-size: clamp(16px, 1.5vw, 19px)`, `--ui-body-line-height: 1.55`; rule `p` (`font-size: 16px`, `line-height: 1.4`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `clamp(44px,12vw,72px)`, `16px`, `30px`, `13px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.22,.68,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.lenis.lenis-autoToggle`**: `transition: 1ms` extracted from `ofrenda-davidlangarica-dev` stylesheet.
- **Selector `.canvas-layer`**: `transition: bottom .32s ease` extracted from `ofrenda-davidlangarica-dev` stylesheet.
- **Selector `media(prefers-reduced-motion:reduce)`**: `transition: .08s` extracted from `ofrenda-davidlangarica-dev` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,.68,.2,1)`)**: Governs interactive state transitions across `<header.experience-chrome>` and `<section.floating-menu>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — OFRENDA — Create a personal Día de Muertos │
│ ====================================================================== │
│ [ <header.experience-chrom | David Langarica                        ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.floating-menu>                              |   │
│ | H1: OFRENDA                                                      |   │
│ | Substrate: #000       | Ink: #f4e6cf    | Accent: #ef893b        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.floating-menu>   ) max-w: 600px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | OFRENDA — A place to remembe |  | Language Choose English or S | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 8px   ) | │
│ | [<header.experience] -> [<section.floating-] -> [<section.floating-] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.menu-footer>  ) | https://ofrenda.davidlangarica.dev │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.experience-chrome> — `ofrenda-davidlangarica-dev`)**:
   - Landmark `<header class="experience-chrome">` hosting `OFRENDA — Create a personal Día de M` navigation (`David Langarica`), DOM attributes (`data-cf-beacon="("token":"e723bd39f9d..."`, `data-engine="three.js r180 webgpu"`, `data-on="true"`, `data-loading-progress="0.9"`), and stylesheet rule `html.lenis body { height:auto }`.
2. **Hero Stage & Focal Lead (<section.floating-menu> — `OFRENDA`)**:
   - Landmark `<section class="floating-menu">` presenting display lead `OFRENDA` and copy excerpt *"For you, who still have a place here."* over `#000` canvas and `#f4e6cf` ink.
3. **Primary Showcase & Content Grid (<section.floating-menu> — `OFRENDA — A place to remember`)**:
   - Landmark `<section class="floating-menu">` rendering section `OFRENDA — A place to remember` with copy *"Language Choose English or Spanish."*, asset references (`favicon.ico`, `Marqen.woff2`, `index-CUtJAqPO.js`, `index-BRkV915_.css`), and grid rule `.lenis-stopped { overflow:clip }`.
4. **Interactive Detail & Feature Matrix (<section.floating-menu> — `Language Choose English or Spanish`)**:
   - Landmark `<section class="floating-menu">` framing `Language Choose English or Spanish.` and `Sound Music and ambience.` (*"Sound Music and ambience."*) with `#d5c4a9` surface cards, `#ef893b` accents, and `.lenis.lenis-smooth iframe { pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.menu-footer> — `https://ofrenda.davidlangarica.dev`)**:
   - Landmark `<footer class="menu-footer">` anchoring `OFRENDA — Create a personal Día ` footer links (`David Langarica`), copy *"Graphics Available after the water and salt."*, and `#efd6a4` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: ofrenda-davidlangarica-dev (OFRENDA — Create a personal Día de Muertos altar)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `ofrenda-davidlangarica-dev` (**OFRENDA — Create a personal Día de Muertos altar** — `https://ofrenda.davidlangarica.dev`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#ef893b`).
- **Identity & Domain Context**: Create a personal Día de Muertos ofrenda with a photograph, flowers, candles, and meaningful offerings. A quiet place to remember someone...
- **Primary Substrate**: `#000` (`var(--ui-backdrop)` in `:root`), **Primary Ink**: `#f4e6cf`, **Accent / Highlight**: `#ef893b`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--ui-backdrop)` in `:root`) paired with `#f4e6cf` primary typography and `#ef893b` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Marqen` for display copy (`OFRENDA`) with `Macario` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `600px` container bounds (`gap: 8px`, padding `6px`) with `cubic-bezier(.22,.68,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `ofrenda-davidlangarica-dev` in your global stylesheet:

:root {
  /* OFRENDA — Create a personal Día de Muertos altar (ofrenda-davidlangarica-dev) — Ground-Truth Extracted CSS Variables */
  --ui-font-heading: "Marqen", Georgia, "Times New Roman", serif; /* Typography Ink Token (ofrenda-davidlangarica-dev) */
  --ui-font-body: Georgia, "Times New Roman", serif; /* Typography / Scale Token (ofrenda-davidlangarica-dev) */
  --ui-text-shadow: 0 2px 14px #000; /* Typography Ink Token (ofrenda-davidlangarica-dev) */
  --ui-backdrop: #000; /* Color / Atmospheric Token (ofrenda-davidlangarica-dev) */
  --ui-text: #f4e6cf; /* Typography Ink Token (ofrenda-davidlangarica-dev) */
  --ui-muted: #d5c4a9; /* Color / Atmospheric Token (ofrenda-davidlangarica-dev) */
  --ui-heading: #ef893b; /* Typography Ink Token (ofrenda-davidlangarica-dev) */
  --ui-home-heading: #f3e3c7; /* Typography Ink Token (ofrenda-davidlangarica-dev) */
  --ui-amber-rgb: 189 149 91; /* Design System Custom Token (ofrenda-davidlangarica-dev) */
  --ui-amber: rgb(var(--ui-amber-rgb)); /* Color / Atmospheric Token (ofrenda-davidlangarica-dev) */
  --ui-surface-rgb: 70 39 17; /* Canvas / Surface Token (ofrenda-davidlangarica-dev) */
  --ui-surface: rgb(var(--ui-surface-rgb) / .18); /* Canvas / Surface Token (ofrenda-davidlangarica-dev) */
  --ui-surface-hover: rgb(160 110 49 / .2); /* Canvas / Surface Token (ofrenda-davidlangarica-dev) */
  --ui-surface-pressed: rgb(184 133 67 / .28); /* Canvas / Surface Token (ofrenda-davidlangarica-dev) */
  --ui-border: rgb(var(--ui-amber-rgb) / .74); /* Elevation / Border Token (ofrenda-davidlangarica-dev) */
  --ui-focus: #efd6a4; /* Color / Atmospheric Token (ofrenda-davidlangarica-dev) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000` — grounded in `var(--ui-backdrop)` in `:root`
- **Primary Typography Ink**: `#f4e6cf` — grounded in `var(--ui-text)` in `:root`
- **Elevated Surface / Card Substrate**: `#d5c4a9` — grounded in `var(--ui-muted)` in `:root`
- **Interactive Accent / Highlight**: `#ef893b` — grounded in `var(--ui-heading)` in `:root`
- **Secondary / Muted Copy**: `#f3e3c7` — grounded in `var(--ui-home-heading)` in `:root`
- **Structural Hairline Border**: `#efd6a4` — grounded in `var(--ui-focus)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `600px` extracted from `ofrenda-davidlangarica-dev` stylesheet
- **Padding & Gutters**: `6px` lateral canvas padding with `8px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 600px`, `gap: 8px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `6px` horizontal padding
- **Media Queries**: `@media (max-width:600px)`, `@media (max-height:500px)and (min-aspect-ratio:1.15/1)`, `@media (max-height:700px)`, `@media (prefers-reduced-motion:reduce)`
- **Corner Radii**: `50%`, `4px`, `5px`, `2px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Marqen`
- **Body Font Stack**: `Macario`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: rule `h1` (`font-size: clamp(44px,12vw,72px)`, `line-height: 1.08`, `font-weight: 400`)
- **H2 Section Rule**: rule `h2` (`font-size: 30px`, `line-height: 1.1`)
- **Body Copy Rule**: CSS variables `--ui-font-body: Georgia, "Times New Roman", serif`, `--ui-body-size: clamp(16px, 1.5vw, 19px)`, `--ui-body-line-height: 1.55`; rule `p` (`font-size: 16px`, `line-height: 1.4`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `clamp(44px,12vw,72px)`, `16px`, `30px`, `13px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `ofrenda-davidlangarica-dev` (`OFRENDA — Create a personal Día de Muertos altar`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.experience-chrome> — `ofrenda-davidlangarica-dev`)**:
   - DOM & Selectors: Landmark `<header class="experience-chrome">` hosting `OFRENDA — Create a personal Día de M` navigation (`David Langarica`), DOM attributes (`data-cf-beacon="("token":"e723bd39f9d..."`, `data-engine="three.js r180 webgpu"`, `data-on="true"`, `data-loading-progress="0.9"`), and stylesheet rule `html.lenis body { height:auto }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.experience-chrome> — `ofrenda-davidlangarica-dev`)` (`ofrenda-davidlangarica-dev`) adapts across `@media (max-width:600px)`, `@media (max-height:500px)and (min-aspect-ratio:1.15/1)`, `@media (max-height:700px)`, `@media (prefers-reduced-motion:reduce)` with `cubic-bezier(.22,.68,.2,1)` transitions and links `David Langarica`.
2. **Hero Stage & Focal Lead (<section.floating-menu> — `OFRENDA`)**:
   - DOM & Selectors: Landmark `<section class="floating-menu">` presenting display lead `OFRENDA` and copy excerpt *"For you, who still have a place here."* over `#000` canvas and `#f4e6cf` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#000` background with `#f4e6cf` headline `OFRENDA`.
3. **Primary Showcase & Content Grid (<section.floating-menu> — `OFRENDA — A place to remember`)**:
   - DOM & Selectors: Landmark `<section class="floating-menu">` rendering section `OFRENDA — A place to remember` with copy *"Language Choose English or Spanish."*, asset references (`favicon.ico`, `Marqen.woff2`, `index-CUtJAqPO.js`, `index-BRkV915_.css`), and grid rule `.lenis-stopped { overflow:clip }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.floating-menu> — `OFRENDA — A place to remember`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 600px`, `gap: 8px`) on desktop and Single-column vertical stack at `390px` viewport width with `6px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.floating-menu> — `Language Choose English or Spanish`)**:
   - DOM & Selectors: Landmark `<section class="floating-menu">` framing `Language Choose English or Spanish.` and `Sound Music and ambience.` (*"Sound Music and ambience."*) with `#d5c4a9` surface cards, `#ef893b` accents, and `.lenis.lenis-smooth iframe { pointer-events:none }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.floating-menu> — `Language Choose English or Spanish`)` uses `50%`, `4px`, `5px`, `2px` radii, `#ef893b` highlights, and assets (favicon.ico, Marqen.woff2, index-CUtJAqPO.js).
5. **Colophon & Global Directory Footer (<footer.menu-footer> — `https://ofrenda.davidlangarica.dev`)**:
   - DOM & Selectors: Landmark `<footer class="menu-footer">` anchoring `OFRENDA — Create a personal Día ` footer links (`David Langarica`), copy *"Graphics Available after the water and salt."*, and `#efd6a4` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.menu-footer> — `https://ofrenda.davidlangarica.dev`)` aligns to `600px` extracted from `ofrenda-davidlangarica-dev` stylesheet with `6px` lateral canvas padding with `8px` grid gap and attributes (data-cf-beacon="("token":"e723bd39f9d...", data-engine="three.js r180 webgpu", data-on="true").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"For you, who still have a place here."*
- Copy Excerpt 2: *"Language Choose English or Spanish."*
- Copy Excerpt 3: *"Sound Music and ambience."*
- Copy Excerpt 4: *"Graphics Available after the water and salt."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.22,.68,.2,1)`
- **Extracted Stylesheet Rules (`ofrenda-davidlangarica-dev`)**:
- `html.lenis body { height:auto }`
- `.lenis-stopped { overflow:clip }`
- `.lenis.lenis-smooth iframe { pointer-events:none }`
- `.lenis.lenis-autoToggle { transition-property:overflow;transition-duration:1ms;transition-behavior... }`
- `.candle-tutorial { position:fixed;inset:0;z-index:80;pointer-events:none;opacity:0;overflow... }`
- **Per-Selector Transition Rules**:
- **Selector `.lenis.lenis-autoToggle`**: `transition: 1ms` extracted from `ofrenda-davidlangarica-dev` stylesheet.
- **Selector `.canvas-layer`**: `transition: bottom .32s ease` extracted from `ofrenda-davidlangarica-dev` stylesheet.
- **Selector `media(prefers-reduced-motion:reduce)`**: `transition: .08s` extracted from `ofrenda-davidlangarica-dev` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,.68,.2,1)`)**: Governs interactive state transitions across `<header.experience-chrome>` and `<section.floating-menu>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `ofrenda-davidlangarica-dev`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
