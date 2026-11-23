---
title: "UI Prompt Blueprint: 100yearsmonet-com"
date: 2026-11-23
captured_at: 2026-11-23
target: "100yearsmonet-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#fbf3c6`)"
---

# UI Design System & Master Generation Blueprint: 100yearsmonet-com

> **Monet 100 — A century without Claude Monet · 3D gallery** (https://100yearsmonet.com) — A hundred years after Claude Monet’s death: walk on water through his paintings into the room of Water Lilies. An immersive 3D tribute wi...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Monet 100 — A century without Claude Monet · 3D gallery** (`https://100yearsmonet.com`). A hundred years after Claude Monet’s death: walk on water through his paintings into the room of Water Lilies. An immersive 3D tribute wi...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#fbf3c6`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#000000` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#fbf3c6` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Manrope` for display copy (`100 years without Monet`) with `Quelia` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 16px`, padding `40px`) with `cubic-bezier(.3,.6,.2,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport).
- **Canvas Lateral Padding & Spacing**: `40px` lateral canvas padding with `16px` grid gap.
- **Border Radius Scale**: `50%`, `2px`, `3px`, `1px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 16px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `40px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:600px)`, `@media (max-width:760px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:700px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `p` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#141006` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#fbf3c6` | `.mui .mui-gslot .btn--solid { background: #fbf3c6 }` |
| **Secondary / Muted Copy** | `#e5dce9` | live computed `body` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#8c8c8c` | `.mui .mui-go:active { border-color: #8c8c8c }` |
| **Variable Token (`--mui-cream`)** | `#fcf4e9` | `var(--mui-cream)` in stylesheet |
| **Variable Token (`--mui-ink`)** | `#282b36` | `var(--mui-ink)` in stylesheet |
| **Variable Token (`--mui-night`)** | `#15141f` | `var(--mui-night)` in stylesheet |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--snd-r` | `var(--mui-gutter,24px)` | Dimension / Scale Token |
| `--snd-b` | `calc(26px + env(safe-area-inset-bottom,0px))` | Dimension / Scale Token |
| `--cat` | `calc(1 - var(--p,0))` | Design System Custom Token |
| `--fs` | `min(52vh,30vw)` | Dimension / Scale Token |
| `--bx` | `50%` | Dimension / Scale Token |
| `--by` | `46%` | Dimension / Scale Token |
| `--ch` | `150px` | Dimension / Scale Token |
| `--mui-cream` | `#FCF4E9` | Color / Atmospheric Token |
| `--mui-cream-rgb` | `252 244 233` | Design System Custom Token |
| `--mui-ink` | `#282B36` | Typography Ink Token |
| `--mui-night` | `#15141f` | Color / Atmospheric Token |
| `--mui-serif` | `"Quelia","Iowan Old Style",Georgia,serif` | Typography / Scale Token |
| `--mui-sans` | `"Manrope","Helvetica Neue",Arial,system-ui,sans-serif` | Typography / Scale Token |
| `--mui-ui` | `"Manrope","Helvetica Neue",Arial,system-ui,sans-serif` | Dimension / Scale Token |
| `--100yearsmonet-co-bg` | `#000000` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--100yearsmonet-co-ink` | `#ffffff` | Primary Typography Ink (computed-derived) |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Manrope`.
- **Primary Body Stack**: `Quelia`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 32px`, `line-height: 49.6px`, `font-weight: 400`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 54.72px`, `line-height: 55.8144px`, `font-weight: 300`); rule `h2` (`letter-spacing: -.01em`).
- **Body Copy**: live computed `body` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 11.5px`, `line-height: 17.25px`, `font-weight: 400`); rule `small` (`letter-spacing: .12em`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.3,.6,.2,1)`, `cubic-bezier(.5,0,.2,1)`, `cubic-bezier(.2,.7,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.mui-pre`**: `transition: opacity 1.4s ease .1s,visibility 1.6s` extracted from `100yearsmonet-com` stylesheet.
- **Selector `.mui-hero`**: `transition: opacity .9s ease,transform 1.4s cubic-bezier(.3,.6,.2,1),filter 1s` extracted from `100yearsmonet-com` stylesheet.
- **Selector `.mui .btn`**: `transition: background .25s,color .25s,border-color .25s` extracted from `100yearsmonet-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.3,.6,.2,1)`)**: Governs interactive state transitions across `<header.mui-hud>` and `<article.mui-card>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Monet 100 — A century without Claude Monet │
│ ====================================================================== │
│ [ <header.mui-hud> (1360x0px)         | Musée de l’Orangerie · Musée ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.mui-hero> (w=1440px)                          | │
│ | H1: 100 years without Monet                                        | │
│ | Substrate: #000000 | Ink: #ffffff | Accent: #fbf3c6                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<article.mui-card>) max-w: 1440px                   | │
│ | +------------------------------+  +------------------------------+ | │
│ | | 100 Years without Monet      |  | Claude Monet died at Giverny | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<article.mui-card:nth(2)>) — This experience needs  | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.mui-garden> ) | https://100yearsmonet.com            │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.mui-hud>        ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.mui-hero>) — 390px Vertical Lead              | │
│ | H1: 100 years without Monet                                        | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<article.mui-card>) — 1-Col Stack                  | │
│ | [ Item 1: 100 Years without Monet                                ] | │
│ | [ Item 2: Claude Monet died at Giverny on 5 December 1926.       ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<article.mui-card:nth(2)) — 1-Col (This experience ne) │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.mui-garden> ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.mui-hud> — `100yearsmonet-com`)**:
   - Landmark `<header class="mui-hud mui-hud--top">` (`1360x0px`) hosting `Monet 100 — A century without Claude` navigation (`Musée de l’Orangerie · Musée d’Orsay · The Met · MFA Boston · Museum Barberini`), DOM attributes (`data-title-stay`, `data-enter="sound"`, `data-v="Dawn"`, `data-card="impression"`), and stylesheet rule `body { background:000 }`.
2. **Hero Stage & Focal Lead (<section.mui-hero> — `100 years without Monet`)**:
   - Landmark `<section class="mui-hero">` presenting display lead `100 years without Monet` and copy excerpt *"He died at Giverny on 5 December 1926. A century later, walk on t"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<article.mui-card> — `100 Years without Monet`)**:
   - Landmark `<article class="mui-card">` rendering section `100 Years without Monet` with copy *"Claude Monet died at Giverny on 5 December 1926. A hundred years "*, asset references (`favicon-32.png`, `apple-touch-icon.png`, `site.webmanifest`, `quelia.woff2`), and grid rule `canvas { position:fixed;inset:0;width:100%;height:100% }`.
4. **Interactive Detail & Feature Matrix (<article.mui-card:nth(2)> — `Claude Monet died at Giverny on 5 `)**:
   - Landmark `<article class="mui-card">` framing `Claude Monet died at Giverny on 5 December 1926.` and `This experience needs JavaScript and WebGL.` (*"This experience needs JavaScript and WebGL."*) with `#141006` surface cards, `#fbf3c6` accents, and `journey { height:2000vh;pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.mui-garden> — `https://100yearsmonet.com`)**:
   - Landmark `<footer class="mui-garden">` anchoring `Monet 100 — A century without Cl` footer links (`Musée de l’Orangerie · Musée d’Orsay · The Met · MFA Boston · Museum Barberini`), copy *"Claude Monet 1926 — 2026"*, and `#8c8c8c` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: 100yearsmonet-com (Monet 100 — A century without Claude Monet · 3D gallery)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `100yearsmonet-com` (**Monet 100 — A century without Claude Monet · 3D gallery** — `https://100yearsmonet.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#fbf3c6`).
