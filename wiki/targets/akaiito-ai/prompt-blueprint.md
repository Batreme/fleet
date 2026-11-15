---
title: "UI Prompt Blueprint: akaiito-ai"
date: 2026-11-15
target: "[[overview|akaiito-ai]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#ecebe5` / `#e4322b`)"
---

# UI Design System & Master Generation Blueprint: akaiito-ai

> **Akai Ito — Your twin dates millions. You go on one date.** (https://akaiito.ai) — Akai Ito builds a digital twin of you. It goes on millions of first dates, lives ten thousand lives with your best match, then books one...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Akai Ito — Your twin dates millions. You go on one date.** (`https://akaiito.ai`). Akai Ito builds a digital twin of you. It goes on millions of first dates, lives ten thousand lives with your best match, then books one...
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#ecebe5` / `#e4322b`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#ecebe5` (`var(--paper)` in `:root`) paired with `#111113` primary typography and `#e4322b` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Geist Fallback` for display copy (`Akai Ito — your twin dates millions.`) with `Geist` and `Geist Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `40ch` container bounds (`gap: .75rem`, padding `.5rem`) with `cubic-bezier(.2,.7,.1,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `40ch` extracted from `akaiito-ai` stylesheet.
- **Canvas Lateral Padding & Spacing**: `.5rem` lateral canvas padding with `.75rem` grid gap.
- **Border Radius Scale**: `50%`, `62.4375rem`, `1.5rem`, `.75rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40ch`, `gap: .75rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `.5rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:1500px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:900px)`, `@media (max-width:56.25rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ecebe5` | `var(--paper)` in `:root` |
| **Primary Typography Ink** | `#111113` | `var(--ink)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fbfaf7` | `var(--card)` in `:root` |
| **Interactive Accent / Highlight** | `#e4322b` | `var(--red)` in `:root` |
| **Secondary / Muted Copy** | `#6f6e6a` | `var(--muted)` in `:root` |
| **Structural Hairline Border** | `#1a73e8` | `var(--blue)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--fit` | `1` | Design System Custom Token |
| `--paper` | `#ecebe5` | Canvas / Surface Token |
| `--ink` | `#111113` | Typography Ink Token |
| `--card` | `#fbfaf7` | Color / Atmospheric Token |
| `--red` | `#e4322b` | Color / Atmospheric Token |
| `--muted` | `#6f6e6a` | Color / Atmospheric Token |
| `--line` | `rgba(17,17,19,.12)` | Color / Atmospheric Token |
| `--blue` | `#1a73e8` | Color / Atmospheric Token |
| `--sans` | `"Geist","Geist Fallback","Inter",system-ui,-apple-system,sans-serif` | Typography / Scale Token |
| `--mono` | `"Geist","Geist Fallback","Inter",system-ui,sans-serif` | Typography / Scale Token |
| `--ii` | `clamp(1.125rem, 2.4vw, 1.875rem)` | Dimension / Scale Token |
| `--tr` | `-.8deg` | Design System Custom Token |
| `--nf` | `var(--ink)` | Design System Custom Token |
| `--nr` | `-1.2deg` | Design System Custom Token |
| `--cr` | `1.6deg` | Design System Custom Token |
| `--bg` | `#ecebe5` | Canvas / Surface Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Geist Fallback`.
- **Primary Body Stack**: `Geist`.
- **Technical / Metadata Stack**: `Geist Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`, `clamp(3rem, 7vw, 7.75rem)`, `clamp(2.375rem, 5vw, 5.5rem)`, `clamp(1.75rem, 2.6vw, 2.75rem)`, `clamp(1rem, 1.3vw, 1.25rem)`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(44px, 6.4vw, 120px)`).
- **Body Copy**: rule `p` (`font-size: .9375rem`).
- **Metadata & Navigation Labels**: CSS variables `--mono: "Geist","Geist Fallback","Inter",system-ui,sans-serif`; rule `small` (`font-size: .74rem`, `line-height: 1.25`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.2,.7,.1,1)`, `cubic-bezier(.2,1.3,.35,1)`, `cubic-bezier(.2,1.45,.35,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.nav`**: `transition: translate .45s cubic-bezier(.2,.7,.1,1),padding .4s` extracted from `akaiito-ai` stylesheet.
- **Selector `.btn`**: `transition: transform .25s cubic-bezier(.2,.7,.1,1)` extracted from `akaiito-ai` stylesheet.
- **Selector `.ln`**: `transition: transform .55s cubic-bezier(.2,.7,.1,1),opacity .4s` extracted from `akaiito-ai` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.2,.7,.1,1)`)**: Governs interactive state transitions across `<header.ahd>` and `<section.hero>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Akai Ito — Your twin dates millions. You g │
│ ====================================================================== │
│ [ <header.ahd>             | Akai Ito · App · How it works · The mo ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.sec>                                        |   │
│ | H1: Akai Ito — your twin dates millions. You go on on...         |   │
│ | Substrate: #ecebe5    | Ink: #111113    | Accent: #e4322b        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.hero>            ) max-w: 40ch           |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Your twin dates millions. Yo |  | 1 window awake on this block | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .75rem) | │
│ | [<header.ahd>] -> [<section.sec>] -> [<section.hero>] |              │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.anim-off>     ) | https://akaiito.ai                 │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.ahd> — `akaiito-ai`)**:
   - Landmark `<header class="ahd">` hosting `Akai Ito — Your twin dates millions.` navigation (`Akai Ito · App · How it works · The model · Simulation`), DOM attributes (`data-slot="head"`, `data-d="-1"`, `data-d="1"`, `data-slot="body"`), and stylesheet rule `html { background:var(--paper);font-size:16px;overflow-x:clip }`.
2. **Hero Stage & Focal Lead (<section.sec> — `Akai Ito — your twin dates million`)**:
   - Landmark `<section class="sec opener">` presenting display lead `Akai Ito — your twin dates millions. You go on on...` and copy excerpt *"100% · Tying the thread"* over `#ecebe5` canvas and `#111113` ink.
