---
title: "UI Prompt Blueprint: tamasolajos-com"
date: 2026-11-15
target: "[[overview|tamasolajos-com]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#0000`)"
---

# UI Design System & Master Generation Blueprint: tamasolajos-com

> **Tamás Olajos — AI Filmmaker & Director · London & Budapest** (https://tamasolajos.com/) — Tamás Olajos is an award-winning AI filmmaker and director, Runway and Dreamina Creative Partner. Cinematic commercial campaigns and expe...

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/tamasolajos-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Tamás Olajos — AI Filmmaker & Director · London & Budapest** (`https://tamasolajos.com/`). Tamás Olajos is an award-winning AI filmmaker and director, Runway and Dreamina Creative Partner. Cinematic commercial campaigns and expe...
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#0000`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`html { background-color: #000 }`) paired with `#0000` primary typography and `#0000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `system-ui, -apple-system, sans-serif` (no custom `@font-face` extracted) for display copy (`Tamás Olajos — AI Filmmaker & Direct`) with `system-ui, -apple-system, sans-serif` (no custom `@font-face` extracted) and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `none (full-bleed `100%` viewport stage)` container bounds (`gap: 0px (flush layout)`, padding `1rem`) with `cubic-bezier(0.25,0.1,0.25,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/tamasolajos-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `none (full-bleed `100%` viewport stage)` extracted from `tamasolajos-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `1rem` lateral canvas padding with `0px (flush layout)` grid gap.
- **Border Radius Scale**: `4rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: none (full-bleed `100%` viewport stage)`, `gap: 0px (flush layout)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `1rem` horizontal padding.
- **Extracted CSS Media Queries**: no `@media` queries in static stylesheet (fluid viewport scaling).

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `html { background-color: #000 }` |
| **Primary Typography Ink** | `#0000` | `.ui .button { border: #0000 }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--inner-height` | `900px` | Layout / Spatial Grid Token |
| `--tamasolajos-com-bg` | `#000` | Canvas Substrate (from `html { background-color: #000 }`) |
| `--tamasolajos-com-ink` | `#0000` | Primary Typography Ink (stylesheet-derived) |
| `--tamasolajos-com-surface` | `#000` | Surface Substrate (stylesheet-derived) |
| `--tamasolajos-com-accent` | `#0000` | Interactive Accent (stylesheet-derived) |
| `--tamasolajos-com-muted` | `#0000` | Secondary Ink (stylesheet-derived) |
| `--tamasolajos-com-border` | `#0000` | Structural Border (stylesheet-derived) |
| `--tamasolajos-com-container` | `none` | Container Bound (stylesheet-derived) |
| `--tamasolajos-com-gap` | `0px` | Grid Gutter (stylesheet-derived) |
| `--tamasolajos-com-pad` | `1rem` | Lateral Padding (stylesheet-derived) |
| `--tamasolajos-com-ease` | `cubic-bezier(0.25,0.1,0.25,1)` | Primary Easing Function |
| `--tamasolajos-com-radius` | `4rem` | Corner Radius (stylesheet-derived) |
| `--tamasolajos-com-fs-base` | `10px` | Observed Font Size Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `system-ui, -apple-system, sans-serif` (no custom `@font-face` extracted).
- **Primary Body Stack**: `system-ui, -apple-system, sans-serif` (no custom `@font-face` extracted).
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `10px`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `10px`).
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `10px`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `10px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`.

### Per-Element Transition & Choreography Rules
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in static CSS).
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Tamás Olajos — AI Filmmaker & Director · L │
│ ====================================================================== │
│ [ <header.webgl>           | Overview · Index · Archive · About · C ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <div.webgl>                                          |   │
│ | H1: Tamás Olajos — AI Filmmaker & Director · London              |   │
│ | Substrate: #000       | Ink: #0000      | Accent: #0000          |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<div.webgl>               ) max-w: none (full-ble |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Featured Work & Interactive  |  | Technical Architecture & Nar | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 0px (f) | │
│ | [<header.webgl>] -> [<div.webgl>] -> [<div.webgl>] |                 │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer>              ) | https://tamasolajos.com/           │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.webgl> — `tamasolajos-com`)**:
   - Landmark `<header class="webgl">` hosting `Tamás Olajos — AI Filmmaker & Direct` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-engine="three.js r181"`), and stylesheet rule `body { overscroll-behavior:none;touch-action:none;margin:0;padding:0;overflow:h... }`.
2. **Hero Stage & Focal Lead (<div.webgl> — `Tamás Olajos — AI Filmmaker & Dire`)**:
   - Landmark `<div class="webgl">` presenting display lead `Tamás Olajos — AI Filmmaker & Director · London ` and copy excerpt *"Tamás Olajos is an award-winning AI filmmaker and director, Runwa"* over `#000` canvas and `#0000` ink.
