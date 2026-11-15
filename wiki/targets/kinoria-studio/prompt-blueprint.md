---
title: "UI Prompt Blueprint: kinoria-studio"
date: 2026-11-15
target: "[[overview|kinoria-studio]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#F2EDE4`)"
---

# UI Design System & Master Generation Blueprint: kinoria-studio

> **KINORIA** (https://kinoria.studio/) — KINORIA 135 is a concept for a fully mechanical 35mm film camera, made as an interactive website. Pick a film, look through the viewfinde...

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/kinoria-studio/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **KINORIA** (`https://kinoria.studio/`). KINORIA 135 is a concept for a fully mechanical 35mm film camera, made as an interactive website. Pick a film, look through the viewfinde...
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#F2EDE4`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`body { background: #000 }`) paired with `#F2EDE4` primary typography and `#F2EDE4` accents.
  - **Extracted Typographic Hierarchy**: Pairs `system-ui, -apple-system, sans-serif` (no custom `@font-face` extracted) for display copy (`KINORIA`) with `system-ui, -apple-system, sans-serif` (no custom `@font-face` extracted) and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `70vw` container bounds (`gap: 0px (flush layout)`, padding `24px`) with `cubic-bezier(0.25,0.1,0.25,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/kinoria-studio/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `70vw` extracted from `kinoria-studio` stylesheet.
- **Canvas Lateral Padding & Spacing**: `24px` lateral canvas padding with `0px (flush layout)` grid gap.
- **Border Radius Scale**: `999px`, `50%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 70vw`, `gap: 0px (flush layout)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `24px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-aspect-ratio: 1672/941)`, `@media (max-aspect-ratio: 2843/4400)`, `@media (prefers-reduced-motion: reduce)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `body { background: #000 }` |
| **Primary Typography Ink** | `#7ee6ff` | `#hud { color: #7ee6ff }` |
| **Elevated Surface / Card Substrate** | `#ff6b6b` | `#err { color: #ff6b6b }` |
| **Interactive Accent / Highlight** | `#F2EDE4` | `#deadnote { color: #F2EDE4 }` |
| **Secondary / Muted Copy** | `#a39a8f` | `#deadnote .db { color: #a39a8f }` |
| **Structural Hairline Border** | `#e8e2d6` | `#deadnote .dr:focus-visible { background: #e8e2d6 }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--kpx` | `clamp(1px, min(100vw / 1920, 100vh / 911), 3px)` | Dimension / Scale Token |
| `--kinoria-studio-bg` | `#000` | Canvas Substrate (from `body { background: #000 }`) |
| `--kinoria-studio-ink` | `#F2EDE4` | Primary Typography Ink (stylesheet-derived) |
| `--kinoria-studio-surface` | `#ff6b6b` | Surface Substrate (stylesheet-derived) |
| `--kinoria-studio-accent` | `#F2EDE4` | Interactive Accent (stylesheet-derived) |
| `--kinoria-studio-muted` | `#a39a8f` | Secondary Ink (stylesheet-derived) |
| `--kinoria-studio-border` | `#e8e2d6` | Structural Border (stylesheet-derived) |
| `--kinoria-studio-container` | `70vw` | Container Bound (stylesheet-derived) |
| `--kinoria-studio-gap` | `0px` | Grid Gutter (stylesheet-derived) |
| `--kinoria-studio-pad` | `24px` | Lateral Padding (stylesheet-derived) |
| `--kinoria-studio-ease` | `cubic-bezier(0.25,0.1,0.25,1)` | Primary Easing Function |
| `--kinoria-studio-radius` | `999px` | Corner Radius (stylesheet-derived) |
| `--kinoria-studio-fs-base` | `12px` | Observed Font Size Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `system-ui, -apple-system, sans-serif` (no custom `@font-face` extracted).
- **Primary Body Stack**: `system-ui, -apple-system, sans-serif` (no custom `@font-face` extracted).
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `14px`, `13px`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `14px`, `13px`).
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `14px`, `13px`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `14px`, `13px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `#boot`**: `transition: opacity .5s ease` extracted from `kinoria-studio` stylesheet.
- **Selector `html.introdead #boot`**: `transition: opacity .45s ease` extracted from `kinoria-studio` stylesheet.
- **Selector `#fotd`**: `transition: opacity .35s ease, visibility 0s linear .35s` extracted from `kinoria-studio` stylesheet.
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in static CSS).
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — KINORIA                                    │
│ ====================================================================== │
│ [ <header.kc-on>           | Overview · Index · Archive · About · C ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <div.dzresp>                                         |   │
│ | H1: KINORIA                                                      |   │
│ | Substrate: #000       | Ink: #F2EDE4    | Accent: #F2EDE4        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<div.bootd>               ) max-w: 70vw           |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Featured Work & Interactive  |  | Technical Architecture & Nar | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 0px (f) | │
│ | [<header.kc-on>] -> [<div.dzresp>] -> [<div.bootd>] |                │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.intro-drawn>  ) | https://kinoria.studio/            │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.kc-on> — `kinoria-studio`)**:
   - Landmark `<header class="kc-on">` hosting `KINORIA` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-doc="intro"`, `data-engine="three.js r185"`), and stylesheet rule `dot { display:none!important }`.
2. **Hero Stage & Focal Lead (<div.dzresp> — `KINORIA`)**:
   - Landmark `<div class="dzresp">` presenting display lead `KINORIA` and copy excerpt *"THE ROLL DID NOT LOAD"* over `#000` canvas and `#F2EDE4` ink.
