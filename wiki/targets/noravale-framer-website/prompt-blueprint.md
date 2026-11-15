---
title: "UI Prompt Blueprint: noravale-framer-website"
date: 2026-11-15
target: "[[overview|noravale-framer-website]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#0d0d0d` ink, `#fafafa` accent)"
---

# UI Design System & Master Generation Blueprint: noravale-framer-website

> **Blankit – Ultimate Portfolio System for Framer** (https://noravale.framer.website/) — The ultimate portfolio system for Framer. Build premium portfolio websites with components, templates and design foundations.

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/noravale-framer-website/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Blankit – Ultimate Portfolio System for Framer** (`https://noravale.framer.website/`). The ultimate portfolio system for Framer. Build premium portfolio websites with components, templates and design foundations.
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#0d0d0d` ink, `#fafafa` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`var(--token-835e5838-ad16-45ed-8524-d371a38640d4)` in `:root`) paired with `#0d0d0d` primary typography and `#fafafa` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Geist` for display copy (`Blankit – Ultimate Portfolio System `) with `Geist Variable` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `809px` container bounds (`gap: 10px`, padding `20px`) with `cubic-bezier(0.25,0.1,0.25,1)` easing and Lenis Smooth Scroll (`data-lenis`), Framer Motion Layout Physics.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/noravale-framer-website/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `809px` extracted from `noravale-framer-website` stylesheet.
- **Canvas Lateral Padding & Spacing**: `20px` lateral canvas padding with `10px` grid gap.
- **Border Radius Scale**: `8px`, `15px`, `0px`, `10px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 809px`, `gap: 10px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `20px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:809px) and (min-width:0)`, `@media (min-width:810px) and (max-width:1199.98px)`, `@media (max-width:809.98px)`, `@media (max-width:1199px) and (min-width:810px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--token-835e5838-ad16-45ed-8524-d371a38640d4)` in `:root` |
| **Primary Typography Ink** | `#292929` | `var(--token-658e57be-7dc2-47f6-a641-0a3d91f5f0a7)` in `:root` |
| **Elevated Surface / Card Substrate** | `#0000` | `var(--token-7454ffba-6ef4-4d38-9965-d502f06ebc49)` in `:root` |
| **Interactive Accent / Highlight** | `#fafafa` | `var(--token-fab8f350-6af4-4276-a121-46955910532e)` in `:root` |
| **Secondary / Muted Copy** | `#f2f2f2` | `var(--token-7edb6191-4ddd-4bbc-96d5-e5e591d6ed9b)` in `:root` |
| **Structural Hairline Border** | `#0d0d0d` | `var(--token-5f666cb9-74f6-4b15-aaed-8cf125fa4837)` in `:root` |
| **Variable Token (`--token-37582e93-848e-41c2-9a6a-be05b3cb724b`)** | `#000` | `var(--token-37582e93-848e-41c2-9a6a-be05b3cb724b)` in `:root` |
| **Variable Token (`--token-58ed9133-56c7-4c1c-83a9-d6e40daeeb72`)** | `#08080880` | `var(--token-58ed9133-56c7-4c1c-83a9-d6e40daeeb72)` in `:root` |
| **Variable Token (`--token-68cbe2e9-85cc-47c7-aa5a-bac039f90af2`)** | `#757575` | `var(--token-68cbe2e9-85cc-47c7-aa5a-bac039f90af2)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--token-835e5838-ad16-45ed-8524-d371a38640d4` | `#fff` | Color / Atmospheric Token |
| `--token-658e57be-7dc2-47f6-a641-0a3d91f5f0a7` | `#292929` | Color / Atmospheric Token |
| `--token-c9613b9a-ea67-4e25-b1ae-1822b810d41e` | `#fff` | Color / Atmospheric Token |
| `--token-7454ffba-6ef4-4d38-9965-d502f06ebc49` | `#0000` | Color / Atmospheric Token |
| `--token-fab8f350-6af4-4276-a121-46955910532e` | `#fafafa` | Color / Atmospheric Token |
| `--token-7edb6191-4ddd-4bbc-96d5-e5e591d6ed9b` | `#f2f2f2` | Color / Atmospheric Token |
| `--token-5f666cb9-74f6-4b15-aaed-8cf125fa4837` | `#0d0d0d` | Color / Atmospheric Token |
| `--token-c2a7bcb4-4b1e-42b6-859b-d5fb68f2e51c` | `#0d0d0d` | Color / Atmospheric Token |
| `--token-37582e93-848e-41c2-9a6a-be05b3cb724b` | `#000` | Color / Atmospheric Token |
| `--token-de44e4c4-2780-4f6a-920a-6573964b909b` | `#fff` | Color / Atmospheric Token |
| `--token-58ed9133-56c7-4c1c-83a9-d6e40daeeb72` | `#08080880` | Color / Atmospheric Token |
| `--token-43292462-1240-4872-bac6-680eed5be9b9` | `#000` | Color / Atmospheric Token |
| `--token-4f3e38f4-83ad-43b0-9e27-1d245f644e53` | `#000` | Color / Atmospheric Token |
| `--token-68cbe2e9-85cc-47c7-aa5a-bac039f90af2` | `#757575` | Color / Atmospheric Token |
| `--token-35adfe75-6afb-4a33-9225-016fa16ccba3` | `#000` | Color / Atmospheric Token |
| `--token-a0b6ff5f-d52f-4ed7-9c5e-cd9e56ee7714` | `#000` | Color / Atmospheric Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Geist`.
- **Primary Body Stack**: `Geist Variable`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `var(--font-size)`, `var(--framer-font-size)`, `16px`, `14px`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `var(--font-size)`, `var(--framer-font-size)`, `16px`, `14px`).
- **Body Copy**: rule `p` (`font-size: 14px`, `line-height: 17px`, `letter-spacing: -.02em`, `font-weight: 400`).
- **Metadata & Navigation Labels**: CSS variables `--letter-spacing: var(--framer-letter-spacing)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `#__framer-editorbar-label`**: `transition: opacity 0.4s ease-out` extracted from `noravale-framer-website` stylesheet.
- **Selector `.lenis.lenis-autoToggle`**: `transition: 1ms` extracted from `noravale-framer-website` stylesheet.
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in static CSS).
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Blankit – Ultimate Portfolio System for Fr │
│ ====================================================================== │
│ [ <header.lenis>           | Overview · Index · Archive · About · C ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <main.framer-17y96vw>                                |   │
│ | H1: Blankit – Ultimate Portfolio System for Framer               |   │
│ | Substrate: #fff       | Ink: #0d0d0d    | Accent: #fafafa        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<main.framer-17y96vw>     ) max-w: 809px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Featured Work & Interactive  |  | Technical Architecture & Nar | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 10px  ) | │
│ | [<header.lenis>] -> [<main.framer-17y96] -> [<main.framer-17y96] |   │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.framer-RrLH2> ) | https://noravale.framer.website/   │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.lenis> — `noravale-framer-website`)**:
   - Landmark `<header class="lenis">` hosting `Blankit – Ultimate Portfolio System ` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-framer-font-css`, `data-framer-css-ssr-minified`, `data-framer-components="framer-lib-cursors-ho..."`, `data-framer-css="true"`), and stylesheet rule `main { box-sizing:border-box;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<main.framer-17y96vw> — `Blankit – Ultimate Portfolio Syste`)**:
   - Landmark `<main class="framer-17y96vw">` presenting display lead `Blankit – Ultimate Portfolio System for Framer` and copy excerpt *"K i n d r e d B u i l d i n g a l i f e s t y l e b r a n d r o o"* over `#fff` canvas and `#0d0d0d` ink.
