---
title: "UI Prompt Blueprint: constellations-icilalune-com"
date: 2026-11-15
target: "[[overview|constellations-icilalune-com]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#f3f2f2` canvas, `#201e1d` ink, `#ec3013` accent)"
---

# UI Design System & Master Generation Blueprint: constellations-icilalune-com

> **Constellation(s) — Immersive virtual 3D art exhibitions** (https://constellations.icilalune.com/) — Immersive virtual galleries: step into the worlds of AG Z, Palash Bag, Jonas Togo, Laura Meinhardt, François Glineur, Adam Krypel, Pia Be...

![Desktop Viewport Capture (1440x2963)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Constellation(s) — Immersive virtual 3D art exhibitions** (`https://constellations.icilalune.com/`). Immersive virtual galleries: step into the worlds of AG Z, Palash Bag, Jonas Togo, Laura Meinhardt, François Glineur, Adam Krypel, Pia Be...
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#f3f2f2` canvas, `#201e1d` ink, `#ec3013` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#f3f2f2` (`var(--color-bg)` in `:root`) paired with `#201e1d` primary typography and `#ec3013` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Archivo` for display copy (`Constellation(s)`) with `Arimo` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `60ch` container bounds (`gap: 6px`, padding `var(--space-2)`) with `cubic-bezier(0.25,0.1,0.25,1)` easing.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2963px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `60ch` extracted from `constellations-icilalune-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--space-2)` lateral canvas padding with `6px` grid gap.
- **Border Radius Scale**: `var(--radius-md)`, `50%`, `var(--radius-lg)`, `2px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 60ch`, `gap: 6px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--space-2)` horizontal padding.
- **Extracted CSS Media Queries**: no `@media` queries in static stylesheet (fluid viewport scaling).

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f3f2f2` | `var(--color-bg)` in `:root` |
| **Primary Typography Ink** | `#eae9e9` | `var(--color-surface)` in `:root` |
| **Elevated Surface / Card Substrate** | `#201e1d` | `var(--color-text)` in `:root` |
| **Interactive Accent / Highlight** | `#ec3013` | `var(--color-accent)` in `:root` |
| **Secondary / Muted Copy** | `#e15b47` | `var(--color-accent-2)` in `:root` |
| **Structural Hairline Border** | `#f8f4f4` | `var(--color-neutral-100)` in `:root` |
| **Variable Token (`--color-neutral-200`)** | `#eae7e7` | `var(--color-neutral-200)` in `:root` |
| **Variable Token (`--color-neutral-300`)** | `#d7d3d3` | `var(--color-neutral-300)` in `:root` |
| **Variable Token (`--color-neutral-400`)** | `#bab6b6` | `var(--color-neutral-400)` in `:root` |
| **Variable Token (`--color-neutral-500`)** | `#9b9797` | `var(--color-neutral-500)` in `:root` |
| **Variable Token (`--color-neutral-600`)** | `#7d7979` | `var(--color-neutral-600)` in `:root` |
| **Variable Token (`--color-neutral-700`)** | `#605d5d` | `var(--color-neutral-700)` in `:root` |
| **Variable Token (`--color-neutral-800`)** | `#444141` | `var(--color-neutral-800)` in `:root` |
| **Variable Token (`--color-neutral-900`)** | `#2d2b2b` | `var(--color-neutral-900)` in `:root` |
| **Variable Token (`--color-accent-100`)** | `#fff2ef` | `var(--color-accent-100)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-bg` | `#f3f2f2` | Canvas / Surface Token |
| `--color-surface` | `#eae9e9` | Canvas / Surface Token |
| `--color-text` | `#201e1d` | Typography Ink Token |
| `--color-accent` | `#ec3013` | Brand / Palette Token |
| `--color-accent-2` | `#e15b47` | Brand / Palette Token |
| `--color-divider` | `color-mix(in srgb, #201e1d 40%, transparent)` | Brand / Palette Token |
| `--color-neutral-100` | `#f8f4f4` | Brand / Palette Token |
| `--color-neutral-200` | `#eae7e7` | Brand / Palette Token |
| `--color-neutral-300` | `#d7d3d3` | Brand / Palette Token |
| `--color-neutral-400` | `#bab6b6` | Brand / Palette Token |
| `--color-neutral-500` | `#9b9797` | Brand / Palette Token |
| `--color-neutral-600` | `#7d7979` | Brand / Palette Token |
| `--color-neutral-700` | `#605d5d` | Brand / Palette Token |
| `--color-neutral-800` | `#444141` | Brand / Palette Token |
| `--color-neutral-900` | `#2d2b2b` | Brand / Palette Token |
| `--color-accent-100` | `#fff2ef` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Archivo`.
- **Primary Body Stack**: `Arimo`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 42px`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 32px`).
- **Body Copy**: CSS variables `--font-body: "Archivo", system-ui, sans-serif`; rule `body` (`font-size: 15px`, `line-height: 1.55`, `font-weight: 400`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `15px`, `42px`, `32px`, `25px`, `20px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `::after`**: `transition: 0s !important` extracted from `constellations-icilalune-com` stylesheet.
- **Selector `style]`**: `transition: unset` extracted from `constellations-icilalune-com` stylesheet.
- **Selector `style]`**: `transition: unset` extracted from `constellations-icilalune-com` stylesheet.
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in static CSS).
- **State & Hover Choreography**: Opacity and transform transitions on `<section.sc-interp>` and `<section.scp0>` interactive targets.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Constellation(s) — Immersive virtual 3D ar │
│ ====================================================================== │
│ [ <header.sc-host>         | Overview · Index · Archive · About · C ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.sc-interp>                                  |   │
│ | H1: Constellation(s)                                             |   │
│ | Substrate: #f3f2f2    | Ink: #201e1d    | Accent: #ec3013        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.scp0>            ) max-w: 60ch           |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Artists                      |  | Exhibit on Constellation(s)  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 6px   ) | │
│ | [<header.sc-host>] -> [<section.sc-interp] -> [<section.scp0>] |     │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.scp2>         ) | https://constellations.icilalune.c │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.sc-host> — `constellations-icilalune-com`)**:
   - Landmark `<header class="sc-host">` hosting `Constellation(s) — Immersive virtual` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-dc-tpl="1"`, `data-dc-tpl="2"`, `data-dc-tpl="3"`, `data-sc-name="Root"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;text-size-adjust:100% }`.
2. **Hero Stage & Focal Lead (<section.sc-interp> — `Constellation(s)`)**:
   - Landmark `<section class="sc-interp">` presenting display lead `Constellation(s)` and copy excerpt *"Immersive virtual galleries: step into the worlds of AG Z, Palash"* over `#f3f2f2` canvas and `#201e1d` ink.
