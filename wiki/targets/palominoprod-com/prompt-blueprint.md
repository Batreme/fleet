---
title: "UI Prompt Blueprint: palominoprod-com"
date: 2026-11-15
target: "[[overview|palominoprod-com]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#ff6568` / `#05df72`)"
---

# UI Design System & Master Generation Blueprint: palominoprod-com

> **Palomino — Cinematic Sports & Brand Films** (https://palominoprod.com/) — Cinematic sports and branded films—from global campaigns to athlete documentaries and live events—with strategy, premium production & edi...

![Desktop Viewport Capture (1440x8375)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Palomino — Cinematic Sports & Brand Films** (`https://palominoprod.com/`). Cinematic sports and branded films—from global campaigns to athlete documentaries and live events—with strategy, premium production & edi...
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#ff6568` / `#05df72`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#ff6568` (`var(--color-red-400)` in `:root`) paired with `#e2e8f0` primary typography and `#05df72` accents.
  - **Extracted Typographic Hierarchy**: Pairs `HostGrotesk` for display copy (`SPORTS INTO STORIES`) with `Apple Color Emoji` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `380px` container bounds (`gap: var(--gap-x-default)`, padding `var(--padding-x-default)`) with `cubic-bezier(.4,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×8375px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `380px` extracted from `palominoprod-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--padding-x-default)` lateral canvas padding with `var(--gap-x-default)` grid gap.
- **Border Radius Scale**: `3px`, `var(--radius-lg)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 380px`, `gap: var(--gap-x-default)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--padding-x-default)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:380px)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ff6568` | `var(--color-red-400)` in `:root` |
| **Primary Typography Ink** | `#fb2c36` | `var(--color-red-500)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ff8b1a` | `var(--color-orange-400)` in `:root` |
| **Interactive Accent / Highlight** | `#05df72` | `var(--color-green-400)` in `:root` |
| **Secondary / Muted Copy** | `#00c758` | `var(--color-green-500)` in `:root` |
| **Structural Hairline Border** | `#e2e8f0` | `var(--color-slate-200)` in `:root` |
| **Variable Token (`--color-slate-300`)** | `#cad5e2` | `var(--color-slate-300)` in `:root` |
| **Variable Token (`--color-slate-400`)** | `#90a1b9` | `var(--color-slate-400)` in `:root` |
| **Variable Token (`--color-slate-600`)** | `#45556c` | `var(--color-slate-600)` in `:root` |
| **Variable Token (`--color-slate-700`)** | `#314158` | `var(--color-slate-700)` in `:root` |
| **Variable Token (`--color-slate-900`)** | `#0f172b` | `var(--color-slate-900)` in `:root` |
| **Variable Token (`--color-black`)** | `#000` | `var(--color-black)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--screen-loader-burst` | `0px` | Dimension / Scale Token |
| `--media-control-background` | `transparent!important` | Canvas / Surface Token |
| `--media-control-hover-background` | `transparent!important` | Canvas / Surface Token |
| `--media-button-icon-width` | `100%!important` | Layout / Spatial Grid Token |
| `--color-red-400` | `#ff6568` | Brand / Palette Token |
| `--color-red-500` | `#fb2c36` | Brand / Palette Token |
| `--color-orange-400` | `#ff8b1a` | Brand / Palette Token |
| `--color-green-400` | `#05df72` | Brand / Palette Token |
| `--color-green-500` | `#00c758` | Brand / Palette Token |
| `--color-slate-200` | `#e2e8f0` | Brand / Palette Token |
| `--color-slate-300` | `#cad5e2` | Brand / Palette Token |
| `--color-slate-400` | `#90a1b9` | Brand / Palette Token |
| `--color-slate-600` | `#45556c` | Brand / Palette Token |
| `--color-slate-700` | `#314158` | Brand / Palette Token |
| `--color-slate-900` | `#0f172b` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `HostGrotesk`.
- **Primary Body Stack**: `Apple Color Emoji`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `,h1` (`font-size: clamp(38px,5vw,101px)`, `line-height: 1.2`, `font-weight: 600`).
- **Section Heading (`H2`)**: CSS variables `--text-3xl: 1.875rem`, `--text-3xl--line-height: calc(2.25 / 1.875)`; rule `,h2` (`font-size: clamp(26px,3vw,50px)`, `line-height: 1.2`, `font-weight: 600`).
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`, `clamp(38px,5vw,101px)`, `clamp(26px,3vw,50px)`, `clamp(20px,2vw,30px)`, `30px`).
- **Metadata & Navigation Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.3,1,.7,1)`, `cubic-bezier(.83,0,.17,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.mux-full-player::part(pre-play)`**: `transition: transform .2s` extracted from `palominoprod-com` stylesheet.
- **Selector `layer theme`**: `transition: .15s` extracted from `palominoprod-com` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `palominoprod-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.px-x-default>` and `<section.pt-y-default>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Palomino — Cinematic Sports & Brand Films  │
│ ====================================================================== │
│ [ <header.px-x-default>    | W O R K W O R K · A B O U T A B O U T  ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.relative>                                   |   │
│ | H1: SPORTS INTO STORIES                                          |   │
│ | Substrate: #ff6568    | Ink: #e2e8f0    | Accent: #05df72        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.pt-y-default>    ) max-w: 380px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | OUR CLIENTS                  |  | SELECTED PROJECTS            | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<header.px-x-defau] -> [<section.relative>] -> [<section.pt-y-defa] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.w-screen>     ) | https://palominoprod.com/          │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.px-x-default> — `palominoprod-com`)**:
   - Landmark `<header class="px-x-default fixed">` hosting `Palomino — Cinematic Sports & Brand ` navigation (`W O R K W O R K · A B O U T A B O U T`), DOM attributes (`data-next-head`, `data-n-g`, `data-n-css`, `data-nimg="1"`), and stylesheet rule `.animation-sample { will-change:transform;animation:6s ease-in-out infinite sample }`.
2. **Hero Stage & Focal Lead (<section.relative> — `SPORTS INTO STORIES`)**:
   - Landmark `<section class="relative top-0">` presenting display lead `SPORTS INTO STORIES` and copy excerpt *"A B O U T A B O U T"* over `#ff6568` canvas and `#e2e8f0` ink.
