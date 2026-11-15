---
title: "UI Prompt Blueprint: herasymenkox-com"
date: 2026-11-15
target: "[[overview|herasymenkox-com]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#cee49f` / `#008000`)"
---

# UI Design System & Master Generation Blueprint: herasymenkox-com

> **Yehor Herasymenko — Digital Designer** (https://herasymenkox.com/) — Z I R K A I N T E R C E P T O R

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/herasymenkox-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Yehor Herasymenko — Digital Designer** (`https://herasymenkox.com/`). Z I R K A I N T E R C E P T O R
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#cee49f` / `#008000`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#cee49f` (`var(--green)` in `:root`) paired with `#000000` primary typography and `#008000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `PP Neue Montreal` for display copy (`Z I R K A I N T E R C E P T O R`) with `PP Neue Montreal Mono` and `PP Neue Montreal Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `600px` container bounds (`gap: 0px (flush layout)`, padding `0px`) with `cubic-bezier(0.625,0.05,0,1)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/herasymenkox-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `600px` extracted from `herasymenkox-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `0px` lateral canvas padding with `0px (flush layout)` grid gap.
- **Border Radius Scale**: `0px` (sharp unrounded corners).

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 600px`, `gap: 0px (flush layout)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `0px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width: 600px)`, `@media (min-width: 601px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#cee49f` | `var(--green)` in `:root` |
| **Primary Typography Ink** | `#0b0b0b` | `var(--black)` in `:root` |
| **Elevated Surface / Card Substrate** | `#000000` | `body { background: black }` (`#000000`) |
| **Interactive Accent / Highlight** | `#008000` | `body { color: green }` (`#008000`) |
| **Secondary / Muted Copy** | `#fff` | SVG/DOM `fill="#fff"` attribute in `dom.html` |
| **Structural Hairline Border** | `#000` | SVG/DOM `fill="#000"` attribute in `dom.html` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--design-width` | `1440` | Layout / Spatial Grid Token |
| `--container` | `clamp(1440px, 100vw, 2560px)` | Layout / Spatial Grid Token |
| `--px` | `calc(var(--container) / var(--design-width))` | Design System Custom Token |
| `--green` | `#cee49f` | Color / Atmospheric Token |
| `--black` | `#0b0b0b` | Canvas / Surface Token |
| `--green-12` | `rgba(206, 228, 159, 0.12)` | Color / Atmospheric Token |
| `--cap-bold` | `0.0215em` | Dimension / Scale Token |
| `--cap-mono` | `0.143em` | Typography / Scale Token |
| `--cap-height` | `0.715em` | Layout / Spatial Grid Token |
| `--fs` | `calc((100vw - 32 * var(--px)) / 6.6006)` | Dimension / Scale Token |
| `--y-w` | `600` | Design System Custom Token |
| `--y-h` | `580` | Design System Custom Token |
| `--cap` | `0.0915em` | Dimension / Scale Token |
| `--ext` | `calc(5.5 * var(--px) - 0.0635em)` | Dimension / Scale Token |
| `--left` | `0` | Design System Custom Token |
| `--width` | `12` | Layout / Spatial Grid Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `PP Neue Montreal`.
- **Primary Body Stack**: `PP Neue Montreal Mono`.
- **Technical / Metadata Stack**: `PP Neue Montreal Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--fs)`, `10px`, `6px`).
- **Section Heading (`H2`)**: rule `h2` (`font-weight: inherit`).
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--fs)`, `10px`, `6px`).
- **Metadata & Navigation Labels**: CSS variables `--cap-mono: 0.143em`; rule `.mono` (`font-size: calc(10 * var(--px))`, `line-height: 1`, `font-weight: 500`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.625,0.05,0,1)`, `cubic-bezier(0.16,1,0.3,1)`, `cubic-bezier(0,0.5,0.5,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.pill`**: `transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out` extracted from `herasymenkox-com` stylesheet.
- **Selector `.pill-knock`**: `transition: opacity 0.2s ease-in-out` extracted from `herasymenkox-com` stylesheet.
- **Selector `.view-switch-item::after`**: `transition: transform 0.735s cubic-bezier(0.625,0.05,0,1)` extracted from `herasymenkox-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.625,0.05,0,1)`)**: Governs interactive state transitions across `<nav.blend>` and `<div.blend>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Yehor Herasymenko — Digital Designer       │
│ ====================================================================== │
│ [ <nav.blend>              | Work (05) WORK (05) · Profile PROFILE  ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <div.gl>                                             |   │
│ | H1: Z I R K A I N T E R C E P T O R                              |   │
│ | Substrate: #cee49f    | Ink: #000000    | Accent: #008000        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<div.blend>               ) max-w: 600px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | E V O Q U E                  |  | D A R K N O D E              | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 0px (f) | │
│ | [<nav.blend>] -> [<div.gl>] -> [<div.blend>] |                       │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.corner>       ) | https://herasymenkox.com/          │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.blend> — `herasymenkox-com`)**:
   - Landmark `<nav class="blend menu">` hosting `Yehor Herasymenko — Digital Designer` navigation (`Work (05) WORK (05) · Profile PROFILE · Connect CONNECT`), DOM attributes (`data-orbit`, `data-engine="three.js r171"`, `data-gl`, `data-ui`), and stylesheet rule `after { box-sizing: border-box; }`.
2. **Hero Stage & Focal Lead (<div.gl> — `Z I R K A I N T E R C E P T O R`)**:
   - Landmark `<div class="gl">` presenting display lead `Z I R K A I N T E R C E P T O R` and copy excerpt *"Work (05) WORK (05) Profile PROFILE Connect CONNECT"* over `#cee49f` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<div.blend> — `E V O Q U E`)**:
   - Landmark `<div class="blend">` rendering section `E V O Q U E` with copy *"Work (05) WORK (05)"*, asset references (`favicon.svg`, `PPNeueMontreal-Bold.woff2`, `PPNeueMontrealMono-Medium.woff2`, `FHPhemister-Light.woff2`), and grid rule `body { margin: 0; height: 100%; overflow: hidden; background: var(--black); }`.
