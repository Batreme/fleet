---
title: "UI Prompt Blueprint: sleutelaar-xyz"
date: 2026-11-15
target: "[[overview|sleutelaar-xyz]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#0d0d0d` / `#f0e6db`)"
---

# UI Design System & Master Generation Blueprint: sleutelaar-xyz

> **Hans Sleutelaar · Officiële website** (https://sleutelaar.xyz/) — Digitaal archief over dichter, journalist en Nieuwe Stijl-oprichter Hans Sleutelaar (1935–2020). Gedichten, essays, foto's en bibliografie.

![Desktop Viewport Capture (1440x8455)](file:///root/projects/fleet/wiki/targets/sleutelaar-xyz/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Hans Sleutelaar · Officiële website** (`https://sleutelaar.xyz/`). Digitaal archief over dichter, journalist en Nieuwe Stijl-oprichter Hans Sleutelaar (1935–2020). Gedichten, essays, foto's en bibliografie.
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#0d0d0d` / `#f0e6db`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#0d0d0d` (`var(--color-black)` in `:root`) paired with `#fff` primary typography and `#f0e6db` accents.
  - **Extracted Typographic Hierarchy**: Pairs `ABC Monument Grotesk` for display copy (`Samen met`) with `Apple Color Emoji` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `none (full-bleed `100%` viewport stage)` container bounds (`gap: 0px (flush layout)`, padding `0px`) with `cubic-bezier(.4,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/sleutelaar-xyz/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×8455px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `none (full-bleed `100%` viewport stage)` extracted from `sleutelaar-xyz` stylesheet.
- **Canvas Lateral Padding & Spacing**: `0px` lateral canvas padding with `0px (flush layout)` grid gap.
- **Border Radius Scale**: `.1rem`, `.125rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: none (full-bleed `100%` viewport stage)`, `gap: 0px (flush layout)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `0px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (width>=64rem)`, `@media (width>=1024px)`, `@media (width>=768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0d0d0d` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#009dd8` | `var(--color-blue)` in `:root` |
| **Interactive Accent / Highlight** | `#f0e6db` | `var(--color-beige)` in `:root` |
| **Secondary / Muted Copy** | `#0000` | `textarea { background-color: #0000 }` |
| **Structural Hairline Border** | `#000000` | `.bg-black { background-color: black }` (`#000000`) |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-black` | `#0d0d0d` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--default-transition-duration` | `.15s` | Motion / Easing Token |
| `--default-transition-timing-function` | `cubic-bezier(.4, 0, .2, 1)` | Motion / Easing Token |
| `--default-font-family` | `var(--font-sans)` | Typography / Scale Token |
| `--default-mono-font-family` | `var(--font-mono)` | Typography / Scale Token |
| `--color-blue` | `#009dd8` | Brand / Palette Token |
| `--color-beige` | `#f0e6db` | Brand / Palette Token |
| `--z-index-filter-clone` | `20` | Elevation / Border Token |
| `--z-index-chrome` | `100` | Elevation / Border Token |
| `--gap-scale` | `1` | Layout / Spatial Grid Token |
| `--tw-translate-x` | `0` | Design System Custom Token |
| `--tw-translate-y` | `0` | Design System Custom Token |
| `--sleutelaar-xyz-bg` | `#0d0d0d` | Canvas Substrate (from `var(--color-black)` in `:root`) |
| `--sleutelaar-xyz-ink` | `#fff` | Primary Typography Ink (stylesheet-derived) |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `ABC Monument Grotesk`.
- **Primary Body Stack**: `Apple Color Emoji`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `.833333vw`, `1.25rem`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `.833333vw`, `1.25rem`).
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `.833333vw`, `1.25rem`).
- **Metadata & Navigation Labels**: CSS variables `--default-mono-font-family: var(--font-mono)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.25,.46,.45,.94)`, `cubic-bezier(.19,1,.22,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `sleutelaar-xyz` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `sleutelaar-xyz` stylesheet.
- **Selector `html`**: `transition: background-color .5s cubic-bezier(.4,0,.2,1),color .5s c...` extracted from `sleutelaar-xyz` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.uppercase>` and `<section.flex>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Hans Sleutelaar · Officiële website        │
│ ====================================================================== │
│ [ <header.uppercase>       | Biografie · Index · Gedichten · Archie ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.flex>                                       |   │
│ | H1: Samen met                                                    |   │
│ | Substrate: #0d0d0d    | Ink: #fff       | Accent: #f0e6db        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.flex>            ) max-w: none (full-ble |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Uitgevers en instituties     |  | Voor het betere schrijfwerk  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 0px (f) | │
│ | [<header.uppercase>] -> [<section.flex>] -> [<section.flex>] |       │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.right-0>      ) | https://sleutelaar.xyz/            │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.uppercase> — `sleutelaar-xyz`)**:
   - Landmark `<header class="uppercase fixed">` hosting `Hans Sleutelaar · Officiële website` navigation (`Biografie · Index · Gedichten · Archief`), DOM attributes (`data-sveltekit-preload-data="hover"`, `data-engine="three.js r185"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.flex> — `Samen met`)**:
   - Landmark `<section class="flex flex-col">` presenting display lead `Samen met` and copy excerpt *"Hans Sleutelaar (22 september 1935 – 25 juni 2020). Dichter - Jou"* over `#0d0d0d` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.flex> — `Uitgevers en instituties`)**:
   - Landmark `<section class="flex flex-col">` rendering section `Uitgevers en instituties` with copy *"Voor het betere schrijfwerk Sleutelaar groeide op als enigs kind "*, asset references (`ABCMonumentGroteskTrial-Regular.otf`, `ABCMonumentGroteskTrial-Medium.otf`, `6b9a08feb31cdbce07aca8010c8613f21...`, `0.CvILTd3z.css`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.flex> — `Voor het betere schrijfwerk Sleute`)**:
   - Landmark `<section class="flex flex-col">` framing `Voor het betere schrijfwerk Sleutelaar groeide o` and `Hij bleef nauw betrokken bij het behoud, het red` (*"Hij bleef nauw betrokken bij het behoud, het redigeren en heruitg"*) with `#009dd8` surface cards, `#f0e6db` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.right-0> — `https://sleutelaar.xyz/`)**:
   - Landmark `<footer class="right-0">` anchoring `Hans Sleutelaar · Officiële webs` footer links (`Biografie · Index · Gedichten · Archief`), copy *"2018 International Film Festival Rotterdam (IFFR) - première"*, and `#000000` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: sleutelaar-xyz (Hans Sleutelaar · Officiële website)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `sleutelaar-xyz` (**Hans Sleutelaar · Officiële website** — `https://sleutelaar.xyz/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0d0d0d` / `#f0e6db`).