3. **Primary Showcase & Content Grid (<main.framer-17y96vw> — `Featured Work & Interactive Showca`)**:
   - Landmark `<main class="framer-17y96vw">` rendering section `Featured Work & Interactive Showcase` with copy *"B u i l d i n g a l i f e s t y l e b r a n d r o o t e d i n c o"*, asset references (`default-favicon-light.v1.png`, `default-favicon-dark.v1.png`, `default-touch-icon.v3.png`, `fonts.gstatic.com`), and grid rule `root { -webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale }`.
4. **Interactive Detail & Feature Matrix (<main.framer-17y96vw> — `Technical Architecture & Narrative`)**:
   - Landmark `<main class="framer-17y96vw">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"L u m a A d i g i t a l - f i r s t i d e n t i t y f o r a f a s"*) with `#0000` surface cards, `#fafafa` accents, and `button { font-family:sans-serif;font-size:12px }`.
5. **Colophon & Global Directory Footer (<footer.framer-RrLH2> — `https://noravale.framer.website/`)**:
   - Landmark `<footer class="framer-RrLH2">` anchoring `Blankit – Ultimate Portfolio Sys` footer links (`Overview · Index · Archive · About · Contact`), copy *"A d i g i t a l - f i r s t i d e n t i t y f o r a f a s t "*, and `#0d0d0d` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: noravale-framer-website (Blankit – Ultimate Portfolio System for Framer)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `noravale-framer-website` (**Blankit – Ultimate Portfolio System for Framer** — `https://noravale.framer.website/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#0d0d0d` ink, `#fafafa` accent).