4. **Interactive Detail & Feature Matrix (<div.h3> — `D A R K N O D E`)**:
   - Landmark `<div class="h3">` framing `D A R K N O D E` and `F I T O S A U N A` (*"I N T E R C E P T O R"*) with `#000000` surface cards, `#008000` accents, and `h2 { margin: 0; font-weight: inherit; }`.
5. **Colophon & Global Directory Footer (<footer.corner> — `https://herasymenkox.com/`)**:
   - Landmark `<footer class="corner">` anchoring `Yehor Herasymenko — Digital Desi` footer links (`Work (05) WORK (05) · Profile PROFILE · Connect CONNECT`), copy *"Real Estate / 2025"*, and `#000` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: herasymenkox-com (Yehor Herasymenko — Digital Designer)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `herasymenkox-com` (**Yehor Herasymenko — Digital Designer** — `https://herasymenkox.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#cee49f` / `#008000`).
- **Identity & Domain Context**: Z I R K A I N T E R C E P T O R
- **Primary Substrate**: `#cee49f` (`var(--green)` in `:root`), **Primary Ink**: `#000000`, **Accent / Highlight**: `#008000`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#cee49f` (`var(--green)` in `:root`) paired with `#000000` primary typography and `#008000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `PP Neue Montreal` for display copy (`Z I R K A I N T E R C E P T O R`) with `PP Neue Montreal Mono` and `PP Neue Montreal Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `600px` container bounds (`gap: 0px (flush layout)`, padding `0px`) with `cubic-bezier(0.625,0.05,0,1)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `herasymenkox-com` in your global stylesheet:

