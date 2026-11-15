---
title: "UI Prompt Blueprint: armor-bd-com"
date: 2026-11-15
target: "armor-bd-com"
status: analyzed
capture: specimen
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#faebe3`)"
---

# UI Design System & Master Generation Blueprint: armor-bd-com

> **Armor Bangladesh Limited — ATM, CRM & Banking Technology Solutions** (https://armor-bd.com) — Armor Bangladesh Limited provides banking hardware and software — cash recyclers, ATMs, kiosks, UPS, payment switching and card managemen...

![Desktop Design Specimen (Offline WebGL/JS Fallback — not live site capture)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Armor Bangladesh Limited — ATM, CRM & Banking Technology Solutions** (`https://armor-bd.com`). Armor Bangladesh Limited provides banking hardware and software — cash recyclers, ATMs, kiosks, UPS, payment switching and card managemen...
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#faebe3`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`var(--normal-bg)` in `:root`) paired with `#fff3` primary typography and `#faebe3` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Manrope` for display copy (`Pioneering Banking Technology Soluti`) with `Unbounded` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `640px` container bounds (`gap: .125rem`, padding `.375rem`) with `cubic-bezier(0,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Design Specimen (Offline WebGL/JS Fallback — not live site capture)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `640px` extracted from `armor-bd-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `.375rem` lateral canvas padding with `.125rem` grid gap.
- **Border Radius Scale**: `.3125rem`, `.375rem`, `.25rem`, `1rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 640px`, `gap: .125rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `.375rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width: 640px)`, `@media (min-width: 768px)`, `@media (min-width: 1024px)`, `@media (min-width: 1280px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--normal-bg)` in `:root` |
| **Primary Typography Ink** | `#e5e7eb` | `:after { border-color: #e5e7eb }` |
| **Elevated Surface / Card Substrate** | `#9ca3af` | `textarea::-moz-placeholder { color: #9ca3af }` |
| **Interactive Accent / Highlight** | `#faebe3` | `.prose-primary { color: #faebe3 }` |
| **Secondary / Muted Copy** | `#fff3` | `20 { border-color: #fff3 }` |
| **Structural Hairline Border** | `#fffc` | `80 { color: #fffc }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--toast-icon-margin-start` | `-3px` | Layout / Spatial Grid Token |
| `--toast-icon-margin-end` | `4px` | Layout / Spatial Grid Token |
| `--toast-svg-margin-start` | `-1px` | Layout / Spatial Grid Token |
| `--toast-svg-margin-end` | `0px` | Layout / Spatial Grid Token |
| `--toast-button-margin-start` | `auto` | Layout / Spatial Grid Token |
| `--toast-button-margin-end` | `0` | Layout / Spatial Grid Token |
| `--toast-close-button-start` | `0` | Design System Custom Token |
| `--toast-close-button-end` | `unset` | Design System Custom Token |
| `--toast-close-button-transform` | `translate(-35%, -35%)` | Dimension / Scale Token |
| `--gray1` | `hsl(0, 0%, 99%)` | Color / Atmospheric Token |
| `--gray2` | `hsl(0, 0%, 97.3%)` | Color / Atmospheric Token |
| `--gray3` | `hsl(0, 0%, 95.1%)` | Color / Atmospheric Token |
| `--gray4` | `hsl(0, 0%, 93%)` | Color / Atmospheric Token |
| `--gray5` | `hsl(0, 0%, 90.9%)` | Color / Atmospheric Token |
| `--gray6` | `hsl(0, 0%, 88.7%)` | Color / Atmospheric Token |
| `--gray7` | `hsl(0, 0%, 85.8%)` | Color / Atmospheric Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Manrope`.
- **Primary Body Stack**: `Unbounded`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`font-weight: 700`).
- **Section Heading (`H2`)**: rule `h2` (`font-weight: 700`).
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `1.25em`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `1.25em`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(0,0,.25,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.transition`**: `transition: cubic-bezier(0,0,.2,1)` extracted from `armor-bd-com` stylesheet.
- **Selector `filter\]`**: `transition: cubic-bezier(0,0,.2,1)` extracted from `armor-bd-com` stylesheet.
- **Selector `.transition-all`**: `transition: cubic-bezier(0,0,.2,1)` extracted from `armor-bd-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<nav.relative>` and `<section.relative>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Armor Bangladesh Limited — ATM, CRM & Bank │
│ ====================================================================== │
│ [ <nav.relative>           | Products · Why us · About · Career · C ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.lenis-smooth>                               |   │
│ | H1: Pioneering Banking Technology Solutions                      |   │
│ | Substrate: #fff       | Ink: #fff3      | Accent: #faebe3        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.relative>        ) max-w: 640px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | We are constantly introducin |  | 150+                         | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .125re) | │
│ | [<nav.relative>] -> [<section.lenis-smo] -> [<section.relative>] |   │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.w-full>       ) | https://armor-bd.com               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.relative> — `armor-bd-com`)**:
   - Landmark `<nav class="relative mx-auto">` hosting `Armor Bangladesh Limited — ATM, CRM ` navigation (`Products · Why us · About · Career · Contact`), DOM attributes (`data-discover="true"`, `data-discover="true"`, `data-discover="true"`, `data-discover="true"`), and stylesheet rule `after { box-sizing:border-box;border-width:0;border-style:solid;border-color:e5e7eb }`.
2. **Hero Stage & Focal Lead (<section.lenis-smooth> — `Pioneering Banking Technology Solu`)**:
   - Landmark `<section class="lenis-smooth">` presenting display lead `Pioneering Banking Technology Solutions` and copy excerpt *"Loading Armor experience"* over `#fff` canvas and `#fff3` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `We are constantly introducing new `)**:
   - Landmark `<section class="relative overflow-hidden">` rendering section `We are constantly introducing new products & solu...` with copy *"Technology Solutions"*, asset references (`favicon.ico`, `index-CjIBsQtn.js`, `index-BvNfHRqr.css`, `HomeV2-CKyWaDQ7.js`), and grid rule `body { margin:0;line-height:inherit }`.
4. **Interactive Detail & Feature Matrix (<section.py-6> — `150+`)**:
   - Landmark `<section class="py-6 overflow-hidden">` framing `150+` and `Everything you need to run modern banking` (*"Trusted nationwide"*) with `#9ca3af` surface cards, `#faebe3` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.w-full> — `https://armor-bd.com`)**:
   - Landmark `<footer class="w-full bg-primary">` anchoring `Armor Bangladesh Limited — ATM, ` footer links (`Products · Why us · About · Career · Contact`), copy *"At Armor, we empower financial institutions to reach new hei"*, and `#fffc` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: armor-bd-com (Armor Bangladesh Limited — ATM, CRM & Banking Technology Solutions)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `armor-bd-com` (**Armor Bangladesh Limited — ATM, CRM & Banking Technology Solutions** — `https://armor-bd.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#faebe3`).
