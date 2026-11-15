---
title: "UI Prompt Blueprint: atmos-gallery"
date: 2026-11-15
target: "[[overview|atmos-gallery]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#f5f5f3` / `#1a1a1a`)"
---

# UI Design System & Master Generation Blueprint: atmos-gallery

> **Atmos Gallery · Image Colour Palette Generator** (https://atmos.gallery) — Atmos Gallery extracts five colours from an image, checks WCAG contrast and exports palettes for Figma, CSS, Tailwind, design tokens and...

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/atmos-gallery/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Atmos Gallery · Image Colour Palette Generator** (`https://atmos.gallery`). Atmos Gallery extracts five colours from an image, checks WCAG contrast and exports palettes for Figma, CSS, Tailwind, design tokens and...
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#f5f5f3` / `#1a1a1a`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#f5f5f3` (`var(--surface)` in `:root`) paired with `#1a1a1a` primary typography and `#1a1a1a` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Neue Montreal` for display copy (`Colour Read from Light and Atmospher`) with `clamp(1.5rem` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `24ch` container bounds (`gap: 40px`, padding `44px`) with `cubic-bezier(.22,1,.36,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/atmos-gallery/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `24ch` extracted from `atmos-gallery` stylesheet.
- **Canvas Lateral Padding & Spacing**: `44px` lateral canvas padding with `40px` grid gap.
- **Border Radius Scale**: `var(--radius-pill)`, `var(--radius-card)`, `var(--button-border-radius)`, `var(--radius-tick)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 24ch`, `gap: 40px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `44px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (hover:hover) and (prefers-reduced-motion:no-preference)`, `@media screen and (width<=700px)`, `@media (prefers-reduced-motion:reduce)`, `@media screen and (width<=720px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f5f5f3` | `var(--surface)` in `:root` |
| **Primary Typography Ink** | `#fafaf8` | `var(--surface-raised)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff` | `var(--surface-white)` in `:root` |
| **Interactive Accent / Highlight** | `#1a1a1a` | `var(--on-surface)` in `:root` |
| **Secondary / Muted Copy** | `#c8322a` | `var(--danger)` in `:root` |
| **Structural Hairline Border** | `#ff6e62` | `var(--danger-inverse)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ease-standard` | `cubic-bezier(.22,1,.36,1)` | Motion / Easing Token |
| `--ease-entrance` | `cubic-bezier(.16,1,.3,1)` | Motion / Easing Token |
| `--ease-exit` | `cubic-bezier(.4,0,1,1)` | Motion / Easing Token |
| `--ease-button-hover` | `cubic-bezier(.675,.15,.1,1)` | Motion / Easing Token |
| `--ease-button-click` | `cubic-bezier(.4,0,.2,1)` | Motion / Easing Token |
| `--ease-button-focus` | `cubic-bezier(.32,.72,0,1)` | Motion / Easing Token |
| `--ease-fold` | `cubic-bezier(.625,.05,0,1)` | Motion / Easing Token |
| `--ease-overlay` | `cubic-bezier(.19,1,.22,1)` | Motion / Easing Token |
| `--ease-progress` | `cubic-bezier(.33,1,.68,1)` | Motion / Easing Token |
| `--ease-ambient` | `cubic-bezier(.42,0,.58,1)` | Motion / Easing Token |
| `--ease-flow-fade` | `cubic-bezier(.33,.67,.67,1)` | Motion / Easing Token |
| `--logo-w` | `136.5px` | Dimension / Scale Token |
| `--logo-h` | `26px` | Dimension / Scale Token |
| `--dur-micro` | `.12s` | Motion / Timing Token |
| `--dur-fast` | `.18s` | Motion / Timing Token |
| `--dur-state` | `.24s` | Motion / Timing Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Neue Montreal`.
- **Primary Body Stack**: `clamp(1.5rem`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: 2.5rem`, `--text-5xl: 3rem`; rule `h1` (`font-size: var(--text-story)`, `line-height: var(--text-story--lin...`, `letter-spacing: var(--track-statement)`, `font-weight: 500`).
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: 2rem`; rule `h2` (`font-size: var(--text-doc-heading)`, `line-height: var(--text-doc-headin...`, `letter-spacing: var(--track-statement)`, `font-weight: 500`).
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: 1.5rem`, `--track-body: 0px`; rule `p` (`font-size: var(--text-base)`, `line-height: var(--text-base--line...`, `letter-spacing: var(--track-body)`).
- **Metadata & Navigation Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: 1rem`, `--text-sm: .875rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.4,0,1,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.land-legal .site-foot__consent`**: `transition: color var(--dur-chrome) var(--ease-button-hover)` extracted from `atmos-gallery` stylesheet.
- **Selector `media (prefers-reduced-motion:red...`**: `transition: .001ms!important` extracted from `atmos-gallery` stylesheet.
- **Selector `data-logo-ring]`**: `transition: opacity var(--dur-fast) var(--ease-standard)` extracted from `atmos-gallery` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,1,.36,1)`)**: Governs interactive state transitions across `<header.glass-bar>` and `<section.boot-inner>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Atmos Gallery · Image Colour Palette Gener │
│ ====================================================================== │
│ [ <header.glass-bar>       | Privacy Privacy · Terms Terms          ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.lenis-stopped>                              |   │
│ | H1: Colour Read from Light and Atmosphere. In Seconds.           |   │
│ | Substrate: #f5f5f3    | Ink: #1a1a1a    | Accent: #1a1a1a        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.boot-inner>      ) max-w: 24ch           |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Library                      |  | Start here                   | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 40px  ) | │
│ | [<header.glass-bar>] -> [<section.lenis-sto] -> [<section.boot-inne] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-foot>    ) | https://atmos.gallery              │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.glass-bar> — `atmos-gallery`)**:
   - Landmark `<header class="glass-bar">` hosting `Atmos Gallery · Image Colour Palette` navigation (`Privacy Privacy · Terms Terms`), DOM attributes (`data-landing-cover`, `data-theme="light"`, `data-bytes="23488"`, `data-bytes="24820"`), and stylesheet rule `.site-foot { padding:0 var(--page-gutter,24px) }`.
2. **Hero Stage & Focal Lead (<section.lenis-stopped> — `Colour Read from Light and Atmosph`)**:
   - Landmark `<section class="lenis-stopped">` presenting display lead `Colour Read from Light and Atmosphere. In Seconds.` and copy excerpt *"Skip to Main Content"* over `#f5f5f3` canvas and `#1a1a1a` ink.
3. **Primary Showcase & Content Grid (<section.boot-inner> — `Library`)**:
   - Landmark `<section class="boot-inner">` rendering section `Library` with copy *"Colour Read from Light and Atmosphere."*, asset references (`atmos-gallery-fav.png`, `NeueMontreal-Regular.woff2`, `NeueMontreal-Medium.woff2`, `gsap.min.js`), and grid rule `.site-foot__brand { padding:44px 0 24px }`.
4. **Interactive Detail & Feature Matrix (<section.boot-row> — `Start here`)**:
   - Landmark `<section class="boot-row">` framing `Start here` and `Atmos Gallery` (*"How it Works How it Works"*) with `#fff` surface cards, `#1a1a1a` accents, and `.site-foot__brand a { line-height:0;text-decoration:none;display:block }`.
5. **Colophon & Global Directory Footer (<footer.site-foot> — `https://atmos.gallery`)**:
   - Landmark `<footer class="site-foot">` anchoring `Atmos Gallery · Image Colour Pal` footer links (`Privacy Privacy · Terms Terms`), copy *"Privacy Settings Privacy Settings"*, and `#ff6e62` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: atmos-gallery (Atmos Gallery · Image Colour Palette Generator)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `atmos-gallery` (**Atmos Gallery · Image Colour Palette Generator** — `https://atmos.gallery`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f5f5f3` / `#1a1a1a`).
- **Identity & Domain Context**: Atmos Gallery extracts five colours from an image, checks WCAG contrast and exports palettes for Figma, CSS, Tailwind, design tokens and...
- **Primary Substrate**: `#f5f5f3` (`var(--surface)` in `:root`), **Primary Ink**: `#1a1a1a`, **Accent / Highlight**: `#1a1a1a`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#f5f5f3` (`var(--surface)` in `:root`) paired with `#1a1a1a` primary typography and `#1a1a1a` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Neue Montreal` for display copy (`Colour Read from Light and Atmospher`) with `clamp(1.5rem` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `24ch` container bounds (`gap: 40px`, padding `44px`) with `cubic-bezier(.22,1,.36,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `atmos-gallery` in your global stylesheet:

:root {
  /* Atmos Gallery · Image Colour Palette Generator (atmos-gallery) — Ground-Truth Extracted CSS Variables */
  --ease-standard: cubic-bezier(.22,1,.36,1); /* Motion / Easing Token (atmos-gallery) */
  --ease-entrance: cubic-bezier(.16,1,.3,1); /* Motion / Easing Token (atmos-gallery) */
  --ease-exit: cubic-bezier(.4,0,1,1); /* Motion / Easing Token (atmos-gallery) */
  --ease-button-hover: cubic-bezier(.675,.15,.1,1); /* Motion / Easing Token (atmos-gallery) */
  --ease-button-click: cubic-bezier(.4,0,.2,1); /* Motion / Easing Token (atmos-gallery) */
  --ease-button-focus: cubic-bezier(.32,.72,0,1); /* Motion / Easing Token (atmos-gallery) */
  --ease-fold: cubic-bezier(.625,.05,0,1); /* Motion / Easing Token (atmos-gallery) */
  --ease-overlay: cubic-bezier(.19,1,.22,1); /* Motion / Easing Token (atmos-gallery) */
  --ease-progress: cubic-bezier(.33,1,.68,1); /* Motion / Easing Token (atmos-gallery) */
  --ease-ambient: cubic-bezier(.42,0,.58,1); /* Motion / Easing Token (atmos-gallery) */
  --ease-flow-fade: cubic-bezier(.33,.67,.67,1); /* Motion / Easing Token (atmos-gallery) */
  --logo-w: 136.5px; /* Dimension / Scale Token (atmos-gallery) */
  --logo-h: 26px; /* Dimension / Scale Token (atmos-gallery) */
  --dur-micro: .12s; /* Motion / Timing Token (atmos-gallery) */
  --dur-fast: .18s; /* Motion / Timing Token (atmos-gallery) */
  --dur-state: .24s; /* Motion / Timing Token (atmos-gallery) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f5f5f3` — grounded in `var(--surface)` in `:root`
- **Primary Typography Ink**: `#fafaf8` — grounded in `var(--surface-raised)` in `:root`
- **Elevated Surface / Card Substrate**: `#fff` — grounded in `var(--surface-white)` in `:root`
- **Interactive Accent / Highlight**: `#1a1a1a` — grounded in `var(--on-surface)` in `:root`
- **Secondary / Muted Copy**: `#c8322a` — grounded in `var(--danger)` in `:root`
- **Structural Hairline Border**: `#ff6e62` — grounded in `var(--danger-inverse)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `24ch` extracted from `atmos-gallery` stylesheet
- **Padding & Gutters**: `44px` lateral canvas padding with `40px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 24ch`, `gap: 40px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `44px` horizontal padding
- **Media Queries**: `@media (hover:hover) and (prefers-reduced-motion:no-preference)`, `@media screen and (width<=700px)`, `@media (prefers-reduced-motion:reduce)`, `@media screen and (width<=720px)`
- **Corner Radii**: `var(--radius-pill)`, `var(--radius-card)`, `var(--button-border-radius)`, `var(--radius-tick)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Neue Montreal`
- **Body Font Stack**: `clamp(1.5rem`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: 2.5rem`, `--text-5xl: 3rem`; rule `h1` (`font-size: var(--text-story)`, `line-height: var(--text-story--lin...`, `letter-spacing: var(--track-statement)`, `font-weight: 500`)
- **H2 Section Rule**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: 2rem`; rule `h2` (`font-size: var(--text-doc-heading)`, `line-height: var(--text-doc-headin...`, `letter-spacing: var(--track-statement)`, `font-weight: 500`)
- **Body Copy Rule**: CSS variables `--text-base: 1rem`, `--text-base--line-height: 1.5rem`, `--track-body: 0px`; rule `p` (`font-size: var(--text-base)`, `line-height: var(--text-base--line...`, `letter-spacing: var(--track-body)`)
- **Metadata & Index Rule**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: 1rem`, `--text-sm: .875rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `atmos-gallery` (`Atmos Gallery · Image Colour Palette Generator`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.glass-bar> — `atmos-gallery`)**:
   - DOM & Selectors: Landmark `<header class="glass-bar">` hosting `Atmos Gallery · Image Colour Palette` navigation (`Privacy Privacy · Terms Terms`), DOM attributes (`data-landing-cover`, `data-theme="light"`, `data-bytes="23488"`, `data-bytes="24820"`), and stylesheet rule `.site-foot { padding:0 var(--page-gutter,24px) }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.glass-bar> — `atmos-gallery`)` (`atmos-gallery`) adapts across `@media (hover:hover) and (prefers-reduced-motion:no-preference)`, `@media screen and (width<=700px)`, `@media (prefers-reduced-motion:reduce)`, `@media screen and (width<=720px)` with `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.4,0,1,1)` transitions and links `Privacy Privacy · Terms Terms`.
2. **Hero Stage & Focal Lead (<section.lenis-stopped> — `Colour Read from Light and Atmosph`)**:
   - DOM & Selectors: Landmark `<section class="lenis-stopped">` presenting display lead `Colour Read from Light and Atmosphere. In Seconds.` and copy excerpt *"Skip to Main Content"* over `#f5f5f3` canvas and `#1a1a1a` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#f5f5f3` background with `#1a1a1a` headline `Colour Read from Light and Atmosphere. In Seconds.`.
3. **Primary Showcase & Content Grid (<section.boot-inner> — `Library`)**:
   - DOM & Selectors: Landmark `<section class="boot-inner">` rendering section `Library` with copy *"Colour Read from Light and Atmosphere."*, asset references (`atmos-gallery-fav.png`, `NeueMontreal-Regular.woff2`, `NeueMontreal-Medium.woff2`, `gsap.min.js`), and grid rule `.site-foot__brand { padding:44px 0 24px }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.boot-inner> — `Library`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 24ch`, `gap: 40px`) on desktop and Single-column vertical stack at `390px` viewport width with `44px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.boot-row> — `Start here`)**:
   - DOM & Selectors: Landmark `<section class="boot-row">` framing `Start here` and `Atmos Gallery` (*"How it Works How it Works"*) with `#fff` surface cards, `#1a1a1a` accents, and `.site-foot__brand a { line-height:0;text-decoration:none;display:block }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.boot-row> — `Start here`)` uses `var(--radius-pill)`, `var(--radius-card)`, `var(--button-border-radius)`, `var(--radius-tick)` radii, `#1a1a1a` highlights, and assets (atmos-gallery-fav.png, NeueMontreal-Regular.woff2, NeueMontreal-Medium.woff2).
5. **Colophon & Global Directory Footer (<footer.site-foot> — `https://atmos.gallery`)**:
   - DOM & Selectors: Landmark `<footer class="site-foot">` anchoring `Atmos Gallery · Image Colour Pal` footer links (`Privacy Privacy · Terms Terms`), copy *"Privacy Settings Privacy Settings"*, and `#ff6e62` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.site-foot> — `https://atmos.gallery`)` aligns to `24ch` extracted from `atmos-gallery` stylesheet with `44px` lateral canvas padding with `40px` grid gap and attributes (data-landing-cover, data-theme="light", data-bytes="23488").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Skip to Main Content"*
- Copy Excerpt 2: *"Colour Read from Light and Atmosphere."*
- Copy Excerpt 3: *"How it Works How it Works"*
- Copy Excerpt 4: *"Privacy Settings Privacy Settings"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.4,0,1,1)`
- **Extracted Stylesheet Rules (`atmos-gallery`)**:
- `.site-foot { padding:0 var(--page-gutter,24px) }`
- `.site-foot__brand { padding:44px 0 24px }`
- `.site-foot__brand a { line-height:0;text-decoration:none;display:block }`
- `.site-foot__brand a:focus-visible { outline:3px solid var(--on-surface);outline-offset:6px }`
- `.site-foot__nav { justify-content:center;gap:40px;display:flex }`
- **Per-Selector Transition Rules**:
- **Selector `.land-legal .site-foot__consent`**: `transition: color var(--dur-chrome) var(--ease-button-hover)` extracted from `atmos-gallery` stylesheet.
- **Selector `media (prefers-reduced-motion:red...`**: `transition: .001ms!important` extracted from `atmos-gallery` stylesheet.
- **Selector `data-logo-ring]`**: `transition: opacity var(--dur-fast) var(--ease-standard)` extracted from `atmos-gallery` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,1,.36,1)`)**: Governs interactive state transitions across `<header.glass-bar>` and `<section.boot-inner>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `atmos-gallery`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
