---
title: "UI Prompt Blueprint: seedance3-si"
date: 2026-11-15
target: "[[overview|seedance3-si]]"
status: analyzed
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#242520` canvas, `#e4e4e7` ink, `#111113` accent)"
---

# UI Design System & Master Generation Blueprint: seedance3-si

> **Seedance 3.0 AI Video Generator: Make Videos from References** (https://seedance3.si/) — Try Seedance 3.0 free online. Turn text, images, video clips, and audio into videos with sound. Keep faces the same and edit any part wit...

![Desktop Viewport Capture (1440x10319)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Seedance 3.0 AI Video Generator: Make Videos from References** (`https://seedance3.si/`). Try Seedance 3.0 free online. Turn text, images, video clips, and audio into videos with sound. Keep faces the same and edit any part wit...
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#242520` canvas, `#e4e4e7` ink, `#111113` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#242520` (`var(--menu-ink)` in `:root`) paired with `#e4e4e7` primary typography and `#111113` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Montserrat` for display copy (`Seedance 3.0 AI Video Generator`) with `Montserrat Fallback` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `440px` container bounds (`gap: 10px`, padding `18px`) with `cubic-bezier(.2,.7,.2,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×10319px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `440px` extracted from `seedance3-si` stylesheet.
- **Canvas Lateral Padding & Spacing**: `18px` lateral canvas padding with `10px` grid gap.
- **Border Radius Scale**: `18px`, `50%`, `10px`, `6px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 440px`, `gap: 10px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `18px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (max-width:440px)`, `@media (max-width:639px)`, `@media (min-width:1280px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#242520` | `var(--menu-ink)` in `:root` |
| **Primary Typography Ink** | `#777970` | `var(--menu-muted)` in `:root` |
| **Elevated Surface / Card Substrate** | `#d3ff02` | `var(--theme-promotion)` in `:root` |
| **Interactive Accent / Highlight** | `#111113` | `var(--theme-promo-background)` in `:root` |
| **Secondary / Muted Copy** | `#e4e4e7` | `var(--theme-promo-foreground)` in `:root` |
| **Structural Hairline Border** | `#b5df00` | `var(--theme-primary-strong)` in `:root` |
| **Variable Token (`--menu-line`)** | `#1c1e181a` | `var(--menu-line)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--menu-ink` | `#242520` | Typography Ink Token |
| `--menu-muted` | `#777970` | Color / Atmospheric Token |
| `--menu-line` | `#1c1e181a` | Color / Atmospheric Token |
| `--theme-promotion` | `#d3ff02` | Brand / Palette Token |
| `--theme-promotion-text` | `#d3ff02` | Typography Ink Token |
| `--theme-discount` | `var(--theme-promotion-text)` | Brand / Palette Token |
| `--theme-primary` | `#d3ff02` | Brand / Palette Token |
| `--theme-primary-text` | `var(--theme-promotion-text)` | Typography Ink Token |
| `--theme-logo-gradient` | `linear-gradient(var(--theme-promotion-text),var(--theme-promotion-text))` | Brand / Palette Token |
| `--theme-highlight` | `var(--theme-primary)` | Canvas / Surface Token |
| `--theme-promo-background` | `#111113` | Canvas / Surface Token |
| `--theme-promo-foreground` | `#e4e4e7` | Typography Ink Token |
| `--brand-from` | `var(--theme-highlight)` | Brand / Palette Token |
| `--brand-via` | `var(--theme-highlight)` | Brand / Palette Token |
| `--brand-to` | `var(--theme-secondary)` | Brand / Palette Token |
| `--brand-accent` | `var(--theme-primary)` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Montserrat`.
- **Primary Body Stack**: `Montserrat Fallback`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--font-display: var(--font-home-heading)`, `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5/2.25)`; rule `h1` (`font-weight: 800`).
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-3xl: 1.875rem`.
- **Body Copy**: CSS variables `--font-body: "Geist","Geist Fallback"`, `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`; rule `p` (`font-size: clamp(16px,1.4vw,18px)`, `letter-spacing: .01em`, `font-weight: 500`).
- **Metadata & Navigation Labels**: CSS variables `--font-mono: var(--font-mono)`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1/.75)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.2,.7,.2,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.navigation-module__C5Mk9a__artwork`**: `transition: transform .65s cubic-bezier(.2,.7,.2,1)` extracted from `seedance3-si` stylesheet.
- **Selector `.navigation-module__C5Mk9a__featu...`**: `transition: background .18s,color .18s,transform .18s` extracted from `seedance3-si` stylesheet.
- **Selector `.navigation-module__C5Mk9a__model`**: `transition: background .18s` extracted from `seedance3-si` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.2,.7,.2,1)`)**: Governs interactive state transitions across `<header.tool-header>` and `<section.py-14>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Seedance 3.0 AI Video Generator: Make Vide │
│ ====================================================================== │
│ [ <header.tool-header>     | Pricing                                ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.theme-gold>                                 |   │
│ | H1: Seedance 3.0 AI Video Generator                              |   │
│ | Substrate: #242520    | Ink: #e4e4e7    | Accent: #111113        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.py-14>           ) max-w: 440px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Seedance 3.0 Features        |  | Multi-Material Input         | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 10px  ) | │
│ | [<header.tool-heade] -> [<section.theme-gol] -> [<section.py-14>] |  │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.flex>         ) | https://seedance3.si/              │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.tool-header> — `seedance3-si`)**:
   - Landmark `<header class="tool-header fixed">` hosting `Seedance 3.0 AI Video Generator: Mak` navigation (`Pricing`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.navigation-module__C5Mk9a__image... { width:min(380px,100vw - 32px) }`.
2. **Hero Stage & Focal Lead (<section.theme-gold> — `Seedance 3.0 AI Video Generator`)**:
   - Landmark `<section class="theme-gold">` presenting display lead `Seedance 3.0 AI Video Generator` and copy excerpt *"Seedance 3.0 Launch Sale: Get 50% off all yearly plans"* over `#242520` canvas and `#e4e4e7` ink.
3. **Primary Showcase & Content Grid (<section.py-14> — `Seedance 3.0 Features`)**:
   - Landmark `<section class="py-14 text-white">` rendering section `Seedance 3.0 Features` with copy *"Seedance 3.0 Launch Sale:"*, asset references (`logo.png`, `799ac774ede1e27a.css`, `49ebc7f384a00a1c.css`, `41592914de078ed4.css`), and grid rule `.navigation-module__C5Mk9a__eyebrow { align-items:center;gap:10px;margin:2px 2px 14px;display:flex }`.
4. **Interactive Detail & Feature Matrix (<article.cursor-pointer> — `Multi-Material Input`)**:
   - Landmark `<article class="cursor-pointer rounded-2xl">` framing `Multi-Material Input` and `Precise Editing` (*"Seedance 3.0 Seedance 3.0"*) with `#d3ff02` surface cards, `#111113` accents, and `vigation-module__C5Mk9a__eyebrow:... { content:"";background:var(--primary);border-radius:50%;width:5px;height:5px }`.
5. **Colophon & Global Directory Footer (<footer.flex> — `https://seedance3.si/`)**:
   - Landmark `<footer class="flex">` anchoring `Seedance 3.0 AI Video Generator:` footer links (`Pricing`), copy *"Models Seedance 2.5 Seedance 2.0"*, and `#b5df00` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: seedance3-si (Seedance 3.0 AI Video Generator: Make Videos from References)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `seedance3-si` (**Seedance 3.0 AI Video Generator: Make Videos from References** — `https://seedance3.si/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#242520` canvas, `#e4e4e7` ink, `#111113` accent).
- **Identity & Domain Context**: Try Seedance 3.0 free online. Turn text, images, video clips, and audio into videos with sound. Keep faces the same and edit any part wit...
- **Primary Substrate**: `#242520` (`var(--menu-ink)` in `:root`), **Primary Ink**: `#e4e4e7`, **Accent / Highlight**: `#111113`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#242520` (`var(--menu-ink)` in `:root`) paired with `#e4e4e7` primary typography and `#111113` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Montserrat` for display copy (`Seedance 3.0 AI Video Generator`) with `Montserrat Fallback` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `440px` container bounds (`gap: 10px`, padding `18px`) with `cubic-bezier(.2,.7,.2,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `seedance3-si` in your global stylesheet:

:root {
  /* Seedance 3.0 AI Video Generator: Make Videos from References (seedance3-si) — Ground-Truth Extracted CSS Variables */
  --menu-ink: #242520; /* Typography Ink Token (seedance3-si) */
  --menu-muted: #777970; /* Color / Atmospheric Token (seedance3-si) */
  --menu-line: #1c1e181a; /* Color / Atmospheric Token (seedance3-si) */
  --theme-promotion: #d3ff02; /* Brand / Palette Token (seedance3-si) */
  --theme-promotion-text: #d3ff02; /* Typography Ink Token (seedance3-si) */
  --theme-discount: var(--theme-promotion-text); /* Brand / Palette Token (seedance3-si) */
  --theme-primary: #d3ff02; /* Brand / Palette Token (seedance3-si) */
  --theme-primary-text: var(--theme-promotion-text); /* Typography Ink Token (seedance3-si) */
  --theme-logo-gradient: linear-gradient(var(--theme-promotion-text),var(--theme-promotion-text)); /* Brand / Palette Token (seedance3-si) */
  --theme-highlight: var(--theme-primary); /* Canvas / Surface Token (seedance3-si) */
  --theme-promo-background: #111113; /* Canvas / Surface Token (seedance3-si) */
  --theme-promo-foreground: #e4e4e7; /* Typography Ink Token (seedance3-si) */
  --brand-from: var(--theme-highlight); /* Brand / Palette Token (seedance3-si) */
  --brand-via: var(--theme-highlight); /* Brand / Palette Token (seedance3-si) */
  --brand-to: var(--theme-secondary); /* Brand / Palette Token (seedance3-si) */
  --brand-accent: var(--theme-primary); /* Brand / Palette Token (seedance3-si) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#242520` — grounded in `var(--menu-ink)` in `:root`
- **Primary Typography Ink**: `#777970` — grounded in `var(--menu-muted)` in `:root`
- **Elevated Surface / Card Substrate**: `#d3ff02` — grounded in `var(--theme-promotion)` in `:root`
- **Interactive Accent / Highlight**: `#111113` — grounded in `var(--theme-promo-background)` in `:root`
- **Secondary / Muted Copy**: `#e4e4e7` — grounded in `var(--theme-promo-foreground)` in `:root`
- **Structural Hairline Border**: `#b5df00` — grounded in `var(--theme-primary-strong)` in `:root`
- **Variable Token (`--menu-line`)**: `#1c1e181a` — grounded in `var(--menu-line)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×10319px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `440px` extracted from `seedance3-si` stylesheet
- **Padding & Gutters**: `18px` lateral canvas padding with `10px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 440px`, `gap: 10px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `18px` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (max-width:440px)`, `@media (max-width:639px)`, `@media (min-width:1280px)`
- **Corner Radii**: `18px`, `50%`, `10px`, `6px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Montserrat`
- **Body Font Stack**: `Montserrat Fallback`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--font-display: var(--font-home-heading)`, `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5/2.25)`; rule `h1` (`font-weight: 800`)
- **H2 Section Rule**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-3xl: 1.875rem`
- **Body Copy Rule**: CSS variables `--font-body: "Geist","Geist Fallback"`, `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`; rule `p` (`font-size: clamp(16px,1.4vw,18px)`, `letter-spacing: .01em`, `font-weight: 500`)
- **Metadata & Index Rule**: CSS variables `--font-mono: var(--font-mono)`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1/.75)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `seedance3-si` (`Seedance 3.0 AI Video Generator: Make Videos from References`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.tool-header> — `seedance3-si`)**:
   - DOM & Selectors: Landmark `<header class="tool-header fixed">` hosting `Seedance 3.0 AI Video Generator: Mak` navigation (`Pricing`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.navigation-module__C5Mk9a__image... { width:min(380px,100vw - 32px) }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.tool-header> — `seedance3-si`)` (`seedance3-si`) adapts across `@media (prefers-reduced-motion:reduce)`, `@media (max-width:440px)`, `@media (max-width:639px)`, `@media (min-width:1280px)` with `cubic-bezier(.2,.7,.2,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `Pricing`.
2. **Hero Stage & Focal Lead (<section.theme-gold> — `Seedance 3.0 AI Video Generator`)**:
   - DOM & Selectors: Landmark `<section class="theme-gold">` presenting display lead `Seedance 3.0 AI Video Generator` and copy excerpt *"Seedance 3.0 Launch Sale: Get 50% off all yearly plans"* over `#242520` canvas and `#e4e4e7` ink.
   - Responsive Contract: Hero stage (`1440×10319px` desktop / `390×2400px` mobile) sets `#242520` background with `#e4e4e7` headline `Seedance 3.0 AI Video Generator`.
3. **Primary Showcase & Content Grid (<section.py-14> — `Seedance 3.0 Features`)**:
   - DOM & Selectors: Landmark `<section class="py-14 text-white">` rendering section `Seedance 3.0 Features` with copy *"Seedance 3.0 Launch Sale:"*, asset references (`logo.png`, `799ac774ede1e27a.css`, `49ebc7f384a00a1c.css`, `41592914de078ed4.css`), and grid rule `.navigation-module__C5Mk9a__eyebrow { align-items:center;gap:10px;margin:2px 2px 14px;display:flex }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.py-14> — `Seedance 3.0 Features`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 440px`, `gap: 10px`) on desktop and Single-column vertical stack at `390px` viewport width with `18px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.cursor-pointer> — `Multi-Material Input`)**:
   - DOM & Selectors: Landmark `<article class="cursor-pointer rounded-2xl">` framing `Multi-Material Input` and `Precise Editing` (*"Seedance 3.0 Seedance 3.0"*) with `#d3ff02` surface cards, `#111113` accents, and `vigation-module__C5Mk9a__eyebrow:... { content:"";background:var(--primary);border-radius:50%;width:5px;height:5px }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.cursor-pointer> — `Multi-Material Input`)` uses `18px`, `50%`, `10px`, `6px` radii, `#111113` highlights, and assets (logo.png, 799ac774ede1e27a.css, 49ebc7f384a00a1c.css).
5. **Colophon & Global Directory Footer (<footer.flex> — `https://seedance3.si/`)**:
   - DOM & Selectors: Landmark `<footer class="flex">` anchoring `Seedance 3.0 AI Video Generator:` footer links (`Pricing`), copy *"Models Seedance 2.5 Seedance 2.0"*, and `#b5df00` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.flex> — `https://seedance3.si/`)` aligns to `440px` extracted from `seedance3-si` stylesheet with `18px` lateral canvas padding with `10px` grid gap and attributes (data-precedence="next", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Seedance 3.0 Launch Sale: Get 50% off all yearly plans"*
- Copy Excerpt 2: *"Seedance 3.0 Launch Sale:"*
- Copy Excerpt 3: *"Seedance 3.0 Seedance 3.0"*
- Copy Excerpt 4: *"Models Seedance 2.5 Seedance 2.0"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.2,.7,.2,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`seedance3-si`)**:
- `.navigation-module__C5Mk9a__image... { width:min(380px,100vw - 32px) }`
- `.navigation-module__C5Mk9a__eyebrow { align-items:center;gap:10px;margin:2px 2px 14px;display:flex }`
- `vigation-module__C5Mk9a__eyebrow:... { content:"";background:var(--primary);border-radius:50%;width:5px;height:5px }`
- `navigation-module__C5Mk9a__sectio... { margin:22px 2px 8px }`
- `avigation-module__C5Mk9a__feature... { content:"";z-index:-1;background:linear-gradient(060c0f0d 10%,060c0f33 4... }`
- **Per-Selector Transition Rules**:
- **Selector `.navigation-module__C5Mk9a__artwork`**: `transition: transform .65s cubic-bezier(.2,.7,.2,1)` extracted from `seedance3-si` stylesheet.
- **Selector `.navigation-module__C5Mk9a__featu...`**: `transition: background .18s,color .18s,transform .18s` extracted from `seedance3-si` stylesheet.
- **Selector `.navigation-module__C5Mk9a__model`**: `transition: background .18s` extracted from `seedance3-si` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.2,.7,.2,1)`)**: Governs interactive state transitions across `<header.tool-header>` and `<section.py-14>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `seedance3-si`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