3. **Primary Showcase & Content Grid (<section.pt-y-default> — `OUR CLIENTS`)**:
   - Landmark `<section class="pt-y-default noise-overlay">` rendering section `OUR CLIENTS` with copy *"C O N T A C T C O N T A C T"*, asset references (`favicon.ico`, `HostGrotesk-Variable.woff2`, `0d_rtsbnnnoar.css`, `0eydbtu3qzciz.js`), and grid rule `html { scrollbar-width:none;-ms-overflow-style:none }`.
4. **Interactive Detail & Feature Matrix (<section.px-x-default> — `SELECTED PROJECTS`)**:
   - Landmark `<section class="px-x-default pt-y-default">` framing `SELECTED PROJECTS` and `Running FW26 × Decathlon` (*"Sports film and photography studio. We turn brand campaigns and a"*) with `#ff8b1a` surface cards, `#05df72` accents, and `html ::selection { background:var(--color-black);color:var(--color-white) }`.
5. **Colophon & Global Directory Footer (<footer.w-screen> — `https://palominoprod.com/`)**:
   - Landmark `<footer class="w-screen bg-white">` anchoring `Palomino — Cinematic Sports & Br` footer links (`W O R K W O R K · A B O U T A B O U T`), copy *"Where effort meets the light. A glimpse of the stories we've"*, and `#e2e8f0` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: palominoprod-com (Palomino — Cinematic Sports & Brand Films)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `palominoprod-com` (**Palomino — Cinematic Sports & Brand Films** — `https://palominoprod.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ff6568` / `#05df72`).
