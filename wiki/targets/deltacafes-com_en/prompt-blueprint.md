---
title: "UI Prompt Blueprint: deltacafes-com_en"
date: 2026-11-15
target: "[[overview|deltacafes-com_en]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#9e0212`)"
---

# UI Design System & Master Generation Blueprint: deltacafes-com_en

> **Delta, coffee with heart · Delta Cafés — The coffee of your life** (https://deltacafes.com/en) — Discover Delta Cafés: Portuguese coffee heritage, culture, sustainability, and experiences from bean to cup for every coffee lover.

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/deltacafes-com_en/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Delta, coffee with heart · Delta Cafés — The coffee of your life** (`https://deltacafes.com/en`). Discover Delta Cafés: Portuguese coffee heritage, culture, sustainability, and experiences from bean to cup for every coffee lover.
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#9e0212`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--color-black)` in `:root`) paired with `#fff` primary typography and `#9e0212` accents.
  - **Extracted Typographic Hierarchy**: Pairs `trade-gothic` for display copy (`Delta Cafés`) with `delta-season` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1023px` container bounds (`gap: 1.445vw`, padding `.51vw`) with `cubic-bezier(.19,1,.22,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/deltacafes-com_en/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `1023px` extracted from `deltacafes-com_en` stylesheet.
- **Canvas Lateral Padding & Spacing**: `.51vw` lateral canvas padding with `1.445vw` grid gap.
- **Border Radius Scale**: `8px`, `38px`, `3px`, `1px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1023px`, `gap: 1.445vw`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `.51vw` horizontal padding.
- **Extracted CSS Media Queries**: `@media only screen and (min-width:2000px)`, `@media only screen and (max-width:1023px)`, `@media only screen and (max-width:1290px)`, `@media only screen and (max-width:743px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ffd300` | `var(--color-geral-delta-yellow)` in `:root` |
| **Interactive Accent / Highlight** | `#9e0212` | `var(--color-geral-delta-darkRed)` in `:root` |
| **Secondary / Muted Copy** | `#e70025` | `var(--color-geral-delta-brightRed)` in `:root` |
| **Structural Hairline Border** | `#aca59e` | `var(--color-aged-oak-200)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--fontPairingTitle-color` | `var(--color-creme-100)` | Brand / Palette Token |
| `--button-color` | `var(--color-brown-500)` | Brand / Palette Token |
| `--button-backgroundColor` | `var(--color-creme-100)` | Canvas / Surface Token |
| `--icon-color` | `var(--footer-color, var(--color-creme-100))` | Brand / Palette Token |
| `--tag-color` | `var(--journalCard-color, var(--color-brown-500))` | Brand / Palette Token |
| `--button-accentColor` | `transparent` | Brand / Palette Token |
| `--tail-width` | `clamp(30px, 25.515px + 100vw * .0115, 45px)` | Layout / Spatial Grid Token |
| `--tail-height` | `clamp(12px, 10.206px + 100vw * .0046, 18px)` | Layout / Spatial Grid Token |
| `--circle-width` | `660` | Layout / Spatial Grid Token |
| `--initial-100vh` | `100vh` | Layout / Spatial Grid Token |
| `--native-scrollbar-width` | `0px` | Layout / Spatial Grid Token |
| `--computed-100vh` | `100vh` | Layout / Spatial Grid Token |
| `--computed-100vw` | `calc(100vw - var(--native-scrollbar-width))` | Layout / Spatial Grid Token |
| `--grid-columns` | `32` | Layout / Spatial Grid Token |
| `--grid-gap` | `clamp(12px, 8.412px + 100vw * .0092, 24px)` | Layout / Spatial Grid Token |
| `--grid-half-gap` | `calc(var(--grid-gap)*.5)` | Layout / Spatial Grid Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `trade-gothic`.
- **Primary Body Stack**: `delta-season`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `14px`, `clamp(18px,16.206px + 100vw * .00...`, `.51vw`, `.595vw`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 12px`, `line-height: 1.3em`, `letter-spacing: -.01em`, `font-weight: 700`).
- **Body Copy**: CSS variables `--body-backgroundColor: #2b1b14`; rule `p` (`font-size: clamp(18px,16.206px + 100vw *...`, `line-height: 1.2em`, `letter-spacing: -.02em`, `font-weight: 420`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `14px`, `clamp(18px,16.206px + 100vw * .00...`, `.51vw`, `.595vw`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.19,1,.22,1)`, `cubic-bezier(.165,.84,.44,1)`, `cubic-bezier(.455,.03,.515,.955)`.

### Per-Element Transition & Choreography Rules
- **Selector `.group-title-wrapper .icon[data-v...`**: `transition: transform .75s cubic-bezier(.19,1,.22,1)` extracted from `deltacafes-com_en` stylesheet.
- **Selector `.main-group .links-wrapper[data-v...`**: `transition: height .75s cubic-bezier(.19,1,.22,1)` extracted from `deltacafes-com_en` stylesheet.
- **Selector `data-component=top][data-v-6c88df...`**: `transition: opacity .5s cubic-bezier(.19,1,.22,1),transform .5s cubic-b...` extracted from `deltacafes-com_en` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.19,1,.22,1)`)**: Governs interactive state transitions across `<header.lenis>` and `<section.scroller>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Delta, coffee with heart · Delta Cafés — T │
│ ====================================================================== │
│ [ <header.lenis>           | About Delta · The Azores Coffee · Prod ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.main>                                       |   │
│ | H1: Delta Cafés                                                  |   │
│ | Substrate: #000       | Ink: #fff       | Accent: #9e0212        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.scroller>        ) max-w: 1023px         |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Coffee Culture               |  | Delta, coffee with heart.    | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 1.445v) | │
│ | [<header.lenis>] -> [<section.main>] -> [<section.scroller>] |       │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.bg-mask-defs> ) | https://deltacafes.com/en          │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.lenis> — `deltacafes-com_en`)**:
   - Landmark `<header class="lenis">` hosting `Delta, coffee with heart · Delta Caf` navigation (`About Delta · The Azores Coffee · Products · The coffee cycle · Delta Sustainability`), DOM attributes (`data-website-id="0f29d428-885f-44b8-ae..."`, `data-component="scroller"`, `data-v-d2630b30`, `data-component="menu"`), and stylesheet rule `before { content:"";position:absolute;inset:0;z-index:1;background-color:var(--co... }`.
2. **Hero Stage & Focal Lead (<section.main> — `Delta Cafés`)**:
   - Landmark `<section class="main">` presenting display lead `Delta Cafés` and copy excerpt *"Business Solutions"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.scroller> — `Coffee Culture`)**:
   - Landmark `<section class="scroller">` rendering section `Coffee Culture` with copy *"Delta Cafés Our History About Delta The Azores coffee"*, asset references (`entry.D_EBu6YN.css`, `Footer.mdCQ3N1U.css`, `TransitionLogoMask.DT4Lfp-V.css`, `TagFlag.BCy09Tyz.css`), and grid rule `video { width:100%;height:100%;-o-object-fit:cover;object-fit:cover }`.