3. **Primary Showcase & Content Grid (<div.webgl> — `Featured Work & Interactive Showca`)**:
   - Landmark `<div class="webgl">` rendering section `Featured Work & Interactive Showcase` with copy *"Tamás Olajos — AI Filmmaker & Director · London "*, asset references (`favicon.svg`, `index-BZCf80GG.js`, `index-DcXtDSRr.css`, `showreel_short.mp4`), and grid rule `html { background-color:000;font-size:10px }`.
4. **Interactive Detail & Feature Matrix (<div.webgl> — `Technical Architecture & Narrative`)**:
   - Landmark `<div class="webgl">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Work & Interactive Showcase"*) with `#000` surface cards, `#0000` accents, and `.webgl { -webkit-user-select:none;user-select:none;width:100dvw;height:100dvh;pos... }`.
5. **Colophon & Global Directory Footer (<footer> — `https://tamasolajos.com/`)**:
   - Landmark `<footer>` landmark anchoring `Tamás Olajos — AI Filmmaker & Di` footer links (`Overview · Index · Archive · About · Contact`), copy *"Technical Architecture & Narrative"*, and `#0000` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: tamasolajos-com (Tamás Olajos — AI Filmmaker & Director · London & Budapest)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `tamasolajos-com` (**Tamás Olajos — AI Filmmaker & Director · London & Budapest** — `https://tamasolajos.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#0000`).
