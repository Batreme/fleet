---
title: "UI Prompt Blueprint: flycrooked-com"
date: 2026-11-15
target: "[[overview|flycrooked-com]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#17181c`)"
---

# UI Design System & Master Generation Blueprint: flycrooked-com

> **Crow · Trip planner and flight finder for iPhone** (https://flycrooked.com/) — Your iPhone travel companion. Plan a trip, compare flight routes, track delays and gate changes, and carry a blunt local guide when you l...

![Desktop Viewport Capture (1440x1254)](file:///root/projects/fleet/wiki/targets/flycrooked-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Crow · Trip planner and flight finder for iPhone** (`https://flycrooked.com/`). Your iPhone travel companion. Plan a trip, compare flight routes, track delays and gate changes, and carry a blunt local guide when you l...
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#17181c`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--color-black)` in `:root`) paired with `#fff` primary typography and `#17181c` accents.
  - **Extracted Typographic Hierarchy**: Pairs `display` for display copy (`Marrakech`) with `display Fallback` and `mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: 1px`, padding `5vw`) with `cubic-bezier(.4,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/flycrooked-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×1254px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `40rem` extracted from `flycrooked-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `5vw` lateral canvas padding with `1px` grid gap.
- **Border Radius Scale**: `.25rem`, `2px`, `3px`, `var(--radius-xl)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: 1px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `5vw` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#eceff3` | `var(--concourse)` in `:root` |
| **Interactive Accent / Highlight** | `#17181c` | `var(--sign-black)` in `:root` |
| **Secondary / Muted Copy** | `#1c1e24` | `var(--panel-black)` in `:root` |
| **Structural Hairline Border** | `#ff3d81` | `var(--accent)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-display` | `"display","display Fallback"` | Typography / Scale Token |
| `--font-mono` | `"mono"` | Typography / Scale Token |
| `--font-body` | `"body","body Fallback"` | Typography / Scale Token |
| `--font-wordmark` | `"wordmark"` | Typography / Scale Token |
| `--color-neutral-100` | `oklch(97% 0 0)` | Brand / Palette Token |
| `--color-neutral-200` | `oklch(92.2% 0 0)` | Brand / Palette Token |
| `--color-neutral-300` | `oklch(87% 0 0)` | Brand / Palette Token |
| `--color-neutral-400` | `oklch(70.8% 0 0)` | Brand / Palette Token |
| `--color-neutral-800` | `oklch(26.9% 0 0)` | Brand / Palette Token |
| `--color-neutral-900` | `oklch(20.5% 0 0)` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-3xl` | `48rem` | Layout / Spatial Grid Token |
| `--font-weight-bold` | `700` | Typography / Scale Token |
| `--tracking-wide` | `.025em` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `display`.
- **Primary Body Stack**: `display Fallback`.
- **Technical / Metadata Stack**: `mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--font-display: "display","display Fallback"`, `--display: var(--font-display),"Arial Narrow",Arial,sans-serif`; rule `h1` (`font-size: 88px`, `line-height: .94`, `letter-spacing: 0`, `font-weight: 700`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 46px`, `line-height: 1.05`, `letter-spacing: 0`, `font-weight: 600`).
- **Body Copy**: CSS variables `--font-body: "body","body Fallback"`, `--body: var(--font-body),-apple-system,"Segoe UI",sans-serif`; rule `p` (`font-size: 16px`, `line-height: 1.75`).
- **Metadata & Navigation Labels**: CSS variables `--font-mono: "mono"`, `--default-mono-font-family: var(--font-mono)`, `--mono: var(--font-mono),ui-monospace,"SF Mono",Menlo,monospace`; rule `small` (`font-size: 11.5px`, `letter-spacing: .08em`, `font-weight: 500`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.4,0,.6,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `flycrooked-com` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `flycrooked-com` stylesheet.
- **Selector `.gshare-btn`**: `transition: border-color .15s,background .15s,color .15s` extracted from `flycrooked-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.nav>` and `<section.stage>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Crow · Trip planner and flight finder for  │
│ ====================================================================== │
│ [ <header.nav>             | Guides · How it works · Support · Priv ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.stage>                                      |   │
│ | H1: Marrakech                                                    |   │
│ | Substrate: #000       | Ink: #fff       | Accent: #17181c        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.stage>           ) max-w: 40rem          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Trip wires                   |  | What Changed                 | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 1px   ) | │
│ | [<header.nav>] -> [<section.stage>] -> [<section.stage>] |           │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.sfoot>        ) | https://flycrooked.com/            │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.nav> — `flycrooked-com`)**:
   - Landmark `<header class="nav">` hosting `Crow · Trip planner and flight finde` navigation (`Guides · How it works · Support · Privacy · Terms`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="story-fonts"`, `data-precedence="story-fonts"`), and stylesheet rule `.__className_2063d3 { font-family:display,display Fallback }`.
