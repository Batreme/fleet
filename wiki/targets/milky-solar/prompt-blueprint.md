---
title: "UI Prompt Blueprint: milky-solar"
date: 2026-11-15
target: "[[overview|milky-solar]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#000000` accent)"
---

# UI Design System & Master Generation Blueprint: milky-solar

> **Earth** (https://milky.solar) — Follow Wolfs journeys on Earth, navigating eternal cycles of conflict and transformation.

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/milky-solar/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Earth** (`https://milky.solar`). Follow Wolfs journeys on Earth, navigating eternal cycles of conflict and transformation.
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#000000` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#ffffff` (`body { background-color: white }` (`#ffffff`)) paired with `#000000` primary typography and `#000000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Arial` for display copy (`Earth`) with `Helvetica` and `Courier New`.
  - **Calibrated Spatial Grid & Motion**: Combines `890px` container bounds (`gap: 0px (flush layout)`, padding `4px`) with `cubic-bezier(0.25,0.1,0.25,1)` easing.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/milky-solar/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `890px` extracted from `milky-solar` stylesheet.
- **Canvas Lateral Padding & Spacing**: `4px` lateral canvas padding with `0px (flush layout)` grid gap.
- **Border Radius Scale**: `1px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 890px`, `gap: 0px (flush layout)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `4px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width: 890px)`, `@media (max-width: 600px)`, `@media (max-width: 320px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | `body { background-color: white }` (`#ffffff`) |
| **Primary Typography Ink** | `#000000` | `body { color: black }` (`#000000`) |
| **Elevated Surface / Card Substrate** | `#ff0000` | `select { border: red }` (`#ff0000`) |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--milky-solar-bg` | `#ffffff` | Canvas Substrate (from `body { background-color: white }` (`#ffffff`)) |
| `--milky-solar-ink` | `#000000` | Primary Typography Ink (stylesheet-derived) |
| `--milky-solar-surface` | `#ff0000` | Surface Substrate (stylesheet-derived) |
| `--milky-solar-accent` | `#000000` | Interactive Accent (stylesheet-derived) |
| `--milky-solar-muted` | `#000000` | Secondary Ink (stylesheet-derived) |
| `--milky-solar-border` | `#000000` | Structural Border (stylesheet-derived) |
| `--milky-solar-container` | `890px` | Container Bound (stylesheet-derived) |
| `--milky-solar-gap` | `0px` | Grid Gutter (stylesheet-derived) |
| `--milky-solar-pad` | `4px` | Lateral Padding (stylesheet-derived) |
| `--milky-solar-ease` | `cubic-bezier(0.25,0.1,0.25,1)` | Primary Easing Function |
| `--milky-solar-radius` | `1px` | Corner Radius (stylesheet-derived) |
| `--milky-solar-fs-base` | `16px` | Observed Font Size Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Arial`.
- **Primary Body Stack**: `Helvetica`.
- **Technical / Metadata Stack**: `Courier New`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`).
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `#user-submit`**: `transition: 0.2s` extracted from `milky-solar` stylesheet.
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in static CSS).
- **State & Hover Choreography**: Opacity and transform transitions on `<main.empty-space>` and `<main.float-up>` interactive targets.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Earth                                      │
│ ====================================================================== │
│ [ <header.button>          | Overview · Index · Archive · About · C ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <main.empty-space>                                   |   │
│ | H1: Earth                                                        |   │
│ | Substrate: #ffffff    | Ink: #000000    | Accent: #000000        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<main.float-up>           ) max-w: 890px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Featured Work & Interactive  |  | Technical Architecture & Nar | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 0px (f) | │
│ | [<header.button>] -> [<main.empty-space>] -> [<main.float-up>] |     │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.float-down>   ) | https://milky.solar                │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.button> — `milky-solar`)**:
   - Landmark `<header class="button">` hosting `Earth` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-scenario="new"`, `data-scenario="otherworld"`, `data-scenario="random"`, `data-scenario="israel"`), and stylesheet rule `body { background-color: white; color: black; width: 800px; text-align: center;... }`.
2. **Hero Stage & Focal Lead (<main.empty-space> — `Earth`)**:
   - Landmark `<main class="empty-space">` presenting display lead `Earth` and copy excerpt *"Follow Wolfs journeys on Earth, navigating eternal cycles of conf"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<main.float-up> — `Featured Work & Interactive Showca`)**:
   - Landmark `<main class="float-up">` rendering section `Featured Work & Interactive Showcase` with copy *"Earth"*, asset references (`milky.solar`, `Logo.ico`, `Logo.svg`, `Logo.jpg`), and grid rule `header { width: 100%; }`.
4. **Interactive Detail & Feature Matrix (<main.balloon> — `Technical Architecture & Narrative`)**:
   - Landmark `<main class="balloon">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Work & Interactive Showcase"*) with `#ff0000` surface cards, `#000000` accents, and `main { margin-bottom: 20px; }`.