3. **Primary Showcase & Content Grid (<section.hero> — `Your twin dates millions. You go o`)**:
   - Landmark `<section class="hero sec">` rendering section `Your twin dates millions. You go on one date.` with copy *"Akai Ito is for grown-ups. Are you 18 or older?"*, asset references (`icon.webp`, `favicon.png`, `apple-touch.png`, `phone.webp`), and grid rule `body { overflow-x:clip }`.
4. **Interactive Detail & Feature Matrix (<section.sec> — `1 window awake on this block Every`)**:
   - Landmark `<section class="sec appsec">` framing `1 window awake on this block Everyone you could l...` and `Your twin lives in your pocket.` (*"Come back on your 18th birthday. Your twin will wait."*) with `#fbfaf7` surface cards, `#e4322b` accents, and `stage { position:fixed;inset:0;width:100%;height:100%;display:block;z-index:0 }`.
5. **Colophon & Global Directory Footer (<footer.anim-off> — `https://akaiito.ai`)**:
   - Landmark `<footer class="anim-off">` anchoring `Akai Ito — Your twin dates milli` footer links (`Akai Ito · App · How it works · The model · Simulation`), copy *"Akai Ito is a concept for an AI dating service. You connect "*, and `#1a73e8` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: akaiito-ai (Akai Ito — Your twin dates millions. You go on one date.)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `akaiito-ai` (**Akai Ito — Your twin dates millions. You go on one date.** — `https://akaiito.ai`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ecebe5` / `#e4322b`).
- **Identity & Domain Context**: Akai Ito builds a digital twin of you. It goes on millions of first dates, lives ten thousand lives with your best match, then books one...
- **Primary Substrate**: `#ecebe5` (`var(--paper)` in `:root`), **Primary Ink**: `#111113`, **Accent / Highlight**: `#e4322b`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#ecebe5` (`var(--paper)` in `:root`) paired with `#111113` primary typography and `#e4322b` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Geist Fallback` for display copy (`Akai Ito — your twin dates millions.`) with `Geist` and `Geist Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `40ch` container bounds (`gap: .75rem`, padding `.5rem`) with `cubic-bezier(.2,.7,.1,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `akaiito-ai` in your global stylesheet:

:root {
  /* Akai Ito — Your twin dates millions. You go on one date. (akaiito-ai) — Ground-Truth Extracted CSS Variables */
  --fit: 1; /* Design System Custom Token (akaiito-ai) */
  --paper: #ecebe5; /* Canvas / Surface Token (akaiito-ai) */
  --ink: #111113; /* Typography Ink Token (akaiito-ai) */
  --card: #fbfaf7; /* Color / Atmospheric Token (akaiito-ai) */
  --red: #e4322b; /* Color / Atmospheric Token (akaiito-ai) */
  --muted: #6f6e6a; /* Color / Atmospheric Token (akaiito-ai) */
  --line: rgba(17,17,19,.12); /* Color / Atmospheric Token (akaiito-ai) */
  --blue: #1a73e8; /* Color / Atmospheric Token (akaiito-ai) */
  --sans: "Geist","Geist Fallback","Inter",system-ui,-apple-system,sans-serif; /* Typography / Scale Token (akaiito-ai) */
  --mono: "Geist","Geist Fallback","Inter",system-ui,sans-serif; /* Typography / Scale Token (akaiito-ai) */
  --ii: clamp(1.125rem, 2.4vw, 1.875rem); /* Dimension / Scale Token (akaiito-ai) */
  --tr: -.8deg; /* Design System Custom Token (akaiito-ai) */
  --nf: var(--ink); /* Design System Custom Token (akaiito-ai) */
  --nr: -1.2deg; /* Design System Custom Token (akaiito-ai) */
  --cr: 1.6deg; /* Design System Custom Token (akaiito-ai) */
  --bg: #ecebe5; /* Canvas / Surface Token (akaiito-ai) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ecebe5` — grounded in `var(--paper)` in `:root`
- **Primary Typography Ink**: `#111113` — grounded in `var(--ink)` in `:root`
- **Elevated Surface / Card Substrate**: `#fbfaf7` — grounded in `var(--card)` in `:root`
- **Interactive Accent / Highlight**: `#e4322b` — grounded in `var(--red)` in `:root`
- **Secondary / Muted Copy**: `#6f6e6a` — grounded in `var(--muted)` in `:root`
- **Structural Hairline Border**: `#1a73e8` — grounded in `var(--blue)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `40ch` extracted from `akaiito-ai` stylesheet
- **Padding & Gutters**: `.5rem` lateral canvas padding with `.75rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40ch`, `gap: .75rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `.5rem` horizontal padding
- **Media Queries**: `@media (min-width:1500px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:900px)`, `@media (max-width:56.25rem)`
- **Corner Radii**: `50%`, `62.4375rem`, `1.5rem`, `.75rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Geist Fallback`
- **Body Font Stack**: `Geist`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`, `clamp(3rem, 7vw, 7.75rem)`, `clamp(2.375rem, 5vw, 5.5rem)`, `clamp(1.75rem, 2.6vw, 2.75rem)`, `clamp(1rem, 1.3vw, 1.25rem)`)
- **H2 Section Rule**: rule `h2` (`font-size: clamp(44px, 6.4vw, 120px)`)
- **Body Copy Rule**: rule `p` (`font-size: .9375rem`)
- **Metadata & Index Rule**: CSS variables `--mono: "Geist","Geist Fallback","Inter",system-ui,sans-serif`; rule `small` (`font-size: .74rem`, `line-height: 1.25`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `akaiito-ai` (`Akai Ito — Your twin dates millions. You go on one date.`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.ahd> — `akaiito-ai`)**:
   - DOM & Selectors: Landmark `<header class="ahd">` hosting `Akai Ito — Your twin dates millions.` navigation (`Akai Ito · App · How it works · The model · Simulation`), DOM attributes (`data-slot="head"`, `data-d="-1"`, `data-d="1"`, `data-slot="body"`), and stylesheet rule `html { background:var(--paper);font-size:16px;overflow-x:clip }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.ahd> — `akaiito-ai`)` (`akaiito-ai`) adapts across `@media (min-width:1500px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:900px)`, `@media (max-width:56.25rem)` with `cubic-bezier(.2,.7,.1,1)`, `cubic-bezier(.2,1.3,.35,1)`, `cubic-bezier(.2,1.45,.35,1)` transitions and links `Akai Ito · App · How it works · The model · Simulation`.
2. **Hero Stage & Focal Lead (<section.sec> — `Akai Ito — your twin dates million`)**:
   - DOM & Selectors: Landmark `<section class="sec opener">` presenting display lead `Akai Ito — your twin dates millions. You go on on...` and copy excerpt *"100% · Tying the thread"* over `#ecebe5` canvas and `#111113` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#ecebe5` background with `#111113` headline `Akai Ito — your twin dates millions. You go on on...`.
3. **Primary Showcase & Content Grid (<section.hero> — `Your twin dates millions. You go o`)**:
   - DOM & Selectors: Landmark `<section class="hero sec">` rendering section `Your twin dates millions. You go on one date.` with copy *"Akai Ito is for grown-ups. Are you 18 or older?"*, asset references (`icon.webp`, `favicon.png`, `apple-touch.png`, `phone.webp`), and grid rule `body { overflow-x:clip }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.hero> — `Your twin dates millions. You go o`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40ch`, `gap: .75rem`) on desktop and Single-column vertical stack at `390px` viewport width with `.5rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.sec> — `1 window awake on this block Every`)**:
   - DOM & Selectors: Landmark `<section class="sec appsec">` framing `1 window awake on this block Everyone you could l...` and `Your twin lives in your pocket.` (*"Come back on your 18th birthday. Your twin will wait."*) with `#fbfaf7` surface cards, `#e4322b` accents, and `stage { position:fixed;inset:0;width:100%;height:100%;display:block;z-index:0 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.sec> — `1 window awake on this block Every`)` uses `50%`, `62.4375rem`, `1.5rem`, `.75rem` radii, `#e4322b` highlights, and assets (icon.webp, favicon.png, apple-touch.png).