2. **Hero Stage & Focal Lead (<section.stage> — `Marrakech`)**:
   - Landmark `<section class="stage">` presenting display lead `Marrakech` and copy excerpt *"First slot of the day. The blue walls, before the coaches."* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.stage> — `Trip wires`)**:
   - Landmark `<section class="stage">` rendering section `Trip wires` with copy *"Timed entry · 08:00"*, asset references (`06ac09dcb8ec7d56.p.woff2`, `4224042929936d69-s.p.woff2`, `422bb7078d9b61dc.p.woff2`, `532b6dda9c49d302-s.p.woff2`), and grid rule `.__variable_2063d3 { --font-display:"display","display Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.stage> — `What Changed`)**:
   - Landmark `<section class="stage">` framing `What Changed` and `WATCHES` (*"In before the tour groups walk over from the square."*) with `#eceff3` surface cards, `#17181c` accents, and `.__className_c3828f { font-family:mono }`.
5. **Colophon & Global Directory Footer (<footer.sfoot> — `https://flycrooked.com/`)**:
   - Landmark `<footer class="sfoot">` anchoring `Crow · Trip planner and flight f` footer links (`Guides · How it works · Support · Privacy · Terms`), copy *"Lose the map. Crow saved the way back offline."*, and `#ff3d81` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: flycrooked-com (Crow · Trip planner and flight finder for iPhone)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `flycrooked-com` (**Crow · Trip planner and flight finder for iPhone** — `https://flycrooked.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#17181c`).
- **Identity & Domain Context**: Your iPhone travel companion. Plan a trip, compare flight routes, track delays and gate changes, and carry a blunt local guide when you l...
- **Primary Substrate**: `#000` (`var(--color-black)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#17181c`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--color-black)` in `:root`) paired with `#fff` primary typography and `#17181c` accents.
  - **Extracted Typographic Hierarchy**: Pairs `display` for display copy (`Marrakech`) with `display Fallback` and `mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: 1px`, padding `5vw`) with `cubic-bezier(.4,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `flycrooked-com` in your global stylesheet:

:root {
  /* Crow · Trip planner and flight finder for iPhone (flycrooked-com) — Ground-Truth Extracted CSS Variables */
  --font-display: "display","display Fallback"; /* Typography / Scale Token (flycrooked-com) */
  --font-mono: "mono"; /* Typography / Scale Token (flycrooked-com) */
  --font-body: "body","body Fallback"; /* Typography / Scale Token (flycrooked-com) */
  --font-wordmark: "wordmark"; /* Typography / Scale Token (flycrooked-com) */
  --color-neutral-100: oklch(97% 0 0); /* Brand / Palette Token (flycrooked-com) */
  --color-neutral-200: oklch(92.2% 0 0); /* Brand / Palette Token (flycrooked-com) */
  --color-neutral-300: oklch(87% 0 0); /* Brand / Palette Token (flycrooked-com) */
  --color-neutral-400: oklch(70.8% 0 0); /* Brand / Palette Token (flycrooked-com) */
  --color-neutral-800: oklch(26.9% 0 0); /* Brand / Palette Token (flycrooked-com) */
  --color-neutral-900: oklch(20.5% 0 0); /* Brand / Palette Token (flycrooked-com) */
  --color-black: #000; /* Canvas / Surface Token (flycrooked-com) */
  --color-white: #fff; /* Canvas / Surface Token (flycrooked-com) */
  --spacing: .25rem; /* Layout / Spatial Grid Token (flycrooked-com) */
  --container-3xl: 48rem; /* Layout / Spatial Grid Token (flycrooked-com) */
  --font-weight-bold: 700; /* Typography / Scale Token (flycrooked-com) */
  --tracking-wide: .025em; /* Typography / Scale Token (flycrooked-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000` — grounded in `var(--color-black)` in `:root`