- **Identity & Domain Context**: The ultimate portfolio system for Framer. Build premium portfolio websites with components, templates and design foundations.
- **Primary Substrate**: `#fff` (`var(--token-835e5838-ad16-45ed-8524-d371a38640d4)` in `:root`), **Primary Ink**: `#0d0d0d`, **Accent / Highlight**: `#fafafa`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`var(--token-835e5838-ad16-45ed-8524-d371a38640d4)` in `:root`) paired with `#0d0d0d` primary typography and `#fafafa` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Geist` for display copy (`Blankit – Ultimate Portfolio System `) with `Geist Variable` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `809px` container bounds (`gap: 10px`, padding `20px`) with `cubic-bezier(0.25,0.1,0.25,1)` easing and Lenis Smooth Scroll (`data-lenis`), Framer Motion Layout Physics.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `noravale-framer-website` in your global stylesheet:

:root {
  /* Blankit – Ultimate Portfolio System for Framer (noravale-framer-website) — Ground-Truth Extracted CSS Variables */
  --token-835e5838-ad16-45ed-8524-d371a38640d4: #fff; /* Color / Atmospheric Token (noravale-framer-website) */
  --token-658e57be-7dc2-47f6-a641-0a3d91f5f0a7: #292929; /* Color / Atmospheric Token (noravale-framer-website) */
  --token-c9613b9a-ea67-4e25-b1ae-1822b810d41e: #fff; /* Color / Atmospheric Token (noravale-framer-website) */
  --token-7454ffba-6ef4-4d38-9965-d502f06ebc49: #0000; /* Color / Atmospheric Token (noravale-framer-website) */
  --token-fab8f350-6af4-4276-a121-46955910532e: #fafafa; /* Color / Atmospheric Token (noravale-framer-website) */
  --token-7edb6191-4ddd-4bbc-96d5-e5e591d6ed9b: #f2f2f2; /* Color / Atmospheric Token (noravale-framer-website) */
  --token-5f666cb9-74f6-4b15-aaed-8cf125fa4837: #0d0d0d; /* Color / Atmospheric Token (noravale-framer-website) */
  --token-c2a7bcb4-4b1e-42b6-859b-d5fb68f2e51c: #0d0d0d; /* Color / Atmospheric Token (noravale-framer-website) */
  --token-37582e93-848e-41c2-9a6a-be05b3cb724b: #000; /* Color / Atmospheric Token (noravale-framer-website) */
  --token-de44e4c4-2780-4f6a-920a-6573964b909b: #fff; /* Color / Atmospheric Token (noravale-framer-website) */
  --token-58ed9133-56c7-4c1c-83a9-d6e40daeeb72: #08080880; /* Color / Atmospheric Token (noravale-framer-website) */
  --token-43292462-1240-4872-bac6-680eed5be9b9: #000; /* Color / Atmospheric Token (noravale-framer-website) */
  --token-4f3e38f4-83ad-43b0-9e27-1d245f644e53: #000; /* Color / Atmospheric Token (noravale-framer-website) */
  --token-68cbe2e9-85cc-47c7-aa5a-bac039f90af2: #757575; /* Color / Atmospheric Token (noravale-framer-website) */
  --token-35adfe75-6afb-4a33-9225-016fa16ccba3: #000; /* Color / Atmospheric Token (noravale-framer-website) */
  --token-a0b6ff5f-d52f-4ed7-9c5e-cd9e56ee7714: #000; /* Color / Atmospheric Token (noravale-framer-website) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fff` — grounded in `var(--token-835e5838-ad16-45ed-8524-d371a38640d4)` in `:root`
