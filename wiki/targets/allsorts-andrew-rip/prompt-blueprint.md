---
title: "UI Prompt Blueprint: allsorts-andrew-rip"
date: 2026-11-15
target: "[[overview|allsorts-andrew-rip]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#888`)"
---

# UI Design System & Master Generation Blueprint: allsorts-andrew-rip

> **Allsorts · Andrew Robinson** (https://allsorts.andrew.rip) — Liquorice allsorts to throw, pile and frame, rendered in your browser. Save one as a wallpaper. By Andrew Robinson.

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Allsorts · Andrew Robinson** (`https://allsorts.andrew.rip`). Liquorice allsorts to throw, pile and frame, rendered in your browser. Save one as a wallpaper. By Andrew Robinson.
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#888`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`body { background: #000 }`) paired with `#fff` primary typography and `#888` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Soehne` for display copy (`Allsorts · Andrew Robinson`) with `Tiempos Fine` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `460px` container bounds (`gap: 12px`, padding `8px`) with `cubic-bezier(0.25,0.1,0.25,1)` easing and HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `460px` extracted from `allsorts-andrew-rip` stylesheet.
- **Canvas Lateral Padding & Spacing**: `8px` lateral canvas padding with `12px` grid gap.
- **Border Radius Scale**: `6px`, `4px`, `1px`, `50%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 460px`, `gap: 12px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `8px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (width<=480px)`, `@media (width<=640px),(pointer:coarse) and (height<=500px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `body { background: #000 }` |
| **Primary Typography Ink** | `#ddd` | `.hud.svelte-qxof8p { color: #ddd }` |
| **Elevated Surface / Card Substrate** | `#fff` | `.big.svelte-qxof8p { color: #fff }` |
| **Interactive Accent / Highlight** | `#888` | `.dim.svelte-qxof8p { color: #888 }` |
| **Secondary / Muted Copy** | `#777` | `.dim.svelte-1tmptad { color: #777 }` |
| **Structural Hairline Border** | `#999` | `.quiet.svelte-1yxt74e { color: #999 }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--size` | `48px` | Layout / Spatial Grid Token |
| `--allsorts-andrew--bg` | `#000` | Canvas Substrate (from `body { background: #000 }`) |
| `--allsorts-andrew--ink` | `#fff` | Primary Typography Ink (stylesheet-derived) |
| `--allsorts-andrew--surface` | `#fff` | Surface Substrate (stylesheet-derived) |
| `--allsorts-andrew--accent` | `#888` | Interactive Accent (stylesheet-derived) |
| `--allsorts-andrew--muted` | `#777` | Secondary Ink (stylesheet-derived) |
| `--allsorts-andrew--border` | `#999` | Structural Border (stylesheet-derived) |
| `--allsorts-andrew--container` | `460px` | Container Bound (stylesheet-derived) |
| `--allsorts-andrew--gap` | `12px` | Grid Gutter (stylesheet-derived) |
| `--allsorts-andrew--pad` | `8px` | Lateral Padding (stylesheet-derived) |
| `--allsorts-andrew--ease` | `cubic-bezier(0.25,0.1,0.25,1)` | Primary Easing Function |
| `--allsorts-andrew--radius` | `6px` | Corner Radius (stylesheet-derived) |
| `--allsorts-andrew--fs-base` | `13px` | Observed Font Size Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Soehne`.
- **Primary Body Stack**: `Tiempos Fine`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `12px`, `16px`, `14px`, `11px`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `12px`, `16px`, `14px`, `11px`).
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `12px`, `16px`, `14px`, `11px`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `12px`, `16px`, `14px`, `11px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `button.svelte-hg5siv`**: `transition: opacity .2s` extracted from `allsorts-andrew-rip` stylesheet.
- **Selector `.lens.svelte-11id0ew`**: `transition: left .25s,top .25s` extracted from `allsorts-andrew-rip` stylesheet.
- **Selector `.close.svelte-11id0ew`**: `transition: left .25s,top .25s` extracted from `allsorts-andrew-rip` stylesheet.
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in static CSS).
- **Runtime Interaction Engine**: Integrates HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Allsorts · Andrew Robinson                 │
│ ====================================================================== │
│ [ <header.stage>           | Andrew Robinson                        ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <div.svelte-1pzb9eq>                                 |   │
│ | H1: Allsorts · Andrew Robinson                                   |   │
│ | Substrate: #000       | Ink: #fff       | Accent: #888           |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<div.light>               ) max-w: 460px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Featured Work & Interactive  |  | Technical Architecture & Nar | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 12px  ) | │
│ | [<header.stage>] -> [<div.svelte-1pzb9e] -> [<div.light>] |          │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.words>        ) | https://allsorts.andrew.rip        │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.stage> — `allsorts-andrew-rip`)**:
   - Landmark `<header class="stage">` hosting `Allsorts · Andrew Robinson` navigation (`Andrew Robinson`), DOM attributes (`data-website-id="ffd157e7-cca9-4ad9-ad..."`, `data-domains="allsorts.andrew.rip"`, `data-auto-track="true"`, `data-auto-pageview="false"`), and stylesheet rule `font-face { font-family:Soehne;src:url(../../../fonts/soehne-leicht.woff2)format("wo... }`.
2. **Hero Stage & Focal Lead (<div.svelte-1pzb9eq> — `Allsorts · Andrew Robinson`)**:
   - Landmark `<div class="svelte-1pzb9eq">` presenting display lead `Allsorts · Andrew Robinson` and copy excerpt *"Allsorts Andrew Robinson"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<div.light> — `Featured Work & Interactive Showca`)**:
   - Landmark `<div class="light">` rendering section `Featured Work & Interactive Showcase` with copy *"Liquorice allsorts to throw, pile and frame, rendered on your gra"*, asset references (`start.ChVgNEA1.js`, `payload.DSmR2FwN.js`, `CRzLMJPS.js`, `CKKoTArS.js`), and grid rule `body { overscroll-behavior:none;background:000;margin:0 }`.