- **Identity & Domain Context**: Digitaal archief over dichter, journalist en Nieuwe Stijl-oprichter Hans Sleutelaar (1935–2020). Gedichten, essays, foto's en bibliografie.
- **Primary Substrate**: `#0d0d0d` (`var(--color-black)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#f0e6db`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#0d0d0d` (`var(--color-black)` in `:root`) paired with `#fff` primary typography and `#f0e6db` accents.
  - **Extracted Typographic Hierarchy**: Pairs `ABC Monument Grotesk` for display copy (`Samen met`) with `Apple Color Emoji` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `none (full-bleed `100%` viewport stage)` container bounds (`gap: 0px (flush layout)`, padding `0px`) with `cubic-bezier(.4,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `sleutelaar-xyz` in your global stylesheet:

:root {
  /* Hans Sleutelaar · Officiële website (sleutelaar-xyz) — Ground-Truth Extracted CSS Variables */
  --color-black: #0d0d0d; /* Canvas / Surface Token (sleutelaar-xyz) */
  --color-white: #fff; /* Canvas / Surface Token (sleutelaar-xyz) */
  --spacing: .25rem; /* Layout / Spatial Grid Token (sleutelaar-xyz) */
  --default-transition-duration: .15s; /* Motion / Easing Token (sleutelaar-xyz) */
  --default-transition-timing-function: cubic-bezier(.4, 0, .2, 1); /* Motion / Easing Token (sleutelaar-xyz) */
  --default-font-family: var(--font-sans); /* Typography / Scale Token (sleutelaar-xyz) */
  --default-mono-font-family: var(--font-mono); /* Typography / Scale Token (sleutelaar-xyz) */
  --color-blue: #009dd8; /* Brand / Palette Token (sleutelaar-xyz) */
  --color-beige: #f0e6db; /* Brand / Palette Token (sleutelaar-xyz) */
  --z-index-filter-clone: 20; /* Elevation / Border Token (sleutelaar-xyz) */
  --z-index-chrome: 100; /* Elevation / Border Token (sleutelaar-xyz) */
  --gap-scale: 1; /* Layout / Spatial Grid Token (sleutelaar-xyz) */
  --tw-translate-x: 0; /* Design System Custom Token (sleutelaar-xyz) */
  --tw-translate-y: 0; /* Design System Custom Token (sleutelaar-xyz) */
  --sleutelaar-xyz-bg: #0d0d0d; /* Canvas Substrate (from `var(--color-black)` in `:root`) (sleutelaar-xyz) */
  --sleutelaar-xyz-ink: #fff; /* Primary Typography Ink (stylesheet-derived) (sleutelaar-xyz) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#0d0d0d` — grounded in `var(--color-black)` in `:root`
- **Primary Typography Ink**: `#fff` — grounded in `var(--color-white)` in `:root`
- **Elevated Surface / Card Substrate**: `#009dd8` — grounded in `var(--color-blue)` in `:root`
- **Interactive Accent / Highlight**: `#f0e6db` — grounded in `var(--color-beige)` in `:root`
- **Secondary / Muted Copy**: `#0000` — grounded in `textarea { background-color: #0000 }`
- **Structural Hairline Border**: `#000000` — grounded in `.bg-black { background-color: black }` (`#000000`)

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×8455px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `none (full-bleed `100%` viewport stage)` extracted from `sleutelaar-xyz` stylesheet
- **Padding & Gutters**: `0px` lateral canvas padding with `0px (flush layout)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: none (full-bleed `100%` viewport stage)`, `gap: 0px (flush layout)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `0px` horizontal padding
- **Media Queries**: `@media (width>=64rem)`, `@media (width>=1024px)`, `@media (width>=768px)`
- **Corner Radii**: `.1rem`, `.125rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `ABC Monument Grotesk`
- **Body Font Stack**: `Apple Color Emoji`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `.833333vw`, `1.25rem`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `.833333vw`, `1.25rem`)
- **Body Copy Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `.833333vw`, `1.25rem`)
- **Metadata & Index Rule**: CSS variables `--default-mono-font-family: var(--font-mono)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `sleutelaar-xyz` (`Hans Sleutelaar · Officiële website`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.uppercase> — `sleutelaar-xyz`)**:
   - DOM & Selectors: Landmark `<header class="uppercase fixed">` hosting `Hans Sleutelaar · Officiële website` navigation (`Biografie · Index · Gedichten · Archief`), DOM attributes (`data-sveltekit-preload-data="hover"`, `data-engine="three.js r185"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.uppercase> — `sleutelaar-xyz`)` (`sleutelaar-xyz`) adapts across `@media (width>=64rem)`, `@media (width>=1024px)`, `@media (width>=768px)` with `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.25,.46,.45,.94)`, `cubic-bezier(.19,1,.22,1)` transitions and links `Biografie · Index · Gedichten · Archief`.
2. **Hero Stage & Focal Lead (<section.flex> — `Samen met`)**:
   - DOM & Selectors: Landmark `<section class="flex flex-col">` presenting display lead `Samen met` and copy excerpt *"Hans Sleutelaar (22 september 1935 – 25 juni 2020). Dichter - Jou"* over `#0d0d0d` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×8455px` desktop / `390×2400px` mobile) sets `#0d0d0d` background with `#fff` headline `Samen met`.