- **Identity & Domain Context**: Armor Bangladesh Limited provides banking hardware and software — cash recyclers, ATMs, kiosks, UPS, payment switching and card managemen...
- **Primary Substrate**: `#fff` (`var(--normal-bg)` in `:root`), **Primary Ink**: `#fff3`, **Accent / Highlight**: `#faebe3`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`var(--normal-bg)` in `:root`) paired with `#fff3` primary typography and `#faebe3` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Manrope` for display copy (`Pioneering Banking Technology Soluti`) with `Unbounded` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `640px` container bounds (`gap: .125rem`, padding `.375rem`) with `cubic-bezier(0,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `armor-bd-com` in your global stylesheet:

:root {
  /* Armor Bangladesh Limited — ATM, CRM & Banking Technology Solutions (armor-bd-com) — Ground-Truth Extracted CSS Variables */
  --toast-icon-margin-start: -3px; /* Layout / Spatial Grid Token (armor-bd-com) */
  --toast-icon-margin-end: 4px; /* Layout / Spatial Grid Token (armor-bd-com) */
  --toast-svg-margin-start: -1px; /* Layout / Spatial Grid Token (armor-bd-com) */
  --toast-svg-margin-end: 0px; /* Layout / Spatial Grid Token (armor-bd-com) */
  --toast-button-margin-start: auto; /* Layout / Spatial Grid Token (armor-bd-com) */
  --toast-button-margin-end: 0; /* Layout / Spatial Grid Token (armor-bd-com) */
  --toast-close-button-start: 0; /* Design System Custom Token (armor-bd-com) */
  --toast-close-button-end: unset; /* Design System Custom Token (armor-bd-com) */
  --toast-close-button-transform: translate(-35%, -35%); /* Dimension / Scale Token (armor-bd-com) */
  --gray1: hsl(0, 0%, 99%); /* Color / Atmospheric Token (armor-bd-com) */
  --gray2: hsl(0, 0%, 97.3%); /* Color / Atmospheric Token (armor-bd-com) */
  --gray3: hsl(0, 0%, 95.1%); /* Color / Atmospheric Token (armor-bd-com) */
  --gray4: hsl(0, 0%, 93%); /* Color / Atmospheric Token (armor-bd-com) */
  --gray5: hsl(0, 0%, 90.9%); /* Color / Atmospheric Token (armor-bd-com) */
  --gray6: hsl(0, 0%, 88.7%); /* Color / Atmospheric Token (armor-bd-com) */
  --gray7: hsl(0, 0%, 85.8%); /* Color / Atmospheric Token (armor-bd-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fff` — grounded in `var(--normal-bg)` in `:root`
- **Primary Typography Ink**: `#e5e7eb` — grounded in `:after { border-color: #e5e7eb }`
- **Elevated Surface / Card Substrate**: `#9ca3af` — grounded in `textarea::-moz-placeholder { color: #9ca3af }`
- **Interactive Accent / Highlight**: `#faebe3` — grounded in `.prose-primary { color: #faebe3 }`
- **Secondary / Muted Copy**: `#fff3` — grounded in `20 { border-color: #fff3 }`
- **Structural Hairline Border**: `#fffc` — grounded in `80 { color: #fffc }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `640px` extracted from `armor-bd-com` stylesheet
- **Padding & Gutters**: `.375rem` lateral canvas padding with `.125rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 640px`, `gap: .125rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `.375rem` horizontal padding
- **Media Queries**: `@media (min-width: 640px)`, `@media (min-width: 768px)`, `@media (min-width: 1024px)`, `@media (min-width: 1280px)`
- **Corner Radii**: `.3125rem`, `.375rem`, `.25rem`, `1rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Manrope`
- **Body Font Stack**: `Unbounded`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: rule `h1` (`font-weight: 700`)
- **H2 Section Rule**: rule `h2` (`font-weight: 700`)
- **Body Copy Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `1.25em`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `1.25em`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `armor-bd-com` (`Armor Bangladesh Limited — ATM, CRM & Banking Technology Solutions`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.relative> — `armor-bd-com`)**:
   - DOM & Selectors: Landmark `<nav class="relative mx-auto">` hosting `Armor Bangladesh Limited — ATM, CRM ` navigation (`Products · Why us · About · Career · Contact`), DOM attributes (`data-discover="true"`, `data-discover="true"`, `data-discover="true"`, `data-discover="true"`), and stylesheet rule `after { box-sizing:border-box;border-width:0;border-style:solid;border-color:e5e7eb }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.relative> — `armor-bd-com`)` (`armor-bd-com`) adapts across `@media (min-width: 640px)`, `@media (min-width: 768px)`, `@media (min-width: 1024px)`, `@media (min-width: 1280px)` with `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(0,0,.25,1)` transitions and links `Products · Why us · About · Career · Contact`.
2. **Hero Stage & Focal Lead (<section.lenis-smooth> — `Pioneering Banking Technology Solu`)**:
   - DOM & Selectors: Landmark `<section class="lenis-smooth">` presenting display lead `Pioneering Banking Technology Solutions` and copy excerpt *"Loading Armor experience"* over `#fff` canvas and `#fff3` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#fff` background with `#fff3` headline `Pioneering Banking Technology Solutions`.
3. **Primary Showcase & Content Grid (<section.relative> — `We are constantly introducing new `)**:
   - DOM & Selectors: Landmark `<section class="relative overflow-hidden">` rendering section `We are constantly introducing new products & solu...` with copy *"Technology Solutions"*, asset references (`favicon.ico`, `index-CjIBsQtn.js`, `index-BvNfHRqr.css`, `HomeV2-CKyWaDQ7.js`), and grid rule `body { margin:0;line-height:inherit }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.relative> — `We are constantly introducing new `)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 640px`, `gap: .125rem`) on desktop and Single-column vertical stack at `390px` viewport width with `.375rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.py-6> — `150+`)**:
   - DOM & Selectors: Landmark `<section class="py-6 overflow-hidden">` framing `150+` and `Everything you need to run modern banking` (*"Trusted nationwide"*) with `#9ca3af` surface cards, `#faebe3` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.py-6> — `150+`)` uses `.3125rem`, `.375rem`, `.25rem`, `1rem` radii, `#faebe3` highlights, and assets (favicon.ico, index-CjIBsQtn.js, index-BvNfHRqr.css).
5. **Colophon & Global Directory Footer (<footer.w-full> — `https://armor-bd.com`)**:
   - DOM & Selectors: Landmark `<footer class="w-full bg-primary">` anchoring `Armor Bangladesh Limited — ATM, ` footer links (`Products · Why us · About · Career · Contact`), copy *"At Armor, we empower financial institutions to reach new hei"*, and `#fffc` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.w-full> — `https://armor-bd.com`)` aligns to `640px` extracted from `armor-bd-com` stylesheet with `.375rem` lateral canvas padding with `.125rem` grid gap and attributes (data-discover="true", data-discover="true", data-discover="true").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Loading Armor experience"*
- Copy Excerpt 2: *"Technology Solutions"*
- Copy Excerpt 3: *"Trusted nationwide"*
- Copy Excerpt 4: *"At Armor, we empower financial institutions to reach new heights — with secure tra..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(0,0,.25,1)`
- **Extracted Stylesheet Rules (`armor-bd-com`)**:
- `after { box-sizing:border-box;border-width:0;border-style:solid;border-color:e5e7eb }`
- `body { margin:0;line-height:inherit }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- `sup { font-size:75%;line-height:0;position:relative;vertical-align:baseline }`
- **Per-Selector Transition Rules**:
- **Selector `.transition`**: `transition: cubic-bezier(0,0,.2,1)` extracted from `armor-bd-com` stylesheet.
- **Selector `filter\]`**: `transition: cubic-bezier(0,0,.2,1)` extracted from `armor-bd-com` stylesheet.
- **Selector `.transition-all`**: `transition: cubic-bezier(0,0,.2,1)` extracted from `armor-bd-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<nav.relative>` and `<section.relative>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `armor-bd-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