:root {
  /* Yehor Herasymenko — Digital Designer (herasymenkox-com) — Ground-Truth Extracted CSS Variables */
  --design-width: 1440; /* Layout / Spatial Grid Token (herasymenkox-com) */
  --container: clamp(1440px, 100vw, 2560px); /* Layout / Spatial Grid Token (herasymenkox-com) */
  --px: calc(var(--container) / var(--design-width)); /* Design System Custom Token (herasymenkox-com) */
  --green: #cee49f; /* Color / Atmospheric Token (herasymenkox-com) */
  --black: #0b0b0b; /* Canvas / Surface Token (herasymenkox-com) */
  --green-12: rgba(206, 228, 159, 0.12); /* Color / Atmospheric Token (herasymenkox-com) */
  --cap-bold: 0.0215em; /* Dimension / Scale Token (herasymenkox-com) */
  --cap-mono: 0.143em; /* Typography / Scale Token (herasymenkox-com) */
  --cap-height: 0.715em; /* Layout / Spatial Grid Token (herasymenkox-com) */
  --fs: calc((100vw - 32 * var(--px)) / 6.6006); /* Dimension / Scale Token (herasymenkox-com) */
  --y-w: 600; /* Design System Custom Token (herasymenkox-com) */
  --y-h: 580; /* Design System Custom Token (herasymenkox-com) */
  --cap: 0.0915em; /* Dimension / Scale Token (herasymenkox-com) */
  --ext: calc(5.5 * var(--px) - 0.0635em); /* Dimension / Scale Token (herasymenkox-com) */
  --left: 0; /* Design System Custom Token (herasymenkox-com) */
  --width: 12; /* Layout / Spatial Grid Token (herasymenkox-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#cee49f` — grounded in `var(--green)` in `:root`
- **Primary Typography Ink**: `#0b0b0b` — grounded in `var(--black)` in `:root`
- **Elevated Surface / Card Substrate**: `#000000` — grounded in `body { background: black }` (`#000000`)
- **Interactive Accent / Highlight**: `#008000` — grounded in `body { color: green }` (`#008000`)
- **Secondary / Muted Copy**: `#fff` — grounded in SVG/DOM `fill="#fff"` attribute in `dom.html`
- **Structural Hairline Border**: `#000` — grounded in SVG/DOM `fill="#000"` attribute in `dom.html`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `600px` extracted from `herasymenkox-com` stylesheet
- **Padding & Gutters**: `0px` lateral canvas padding with `0px (flush layout)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 600px`, `gap: 0px (flush layout)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `0px` horizontal padding
- **Media Queries**: `@media (max-width: 600px)`, `@media (min-width: 601px)`
- **Corner Radii**: `0px` (sharp unrounded corners)

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `PP Neue Montreal`
- **Body Font Stack**: `PP Neue Montreal Mono`
- **Monospace / Technical Font Stack**: `PP Neue Montreal Mono`
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--fs)`, `10px`, `6px`)
- **H2 Section Rule**: rule `h2` (`font-weight: inherit`)
- **Body Copy Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--fs)`, `10px`, `6px`)
- **Metadata & Index Rule**: CSS variables `--cap-mono: 0.143em`; rule `.mono` (`font-size: calc(10 * var(--px))`, `line-height: 1`, `font-weight: 500`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `herasymenkox-com` (`Yehor Herasymenko — Digital Designer`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.blend> — `herasymenkox-com`)**:
   - DOM & Selectors: Landmark `<nav class="blend menu">` hosting `Yehor Herasymenko — Digital Designer` navigation (`Work (05) WORK (05) · Profile PROFILE · Connect CONNECT`), DOM attributes (`data-orbit`, `data-engine="three.js r171"`, `data-gl`, `data-ui`), and stylesheet rule `after { box-sizing: border-box; }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.blend> — `herasymenkox-com`)` (`herasymenkox-com`) adapts across `@media (max-width: 600px)`, `@media (min-width: 601px)` with `cubic-bezier(0.625,0.05,0,1)`, `cubic-bezier(0.16,1,0.3,1)`, `cubic-bezier(0,0.5,0.5,1)` transitions and links `Work (05) WORK (05) · Profile PROFILE · Connect CONNECT`.
2. **Hero Stage & Focal Lead (<div.gl> — `Z I R K A I N T E R C E P T O R`)**:
   - DOM & Selectors: Landmark `<div class="gl">` presenting display lead `Z I R K A I N T E R C E P T O R` and copy excerpt *"Work (05) WORK (05) Profile PROFILE Connect CONNECT"* over `#cee49f` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#cee49f` background with `#000000` headline `Z I R K A I N T E R C E P T O R`.
3. **Primary Showcase & Content Grid (<div.blend> — `E V O Q U E`)**:
   - DOM & Selectors: Landmark `<div class="blend">` rendering section `E V O Q U E` with copy *"Work (05) WORK (05)"*, asset references (`favicon.svg`, `PPNeueMontreal-Bold.woff2`, `PPNeueMontrealMono-Medium.woff2`, `FHPhemister-Light.woff2`), and grid rule `body { margin: 0; height: 100%; overflow: hidden; background: var(--black); }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<div.blend> — `E V O Q U E`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 600px`, `gap: 0px (flush layout)`) on desktop and Single-column vertical stack at `390px` viewport width with `0px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<div.h3> — `D A R K N O D E`)**:
   - DOM & Selectors: Landmark `<div class="h3">` framing `D A R K N O D E` and `F I T O S A U N A` (*"I N T E R C E P T O R"*) with `#000000` surface cards, `#008000` accents, and `h2 { margin: 0; font-weight: inherit; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<div.h3> — `D A R K N O D E`)` uses `0px` (sharp unrounded corners) radii, `#008000` highlights, and assets (favicon.svg, PPNeueMontreal-Bold.woff2, PPNeueMontrealMono-Medium.woff2).
5. **Colophon & Global Directory Footer (<footer.corner> — `https://herasymenkox.com/`)**:
   - DOM & Selectors: Landmark `<footer class="corner">` anchoring `Yehor Herasymenko — Digital Desi` footer links (`Work (05) WORK (05) · Profile PROFILE · Connect CONNECT`), copy *"Real Estate / 2025"*, and `#000` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.corner> — `https://herasymenkox.com/`)` aligns to `600px` extracted from `herasymenkox-com` stylesheet with `0px` lateral canvas padding with `0px (flush layout)` grid gap and attributes (data-orbit, data-engine="three.js r171", data-gl).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Work (05) WORK (05) Profile PROFILE Connect CONNECT"*
- Copy Excerpt 2: *"Work (05) WORK (05)"*
- Copy Excerpt 3: *"I N T E R C E P T O R"*
- Copy Excerpt 4: *"Real Estate / 2025"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.625,0.05,0,1)`, `cubic-bezier(0.16,1,0.3,1)`, `cubic-bezier(0,0.5,0.5,1)`
- **Extracted Stylesheet Rules (`herasymenkox-com`)**:
- `after { box-sizing: border-box; }`
- `body { margin: 0; height: 100%; overflow: hidden; background: var(--black); }`
- `h2 { margin: 0; font-weight: inherit; }`
- `.orbit { position: fixed; inset: 0; width: 100%; height: 100%; display: block; op... }`
- `.gl { position: fixed; inset: 0; width: 100%; height: 100%; display: block; op... }`
- **Per-Selector Transition Rules**:
- **Selector `.pill`**: `transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out` extracted from `herasymenkox-com` stylesheet.
- **Selector `.pill-knock`**: `transition: opacity 0.2s ease-in-out` extracted from `herasymenkox-com` stylesheet.
- **Selector `.view-switch-item::after`**: `transition: transform 0.735s cubic-bezier(0.625,0.05,0,1)` extracted from `herasymenkox-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.625,0.05,0,1)`)**: Governs interactive state transitions across `<nav.blend>` and `<div.blend>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `herasymenkox-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
