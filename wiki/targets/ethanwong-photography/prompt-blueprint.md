---
title: "UI Prompt Blueprint: ethanwong-photography"
date: 2026-11-15
target: "[[overview|ethanwong-photography]]"
status: analyzed
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#9b1120` canvas, `#8a8174` ink, `#c01f34` accent)"
---

# UI Design System & Master Generation Blueprint: ethanwong-photography

> **Ethan W · Film-Inspired Wedding & Editorial Photographer · Washington DC...** (http://ethanwong.photography) — Documentary wedding, editorial, portrait and commercial photography by Ethan Wong of Ethan W Photography. Film-inspired, vintage-leaning...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Ethan W · Film-Inspired Wedding & Editorial Photographer · Washington DC...** (`http://ethanwong.photography`). Documentary wedding, editorial, portrait and commercial photography by Ethan Wong of Ethan W Photography. Film-inspired, vintage-leaning...
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#9b1120` canvas, `#8a8174` ink, `#c01f34` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#9b1120` (`var(--red)` in `:root`) paired with `#8a8174` primary typography and `#c01f34` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Cormorant` for display copy (`Ethan W (Ethan Wong), film-inspired `) with `Pinyon Script` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `700px` container bounds (`gap: 22px`, padding `10px`) with `cubic-bezier(.16,1,.3,1)` easing and Lenis Smooth Scroll (`data-lenis`).

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `700px` extracted from `ethanwong-photography` stylesheet.
- **Canvas Lateral Padding & Spacing**: `10px` lateral canvas padding with `22px` grid gap.
- **Border Radius Scale**: `50%`, `2px`, `999px`, `10px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 700px`, `gap: 22px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `10px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:700px),(max-height:520px)`, `@media (max-width:640px),(pointer:coarse)and (max-height:520px)`, `@media (pointer:coarse)and (max-height:520px)`, `@media (min-width:1025px)and (max-height:940px)and (pointer:fine)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#9b1120` | `var(--red)` in `:root` |
| **Primary Typography Ink** | `#b3162a` | `var(--red-hover)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ab182c` | `var(--red-lift)` in `:root` |
| **Interactive Accent / Highlight** | `#c01f34` | `var(--red-lift-hover)` in `:root` |
| **Secondary / Muted Copy** | `#8a0f1e` | `var(--red-deep)` in `:root` |
| **Structural Hairline Border** | `#8a8174` | `var(--sf-ink)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--fit-lh` | `1` | Design System Custom Token |
| `--fit-reserve` | `0px` | Dimension / Scale Token |
| `--red` | `#9b1120` | Color / Atmospheric Token |
| `--red-hover` | `#b3162a` | Color / Atmospheric Token |
| `--red-lift` | `#ab182c` | Color / Atmospheric Token |
| `--red-lift-hover` | `#c01f34` | Color / Atmospheric Token |
| `--red-deep` | `#8a0f1e` | Color / Atmospheric Token |
| `--lab-nav` | `13px` | Layout / Spatial Grid Token |
| `--lab` | `12px` | Dimension / Scale Token |
| `--lab-sm` | `11px` | Dimension / Scale Token |
| `--lab-dock` | `9.5px` | Dimension / Scale Token |
| `--lab-quiet` | `10px` | Dimension / Scale Token |
| `--lab-w` | `400` | Design System Custom Token |
| `--lab-w-nav` | `400` | Layout / Spatial Grid Token |
| `--lab-w-dock` | `500` | Design System Custom Token |
| `--head-band` | `74px` | Dimension / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Cormorant`.
- **Primary Body Stack**: `Pinyon Script`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(var(--fit-min)`, `29px`, `var(--lab-nav)`, `clamp(28px,4.4vw,72px)`, `var(--lab-quiet)`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(var(--fit-min)`, `29px`, `var(--lab-nav)`, `clamp(28px,4.4vw,72px)`, `var(--lab-quiet)`).
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(var(--fit-min)`, `29px`, `var(--lab-nav)`, `clamp(28px,4.4vw,72px)`, `var(--lab-quiet)`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(var(--fit-min)`, `29px`, `var(--lab-nav)`, `clamp(28px,4.4vw,72px)`, `var(--lab-quiet)`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.55,0,1,.45)`, `cubic-bezier(.85,0,.15,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.page-shell`**: `transition: opacity .3s ease` extracted from `ethanwong-photography` stylesheet.
- **Selector `header.site .h-right`**: `transition: transform .62s cubic-bezier(.16,1,.3,1),opacity .5s ease` extracted from `ethanwong-photography` stylesheet.
- **Selector `header.site.nav-hide .h-right`**: `transition: transform .4s cubic-bezier(.16,1,.3,1),opacity .28s ease` extracted from `ethanwong-photography` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<header.site>` and `<main.idx-main>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`) with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Ethan W · Film-Inspired Wedding & Editoria │
│ ====================================================================== │
│ [ <header.site>            | Editorial Exchange                     ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <main.idx-main>                                      |   │
│ | H1: Ethan W (Ethan Wong), film-inspired documentary w...         |   │
│ | Substrate: #9b1120    | Ink: #8a8174    | Accent: #c01f34        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<main.idx-main>           ) max-w: 700px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | 01 W e d d i n g s W e d d i |  | W e d d i n g s W e d d i n  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 22px  ) | │
│ | [<header.site>] -> [<main.idx-main>] -> [<main.idx-main>] |          │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.sf>           ) | http://ethanwong.photography       │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.site> — `ethanwong-photography`)**:
   - Landmark `<header class="site nav-on-dark">` hosting `Ethan W · Film-Inspired Wedding & Ed` navigation (`Editorial Exchange`), DOM attributes (`data-cursor="always"`, `data-nav`, `data-cta-ink`, `data-nav-theme="dark"`), and stylesheet rule `html { -ms-overflow-style:none;scrollbar-width:none;-webkit-text-size-adjust:100% }`.
2. **Hero Stage & Focal Lead (<main.idx-main> — `Ethan W (Ethan Wong), film-inspire`)**:
   - Landmark `<main class="idx-main">` presenting display lead `Ethan W (Ethan Wong), film-inspired documentary w...` and copy excerpt *"01 W e d d i n g s W e d d i n g s Stories & galleries"* over `#9b1120` canvas and `#8a8174` ink.
3. **Primary Showcase & Content Grid (<main.idx-main> — `01 W e d d i n g s W e d d i n g s`)**:
   - Landmark `<main class="idx-main">` rendering section `01 W e d d i n g s W e d d i n g s Stories & gal` with copy *"W e d d i n g s W e d d i n g s"*, asset references (`favicon-32.png`, `favicon-16.png`, `favicon-32-dark.png`, `favicon-16-dark.png`), and grid rule `html::-webkit-scrollbar { display:none }`.
4. **Interactive Detail & Feature Matrix (<main.idx-main> — `W e d d i n g s W e d d i n g s`)**:
   - Landmark `<main class="idx-main">` framing `W e d d i n g s W e d d i n g s` and `Stories & galleries` (*"Stories & galleries"*) with `#ab182c` surface cards, `#c01f34` accents, and `body { background:efede7 }`.
5. **Colophon & Global Directory Footer (<footer.sf> — `http://ethanwong.photography`)**:
   - Landmark `<footer class="sf sf--fixed">` anchoring `Ethan W · Film-Inspired Wedding ` footer links (`Editorial Exchange`), copy *"All visual stories More coming"*, and `#8a8174` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: ethanwong-photography (Ethan W · Film-Inspired Wedding & Editorial Photographer · Washington DC...)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `ethanwong-photography` (**Ethan W · Film-Inspired Wedding & Editorial Photographer · Washington DC...** — `http://ethanwong.photography`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#9b1120` canvas, `#8a8174` ink, `#c01f34` accent).
- **Identity & Domain Context**: Documentary wedding, editorial, portrait and commercial photography by Ethan Wong of Ethan W Photography. Film-inspired, vintage-leaning...
- **Primary Substrate**: `#9b1120` (`var(--red)` in `:root`), **Primary Ink**: `#8a8174`, **Accent / Highlight**: `#c01f34`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#9b1120` (`var(--red)` in `:root`) paired with `#8a8174` primary typography and `#c01f34` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Cormorant` for display copy (`Ethan W (Ethan Wong), film-inspired `) with `Pinyon Script` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `700px` container bounds (`gap: 22px`, padding `10px`) with `cubic-bezier(.16,1,.3,1)` easing and Lenis Smooth Scroll (`data-lenis`).

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `ethanwong-photography` in your global stylesheet:

:root {
  /* Ethan W · Film-Inspired Wedding & Editorial Photographer · Washington DC... (ethanwong-photography) — Ground-Truth Extracted CSS Variables */
  --fit-lh: 1; /* Design System Custom Token (ethanwong-photography) */
  --fit-reserve: 0px; /* Dimension / Scale Token (ethanwong-photography) */
  --red: #9b1120; /* Color / Atmospheric Token (ethanwong-photography) */
  --red-hover: #b3162a; /* Color / Atmospheric Token (ethanwong-photography) */
  --red-lift: #ab182c; /* Color / Atmospheric Token (ethanwong-photography) */
  --red-lift-hover: #c01f34; /* Color / Atmospheric Token (ethanwong-photography) */
  --red-deep: #8a0f1e; /* Color / Atmospheric Token (ethanwong-photography) */
  --lab-nav: 13px; /* Layout / Spatial Grid Token (ethanwong-photography) */
  --lab: 12px; /* Dimension / Scale Token (ethanwong-photography) */
  --lab-sm: 11px; /* Dimension / Scale Token (ethanwong-photography) */
  --lab-dock: 9.5px; /* Dimension / Scale Token (ethanwong-photography) */
  --lab-quiet: 10px; /* Dimension / Scale Token (ethanwong-photography) */
  --lab-w: 400; /* Design System Custom Token (ethanwong-photography) */
  --lab-w-nav: 400; /* Layout / Spatial Grid Token (ethanwong-photography) */
  --lab-w-dock: 500; /* Design System Custom Token (ethanwong-photography) */
  --head-band: 74px; /* Dimension / Scale Token (ethanwong-photography) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#9b1120` — grounded in `var(--red)` in `:root`
- **Primary Typography Ink**: `#b3162a` — grounded in `var(--red-hover)` in `:root`
- **Elevated Surface / Card Substrate**: `#ab182c` — grounded in `var(--red-lift)` in `:root`
- **Interactive Accent / Highlight**: `#c01f34` — grounded in `var(--red-lift-hover)` in `:root`
- **Secondary / Muted Copy**: `#8a0f1e` — grounded in `var(--red-deep)` in `:root`
- **Structural Hairline Border**: `#8a8174` — grounded in `var(--sf-ink)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `700px` extracted from `ethanwong-photography` stylesheet
- **Padding & Gutters**: `10px` lateral canvas padding with `22px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 700px`, `gap: 22px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `10px` horizontal padding
- **Media Queries**: `@media (max-width:700px),(max-height:520px)`, `@media (max-width:640px),(pointer:coarse)and (max-height:520px)`, `@media (pointer:coarse)and (max-height:520px)`, `@media (min-width:1025px)and (max-height:940px)and (pointer:fine)`
- **Corner Radii**: `50%`, `2px`, `999px`, `10px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Cormorant`
- **Body Font Stack**: `Pinyon Script`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(var(--fit-min)`, `29px`, `var(--lab-nav)`, `clamp(28px,4.4vw,72px)`, `var(--lab-quiet)`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(var(--fit-min)`, `29px`, `var(--lab-nav)`, `clamp(28px,4.4vw,72px)`, `var(--lab-quiet)`)
- **Body Copy Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(var(--fit-min)`, `29px`, `var(--lab-nav)`, `clamp(28px,4.4vw,72px)`, `var(--lab-quiet)`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(var(--fit-min)`, `29px`, `var(--lab-nav)`, `clamp(28px,4.4vw,72px)`, `var(--lab-quiet)`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `ethanwong-photography` (`Ethan W · Film-Inspired Wedding & Editorial Photographer · Washington DC...`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.site> — `ethanwong-photography`)**:
   - DOM & Selectors: Landmark `<header class="site nav-on-dark">` hosting `Ethan W · Film-Inspired Wedding & Ed` navigation (`Editorial Exchange`), DOM attributes (`data-cursor="always"`, `data-nav`, `data-cta-ink`, `data-nav-theme="dark"`), and stylesheet rule `html { -ms-overflow-style:none;scrollbar-width:none;-webkit-text-size-adjust:100% }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.site> — `ethanwong-photography`)` (`ethanwong-photography`) adapts across `@media (max-width:700px),(max-height:520px)`, `@media (max-width:640px),(pointer:coarse)and (max-height:520px)`, `@media (pointer:coarse)and (max-height:520px)`, `@media (min-width:1025px)and (max-height:940px)and (pointer:fine)` with `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.55,0,1,.45)`, `cubic-bezier(.85,0,.15,1)` transitions and links `Editorial Exchange`.
2. **Hero Stage & Focal Lead (<main.idx-main> — `Ethan W (Ethan Wong), film-inspire`)**:
   - DOM & Selectors: Landmark `<main class="idx-main">` presenting display lead `Ethan W (Ethan Wong), film-inspired documentary w...` and copy excerpt *"01 W e d d i n g s W e d d i n g s Stories & galleries"* over `#9b1120` canvas and `#8a8174` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#9b1120` background with `#8a8174` headline `Ethan W (Ethan Wong), film-inspired documentary w...`.
3. **Primary Showcase & Content Grid (<main.idx-main> — `01 W e d d i n g s W e d d i n g s`)**:
   - DOM & Selectors: Landmark `<main class="idx-main">` rendering section `01 W e d d i n g s W e d d i n g s Stories & gal` with copy *"W e d d i n g s W e d d i n g s"*, asset references (`favicon-32.png`, `favicon-16.png`, `favicon-32-dark.png`, `favicon-16-dark.png`), and grid rule `html::-webkit-scrollbar { display:none }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<main.idx-main> — `01 W e d d i n g s W e d d i n g s`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 700px`, `gap: 22px`) on desktop and Single-column vertical stack at `390px` viewport width with `10px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<main.idx-main> — `W e d d i n g s W e d d i n g s`)**:
   - DOM & Selectors: Landmark `<main class="idx-main">` framing `W e d d i n g s W e d d i n g s` and `Stories & galleries` (*"Stories & galleries"*) with `#ab182c` surface cards, `#c01f34` accents, and `body { background:efede7 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<main.idx-main> — `W e d d i n g s W e d d i n g s`)` uses `50%`, `2px`, `999px`, `10px` radii, `#c01f34` highlights, and assets (favicon-32.png, favicon-16.png, favicon-32-dark.png).
5. **Colophon & Global Directory Footer (<footer.sf> — `http://ethanwong.photography`)**:
   - DOM & Selectors: Landmark `<footer class="sf sf--fixed">` anchoring `Ethan W · Film-Inspired Wedding ` footer links (`Editorial Exchange`), copy *"All visual stories More coming"*, and `#8a8174` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.sf> — `http://ethanwong.photography`)` aligns to `700px` extracted from `ethanwong-photography` stylesheet with `10px` lateral canvas padding with `22px` grid gap and attributes (data-cursor="always", data-nav, data-cta-ink).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"01 W e d d i n g s W e d d i n g s Stories & galleries"*
- Copy Excerpt 2: *"W e d d i n g s W e d d i n g s"*
- Copy Excerpt 3: *"Stories & galleries"*
- Copy Excerpt 4: *"All visual stories More coming"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.55,0,1,.45)`, `cubic-bezier(.85,0,.15,1)`
- **Extracted Stylesheet Rules (`ethanwong-photography`)**:
- `html { -ms-overflow-style:none;scrollbar-width:none;-webkit-text-size-adjust:100% }`
- `html::-webkit-scrollbar { display:none }`
- `body { background:efede7 }`
- `button { font:inherit;color:inherit;background:none;border:none;cursor:pointer }`
- `img { display:block }`
- **Per-Selector Transition Rules**:
- **Selector `.page-shell`**: `transition: opacity .3s ease` extracted from `ethanwong-photography` stylesheet.
- **Selector `header.site .h-right`**: `transition: transform .62s cubic-bezier(.16,1,.3,1),opacity .5s ease` extracted from `ethanwong-photography` stylesheet.
- **Selector `header.site.nav-hide .h-right`**: `transition: transform .4s cubic-bezier(.16,1,.3,1),opacity .28s ease` extracted from `ethanwong-photography` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<header.site>` and `<main.idx-main>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`) with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `ethanwong-photography`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