- **Identity & Domain Context**: Tamás Olajos is an award-winning AI filmmaker and director, Runway and Dreamina Creative Partner. Cinematic commercial campaigns and expe...
- **Primary Substrate**: `#000` (`html { background-color: #000 }`), **Primary Ink**: `#0000`, **Accent / Highlight**: `#0000`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`html { background-color: #000 }`) paired with `#0000` primary typography and `#0000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `system-ui, -apple-system, sans-serif` (no custom `@font-face` extracted) for display copy (`Tamás Olajos — AI Filmmaker & Direct`) with `system-ui, -apple-system, sans-serif` (no custom `@font-face` extracted) and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `none (full-bleed `100%` viewport stage)` container bounds (`gap: 0px (flush layout)`, padding `1rem`) with `cubic-bezier(0.25,0.1,0.25,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `tamasolajos-com` in your global stylesheet:

:root {
  /* Tamás Olajos — AI Filmmaker & Director · London & Budapest (tamasolajos-com) — Ground-Truth Extracted CSS Variables */
  --inner-height: 900px; /* Layout / Spatial Grid Token (tamasolajos-com) */
  --tamasolajos-com-bg: #000; /* Canvas Substrate (from `html { background-color: #000 }`) (tamasolajos-com) */
  --tamasolajos-com-ink: #0000; /* Primary Typography Ink (stylesheet-derived) (tamasolajos-com) */
  --tamasolajos-com-surface: #000; /* Surface Substrate (stylesheet-derived) (tamasolajos-com) */
  --tamasolajos-com-accent: #0000; /* Interactive Accent (stylesheet-derived) (tamasolajos-com) */
  --tamasolajos-com-muted: #0000; /* Secondary Ink (stylesheet-derived) (tamasolajos-com) */
  --tamasolajos-com-border: #0000; /* Structural Border (stylesheet-derived) (tamasolajos-com) */
  --tamasolajos-com-container: none; /* Container Bound (stylesheet-derived) (tamasolajos-com) */
  --tamasolajos-com-gap: 0px; /* Grid Gutter (stylesheet-derived) (tamasolajos-com) */
  --tamasolajos-com-pad: 1rem; /* Lateral Padding (stylesheet-derived) (tamasolajos-com) */
  --tamasolajos-com-ease: cubic-bezier(0.25,0.1,0.25,1); /* Primary Easing Function (tamasolajos-com) */
  --tamasolajos-com-radius: 4rem; /* Corner Radius (stylesheet-derived) (tamasolajos-com) */
  --tamasolajos-com-fs-base: 10px; /* Observed Font Size Token (tamasolajos-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000` — grounded in `html { background-color: #000 }`
- **Primary Typography Ink**: `#0000` — grounded in `.ui .button { border: #0000 }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `none (full-bleed `100%` viewport stage)` extracted from `tamasolajos-com` stylesheet
- **Padding & Gutters**: `1rem` lateral canvas padding with `0px (flush layout)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: none (full-bleed `100%` viewport stage)`, `gap: 0px (flush layout)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `1rem` horizontal padding
- **Media Queries**: no `@media` queries in static stylesheet (fluid viewport scaling)
- **Corner Radii**: `4rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `system-ui, -apple-system, sans-serif` (no custom `@font-face` extracted)
- **Body Font Stack**: `system-ui, -apple-system, sans-serif` (no custom `@font-face` extracted)
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `10px`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `10px`)
- **Body Copy Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `10px`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `10px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `tamasolajos-com` (`Tamás Olajos — AI Filmmaker & Director · London & Budapest`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.webgl> — `tamasolajos-com`)**:
   - DOM & Selectors: Landmark `<header class="webgl">` hosting `Tamás Olajos — AI Filmmaker & Direct` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-engine="three.js r181"`), and stylesheet rule `body { overscroll-behavior:none;touch-action:none;margin:0;padding:0;overflow:h... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.webgl> — `tamasolajos-com`)` (`tamasolajos-com`) adapts across no `@media` queries in static stylesheet (fluid viewport scaling) with `cubic-bezier(0.25,0.1,0.25,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<div.webgl> — `Tamás Olajos — AI Filmmaker & Dire`)**:
   - DOM & Selectors: Landmark `<div class="webgl">` presenting display lead `Tamás Olajos — AI Filmmaker & Director · London ` and copy excerpt *"Tamás Olajos is an award-winning AI filmmaker and director, Runwa"* over `#000` canvas and `#0000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#000` background with `#0000` headline `Tamás Olajos — AI Filmmaker & Director · London `.
3. **Primary Showcase & Content Grid (<div.webgl> — `Featured Work & Interactive Showca`)**:
   - DOM & Selectors: Landmark `<div class="webgl">` rendering section `Featured Work & Interactive Showcase` with copy *"Tamás Olajos — AI Filmmaker & Director · London "*, asset references (`favicon.svg`, `index-BZCf80GG.js`, `index-DcXtDSRr.css`, `showreel_short.mp4`), and grid rule `html { background-color:000;font-size:10px }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<div.webgl> — `Featured Work & Interactive Showca`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: none (full-bleed `100%` viewport stage)`, `gap: 0px (flush layout)`) on desktop and Single-column vertical stack at `390px` viewport width with `1rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<div.webgl> — `Technical Architecture & Narrative`)**:
   - DOM & Selectors: Landmark `<div class="webgl">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Work & Interactive Showcase"*) with `#000` surface cards, `#0000` accents, and `.webgl { -webkit-user-select:none;user-select:none;width:100dvw;height:100dvh;pos... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<div.webgl> — `Technical Architecture & Narrative`)` uses `4rem` radii, `#0000` highlights, and assets (favicon.svg, index-BZCf80GG.js, index-DcXtDSRr.css).
5. **Colophon & Global Directory Footer (<footer> — `https://tamasolajos.com/`)**:
   - DOM & Selectors: Landmark `<footer>` landmark anchoring `Tamás Olajos — AI Filmmaker & Di` footer links (`Overview · Index · Archive · About · Contact`), copy *"Technical Architecture & Narrative"*, and `#0000` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer> — `https://tamasolajos.com/`)` aligns to `none (full-bleed `100%` viewport stage)` extracted from `tamasolajos-com` stylesheet with `1rem` lateral canvas padding with `0px (flush layout)` grid gap and attributes (data-engine="three.js r181").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Lead Copy: *"Tamás Olajos is an award-winning AI filmmaker and director, Runway and Dreamina Creative Partner. Cinematic commercial campaigns and expe..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`
- **Extracted Stylesheet Rules (`tamasolajos-com`)**:
- `body { overscroll-behavior:none;touch-action:none;margin:0;padding:0;overflow:h... }`
- `html { background-color:000;font-size:10px }`
- `.webgl { -webkit-user-select:none;user-select:none;width:100dvw;height:100dvh;pos... }`
- `.ui { justify-content:space-between;width:100%;padding:1rem;display:flex;posit... }`
- `.ui .button img { opacity:.8;width:100%;height:100%;padding:1rem }`
- **Per-Selector Transition Rules**:
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in static CSS).
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `tamasolajos-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
