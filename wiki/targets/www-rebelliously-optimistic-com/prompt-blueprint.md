---
title: "UI Prompt Blueprint: www-rebelliously-optimistic-com"
date: 2026-11-15
target: "[[overview|www-rebelliously-optimistic-com]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#e5e7eb` / `#fff9`)"
---

# UI Design System & Master Generation Blueprint: www-rebelliously-optimistic-com

> **Rebelliously Optimistic — A movement for the human future** (https://www.rebelliously-optimistic.com/) — A movement for the human future in the age of AI. Quarterly gatherings and Human Notes for people who refuse to let progress be anything...

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/www-rebelliously-optimistic-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Rebelliously Optimistic — A movement for the human future** (`https://www.rebelliously-optimistic.com/`). A movement for the human future in the age of AI. Quarterly gatherings and Human Notes for people who refuse to let progress be anything...
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#e5e7eb` / `#fff9`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#e5e7eb` (`:after { border: #e5e7eb }`) paired with `#fff3` primary typography and `#fff9` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Bebas Neue` for display copy (`Our Story`) with `Instrument Sans` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `640px` container bounds (`gap: .25rem`, padding `.25rem`) with `cubic-bezier(.4,0,.6,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/www-rebelliously-optimistic-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `640px` extracted from `www-rebelliously-optimistic-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `.25rem` lateral canvas padding with `.25rem` grid gap.
- **Border Radius Scale**: `.25rem`, `1rem`, `14px`, `20px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 640px`, `gap: .25rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `.25rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (width>=640px)`, `@media (width>=768px)`, `@media (width>=1024px)`, `@media (width>=1280px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#e5e7eb` | `:after { border: #e5e7eb }` |
| **Primary Typography Ink** | `#9ca3af` | `input::-moz-placeholder { color: #9ca3af }` |
| **Elevated Surface / Card Substrate** | `#fff3` | `20 { border-color: #fff3 }` |
| **Interactive Accent / Highlight** | `#fff9` | `60 { border-color: #fff9 }` |
| **Secondary / Muted Copy** | `#0003` | `20 { background-color: #0003 }` |
| **Structural Hairline Border** | `#0000` | `.bg-transparent { background-color: #0000 }` |
| **Variable Token (`--line`)** | `#3e1c2a40` | `var(--line)` in `:root` |
| **Variable Token (`--line-soft`)** | `#3e1c2a1f` | `var(--line-soft)` in `:root` |
| **Variable Token (`--line-faint`)** | `#3e1c2a14` | `var(--line-faint)` in `:root` |
| **Variable Token (`--line-cream`)** | `#f3ebd938` | `var(--line-cream)` in `:root` |
| **Variable Token (`--line-cream-soft`)** | `#f3ebd91f` | `var(--line-cream-soft)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--line` | `#3e1c2a40` | Color / Atmospheric Token |
| `--line-soft` | `#3e1c2a1f` | Color / Atmospheric Token |
| `--line-faint` | `#3e1c2a14` | Color / Atmospheric Token |
| `--line-cream` | `#f3ebd938` | Color / Atmospheric Token |
| `--line-cream-soft` | `#f3ebd91f` | Color / Atmospheric Token |
| `--tw-border-spacing-x` | `0` | Layout / Spatial Grid Token |
| `--tw-border-spacing-y` | `0` | Layout / Spatial Grid Token |
| `--tw-translate-x` | `0` | Design System Custom Token |
| `--tw-translate-y` | `0` | Design System Custom Token |
| `--tw-rotate` | `0` | Design System Custom Token |
| `--tw-skew-x` | `0` | Design System Custom Token |
| `--tw-skew-y` | `0` | Design System Custom Token |
| `--tw-scale-x` | `1` | Design System Custom Token |
| `--tw-scale-y` | `1` | Design System Custom Token |
| `--www-rebelliously-bg` | `#e5e7eb` | Canvas Substrate (from `:after { border: #e5e7eb }`) |
| `--www-rebelliously-ink` | `#fff3` | Primary Typography Ink (stylesheet-derived) |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Bebas Neue`.
- **Primary Body Stack**: `Instrument Sans`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `1.5rem`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `1.5rem`).
- **Body Copy**: rule `p` (`font-size: calc(6em + 13.3px)`, `font-weight: 400`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `1.5rem`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.22,1,.36,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.transition`**: `transition: .15s` extracted from `www-rebelliously-optimistic-com` stylesheet.
- **Selector `box-shadow\]`**: `transition: .15s` extracted from `www-rebelliously-optimistic-com` stylesheet.
- **Selector `.transition-all`**: `transition: .15s` extracted from `www-rebelliously-optimistic-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.6,1)`)**: Governs interactive state transitions across `<header.fixed>` and `<section.relative>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Rebelliously Optimistic — A movement for t │
│ ====================================================================== │
│ [ <header.fixed>           | The Experience · Human Notes           ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hidden>                                     |   │
│ | H1: Our Story                                                    |   │
│ | Substrate: #e5e7eb    | Ink: #fff3      | Accent: #fff9          |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.relative>        ) max-w: 640px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Four commitments. One moveme |  | Build human-first            | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .25rem) | │
│ | [<header.fixed>] -> [<section.hidden>] -> [<section.relative>] |     │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.sticky>       ) | https://www.rebelliously-optimisti │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.fixed> — `www-rebelliously-optimistic-com`)**:
   - Landmark `<header class="fixed top-0">` hosting `Rebelliously Optimistic — A movement` navigation (`The Experience · Human Notes`), DOM attributes (`data-sdkn="@vercel/analytics/react"`, `data-sdkv="2.0.1"`, `data-engine="three.js r184"`), and stylesheet rule `after { box-sizing:border-box;border:0 solid e5e7eb }`.
2. **Hero Stage & Focal Lead (<section.hidden> — `Our Story`)**:
   - Landmark `<section class="hidden relative">` presenting display lead `Our Story` and copy excerpt *"Rebelliously Optimistic."* over `#e5e7eb` canvas and `#fff3` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `Four commitments. One movement.`)**:
   - Landmark `<section class="relative w-full">` rendering section `Four commitments. One movement.` with copy *"Become a partner Partner"*, asset references (`favicon.svg`, `favicon-32.png`, `favicon-16.png`, `apple-touch-icon.png`), and grid rule `body { line-height:inherit;margin:0 }`.
4. **Interactive Detail & Feature Matrix (<section.relative> — `Build human-first`)**:
   - Landmark `<section class="relative z-10">` framing `Build human-first` and `the Experience` (*"Elevating shared humanity in the age of AI."*) with `#fff3` surface cards, `#fff9` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.sticky> — `https://www.rebelliously-optimistic.com/`)**:
   - Landmark `<footer class="sticky bottom-0">` anchoring `Rebelliously Optimistic — A move` footer links (`The Experience · Human Notes`), copy *"W r i t e i t i n a h u m a n v o i c e ."*, and `#0000` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-rebelliously-optimistic-com (Rebelliously Optimistic — A movement for the human future)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-rebelliously-optimistic-com` (**Rebelliously Optimistic — A movement for the human future** — `https://www.rebelliously-optimistic.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#e5e7eb` / `#fff9`).