- **Primary Typography Ink**: `#fff` — grounded in `var(--color-white)` in `:root`
- **Elevated Surface / Card Substrate**: `#eceff3` — grounded in `var(--concourse)` in `:root`
- **Interactive Accent / Highlight**: `#17181c` — grounded in `var(--sign-black)` in `:root`
- **Secondary / Muted Copy**: `#1c1e24` — grounded in `var(--panel-black)` in `:root`
- **Structural Hairline Border**: `#ff3d81` — grounded in `var(--accent)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×1254px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `40rem` extracted from `flycrooked-com` stylesheet
- **Padding & Gutters**: `5vw` lateral canvas padding with `1px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: 1px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `5vw` horizontal padding
- **Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`
- **Corner Radii**: `.25rem`, `2px`, `3px`, `var(--radius-xl)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `display`
- **Body Font Stack**: `display Fallback`
- **Monospace / Technical Font Stack**: `mono`
- **H1 Display Rule**: CSS variables `--font-display: "display","display Fallback"`, `--display: var(--font-display),"Arial Narrow",Arial,sans-serif`; rule `h1` (`font-size: 88px`, `line-height: .94`, `letter-spacing: 0`, `font-weight: 700`)
- **H2 Section Rule**: rule `h2` (`font-size: 46px`, `line-height: 1.05`, `letter-spacing: 0`, `font-weight: 600`)
- **Body Copy Rule**: CSS variables `--font-body: "body","body Fallback"`, `--body: var(--font-body),-apple-system,"Segoe UI",sans-serif`; rule `p` (`font-size: 16px`, `line-height: 1.75`)
- **Metadata & Index Rule**: CSS variables `--font-mono: "mono"`, `--default-mono-font-family: var(--font-mono)`, `--mono: var(--font-mono),ui-monospace,"SF Mono",Menlo,monospace`; rule `small` (`font-size: 11.5px`, `letter-spacing: .08em`, `font-weight: 500`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `flycrooked-com` (`Crow · Trip planner and flight finder for iPhone`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.nav> — `flycrooked-com`)**:
   - DOM & Selectors: Landmark `<header class="nav">` hosting `Crow · Trip planner and flight finde` navigation (`Guides · How it works · Support · Privacy · Terms`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="story-fonts"`, `data-precedence="story-fonts"`), and stylesheet rule `.__className_2063d3 { font-family:display,display Fallback }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.nav> — `flycrooked-com`)` (`flycrooked-com`) adapts across `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)` with `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.4,0,.6,1)` transitions and links `Guides · How it works · Support · Privacy · Terms`.
2. **Hero Stage & Focal Lead (<section.stage> — `Marrakech`)**:
   - DOM & Selectors: Landmark `<section class="stage">` presenting display lead `Marrakech` and copy excerpt *"First slot of the day. The blue walls, before the coaches."* over `#000` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×1254px` desktop / `390×2400px` mobile) sets `#000` background with `#fff` headline `Marrakech`.
3. **Primary Showcase & Content Grid (<section.stage> — `Trip wires`)**:
   - DOM & Selectors: Landmark `<section class="stage">` rendering section `Trip wires` with copy *"Timed entry · 08:00"*, asset references (`06ac09dcb8ec7d56.p.woff2`, `4224042929936d69-s.p.woff2`, `422bb7078d9b61dc.p.woff2`, `532b6dda9c49d302-s.p.woff2`), and grid rule `.__variable_2063d3 { --font-display:"display","display Fallback" }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.stage> — `Trip wires`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: 1px`) on desktop and Single-column vertical stack at `390px` viewport width with `5vw` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.stage> — `What Changed`)**:
   - DOM & Selectors: Landmark `<section class="stage">` framing `What Changed` and `WATCHES` (*"In before the tour groups walk over from the square."*) with `#eceff3` surface cards, `#17181c` accents, and `.__className_c3828f { font-family:mono }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.stage> — `What Changed`)` uses `.25rem`, `2px`, `3px`, `var(--radius-xl)` radii, `#17181c` highlights, and assets (06ac09dcb8ec7d56.p.woff2, 4224042929936d69-s.p.woff2, 422bb7078d9b61dc.p.woff2).
5. **Colophon & Global Directory Footer (<footer.sfoot> — `https://flycrooked.com/`)**:
   - DOM & Selectors: Landmark `<footer class="sfoot">` anchoring `Crow · Trip planner and flight f` footer links (`Guides · How it works · Support · Privacy · Terms`), copy *"Lose the map. Crow saved the way back offline."*, and `#ff3d81` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.sfoot> — `https://flycrooked.com/`)` aligns to `40rem` extracted from `flycrooked-com` stylesheet with `5vw` lateral canvas padding with `1px` grid gap and attributes (data-precedence="next", data-precedence="next", data-precedence="story-fonts").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"First slot of the day. The blue walls, before the coaches."*
- Copy Excerpt 2: *"Timed entry · 08:00"*
- Copy Excerpt 3: *"In before the tour groups walk over from the square."*
- Copy Excerpt 4: *"Lose the map. Crow saved the way back offline."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.4,0,.6,1)`
- **Extracted Stylesheet Rules (`flycrooked-com`)**:
- `.__className_2063d3 { font-family:display,display Fallback }`
- `.__variable_2063d3 { --font-display:"display","display Fallback" }`
- `.__className_c3828f { font-family:mono }`
- `.__variable_c3828f { --font-mono:"mono" }`
- `.__className_b7c917 { font-family:body,body Fallback }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `flycrooked-com` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `flycrooked-com` stylesheet.
- **Selector `.gshare-btn`**: `transition: border-color .15s,background .15s,color .15s` extracted from `flycrooked-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.nav>` and `<section.stage>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `flycrooked-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