3. **Primary Showcase & Content Grid (<section.scp0> — `Artists`)**:
   - Landmark `<section class="scp0">` rendering section `Artists` with copy *"AG Z — Ten Thousand Li · Travel and street photography, China"*, asset references (`manifest.webmanifest`, `favicon.svg`, `favicon-32.png`, `favicon-16.png`), and grid rule `body { background: var(--color-bg); color: var(--color-text); font-family: var(... }`.
4. **Interactive Detail & Feature Matrix (<section.scp1> — `Exhibit on Constellation(s)`)**:
   - Landmark `<section class="scp1">` framing `Exhibit on Constellation(s)` and `AG Z — Ten Thousand Li` (*"AG Z — Ten Thousand Li"*) with `#201e1d` surface cards, `#ec3013` accents, and `h4 { font-family: var(--font-heading); font-weight: var(--font-heading-weight); }`.
5. **Colophon & Global Directory Footer (<footer.scp2> — `https://constellations.icilalune.com/`)**:
   - Landmark `<footer class="scp2">` anchoring `Constellation(s) — Immersive vir` footer links (`Overview · Index · Archive · About · Contact`), copy *"Palash Bag — Still Water · Macro photography, India"*, and `#f8f4f4` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: constellations-icilalune-com (Constellation(s) — Immersive virtual 3D art exhibitions)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `constellations-icilalune-com` (**Constellation(s) — Immersive virtual 3D art exhibitions** — `https://constellations.icilalune.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#f3f2f2` canvas, `#201e1d` ink, `#ec3013` accent).
- **Identity & Domain Context**: Immersive virtual galleries: step into the worlds of AG Z, Palash Bag, Jonas Togo, Laura Meinhardt, François Glineur, Adam Krypel, Pia Be...
- **Primary Substrate**: `#f3f2f2` (`var(--color-bg)` in `:root`), **Primary Ink**: `#201e1d`, **Accent / Highlight**: `#ec3013`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#f3f2f2` (`var(--color-bg)` in `:root`) paired with `#201e1d` primary typography and `#ec3013` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Archivo` for display copy (`Constellation(s)`) with `Arimo` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `60ch` container bounds (`gap: 6px`, padding `var(--space-2)`) with `cubic-bezier(0.25,0.1,0.25,1)` easing.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `constellations-icilalune-com` in your global stylesheet:

:root {
  /* Constellation(s) — Immersive virtual 3D art exhibitions (constellations-icilalune-com) — Ground-Truth Extracted CSS Variables */
  --color-bg: #f3f2f2; /* Canvas / Surface Token (constellations-icilalune-com) */
  --color-surface: #eae9e9; /* Canvas / Surface Token (constellations-icilalune-com) */
  --color-text: #201e1d; /* Typography Ink Token (constellations-icilalune-com) */
  --color-accent: #ec3013; /* Brand / Palette Token (constellations-icilalune-com) */
  --color-accent-2: #e15b47; /* Brand / Palette Token (constellations-icilalune-com) */
  --color-divider: color-mix(in srgb, #201e1d 40%, transparent); /* Brand / Palette Token (constellations-icilalune-com) */
  --color-neutral-100: #f8f4f4; /* Brand / Palette Token (constellations-icilalune-com) */
  --color-neutral-200: #eae7e7; /* Brand / Palette Token (constellations-icilalune-com) */
  --color-neutral-300: #d7d3d3; /* Brand / Palette Token (constellations-icilalune-com) */
  --color-neutral-400: #bab6b6; /* Brand / Palette Token (constellations-icilalune-com) */
  --color-neutral-500: #9b9797; /* Brand / Palette Token (constellations-icilalune-com) */
  --color-neutral-600: #7d7979; /* Brand / Palette Token (constellations-icilalune-com) */
  --color-neutral-700: #605d5d; /* Brand / Palette Token (constellations-icilalune-com) */
  --color-neutral-800: #444141; /* Brand / Palette Token (constellations-icilalune-com) */
  --color-neutral-900: #2d2b2b; /* Brand / Palette Token (constellations-icilalune-com) */
  --color-accent-100: #fff2ef; /* Brand / Palette Token (constellations-icilalune-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f3f2f2` — grounded in `var(--color-bg)` in `:root`
- **Primary Typography Ink**: `#eae9e9` — grounded in `var(--color-surface)` in `:root`
- **Elevated Surface / Card Substrate**: `#201e1d` — grounded in `var(--color-text)` in `:root`
- **Interactive Accent / Highlight**: `#ec3013` — grounded in `var(--color-accent)` in `:root`
- **Secondary / Muted Copy**: `#e15b47` — grounded in `var(--color-accent-2)` in `:root`
- **Structural Hairline Border**: `#f8f4f4` — grounded in `var(--color-neutral-100)` in `:root`
- **Variable Token (`--color-neutral-200`)**: `#eae7e7` — grounded in `var(--color-neutral-200)` in `:root`
- **Variable Token (`--color-neutral-300`)**: `#d7d3d3` — grounded in `var(--color-neutral-300)` in `:root`
- **Variable Token (`--color-neutral-400`)**: `#bab6b6` — grounded in `var(--color-neutral-400)` in `:root`
- **Variable Token (`--color-neutral-500`)**: `#9b9797` — grounded in `var(--color-neutral-500)` in `:root`
- **Variable Token (`--color-neutral-600`)**: `#7d7979` — grounded in `var(--color-neutral-600)` in `:root`
- **Variable Token (`--color-neutral-700`)**: `#605d5d` — grounded in `var(--color-neutral-700)` in `:root`
- **Variable Token (`--color-neutral-800`)**: `#444141` — grounded in `var(--color-neutral-800)` in `:root`
- **Variable Token (`--color-neutral-900`)**: `#2d2b2b` — grounded in `var(--color-neutral-900)` in `:root`
- **Variable Token (`--color-accent-100`)**: `#fff2ef` — grounded in `var(--color-accent-100)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2963px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `60ch` extracted from `constellations-icilalune-com` stylesheet
- **Padding & Gutters**: `var(--space-2)` lateral canvas padding with `6px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 60ch`, `gap: 6px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--space-2)` horizontal padding
- **Media Queries**: no `@media` queries in static stylesheet (fluid viewport scaling)
- **Corner Radii**: `var(--radius-md)`, `50%`, `var(--radius-lg)`, `2px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Archivo`
- **Body Font Stack**: `Arimo`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: rule `h1` (`font-size: 42px`)
- **H2 Section Rule**: rule `h2` (`font-size: 32px`)
- **Body Copy Rule**: CSS variables `--font-body: "Archivo", system-ui, sans-serif`; rule `body` (`font-size: 15px`, `line-height: 1.55`, `font-weight: 400`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `15px`, `42px`, `32px`, `25px`, `20px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `constellations-icilalune-com` (`Constellation(s) — Immersive virtual 3D art exhibitions`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.sc-host> — `constellations-icilalune-com`)**:
   - DOM & Selectors: Landmark `<header class="sc-host">` hosting `Constellation(s) — Immersive virtual` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-dc-tpl="1"`, `data-dc-tpl="2"`, `data-dc-tpl="3"`, `data-sc-name="Root"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;text-size-adjust:100% }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.sc-host> — `constellations-icilalune-com`)` (`constellations-icilalune-com`) adapts across no `@media` queries in static stylesheet (fluid viewport scaling) with `cubic-bezier(0.25,0.1,0.25,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<section.sc-interp> — `Constellation(s)`)**:
   - DOM & Selectors: Landmark `<section class="sc-interp">` presenting display lead `Constellation(s)` and copy excerpt *"Immersive virtual galleries: step into the worlds of AG Z, Palash"* over `#f3f2f2` canvas and `#201e1d` ink.
   - Responsive Contract: Hero stage (`1440×2963px` desktop / `390×2400px` mobile) sets `#f3f2f2` background with `#201e1d` headline `Constellation(s)`.