- **Identity & Domain Context**: Cinematic sports and branded films—from global campaigns to athlete documentaries and live events—with strategy, premium production & edi...
- **Primary Substrate**: `#ff6568` (`var(--color-red-400)` in `:root`), **Primary Ink**: `#e2e8f0`, **Accent / Highlight**: `#05df72`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#ff6568` (`var(--color-red-400)` in `:root`) paired with `#e2e8f0` primary typography and `#05df72` accents.
  - **Extracted Typographic Hierarchy**: Pairs `HostGrotesk` for display copy (`SPORTS INTO STORIES`) with `Apple Color Emoji` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `380px` container bounds (`gap: var(--gap-x-default)`, padding `var(--padding-x-default)`) with `cubic-bezier(.4,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `palominoprod-com` in your global stylesheet:

:root {
  /* Palomino — Cinematic Sports & Brand Films (palominoprod-com) — Ground-Truth Extracted CSS Variables */
  --screen-loader-burst: 0px; /* Dimension / Scale Token (palominoprod-com) */
  --media-control-background: transparent!important; /* Canvas / Surface Token (palominoprod-com) */
  --media-control-hover-background: transparent!important; /* Canvas / Surface Token (palominoprod-com) */
  --media-button-icon-width: 100%!important; /* Layout / Spatial Grid Token (palominoprod-com) */
  --color-red-400: #ff6568; /* Brand / Palette Token (palominoprod-com) */
  --color-red-500: #fb2c36; /* Brand / Palette Token (palominoprod-com) */
  --color-orange-400: #ff8b1a; /* Brand / Palette Token (palominoprod-com) */
  --color-green-400: #05df72; /* Brand / Palette Token (palominoprod-com) */
  --color-green-500: #00c758; /* Brand / Palette Token (palominoprod-com) */
  --color-slate-200: #e2e8f0; /* Brand / Palette Token (palominoprod-com) */
  --color-slate-300: #cad5e2; /* Brand / Palette Token (palominoprod-com) */
  --color-slate-400: #90a1b9; /* Brand / Palette Token (palominoprod-com) */
  --color-slate-600: #45556c; /* Brand / Palette Token (palominoprod-com) */
  --color-slate-700: #314158; /* Brand / Palette Token (palominoprod-com) */
  --color-slate-900: #0f172b; /* Brand / Palette Token (palominoprod-com) */
  --color-black: #000; /* Canvas / Surface Token (palominoprod-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ff6568` — grounded in `var(--color-red-400)` in `:root`
- **Primary Typography Ink**: `#fb2c36` — grounded in `var(--color-red-500)` in `:root`
- **Elevated Surface / Card Substrate**: `#ff8b1a` — grounded in `var(--color-orange-400)` in `:root`
- **Interactive Accent / Highlight**: `#05df72` — grounded in `var(--color-green-400)` in `:root`
- **Secondary / Muted Copy**: `#00c758` — grounded in `var(--color-green-500)` in `:root`
- **Structural Hairline Border**: `#e2e8f0` — grounded in `var(--color-slate-200)` in `:root`
- **Variable Token (`--color-slate-300`)**: `#cad5e2` — grounded in `var(--color-slate-300)` in `:root`
- **Variable Token (`--color-slate-400`)**: `#90a1b9` — grounded in `var(--color-slate-400)` in `:root`
- **Variable Token (`--color-slate-600`)**: `#45556c` — grounded in `var(--color-slate-600)` in `:root`
- **Variable Token (`--color-slate-700`)**: `#314158` — grounded in `var(--color-slate-700)` in `:root`
- **Variable Token (`--color-slate-900`)**: `#0f172b` — grounded in `var(--color-slate-900)` in `:root`
- **Variable Token (`--color-black`)**: `#000` — grounded in `var(--color-black)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×8375px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `380px` extracted from `palominoprod-com` stylesheet
- **Padding & Gutters**: `var(--padding-x-default)` lateral canvas padding with `var(--gap-x-default)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 380px`, `gap: var(--gap-x-default)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--padding-x-default)` horizontal padding
- **Media Queries**: `@media (min-width:380px)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`
- **Corner Radii**: `3px`, `var(--radius-lg)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `HostGrotesk`
- **Body Font Stack**: `Apple Color Emoji`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: rule `,h1` (`font-size: clamp(38px,5vw,101px)`, `line-height: 1.2`, `font-weight: 600`)
- **H2 Section Rule**: CSS variables `--text-3xl: 1.875rem`, `--text-3xl--line-height: calc(2.25 / 1.875)`; rule `,h2` (`font-size: clamp(26px,3vw,50px)`, `line-height: 1.2`, `font-weight: 600`)
- **Body Copy Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`, `clamp(38px,5vw,101px)`, `clamp(26px,3vw,50px)`, `clamp(20px,2vw,30px)`, `30px`)
- **Metadata & Index Rule**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `palominoprod-com` (`Palomino — Cinematic Sports & Brand Films`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.px-x-default> — `palominoprod-com`)**:
   - DOM & Selectors: Landmark `<header class="px-x-default fixed">` hosting `Palomino — Cinematic Sports & Brand ` navigation (`W O R K W O R K · A B O U T A B O U T`), DOM attributes (`data-next-head`, `data-n-g`, `data-n-css`, `data-nimg="1"`), and stylesheet rule `.animation-sample { will-change:transform;animation:6s ease-in-out infinite sample }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.px-x-default> — `palominoprod-com`)` (`palominoprod-com`) adapts across `@media (min-width:380px)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)` with `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.3,1,.7,1)`, `cubic-bezier(.83,0,.17,1)` transitions and links `W O R K W O R K · A B O U T A B O U T`.
2. **Hero Stage & Focal Lead (<section.relative> — `SPORTS INTO STORIES`)**:
   - DOM & Selectors: Landmark `<section class="relative top-0">` presenting display lead `SPORTS INTO STORIES` and copy excerpt *"A B O U T A B O U T"* over `#ff6568` canvas and `#e2e8f0` ink.
   - Responsive Contract: Hero stage (`1440×8375px` desktop / `390×2400px` mobile) sets `#ff6568` background with `#e2e8f0` headline `SPORTS INTO STORIES`.