- **Identity & Domain Context**: A hundred years after Claude Monet’s death: walk on water through his paintings into the room of Water Lilies. An immersive 3D tribute wi...
- **Primary Substrate**: `#000000` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#ffffff`, **Accent / Highlight**: `#fbf3c6`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#000000` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#fbf3c6` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Manrope` for display copy (`100 years without Monet`) with `Quelia` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 16px`, padding `40px`) with `cubic-bezier(.3,.6,.2,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `100yearsmonet-com` in your global stylesheet:

:root {
  /* Monet 100 — A century without Claude Monet · 3D gallery (100yearsmonet-com) — Live-Grounded CSS Variables */
  --snd-r: var(--mui-gutter,24px); /* Dimension / Scale Token (100yearsmonet-com) */
  --snd-b: calc(26px + env(safe-area-inset-bottom,0px)); /* Dimension / Scale Token (100yearsmonet-com) */
  --cat: calc(1 - var(--p,0)); /* Design System Custom Token (100yearsmonet-com) */
  --fs: min(52vh,30vw); /* Dimension / Scale Token (100yearsmonet-com) */
  --bx: 50%; /* Dimension / Scale Token (100yearsmonet-com) */
  --by: 46%; /* Dimension / Scale Token (100yearsmonet-com) */
  --ch: 150px; /* Dimension / Scale Token (100yearsmonet-com) */
  --mui-cream: #FCF4E9; /* Color / Atmospheric Token (100yearsmonet-com) */
  --mui-cream-rgb: 252 244 233; /* Design System Custom Token (100yearsmonet-com) */
  --mui-ink: #282B36; /* Typography Ink Token (100yearsmonet-com) */
  --mui-night: #15141f; /* Color / Atmospheric Token (100yearsmonet-com) */
  --mui-serif: "Quelia","Iowan Old Style",Georgia,serif; /* Typography / Scale Token (100yearsmonet-com) */
  --mui-sans: "Manrope","Helvetica Neue",Arial,system-ui,sans-serif; /* Typography / Scale Token (100yearsmonet-com) */
  --mui-ui: "Manrope","Helvetica Neue",Arial,system-ui,sans-serif; /* Dimension / Scale Token (100yearsmonet-com) */
  --100yearsmonet-co-bg: #000000; /* Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) (100yearsmonet-com) */
  --100yearsmonet-co-ink: #ffffff; /* Primary Typography Ink (computed-derived) (100yearsmonet-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000000` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#ffffff` — grounded in live computed `p` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#141006` — grounded in live computed `button` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#fbf3c6` — grounded in `.mui .mui-gslot .btn--solid { background: #fbf3c6 }`
- **Secondary / Muted Copy**: `#e5dce9` — grounded in live computed `body` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#8c8c8c` — grounded in `.mui .mui-go:active { border-color: #8c8c8c }`
- **Variable Token (`--mui-cream`)**: `#fcf4e9` — grounded in `var(--mui-cream)` in stylesheet
- **Variable Token (`--mui-ink`)**: `#282b36` — grounded in `var(--mui-ink)` in stylesheet
- **Variable Token (`--mui-night`)**: `#15141f` — grounded in `var(--mui-night)` in stylesheet

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport)
- **Padding & Gutters**: `40px` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `40px` horizontal padding
- **Media Queries**: `@media (max-width:600px)`, `@media (max-width:760px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:700px)`
- **Corner Radii**: `50%`, `2px`, `3px`, `1px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Manrope`
- **Body Font Stack**: `Quelia`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 32px`, `line-height: 49.6px`, `font-weight: 400`)
- **H2 Section Rule**: live computed `h2` (`font-size: 54.72px`, `line-height: 55.8144px`, `font-weight: 300`); rule `h2` (`letter-spacing: -.01em`)
- **Body Copy Rule**: live computed `body` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 11.5px`, `line-height: 17.25px`, `font-weight: 400`); rule `small` (`letter-spacing: .12em`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `100yearsmonet-com` (`Monet 100 — A century without Claude Monet · 3D gallery`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.mui-hud> — `100yearsmonet-com`)**:
   - DOM & Selectors: Landmark `<header class="mui-hud mui-hud--top">` (`1360x0px`) hosting `Monet 100 — A century without Claude` navigation (`Musée de l’Orangerie · Musée d’Orsay · The Met · MFA Boston · Museum Barberini`), DOM attributes (`data-title-stay`, `data-enter="sound"`, `data-v="Dawn"`, `data-card="impression"`), and stylesheet rule `body { background:000 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.mui-hud> — `100yearsmonet-com`)` (`100yearsmonet-com`) adapts across `@media (max-width:600px)`, `@media (max-width:760px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:700px)` with `cubic-bezier(.3,.6,.2,1)`, `cubic-bezier(.5,0,.2,1)`, `cubic-bezier(.2,.7,.2,1)` transitions and links `Musée de l’Orangerie · Musée d’Orsay · The Met · MFA Boston · Museum Barberini`.
2. **Hero Stage & Focal Lead (<section.mui-hero> — `100 years without Monet`)**:
   - DOM & Selectors: Landmark `<section class="mui-hero">` presenting display lead `100 years without Monet` and copy excerpt *"He died at Giverny on 5 December 1926. A century later, walk on t"* over `#000000` canvas and `#ffffff` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#000000` background with `#ffffff` headline `100 years without Monet`.
3. **Primary Showcase & Content Grid (<article.mui-card> — `100 Years without Monet`)**:
   - DOM & Selectors: Landmark `<article class="mui-card">` rendering section `100 Years without Monet` with copy *"Claude Monet died at Giverny on 5 December 1926. A hundred years "*, asset references (`favicon-32.png`, `apple-touch-icon.png`, `site.webmanifest`, `quelia.woff2`), and grid rule `canvas { position:fixed;inset:0;width:100%;height:100% }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<article.mui-card> — `100 Years without Monet`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `40px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.mui-card:nth(2)> — `Claude Monet died at Giverny on 5 `)**:
   - DOM & Selectors: Landmark `<article class="mui-card">` framing `Claude Monet died at Giverny on 5 December 1926.` and `This experience needs JavaScript and WebGL.` (*"This experience needs JavaScript and WebGL."*) with `#141006` surface cards, `#fbf3c6` accents, and `journey { height:2000vh;pointer-events:none }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.mui-card:nth(2)> — `Claude Monet died at Giverny on 5 `)` uses `50%`, `2px`, `3px`, `1px` radii, `#fbf3c6` highlights, and assets (favicon-32.png, apple-touch-icon.png, site.webmanifest).