- **Identity & Domain Context**: A movement for the human future in the age of AI. Quarterly gatherings and Human Notes for people who refuse to let progress be anything...
- **Primary Substrate**: `#e5e7eb` (`:after { border: #e5e7eb }`), **Primary Ink**: `#fff3`, **Accent / Highlight**: `#fff9`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#e5e7eb` (`:after { border: #e5e7eb }`) paired with `#fff3` primary typography and `#fff9` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Bebas Neue` for display copy (`Our Story`) with `Instrument Sans` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `640px` container bounds (`gap: .25rem`, padding `.25rem`) with `cubic-bezier(.4,0,.6,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-rebelliously-optimistic-com` in your global stylesheet:

:root {
  /* Rebelliously Optimistic — A movement for the human future (www-rebelliously-optimistic-com) — Ground-Truth Extracted CSS Variables */
  --line: #3e1c2a40; /* Color / Atmospheric Token (www-rebelliously-optimistic-com) */
  --line-soft: #3e1c2a1f; /* Color / Atmospheric Token (www-rebelliously-optimistic-com) */
  --line-faint: #3e1c2a14; /* Color / Atmospheric Token (www-rebelliously-optimistic-com) */
  --line-cream: #f3ebd938; /* Color / Atmospheric Token (www-rebelliously-optimistic-com) */
  --line-cream-soft: #f3ebd91f; /* Color / Atmospheric Token (www-rebelliously-optimistic-com) */
  --tw-border-spacing-x: 0; /* Layout / Spatial Grid Token (www-rebelliously-optimistic-com) */
  --tw-border-spacing-y: 0; /* Layout / Spatial Grid Token (www-rebelliously-optimistic-com) */
  --tw-translate-x: 0; /* Design System Custom Token (www-rebelliously-optimistic-com) */
  --tw-translate-y: 0; /* Design System Custom Token (www-rebelliously-optimistic-com) */
  --tw-rotate: 0; /* Design System Custom Token (www-rebelliously-optimistic-com) */
  --tw-skew-x: 0; /* Design System Custom Token (www-rebelliously-optimistic-com) */
  --tw-skew-y: 0; /* Design System Custom Token (www-rebelliously-optimistic-com) */
  --tw-scale-x: 1; /* Design System Custom Token (www-rebelliously-optimistic-com) */
  --tw-scale-y: 1; /* Design System Custom Token (www-rebelliously-optimistic-com) */
  --www-rebelliously-bg: #e5e7eb; /* Canvas Substrate (from `:after { border: #e5e7eb }`) (www-rebelliously-optimistic-com) */
  --www-rebelliously-ink: #fff3; /* Primary Typography Ink (stylesheet-derived) (www-rebelliously-optimistic-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#e5e7eb` — grounded in `:after { border: #e5e7eb }`
- **Primary Typography Ink**: `#9ca3af` — grounded in `input::-moz-placeholder { color: #9ca3af }`
- **Elevated Surface / Card Substrate**: `#fff3` — grounded in `20 { border-color: #fff3 }`
- **Interactive Accent / Highlight**: `#fff9` — grounded in `60 { border-color: #fff9 }`
- **Secondary / Muted Copy**: `#0003` — grounded in `20 { background-color: #0003 }`
- **Structural Hairline Border**: `#0000` — grounded in `.bg-transparent { background-color: #0000 }`
- **Variable Token (`--line`)**: `#3e1c2a40` — grounded in `var(--line)` in `:root`
- **Variable Token (`--line-soft`)**: `#3e1c2a1f` — grounded in `var(--line-soft)` in `:root`
- **Variable Token (`--line-faint`)**: `#3e1c2a14` — grounded in `var(--line-faint)` in `:root`
- **Variable Token (`--line-cream`)**: `#f3ebd938` — grounded in `var(--line-cream)` in `:root`
- **Variable Token (`--line-cream-soft`)**: `#f3ebd91f` — grounded in `var(--line-cream-soft)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `640px` extracted from `www-rebelliously-optimistic-com` stylesheet
- **Padding & Gutters**: `.25rem` lateral canvas padding with `.25rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 640px`, `gap: .25rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `.25rem` horizontal padding
- **Media Queries**: `@media (width>=640px)`, `@media (width>=768px)`, `@media (width>=1024px)`, `@media (width>=1280px)`
- **Corner Radii**: `.25rem`, `1rem`, `14px`, `20px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Bebas Neue`
- **Body Font Stack**: `Instrument Sans`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `1.5rem`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `1.5rem`)
- **Body Copy Rule**: rule `p` (`font-size: calc(6em + 13.3px)`, `font-weight: 400`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `1.5rem`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-rebelliously-optimistic-com` (`Rebelliously Optimistic — A movement for the human future`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.fixed> — `www-rebelliously-optimistic-com`)**:
   - DOM & Selectors: Landmark `<header class="fixed top-0">` hosting `Rebelliously Optimistic — A movement` navigation (`The Experience · Human Notes`), DOM attributes (`data-sdkn="@vercel/analytics/react"`, `data-sdkv="2.0.1"`, `data-engine="three.js r184"`), and stylesheet rule `after { box-sizing:border-box;border:0 solid e5e7eb }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.fixed> — `www-rebelliously-optimistic-com`)` (`www-rebelliously-optimistic-com`) adapts across `@media (width>=640px)`, `@media (width>=768px)`, `@media (width>=1024px)`, `@media (width>=1280px)` with `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.22,1,.36,1)` transitions and links `The Experience · Human Notes`.
2. **Hero Stage & Focal Lead (<section.hidden> — `Our Story`)**:
   - DOM & Selectors: Landmark `<section class="hidden relative">` presenting display lead `Our Story` and copy excerpt *"Rebelliously Optimistic."* over `#e5e7eb` canvas and `#fff3` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#e5e7eb` background with `#fff3` headline `Our Story`.