3. **Primary Showcase & Content Grid (<section.pt-y-default> — `OUR CLIENTS`)**:
   - DOM & Selectors: Landmark `<section class="pt-y-default noise-overlay">` rendering section `OUR CLIENTS` with copy *"C O N T A C T C O N T A C T"*, asset references (`favicon.ico`, `HostGrotesk-Variable.woff2`, `0d_rtsbnnnoar.css`, `0eydbtu3qzciz.js`), and grid rule `html { scrollbar-width:none;-ms-overflow-style:none }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.pt-y-default> — `OUR CLIENTS`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 380px`, `gap: var(--gap-x-default)`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--padding-x-default)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.px-x-default> — `SELECTED PROJECTS`)**:
   - DOM & Selectors: Landmark `<section class="px-x-default pt-y-default">` framing `SELECTED PROJECTS` and `Running FW26 × Decathlon` (*"Sports film and photography studio. We turn brand campaigns and a"*) with `#ff8b1a` surface cards, `#05df72` accents, and `html ::selection { background:var(--color-black);color:var(--color-white) }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.px-x-default> — `SELECTED PROJECTS`)` uses `3px`, `var(--radius-lg)` radii, `#05df72` highlights, and assets (favicon.ico, HostGrotesk-Variable.woff2, 0d_rtsbnnnoar.css).
5. **Colophon & Global Directory Footer (<footer.w-screen> — `https://palominoprod.com/`)**:
   - DOM & Selectors: Landmark `<footer class="w-screen bg-white">` anchoring `Palomino — Cinematic Sports & Br` footer links (`W O R K W O R K · A B O U T A B O U T`), copy *"Where effort meets the light. A glimpse of the stories we've"*, and `#e2e8f0` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.w-screen> — `https://palominoprod.com/`)` aligns to `380px` extracted from `palominoprod-com` stylesheet with `var(--padding-x-default)` lateral canvas padding with `var(--gap-x-default)` grid gap and attributes (data-next-head, data-n-g, data-n-css).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"A B O U T A B O U T"*
- Copy Excerpt 2: *"C O N T A C T C O N T A C T"*
- Copy Excerpt 3: *"Sports film and photography studio. We turn brand campaigns and athlete journeys i..."*
- Copy Excerpt 4: *"Where effort meets the light. A glimpse of the stories we've brought to life, fram..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.3,1,.7,1)`, `cubic-bezier(.83,0,.17,1)`
- **Extracted Stylesheet Rules (`palominoprod-com`)**:
- `.animation-sample { will-change:transform;animation:6s ease-in-out infinite sample }`
- `html { scrollbar-width:none;-ms-overflow-style:none }`
- `html ::selection { background:var(--color-black);color:var(--color-white) }`
- `html::-webkit-scrollbar { display:none }`
- `.no-scrollbar { scrollbar-width:none;-ms-overflow-style:none }`
- **Per-Selector Transition Rules**:
- **Selector `.mux-full-player::part(pre-play)`**: `transition: transform .2s` extracted from `palominoprod-com` stylesheet.
- **Selector `layer theme`**: `transition: .15s` extracted from `palominoprod-com` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `palominoprod-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.px-x-default>` and `<section.pt-y-default>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `palominoprod-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
