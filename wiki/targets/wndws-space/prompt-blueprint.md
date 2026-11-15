---
title: "UI Prompt Blueprint: wndws-space"
date: 2026-11-15
target: "[[overview|wndws-space]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#dcdcdc` / `#000`)"
---

# UI Design System & Master Generation Blueprint: wndws-space

> **windows · place is temporary. you are not.** (https://wndws.space/) — Upload your window — tell what chapter of life you're living through.

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **windows · place is temporary. you are not.** (`https://wndws.space/`). Upload your window — tell what chapter of life you're living through.
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#dcdcdc` / `#000`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#dcdcdc` (`html::-webkit-scrollbar-thumb { background: #dcdcdc }`) paired with `#000` primary typography and `#000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Inter` for display copy (`windows · place is temporary. you ar`) with `Times New Roman` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `700px` container bounds (`gap: 34px`, padding `9px`) with `cubic-bezier(.22,1,.36,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `700px` extracted from `wndws-space` stylesheet.
- **Canvas Lateral Padding & Spacing**: `9px` lateral canvas padding with `34px` grid gap.
- **Border Radius Scale**: `999px`, `2px`, `6px`, `5px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 700px`, `gap: 34px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:700px)`, `@media (max-width:900px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:430px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#dcdcdc` | `html::-webkit-scrollbar-thumb { background: #dcdcdc }` |
| **Primary Typography Ink** | `#cacaca` | `html::-webkit-scrollbar-thumb { border: #cacaca }` |
| **Elevated Surface / Card Substrate** | `#fff` | `tml.prelude-route::-webkit-scro... { border-color: #fff }` |
| **Interactive Accent / Highlight** | `#000` | `::-moz-selection { color: #000 }` |
| **Secondary / Muted Copy** | `#d9d9d9` | `::-webkit-scrollbar-thumb { background: #d9d9d9 }` |
| **Structural Hairline Border** | `#c9c9c9` | `::-webkit-scrollbar-thumb:hover { background: #c9c9c9 }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--text-reveal-duration` | `.92s` | Typography Ink Token |
| `--text-reveal-ease` | `cubic-bezier(.22,1,.36,1)` | Typography Ink Token |
| `--frame` | `10px` | Dimension / Scale Token |
| `--frame-radius` | `6px` | Elevation / Border Token |
| `--nav-drop` | `8px` | Layout / Spatial Grid Token |
| `--fr` | `var(--frame-radius)` | Dimension / Scale Token |
| `--edge` | `linear-gradient(#000,#000)` | Color / Atmospheric Token |
| `--band` | `10px` | Dimension / Scale Token |
| `--logo-h` | `25px` | Dimension / Scale Token |
| `--lift` | `0px` | Dimension / Scale Token |
| `--slide` | `-7px` | Dimension / Scale Token |
| `--tilt` | `-2.5deg` | Design System Custom Token |
| `--teaser-i` | `0` | Motion / Easing Token |
| `--wndws-space-bg` | `#dcdcdc` | Canvas Substrate (from `html::-webkit-scrollbar-thumb { background: #dcdcdc }`) |
| `--wndws-space-ink` | `#000` | Primary Typography Ink (stylesheet-derived) |
| `--wndws-space-surface` | `#fff` | Surface Substrate (stylesheet-derived) |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Inter`.
- **Primary Body Stack**: `Times New Roman`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `64px`, `24px`, `20px`, `13px`, `40px`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `64px`, `24px`, `20px`, `13px`, `40px`).
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `64px`, `24px`, `20px`, `13px`, `40px`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `64px`, `24px`, `20px`, `13px`, `40px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.4,0,.4,1)`, `cubic-bezier(.34,1.4,.5,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.slide-label-face`**: `transition: transform .34s cubic-bezier(.22,1,.36,1)` extracted from `wndws-space` stylesheet.
- **Selector `.route-outgoing.up.closing[data-v...`**: `transition: opacity .45s cubic-bezier(.22,1,.36,1)` extracted from `wndws-space` stylesheet.
- **Selector `media(prefers-reduced-motion:reduce)`**: `transition: 1ms` extracted from `wndws-space` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,1,.36,1)`)**: Governs interactive state transitions across `<nav.nav>` and `<div.nuxt-route-announcer>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — windows · place is temporary. you are not. │
│ ====================================================================== │
│ [ <nav.nav>                | prelude prelude                        ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <div.custom-cursor-enabled>                          |   │
│ | H1: windows · place is temporary. you are not.                   |   │
│ | Substrate: #dcdcdc    | Ink: #000       | Accent: #000           |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<div.nuxt-route-announcer>) max-w: 700px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Featured Work & Interactive  |  | Technical Architecture & Nar | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 34px  ) | │
│ | [<nav.nav>] -> [<div.custom-cursor] -> [<div.nuxt-route-an] |        │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer>  ) | https://wndws.space/               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.nav> — `wndws-space`)**:
   - Landmark `<nav class="nav">` hosting `windows · place is temporary. you ar` navigation (`prelude prelude`), DOM attributes (`data-v-20a15833`, `data-v-e0841100`, `data-v-feaf1087`, `data-v-217c40e4`), and stylesheet rule `before { box-sizing:border-box;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<div.custom-cursor-enabled> — `windows · place is temporary. you `)**:
   - Landmark `<div class="custom-cursor-enabled">` presenting display lead `windows · place is temporary. you are not.` and copy excerpt *"windows · place is temporary. you are not."* over `#dcdcdc` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<div.nuxt-route-announcer> — `Featured Work & Interactive Showca`)**:
   - Landmark `<div class="nuxt-route-announcer">` rendering section `Featured Work & Interactive Showcase` with copy *"𝕲𝖊𝖔𝖗𝖌𝖎𝖔 𝕲𝖔𝖌𝖆𝖓𝖓𝖎 — Tbilisi, Georgia"*, asset references (`fonts.googleapis.com`, `fonts.gstatic.com`, `css2`, `entry.DtyUHzly.css`), and grid rule `html::-webkit-scrollbar { width:10px }`.
