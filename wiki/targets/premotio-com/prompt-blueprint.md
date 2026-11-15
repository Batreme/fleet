---
title: "UI Prompt Blueprint: premotio-com"
date: 2026-11-15
target: "[[overview|premotio-com]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#f5f5f7` / `#000000`)"
---

# UI Design System & Master Generation Blueprint: premotio-com

> **premotio — finished design into polished motion** (https://premotio.com/) — premotio turns finished design into polished motion without sending you into a video editor. Pick a preset, drop in your work and export...

![Desktop Viewport Capture (1440x50734)](file:///root/projects/fleet/wiki/targets/premotio-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **premotio — finished design into polished motion** (`https://premotio.com/`). premotio turns finished design into polished motion without sending you into a video editor. Pick a preset, drop in your work and export...
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#f5f5f7` / `#000000`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#f5f5f7` (`var(--bg)` in `:root`) paired with `#000000` primary typography and `#000000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Inter Tight Fallback\: BlinkMacSystemFont` for display copy (`D e s i g n e d a l r e a d y N o w `) with `Inter Tight Fallback\: Segoe UI` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `17.375rem` container bounds (`gap: var(--space-40)`, padding `var(--space-12)`) with `cubic-bezier(.16,1,.3,1)` easing and Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/premotio-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×50734px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `17.375rem` extracted from `premotio-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--space-12)` lateral canvas padding with `var(--space-40)` grid gap.
- **Border Radius Scale**: `var(--corner)`, `var(--radius-pill)`, `var(--radius-card)`, `var(--rounded)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 17.375rem`, `gap: var(--space-40)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--space-12)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (width<=1024px)`, `@media (width<=640px) and (aspect-ratio<=1)`, `@media (width<=640px)`, `@media (prefers-reduced-motion:reduce)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f5f5f7` | `var(--bg)` in `:root` |
| **Primary Typography Ink** | `#1d1d1f` | `var(--fg)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ffffff` | `var(--on-fg)` in `:root` |
| **Interactive Accent / Highlight** | `#000000` | `var(--logo)` in `:root` |
| **Secondary / Muted Copy** | `#6e6e73` | `var(--fg-muted)` in `:root` |
| **Structural Hairline Border** | `#e5e5ea` | `var(--border)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--step` | `13.875rem` | Dimension / Scale Token |
| `--scale` | `.66` | Design System Custom Token |
| `--corner` | `1.25rem` | Dimension / Scale Token |
| `--drum` | `0` | Design System Custom Token |
| `--top` | `1.125rem` | Dimension / Scale Token |
| `--room` | `max(7.5rem, 100svh - 25.3125rem)` | Dimension / Scale Token |
| `--panel` | `47.1875rem` | Dimension / Scale Token |
| `--rounded` | `calc(var(--panel)*20/755)` | Elevation / Border Token |
| `--bottom` | `2rem` | Dimension / Scale Token |
| `--swatch` | `min(2.25rem, (100cqi - 3 * var(--swatch-gap) - var(--space-8)) / 4)` | Brand / Palette Token |
| `--swatch-gap` | `.625rem` | Brand / Palette Token |
| `--full` | `0` | Design System Custom Token |
| `--open` | `0` | Design System Custom Token |
| `--late` | `0` | Design System Custom Token |
| `--height` | `clamp(39.25rem, 100svh, 48rem)` | Layout / Spatial Grid Token |
| `--chat-top` | `calc(var(--height) - 9.875rem)` | Dimension / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Inter Tight Fallback\: BlinkMacSystemFont`.
- **Primary Body Stack**: `Inter Tight Fallback\: Segoe UI`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--font-size-h1: 6.25rem`, `--font-size-tablet-h1: 5rem`, `--font-size-mobile-h1: 3.5rem`.
- **Section Heading (`H2`)**: CSS variables `--font-size-h2: 3.25rem`, `--font-size-tablet-h2: 2.75rem`, `--font-size-mobile-h2: 2rem`.
- **Body Copy**: CSS variables `--body-top: 59`, `--font-size-paragraph: 1rem`, `--font-size-body: 1.0625rem`.
- **Metadata & Navigation Labels**: CSS variables `--shadow-caption: 0 .5rem 1.5rem #1d1d1f1f`, `--font-size-label: .9375rem`, `--font-size-meta: .75rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.16,1,.3,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.handoff-layer__fill[data-v-90766...`**: `transition: transform .12s linear` extracted from `premotio-com` stylesheet.
- **Selector `.fade-leave-active`**: `transition: opacity .3s` extracted from `premotio-com` stylesheet.
- **Selector `.app-loader.is-fading>*`**: `transition: opacity .3s linear` extracted from `premotio-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<header.app-nav>` and `<section.library>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — premotio — finished design into polished m │
│ ====================================================================== │
│ [ <header.app-nav>         | Library · How it works · MCP · Pricing ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero>                                       |   │
│ | H1: D e s i g n e d a l r e a d y N o w m a k e i t (...         |   │
│ | Substrate: #f5f5f7    | Ink: #000000    | Accent: #000000        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.library>         ) max-w: 17.375rem      |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | S t a r t w i t h t h e g o  |  | Preset categories            | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<header.app-nav>] -> [<section.hero>] -> [<section.library>] |      │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.app-footer>   ) | https://premotio.com/              │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.app-nav> — `premotio-com`)**:
   - Landmark `<header class="app-nav app-nav--active">` hosting `premotio — finished design into poli` navigation (`Library · How it works · MCP · Pricing · Contact`), DOM attributes (`data-v-a799f99b`, `data-v-a3457c20`, `data-v-39640a56`, `data-v-f9a31650`), and stylesheet rule `before { content:attr(data-word) }`.
2. **Hero Stage & Focal Lead (<section.hero> — `D e s i g n e d a l r e a d y N o `)**:
   - Landmark `<section class="hero is-on">` presenting display lead `D e s i g n e d a l r e a d y N o w m a k e i t (...` and copy excerpt *"D e s i g n e d a l r e a d y"* over `#f5f5f7` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.library> — `S t a r t w i t h t h e g o o d p `)**:
   - Landmark `<section class="library">` rendering section `S t a r t w i t h t h e g o o d p a r t` with copy *"N o w m a k e i t ( move )"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `_payload.json`), and grid rule `.reveal-line-mask { clip-path:inset(0 -100vw -.2em -.15em) }`.
4. **Interactive Detail & Feature Matrix (<section.categories> — `Preset categories`)**:
   - Landmark `<section class="categories">` framing `Preset categories` and `T a k e t h e s h o r t c u t . K i l l t h e ( t...` (*"Designed already Now make it move"*) with `#ffffff` surface cards, `#000000` accents, and `focus-visible { outline:2px solid var(--fg);outline-offset:.125rem }`.
5. **Colophon & Global Directory Footer (<footer.app-footer> — `https://premotio.com/`)**:
   - Landmark `<footer class="app-footer">` anchoring `premotio — finished design into ` footer links (`Library · How it works · MCP · Pricing · Contact`), copy *"Premotio turns finished design into polished motion — withou"*, and `#e5e5ea` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: premotio-com (premotio — finished design into polished motion)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `premotio-com` (**premotio — finished design into polished motion** — `https://premotio.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f5f5f7` / `#000000`).
- **Identity & Domain Context**: premotio turns finished design into polished motion without sending you into a video editor. Pick a preset, drop in your work and export...
- **Primary Substrate**: `#f5f5f7` (`var(--bg)` in `:root`), **Primary Ink**: `#000000`, **Accent / Highlight**: `#000000`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#f5f5f7` (`var(--bg)` in `:root`) paired with `#000000` primary typography and `#000000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Inter Tight Fallback\: BlinkMacSystemFont` for display copy (`D e s i g n e d a l r e a d y N o w `) with `Inter Tight Fallback\: Segoe UI` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `17.375rem` container bounds (`gap: var(--space-40)`, padding `var(--space-12)`) with `cubic-bezier(.16,1,.3,1)` easing and Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `premotio-com` in your global stylesheet:

:root {
  /* premotio — finished design into polished motion (premotio-com) — Ground-Truth Extracted CSS Variables */
  --step: 13.875rem; /* Dimension / Scale Token (premotio-com) */
  --scale: .66; /* Design System Custom Token (premotio-com) */
  --corner: 1.25rem; /* Dimension / Scale Token (premotio-com) */
  --drum: 0; /* Design System Custom Token (premotio-com) */
  --top: 1.125rem; /* Dimension / Scale Token (premotio-com) */
  --room: max(7.5rem, 100svh - 25.3125rem); /* Dimension / Scale Token (premotio-com) */
  --panel: 47.1875rem; /* Dimension / Scale Token (premotio-com) */
  --rounded: calc(var(--panel)*20/755); /* Elevation / Border Token (premotio-com) */
  --bottom: 2rem; /* Dimension / Scale Token (premotio-com) */
  --swatch: min(2.25rem, (100cqi - 3 * var(--swatch-gap) - var(--space-8)) / 4); /* Brand / Palette Token (premotio-com) */
  --swatch-gap: .625rem; /* Brand / Palette Token (premotio-com) */
  --full: 0; /* Design System Custom Token (premotio-com) */
  --open: 0; /* Design System Custom Token (premotio-com) */
  --late: 0; /* Design System Custom Token (premotio-com) */
  --height: clamp(39.25rem, 100svh, 48rem); /* Layout / Spatial Grid Token (premotio-com) */
  --chat-top: calc(var(--height) - 9.875rem); /* Dimension / Scale Token (premotio-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f5f5f7` — grounded in `var(--bg)` in `:root`
- **Primary Typography Ink**: `#1d1d1f` — grounded in `var(--fg)` in `:root`
- **Elevated Surface / Card Substrate**: `#ffffff` — grounded in `var(--on-fg)` in `:root`
- **Interactive Accent / Highlight**: `#000000` — grounded in `var(--logo)` in `:root`
- **Secondary / Muted Copy**: `#6e6e73` — grounded in `var(--fg-muted)` in `:root`
- **Structural Hairline Border**: `#e5e5ea` — grounded in `var(--border)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×50734px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `17.375rem` extracted from `premotio-com` stylesheet
- **Padding & Gutters**: `var(--space-12)` lateral canvas padding with `var(--space-40)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 17.375rem`, `gap: var(--space-40)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--space-12)` horizontal padding
- **Media Queries**: `@media (width<=1024px)`, `@media (width<=640px) and (aspect-ratio<=1)`, `@media (width<=640px)`, `@media (prefers-reduced-motion:reduce)`
- **Corner Radii**: `var(--corner)`, `var(--radius-pill)`, `var(--radius-card)`, `var(--rounded)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Inter Tight Fallback\: BlinkMacSystemFont`
- **Body Font Stack**: `Inter Tight Fallback\: Segoe UI`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--font-size-h1: 6.25rem`, `--font-size-tablet-h1: 5rem`, `--font-size-mobile-h1: 3.5rem`
- **H2 Section Rule**: CSS variables `--font-size-h2: 3.25rem`, `--font-size-tablet-h2: 2.75rem`, `--font-size-mobile-h2: 2rem`
- **Body Copy Rule**: CSS variables `--body-top: 59`, `--font-size-paragraph: 1rem`, `--font-size-body: 1.0625rem`
- **Metadata & Index Rule**: CSS variables `--shadow-caption: 0 .5rem 1.5rem #f5f5f7`, `--font-size-label: .9375rem`, `--font-size-meta: .75rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `premotio-com` (`premotio — finished design into polished motion`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.app-nav> — `premotio-com`)**:
   - DOM & Selectors: Landmark `<header class="app-nav app-nav--active">` hosting `premotio — finished design into poli` navigation (`Library · How it works · MCP · Pricing · Contact`), DOM attributes (`data-v-a799f99b`, `data-v-a3457c20`, `data-v-39640a56`, `data-v-f9a31650`), and stylesheet rule `before { content:attr(data-word) }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.app-nav> — `premotio-com`)` (`premotio-com`) adapts across `@media (width<=1024px)`, `@media (width<=640px) and (aspect-ratio<=1)`, `@media (width<=640px)`, `@media (prefers-reduced-motion:reduce)` with `cubic-bezier(.16,1,.3,1)` transitions and links `Library · How it works · MCP · Pricing · Contact`.
2. **Hero Stage & Focal Lead (<section.hero> — `D e s i g n e d a l r e a d y N o `)**:
   - DOM & Selectors: Landmark `<section class="hero is-on">` presenting display lead `D e s i g n e d a l r e a d y N o w m a k e i t (...` and copy excerpt *"D e s i g n e d a l r e a d y"* over `#f5f5f7` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1440×50734px` desktop / `390×2400px` mobile) sets `#f5f5f7` background with `#000000` headline `D e s i g n e d a l r e a d y N o w m a k e i t (...`.
3. **Primary Showcase & Content Grid (<section.library> — `S t a r t w i t h t h e g o o d p `)**:
   - DOM & Selectors: Landmark `<section class="library">` rendering section `S t a r t w i t h t h e g o o d p a r t` with copy *"N o w m a k e i t ( move )"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `_payload.json`), and grid rule `.reveal-line-mask { clip-path:inset(0 -100vw -.2em -.15em) }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.library> — `S t a r t w i t h t h e g o o d p `)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 17.375rem`, `gap: var(--space-40)`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--space-12)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.categories> — `Preset categories`)**:
   - DOM & Selectors: Landmark `<section class="categories">` framing `Preset categories` and `T a k e t h e s h o r t c u t . K i l l t h e ( t...` (*"Designed already Now make it move"*) with `#ffffff` surface cards, `#000000` accents, and `focus-visible { outline:2px solid var(--fg);outline-offset:.125rem }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.categories> — `Preset categories`)` uses `var(--corner)`, `var(--radius-pill)`, `var(--radius-card)`, `var(--rounded)` radii, `#000000` highlights, and assets (favicon.ico, favicon.svg, apple-touch-icon.png).
5. **Colophon & Global Directory Footer (<footer.app-footer> — `https://premotio.com/`)**:
   - DOM & Selectors: Landmark `<footer class="app-footer">` anchoring `premotio — finished design into ` footer links (`Library · How it works · MCP · Pricing · Contact`), copy *"Premotio turns finished design into polished motion — withou"*, and `#e5e5ea` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.app-footer> — `https://premotio.com/`)` aligns to `17.375rem` extracted from `premotio-com` stylesheet with `var(--space-12)` lateral canvas padding with `var(--space-40)` grid gap and attributes (data-v-a799f99b, data-v-a3457c20, data-v-39640a56).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"D e s i g n e d a l r e a d y"*
- Copy Excerpt 2: *"N o w m a k e i t ( move )"*
- Copy Excerpt 3: *"Designed already Now make it move"*
- Copy Excerpt 4: *"Premotio turns finished design into polished motion — without sending you into a v..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.16,1,.3,1)`
- **Extracted Stylesheet Rules (`premotio-com`)**:
- `before { content:attr(data-word) }`
- `.reveal-line-mask { clip-path:inset(0 -100vw -.2em -.15em) }`
- `focus-visible { outline:2px solid var(--fg);outline-offset:.125rem }`
- `root { --layout-margin:max(var(--space-32), var(--safe-x));--grid-columns:8;--g... }`
- `video { vertical-align:baseline;border:0;margin:0;padding:0 }`
- **Per-Selector Transition Rules**:
- **Selector `.handoff-layer__fill[data-v-90766...`**: `transition: transform .12s linear` extracted from `premotio-com` stylesheet.
- **Selector `.fade-leave-active`**: `transition: opacity .3s` extracted from `premotio-com` stylesheet.
- **Selector `.app-loader.is-fading>*`**: `transition: opacity .3s linear` extracted from `premotio-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<header.app-nav>` and `<section.library>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `premotio-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