- **Primary Typography Ink**: `#292929` — grounded in `var(--token-658e57be-7dc2-47f6-a641-0a3d91f5f0a7)` in `:root`
- **Elevated Surface / Card Substrate**: `#0000` — grounded in `var(--token-7454ffba-6ef4-4d38-9965-d502f06ebc49)` in `:root`
- **Interactive Accent / Highlight**: `#fafafa` — grounded in `var(--token-fab8f350-6af4-4276-a121-46955910532e)` in `:root`
- **Secondary / Muted Copy**: `#f2f2f2` — grounded in `var(--token-7edb6191-4ddd-4bbc-96d5-e5e591d6ed9b)` in `:root`
- **Structural Hairline Border**: `#0d0d0d` — grounded in `var(--token-5f666cb9-74f6-4b15-aaed-8cf125fa4837)` in `:root`
- **Variable Token (`--token-37582e93-848e-41c2-9a6a-be05b3cb724b`)**: `#000` — grounded in `var(--token-37582e93-848e-41c2-9a6a-be05b3cb724b)` in `:root`
- **Variable Token (`--token-58ed9133-56c7-4c1c-83a9-d6e40daeeb72`)**: `#08080880` — grounded in `var(--token-58ed9133-56c7-4c1c-83a9-d6e40daeeb72)` in `:root`
- **Variable Token (`--token-68cbe2e9-85cc-47c7-aa5a-bac039f90af2`)**: `#757575` — grounded in `var(--token-68cbe2e9-85cc-47c7-aa5a-bac039f90af2)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `809px` extracted from `noravale-framer-website` stylesheet
- **Padding & Gutters**: `20px` lateral canvas padding with `10px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 809px`, `gap: 10px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `20px` horizontal padding
- **Media Queries**: `@media (max-width:809px) and (min-width:0)`, `@media (min-width:810px) and (max-width:1199.98px)`, `@media (max-width:809.98px)`, `@media (max-width:1199px) and (min-width:810px)`
- **Corner Radii**: `8px`, `15px`, `0px`, `10px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Geist`
- **Body Font Stack**: `Geist Variable`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `var(--font-size)`, `var(--framer-font-size)`, `16px`, `14px`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `var(--font-size)`, `var(--framer-font-size)`, `16px`, `14px`)
- **Body Copy Rule**: rule `p` (`font-size: 14px`, `line-height: 17px`, `letter-spacing: -.02em`, `font-weight: 400`)
- **Metadata & Index Rule**: CSS variables `--letter-spacing: var(--framer-letter-spacing)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `noravale-framer-website` (`Blankit – Ultimate Portfolio System for Framer`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.lenis> — `noravale-framer-website`)**:
   - DOM & Selectors: Landmark `<header class="lenis">` hosting `Blankit – Ultimate Portfolio System ` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-framer-font-css`, `data-framer-css-ssr-minified`, `data-framer-components="framer-lib-cursors-ho..."`, `data-framer-css="true"`), and stylesheet rule `main { box-sizing:border-box;margin:0;padding:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.lenis> — `noravale-framer-website`)` (`noravale-framer-website`) adapts across `@media (max-width:809px) and (min-width:0)`, `@media (min-width:810px) and (max-width:1199.98px)`, `@media (max-width:809.98px)`, `@media (max-width:1199px) and (min-width:810px)` with `cubic-bezier(0.25,0.1,0.25,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<main.framer-17y96vw> — `Blankit – Ultimate Portfolio Syste`)**:
   - DOM & Selectors: Landmark `<main class="framer-17y96vw">` presenting display lead `Blankit – Ultimate Portfolio System for Framer` and copy excerpt *"K i n d r e d B u i l d i n g a l i f e s t y l e b r a n d r o o"* over `#fff` canvas and `#0d0d0d` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#fff` background with `#0d0d0d` headline `Blankit – Ultimate Portfolio System for Framer`.