4. **Interactive Detail & Feature Matrix (<div.route-stage> — `Technical Architecture & Narrative`)**:
   - Landmark `<div class="route-stage">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Rita — Moscow, Russia"*) with `#fff` surface cards, `#000` accents, and `html::-webkit-scrollbar-track { background:transparent }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://wndws.space/`)**:
   - Landmark `<footer class="site-footer">` anchoring `windows · place is temporary. yo` footer links (`prelude prelude`), copy *"Andrey — Marseille, France"*, and `#c9c9c9` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: wndws-space (windows · place is temporary. you are not.)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `wndws-space` (**windows · place is temporary. you are not.** — `https://wndws.space/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#dcdcdc` / `#000`).
- **Identity & Domain Context**: Upload your window — tell what chapter of life you're living through.
- **Primary Substrate**: `#dcdcdc` (`html::-webkit-scrollbar-thumb { background: #dcdcdc }`), **Primary Ink**: `#000`, **Accent / Highlight**: `#000`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#dcdcdc` (`html::-webkit-scrollbar-thumb { background: #dcdcdc }`) paired with `#000` primary typography and `#000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Inter` for display copy (`windows · place is temporary. you ar`) with `Times New Roman` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `700px` container bounds (`gap: 34px`, padding `9px`) with `cubic-bezier(.22,1,.36,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `wndws-space` in your global stylesheet:

:root {
  /* windows · place is temporary. you are not. (wndws-space) — Ground-Truth Extracted CSS Variables */
  --text-reveal-duration: .92s; /* Typography Ink Token (wndws-space) */
  --text-reveal-ease: cubic-bezier(.22,1,.36,1); /* Typography Ink Token (wndws-space) */
  --frame: 10px; /* Dimension / Scale Token (wndws-space) */
  --frame-radius: 6px; /* Elevation / Border Token (wndws-space) */
  --nav-drop: 8px; /* Layout / Spatial Grid Token (wndws-space) */
  --fr: var(--frame-radius); /* Dimension / Scale Token (wndws-space) */
  --edge: linear-gradient(#000,#000); /* Color / Atmospheric Token (wndws-space) */
  --band: 10px; /* Dimension / Scale Token (wndws-space) */
  --logo-h: 25px; /* Dimension / Scale Token (wndws-space) */
  --lift: 0px; /* Dimension / Scale Token (wndws-space) */
  --slide: -7px; /* Dimension / Scale Token (wndws-space) */
  --tilt: -2.5deg; /* Design System Custom Token (wndws-space) */
  --teaser-i: 0; /* Motion / Easing Token (wndws-space) */
  --wndws-space-bg: #dcdcdc; /* Canvas Substrate (from `html::-webkit-scrollbar-thumb { background: #dcdcdc }`) (wndws-space) */
  --wndws-space-ink: #000; /* Primary Typography Ink (stylesheet-derived) (wndws-space) */
  --wndws-space-surface: #fff; /* Surface Substrate (stylesheet-derived) (wndws-space) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#dcdcdc` — grounded in `html::-webkit-scrollbar-thumb { background: #dcdcdc }`
- **Primary Typography Ink**: `#cacaca` — grounded in `html::-webkit-scrollbar-thumb { border: #cacaca }`
- **Elevated Surface / Card Substrate**: `#fff` — grounded in `tml.prelude-route::-webkit-scro... { border-color: #fff }`
- **Interactive Accent / Highlight**: `#000` — grounded in `::-moz-selection { color: #000 }`
- **Secondary / Muted Copy**: `#d9d9d9` — grounded in `::-webkit-scrollbar-thumb { background: #d9d9d9 }`
- **Structural Hairline Border**: `#c9c9c9` — grounded in `::-webkit-scrollbar-thumb:hover { background: #c9c9c9 }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `700px` extracted from `wndws-space` stylesheet
- **Padding & Gutters**: `9px` lateral canvas padding with `34px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 700px`, `gap: 34px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding
- **Media Queries**: `@media (max-width:700px)`, `@media (max-width:900px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:430px)`
- **Corner Radii**: `999px`, `2px`, `6px`, `5px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Times New Roman`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `64px`, `24px`, `20px`, `13px`, `40px`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `64px`, `24px`, `20px`, `13px`, `40px`)
- **Body Copy Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `64px`, `24px`, `20px`, `13px`, `40px`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `64px`, `24px`, `20px`, `13px`, `40px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `wndws-space` (`windows · place is temporary. you are not.`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.nav> — `wndws-space`)**:
   - DOM & Selectors: Landmark `<nav class="nav">` hosting `windows · place is temporary. you ar` navigation (`prelude prelude`), DOM attributes (`data-v-20a15833`, `data-v-e0841100`, `data-v-feaf1087`, `data-v-217c40e4`), and stylesheet rule `before { box-sizing:border-box;margin:0;padding:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.nav> — `wndws-space`)` (`wndws-space`) adapts across `@media (max-width:700px)`, `@media (max-width:900px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:430px)` with `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.4,0,.4,1)`, `cubic-bezier(.34,1.4,.5,1)` transitions and links `prelude prelude`.
2. **Hero Stage & Focal Lead (<div.custom-cursor-enabled> — `windows · place is temporary. you `)**:
   - DOM & Selectors: Landmark `<div class="custom-cursor-enabled">` presenting display lead `windows · place is temporary. you are not.` and copy excerpt *"windows · place is temporary. you are not."* over `#dcdcdc` canvas and `#000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#dcdcdc` background with `#000` headline `windows · place is temporary. you are not.`.
