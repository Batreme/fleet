---
title: "UI Prompt Blueprint: newminds-studio_concept-elune"
date: 2026-11-15
target: "[[overview|newminds-studio_concept-elune]]"
status: analyzed
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#151a18` canvas, `#fff` ink, `#c9d1cc` accent)"
---

# UI Design System & Master Generation Blueprint: newminds-studio_concept-elune

> **ELUNE Women's Health App UX/UI Concept · New Minds** (https://newminds.studio/concept-elune) — Women's health app UX/UI concept by New Minds: cycle tracking, bloodwork records and a separate pregnancy journey. Explore the complete c...

![Desktop Viewport Capture (1440x11083)](file:///root/projects/fleet/wiki/targets/newminds-studio_concept-elune/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **ELUNE Women's Health App UX/UI Concept · New Minds** (`https://newminds.studio/concept-elune`). Women's health app UX/UI concept by New Minds: cycle tracking, bloodwork records and a separate pregnancy journey. Explore the complete c...
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#151a18` canvas, `#fff` ink, `#c9d1cc` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#151a18` (`body { background: #151a18 }`) paired with `#fff` primary typography and `#c9d1cc` accents.
  - **Extracted Typographic Hierarchy**: Pairs `system-ui, -apple-system, sans-serif` (no custom `@font-face` extracted) for display copy (`Women's health, with room for contex`) with `system-ui, -apple-system, sans-serif` (no custom `@font-face` extracted) and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1400px` container bounds (`gap: 15px`, padding `24px`) with `cubic-bezier(0.25,0.1,0.25,1)` easing.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/newminds-studio_concept-elune/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×11083px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `1400px` extracted from `newminds-studio_concept-elune` stylesheet.
- **Canvas Lateral Padding & Spacing**: `24px` lateral canvas padding with `15px` grid gap.
- **Border Radius Scale**: `7px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1400px`, `gap: 15px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `24px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:600px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#151a18` | `body { background: #151a18 }` |
| **Primary Typography Ink** | `#fff` | `body { color: #fff }` |
| **Elevated Surface / Card Substrate** | `#d5fc65` | `a { color: #d5fc65 }` |
| **Interactive Accent / Highlight** | `#c9d1cc` | `.case-context p { color: #c9d1cc }` |
| **Secondary / Muted Copy** | `#7e8c77` | `.case-actions a { border: #7e8c77 }` |
| **Structural Hairline Border** | `#a9b6ac` | `footer { color: #a9b6ac }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--newminds-studio--bg` | `#151a18` | Canvas Substrate (from `body { background: #151a18 }`) |
| `--newminds-studio--ink` | `#fff` | Primary Typography Ink (stylesheet-derived) |
| `--newminds-studio--surface` | `#d5fc65` | Surface Substrate (stylesheet-derived) |
| `--newminds-studio--accent` | `#c9d1cc` | Interactive Accent (stylesheet-derived) |
| `--newminds-studio--muted` | `#7e8c77` | Secondary Ink (stylesheet-derived) |
| `--newminds-studio--border` | `#a9b6ac` | Structural Border (stylesheet-derived) |
| `--newminds-studio--container` | `1400px` | Container Bound (stylesheet-derived) |
| `--newminds-studio--gap` | `15px` | Grid Gutter (stylesheet-derived) |
| `--newminds-studio--pad` | `24px` | Lateral Padding (stylesheet-derived) |
| `--newminds-studio--ease` | `cubic-bezier(0.25,0.1,0.25,1)` | Primary Easing Function |
| `--newminds-studio--radius` | `7px` | Corner Radius (stylesheet-derived) |
| `--newminds-studio--fs-base` | `11px` | Observed Font Size Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `system-ui, -apple-system, sans-serif` (no custom `@font-face` extracted).
- **Primary Body Stack**: `system-ui, -apple-system, sans-serif` (no custom `@font-face` extracted).
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`font-size: clamp(38px,6vw,76px)`, `line-height: 1.06`, `letter-spacing: -.045em`, `font-weight: 500`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(26px,3.5vw,42px)`, `line-height: 1.15`, `letter-spacing: -.03em`, `font-weight: 500`).
- **Body Copy**: rule `p` (`font-size: clamp(16px,1.7vw,20px)`, `line-height: 1.75`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `11px`, `clamp(38px,6vw,76px)`, `clamp(16px,1.7vw,20px)`, `14px`, `clamp(26px,3.5vw,42px)`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`.

### Per-Element Transition & Choreography Rules
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in static CSS).
- **State & Hover Choreography**: Opacity and transform transitions on `<section.case-intro>` and `<section.case-context>` interactive targets.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — ELUNE Women's Health App UX/UI Concept · N │
│ ====================================================================== │
│ [ <header.skip-case>       | More concepts                          ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.case-intro>                                 |   │
│ | H1: Women's health, with room for context.                       |   │
│ | Substrate: #151a18    | Ink: #fff       | Accent: #c9d1cc        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.case-context>    ) max-w: 1400px         |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Design scope and interactive |  | Try interactive prototype ↗  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 15px  ) | │
│ | [<header.skip-case>] -> [<section.case-intr] -> [<section.case-cont] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.case-context> ) | https://newminds.studio/concept-el │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.skip-case> — `newminds-studio_concept-elune`)**:
   - Landmark `<header class="skip-case">` hosting `ELUNE Women's Health App UX/UI Conce` navigation (`More concepts`), DOM attributes (`data-target="newminds-studio_concept-elune"`), and stylesheet rule `body { margin:0;background:151a18;font:16px Arial;color:fff }`.