3. **Primary Showcase & Content Grid (<div.bootd> — `Featured Work & Interactive Showca`)**:
   - Landmark `<div class="bootd">` rendering section `Featured Work & Interactive Showcase` with copy *"This page could not be drawn. The connection may have dropped, or"*, asset references (`Archivo-Variable.woff2`, `wordmark.svg`, `details_entry_1920x911-DmzTlZIo.webp`, `favicon.svg`), and grid rule `body { height: 100%; background: 000; overflow: hidden; }`.
4. **Interactive Detail & Feature Matrix (<div.bootvf> — `Technical Architecture & Narrative`)**:
   - Landmark `<div class="bootvf">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Reload to try again."*) with `#ff6b6b` surface cards, `#F2EDE4` accents, and `stage { position: fixed; inset: 0; touch-action: none; }`.
5. **Colophon & Global Directory Footer (<footer.intro-drawn> — `https://kinoria.studio/`)**:
   - Landmark `<footer class="intro-drawn">` anchoring `KINORIA` footer links (`Overview · Index · Archive · About · Contact`), copy *"Technical Architecture & Narrative"*, and `#e8e2d6` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: kinoria-studio (KINORIA)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `kinoria-studio` (**KINORIA** — `https://kinoria.studio/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#F2EDE4`).