3. **Primary Showcase & Content Grid (<section.relative> — `Four commitments. One movement.`)**:
   - DOM & Selectors: Landmark `<section class="relative w-full">` rendering section `Four commitments. One movement.` with copy *"Become a partner Partner"*, asset references (`favicon.svg`, `favicon-32.png`, `favicon-16.png`, `apple-touch-icon.png`), and grid rule `body { line-height:inherit;margin:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.relative> — `Four commitments. One movement.`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 640px`, `gap: .25rem`) on desktop and Single-column vertical stack at `390px` viewport width with `.25rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.relative> — `Build human-first`)**:
   - DOM & Selectors: Landmark `<section class="relative z-10">` framing `Build human-first` and `the Experience` (*"Elevating shared humanity in the age of AI."*) with `#fff3` surface cards, `#fff9` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.relative> — `Build human-first`)` uses `.25rem`, `1rem`, `14px`, `20px` radii, `#fff9` highlights, and assets (favicon.svg, favicon-32.png, favicon-16.png).
5. **Colophon & Global Directory Footer (<footer.sticky> — `https://www.rebelliously-optimistic.com/`)**:
   - DOM & Selectors: Landmark `<footer class="sticky bottom-0">` anchoring `Rebelliously Optimistic — A move` footer links (`The Experience · Human Notes`), copy *"W r i t e i t i n a h u m a n v o i c e ."*, and `#0000` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.sticky> — `https://www.rebelliously-optimistic.com/`)` aligns to `640px` extracted from `www-rebelliously-optimistic-com` stylesheet with `.25rem` lateral canvas padding with `.25rem` grid gap and attributes (data-sdkn="@vercel/analytics/react", data-sdkv="2.0.1", data-engine="three.js r184").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Rebelliously Optimistic."*
- Copy Excerpt 2: *"Become a partner Partner"*
- Copy Excerpt 3: *"Elevating shared humanity in the age of AI."*
- Copy Excerpt 4: *"W r i t e i t i n a h u m a n v o i c e ."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.22,1,.36,1)`
- **Extracted Stylesheet Rules (`www-rebelliously-optimistic-com`)**:
- `after { box-sizing:border-box;border:0 solid e5e7eb }`
- `body { line-height:inherit;margin:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- `sup { vertical-align:baseline;font-size:75%;line-height:0;position:relative }`
- **Per-Selector Transition Rules**:
- **Selector `.transition`**: `transition: .15s` extracted from `www-rebelliously-optimistic-com` stylesheet.
- **Selector `box-shadow\]`**: `transition: .15s` extracted from `www-rebelliously-optimistic-com` stylesheet.
- **Selector `.transition-all`**: `transition: .15s` extracted from `www-rebelliously-optimistic-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.6,1)`)**: Governs interactive state transitions across `<header.fixed>` and `<section.relative>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-rebelliously-optimistic-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
