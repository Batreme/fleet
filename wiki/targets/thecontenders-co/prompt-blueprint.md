---
title: "UI Prompt Blueprint: thecontenders-co"
date: 2026-11-15
target: "[[overview|thecontenders-co]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#e40014` / `#f3f4f6`)"
---

# UI Design System & Master Generation Blueprint: thecontenders-co

> **The Contenders · Strategic Brand & Design Consultancy** (https://thecontenders.co/) — Where business meets brand. The Contenders is an independent Australian consultancy creating distinctive brands that deliver measurable i...

![Desktop Viewport Capture (1440x1312)](file:///root/projects/fleet/wiki/targets/thecontenders-co/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **The Contenders · Strategic Brand & Design Consultancy** (`https://thecontenders.co/`). Where business meets brand. The Contenders is an independent Australian consultancy creating distinctive brands that deliver measurable i...
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#e40014` / `#f3f4f6`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#e40014` (`var(--color-red-600)` in `:root`) paired with `#f9fafb` primary typography and `#f3f4f6` accents.
  - **Extracted Typographic Hierarchy**: Pairs `DieGrotesk` for display copy (`THE CONTENDERS IS A CONSULTANCY WHER`) with `DieGrotesk Fallback` and `iki-mono-variable`.
  - **Calibrated Spatial Grid & Motion**: Combines `37.5rem` container bounds (`gap: var(--grid-column-gap)`, padding `var(--inline-spacing)`) with `cubic-bezier(0,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/thecontenders-co/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×1312px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `37.5rem` extracted from `thecontenders-co` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--inline-spacing)` lateral canvas padding with `var(--grid-column-gap)` grid gap.
- **Border Radius Scale**: `.3125rem`, `.375rem`, `2147483647px`, `var(--radius-md)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 37.5rem`, `gap: var(--grid-column-gap)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--inline-spacing)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:37.5rem)`, `@media (min-width:48rem)`, `@media (min-width:80rem)`, `@media (min-width:96rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#e40014` | `var(--color-red-600)` in `:root` |
| **Primary Typography Ink** | `#bf000f` | `var(--color-red-700)` in `:root` |
| **Elevated Surface / Card Substrate** | `#f9fafb` | `var(--color-gray-50)` in `:root` |
| **Interactive Accent / Highlight** | `#f3f4f6` | `var(--color-gray-100)` in `:root` |
| **Secondary / Muted Copy** | `#e5e7eb` | `var(--color-gray-200)` in `:root` |
| **Structural Hairline Border** | `#d1d5dc` | `var(--color-gray-300)` in `:root` |
| **Variable Token (`--color-gray-400`)** | `#99a1af` | `var(--color-gray-400)` in `:root` |
| **Variable Token (`--color-gray-800`)** | `#1e2939` | `var(--color-gray-800)` in `:root` |
| **Variable Token (`--color-gray-900`)** | `#101828` | `var(--color-gray-900)` in `:root` |
| **Variable Token (`--color-gray-950`)** | `#030712` | `var(--color-gray-950)` in `:root` |
| **Variable Token (`--color-black`)** | `#000` | `var(--color-black)` in `:root` |
| **Variable Token (`--color-white`)** | `#fff` | `var(--color-white)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-die-grotesk` | `"DieGrotesk", "DieGrotesk Fallback"` | Typography / Scale Token |
| `--font-mesapholic` | `"Mesapholic", "Mesapholic Fallback"` | Typography / Scale Token |
| `--font-serif` | `ui-serif, Georgia, Cambria, "Times New Roman", Times, serif` | Typography / Scale Token |
| `--color-red-600` | `#e40014` | Brand / Palette Token |
| `--color-red-700` | `#bf000f` | Brand / Palette Token |
| `--color-gray-50` | `#f9fafb` | Brand / Palette Token |
| `--color-gray-100` | `#f3f4f6` | Brand / Palette Token |
| `--color-gray-200` | `#e5e7eb` | Brand / Palette Token |
| `--color-gray-300` | `#d1d5dc` | Brand / Palette Token |
| `--color-gray-400` | `#99a1af` | Brand / Palette Token |
| `--color-gray-800` | `#1e2939` | Brand / Palette Token |
| `--color-gray-900` | `#101828` | Brand / Palette Token |
| `--color-gray-950` | `#030712` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `DieGrotesk`.
- **Primary Body Stack**: `DieGrotesk Fallback`.
- **Technical / Metadata Stack**: `iki-mono-variable`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--heading-h1-font-family: var(--font-serif)`, `--heading-h1-font-size: 4rem`, `--heading-h1-font-weight: 400`.
- **Section Heading (`H2`)**: CSS variables `--heading-h2-font-family: var(--font-serif)`, `--heading-h2-font-size: 3.5rem`, `--heading-h2-font-weight: 400`.
- **Body Copy**: CSS variables `--body-l-font-family: var(--font-sans)`, `--body-l-font-size: 1.125rem`, `--body-l-font-weight: 400`.
- **Metadata & Navigation Labels**: CSS variables `--text-sm: .875rem`, `--text-sm--line-height: calc(1.25 / .875)`, `--default-mono-font-family: var(--font-mono)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.78,0,.22,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `thecontenders-co` stylesheet.
- **Selector `body`**: `transition: background-color .85s ease-out` extracted from `thecontenders-co` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `thecontenders-co` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<nav.fixed>` and `<section.homepage-intro-copy>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — The Contenders · Strategic Brand & Design  │
│ ====================================================================== │
│ [ <nav.fixed>              | Overview · Index · Archive · About · C ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.homepage-intro-copy>                        |   │
│ | H1: THE CONTENDERS IS A CONSULTANCY WHERE BUSINESS ME...         |   │
│ | Substrate: #e40014    | Ink: #f9fafb    | Accent: #f3f4f6        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.homepage-intro-co) max-w: 37.5rem        |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | THE CONTENDERS               |  | Newsletter sign up           | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<nav.fixed>] -> [<section.homepage-] -> [<section.homepage-] |      │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.fixed>        ) | https://thecontenders.co/          │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.fixed> — `thecontenders-co`)**:
   - Landmark `<nav class="fixed z-50">` hosting `The Contenders · Strategic Brand & D` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-theme="white"`, `data-homepage="true"`, `data-lenis-prevent="true"`), and stylesheet rule `.WkV8yq_className { font-family:DieGrotesk,DieGrotesk Fallback }`.
2. **Hero Stage & Focal Lead (<section.homepage-intro-copy> — `THE CONTENDERS IS A CONSULTANCY WH`)**:
   - Landmark `<section class="homepage-intro-copy">` presenting display lead `THE CONTENDERS IS A CONSULTANCY WHERE BUSINESS ME...` and copy excerpt *"arrow_forward Newsletter sign up arrow_forward"* over `#e40014` canvas and `#f9fafb` ink.
3. **Primary Showcase & Content Grid (<section.homepage-intro-copy> — `THE CONTENDERS`)**:
   - Landmark `<section class="homepage-intro-copy">` rendering section `THE CONTENDERS` with copy *"Newsletter sign up"*, asset references (`Horizontal-3fa5268f-53f1-4223-a6c...`, `Compact-7923dd47-d322-4f23-802c-c...`, `00k7ot6zx_lfg.css`, `123l3rregymnq.js`), and grid rule `.WkV8yq_variable { --font-die-grotesk:"DieGrotesk", "DieGrotesk Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.homepage-intro-copy> — `Newsletter sign up`)**:
   - Landmark `<section class="homepage-intro-copy">` framing `Newsletter sign up` and `THE CONTENDERS IS A CONSULTANCY WHERE BUSINESS M` (*"THE CONTENDERS IS A CONSULTANCY WHERE BUSINESS MEETS BRAND."*) with `#f9fafb` surface cards, `#f3f4f6` accents, and `.HMGLSG_className { font-family:Mesapholic,Mesapholic Fallback }`.
5. **Colophon & Global Directory Footer (<footer.fixed> — `https://thecontenders.co/`)**:
   - Landmark `<footer class="fixed">` anchoring `The Contenders · Strategic Brand` footer links (`Overview · Index · Archive · About · Contact`), copy *"WE UNDERSTAND THAT YOUR ORGANISATION IS FIGHTING FOR SOMETHI"*, and `#d1d5dc` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: thecontenders-co (The Contenders · Strategic Brand & Design Consultancy)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `thecontenders-co` (**The Contenders · Strategic Brand & Design Consultancy** — `https://thecontenders.co/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#e40014` / `#f3f4f6`).
- **Identity & Domain Context**: Where business meets brand. The Contenders is an independent Australian consultancy creating distinctive brands that deliver measurable i...
- **Primary Substrate**: `#e40014` (`var(--color-red-600)` in `:root`), **Primary Ink**: `#f9fafb`, **Accent / Highlight**: `#f3f4f6`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#e40014` (`var(--color-red-600)` in `:root`) paired with `#f9fafb` primary typography and `#f3f4f6` accents.
  - **Extracted Typographic Hierarchy**: Pairs `DieGrotesk` for display copy (`THE CONTENDERS IS A CONSULTANCY WHER`) with `DieGrotesk Fallback` and `iki-mono-variable`.
  - **Calibrated Spatial Grid & Motion**: Combines `37.5rem` container bounds (`gap: var(--grid-column-gap)`, padding `var(--inline-spacing)`) with `cubic-bezier(0,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `thecontenders-co` in your global stylesheet:

:root {
  /* The Contenders · Strategic Brand & Design Consultancy (thecontenders-co) — Ground-Truth Extracted CSS Variables */
  --font-die-grotesk: "DieGrotesk", "DieGrotesk Fallback"; /* Typography / Scale Token (thecontenders-co) */
  --font-mesapholic: "Mesapholic", "Mesapholic Fallback"; /* Typography / Scale Token (thecontenders-co) */
  --font-serif: ui-serif, Georgia, Cambria, "Times New Roman", Times, serif; /* Typography / Scale Token (thecontenders-co) */
  --color-red-600: #e40014; /* Brand / Palette Token (thecontenders-co) */
  --color-red-700: #bf000f; /* Brand / Palette Token (thecontenders-co) */
  --color-gray-50: #f9fafb; /* Brand / Palette Token (thecontenders-co) */
  --color-gray-100: #f3f4f6; /* Brand / Palette Token (thecontenders-co) */
  --color-gray-200: #e5e7eb; /* Brand / Palette Token (thecontenders-co) */
  --color-gray-300: #d1d5dc; /* Brand / Palette Token (thecontenders-co) */
  --color-gray-400: #99a1af; /* Brand / Palette Token (thecontenders-co) */
  --color-gray-800: #1e2939; /* Brand / Palette Token (thecontenders-co) */
  --color-gray-900: #101828; /* Brand / Palette Token (thecontenders-co) */
  --color-gray-950: #030712; /* Brand / Palette Token (thecontenders-co) */
  --color-black: #000; /* Canvas / Surface Token (thecontenders-co) */
  --color-white: #fff; /* Canvas / Surface Token (thecontenders-co) */
  --spacing: .25rem; /* Layout / Spatial Grid Token (thecontenders-co) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#e40014` — grounded in `var(--color-red-600)` in `:root`
- **Primary Typography Ink**: `#bf000f` — grounded in `var(--color-red-700)` in `:root`
- **Elevated Surface / Card Substrate**: `#f9fafb` — grounded in `var(--color-gray-50)` in `:root`
- **Interactive Accent / Highlight**: `#f3f4f6` — grounded in `var(--color-gray-100)` in `:root`
- **Secondary / Muted Copy**: `#e5e7eb` — grounded in `var(--color-gray-200)` in `:root`
- **Structural Hairline Border**: `#d1d5dc` — grounded in `var(--color-gray-300)` in `:root`
- **Variable Token (`--color-gray-400`)**: `#99a1af` — grounded in `var(--color-gray-400)` in `:root`
- **Variable Token (`--color-gray-800`)**: `#1e2939` — grounded in `var(--color-gray-800)` in `:root`
- **Variable Token (`--color-gray-900`)**: `#101828` — grounded in `var(--color-gray-900)` in `:root`
- **Variable Token (`--color-gray-950`)**: `#030712` — grounded in `var(--color-gray-950)` in `:root`
- **Variable Token (`--color-black`)**: `#000` — grounded in `var(--color-black)` in `:root`
- **Variable Token (`--color-white`)**: `#fff` — grounded in `var(--color-white)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×1312px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `37.5rem` extracted from `thecontenders-co` stylesheet
- **Padding & Gutters**: `var(--inline-spacing)` lateral canvas padding with `var(--grid-column-gap)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 37.5rem`, `gap: var(--grid-column-gap)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--inline-spacing)` horizontal padding
- **Media Queries**: `@media (min-width:37.5rem)`, `@media (min-width:48rem)`, `@media (min-width:80rem)`, `@media (min-width:96rem)`
- **Corner Radii**: `.3125rem`, `.375rem`, `2147483647px`, `var(--radius-md)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `DieGrotesk`
- **Body Font Stack**: `DieGrotesk Fallback`
- **Monospace / Technical Font Stack**: `iki-mono-variable`
- **H1 Display Rule**: CSS variables `--heading-h1-font-family: var(--font-serif)`, `--heading-h1-font-size: 4rem`, `--heading-h1-font-weight: 400`
- **H2 Section Rule**: CSS variables `--heading-h2-font-family: var(--font-serif)`, `--heading-h2-font-size: 3.5rem`, `--heading-h2-font-weight: 400`
- **Body Copy Rule**: CSS variables `--body-l-font-family: var(--font-sans)`, `--body-l-font-size: 1.125rem`, `--body-l-font-weight: 400`
- **Metadata & Index Rule**: CSS variables `--text-sm: .875rem`, `--text-sm--line-height: calc(1.25 / .875)`, `--default-mono-font-family: var(--font-mono)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `thecontenders-co` (`The Contenders · Strategic Brand & Design Consultancy`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.fixed> — `thecontenders-co`)**:
   - DOM & Selectors: Landmark `<nav class="fixed z-50">` hosting `The Contenders · Strategic Brand & D` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-theme="white"`, `data-homepage="true"`, `data-lenis-prevent="true"`), and stylesheet rule `.WkV8yq_className { font-family:DieGrotesk,DieGrotesk Fallback }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.fixed> — `thecontenders-co`)` (`thecontenders-co`) adapts across `@media (min-width:37.5rem)`, `@media (min-width:48rem)`, `@media (min-width:80rem)`, `@media (min-width:96rem)` with `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.78,0,.22,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<section.homepage-intro-copy> — `THE CONTENDERS IS A CONSULTANCY WH`)**:
   - DOM & Selectors: Landmark `<section class="homepage-intro-copy">` presenting display lead `THE CONTENDERS IS A CONSULTANCY WHERE BUSINESS ME...` and copy excerpt *"arrow_forward Newsletter sign up arrow_forward"* over `#e40014` canvas and `#f9fafb` ink.
   - Responsive Contract: Hero stage (`1440×1312px` desktop / `390×2400px` mobile) sets `#e40014` background with `#f9fafb` headline `THE CONTENDERS IS A CONSULTANCY WHERE BUSINESS ME...`.
3. **Primary Showcase & Content Grid (<section.homepage-intro-copy> — `THE CONTENDERS`)**:
   - DOM & Selectors: Landmark `<section class="homepage-intro-copy">` rendering section `THE CONTENDERS` with copy *"Newsletter sign up"*, asset references (`Horizontal-3fa5268f-53f1-4223-a6c...`, `Compact-7923dd47-d322-4f23-802c-c...`, `00k7ot6zx_lfg.css`, `123l3rregymnq.js`), and grid rule `.WkV8yq_variable { --font-die-grotesk:"DieGrotesk", "DieGrotesk Fallback" }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.homepage-intro-copy> — `THE CONTENDERS`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 37.5rem`, `gap: var(--grid-column-gap)`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--inline-spacing)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.homepage-intro-copy> — `Newsletter sign up`)**:
   - DOM & Selectors: Landmark `<section class="homepage-intro-copy">` framing `Newsletter sign up` and `THE CONTENDERS IS A CONSULTANCY WHERE BUSINESS M` (*"THE CONTENDERS IS A CONSULTANCY WHERE BUSINESS MEETS BRAND."*) with `#f9fafb` surface cards, `#f3f4f6` accents, and `.HMGLSG_className { font-family:Mesapholic,Mesapholic Fallback }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.homepage-intro-copy> — `Newsletter sign up`)` uses `.3125rem`, `.375rem`, `2147483647px`, `var(--radius-md)` radii, `#f3f4f6` highlights, and assets (Horizontal-3fa5268f-53f1-4223-a6c..., Compact-7923dd47-d322-4f23-802c-c..., 00k7ot6zx_lfg.css).
