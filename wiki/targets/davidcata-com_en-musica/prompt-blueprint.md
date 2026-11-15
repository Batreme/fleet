---
title: "UI Prompt Blueprint: davidcata-com_en-musica"
date: 2026-11-15
target: "davidcata-com_en-musica"
status: analyzed
capture: dom
capture_desktop: dom
capture_mobile: dom
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#1f3a78` / `#EDE7DE`)"
---

# UI Design System & Master Generation Blueprint: davidcata-com_en-musica

> **Music — “Queridos todos:” and “Origen”, by David Catá** (https://davidcata.com/en/musica/) — The music of David Catá: his new album “Queridos todos:” (20 November 2026), pre-order signed and dedicated, and the instrumental album “...

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Music — “Queridos todos:” and “Origen”, by David Catá** (`https://davidcata.com/en/musica/`). The music of David Catá: his new album “Queridos todos:” (20 November 2026), pre-order signed and dedicated, and the instrumental album “...
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#1f3a78` / `#EDE7DE`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#1f3a78` (`var(--tinta-pluma)` in `:root`) paired with `#fff` primary typography and `#EDE7DE` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Caveat` for display copy (`Queridos todos:`) with `Caveat Fallback` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `42rem` container bounds (`gap: .125rem`, padding `1.5rem`) with `cubic-bezier(0,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×15917px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `42rem` extracted from `davidcata-com_en-musica` stylesheet.
- **Canvas Lateral Padding & Spacing**: `1.5rem` lateral canvas padding with `.125rem` grid gap.
- **Border Radius Scale**: `.25rem`, `1rem`, `14px`, `3px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 42rem`, `gap: .125rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `1.5rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (min-width:768px)`, `@media (max-width:767px)`, `@media (max-width:639px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#1f3a78` | `var(--tinta-pluma)` in `:root` |
| **Primary Typography Ink** | `#e5e7eb` | `:before { border: #e5e7eb }` |
| **Elevated Surface / Card Substrate** | `#9ca3af` | `textarea::-moz-placeholder { color: #9ca3af }` |
| **Interactive Accent / Highlight** | `#EDE7DE` | `.fill-hueso { fill: #EDE7DE }` |
| **Secondary / Muted Copy** | `#fff` | `.fill-white { fill: #fff }` |
| **Structural Hairline Border** | `#F2EEE7` | `html { background: #F2EEE7 }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--f-titular` | `"Fraunces",Georgia,serif` | Dimension / Scale Token |
| `--f-texto` | `"Karla",system-ui,sans-serif` | Typography Ink Token |
| `--papel` | `242 238 231` | Design System Custom Token |
| `--sala` | `10 9 8` | Design System Custom Token |
| `--hilo` | `158 43 37` | Design System Custom Token |
| `--renglon` | `2.25rem` | Dimension / Scale Token |
| `--tinta-pluma` | `#1f3a78` | Canvas / Surface Token |
| `--f-mano` | `"Caveat","Caveat Fallback"` | Design System Custom Token |
| `--marca` | `29, 185, 84` | Design System Custom Token |
| `--movil` | `0% 50%` | Dimension / Scale Token |
| `--pos` | `50% 50%` | Dimension / Scale Token |
| `--acento` | `204, 139, 61` | Design System Custom Token |
| `--tw-border-spacing-x` | `0` | Layout / Spatial Grid Token |
| `--tw-border-spacing-y` | `0` | Layout / Spatial Grid Token |
| `--davidcata-com-en-bg` | `#1f3a78` | Canvas Substrate (from `var(--tinta-pluma)` in `:root`) |
| `--davidcata-com-en-ink` | `#fff` | Primary Typography Ink (stylesheet-derived) |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Caveat`.
- **Primary Body Stack**: `Caveat Fallback`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `1.5rem`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 1.55rem`, `line-height: 1.15`, `letter-spacing: -.02em`).
- **Body Copy**: rule `p` (`font-size: 15px`, `line-height: 1.75`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `1.5rem`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.transition`**: `transition: cubic-bezier(0,0,.2,1)` extracted from `davidcata-com_en-musica` stylesheet.
- **Selector `ansition-\[opacity\2c filter\2c t...`**: `transition: cubic-bezier(0,0,.2,1)` extracted from `davidcata-com_en-musica` stylesheet.
- **Selector `ansition-\[opacity\2c transform\2...`**: `transition: cubic-bezier(0,0,.2,1)` extracted from `davidcata-com_en-musica` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.mundo-calido>` and `<section.relative>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Music — “Queridos todos:” and “Origen”, by │
│ ====================================================================== │
│ [ <header.mundo-calido>    | In cinemas · Albums ▾ · Origen Album · ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.relative>                                   |   │
│ | H1: Queridos todos:                                              |   │
│ | Substrate: #1f3a78    | Ink: #fff       | Accent: #EDE7DE        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.relative>        ) max-w: 42rem          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | His theme in “Arriba Tutto”  |  | Three ways to experience it  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .125re) | │
│ | [<header.mundo-cali] -> [<section.relative>] -> [<section.relative>] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.border-t>     ) | https://davidcata.com/en/musica/   │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.mundo-calido> — `davidcata-com_en-musica`)**:
   - Landmark `<header class="mundo-calido mundo-musica">` hosting `Music — “Queridos todos:” and “Orige` navigation (`In cinemas · Albums ▾ · Origen Album · 2023 · Listen · Concerts`), DOM attributes (`data-mundo="sala"`, `data-hero="oscuro"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid e5e7eb }`.
2. **Hero Stage & Focal Lead (<section.relative> — `Queridos todos:`)**:
   - Landmark `<section class="relative flex">` presenting display lead `Queridos todos:` and copy excerpt *"Queridos todos: New album · 20.11.2026"* over `#1f3a78` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `His theme in “Arriba Tutto”`)**:
   - Landmark `<section class="relative overflow-clip">` rendering section `His theme in “Arriba Tutto”` with copy *"New album · 20.11.2026"*, asset references (`cd-queridos-limpio-240.webp`, `portada-240.webp`, `amazonmusic.png`, `07c1226183551f0e.css`), and grid rule `body { margin:0;line-height:inherit }`.
4. **Interactive Detail & Feature Matrix (<section.border-t> — `Three ways to experience it`)**:
   - Landmark `<section class="border-t py-20">` framing `Three ways to experience it` and `Two albums. One memory.` (*"Origen Album · 2023"*) with `#9ca3af` surface cards, `#EDE7DE` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.border-t> — `https://davidcata.com/en/musica/`)**:
   - Landmark `<footer class="border-t bg-papel">` anchoring `Music — “Queridos todos:” and “O` footer links (`In cinemas · Albums ▾ · Origen Album · 2023 · Listen · Concerts`), copy *"Pre-order signed · € 20"*, and `#F2EEE7` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: davidcata-com_en-musica (Music — “Queridos todos:” and “Origen”, by David Catá)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `davidcata-com_en-musica` (**Music — “Queridos todos:” and “Origen”, by David Catá** — `https://davidcata.com/en/musica/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#1f3a78` / `#EDE7DE`).
- **Identity & Domain Context**: The music of David Catá: his new album “Queridos todos:” (20 November 2026), pre-order signed and dedicated, and the instrumental album “...
- **Primary Substrate**: `#1f3a78` (`var(--tinta-pluma)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#EDE7DE`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#1f3a78` (`var(--tinta-pluma)` in `:root`) paired with `#fff` primary typography and `#EDE7DE` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Caveat` for display copy (`Queridos todos:`) with `Caveat Fallback` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `42rem` container bounds (`gap: .125rem`, padding `1.5rem`) with `cubic-bezier(0,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `davidcata-com_en-musica` in your global stylesheet:

:root {
  /* Music — “Queridos todos:” and “Origen”, by David Catá (davidcata-com_en-musica) — Ground-Truth Extracted CSS Variables */
  --f-titular: "Fraunces",Georgia,serif; /* Dimension / Scale Token (davidcata-com_en-musica) */
  --f-texto: "Karla",system-ui,sans-serif; /* Typography Ink Token (davidcata-com_en-musica) */
  --papel: 242 238 231; /* Design System Custom Token (davidcata-com_en-musica) */
  --sala: 10 9 8; /* Design System Custom Token (davidcata-com_en-musica) */
  --hilo: 158 43 37; /* Design System Custom Token (davidcata-com_en-musica) */
  --renglon: 2.25rem; /* Dimension / Scale Token (davidcata-com_en-musica) */
  --tinta-pluma: #1f3a78; /* Canvas / Surface Token (davidcata-com_en-musica) */
  --f-mano: "Caveat","Caveat Fallback"; /* Design System Custom Token (davidcata-com_en-musica) */
  --marca: 29, 185, 84; /* Design System Custom Token (davidcata-com_en-musica) */
  --movil: 0% 50%; /* Dimension / Scale Token (davidcata-com_en-musica) */
  --pos: 50% 50%; /* Dimension / Scale Token (davidcata-com_en-musica) */
  --acento: 204, 139, 61; /* Design System Custom Token (davidcata-com_en-musica) */
  --tw-border-spacing-x: 0; /* Layout / Spatial Grid Token (davidcata-com_en-musica) */
  --tw-border-spacing-y: 0; /* Layout / Spatial Grid Token (davidcata-com_en-musica) */
  --davidcata-com-en-bg: #1f3a78; /* Canvas Substrate (from `var(--tinta-pluma)` in `:root`) (davidcata-com_en-musica) */
  --davidcata-com-en-ink: #fff; /* Primary Typography Ink (stylesheet-derived) (davidcata-com_en-musica) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#1f3a78` — grounded in `var(--tinta-pluma)` in `:root`
- **Primary Typography Ink**: `#e5e7eb` — grounded in `:before { border: #e5e7eb }`
- **Elevated Surface / Card Substrate**: `#9ca3af` — grounded in `textarea::-moz-placeholder { color: #9ca3af }`
- **Interactive Accent / Highlight**: `#EDE7DE` — grounded in `.fill-hueso { fill: #EDE7DE }`
- **Secondary / Muted Copy**: `#fff` — grounded in `.fill-white { fill: #fff }`
- **Structural Hairline Border**: `#F2EEE7` — grounded in `html { background: #F2EEE7 }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×15917px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `42rem` extracted from `davidcata-com_en-musica` stylesheet
- **Padding & Gutters**: `1.5rem` lateral canvas padding with `.125rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 42rem`, `gap: .125rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `1.5rem` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (min-width:768px)`, `@media (max-width:767px)`, `@media (max-width:639px)`
- **Corner Radii**: `.25rem`, `1rem`, `14px`, `3px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Caveat`
- **Body Font Stack**: `Caveat Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `1.5rem`)
- **H2 Section Rule**: rule `h2` (`font-size: 1.55rem`, `line-height: 1.15`, `letter-spacing: -.02em`)
- **Body Copy Rule**: rule `p` (`font-size: 15px`, `line-height: 1.75`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `1.5rem`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `davidcata-com_en-musica` (`Music — “Queridos todos:” and “Origen”, by David Catá`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.mundo-calido> — `davidcata-com_en-musica`)**:
   - DOM & Selectors: Landmark `<header class="mundo-calido mundo-musica">` hosting `Music — “Queridos todos:” and “Orige` navigation (`In cinemas · Albums ▾ · Origen Album · 2023 · Listen · Concerts`), DOM attributes (`data-mundo="sala"`, `data-hero="oscuro"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid e5e7eb }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.mundo-calido> — `davidcata-com_en-musica`)` (`davidcata-com_en-musica`) adapts across `@media (prefers-reduced-motion:reduce)`, `@media (min-width:768px)`, `@media (max-width:767px)`, `@media (max-width:639px)` with `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `In cinemas · Albums ▾ · Origen Album · 2023 · Listen · Concerts`.
2. **Hero Stage & Focal Lead (<section.relative> — `Queridos todos:`)**:
   - DOM & Selectors: Landmark `<section class="relative flex">` presenting display lead `Queridos todos:` and copy excerpt *"Queridos todos: New album · 20.11.2026"* over `#1f3a78` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×15917px` desktop / `390×2400px` mobile) sets `#1f3a78` background with `#fff` headline `Queridos todos:`.
3. **Primary Showcase & Content Grid (<section.relative> — `His theme in “Arriba Tutto”`)**:
   - DOM & Selectors: Landmark `<section class="relative overflow-clip">` rendering section `His theme in “Arriba Tutto”` with copy *"New album · 20.11.2026"*, asset references (`cd-queridos-limpio-240.webp`, `portada-240.webp`, `amazonmusic.png`, `07c1226183551f0e.css`), and grid rule `body { margin:0;line-height:inherit }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.relative> — `His theme in “Arriba Tutto”`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 42rem`, `gap: .125rem`) on desktop and Single-column vertical stack at `390px` viewport width with `1.5rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.border-t> — `Three ways to experience it`)**:
   - DOM & Selectors: Landmark `<section class="border-t py-20">` framing `Three ways to experience it` and `Two albums. One memory.` (*"Origen Album · 2023"*) with `#9ca3af` surface cards, `#EDE7DE` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.border-t> — `Three ways to experience it`)` uses `.25rem`, `1rem`, `14px`, `3px` radii, `#EDE7DE` highlights, and assets (cd-queridos-limpio-240.webp, portada-240.webp, amazonmusic.png).
5. **Colophon & Global Directory Footer (<footer.border-t> — `https://davidcata.com/en/musica/`)**:
   - DOM & Selectors: Landmark `<footer class="border-t bg-papel">` anchoring `Music — “Queridos todos:” and “O` footer links (`In cinemas · Albums ▾ · Origen Album · 2023 · Listen · Concerts`), copy *"Pre-order signed · € 20"*, and `#F2EEE7` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.border-t> — `https://davidcata.com/en/musica/`)` aligns to `42rem` extracted from `davidcata-com_en-musica` stylesheet with `1.5rem` lateral canvas padding with `.125rem` grid gap and attributes (data-mundo="sala", data-hero="oscuro", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Queridos todos: New album · 20.11.2026"*
- Copy Excerpt 2: *"New album · 20.11.2026"*
- Copy Excerpt 3: *"Origen Album · 2023"*
- Copy Excerpt 4: *"Pre-order signed · € 20"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`davidcata-com_en-musica`)**:
- `before { box-sizing:border-box;border:0 solid e5e7eb }`
- `body { margin:0;line-height:inherit }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- `sup { font-size:75%;line-height:0;position:relative;vertical-align:baseline }`
- **Per-Selector Transition Rules**:
- **Selector `.transition`**: `transition: cubic-bezier(0,0,.2,1)` extracted from `davidcata-com_en-musica` stylesheet.
- **Selector `ansition-\[opacity\2c filter\2c t...`**: `transition: cubic-bezier(0,0,.2,1)` extracted from `davidcata-com_en-musica` stylesheet.
- **Selector `ansition-\[opacity\2c transform\2...`**: `transition: cubic-bezier(0,0,.2,1)` extracted from `davidcata-com_en-musica` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.mundo-calido>` and `<section.relative>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `davidcata-com_en-musica`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