3. **Primary Showcase & Content Grid (<section.flex> — `Uitgevers en instituties`)**:
   - DOM & Selectors: Landmark `<section class="flex flex-col">` rendering section `Uitgevers en instituties` with copy *"Voor het betere schrijfwerk Sleutelaar groeide op als enigs kind "*, asset references (`ABCMonumentGroteskTrial-Regular.otf`, `ABCMonumentGroteskTrial-Medium.otf`, `6b9a08feb31cdbce07aca8010c8613f21...`, `0.CvILTd3z.css`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.flex> — `Uitgevers en instituties`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: none (full-bleed `100%` viewport stage)`, `gap: 0px (flush layout)`) on desktop and Single-column vertical stack at `390px` viewport width with `0px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.flex> — `Voor het betere schrijfwerk Sleute`)**:
   - DOM & Selectors: Landmark `<section class="flex flex-col">` framing `Voor het betere schrijfwerk Sleutelaar groeide o` and `Hij bleef nauw betrokken bij het behoud, het red` (*"Hij bleef nauw betrokken bij het behoud, het redigeren en heruitg"*) with `#009dd8` surface cards, `#f0e6db` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.flex> — `Voor het betere schrijfwerk Sleute`)` uses `.1rem`, `.125rem` radii, `#f0e6db` highlights, and assets (ABCMonumentGroteskTrial-Regular.otf, ABCMonumentGroteskTrial-Medium.otf, 6b9a08feb31cdbce07aca8010c8613f21...).
5. **Colophon & Global Directory Footer (<footer.right-0> — `https://sleutelaar.xyz/`)**:
   - DOM & Selectors: Landmark `<footer class="right-0">` anchoring `Hans Sleutelaar · Officiële webs` footer links (`Biografie · Index · Gedichten · Archief`), copy *"2018 International Film Festival Rotterdam (IFFR) - première"*, and `#000000` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.right-0> — `https://sleutelaar.xyz/`)` aligns to `none (full-bleed `100%` viewport stage)` extracted from `sleutelaar-xyz` stylesheet with `0px` lateral canvas padding with `0px (flush layout)` grid gap and attributes (data-sveltekit-preload-data="hover", data-engine="three.js r185").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Hans Sleutelaar (22 september 1935 – 25 juni 2020). Dichter - Journalist - Redacte..."*
- Copy Excerpt 2: *"Voor het betere schrijfwerk Sleutelaar groeide op als enigs kind in Rotterdam. Een..."*
- Copy Excerpt 3: *"Hij bleef nauw betrokken bij het behoud, het redigeren en heruitgeven van het werk..."*
- Copy Excerpt 4: *"2018 International Film Festival Rotterdam (IFFR) - première documentaire Sleutela..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.25,.46,.45,.94)`, `cubic-bezier(.19,1,.22,1)`
- **Extracted Stylesheet Rules (`sleutelaar-xyz`)**:
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- `sup { vertical-align:baseline;font-size:75%;line-height:0;position:relative }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `sleutelaar-xyz` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `sleutelaar-xyz` stylesheet.
- **Selector `html`**: `transition: background-color .5s cubic-bezier(.4,0,.2,1),color .5s c...` extracted from `sleutelaar-xyz` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.uppercase>` and `<section.flex>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `sleutelaar-xyz`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