5. **Colophon & Global Directory Footer (<footer.fixed> — `https://thecontenders.co/`)**:
   - DOM & Selectors: Landmark `<footer class="fixed">` anchoring `The Contenders · Strategic Brand` footer links (`Overview · Index · Archive · About · Contact`), copy *"WE UNDERSTAND THAT YOUR ORGANISATION IS FIGHTING FOR SOMETHI"*, and `#d1d5dc` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.fixed> — `https://thecontenders.co/`)` aligns to `37.5rem` extracted from `thecontenders-co` stylesheet with `var(--inline-spacing)` lateral canvas padding with `var(--grid-column-gap)` grid gap and attributes (data-precedence="next", data-theme="white", data-homepage="true").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"arrow_forward Newsletter sign up arrow_forward"*
- Copy Excerpt 2: *"Newsletter sign up"*
- Copy Excerpt 3: *"THE CONTENDERS IS A CONSULTANCY WHERE BUSINESS MEETS BRAND."*
- Copy Excerpt 4: *"WE UNDERSTAND THAT YOUR ORGANISATION IS FIGHTING FOR SOMETHING."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.78,0,.22,1)`
- **Extracted Stylesheet Rules (`thecontenders-co`)**:
- `.WkV8yq_className { font-family:DieGrotesk,DieGrotesk Fallback }`
- `.WkV8yq_variable { --font-die-grotesk:"DieGrotesk", "DieGrotesk Fallback" }`
- `.HMGLSG_className { font-family:Mesapholic,Mesapholic Fallback }`
- `.HMGLSG_variable { --font-mesapholic:"Mesapholic", "Mesapholic Fallback" }`
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `thecontenders-co` stylesheet.
- **Selector `body`**: `transition: background-color .85s ease-out` extracted from `thecontenders-co` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `thecontenders-co` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<nav.fixed>` and `<section.homepage-intro-copy>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `thecontenders-co`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
