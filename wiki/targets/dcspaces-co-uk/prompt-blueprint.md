---
title: "UI Prompt Blueprint: dcspaces-co-uk"
date: 2026-11-15
target: "[[overview|dcspaces-co-uk]]"
status: analyzed
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#14161A` canvas, `#FFFFFF` ink, `#F2F1ED` accent)"
---

# UI Design System & Master Generation Blueprint: dcspaces-co-uk

> **Chorley Builders · Extensions & Renovations · DC Carpentry** (https://dcspaces.co.uk/) — Family-run builders in Chorley. House extensions, wall and chimney breast removals, kitchens and bespoke staircases across Lancashire. Fr...

![Desktop Viewport Capture (1440x11093)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Chorley Builders · Extensions & Renovations · DC Carpentry** (`https://dcspaces.co.uk/`). Family-run builders in Chorley. House extensions, wall and chimney breast removals, kitchens and bespoke staircases across Lancashire. Fr...
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#14161A` canvas, `#FFFFFF` ink, `#F2F1ED` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#14161A` (`var(--ink)` in `:root`) paired with `#FFFFFF` primary typography and `#F2F1ED` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Satoshi` for display copy (`Building & Renovation Specialists Ac`) with `Segoe UI` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `var(--max)` container bounds (`gap: 12px`, padding `var(--gut)`) with `cubic-bezier(.22,.61,.36,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×11093px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `var(--max)` extracted from `dcspaces-co-uk` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--gut)` lateral canvas padding with `12px` grid gap.
- **Border Radius Scale**: `999px`, `50%`, `8px`, `var(--r)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--max)`, `gap: 12px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--gut)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion: no-preference)`, `@media (prefers-reduced-motion: reduce)`, `@media (max-width: 1140px)`, `@media (max-width: 900px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#14161A` | `var(--ink)` in `:root` |
| **Primary Typography Ink** | `#4A5058` | `var(--ink-2)` in `:root` |
| **Elevated Surface / Card Substrate** | `#767D86` | `var(--ink-3)` in `:root` |
| **Interactive Accent / Highlight** | `#F2F1ED` | `var(--paper)` in `:root` |
| **Secondary / Muted Copy** | `#E8E6E0` | `var(--paper-2)` in `:root` |
| **Structural Hairline Border** | `#FFFFFF` | `var(--white)` in `:root` |
| **Variable Token (`--brand`)** | `#2e432f` | `var(--brand)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#14161A` | Typography Ink Token |
| `--ink-2` | `#4A5058` | Typography Ink Token |
| `--ink-3` | `#767D86` | Typography Ink Token |
| `--paper` | `#F2F1ED` | Canvas / Surface Token |
| `--paper-2` | `#E8E6E0` | Canvas / Surface Token |
| `--white` | `#FFFFFF` | Canvas / Surface Token |
| `--line` | `rgba(20,22,26,.09)` | Color / Atmospheric Token |
| `--line-2` | `rgba(20,22,26,.16)` | Color / Atmospheric Token |
| `--r-xl` | `32px` | Dimension / Scale Token |
| `--r-sm` | `16px` | Dimension / Scale Token |
| `--gut` | `24px` | Dimension / Scale Token |
| `--max` | `1340px` | Dimension / Scale Token |
| `--shadow` | `0 1px 2px rgba(20,22,26,.04), 0 10px 30px -14px rgba(20,22,26,.14)` | Elevation / Border Token |
| `--shadow-lg` | `0 2px 6px rgba(20,22,26,.05), 0 30px 70px -28px rgba(20,22,26,.30)` | Elevation / Border Token |
| `--ease` | `cubic-bezier(.22,.61,.36,1)` | Motion / Easing Token |
| `--brand` | `#2e432f` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Satoshi`.
- **Primary Body Stack**: `Segoe UI`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--cc-font-display: 'Satoshi', system-ui, sans-serif`; rule `h1` (`font-size: clamp(2.6rem, 5.6vw, 4.6rem)`, `line-height: 1`, `letter-spacing: -.045em`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(1.5rem, 2.4vw, 2.1rem)`).
- **Body Copy**: CSS variables `--cc-font-body: 'Satoshi', system-ui, sans-serif`; rule `body` (`font-size: 17px`, `line-height: 1.6`, `font-weight: 400`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `17px`, `.76rem`, `clamp(2.7rem, 6.4vw, 5rem)`, `clamp(2.1rem, 4.4vw, 3.5rem)`, `clamp(1.6rem, 2.6vw, 2.2rem)`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.22,.61,.36,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.btn`**: `transition: background .25s var(--ease), color .25s var(--ease), border-co...` extracted from `dcspaces-co-uk` stylesheet.
- **Selector `.btn__ico`**: `transition: background .25s var(--ease), transform .3s var(--ease)` extracted from `dcspaces-co-uk` stylesheet.
- **Selector `.tlink`**: `transition: gap .25s var(--ease)` extracted from `dcspaces-co-uk` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,.61,.36,1)`)**: Governs interactive state transitions across `<header.hdr>` and `<section.opening>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Chorley Builders · Extensions & Renovation │
│ ====================================================================== │
│ [ <header.hdr>             | Home · About · All services · Extensio ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero>                                       |   │
│ | H1: Building & Renovation Specialists Across Chorley...          |   │
│ | Substrate: #14161A    | Ink: #FFFFFF    | Accent: #F2F1ED        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.opening>         ) max-w: var(--max)     |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Everything your house needs, |  | Home Extensions              | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 12px  ) | │
│ | [<header.hdr>] -> [<section.hero>] -> [<section.opening>] |          │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.ftr>          ) | https://dcspaces.co.uk/            │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.hdr> — `dcspaces-co-uk`)**:
   - Landmark `<header class="hdr">` hosting `Chorley Builders · Extensions & Reno` navigation (`Home · About · All services · Extensions · Projects`), DOM attributes (`data-carousel`, `data-dir="prev"`, `data-dir="next"`, `data-dir="prev"`), and stylesheet rule `font-face { font-family: "Satoshi"; src: url("../fonts/satoshi-400.woff2") format("w... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Building & Renovation Specialists `)**:
   - Landmark `<section class="hero is-ready">` presenting display lead `Building & Renovation Specialists Across Chorley...` and copy excerpt *"Structural walls and chimney breasts"* over `#14161A` canvas and `#FFFFFF` ink.
3. **Primary Showcase & Content Grid (<section.opening> — `Everything your house needs, from `)**:
   - Landmark `<section class="opening">` rendering section `Everything your house needs, from one team` with copy *"Kitchen renovations and fitting"*, asset references (`favicon.png`, `apple-touch-icon.png`, `satoshi-900.woff2`, `satoshi-400.woff2`), and grid rule `after { box-sizing: border-box; }`.
4. **Interactive Detail & Feature Matrix (<section.section> — `Home Extensions`)**:
   - Landmark `<section class="section">` framing `Home Extensions` and `Loft Conversions` (*"Bespoke carpentry and staircases"*) with `#767D86` surface cards, `#F2F1ED` accents, and `html { -webkit-text-size-adjust: 100%; scroll-behavior: smooth; }`.
5. **Colophon & Global Directory Footer (<footer.ftr> — `https://dcspaces.co.uk/`)**:
   - Landmark `<footer class="ftr">` anchoring `Chorley Builders · Extensions & ` footer links (`Home · About · All services · Extensions · Projects`), copy *"Crafting unique spaces"*, and `#FFFFFF` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: dcspaces-co-uk (Chorley Builders · Extensions & Renovations · DC Carpentry)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `dcspaces-co-uk` (**Chorley Builders · Extensions & Renovations · DC Carpentry** — `https://dcspaces.co.uk/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#14161A` canvas, `#FFFFFF` ink, `#F2F1ED` accent).
- **Identity & Domain Context**: Family-run builders in Chorley. House extensions, wall and chimney breast removals, kitchens and bespoke staircases across Lancashire. Fr...
- **Primary Substrate**: `#14161A` (`var(--ink)` in `:root`), **Primary Ink**: `#FFFFFF`, **Accent / Highlight**: `#F2F1ED`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#14161A` (`var(--ink)` in `:root`) paired with `#FFFFFF` primary typography and `#F2F1ED` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Satoshi` for display copy (`Building & Renovation Specialists Ac`) with `Segoe UI` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `var(--max)` container bounds (`gap: 12px`, padding `var(--gut)`) with `cubic-bezier(.22,.61,.36,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `dcspaces-co-uk` in your global stylesheet:

:root {
  /* Chorley Builders · Extensions & Renovations · DC Carpentry (dcspaces-co-uk) — Ground-Truth Extracted CSS Variables */
  --ink: #14161A; /* Typography Ink Token (dcspaces-co-uk) */
  --ink-2: #4A5058; /* Typography Ink Token (dcspaces-co-uk) */
  --ink-3: #767D86; /* Typography Ink Token (dcspaces-co-uk) */
  --paper: #F2F1ED; /* Canvas / Surface Token (dcspaces-co-uk) */
  --paper-2: #E8E6E0; /* Canvas / Surface Token (dcspaces-co-uk) */
  --white: #FFFFFF; /* Canvas / Surface Token (dcspaces-co-uk) */
  --line: rgba(20,22,26,.09); /* Color / Atmospheric Token (dcspaces-co-uk) */
  --line-2: rgba(20,22,26,.16); /* Color / Atmospheric Token (dcspaces-co-uk) */
  --r-xl: 32px; /* Dimension / Scale Token (dcspaces-co-uk) */
  --r-sm: 16px; /* Dimension / Scale Token (dcspaces-co-uk) */
  --gut: 24px; /* Dimension / Scale Token (dcspaces-co-uk) */
  --max: 1340px; /* Dimension / Scale Token (dcspaces-co-uk) */
  --shadow: 0 1px 2px rgba(20,22,26,.04), 0 10px 30px -14px rgba(20,22,26,.14); /* Elevation / Border Token (dcspaces-co-uk) */
  --shadow-lg: 0 2px 6px rgba(20,22,26,.05), 0 30px 70px -28px rgba(20,22,26,.30); /* Elevation / Border Token (dcspaces-co-uk) */
  --ease: cubic-bezier(.22,.61,.36,1); /* Motion / Easing Token (dcspaces-co-uk) */
  --brand: #2e432f; /* Brand / Palette Token (dcspaces-co-uk) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#14161A` — grounded in `var(--ink)` in `:root`
- **Primary Typography Ink**: `#4A5058` — grounded in `var(--ink-2)` in `:root`
- **Elevated Surface / Card Substrate**: `#767D86` — grounded in `var(--ink-3)` in `:root`
- **Interactive Accent / Highlight**: `#F2F1ED` — grounded in `var(--paper)` in `:root`
- **Secondary / Muted Copy**: `#E8E6E0` — grounded in `var(--paper-2)` in `:root`
- **Structural Hairline Border**: `#FFFFFF` — grounded in `var(--white)` in `:root`
- **Variable Token (`--brand`)**: `#2e432f` — grounded in `var(--brand)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×11093px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `var(--max)` extracted from `dcspaces-co-uk` stylesheet
- **Padding & Gutters**: `var(--gut)` lateral canvas padding with `12px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--max)`, `gap: 12px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--gut)` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion: no-preference)`, `@media (prefers-reduced-motion: reduce)`, `@media (max-width: 1140px)`, `@media (max-width: 900px)`
- **Corner Radii**: `999px`, `50%`, `8px`, `var(--r)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Satoshi`
- **Body Font Stack**: `Segoe UI`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--cc-font-display: 'Satoshi', system-ui, sans-serif`; rule `h1` (`font-size: clamp(2.6rem, 5.6vw, 4.6rem)`, `line-height: 1`, `letter-spacing: -.045em`)
- **H2 Section Rule**: rule `h2` (`font-size: clamp(1.5rem, 2.4vw, 2.1rem)`)
- **Body Copy Rule**: CSS variables `--cc-font-body: 'Satoshi', system-ui, sans-serif`; rule `body` (`font-size: 17px`, `line-height: 1.6`, `font-weight: 400`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `17px`, `.76rem`, `clamp(2.7rem, 6.4vw, 5rem)`, `clamp(2.1rem, 4.4vw, 3.5rem)`, `clamp(1.6rem, 2.6vw, 2.2rem)`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `dcspaces-co-uk` (`Chorley Builders · Extensions & Renovations · DC Carpentry`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.hdr> — `dcspaces-co-uk`)**:
   - DOM & Selectors: Landmark `<header class="hdr">` hosting `Chorley Builders · Extensions & Reno` navigation (`Home · About · All services · Extensions · Projects`), DOM attributes (`data-carousel`, `data-dir="prev"`, `data-dir="next"`, `data-dir="prev"`), and stylesheet rule `font-face { font-family: "Satoshi"; src: url("../fonts/satoshi-400.woff2") format("w... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.hdr> — `dcspaces-co-uk`)` (`dcspaces-co-uk`) adapts across `@media (prefers-reduced-motion: no-preference)`, `@media (prefers-reduced-motion: reduce)`, `@media (max-width: 1140px)`, `@media (max-width: 900px)` with `cubic-bezier(.22,.61,.36,1)` transitions and links `Home · About · All services · Extensions · Projects`.
2. **Hero Stage & Focal Lead (<section.hero> — `Building & Renovation Specialists `)**:
   - DOM & Selectors: Landmark `<section class="hero is-ready">` presenting display lead `Building & Renovation Specialists Across Chorley...` and copy excerpt *"Structural walls and chimney breasts"* over `#14161A` canvas and `#FFFFFF` ink.
   - Responsive Contract: Hero stage (`1440×11093px` desktop / `390×2400px` mobile) sets `#14161A` background with `#FFFFFF` headline `Building & Renovation Specialists Across Chorley...`.
3. **Primary Showcase & Content Grid (<section.opening> — `Everything your house needs, from `)**:
   - DOM & Selectors: Landmark `<section class="opening">` rendering section `Everything your house needs, from one team` with copy *"Kitchen renovations and fitting"*, asset references (`favicon.png`, `apple-touch-icon.png`, `satoshi-900.woff2`, `satoshi-400.woff2`), and grid rule `after { box-sizing: border-box; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.opening> — `Everything your house needs, from `)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--max)`, `gap: 12px`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--gut)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.section> — `Home Extensions`)**:
   - DOM & Selectors: Landmark `<section class="section">` framing `Home Extensions` and `Loft Conversions` (*"Bespoke carpentry and staircases"*) with `#767D86` surface cards, `#F2F1ED` accents, and `html { -webkit-text-size-adjust: 100%; scroll-behavior: smooth; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.section> — `Home Extensions`)` uses `999px`, `50%`, `8px`, `var(--r)` radii, `#F2F1ED` highlights, and assets (favicon.png, apple-touch-icon.png, satoshi-900.woff2).