2. **Hero Stage & Focal Lead (<section.case-intro> — `Women's health, with room for cont`)**:
   - Landmark `<section class="case-intro">` presenting display lead `Women's health, with room for context.` and copy excerpt *"Skip to case study"* over `#151a18` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.case-context> — `Design scope and interactive proto`)**:
   - Landmark `<section class="case-context">` rendering section `Design scope and interactive prototype` with copy *"Try interactive prototype ↗"*, asset references (`concept-elune`, `elune-case-01.jpg (ELUNE, a fictional women’s health mob...)`, `elune-case-02.jpg (Product framing, design objectives an...)`, `elune-case-03.jpg (Cycle overview, calendar with dashed...)`), and grid rule `main { max-width:1400px;margin:auto }`.
4. **Interactive Detail & Feature Matrix (<section.case-context> — `Try interactive prototype ↗`)**:
   - Landmark `<section class="case-context">` framing `Try interactive prototype ↗` and `ELUNE / MOBILE APP UX/UI DESIGN CONCEPT` (*"ELUNE / MOBILE APP UX/UI DESIGN CONCEPT"*) with `#d5fc65` surface cards, `#c9d1cc` accents, and `img { display:block;width:100%;height:auto }`.
5. **Colophon & Global Directory Footer (<footer.case-context> — `https://newminds.studio/concept-elune`)**:
   - Landmark `<footer class="case-context">` anchoring `ELUNE Women's Health App UX/UI C` footer links (`More concepts`), copy *"ELUNE is an independent women's health app design concept by"*, and `#a9b6ac` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: newminds-studio_concept-elune (ELUNE Women's Health App UX/UI Concept · New Minds)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `newminds-studio_concept-elune` (**ELUNE Women's Health App UX/UI Concept · New Minds** — `https://newminds.studio/concept-elune`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#151a18` canvas, `#fff` ink, `#c9d1cc` accent).
- **Identity & Domain Context**: Women's health app UX/UI concept by New Minds: cycle tracking, bloodwork records and a separate pregnancy journey. Explore the complete c...
- **Primary Substrate**: `#151a18` (`body { background: #151a18 }`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#c9d1cc`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#151a18` (`body { background: #151a18 }`) paired with `#fff` primary typography and `#c9d1cc` accents.
  - **Extracted Typographic Hierarchy**: Pairs `system-ui, -apple-system, sans-serif` (no custom `@font-face` extracted) for display copy (`Women's health, with room for contex`) with `system-ui, -apple-system, sans-serif` (no custom `@font-face` extracted) and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1400px` container bounds (`gap: 15px`, padding `24px`) with `cubic-bezier(0.25,0.1,0.25,1)` easing.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `newminds-studio_concept-elune` in your global stylesheet:

:root {
  /* ELUNE Women's Health App UX/UI Concept · New Minds (newminds-studio_concept-elune) — Ground-Truth Extracted CSS Variables */
  --newminds-studio--bg: #151a18; /* Canvas Substrate (from `body { background: #151a18 }`) (newminds-studio_concept-elune) */
  --newminds-studio--ink: #fff; /* Primary Typography Ink (stylesheet-derived) (newminds-studio_concept-elune) */
  --newminds-studio--surface: #d5fc65; /* Surface Substrate (stylesheet-derived) (newminds-studio_concept-elune) */
  --newminds-studio--accent: #c9d1cc; /* Interactive Accent (stylesheet-derived) (newminds-studio_concept-elune) */
  --newminds-studio--muted: #7e8c77; /* Secondary Ink (stylesheet-derived) (newminds-studio_concept-elune) */
  --newminds-studio--border: #a9b6ac; /* Structural Border (stylesheet-derived) (newminds-studio_concept-elune) */
  --newminds-studio--container: 1400px; /* Container Bound (stylesheet-derived) (newminds-studio_concept-elune) */
  --newminds-studio--gap: 15px; /* Grid Gutter (stylesheet-derived) (newminds-studio_concept-elune) */
  --newminds-studio--pad: 24px; /* Lateral Padding (stylesheet-derived) (newminds-studio_concept-elune) */
  --newminds-studio--ease: cubic-bezier(0.25,0.1,0.25,1); /* Primary Easing Function (newminds-studio_concept-elune) */
  --newminds-studio--radius: 7px; /* Corner Radius (stylesheet-derived) (newminds-studio_concept-elune) */
  --newminds-studio--fs-base: 11px; /* Observed Font Size Token (newminds-studio_concept-elune) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#151a18` — grounded in `body { background: #151a18 }`
- **Primary Typography Ink**: `#fff` — grounded in `body { color: #fff }`
- **Elevated Surface / Card Substrate**: `#d5fc65` — grounded in `a { color: #d5fc65 }`
- **Interactive Accent / Highlight**: `#c9d1cc` — grounded in `.case-context p { color: #c9d1cc }`
- **Secondary / Muted Copy**: `#7e8c77` — grounded in `.case-actions a { border: #7e8c77 }`
- **Structural Hairline Border**: `#a9b6ac` — grounded in `footer { color: #a9b6ac }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×11083px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1400px` extracted from `newminds-studio_concept-elune` stylesheet
- **Padding & Gutters**: `24px` lateral canvas padding with `15px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1400px`, `gap: 15px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `24px` horizontal padding
- **Media Queries**: `@media (max-width:600px)`
- **Corner Radii**: `7px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `system-ui, -apple-system, sans-serif` (no custom `@font-face` extracted)
- **Body Font Stack**: `system-ui, -apple-system, sans-serif` (no custom `@font-face` extracted)
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: rule `h1` (`font-size: clamp(38px,6vw,76px)`, `line-height: 1.06`, `letter-spacing: -.045em`, `font-weight: 500`)
- **H2 Section Rule**: rule `h2` (`font-size: clamp(26px,3.5vw,42px)`, `line-height: 1.15`, `letter-spacing: -.03em`, `font-weight: 500`)
- **Body Copy Rule**: rule `p` (`font-size: clamp(16px,1.7vw,20px)`, `line-height: 1.75`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `11px`, `clamp(38px,6vw,76px)`, `clamp(16px,1.7vw,20px)`, `14px`, `clamp(26px,3.5vw,42px)`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `newminds-studio_concept-elune` (`ELUNE Women's Health App UX/UI Concept · New Minds`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.skip-case> — `newminds-studio_concept-elune`)**:
   - DOM & Selectors: Landmark `<header class="skip-case">` hosting `ELUNE Women's Health App UX/UI Conce` navigation (`More concepts`), DOM attributes (`data-target="newminds-studio_concept-elune"`), and stylesheet rule `body { margin:0;background:151a18;font:16px Arial;color:fff }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.skip-case> — `newminds-studio_concept-elune`)` (`newminds-studio_concept-elune`) adapts across `@media (max-width:600px)` with `cubic-bezier(0.25,0.1,0.25,1)` transitions and links `More concepts`.
2. **Hero Stage & Focal Lead (<section.case-intro> — `Women's health, with room for cont`)**:
   - DOM & Selectors: Landmark `<section class="case-intro">` presenting display lead `Women's health, with room for context.` and copy excerpt *"Skip to case study"* over `#151a18` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×11083px` desktop / `390×2400px` mobile) sets `#151a18` background with `#fff` headline `Women's health, with room for context.`.
3. **Primary Showcase & Content Grid (<section.case-context> — `Design scope and interactive proto`)**:
   - DOM & Selectors: Landmark `<section class="case-context">` rendering section `Design scope and interactive prototype` with copy *"Try interactive prototype ↗"*, asset references (`concept-elune`, `elune-case-01.jpg (ELUNE, a fictional women’s health mob...)`, `elune-case-02.jpg (Product framing, design objectives an...)`, `elune-case-03.jpg (Cycle overview, calendar with dashed...)`), and grid rule `main { max-width:1400px;margin:auto }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.case-context> — `Design scope and interactive proto`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1400px`, `gap: 15px`) on desktop and Single-column vertical stack at `390px` viewport width with `24px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.case-context> — `Try interactive prototype ↗`)**:
   - DOM & Selectors: Landmark `<section class="case-context">` framing `Try interactive prototype ↗` and `ELUNE / MOBILE APP UX/UI DESIGN CONCEPT` (*"ELUNE / MOBILE APP UX/UI DESIGN CONCEPT"*) with `#d5fc65` surface cards, `#c9d1cc` accents, and `img { display:block;width:100%;height:auto }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.case-context> — `Try interactive prototype ↗`)` uses `7px` radii, `#c9d1cc` highlights, and assets (concept-elune, elune-case-01.jpg (ELUNE, a fictional women’s health mob...), elune-case-02.jpg (Product framing, design objectives an...)).
5. **Colophon & Global Directory Footer (<footer.case-context> — `https://newminds.studio/concept-elune`)**:
   - DOM & Selectors: Landmark `<footer class="case-context">` anchoring `ELUNE Women's Health App UX/UI C` footer links (`More concepts`), copy *"ELUNE is an independent women's health app design concept by"*, and `#a9b6ac` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.case-context> — `https://newminds.studio/concept-elune`)` aligns to `1400px` extracted from `newminds-studio_concept-elune` stylesheet with `24px` lateral canvas padding with `15px` grid gap and attributes (newminds-studio_concept-elune).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Skip to case study"*
- Copy Excerpt 2: *"Try interactive prototype ↗"*
- Copy Excerpt 3: *"ELUNE / MOBILE APP UX/UI DESIGN CONCEPT"*
- Copy Excerpt 4: *"ELUNE is an independent women's health app design concept by New Minds. It brings..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`
- **Extracted Stylesheet Rules (`newminds-studio_concept-elune`)**:
- `body { margin:0;background:151a18;font:16px Arial;color:fff }`
- `main { max-width:1400px;margin:auto }`
- `img { display:block;width:100%;height:auto }`
- `footer { padding:40px;line-height:1.7 }`
- `a:focus-visible { outline:2px solid white }`
- **Per-Selector Transition Rules**:
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in static CSS).
- **State & Hover Choreography**: Opacity and transform transitions on `<section.case-intro>` and `<section.case-context>` interactive targets.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `newminds-studio_concept-elune`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