- **Identity & Domain Context**: KINORIA 135 is a concept for a fully mechanical 35mm film camera, made as an interactive website. Pick a film, look through the viewfinde...
- **Primary Substrate**: `#000` (`body { background: #000 }`), **Primary Ink**: `#F2EDE4`, **Accent / Highlight**: `#F2EDE4`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`body { background: #000 }`) paired with `#F2EDE4` primary typography and `#F2EDE4` accents.
  - **Extracted Typographic Hierarchy**: Pairs `system-ui, -apple-system, sans-serif` (no custom `@font-face` extracted) for display copy (`KINORIA`) with `system-ui, -apple-system, sans-serif` (no custom `@font-face` extracted) and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `70vw` container bounds (`gap: 0px (flush layout)`, padding `24px`) with `cubic-bezier(0.25,0.1,0.25,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `kinoria-studio` in your global stylesheet:

:root {
  /* KINORIA (kinoria-studio) — Ground-Truth Extracted CSS Variables */
  --kpx: clamp(1px, min(100vw / 1920, 100vh / 911), 3px); /* Dimension / Scale Token (kinoria-studio) */
  --kinoria-studio-bg: #000; /* Canvas Substrate (from `body { background: #000 }`) (kinoria-studio) */
  --kinoria-studio-ink: #F2EDE4; /* Primary Typography Ink (stylesheet-derived) (kinoria-studio) */
  --kinoria-studio-surface: #ff6b6b; /* Surface Substrate (stylesheet-derived) (kinoria-studio) */
  --kinoria-studio-accent: #F2EDE4; /* Interactive Accent (stylesheet-derived) (kinoria-studio) */
  --kinoria-studio-muted: #a39a8f; /* Secondary Ink (stylesheet-derived) (kinoria-studio) */
  --kinoria-studio-border: #e8e2d6; /* Structural Border (stylesheet-derived) (kinoria-studio) */
  --kinoria-studio-container: 70vw; /* Container Bound (stylesheet-derived) (kinoria-studio) */
  --kinoria-studio-gap: 0px; /* Grid Gutter (stylesheet-derived) (kinoria-studio) */
  --kinoria-studio-pad: 24px; /* Lateral Padding (stylesheet-derived) (kinoria-studio) */
  --kinoria-studio-ease: cubic-bezier(0.25,0.1,0.25,1); /* Primary Easing Function (kinoria-studio) */
  --kinoria-studio-radius: 999px; /* Corner Radius (stylesheet-derived) (kinoria-studio) */
  --kinoria-studio-fs-base: 12px; /* Observed Font Size Token (kinoria-studio) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000` — grounded in `body { background: #000 }`
- **Primary Typography Ink**: `#7ee6ff` — grounded in `#hud { color: #7ee6ff }`
- **Elevated Surface / Card Substrate**: `#ff6b6b` — grounded in `#err { color: #ff6b6b }`
- **Interactive Accent / Highlight**: `#F2EDE4` — grounded in `#deadnote { color: #F2EDE4 }`
- **Secondary / Muted Copy**: `#a39a8f` — grounded in `#deadnote .db { color: #a39a8f }`
- **Structural Hairline Border**: `#e8e2d6` — grounded in `#deadnote .dr:focus-visible { background: #e8e2d6 }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `70vw` extracted from `kinoria-studio` stylesheet
- **Padding & Gutters**: `24px` lateral canvas padding with `0px (flush layout)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 70vw`, `gap: 0px (flush layout)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `24px` horizontal padding
- **Media Queries**: `@media (max-aspect-ratio: 1672/941)`, `@media (max-aspect-ratio: 2843/4400)`, `@media (prefers-reduced-motion: reduce)`
- **Corner Radii**: `999px`, `50%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `system-ui, -apple-system, sans-serif` (no custom `@font-face` extracted)
- **Body Font Stack**: `system-ui, -apple-system, sans-serif` (no custom `@font-face` extracted)
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `14px`, `13px`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `14px`, `13px`)
- **Body Copy Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `14px`, `13px`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `14px`, `13px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `kinoria-studio` (`KINORIA`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.kc-on> — `kinoria-studio`)**:
   - DOM & Selectors: Landmark `<header class="kc-on">` hosting `KINORIA` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-doc="intro"`, `data-engine="three.js r185"`), and stylesheet rule `dot { display:none!important }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.kc-on> — `kinoria-studio`)` (`kinoria-studio`) adapts across `@media (max-aspect-ratio: 1672/941)`, `@media (max-aspect-ratio: 2843/4400)`, `@media (prefers-reduced-motion: reduce)` with `cubic-bezier(0.25,0.1,0.25,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<div.dzresp> — `KINORIA`)**:
   - DOM & Selectors: Landmark `<div class="dzresp">` presenting display lead `KINORIA` and copy excerpt *"THE ROLL DID NOT LOAD"* over `#000` canvas and `#F2EDE4` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#000` background with `#F2EDE4` headline `KINORIA`.
3. **Primary Showcase & Content Grid (<div.bootd> — `Featured Work & Interactive Showca`)**:
   - DOM & Selectors: Landmark `<div class="bootd">` rendering section `Featured Work & Interactive Showcase` with copy *"This page could not be drawn. The connection may have dropped, or"*, asset references (`Archivo-Variable.woff2`, `wordmark.svg`, `details_entry_1920x911-DmzTlZIo.webp`, `favicon.svg`), and grid rule `body { height: 100%; background: 000; overflow: hidden; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<div.bootd> — `Featured Work & Interactive Showca`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 70vw`, `gap: 0px (flush layout)`) on desktop and Single-column vertical stack at `390px` viewport width with `24px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<div.bootvf> — `Technical Architecture & Narrative`)**:
   - DOM & Selectors: Landmark `<div class="bootvf">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Reload to try again."*) with `#ff6b6b` surface cards, `#F2EDE4` accents, and `stage { position: fixed; inset: 0; touch-action: none; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<div.bootvf> — `Technical Architecture & Narrative`)` uses `999px`, `50%` radii, `#F2EDE4` highlights, and assets (Archivo-Variable.woff2, wordmark.svg, details_entry_1920x911-DmzTlZIo.webp).
5. **Colophon & Global Directory Footer (<footer.intro-drawn> — `https://kinoria.studio/`)**:
   - DOM & Selectors: Landmark `<footer class="intro-drawn">` anchoring `KINORIA` footer links (`Overview · Index · Archive · About · Contact`), copy *"Technical Architecture & Narrative"*, and `#e8e2d6` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.intro-drawn> — `https://kinoria.studio/`)` aligns to `70vw` extracted from `kinoria-studio` stylesheet with `24px` lateral canvas padding with `0px (flush layout)` grid gap and attributes (data-doc="intro", data-engine="three.js r185").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"THE ROLL DID NOT LOAD"*
- Copy Excerpt 2: *"This page could not be drawn. The connection may have dropped, or this browser cou..."*
- Copy Excerpt 3: *"Reload to try again."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`
- **Extracted Stylesheet Rules (`kinoria-studio`)**:
- `dot { display:none!important }`
- `body { height: 100%; background: 000; overflow: hidden; }`
- `stage { position: fixed; inset: 0; touch-action: none; }`
- `herostage { position: absolute; inset: 0; }`
- `flowstage { z-index: 1; }`
- **Per-Selector Transition Rules**:
- **Selector `#boot`**: `transition: opacity .5s ease` extracted from `kinoria-studio` stylesheet.
- **Selector `html.introdead #boot`**: `transition: opacity .45s ease` extracted from `kinoria-studio` stylesheet.
- **Selector `#fotd`**: `transition: opacity .35s ease, visibility 0s linear .35s` extracted from `kinoria-studio` stylesheet.
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in static CSS).
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `kinoria-studio`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