3. **Primary Showcase & Content Grid (<section.scp0> — `Artists`)**:
   - DOM & Selectors: Landmark `<section class="scp0">` rendering section `Artists` with copy *"AG Z — Ten Thousand Li · Travel and street photography, China"*, asset references (`manifest.webmanifest`, `favicon.svg`, `favicon-32.png`, `favicon-16.png`), and grid rule `body { background: var(--color-bg); color: var(--color-text); font-family: var(... }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.scp0> — `Artists`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 60ch`, `gap: 6px`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--space-2)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.scp1> — `Exhibit on Constellation(s)`)**:
   - DOM & Selectors: Landmark `<section class="scp1">` framing `Exhibit on Constellation(s)` and `AG Z — Ten Thousand Li` (*"AG Z — Ten Thousand Li"*) with `#201e1d` surface cards, `#ec3013` accents, and `h4 { font-family: var(--font-heading); font-weight: var(--font-heading-weight); }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.scp1> — `Exhibit on Constellation(s)`)` uses `var(--radius-md)`, `50%`, `var(--radius-lg)`, `2px` radii, `#ec3013` highlights, and assets (manifest.webmanifest, favicon.svg, favicon-32.png).
5. **Colophon & Global Directory Footer (<footer.scp2> — `https://constellations.icilalune.com/`)**:
   - DOM & Selectors: Landmark `<footer class="scp2">` anchoring `Constellation(s) — Immersive vir` footer links (`Overview · Index · Archive · About · Contact`), copy *"Palash Bag — Still Water · Macro photography, India"*, and `#f8f4f4` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.scp2> — `https://constellations.icilalune.com/`)` aligns to `60ch` extracted from `constellations-icilalune-com` stylesheet with `var(--space-2)` lateral canvas padding with `6px` grid gap and attributes (data-dc-tpl="1", data-dc-tpl="2", data-dc-tpl="3").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Immersive virtual galleries: step into the worlds of AG Z, Palash Bag, Jonas Togo,..."*
- Copy Excerpt 2: *"AG Z — Ten Thousand Li · Travel and street photography, China"*
- Copy Excerpt 3: *"AG Z — Ten Thousand Li"*
- Copy Excerpt 4: *"Palash Bag — Still Water · Macro photography, India"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`
- **Extracted Stylesheet Rules (`constellations-icilalune-com`)**:
- `html { -webkit-text-size-adjust:100%;text-size-adjust:100% }`
- `body { background: var(--color-bg); color: var(--color-text); font-family: var(... }`
- `h4 { font-family: var(--font-heading); font-weight: var(--font-heading-weight); }`
- `.grayscale { filter:grayscale(1) contrast(1.08) }`
- `after { box-sizing: border-box; }`
- **Per-Selector Transition Rules**:
- **Selector `::after`**: `transition: 0s !important` extracted from `constellations-icilalune-com` stylesheet.
- **Selector `style]`**: `transition: unset` extracted from `constellations-icilalune-com` stylesheet.
- **Selector `style]`**: `transition: unset` extracted from `constellations-icilalune-com` stylesheet.
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in static CSS).
- **State & Hover Choreography**: Opacity and transform transitions on `<section.sc-interp>` and `<section.scp0>` interactive targets.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `constellations-icilalune-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
