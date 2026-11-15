---
title: "UI Prompt Blueprint: gracefashion-ai"
date: 2026-11-15
target: "gracefashion-ai"
status: analyzed
capture: specimen
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#d1d3d4` accent)"
---

# UI Design System & Master Generation Blueprint: gracefashion-ai

> **KI-Fotostudio für Mode: Bilder ohne Shooting · grace ai** (https://gracefashion.ai) — KI-Modefotografie aus deinen eigenen Teilen: On-Model-Bilder, Kampagnen und Videos. Als Software oder als Service, rund 80 Prozent unter...

![Desktop Design Specimen (Offline WebGL/JS Fallback — not live site capture)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **KI-Fotostudio für Mode: Bilder ohne Shooting · grace ai** (`https://gracefashion.ai`). KI-Modefotografie aus deinen eigenen Teilen: On-Model-Bilder, Kampagnen und Videos. Als Software oder als Service, rund 80 Prozent unter...
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#d1d3d4` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--color-black)` in `:root`) paired with `#fff` primary typography and `#d1d3d4` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Instrument Sans` for display copy (`KI-Fotostudio für Modemarken: Softwa`) with `Instrument Sans Fallback` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `640px` container bounds (`gap: .125rem`, padding `.25rem`) with `cubic-bezier(.4,0,.6,1)` easing.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Design Specimen (Offline WebGL/JS Fallback — not live site capture)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `640px` extracted from `gracefashion-ai` stylesheet.
- **Canvas Lateral Padding & Spacing**: `.25rem` lateral canvas padding with `.125rem` grid gap.
- **Border Radius Scale**: `.25rem`, `1rem`, `10px`, `22%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 640px`, `gap: .125rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `.25rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:640px)`, `@media (min-width:768px)`, `@media (min-width:1024px)`, `@media (min-width:1280px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#808285` | `var(--color-cool-gray)` in `:root` |
| **Interactive Accent / Highlight** | `#d1d3d4` | `var(--color-light-gray)` in `:root` |
| **Secondary / Muted Copy** | `#a7a9ac` | `var(--color-warm-gray)` in `:root` |
| **Structural Hairline Border** | `#e5e7eb` | `:after { border: #e5e7eb }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-instrument-sans` | `"Instrument Sans", "Instrument Sans Fallback"` | Typography / Scale Token |
| `--font-space-grotesk` | `"Space Grotesk", "Space Grotesk Fallback"` | Typography / Scale Token |
| `--ai-mark-w` | `70vw` | Dimension / Scale Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--color-cool-gray` | `#808285` | Brand / Palette Token |
| `--color-light-gray` | `#d1d3d4` | Canvas / Surface Token |
| `--color-warm-gray` | `#a7a9ac` | Brand / Palette Token |
| `--font-sans` | `var(--font-instrument-sans), "Instrument Sans", sans-serif` | Typography / Scale Token |
| `--font-display` | `var(--font-sans)` | Typography / Scale Token |
| `--orbit-frame` | `min(21vh, 16vw, 290px)` | Dimension / Scale Token |
| `--tw-border-spacing-x` | `0` | Layout / Spatial Grid Token |
| `--tw-border-spacing-y` | `0` | Layout / Spatial Grid Token |
| `--tw-translate-x` | `0` | Design System Custom Token |
| `--gracefashion-ai-bg` | `#000` | Canvas Substrate (from `var(--color-black)` in `:root`) |
| `--gracefashion-ai-ink` | `#fff` | Primary Typography Ink (stylesheet-derived) |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Instrument Sans`.
- **Primary Body Stack**: `Instrument Sans Fallback`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--font-display: var(--font-sans)`.
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(21px,16.62px + 1.124vw,...`, `line-height: 1.15`, `letter-spacing: -.026em`, `font-weight: 500`).
- **Body Copy**: rule `p` (`font-size: 18px`, `line-height: 1.5`, `letter-spacing: -.011em`, `font-weight: 400`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `clamp(32px,17.1px + 3.82vw,66px)`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.16,1,.3,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.transition`**: `transition: .15s` extracted from `gracefashion-ai` stylesheet.
- **Selector `.transition-\[fill\]`**: `transition: .15s` extracted from `gracefashion-ai` stylesheet.
- **Selector `.transition-\[filter\]`**: `transition: .15s` extracted from `gracefashion-ai` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.6,1)`)**: Governs interactive state transitions across `<nav.fixed>` and `<section.bg-black>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.page-surface>` and `<section.bg-black>` interactive targets.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — KI-Fotostudio für Mode: Bilder ohne Shooti │
│ ====================================================================== │
│ [ <nav.fixed>              | Software · Service · Ratgeber · Team · ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.page-surface>                               |   │
│ | H1: KI-Fotostudio für Modemarken: Software und Servic...         |   │
│ | Substrate: #000       | Ink: #fff       | Accent: #d1d3d4        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.bg-black>        ) max-w: 640px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Du entscheidest, was die Wel |  | Jedes Detail sitzt.          | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .125re) | │
│ | [<nav.fixed>] -> [<section.page-surf] -> [<section.bg-black>] |      │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.relative>     ) | https://gracefashion.ai            │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.fixed> — `gracefashion-ai`)**:
   - Landmark `<nav class="fixed top-0">` hosting `KI-Fotostudio für Mode: Bilder ohne ` navigation (`Software · Service · Ratgeber · Team · Demo buchen`), DOM attributes (`data-precedence="next"`), and stylesheet rule `.vGn8MW_className { font-family:Instrument Sans,Instrument Sans Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.page-surface> — `KI-Fotostudio für Modemarken: Soft`)**:
   - Landmark `<section class="page-surface px-8">` presenting display lead `KI-Fotostudio für Modemarken: Software und Servic...` and copy excerpt *"Wir verwenden Cookies 🍪"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.bg-black> — `Du entscheidest, was die Welt sehe`)**:
   - Landmark `<section class="bg-black">` rendering section `Du entscheidest, was die Welt sehen und tragen soll.` with copy *"Wir nutzen Cookies, um Ihre Erfahrung zu verbessern, das Nutzerve"*, asset references (`237858b39a32779d-s.p.1ii7211jqpzi...`, `4cf231d25563e07b-s.p.3uuun_-7zsf1...`, `62f37606a5bd6f6f-s.p.3wn_q526zaol...`, `92b6de9cb55945e2-s.p.44ks8kcggj01...`), and grid rule `.vGn8MW_variable { --font-instrument-sans:"Instrument Sans", "Instrument Sans Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.relative> — `Jedes Detail sitzt.`)**:
   - Landmark `<section class="relative h-screen">` framing `Jedes Detail sitzt.` and `Dasselbe Model. Jede Szene.` (*"Datenschutzerklärung"*) with `#808285` surface cards, `#d1d3d4` accents, and `.wdTYSa_className { font-family:Space Grotesk,Space Grotesk Fallback;font-style:normal }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://gracefashion.ai`)**:
   - Landmark `<footer class="relative text-white">` anchoring `KI-Fotostudio für Mode: Bilder o` footer links (`Software · Service · Ratgeber · Team · Demo buchen`), copy *"Ein Studio ohne Set."*, and `#e5e7eb` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: gracefashion-ai (KI-Fotostudio für Mode: Bilder ohne Shooting · grace ai)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `gracefashion-ai` (**KI-Fotostudio für Mode: Bilder ohne Shooting · grace ai** — `https://gracefashion.ai`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#d1d3d4` accent).
- **Identity & Domain Context**: KI-Modefotografie aus deinen eigenen Teilen: On-Model-Bilder, Kampagnen und Videos. Als Software oder als Service, rund 80 Prozent unter...
- **Primary Substrate**: `#000` (`var(--color-black)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#d1d3d4`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--color-black)` in `:root`) paired with `#fff` primary typography and `#d1d3d4` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Instrument Sans` for display copy (`KI-Fotostudio für Modemarken: Softwa`) with `Instrument Sans Fallback` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `640px` container bounds (`gap: .125rem`, padding `.25rem`) with `cubic-bezier(.4,0,.6,1)` easing.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `gracefashion-ai` in your global stylesheet:

:root {
  /* KI-Fotostudio für Mode: Bilder ohne Shooting · grace ai (gracefashion-ai) — Ground-Truth Extracted CSS Variables */
  --font-instrument-sans: "Instrument Sans", "Instrument Sans Fallback"; /* Typography / Scale Token (gracefashion-ai) */
  --font-space-grotesk: "Space Grotesk", "Space Grotesk Fallback"; /* Typography / Scale Token (gracefashion-ai) */
  --ai-mark-w: 70vw; /* Dimension / Scale Token (gracefashion-ai) */
  --color-black: #000; /* Canvas / Surface Token (gracefashion-ai) */
  --color-white: #fff; /* Canvas / Surface Token (gracefashion-ai) */
  --color-cool-gray: #808285; /* Brand / Palette Token (gracefashion-ai) */
  --color-light-gray: #d1d3d4; /* Canvas / Surface Token (gracefashion-ai) */
  --color-warm-gray: #a7a9ac; /* Brand / Palette Token (gracefashion-ai) */
  --font-sans: var(--font-instrument-sans), "Instrument Sans", sans-serif; /* Typography / Scale Token (gracefashion-ai) */
  --font-display: var(--font-sans); /* Typography / Scale Token (gracefashion-ai) */
  --orbit-frame: min(21vh, 16vw, 290px); /* Dimension / Scale Token (gracefashion-ai) */
  --tw-border-spacing-x: 0; /* Layout / Spatial Grid Token (gracefashion-ai) */
  --tw-border-spacing-y: 0; /* Layout / Spatial Grid Token (gracefashion-ai) */
  --tw-translate-x: 0; /* Design System Custom Token (gracefashion-ai) */
  --gracefashion-ai-bg: #000; /* Canvas Substrate (from `var(--color-black)` in `:root`) (gracefashion-ai) */
  --gracefashion-ai-ink: #fff; /* Primary Typography Ink (stylesheet-derived) (gracefashion-ai) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000` — grounded in `var(--color-black)` in `:root`
- **Primary Typography Ink**: `#fff` — grounded in `var(--color-white)` in `:root`
- **Elevated Surface / Card Substrate**: `#808285` — grounded in `var(--color-cool-gray)` in `:root`
- **Interactive Accent / Highlight**: `#d1d3d4` — grounded in `var(--color-light-gray)` in `:root`
- **Secondary / Muted Copy**: `#a7a9ac` — grounded in `var(--color-warm-gray)` in `:root`
- **Structural Hairline Border**: `#e5e7eb` — grounded in `:after { border: #e5e7eb }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `640px` extracted from `gracefashion-ai` stylesheet
- **Padding & Gutters**: `.25rem` lateral canvas padding with `.125rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 640px`, `gap: .125rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `.25rem` horizontal padding
- **Media Queries**: `@media (min-width:640px)`, `@media (min-width:768px)`, `@media (min-width:1024px)`, `@media (min-width:1280px)`
- **Corner Radii**: `.25rem`, `1rem`, `10px`, `22%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Instrument Sans`
- **Body Font Stack**: `Instrument Sans Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: CSS variables `--font-display: var(--font-sans)`
- **H2 Section Rule**: rule `h2` (`font-size: clamp(21px,16.62px + 1.124vw,...`, `line-height: 1.15`, `letter-spacing: -.026em`, `font-weight: 500`)
- **Body Copy Rule**: rule `p` (`font-size: 18px`, `line-height: 1.5`, `letter-spacing: -.011em`, `font-weight: 400`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `clamp(32px,17.1px + 3.82vw,66px)`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `gracefashion-ai` (`KI-Fotostudio für Mode: Bilder ohne Shooting · grace ai`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.fixed> — `gracefashion-ai`)**:
   - DOM & Selectors: Landmark `<nav class="fixed top-0">` hosting `KI-Fotostudio für Mode: Bilder ohne ` navigation (`Software · Service · Ratgeber · Team · Demo buchen`), DOM attributes (`data-precedence="next"`), and stylesheet rule `.vGn8MW_className { font-family:Instrument Sans,Instrument Sans Fallback;font-style:normal }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.fixed> — `gracefashion-ai`)` (`gracefashion-ai`) adapts across `@media (min-width:640px)`, `@media (min-width:768px)`, `@media (min-width:1024px)`, `@media (min-width:1280px)` with `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.16,1,.3,1)` transitions and links `Software · Service · Ratgeber · Team · Demo buchen`.
2. **Hero Stage & Focal Lead (<section.page-surface> — `KI-Fotostudio für Modemarken: Soft`)**:
   - DOM & Selectors: Landmark `<section class="page-surface px-8">` presenting display lead `KI-Fotostudio für Modemarken: Software und Servic...` and copy excerpt *"Wir verwenden Cookies 🍪"* over `#000` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#000` background with `#fff` headline `KI-Fotostudio für Modemarken: Software und Servic...`.
3. **Primary Showcase & Content Grid (<section.bg-black> — `Du entscheidest, was die Welt sehe`)**:
   - DOM & Selectors: Landmark `<section class="bg-black">` rendering section `Du entscheidest, was die Welt sehen und tragen soll.` with copy *"Wir nutzen Cookies, um Ihre Erfahrung zu verbessern, das Nutzerve"*, asset references (`237858b39a32779d-s.p.1ii7211jqpzi...`, `4cf231d25563e07b-s.p.3uuun_-7zsf1...`, `62f37606a5bd6f6f-s.p.3wn_q526zaol...`, `92b6de9cb55945e2-s.p.44ks8kcggj01...`), and grid rule `.vGn8MW_variable { --font-instrument-sans:"Instrument Sans", "Instrument Sans Fallback" }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.bg-black> — `Du entscheidest, was die Welt sehe`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 640px`, `gap: .125rem`) on desktop and Single-column vertical stack at `390px` viewport width with `.25rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.relative> — `Jedes Detail sitzt.`)**:
   - DOM & Selectors: Landmark `<section class="relative h-screen">` framing `Jedes Detail sitzt.` and `Dasselbe Model. Jede Szene.` (*"Datenschutzerklärung"*) with `#808285` surface cards, `#d1d3d4` accents, and `.wdTYSa_className { font-family:Space Grotesk,Space Grotesk Fallback;font-style:normal }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.relative> — `Jedes Detail sitzt.`)` uses `.25rem`, `1rem`, `10px`, `22%` radii, `#d1d3d4` highlights, and assets (237858b39a32779d-s.p.1ii7211jqpzi..., 4cf231d25563e07b-s.p.3uuun_-7zsf1..., 62f37606a5bd6f6f-s.p.3wn_q526zaol...).
5. **Colophon & Global Directory Footer (<footer.relative> — `https://gracefashion.ai`)**:
   - DOM & Selectors: Landmark `<footer class="relative text-white">` anchoring `KI-Fotostudio für Mode: Bilder o` footer links (`Software · Service · Ratgeber · Team · Demo buchen`), copy *"Ein Studio ohne Set."*, and `#e5e7eb` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.relative> — `https://gracefashion.ai`)` aligns to `640px` extracted from `gracefashion-ai` stylesheet with `.25rem` lateral canvas padding with `.125rem` grid gap and attributes (data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Wir verwenden Cookies 🍪"*
- Copy Excerpt 2: *"Wir nutzen Cookies, um Ihre Erfahrung zu verbessern, das Nutzerverhalten zu analys..."*
- Copy Excerpt 3: *"Datenschutzerklärung"*
- Copy Excerpt 4: *"Ein Studio ohne Set."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.16,1,.3,1)`
- **Extracted Stylesheet Rules (`gracefashion-ai`)**:
- `.vGn8MW_className { font-family:Instrument Sans,Instrument Sans Fallback;font-style:normal }`
- `.vGn8MW_variable { --font-instrument-sans:"Instrument Sans", "Instrument Sans Fallback" }`
- `.wdTYSa_className { font-family:Space Grotesk,Space Grotesk Fallback;font-style:normal }`
- `.wdTYSa_variable { --font-space-grotesk:"Space Grotesk", "Space Grotesk Fallback" }`
- `after { box-sizing:border-box;border:0 solid e5e7eb }`
- **Per-Selector Transition Rules**:
- **Selector `.transition`**: `transition: .15s` extracted from `gracefashion-ai` stylesheet.
- **Selector `.transition-\[fill\]`**: `transition: .15s` extracted from `gracefashion-ai` stylesheet.
- **Selector `.transition-\[filter\]`**: `transition: .15s` extracted from `gracefashion-ai` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.6,1)`)**: Governs interactive state transitions across `<nav.fixed>` and `<section.bg-black>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.page-surface>` and `<section.bg-black>` interactive targets.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `gracefashion-ai`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
