---
title: "UI Prompt Blueprint: www-raomuhammadhamza-tech"
date: 2026-11-15
target: "[[overview|www-raomuhammadhamza-tech]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#0f1220` / `#f4e7e2`)"
---

# UI Design System & Master Generation Blueprint: www-raomuhammadhamza-tech

> **Rao Muhammad Hamza, AI Engineer** (https://www.raomuhammadhamza.tech/) — Rao Muhammad Hamza, AI Engineer. RAG pipelines, LLM orchestration and agentic workflows, built to hold up in production.

![Desktop Viewport Capture (1440x10474)](file:///root/projects/fleet/wiki/targets/www-raomuhammadhamza-tech/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Rao Muhammad Hamza, AI Engineer** (`https://www.raomuhammadhamza.tech/`). Rao Muhammad Hamza, AI Engineer. RAG pipelines, LLM orchestration and agentic workflows, built to hold up in production.
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#0f1220` / `#f4e7e2`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#0f1220` (`var(--ink)` in `:root`) paired with `#f4e7e2` primary typography and `#f4e7e2` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Space Grotesk` for display copy (`R a o M u h a m m a d H a m z a`) with `Space Mono` and `Space Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `34ch` container bounds (`gap: 22px`, padding `13px`) with `cubic-bezier(.2,.7,.2,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/www-raomuhammadhamza-tech/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×10474px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `34ch` extracted from `www-raomuhammadhamza-tech` stylesheet.
- **Canvas Lateral Padding & Spacing**: `13px` lateral canvas padding with `22px` grid gap.
- **Border Radius Scale**: `var(--tv-radius)`, `50%`, `11px`, `8px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 34ch`, `gap: 22px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `13px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (width<=700px),(height<=500px)`, `@media (width<=480px)`, `@media (prefers-reduced-motion:reduce)`, `@media (width<=700px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0f1220` | `var(--ink)` in `:root` |
| **Primary Typography Ink** | `#ff9ebb` | `var(--screen)` in `:root` |
| **Elevated Surface / Card Substrate** | `#1b1f33` | `var(--screen-ink)` in `:root` |
| **Interactive Accent / Highlight** | `#f4e7e2` | `var(--text)` in `:root` |
| **Secondary / Muted Copy** | `#b9b2c4` | `var(--muted)` in `:root` |
| **Structural Hairline Border** | `#1a1a26` | `var(--d-surf)` in `:root` |
| **Variable Token (`--tv-edge`)** | `#ff9ebb33` | `var(--tv-edge)` in `:root` |
| **Variable Token (`--tv-bg`)** | `#161a30db` | `var(--tv-bg)` in `:root` |
| **Variable Token (`--tv-bg`)** | `#0c0e1ce6` | `var(--tv-bg)` in `:root` |
| **Variable Token (`--tv-glow`)** | `#ffffff08` | `var(--tv-glow)` in `:root` |
| **Variable Token (`--tv-glow`)** | `#ff9ebb12` | `var(--tv-glow)` in `:root` |
| **Variable Token (`--tv-glow`)** | `#00000073` | `var(--tv-glow)` in `:root` |
| **Variable Token (`--scan`)** | `#ffffff09` | `var(--scan)` in `:root` |
| **Variable Token (`--grid-line`)** | `#ffffff0f` | `var(--grid-line)` in `:root` |
| **Variable Token (`--d-surf2`)** | `#222232` | `var(--d-surf2)` in `:root` |
| **Variable Token (`--d-line`)** | `#ffffff14` | `var(--d-line)` in `:root` |
| **Variable Token (`--d-ink`)** | `#e9e3ef` | `var(--d-ink)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#0f1220` | Typography Ink Token |
| `--screen` | `#ff9ebb` | Color / Atmospheric Token |
| `--screen-ink` | `#1b1f33` | Typography Ink Token |
| `--text` | `#f4e7e2` | Typography Ink Token |
| `--muted` | `#b9b2c4` | Color / Atmospheric Token |
| `--tv-edge` | `#ff9ebb33` | Color / Atmospheric Token |
| `--tv-bg` | `linear-gradient(180deg, #161a30db, #0c0e1ce6)` | Canvas / Surface Token |
| `--tv-glow` | `inset 0 0 0 1px #ffffff08, inset 0 0 22px #ff9ebb12, 0 12px 40px #00000073` | Color / Atmospheric Token |
| `--scan` | `repeating-linear-gradient(0deg, #ffffff09 0 1px, transparent 1px 3px)` | Color / Atmospheric Token |
| `--tv-radius` | `12px` | Elevation / Border Token |
| `--grid-line` | `linear-gradient(#ffffff0f, #ffffff0f)` | Layout / Spatial Grid Token |
| `--sheet-bottom` | `84px` | Dimension / Scale Token |
| `--d-surf` | `#1a1a26` | Color / Atmospheric Token |
| `--d-surf2` | `#222232` | Color / Atmospheric Token |
| `--d-line` | `#ffffff14` | Color / Atmospheric Token |
| `--d-ink` | `#e9e3ef` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Space Grotesk`.
- **Primary Body Stack**: `Space Mono`.
- **Technical / Metadata Stack**: `Space Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `11px`, `12px`, `clamp(15px,1.45vw,21px)`, `19px`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `11px`, `12px`, `clamp(15px,1.45vw,21px)`, `19px`).
- **Body Copy**: rule `p` (`letter-spacing: .16em`).
- **Metadata & Navigation Labels**: CSS variables `--d-mono: "Space Mono", ui-monospace, monospace`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.2,.7,.2,1)`, `cubic-bezier(.65,0,.35,1)`, `cubic-bezier(.2,.8,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.loader`**: `transition: opacity .45s,visibility 0s .45s` extracted from `www-raomuhammadhamza-tech` stylesheet.
- **Selector `#awwwards`**: `transition: opacity .45s` extracted from `www-raomuhammadhamza-tech` stylesheet.
- **Selector `.enter button`**: `transition: background .2s,border-color .2s` extracted from `www-raomuhammadhamza-tech` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.2,.7,.2,1)`)**: Governs interactive state transitions across `<header.ui>` and `<article.case>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Rao Muhammad Hamza, AI Engineer            │
│ ====================================================================== │
│ [ <header.ui>              | Overview · Index · Archive · About · C ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.surface>                                    |   │
│ | H1: R a o M u h a m m a d H a m z a                              |   │
│ | Substrate: #0f1220    | Ink: #f4e7e2    | Accent: #f4e7e2        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<article.case>            ) max-w: 34ch           |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Projects                     |  | EDI                          | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 22px  ) | │
│ | [<header.ui>] -> [<section.surface>] -> [<article.case>] |           │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.train-chart>  ) | https://www.raomuhammadhamza.tech/ │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.ui> — `www-raomuhammadhamza-tech`)**:
   - Landmark `<header class="ui sig">` hosting `Rao Muhammad Hamza, AI Engineer` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-sound="on"`, `data-sound="off"`, `data-go="projects"`, `data-go="experience"`), and stylesheet rule `font-face { font-family:Space Mono;src:url(/fonts/SpaceMono-400.woff2)format("woff2"... }`.
2. **Hero Stage & Focal Lead (<section.surface> — `R a o M u h a m m a d H a m z a`)**:
   - Landmark `<section class="surface desk">` presenting display lead `R a o M u h a m m a d H a m z a` and copy excerpt *"$ python train.py --model hamza-1 --data ./room"* over `#0f1220` canvas and `#f4e7e2` ink.
3. **Primary Showcase & Content Grid (<article.case> — `Projects`)**:
   - Landmark `<article class="case">` rendering section `Projects` with copy *"step 0/6000 · 0.0k tok/s · gpu 0%"*, asset references (`favicon.svg`, `SpaceGrotesk-Variable.woff2`, `index.58LUSp4D.css`, `edi-poster.webp`), and grid rule `body { color:f4e7e2;background:0f1220;height:100%;font-family:Space Grotesk,sys... }`.
4. **Interactive Detail & Feature Matrix (<article.case> — `EDI`)**:
   - Landmark `<article class="case">` framing `EDI` and `ResumeWesume` (*"Drag to look around"*) with `#1b1f33` surface cards, `#f4e7e2` accents, and `.loader.done { opacity:0;visibility:hidden }`.
5. **Colophon & Global Directory Footer (<footer.train-chart> — `https://www.raomuhammadhamza.tech/`)**:
   - Landmark `<footer class="train-chart">` anchoring `Rao Muhammad Hamza, AI Engineer` footer links (`Overview · Index · Archive · About · Contact`), copy *"I build AI that ships."*, and `#1a1a26` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-raomuhammadhamza-tech (Rao Muhammad Hamza, AI Engineer)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-raomuhammadhamza-tech` (**Rao Muhammad Hamza, AI Engineer** — `https://www.raomuhammadhamza.tech/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0f1220` / `#f4e7e2`).
- **Identity & Domain Context**: Rao Muhammad Hamza, AI Engineer. RAG pipelines, LLM orchestration and agentic workflows, built to hold up in production.
- **Primary Substrate**: `#0f1220` (`var(--ink)` in `:root`), **Primary Ink**: `#f4e7e2`, **Accent / Highlight**: `#f4e7e2`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#0f1220` (`var(--ink)` in `:root`) paired with `#f4e7e2` primary typography and `#f4e7e2` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Space Grotesk` for display copy (`R a o M u h a m m a d H a m z a`) with `Space Mono` and `Space Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `34ch` container bounds (`gap: 22px`, padding `13px`) with `cubic-bezier(.2,.7,.2,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-raomuhammadhamza-tech` in your global stylesheet:

:root {
  /* Rao Muhammad Hamza, AI Engineer (www-raomuhammadhamza-tech) — Ground-Truth Extracted CSS Variables */
  --ink: #0f1220; /* Typography Ink Token (www-raomuhammadhamza-tech) */
  --screen: #ff9ebb; /* Color / Atmospheric Token (www-raomuhammadhamza-tech) */
  --screen-ink: #1b1f33; /* Typography Ink Token (www-raomuhammadhamza-tech) */
  --text: #f4e7e2; /* Typography Ink Token (www-raomuhammadhamza-tech) */
  --muted: #b9b2c4; /* Color / Atmospheric Token (www-raomuhammadhamza-tech) */
  --tv-edge: #ff9ebb33; /* Color / Atmospheric Token (www-raomuhammadhamza-tech) */
  --tv-bg: linear-gradient(180deg, #161a30db, #0c0e1ce6); /* Canvas / Surface Token (www-raomuhammadhamza-tech) */
  --tv-glow: inset 0 0 0 1px #ffffff08, inset 0 0 22px #ff9ebb12, 0 12px 40px #00000073; /* Color / Atmospheric Token (www-raomuhammadhamza-tech) */
  --scan: repeating-linear-gradient(0deg, #ffffff09 0 1px, transparent 1px 3px); /* Color / Atmospheric Token (www-raomuhammadhamza-tech) */
  --tv-radius: 12px; /* Elevation / Border Token (www-raomuhammadhamza-tech) */
  --grid-line: linear-gradient(#ffffff0f, #ffffff0f); /* Layout / Spatial Grid Token (www-raomuhammadhamza-tech) */
  --sheet-bottom: 84px; /* Dimension / Scale Token (www-raomuhammadhamza-tech) */
  --d-surf: #1a1a26; /* Color / Atmospheric Token (www-raomuhammadhamza-tech) */
  --d-surf2: #222232; /* Color / Atmospheric Token (www-raomuhammadhamza-tech) */
  --d-line: #ffffff14; /* Color / Atmospheric Token (www-raomuhammadhamza-tech) */
  --d-ink: #e9e3ef; /* Typography Ink Token (www-raomuhammadhamza-tech) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#0f1220` — grounded in `var(--ink)` in `:root`
- **Primary Typography Ink**: `#ff9ebb` — grounded in `var(--screen)` in `:root`
- **Elevated Surface / Card Substrate**: `#1b1f33` — grounded in `var(--screen-ink)` in `:root`
- **Interactive Accent / Highlight**: `#f4e7e2` — grounded in `var(--text)` in `:root`
- **Secondary / Muted Copy**: `#b9b2c4` — grounded in `var(--muted)` in `:root`
- **Structural Hairline Border**: `#1a1a26` — grounded in `var(--d-surf)` in `:root`
- **Variable Token (`--tv-edge`)**: `#ff9ebb33` — grounded in `var(--tv-edge)` in `:root`
- **Variable Token (`--tv-bg`)**: `#161a30db` — grounded in `var(--tv-bg)` in `:root`
- **Variable Token (`--tv-bg`)**: `#0c0e1ce6` — grounded in `var(--tv-bg)` in `:root`
- **Variable Token (`--tv-glow`)**: `#ffffff08` — grounded in `var(--tv-glow)` in `:root`
- **Variable Token (`--tv-glow`)**: `#ff9ebb12` — grounded in `var(--tv-glow)` in `:root`
- **Variable Token (`--tv-glow`)**: `#00000073` — grounded in `var(--tv-glow)` in `:root`
- **Variable Token (`--scan`)**: `#ffffff09` — grounded in `var(--scan)` in `:root`
- **Variable Token (`--grid-line`)**: `#ffffff0f` — grounded in `var(--grid-line)` in `:root`
- **Variable Token (`--d-surf2`)**: `#222232` — grounded in `var(--d-surf2)` in `:root`
- **Variable Token (`--d-line`)**: `#ffffff14` — grounded in `var(--d-line)` in `:root`
- **Variable Token (`--d-ink`)**: `#e9e3ef` — grounded in `var(--d-ink)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×10474px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `34ch` extracted from `www-raomuhammadhamza-tech` stylesheet
- **Padding & Gutters**: `13px` lateral canvas padding with `22px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 34ch`, `gap: 22px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `13px` horizontal padding
- **Media Queries**: `@media (width<=700px),(height<=500px)`, `@media (width<=480px)`, `@media (prefers-reduced-motion:reduce)`, `@media (width<=700px)`
- **Corner Radii**: `var(--tv-radius)`, `50%`, `11px`, `8px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Space Grotesk`
- **Body Font Stack**: `Space Mono`
- **Monospace / Technical Font Stack**: `Space Mono`
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `11px`, `12px`, `clamp(15px,1.45vw,21px)`, `19px`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `11px`, `12px`, `clamp(15px,1.45vw,21px)`, `19px`)
- **Body Copy Rule**: rule `p` (`letter-spacing: .16em`)
- **Metadata & Index Rule**: CSS variables `--d-mono: "Space Mono", ui-monospace, monospace`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-raomuhammadhamza-tech` (`Rao Muhammad Hamza, AI Engineer`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.ui> — `www-raomuhammadhamza-tech`)**:
   - DOM & Selectors: Landmark `<header class="ui sig">` hosting `Rao Muhammad Hamza, AI Engineer` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-sound="on"`, `data-sound="off"`, `data-go="projects"`, `data-go="experience"`), and stylesheet rule `font-face { font-family:Space Mono;src:url(/fonts/SpaceMono-400.woff2)format("woff2"... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.ui> — `www-raomuhammadhamza-tech`)` (`www-raomuhammadhamza-tech`) adapts across `@media (width<=700px),(height<=500px)`, `@media (width<=480px)`, `@media (prefers-reduced-motion:reduce)`, `@media (width<=700px)` with `cubic-bezier(.2,.7,.2,1)`, `cubic-bezier(.65,0,.35,1)`, `cubic-bezier(.2,.8,.2,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<section.surface> — `R a o M u h a m m a d H a m z a`)**:
   - DOM & Selectors: Landmark `<section class="surface desk">` presenting display lead `R a o M u h a m m a d H a m z a` and copy excerpt *"$ python train.py --model hamza-1 --data ./room"* over `#0f1220` canvas and `#f4e7e2` ink.
   - Responsive Contract: Hero stage (`1440×10474px` desktop / `390×2400px` mobile) sets `#0f1220` background with `#f4e7e2` headline `R a o M u h a m m a d H a m z a`.
3. **Primary Showcase & Content Grid (<article.case> — `Projects`)**:
   - DOM & Selectors: Landmark `<article class="case">` rendering section `Projects` with copy *"step 0/6000 · 0.0k tok/s · gpu 0%"*, asset references (`favicon.svg`, `SpaceGrotesk-Variable.woff2`, `index.58LUSp4D.css`, `edi-poster.webp`), and grid rule `body { color:f4e7e2;background:0f1220;height:100%;font-family:Space Grotesk,sys... }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<article.case> — `Projects`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 34ch`, `gap: 22px`) on desktop and Single-column vertical stack at `390px` viewport width with `13px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.case> — `EDI`)**:
   - DOM & Selectors: Landmark `<article class="case">` framing `EDI` and `ResumeWesume` (*"Drag to look around"*) with `#1b1f33` surface cards, `#f4e7e2` accents, and `.loader.done { opacity:0;visibility:hidden }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.case> — `EDI`)` uses `var(--tv-radius)`, `50%`, `11px`, `8px` radii, `#f4e7e2` highlights, and assets (favicon.svg, SpaceGrotesk-Variable.woff2, index.58LUSp4D.css).
5. **Colophon & Global Directory Footer (<footer.train-chart> — `https://www.raomuhammadhamza.tech/`)**:
   - DOM & Selectors: Landmark `<footer class="train-chart">` anchoring `Rao Muhammad Hamza, AI Engineer` footer links (`Overview · Index · Archive · About · Contact`), copy *"I build AI that ships."*, and `#1a1a26` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.train-chart> — `https://www.raomuhammadhamza.tech/`)` aligns to `34ch` extracted from `www-raomuhammadhamza-tech` stylesheet with `13px` lateral canvas padding with `22px` grid gap and attributes (data-sound="on", data-sound="off", data-go="projects").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"$ python train.py --model hamza-1 --data ./room"*
- Copy Excerpt 2: *"step 0/6000 · 0.0k tok/s · gpu 0%"*
- Copy Excerpt 3: *"Drag to look around"*
- Copy Excerpt 4: *"I build AI that ships."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.2,.7,.2,1)`, `cubic-bezier(.65,0,.35,1)`, `cubic-bezier(.2,.8,.2,1)`
- **Extracted Stylesheet Rules (`www-raomuhammadhamza-tech`)**:
- `font-face { font-family:Space Mono;src:url(/fonts/SpaceMono-400.woff2)format("woff2"... }`
- `body { color:f4e7e2;background:0f1220;height:100%;font-family:Space Grotesk,sys... }`
- `.loader.done { opacity:0;visibility:hidden }`
- `awwwards { transition:opacity .45s }`
- `.loader:after { content:"";background:var(--scan);pointer-events:none;position:absolute;... }`
- **Per-Selector Transition Rules**:
- **Selector `.loader`**: `transition: opacity .45s,visibility 0s .45s` extracted from `www-raomuhammadhamza-tech` stylesheet.
- **Selector `#awwwards`**: `transition: opacity .45s` extracted from `www-raomuhammadhamza-tech` stylesheet.
- **Selector `.enter button`**: `transition: background .2s,border-color .2s` extracted from `www-raomuhammadhamza-tech` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.2,.7,.2,1)`)**: Governs interactive state transitions across `<header.ui>` and `<article.case>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-raomuhammadhamza-tech`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