5. **Colophon & Global Directory Footer (<footer.float-down> — `https://milky.solar`)**:
   - Landmark `<footer class="float-down">` anchoring `Earth` footer links (`Overview · Index · Archive · About · Contact`), copy *"Technical Architecture & Narrative"*, and `#000000` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: milky-solar (Earth)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `milky-solar` (**Earth** — `https://milky.solar`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#000000` accent).
- **Identity & Domain Context**: Follow Wolfs journeys on Earth, navigating eternal cycles of conflict and transformation.
- **Primary Substrate**: `#ffffff` (`body { background-color: white }` (`#ffffff`)), **Primary Ink**: `#000000`, **Accent / Highlight**: `#000000`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#ffffff` (`body { background-color: white }` (`#ffffff`)) paired with `#000000` primary typography and `#000000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Arial` for display copy (`Earth`) with `Helvetica` and `Courier New`.
  - **Calibrated Spatial Grid & Motion**: Combines `890px` container bounds (`gap: 0px (flush layout)`, padding `4px`) with `cubic-bezier(0.25,0.1,0.25,1)` easing.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `milky-solar` in your global stylesheet:

:root {
  /* Earth (milky-solar) — Ground-Truth Extracted CSS Variables */
  --milky-solar-bg: #ffffff; /* Canvas Substrate (from `body { background-color: white }` (`#ffffff`)) (milky-solar) */
  --milky-solar-ink: #000000; /* Primary Typography Ink (stylesheet-derived) (milky-solar) */
  --milky-solar-surface: #ff0000; /* Surface Substrate (stylesheet-derived) (milky-solar) */
  --milky-solar-accent: #000000; /* Interactive Accent (stylesheet-derived) (milky-solar) */
  --milky-solar-muted: #000000; /* Secondary Ink (stylesheet-derived) (milky-solar) */
  --milky-solar-border: #000000; /* Structural Border (stylesheet-derived) (milky-solar) */
  --milky-solar-container: 890px; /* Container Bound (stylesheet-derived) (milky-solar) */
  --milky-solar-gap: 0px; /* Grid Gutter (stylesheet-derived) (milky-solar) */
  --milky-solar-pad: 4px; /* Lateral Padding (stylesheet-derived) (milky-solar) */
  --milky-solar-ease: cubic-bezier(0.25,0.1,0.25,1); /* Primary Easing Function (milky-solar) */
  --milky-solar-radius: 1px; /* Corner Radius (stylesheet-derived) (milky-solar) */
  --milky-solar-fs-base: 16px; /* Observed Font Size Token (milky-solar) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in `body { background-color: white }` (`#ffffff`)
- **Primary Typography Ink**: `#000000` — grounded in `body { color: black }` (`#000000`)
- **Elevated Surface / Card Substrate**: `#ff0000` — grounded in `select { border: red }` (`#ff0000`)

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `890px` extracted from `milky-solar` stylesheet
- **Padding & Gutters**: `4px` lateral canvas padding with `0px (flush layout)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 890px`, `gap: 0px (flush layout)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `4px` horizontal padding
- **Media Queries**: `@media (max-width: 890px)`, `@media (max-width: 600px)`, `@media (max-width: 320px)`
- **Corner Radii**: `1px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Arial`
- **Body Font Stack**: `Helvetica`
- **Monospace / Technical Font Stack**: `Courier New`
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`)
- **Body Copy Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `milky-solar` (`Earth`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.button> — `milky-solar`)**:
   - DOM & Selectors: Landmark `<header class="button">` hosting `Earth` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-scenario="new"`, `data-scenario="otherworld"`, `data-scenario="random"`, `data-scenario="israel"`), and stylesheet rule `body { background-color: white; color: black; width: 800px; text-align: center;... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.button> — `milky-solar`)` (`milky-solar`) adapts across `@media (max-width: 890px)`, `@media (max-width: 600px)`, `@media (max-width: 320px)` with `cubic-bezier(0.25,0.1,0.25,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<main.empty-space> — `Earth`)**:
   - DOM & Selectors: Landmark `<main class="empty-space">` presenting display lead `Earth` and copy excerpt *"Follow Wolfs journeys on Earth, navigating eternal cycles of conf"* over `#ffffff` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#ffffff` background with `#000000` headline `Earth`.
3. **Primary Showcase & Content Grid (<main.float-up> — `Featured Work & Interactive Showca`)**:
   - DOM & Selectors: Landmark `<main class="float-up">` rendering section `Featured Work & Interactive Showcase` with copy *"Earth"*, asset references (`milky.solar`, `Logo.ico`, `Logo.svg`, `Logo.jpg`), and grid rule `header { width: 100%; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<main.float-up> — `Featured Work & Interactive Showca`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 890px`, `gap: 0px (flush layout)`) on desktop and Single-column vertical stack at `390px` viewport width with `4px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<main.balloon> — `Technical Architecture & Narrative`)**:
   - DOM & Selectors: Landmark `<main class="balloon">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Work & Interactive Showcase"*) with `#ff0000` surface cards, `#000000` accents, and `main { margin-bottom: 20px; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<main.balloon> — `Technical Architecture & Narrative`)` uses `1px` radii, `#000000` highlights, and assets (milky.solar, Logo.ico, Logo.svg).
5. **Colophon & Global Directory Footer (<footer.float-down> — `https://milky.solar`)**:
   - DOM & Selectors: Landmark `<footer class="float-down">` anchoring `Earth` footer links (`Overview · Index · Archive · About · Contact`), copy *"Technical Architecture & Narrative"*, and `#000000` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.float-down> — `https://milky.solar`)` aligns to `890px` extracted from `milky-solar` stylesheet with `4px` lateral canvas padding with `0px (flush layout)` grid gap and attributes (data-scenario="new", data-scenario="otherworld", data-scenario="random").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Lead Copy: *"Follow Wolfs journeys on Earth, navigating eternal cycles of conflict and transformation."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`
- **Extracted Stylesheet Rules (`milky-solar`)**:
- `body { background-color: white; color: black; width: 800px; text-align: center;... }`
- `header { width: 100%; }`
- `main { margin-bottom: 20px; }`
- `footer { border-top: 1px solid black; padding-top: 10px; margin-bottom: 62px; }`
- `select option { background-color: white; color: red; }`
- **Per-Selector Transition Rules**:
- **Selector `#user-submit`**: `transition: 0.2s` extracted from `milky-solar` stylesheet.
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in static CSS).
- **State & Hover Choreography**: Opacity and transform transitions on `<main.empty-space>` and `<main.float-up>` interactive targets.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `milky-solar`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