4. **Interactive Detail & Feature Matrix (<section.is-ready> — `Delta, coffee with heart.`)**:
   - Landmark `<section class="is-ready">` framing `Delta, coffee with heart.` and `The first Portuguese coffee.` (*"Coffee Culture Coffee Cycle Barista Academy Coffee Science Centre"*) with `#ffd300` surface cards, `#9e0212` accents, and `after { bottom:1px;background:0000004d }`.
5. **Colophon & Global Directory Footer (<footer.bg-mask-defs> — `https://deltacafes.com/en`)**:
   - Landmark `<footer class="bg-mask-defs">` anchoring `Delta, coffee with heart · Delta` footer links (`About Delta · The Azores Coffee · Products · The coffee cycle · Delta Sustainability`), copy *"Coffee Science Centre"*, and `#aca59e` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: deltacafes-com_en (Delta, coffee with heart · Delta Cafés — The coffee of your life)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `deltacafes-com_en` (**Delta, coffee with heart · Delta Cafés — The coffee of your life** — `https://deltacafes.com/en`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#9e0212`).
- **Identity & Domain Context**: Discover Delta Cafés: Portuguese coffee heritage, culture, sustainability, and experiences from bean to cup for every coffee lover.
- **Primary Substrate**: `#000` (`var(--color-black)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#9e0212`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--color-black)` in `:root`) paired with `#fff` primary typography and `#9e0212` accents.
  - **Extracted Typographic Hierarchy**: Pairs `trade-gothic` for display copy (`Delta Cafés`) with `delta-season` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1023px` container bounds (`gap: 1.445vw`, padding `.51vw`) with `cubic-bezier(.19,1,.22,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `deltacafes-com_en` in your global stylesheet:

:root {
  /* Delta, coffee with heart · Delta Cafés — The coffee of your life (deltacafes-com_en) — Ground-Truth Extracted CSS Variables */
  --fontPairingTitle-color: var(--color-creme-100); /* Brand / Palette Token (deltacafes-com_en) */
  --button-color: var(--color-brown-500); /* Brand / Palette Token (deltacafes-com_en) */
  --button-backgroundColor: var(--color-creme-100); /* Canvas / Surface Token (deltacafes-com_en) */
  --icon-color: var(--footer-color, var(--color-creme-100)); /* Brand / Palette Token (deltacafes-com_en) */
  --tag-color: var(--journalCard-color, var(--color-brown-500)); /* Brand / Palette Token (deltacafes-com_en) */
  --button-accentColor: transparent; /* Brand / Palette Token (deltacafes-com_en) */
  --tail-width: clamp(30px, 25.515px + 100vw * .0115, 45px); /* Layout / Spatial Grid Token (deltacafes-com_en) */
  --tail-height: clamp(12px, 10.206px + 100vw * .0046, 18px); /* Layout / Spatial Grid Token (deltacafes-com_en) */
  --circle-width: 660; /* Layout / Spatial Grid Token (deltacafes-com_en) */
  --initial-100vh: 100vh; /* Layout / Spatial Grid Token (deltacafes-com_en) */
  --native-scrollbar-width: 0px; /* Layout / Spatial Grid Token (deltacafes-com_en) */
  --computed-100vh: 100vh; /* Layout / Spatial Grid Token (deltacafes-com_en) */
  --computed-100vw: calc(100vw - var(--native-scrollbar-width)); /* Layout / Spatial Grid Token (deltacafes-com_en) */
  --grid-columns: 32; /* Layout / Spatial Grid Token (deltacafes-com_en) */
  --grid-gap: clamp(12px, 8.412px + 100vw * .0092, 24px); /* Layout / Spatial Grid Token (deltacafes-com_en) */
  --grid-half-gap: calc(var(--grid-gap)*.5); /* Layout / Spatial Grid Token (deltacafes-com_en) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000` — grounded in `var(--color-black)` in `:root`
- **Primary Typography Ink**: `#fff` — grounded in `var(--color-white)` in `:root`
- **Elevated Surface / Card Substrate**: `#ffd300` — grounded in `var(--color-geral-delta-yellow)` in `:root`
- **Interactive Accent / Highlight**: `#9e0212` — grounded in `var(--color-geral-delta-darkRed)` in `:root`
- **Secondary / Muted Copy**: `#e70025` — grounded in `var(--color-geral-delta-brightRed)` in `:root`
- **Structural Hairline Border**: `#aca59e` — grounded in `var(--color-aged-oak-200)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1023px` extracted from `deltacafes-com_en` stylesheet
- **Padding & Gutters**: `.51vw` lateral canvas padding with `1.445vw` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1023px`, `gap: 1.445vw`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `.51vw` horizontal padding
- **Media Queries**: `@media only screen and (min-width:2000px)`, `@media only screen and (max-width:1023px)`, `@media only screen and (max-width:1290px)`, `@media only screen and (max-width:743px)`
- **Corner Radii**: `8px`, `38px`, `3px`, `1px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `trade-gothic`
- **Body Font Stack**: `delta-season`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `14px`, `clamp(18px,16.206px + 100vw * .00...`, `.51vw`, `.595vw`)
- **H2 Section Rule**: rule `h2` (`font-size: 12px`, `line-height: 1.3em`, `letter-spacing: -.01em`, `font-weight: 700`)
- **Body Copy Rule**: CSS variables `--body-backgroundColor: #000`; rule `p` (`font-size: clamp(18px,16.206px + 100vw *...`, `line-height: 1.2em`, `letter-spacing: -.02em`, `font-weight: 420`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `14px`, `clamp(18px,16.206px + 100vw * .00...`, `.51vw`, `.595vw`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `deltacafes-com_en` (`Delta, coffee with heart · Delta Cafés — The coffee of your life`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.lenis> — `deltacafes-com_en`)**:
   - DOM & Selectors: Landmark `<header class="lenis">` hosting `Delta, coffee with heart · Delta Caf` navigation (`About Delta · The Azores Coffee · Products · The coffee cycle · Delta Sustainability`), DOM attributes (`data-website-id="0f29d428-885f-44b8-ae..."`, `data-component="scroller"`, `data-v-d2630b30`, `data-component="menu"`), and stylesheet rule `before { content:"";position:absolute;inset:0;z-index:1;background-color:var(--co... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.lenis> — `deltacafes-com_en`)` (`deltacafes-com_en`) adapts across `@media only screen and (min-width:2000px)`, `@media only screen and (max-width:1023px)`, `@media only screen and (max-width:1290px)`, `@media only screen and (max-width:743px)` with `cubic-bezier(.19,1,.22,1)`, `cubic-bezier(.165,.84,.44,1)`, `cubic-bezier(.455,.03,.515,.955)` transitions and links `About Delta · The Azores Coffee · Products · The coffee cycle · Delta Sustainability`.
2. **Hero Stage & Focal Lead (<section.main> — `Delta Cafés`)**:
   - DOM & Selectors: Landmark `<section class="main">` presenting display lead `Delta Cafés` and copy excerpt *"Business Solutions"* over `#000` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#000` background with `#fff` headline `Delta Cafés`.
3. **Primary Showcase & Content Grid (<section.scroller> — `Coffee Culture`)**:
   - DOM & Selectors: Landmark `<section class="scroller">` rendering section `Coffee Culture` with copy *"Delta Cafés Our History About Delta The Azores coffee"*, asset references (`entry.D_EBu6YN.css`, `Footer.mdCQ3N1U.css`, `TransitionLogoMask.DT4Lfp-V.css`, `TagFlag.BCy09Tyz.css`), and grid rule `video { width:100%;height:100%;-o-object-fit:cover;object-fit:cover }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.scroller> — `Coffee Culture`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1023px`, `gap: 1.445vw`) on desktop and Single-column vertical stack at `390px` viewport width with `.51vw` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.is-ready> — `Delta, coffee with heart.`)**:
   - DOM & Selectors: Landmark `<section class="is-ready">` framing `Delta, coffee with heart.` and `The first Portuguese coffee.` (*"Coffee Culture Coffee Cycle Barista Academy Coffee Science Centre"*) with `#ffd300` surface cards, `#9e0212` accents, and `after { bottom:1px;background:0000004d }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.is-ready> — `Delta, coffee with heart.`)` uses `8px`, `38px`, `3px`, `1px` radii, `#9e0212` highlights, and assets (entry.D_EBu6YN.css, Footer.mdCQ3N1U.css, TransitionLogoMask.DT4Lfp-V.css).
5. **Colophon & Global Directory Footer (<footer.bg-mask-defs> — `https://deltacafes.com/en`)**:
   - DOM & Selectors: Landmark `<footer class="bg-mask-defs">` anchoring `Delta, coffee with heart · Delta` footer links (`About Delta · The Azores Coffee · Products · The coffee cycle · Delta Sustainability`), copy *"Coffee Science Centre"*, and `#aca59e` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.bg-mask-defs> — `https://deltacafes.com/en`)` aligns to `1023px` extracted from `deltacafes-com_en` stylesheet with `.51vw` lateral canvas padding with `1.445vw` grid gap and attributes (data-website-id="0f29d428-885f-44b8-ae...", data-component="scroller", data-v-d2630b30).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Business Solutions"*
- Copy Excerpt 2: *"Delta Cafés Our History About Delta The Azores coffee"*
- Copy Excerpt 3: *"Coffee Culture Coffee Cycle Barista Academy Coffee Science Centre"*
- Copy Excerpt 4: *"Coffee Science Centre"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.19,1,.22,1)`, `cubic-bezier(.165,.84,.44,1)`, `cubic-bezier(.455,.03,.515,.955)`
- **Extracted Stylesheet Rules (`deltacafes-com_en`)**:
- `before { content:"";position:absolute;inset:0;z-index:1;background-color:var(--co... }`
- `video { width:100%;height:100%;-o-object-fit:cover;object-fit:cover }`
- `after { bottom:1px;background:0000004d }`
- `path { fill:var(--color-creme-100) }`
- `a:before { content:"";position:absolute;left:-10px;top:-10px;width:calc(100% + 20px... }`
- **Per-Selector Transition Rules**:
- **Selector `.group-title-wrapper .icon[data-v...`**: `transition: transform .75s cubic-bezier(.19,1,.22,1)` extracted from `deltacafes-com_en` stylesheet.
- **Selector `.main-group .links-wrapper[data-v...`**: `transition: height .75s cubic-bezier(.19,1,.22,1)` extracted from `deltacafes-com_en` stylesheet.
- **Selector `data-component=top][data-v-6c88df...`**: `transition: opacity .5s cubic-bezier(.19,1,.22,1),transform .5s cubic-b...` extracted from `deltacafes-com_en` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.19,1,.22,1)`)**: Governs interactive state transitions across `<header.lenis>` and `<section.scroller>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `deltacafes-com_en`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