5. **Colophon & Global Directory Footer (<footer.anim-off> — `https://akaiito.ai`)**:
   - DOM & Selectors: Landmark `<footer class="anim-off">` anchoring `Akai Ito — Your twin dates milli` footer links (`Akai Ito · App · How it works · The model · Simulation`), copy *"Akai Ito is a concept for an AI dating service. You connect "*, and `#1a73e8` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.anim-off> — `https://akaiito.ai`)` aligns to `40ch` extracted from `akaiito-ai` stylesheet with `.5rem` lateral canvas padding with `.75rem` grid gap and attributes (data-slot="head", data-d="-1", data-d="1").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"100% · Tying the thread"*
- Copy Excerpt 2: *"Akai Ito is for grown-ups. Are you 18 or older?"*
- Copy Excerpt 3: *"Come back on your 18th birthday. Your twin will wait."*
- Copy Excerpt 4: *"Akai Ito is a concept for an AI dating service. You connect the apps you already u..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.2,.7,.1,1)`, `cubic-bezier(.2,1.3,.35,1)`, `cubic-bezier(.2,1.45,.35,1)`
- **Extracted Stylesheet Rules (`akaiito-ai`)**:
- `html { background:var(--paper);font-size:16px;overflow-x:clip }`
- `body { overflow-x:clip }`
- `stage { position:fixed;inset:0;width:100%;height:100%;display:block;z-index:0 }`
- `flow { position:fixed;inset:0;width:100%;height:100%;z-index:2;pointer-events:none }`
- `main { position:relative;z-index:1 }`
- **Per-Selector Transition Rules**:
- **Selector `.nav`**: `transition: translate .45s cubic-bezier(.2,.7,.1,1),padding .4s` extracted from `akaiito-ai` stylesheet.
- **Selector `.btn`**: `transition: transform .25s cubic-bezier(.2,.7,.1,1)` extracted from `akaiito-ai` stylesheet.
- **Selector `.ln`**: `transition: transform .55s cubic-bezier(.2,.7,.1,1),opacity .4s` extracted from `akaiito-ai` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.2,.7,.1,1)`)**: Governs interactive state transitions across `<header.ahd>` and `<section.hero>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `akaiito-ai`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