5. **Colophon & Global Directory Footer (<footer.ftr> — `https://dcspaces.co.uk/`)**:
   - DOM & Selectors: Landmark `<footer class="ftr">` anchoring `Chorley Builders · Extensions & ` footer links (`Home · About · All services · Extensions · Projects`), copy *"Crafting unique spaces"*, and `#FFFFFF` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.ftr> — `https://dcspaces.co.uk/`)` aligns to `var(--max)` extracted from `dcspaces-co-uk` stylesheet with `var(--gut)` lateral canvas padding with `12px` grid gap and attributes (data-carousel, data-dir="prev", data-dir="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Structural walls and chimney breasts"*
- Copy Excerpt 2: *"Kitchen renovations and fitting"*
- Copy Excerpt 3: *"Bespoke carpentry and staircases"*
- Copy Excerpt 4: *"Crafting unique spaces"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.22,.61,.36,1)`
- **Extracted Stylesheet Rules (`dcspaces-co-uk`)**:
- `font-face { font-family: "Satoshi"; src: url("../fonts/satoshi-400.woff2") format("w... }`
- `after { box-sizing: border-box; }`
- `html { -webkit-text-size-adjust: 100%; scroll-behavior: smooth; }`
- `video { display: block; max-width: 100%; height: auto; }`
- `button { font: inherit; }`
- **Per-Selector Transition Rules**:
- **Selector `.btn`**: `transition: background .25s var(--ease), color .25s var(--ease), border-co...` extracted from `dcspaces-co-uk` stylesheet.
- **Selector `.btn__ico`**: `transition: background .25s var(--ease), transform .3s var(--ease)` extracted from `dcspaces-co-uk` stylesheet.
- **Selector `.tlink`**: `transition: gap .25s var(--ease)` extracted from `dcspaces-co-uk` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,.61,.36,1)`)**: Governs interactive state transitions across `<header.hdr>` and `<section.opening>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `dcspaces-co-uk`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