5. **Colophon & Global Directory Footer (<footer.mui-garden> — `https://100yearsmonet.com`)**:
   - DOM & Selectors: Landmark `<footer class="mui-garden">` anchoring `Monet 100 — A century without Cl` footer links (`Musée de l’Orangerie · Musée d’Orsay · The Met · MFA Boston · Museum Barberini`), copy *"Claude Monet 1926 — 2026"*, and `#8c8c8c` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.mui-garden> — `https://100yearsmonet.com`)` aligns to `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport) with `40px` lateral canvas padding with `16px` grid gap and attributes (data-title-stay, data-enter="sound", data-v="Dawn").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"He died at Giverny on 5 December 1926. A century later, walk on the water through..."*
- Copy Excerpt 2: *"Claude Monet died at Giverny on 5 December 1926. A hundred years later, walk on th..."*
- Copy Excerpt 3: *"This experience needs JavaScript and WebGL."*
- Copy Excerpt 4: *"Claude Monet 1926 — 2026"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.3,.6,.2,1)`, `cubic-bezier(.5,0,.2,1)`, `cubic-bezier(.2,.7,.2,1)`
- **Extracted Stylesheet Rules (`100yearsmonet-com`)**:
- `body { background:000 }`
- `canvas { position:fixed;inset:0;width:100%;height:100% }`
- `journey { height:2000vh;pointer-events:none }`
- `header { position:fixed;top:28px;left:30px;letter-spacing:.2em;pointer-events:none }`
- `footer { position:fixed;bottom:28px;left:30px;right:30px;display:flex;justify-con... }`
- **Per-Selector Transition Rules**:
- **Selector `.mui-pre`**: `transition: opacity 1.4s ease .1s,visibility 1.6s` extracted from `100yearsmonet-com` stylesheet.
- **Selector `.mui-hero`**: `transition: opacity .9s ease,transform 1.4s cubic-bezier(.3,.6,.2,1),filter 1s` extracted from `100yearsmonet-com` stylesheet.
- **Selector `.mui .btn`**: `transition: background .25s,color .25s,border-color .25s` extracted from `100yearsmonet-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.3,.6,.2,1)`)**: Governs interactive state transitions across `<header.mui-hud>` and `<article.mui-card>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `100yearsmonet-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
