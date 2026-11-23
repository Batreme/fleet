---
title: "UI Prompt Blueprint: deltacafes-com_en"
date: 2026-11-23
captured_at: 2026-11-23
target: "deltacafes-com_en"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#2b1b14` / `#f7a200`)"
---

# UI Design System & Master Generation Blueprint: deltacafes-com_en

> **Delta, coffee with heart · Delta Cafés — The coffee of your life** (https://deltacafes.com/en) — Discover Delta Cafés: Portuguese coffee heritage, culture, sustainability, and experiences from bean to cup for every coffee lover.

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Delta, coffee with heart · Delta Cafés — The coffee of your life** (`https://deltacafes.com/en`). Discover Delta Cafés: Portuguese coffee heritage, culture, sustainability, and experiences from bean to cup for every coffee lover.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#2b1b14` / `#f7a200`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#2b1b14` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#fcf3ed` primary typography and `#f7a200` accents.
  - **Grounded Typographic Hierarchy**: Pairs `delta-season` for display copy (`Delta, coffee with heart.`) with `trade-gothic` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 21.784px`, padding `.68vw`) with `cubic-bezier(.19,1,.22,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x844)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×844px` (`assets/mobile.png`, single-viewport 100vh live capture (844px)).
- **Master Container Bounds**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport).
- **Canvas Lateral Padding & Spacing**: `.68vw` lateral canvas padding with `21.784px` grid gap.
- **Border Radius Scale**: `8px`, `3px`, `1px`, `5px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 21.784px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `.68vw` horizontal padding.
- **Extracted CSS Media Queries**: `@media only screen and (min-width:2000px)`, `@media only screen and (max-width:1023px)`, `@media only screen and (max-width:1290px)`, `@media only screen and (max-width:743px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#2b1b14` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#fcf3ed` | live computed `a` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | `:before { background-color: black }` (`#000000`) |
| **Interactive Accent / Highlight** | `#f7a200` | `var(--color-product-superior-accent-500)` in `:root` |
| **Secondary / Muted Copy** | `#e3c1ad` | live computed `h1` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#cccccc` | `var(--iti-border-color)` in `:root` |
| **Variable Token (`--color-white`)** | `#ffffff` | `var(--color-white)` in `:root` |
| **Variable Token (`--color-geral-delta-yellow`)** | `#ffd300` | `var(--color-geral-delta-yellow)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--initial-100vh` | `100vh` | Layout / Spatial Grid Token |
| `--native-scrollbar-width` | `0px` | Layout / Spatial Grid Token |
| `--computed-100vh` | `100vh` | Layout / Spatial Grid Token |
| `--computed-100vw` | `calc(100vw - var(--native-scrollbar-width))` | Layout / Spatial Grid Token |
| `--grid-columns` | `32` | Layout / Spatial Grid Token |
| `--grid-gap` | `clamp(12px, 8.412px + 100vw * .0092, 24px)` | Layout / Spatial Grid Token |
| `--grid-half-gap` | `calc(var(--grid-gap)*.5)` | Layout / Spatial Grid Token |
| `--grid-margin` | `clamp(12px, 8.412px + 100vw * .0092, 24px)` | Layout / Spatial Grid Token |
| `--grid-padding` | `calc(var(--grid-margin) - var(--grid-gap)*.5)` | Layout / Spatial Grid Token |
| `--grid-width` | `calc(var(--100vw) - var(--grid-margin)*2)` | Layout / Spatial Grid Token |
| `--modal-width` | `calc(var(--modal-row-width) + var(--grid-half-gap))` | Layout / Spatial Grid Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--color-geral-black` | `#000` | Canvas / Surface Token |
| `--color-geral-white` | `#fff` | Canvas / Surface Token |
| `--color-geral-delta-yellow` | `#ffd300` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `delta-season`.
- **Primary Body Stack**: `trade-gothic`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 77.28px`, `line-height: 77.28px`, `font-weight: 300`, `letter-spacing: -1.5456px`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 77.28px`, `line-height: 77.28px`, `font-weight: 300`, `letter-spacing: -1.5456px`); rule `h2` (`font-size: 12px`, `line-height: 1.3em`, `letter-spacing: -.01em`, `font-weight: 700`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 16px`, `font-weight: 400`); rule `p` (`font-size: clamp(18px,16.206px + 100vw *...`, `line-height: 1.2em`, `letter-spacing: -.02em`, `font-weight: 420`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 11.84px`, `line-height: 14.208px`, `font-weight: 650`, `letter-spacing: 0.7104px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.19,1,.22,1)`, `cubic-bezier(.165,.84,.44,1)`, `cubic-bezier(.77,0,.175,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `-component=popup] .content[data-v...`**: `transition: height .5s cubic-bezier(.19,1,.22,1),width .5s cubic-bezier(.1...` extracted from `deltacafes-com_en` stylesheet.
- **Selector `nent=popup] .content .item[data-v...`**: `transition: opacity .5s cubic-bezier(.19,1,.22,1),transform .5s cubic-bezi...` extracted from `deltacafes-com_en` stylesheet.
- **Selector `.group-title-wrapper .icon[data-v...`**: `transition: transform .75s cubic-bezier(.19,1,.22,1)` extracted from `deltacafes-com_en` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.19,1,.22,1)`)**: Governs interactive state transitions across `<header.lenis>` and `<section.scroller>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Delta, coffee with heart · Delta Cafés — T │
│ ====================================================================== │
│ [ <header.lenis> (1440x1127px)        | About Delta · The Azores Cof ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.main> (w=1440px)                              | │
│ | H1: Delta, coffee with heart.                                      | │
│ | Substrate: #2b1b14 | Ink: #fcf3ed | Accent: #f7a200                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.scroller>) max-w: 1440px                   | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Since 1961, coffee that awak |  | The journey of coffee        | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.is-ready>) — The Culture of Coffee         | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.bg-mask-defs) | https://deltacafes.com/en            │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 21.784px)   │
│ ====================================================================== │
│ [ HEADER BAR (<header.lenis>          ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.main>) — 390px Vertical Lead                  | │
│ | H1: Delta, coffee with heart.                                      | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.scroller>) — 1-Col Stack                  | │
│ | [ Item 1: Since 1961, coffee that awakens stories                ] | │
│ | [ Item 2: The journey of coffee                                  ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.is-ready>) — 1-Col (The Culture of Cof)     | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.bg-mask-defs) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.lenis> — `deltacafes-com_en`)**:
   - Landmark `<header class="lenis">` (`1440x1127px`) hosting `Delta, coffee with heart · Delta Caf` navigation (`About Delta · The Azores Coffee · Products · The coffee cycle · Delta Sustainability`), DOM attributes (`data-website-id="0f29d428-885f-44b8-ae..."`, `data-onload`, `data-onerror`, `data-hid="googleTagManager"`), and stylesheet rule `before { display:none }`.
2. **Hero Stage & Focal Lead (<section.main> — `Delta, coffee with heart.`)**:
   - Landmark `<section class="main">` presenting display lead `Delta, coffee with heart.` and copy excerpt *"coffee that awakens"* over `#2b1b14` canvas and `#fcf3ed` ink.
3. **Primary Showcase & Content Grid (<section.scroller> — `Since 1961, coffee that awakens st`)**:
   - Landmark `<section class="scroller">` rendering section `Since 1961, coffee that awakens stories` with copy *"Delta Cafés was born in Campo Maior from a family’s dream. Today,"*, asset references (`entry.DAMcazEw.css`, `Footer.BmMrv4ac.css`, `TransitionLogoMask.DT4Lfp-V.css`, `TagFlag.BCy09Tyz.css`), and grid rule `video { width:100%;height:100%;-o-object-fit:cover;object-fit:cover }`.
4. **Interactive Detail & Feature Matrix (<section.is-ready> — `The journey of coffee`)**:
   - Landmark `<section class="is-ready">` framing `The journey of coffee` and `The Culture of Coffee` (*"1986 Start of activity in Spain"*) with `#000000` surface cards, `#f7a200` accents, and `after { bottom:1px;background:0000004d }`.
5. **Colophon & Global Directory Footer (<footer.bg-mask-defs> — `https://deltacafes.com/en`)**:
   - Landmark `<footer class="bg-mask-defs">` anchoring `Delta, coffee with heart · Delta` footer links (`About Delta · The Azores Coffee · Products · The coffee cycle · Delta Sustainability`), copy *"Start of activity in Spain"*, and `#cccccc` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: deltacafes-com_en (Delta, coffee with heart · Delta Cafés — The coffee of your life)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `deltacafes-com_en` (**Delta, coffee with heart · Delta Cafés — The coffee of your life** — `https://deltacafes.com/en`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#2b1b14` / `#f7a200`).
- **Identity & Domain Context**: Discover Delta Cafés: Portuguese coffee heritage, culture, sustainability, and experiences from bean to cup for every coffee lover.
- **Primary Substrate**: `#2b1b14` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#fcf3ed`, **Accent / Highlight**: `#f7a200`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#2b1b14` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#fcf3ed` primary typography and `#f7a200` accents.
  - **Grounded Typographic Hierarchy**: Pairs `delta-season` for display copy (`Delta, coffee with heart.`) with `trade-gothic` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 21.784px`, padding `.68vw`) with `cubic-bezier(.19,1,.22,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `deltacafes-com_en` in your global stylesheet:

:root {
  /* Delta, coffee with heart · Delta Cafés — The coffee of your life (deltacafes-com_en) — Live-Grounded CSS Variables */
  --initial-100vh: 100vh; /* Layout / Spatial Grid Token (deltacafes-com_en) */
  --native-scrollbar-width: 0px; /* Layout / Spatial Grid Token (deltacafes-com_en) */
  --computed-100vh: 100vh; /* Layout / Spatial Grid Token (deltacafes-com_en) */
  --computed-100vw: calc(100vw - var(--native-scrollbar-width)); /* Layout / Spatial Grid Token (deltacafes-com_en) */
  --grid-columns: 32; /* Layout / Spatial Grid Token (deltacafes-com_en) */
  --grid-gap: clamp(12px, 8.412px + 100vw * .0092, 24px); /* Layout / Spatial Grid Token (deltacafes-com_en) */
  --grid-half-gap: calc(var(--grid-gap)*.5); /* Layout / Spatial Grid Token (deltacafes-com_en) */
  --grid-margin: clamp(12px, 8.412px + 100vw * .0092, 24px); /* Layout / Spatial Grid Token (deltacafes-com_en) */
  --grid-padding: calc(var(--grid-margin) - var(--grid-gap)*.5); /* Layout / Spatial Grid Token (deltacafes-com_en) */
  --grid-width: calc(var(--100vw) - var(--grid-margin)*2); /* Layout / Spatial Grid Token (deltacafes-com_en) */
  --modal-width: calc(var(--modal-row-width) + var(--grid-half-gap)); /* Layout / Spatial Grid Token (deltacafes-com_en) */
  --color-black: #000; /* Canvas / Surface Token (deltacafes-com_en) */
  --color-white: #fff; /* Canvas / Surface Token (deltacafes-com_en) */
  --color-geral-black: #000; /* Canvas / Surface Token (deltacafes-com_en) */
  --color-geral-white: #fff; /* Canvas / Surface Token (deltacafes-com_en) */
  --color-geral-delta-yellow: #ffd300; /* Brand / Palette Token (deltacafes-com_en) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#2b1b14` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#fcf3ed` — grounded in live computed `a` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#000000` — grounded in `:before { background-color: black }` (`#000000`)
- **Interactive Accent / Highlight**: `#f7a200` — grounded in `var(--color-product-superior-accent-500)` in `:root`
- **Secondary / Muted Copy**: `#e3c1ad` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#cccccc` — grounded in `var(--iti-border-color)` in `:root`
- **Variable Token (`--color-white`)**: `#ffffff` — grounded in `var(--color-white)` in `:root`
- **Variable Token (`--color-geral-delta-yellow`)**: `#ffd300` — grounded in `var(--color-geral-delta-yellow)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×844px` (single-viewport 100vh live capture (844px), `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport)
- **Padding & Gutters**: `.68vw` lateral canvas padding with `21.784px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 21.784px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `.68vw` horizontal padding
- **Media Queries**: `@media only screen and (min-width:2000px)`, `@media only screen and (max-width:1023px)`, `@media only screen and (max-width:1290px)`, `@media only screen and (max-width:743px)`
- **Corner Radii**: `8px`, `3px`, `1px`, `5px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `delta-season`
- **Body Font Stack**: `trade-gothic`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 77.28px`, `line-height: 77.28px`, `font-weight: 300`, `letter-spacing: -1.5456px`)
- **H2 Section Rule**: live computed `h2` (`font-size: 77.28px`, `line-height: 77.28px`, `font-weight: 300`, `letter-spacing: -1.5456px`); rule `h2` (`font-size: 12px`, `line-height: 1.3em`, `letter-spacing: -.01em`, `font-weight: 700`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 16px`, `font-weight: 400`); rule `p` (`font-size: clamp(18px,16.206px + 100vw *...`, `line-height: 1.2em`, `letter-spacing: -.02em`, `font-weight: 420`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 11.84px`, `line-height: 14.208px`, `font-weight: 650`, `letter-spacing: 0.7104px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `deltacafes-com_en` (`Delta, coffee with heart · Delta Cafés — The coffee of your life`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.lenis> — `deltacafes-com_en`)**:
   - DOM & Selectors: Landmark `<header class="lenis">` (`1440x1127px`) hosting `Delta, coffee with heart · Delta Caf` navigation (`About Delta · The Azores Coffee · Products · The coffee cycle · Delta Sustainability`), DOM attributes (`data-website-id="0f29d428-885f-44b8-ae..."`, `data-onload`, `data-onerror`, `data-hid="googleTagManager"`), and stylesheet rule `before { display:none }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.lenis> — `deltacafes-com_en`)` (`deltacafes-com_en`) adapts across `@media only screen and (min-width:2000px)`, `@media only screen and (max-width:1023px)`, `@media only screen and (max-width:1290px)`, `@media only screen and (max-width:743px)` with `cubic-bezier(.19,1,.22,1)`, `cubic-bezier(.165,.84,.44,1)`, `cubic-bezier(.77,0,.175,1)` transitions and links `About Delta · The Azores Coffee · Products · The coffee cycle · Delta Sustainability`.
2. **Hero Stage & Focal Lead (<section.main> — `Delta, coffee with heart.`)**:
   - DOM & Selectors: Landmark `<section class="main">` presenting display lead `Delta, coffee with heart.` and copy excerpt *"coffee that awakens"* over `#2b1b14` canvas and `#fcf3ed` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×844px` mobile) sets `#2b1b14` background with `#fcf3ed` headline `Delta, coffee with heart.`.
3. **Primary Showcase & Content Grid (<section.scroller> — `Since 1961, coffee that awakens st`)**:
   - DOM & Selectors: Landmark `<section class="scroller">` rendering section `Since 1961, coffee that awakens stories` with copy *"Delta Cafés was born in Campo Maior from a family’s dream. Today,"*, asset references (`entry.DAMcazEw.css`, `Footer.BmMrv4ac.css`, `TransitionLogoMask.DT4Lfp-V.css`, `TagFlag.BCy09Tyz.css`), and grid rule `video { width:100%;height:100%;-o-object-fit:cover;object-fit:cover }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.scroller> — `Since 1961, coffee that awakens st`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 21.784px`) on desktop and Single-column vertical stack at `390px` viewport width with `.68vw` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.is-ready> — `The journey of coffee`)**:
   - DOM & Selectors: Landmark `<section class="is-ready">` framing `The journey of coffee` and `The Culture of Coffee` (*"1986 Start of activity in Spain"*) with `#000000` surface cards, `#f7a200` accents, and `after { bottom:1px;background:0000004d }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.is-ready> — `The journey of coffee`)` uses `8px`, `3px`, `1px`, `5px` radii, `#f7a200` highlights, and assets (entry.DAMcazEw.css, Footer.BmMrv4ac.css, TransitionLogoMask.DT4Lfp-V.css).
5. **Colophon & Global Directory Footer (<footer.bg-mask-defs> — `https://deltacafes.com/en`)**:
   - DOM & Selectors: Landmark `<footer class="bg-mask-defs">` anchoring `Delta, coffee with heart · Delta` footer links (`About Delta · The Azores Coffee · Products · The coffee cycle · Delta Sustainability`), copy *"Start of activity in Spain"*, and `#cccccc` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.bg-mask-defs> — `https://deltacafes.com/en`)` aligns to `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport) with `.68vw` lateral canvas padding with `21.784px` grid gap and attributes (data-website-id="0f29d428-885f-44b8-ae...", data-onload, data-onerror).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"coffee that awakens"*
- Copy Excerpt 2: *"Delta Cafés was born in Campo Maior from a family’s dream. Today, it is part of th..."*
- Copy Excerpt 3: *"1986 Start of activity in Spain"*
- Copy Excerpt 4: *"Start of activity in Spain"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.19,1,.22,1)`, `cubic-bezier(.165,.84,.44,1)`, `cubic-bezier(.77,0,.175,1)`
- **Extracted Stylesheet Rules (`deltacafes-com_en`)**:
- `before { display:none }`
- `video { width:100%;height:100%;-o-object-fit:cover;object-fit:cover }`
- `after { bottom:1px;background:0000004d }`
- `path { fill:var(--color-creme-100) }`
- `a:before { content:"";position:absolute;left:-10px;top:-10px;width:calc(100% + 20px... }`
- **Per-Selector Transition Rules**:
- **Selector `-component=popup] .content[data-v...`**: `transition: height .5s cubic-bezier(.19,1,.22,1),width .5s cubic-bezier(.1...` extracted from `deltacafes-com_en` stylesheet.
- **Selector `nent=popup] .content .item[data-v...`**: `transition: opacity .5s cubic-bezier(.19,1,.22,1),transform .5s cubic-bezi...` extracted from `deltacafes-com_en` stylesheet.
- **Selector `.group-title-wrapper .icon[data-v...`**: `transition: transform .75s cubic-bezier(.19,1,.22,1)` extracted from `deltacafes-com_en` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.19,1,.22,1)`)**: Governs interactive state transitions across `<header.lenis>` and `<section.scroller>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `deltacafes-com_en`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