3. **Primary Showcase & Content Grid (<div.nuxt-route-announcer> — `Featured Work & Interactive Showca`)**:
   - DOM & Selectors: Landmark `<div class="nuxt-route-announcer">` rendering section `Featured Work & Interactive Showcase` with copy *"𝕲𝖊𝖔𝖗𝖌𝖎𝖔 𝕲𝖔𝖌𝖆𝖓𝖓𝖎 — Tbilisi, Georgia"*, asset references (`fonts.googleapis.com`, `fonts.gstatic.com`, `css2`, `entry.DtyUHzly.css`), and grid rule `html::-webkit-scrollbar { width:10px }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<div.nuxt-route-announcer> — `Featured Work & Interactive Showca`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 700px`, `gap: 34px`) on desktop and Single-column vertical stack at `390px` viewport width with `9px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<div.route-stage> — `Technical Architecture & Narrative`)**:
   - DOM & Selectors: Landmark `<div class="route-stage">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Rita — Moscow, Russia"*) with `#fff` surface cards, `#000` accents, and `html::-webkit-scrollbar-track { background:transparent }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<div.route-stage> — `Technical Architecture & Narrative`)` uses `999px`, `2px`, `6px`, `5px` radii, `#000` highlights, and assets (fonts.googleapis.com, fonts.gstatic.com, css2).
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://wndws.space/`)**:
   - DOM & Selectors: Landmark `<footer class="site-footer">` anchoring `windows · place is temporary. yo` footer links (`prelude prelude`), copy *"Andrey — Marseille, France"*, and `#c9c9c9` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.site-footer> — `https://wndws.space/`)` aligns to `700px` extracted from `wndws-space` stylesheet with `9px` lateral canvas padding with `34px` grid gap and attributes (data-v-20a15833, data-v-e0841100, data-v-feaf1087).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"windows · place is temporary. you are not."*
- Copy Excerpt 2: *"𝕲𝖊𝖔𝖗𝖌𝖎𝖔 𝕲𝖔𝖌𝖆𝖓𝖓𝖎 — Tbilisi, Georgia"*
- Copy Excerpt 3: *"Rita — Moscow, Russia"*
- Copy Excerpt 4: *"Andrey — Marseille, France"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.4,0,.4,1)`, `cubic-bezier(.34,1.4,.5,1)`
- **Extracted Stylesheet Rules (`wndws-space`)**:
- `before { box-sizing:border-box;margin:0;padding:0 }`
- `html::-webkit-scrollbar { width:10px }`
- `html::-webkit-scrollbar-track { background:transparent }`
- `html::-webkit-scrollbar-thumb { background:dcdcdc;border-radius:999px;border:2px solid cacaca;background... }`
- `.prelude-route::-webkit-scrollbar... { border-color:fff }`
- **Per-Selector Transition Rules**:
- **Selector `.slide-label-face`**: `transition: transform .34s cubic-bezier(.22,1,.36,1)` extracted from `wndws-space` stylesheet.
- **Selector `.route-outgoing.up.closing[data-v...`**: `transition: opacity .45s cubic-bezier(.22,1,.36,1)` extracted from `wndws-space` stylesheet.
- **Selector `media(prefers-reduced-motion:reduce)`**: `transition: 1ms` extracted from `wndws-space` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,1,.36,1)`)**: Governs interactive state transitions across `<nav.nav>` and `<div.nuxt-route-announcer>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `wndws-space`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