3. **Primary Showcase & Content Grid (<main.framer-17y96vw> — `Featured Work & Interactive Showca`)**:
   - DOM & Selectors: Landmark `<main class="framer-17y96vw">` rendering section `Featured Work & Interactive Showcase` with copy *"B u i l d i n g a l i f e s t y l e b r a n d r o o t e d i n c o"*, asset references (`default-favicon-light.v1.png`, `default-favicon-dark.v1.png`, `default-touch-icon.v3.png`, `fonts.gstatic.com`), and grid rule `root { -webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<main.framer-17y96vw> — `Featured Work & Interactive Showca`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 809px`, `gap: 10px`) on desktop and Single-column vertical stack at `390px` viewport width with `20px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<main.framer-17y96vw> — `Technical Architecture & Narrative`)**:
   - DOM & Selectors: Landmark `<main class="framer-17y96vw">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"L u m a A d i g i t a l - f i r s t i d e n t i t y f o r a f a s"*) with `#0000` surface cards, `#fafafa` accents, and `button { font-family:sans-serif;font-size:12px }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<main.framer-17y96vw> — `Technical Architecture & Narrative`)` uses `8px`, `15px`, `0px`, `10px` radii, `#fafafa` highlights, and assets (default-favicon-light.v1.png, default-favicon-dark.v1.png, default-touch-icon.v3.png).
5. **Colophon & Global Directory Footer (<footer.framer-RrLH2> — `https://noravale.framer.website/`)**:
   - DOM & Selectors: Landmark `<footer class="framer-RrLH2">` anchoring `Blankit – Ultimate Portfolio Sys` footer links (`Overview · Index · Archive · About · Contact`), copy *"A d i g i t a l - f i r s t i d e n t i t y f o r a f a s t "*, and `#0d0d0d` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.framer-RrLH2> — `https://noravale.framer.website/`)` aligns to `809px` extracted from `noravale-framer-website` stylesheet with `20px` lateral canvas padding with `10px` grid gap and attributes (data-framer-font-css, data-framer-css-ssr-minified, data-framer-components="framer-lib-cursors-ho...").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"K i n d r e d B u i l d i n g a l i f e s t y l e b r a n d r o o t e d i n c o m..."*
- Copy Excerpt 2: *"B u i l d i n g a l i f e s t y l e b r a n d r o o t e d i n c o m m u n i t y a..."*
- Copy Excerpt 3: *"L u m a A d i g i t a l - f i r s t i d e n t i t y f o r a f a s t - g r o w i n..."*
- Copy Excerpt 4: *"A d i g i t a l - f i r s t i d e n t i t y f o r a f a s t - g r o w i n g s k i..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`
- **Extracted Stylesheet Rules (`noravale-framer-website`)**:
- `main { box-sizing:border-box;margin:0;padding:0 }`
- `root { -webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale }`
- `button { font-family:sans-serif;font-size:12px }`
- `__framer-badge-container { --infinity:infinity }`
- `body { --framer-will-change-override:none }`
- **Per-Selector Transition Rules**:
- **Selector `#__framer-editorbar-label`**: `transition: opacity 0.4s ease-out` extracted from `noravale-framer-website` stylesheet.
- **Selector `.lenis.lenis-autoToggle`**: `transition: 1ms` extracted from `noravale-framer-website` stylesheet.
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in static CSS).
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `noravale-framer-website`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