4. **Interactive Detail & Feature Matrix (<div.fallback> — `Technical Architecture & Narrative`)**:
   - Landmark `<div class="fallback">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Open it in the latest Chrome, Edge or Safari. In an app? Open it "*) with `#fff` surface cards, `#888` accents, and `.row.svelte-qxof8p { justify-content:space-between;gap:12px;display:flex }`.
5. **Colophon & Global Directory Footer (<footer.words> — `https://allsorts.andrew.rip`)**:
   - Landmark `<footer class="words">` anchoring `Allsorts · Andrew Robinson` footer links (`Andrew Robinson`), copy *"Technical Architecture & Narrative"*, and `#999` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: allsorts-andrew-rip (Allsorts · Andrew Robinson)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `allsorts-andrew-rip` (**Allsorts · Andrew Robinson** — `https://allsorts.andrew.rip`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#888`).
- **Identity & Domain Context**: Liquorice allsorts to throw, pile and frame, rendered in your browser. Save one as a wallpaper. By Andrew Robinson.
- **Primary Substrate**: `#000` (`body { background: #000 }`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#888`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`body { background: #000 }`) paired with `#fff` primary typography and `#888` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Soehne` for display copy (`Allsorts · Andrew Robinson`) with `Tiempos Fine` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `460px` container bounds (`gap: 12px`, padding `8px`) with `cubic-bezier(0.25,0.1,0.25,1)` easing and HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `allsorts-andrew-rip` in your global stylesheet:

:root {
  /* Allsorts · Andrew Robinson (allsorts-andrew-rip) — Ground-Truth Extracted CSS Variables */
  --size: 48px; /* Layout / Spatial Grid Token (allsorts-andrew-rip) */
  --allsorts-andrew--bg: #000; /* Canvas Substrate (from `body { background: #000 }`) (allsorts-andrew-rip) */
  --allsorts-andrew--ink: #fff; /* Primary Typography Ink (stylesheet-derived) (allsorts-andrew-rip) */
  --allsorts-andrew--surface: #fff; /* Surface Substrate (stylesheet-derived) (allsorts-andrew-rip) */
  --allsorts-andrew--accent: #888; /* Interactive Accent (stylesheet-derived) (allsorts-andrew-rip) */
  --allsorts-andrew--muted: #777; /* Secondary Ink (stylesheet-derived) (allsorts-andrew-rip) */
  --allsorts-andrew--border: #999; /* Structural Border (stylesheet-derived) (allsorts-andrew-rip) */
  --allsorts-andrew--container: 460px; /* Container Bound (stylesheet-derived) (allsorts-andrew-rip) */
  --allsorts-andrew--gap: 12px; /* Grid Gutter (stylesheet-derived) (allsorts-andrew-rip) */
  --allsorts-andrew--pad: 8px; /* Lateral Padding (stylesheet-derived) (allsorts-andrew-rip) */
  --allsorts-andrew--ease: cubic-bezier(0.25,0.1,0.25,1); /* Primary Easing Function (allsorts-andrew-rip) */
  --allsorts-andrew--radius: 6px; /* Corner Radius (stylesheet-derived) (allsorts-andrew-rip) */
  --allsorts-andrew--fs-base: 13px; /* Observed Font Size Token (allsorts-andrew-rip) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000` — grounded in `body { background: #000 }`
- **Primary Typography Ink**: `#ddd` — grounded in `.hud.svelte-qxof8p { color: #ddd }`
- **Elevated Surface / Card Substrate**: `#fff` — grounded in `.big.svelte-qxof8p { color: #fff }`
- **Interactive Accent / Highlight**: `#888` — grounded in `.dim.svelte-qxof8p { color: #888 }`
- **Secondary / Muted Copy**: `#777` — grounded in `.dim.svelte-1tmptad { color: #777 }`
- **Structural Hairline Border**: `#999` — grounded in `.quiet.svelte-1yxt74e { color: #999 }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `460px` extracted from `allsorts-andrew-rip` stylesheet
- **Padding & Gutters**: `8px` lateral canvas padding with `12px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 460px`, `gap: 12px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `8px` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (width<=480px)`, `@media (width<=640px),(pointer:coarse) and (height<=500px)`
- **Corner Radii**: `6px`, `4px`, `1px`, `50%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Soehne`
- **Body Font Stack**: `Tiempos Fine`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `12px`, `16px`, `14px`, `11px`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `12px`, `16px`, `14px`, `11px`)
- **Body Copy Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `12px`, `16px`, `14px`, `11px`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `12px`, `16px`, `14px`, `11px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `allsorts-andrew-rip` (`Allsorts · Andrew Robinson`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.stage> — `allsorts-andrew-rip`)**:
   - DOM & Selectors: Landmark `<header class="stage">` hosting `Allsorts · Andrew Robinson` navigation (`Andrew Robinson`), DOM attributes (`data-website-id="ffd157e7-cca9-4ad9-ad..."`, `data-domains="allsorts.andrew.rip"`, `data-auto-track="true"`, `data-auto-pageview="false"`), and stylesheet rule `font-face { font-family:Soehne;src:url(../../../fonts/soehne-leicht.woff2)format("wo... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.stage> — `allsorts-andrew-rip`)` (`allsorts-andrew-rip`) adapts across `@media (prefers-reduced-motion:reduce)`, `@media (width<=480px)`, `@media (width<=640px),(pointer:coarse) and (height<=500px)` with `cubic-bezier(0.25,0.1,0.25,1)` transitions and links `Andrew Robinson`.
2. **Hero Stage & Focal Lead (<div.svelte-1pzb9eq> — `Allsorts · Andrew Robinson`)**:
   - DOM & Selectors: Landmark `<div class="svelte-1pzb9eq">` presenting display lead `Allsorts · Andrew Robinson` and copy excerpt *"Allsorts Andrew Robinson"* over `#000` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#000` background with `#fff` headline `Allsorts · Andrew Robinson`.
3. **Primary Showcase & Content Grid (<div.light> — `Featured Work & Interactive Showca`)**:
   - DOM & Selectors: Landmark `<div class="light">` rendering section `Featured Work & Interactive Showcase` with copy *"Liquorice allsorts to throw, pile and frame, rendered on your gra"*, asset references (`start.ChVgNEA1.js`, `payload.DSmR2FwN.js`, `CRzLMJPS.js`, `CKKoTArS.js`), and grid rule `body { overscroll-behavior:none;background:000;margin:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<div.light> — `Featured Work & Interactive Showca`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 460px`, `gap: 12px`) on desktop and Single-column vertical stack at `390px` viewport width with `8px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<div.fallback> — `Technical Architecture & Narrative`)**:
   - DOM & Selectors: Landmark `<div class="fallback">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Open it in the latest Chrome, Edge or Safari. In an app? Open it "*) with `#fff` surface cards, `#888` accents, and `.row.svelte-qxof8p { justify-content:space-between;gap:12px;display:flex }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<div.fallback> — `Technical Architecture & Narrative`)` uses `6px`, `4px`, `1px`, `50%` radii, `#888` highlights, and assets (start.ChVgNEA1.js, payload.DSmR2FwN.js, CRzLMJPS.js).
5. **Colophon & Global Directory Footer (<footer.words> — `https://allsorts.andrew.rip`)**:
   - DOM & Selectors: Landmark `<footer class="words">` anchoring `Allsorts · Andrew Robinson` footer links (`Andrew Robinson`), copy *"Technical Architecture & Narrative"*, and `#999` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.words> — `https://allsorts.andrew.rip`)` aligns to `460px` extracted from `allsorts-andrew-rip` stylesheet with `8px` lateral canvas padding with `12px` grid gap and attributes (data-website-id="ffd157e7-cca9-4ad9-ad...", data-domains="allsorts.andrew.rip", data-auto-track="true").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Allsorts Andrew Robinson"*
- Copy Excerpt 2: *"Liquorice allsorts to throw, pile and frame, rendered on your graphics card. This..."*
- Copy Excerpt 3: *"Open it in the latest Chrome, Edge or Safari. In an app? Open it in your browser."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`
- **Extracted Stylesheet Rules (`allsorts-andrew-rip`)**:
- `font-face { font-family:Soehne;src:url(../../../fonts/soehne-leicht.woff2)format("wo... }`
- `body { overscroll-behavior:none;background:000;margin:0 }`
- `.row.svelte-qxof8p { justify-content:space-between;gap:12px;display:flex }`
- `.big.svelte-qxof8p { color:fff;font-size:13px }`
- `.total.svelte-qxof8p { border-top:1px solid ffffff26;margin-top:2px;padding-top:2px }`
- **Per-Selector Transition Rules**:
- **Selector `button.svelte-hg5siv`**: `transition: opacity .2s` extracted from `allsorts-andrew-rip` stylesheet.
- **Selector `.lens.svelte-11id0ew`**: `transition: left .25s,top .25s` extracted from `allsorts-andrew-rip` stylesheet.
- **Selector `.close.svelte-11id0ew`**: `transition: left .25s,top .25s` extracted from `allsorts-andrew-rip` stylesheet.
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in static CSS).
- **Runtime Interaction Engine**: Integrates HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `allsorts-andrew-rip`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
