---
title: "UI Prompt Blueprint: www-raomuhammadhamza-tech"
date: 2026-11-24
captured_at: 2026-11-24
target: "www-raomuhammadhamza-tech"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
capture_mode: behavioral_journey_v2
asset_format: webp
scroll_driver: native
desktop_keyframes: 8
subpages_crawled: 0
http_status: 200
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#0f1220` / `#ff9ebb`)"
---

# UI Design System & Master Generation Blueprint: www-raomuhammadhamza-tech

> **Rao Muhammad Hamza, AI Engineer** (https://www.raomuhammadhamza.tech/) — Rao Muhammad Hamza, AI Engineer. RAG pipelines, LLM orchestration and agentic workflows, built to hold up in production.

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Rao Muhammad Hamza, AI Engineer** (`https://www.raomuhammadhamza.tech/`). Rao Muhammad Hamza, AI Engineer. RAG pipelines, LLM orchestration and agentic workflows, built to hold up in production.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#0f1220` / `#ff9ebb`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#0f1220` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#f4e7e2` primary typography and `#ff9ebb` accents.
  - **Grounded Typographic Hierarchy**: Uses `Space Grotesk` across display (`R A O M U H A M M A D H A M Z A`) and body copy, paired with `Space Mono` for monospace/code.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 14px`, padding `20px`) with `cubic-bezier(.2,.7,.2,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=9830px` / doc `10730px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport).
- **Canvas Lateral Padding & Spacing**: `20px` lateral canvas padding with `14px` grid gap.
- **Border Radius Scale**: `8px`, `var(--tv-radius)`, `50%`, `11px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 14px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `20px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (width<=700px),(height<=500px)`, `@media (width<=480px)`, `@media (prefers-reduced-motion:reduce)`, `@media (width<=700px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0f1220` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f4e7e2` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#0b0e17` | `.surface { background: #0b0e17 }` |
| **Interactive Accent / Highlight** | `#ff9ebb` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#b9b2c4` | `var(--muted)` in `:root` |
| **Structural Hairline Border** | `#1d202d` | `var(--grid-line)` in `:root` (`linear-gradient(ffffff0f, ffffff0f)`) |
| **Variable Token (`--screen-ink`)** | `#1b1f33` | `var(--screen-ink)` in `:root` |
| **Variable Token (`--tv-bg`)** | `#161a30` | `var(--tv-bg)` in `:root` |
| **Variable Token (`--tv-bg`)** | `#0c0e1c` | `var(--tv-bg)` in `:root` |
| **Variable Token (`--tv-glow`)** | `#ffffff` | `var(--tv-glow)` in `:root` |
| **Variable Token (`--tv-glow`)** | `#000000` | `var(--tv-glow)` in `:root` |
| **Variable Token (`--d-surf`)** | `#1a1a26` | `var(--d-surf)` in `:root` |
| **Variable Token (`--d-surf2`)** | `#222232` | `var(--d-surf2)` in `:root` |
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
- **Primary Body Stack**: `Space Grotesk`.
- **Technical / Metadata Stack**: `Space Mono`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 56px`, `line-height: 50.4px`, `font-weight: 700`, `letter-spacing: -1.96px`).
- **Section Heading (`H2`)**: live computed `h3 (primary section heading)` (`font-size: 31.5px`, `line-height: 31.5px`, `font-weight: 600`, `letter-spacing: -1.1025px`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`letter-spacing: .16em`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--d-mono: "Space Mono", ui-monospace, monospace`, `--l-mono: "Space Mono", ui-monospace, monospace`.

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
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `10730px`, deepest scrollY reached `9830px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: `WebGL/Canvas`.
- **Hover Physics (`primary_cta` · `01 PROJECTS`)**: `color`: `rgb(217, 205, 208)` -> `rgb(255, 255, 255)`; `backgroundColor`: `rgba(0, 0, 0, 0)` -> `rgba(255, 158, 187, 0.08)`; `borderColor`: `rgb(217, 205, 208)` -> `rgb(255, 255, 255)` (`transition-duration: 0.3s, 0.3s`, `timing: ease, ease`).
- **Interactive Control Probe (`tab` · `ABOUT`)**: Triggered visual diff `5.389` (attr `false -> true`, captured in `assets/state-interactive.webp`).

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Rao Muhammad Hamza, AI Engineer            │
│ ====================================================================== │
│ [ <header.ui> (680x228px)             | Overview · Index · Archive · ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.surface> (w=1440px)                           | │
│ | H1: R A O M U H A M M A D H A M Z A                                | │
│ | Substrate: #0f1220 | Ink: #f4e7e2 | Accent: #ff9ebb                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<article.case>) max-w: 1440px                       | │
│ | +------------------------------+  +------------------------------+ | │
│ | | R a o M u h a m m a d H a m  |  | ResumeWesume                 | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<article.case:nth(2)>) — Nothing on right now       | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.train-chart>) | https://www.raomuhammadhamza.tech/   │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 14px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.ui>             ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.surface>) — 390px Vertical Lead               | │
│ | H1: R A O M U H A M M A D H A M Z A                                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<article.case>) — 1-Col Stack                      | │
│ | [ Item 1: R a o M u h a m m a d H a m z a                        ] | │
│ | [ Item 2: ResumeWesume                                           ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<article.case:nth(2)>) — 1-Col (Nothing on right n)  | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.train-chart>) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.ui> — `www-raomuhammadhamza-tech`)**:
   - Landmark `<header class="ui sig">` (`680x228px`) hosting `Rao Muhammad Hamza, AI Engineer` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-sound="on"`, `data-sound="off"`, `data-go="projects"`, `data-go="experience"`), and stylesheet rule `font-face { font-family:Space Mono;src:url(/fonts/SpaceMono-400.woff2)format("woff2"... }`.
2. **Hero Stage & Focal Lead (<section.surface> — `R A O M U H A M M A D H A M Z A`)**:
   - Landmark `<section class="surface desk">` presenting display lead `R A O M U H A M M A D H A M Z A` and copy excerpt *"I build AI that ships."* over `#0f1220` canvas and `#f4e7e2` ink.
3. **Primary Showcase & Content Grid (<article.case> — `R a o M u h a m m a d H a m z a`)**:
   - Landmark `<article class="case">` rendering section `R a o M u h a m m a d H a m z a` with copy *"Drag to look around"*, asset references (`favicon.svg`, `SpaceGrotesk-Variable.woff2`, `index.BGUfTFpU.css`, `edi-poster.webp`), and grid rule `body { color:f4e7e2;background:0f1220;height:100%;font-family:Space Grotesk,sys... }`.
4. **Interactive Detail & Feature Matrix (<article.case:nth(2)> — `ResumeWesume`)**:
   - Landmark `<article class="case">` framing `ResumeWesume` and `Nothing on right now` (*"AI Engineer · Karachi"*) with `#0b0e17` surface cards, `#ff9ebb` accents, and `.loader.done { opacity:0;visibility:hidden }`.
5. **Colophon & Global Directory Footer (<footer.train-chart> — `https://www.raomuhammadhamza.tech/`)**:
   - Landmark `<footer class="train-chart">` anchoring `Rao Muhammad Hamza, AI Engineer` footer links (`Overview · Index · Archive · About · Contact`), copy *"Flat version WebGL isn't available in this browser."*, and `#1d202d` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `R A O M U H A M M A D H A M Z A` · sticky/fixed elements: `2`
- **Step 02** (`y=850px`, `9%`): Active landmark `#projects` · sticky/fixed elements: `2`
- **Step 03** (`y=2550px`, `26%`): Active landmark `#projects` · sticky/fixed elements: `2`
- **Step 04** (`y=4250px`, `43%`): Active landmark `Mentora` · sticky/fixed elements: `2`
- **Step 05** (`y=5950px`, `61%`): Active landmark `Naqsha` · sticky/fixed elements: `2`
- **Step 06** (`y=7650px`, `78%`): Active landmark `EXPERIENCE` · sticky/fixed elements: `2`
- **Step 07** (`y=9350px`, `95%`): Active landmark `Rao Muhammad Hamza` · sticky/fixed elements: `2`
- **Step 08** (`y=9830px`, `100%`): Active landmark `Nothing on right now` · sticky/fixed elements: `2`

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-raomuhammadhamza-tech (Rao Muhammad Hamza, AI Engineer)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-raomuhammadhamza-tech` (**Rao Muhammad Hamza, AI Engineer** — `https://www.raomuhammadhamza.tech/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0f1220` / `#ff9ebb`).
- **Identity & Domain Context**: Rao Muhammad Hamza, AI Engineer. RAG pipelines, LLM orchestration and agentic workflows, built to hold up in production.
- **Primary Substrate**: `#0f1220` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#f4e7e2`, **Accent / Highlight**: `#ff9ebb`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#0f1220` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#f4e7e2` primary typography and `#ff9ebb` accents.
  - **Grounded Typographic Hierarchy**: Uses `Space Grotesk` across display (`R A O M U H A M M A D H A M Z A`) and body copy, paired with `Space Mono` for monospace/code.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 14px`, padding `20px`) with `cubic-bezier(.2,.7,.2,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-raomuhammadhamza-tech` in your global stylesheet:

:root {
  /* Rao Muhammad Hamza, AI Engineer (www-raomuhammadhamza-tech) — Live-Grounded CSS Variables */
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
- **Primary Canvas Substrate**: `#0f1220` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#f4e7e2` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#0b0e17` — grounded in `.surface { background: #0b0e17 }`
- **Interactive Accent / Highlight**: `#ff9ebb` — grounded in live computed `a` `color` (`computed_styles.json`)
- **Secondary / Muted Copy**: `#b9b2c4` — grounded in `var(--muted)` in `:root`
- **Structural Hairline Border**: `#1d202d` — grounded in `var(--grid-line)` in `:root` (`linear-gradient(ffffff0f, ffffff0f)`)
- **Variable Token (`--screen-ink`)**: `#1b1f33` — grounded in `var(--screen-ink)` in `:root`
- **Variable Token (`--tv-bg`)**: `#161a30` — grounded in `var(--tv-bg)` in `:root`
- **Variable Token (`--tv-bg`)**: `#0c0e1c` — grounded in `var(--tv-bg)` in `:root`
- **Variable Token (`--tv-glow`)**: `#ffffff` — grounded in `var(--tv-glow)` in `:root`
- **Variable Token (`--tv-glow`)**: `#000000` — grounded in `var(--tv-glow)` in `:root`
- **Variable Token (`--d-surf`)**: `#1a1a26` — grounded in `var(--d-surf)` in `:root`
- **Variable Token (`--d-surf2`)**: `#222232` — grounded in `var(--d-surf2)` in `:root`
- **Variable Token (`--d-ink`)**: `#e9e3ef` — grounded in `var(--d-ink)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport)
- **Padding & Gutters**: `20px` lateral canvas padding with `14px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 14px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `20px` horizontal padding
- **Media Queries**: `@media (width<=700px),(height<=500px)`, `@media (width<=480px)`, `@media (prefers-reduced-motion:reduce)`, `@media (width<=700px)`
- **Corner Radii**: `8px`, `var(--tv-radius)`, `50%`, `11px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Space Grotesk`
- **Body Font Stack**: `Space Grotesk`
- **Monospace / Technical Font Stack**: `Space Mono`
- **H1 Display Rule**: live computed `h1` (`font-size: 56px`, `line-height: 50.4px`, `font-weight: 700`, `letter-spacing: -1.96px`)
- **H2 Section Rule**: live computed `h3 (primary section heading)` (`font-size: 31.5px`, `line-height: 31.5px`, `font-weight: 600`, `letter-spacing: -1.1025px`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`letter-spacing: .16em`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--d-mono: "Space Mono", ui-monospace, monospace`, `--l-mono: "Space Mono", ui-monospace, monospace`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-raomuhammadhamza-tech` (`Rao Muhammad Hamza, AI Engineer`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.ui> — `www-raomuhammadhamza-tech`)**:
   - DOM & Selectors: Landmark `<header class="ui sig">` (`680x228px`) hosting `Rao Muhammad Hamza, AI Engineer` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-sound="on"`, `data-sound="off"`, `data-go="projects"`, `data-go="experience"`), and stylesheet rule `font-face { font-family:Space Mono;src:url(/fonts/SpaceMono-400.woff2)format("woff2"... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.ui> — `www-raomuhammadhamza-tech`)` (`www-raomuhammadhamza-tech`) adapts across `@media (width<=700px),(height<=500px)`, `@media (width<=480px)`, `@media (prefers-reduced-motion:reduce)`, `@media (width<=700px)` with `cubic-bezier(.2,.7,.2,1)`, `cubic-bezier(.65,0,.35,1)`, `cubic-bezier(.2,.8,.2,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<section.surface> — `R A O M U H A M M A D H A M Z A`)**:
   - DOM & Selectors: Landmark `<section class="surface desk">` presenting display lead `R A O M U H A M M A D H A M Z A` and copy excerpt *"I build AI that ships."* over `#0f1220` canvas and `#f4e7e2` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×2616px` mobile) sets `#0f1220` background with `#f4e7e2` headline `R A O M U H A M M A D H A M Z A`.
3. **Primary Showcase & Content Grid (<article.case> — `R a o M u h a m m a d H a m z a`)**:
   - DOM & Selectors: Landmark `<article class="case">` rendering section `R a o M u h a m m a d H a m z a` with copy *"Drag to look around"*, asset references (`favicon.svg`, `SpaceGrotesk-Variable.woff2`, `index.BGUfTFpU.css`, `edi-poster.webp`), and grid rule `body { color:f4e7e2;background:0f1220;height:100%;font-family:Space Grotesk,sys... }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<article.case> — `R a o M u h a m m a d H a m z a`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 14px`) on desktop and Single-column vertical stack at `390px` viewport width with `20px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.case:nth(2)> — `ResumeWesume`)**:
   - DOM & Selectors: Landmark `<article class="case">` framing `ResumeWesume` and `Nothing on right now` (*"AI Engineer · Karachi"*) with `#0b0e17` surface cards, `#ff9ebb` accents, and `.loader.done { opacity:0;visibility:hidden }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.case:nth(2)> — `ResumeWesume`)` uses `8px`, `var(--tv-radius)`, `50%`, `11px` radii, `#ff9ebb` highlights, and assets (favicon.svg, SpaceGrotesk-Variable.woff2, index.BGUfTFpU.css).
5. **Colophon & Global Directory Footer (<footer.train-chart> — `https://www.raomuhammadhamza.tech/`)**:
   - DOM & Selectors: Landmark `<footer class="train-chart">` anchoring `Rao Muhammad Hamza, AI Engineer` footer links (`Overview · Index · Archive · About · Contact`), copy *"Flat version WebGL isn't available in this browser."*, and `#1d202d` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.train-chart> — `https://www.raomuhammadhamza.tech/`)` aligns to `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport) with `20px` lateral canvas padding with `14px` grid gap and attributes (data-sound="on", data-sound="off", data-go="projects").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"I build AI that ships."*
- Copy Excerpt 2: *"Drag to look around"*
- Copy Excerpt 3: *"AI Engineer · Karachi"*
- Copy Excerpt 4: *"Flat version WebGL isn't available in this browser."*

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
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `10730px` across 8 distinct viewport chapters using WebGL/Canvas.
- **Vertical Chapter Sequence**: R A O M U H A M M A D H A M... (0%) -> #projects (9%) -> #projects (26%) -> Mentora (43%) -> Naqsha (61%) -> EXPERIENCE (78%) -> Rao Muhammad Hamza (95%) -> Nothing on right now (100%).
- **Hover Micro-Interaction (`primary_cta`)**: Animate `color, backgroundColor, borderColor` with `0.3s, 0.3s ease, ease`.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-raomuhammadhamza-tech`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | R A O M U H A M M A D H A M Z A | `2` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `9%` | #projects | `2` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `2550px` | `26%` | #projects | `2` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `4250px` | `43%` | Mentora | `2` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `5950px` | `61%` | Naqsha | `2` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `7650px` | `78%` | EXPERIENCE | `2` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `9350px` | `95%` | Rao Muhammad Hamza | `2` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `9830px` | `100%` | Nothing on right now | `2` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | R A O M U H A M M A D H A M Z A | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `5772px` | `50%` | Mentora | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `11545px` | `100%` | Nothing on right now | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Interactive UI State Captures (`1440×900` WebP)
| State Type | Trigger / Observation | Visual Asset |
| :--- | :--- | :--- |
| `interactive_control` | Control `tab` (`ABOUT`, diff `5.389`) | [state-interactive.webp](assets/state-interactive.webp) |

