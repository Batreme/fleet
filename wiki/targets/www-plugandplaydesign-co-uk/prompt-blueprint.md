---
title: "UI Prompt Blueprint: www-plugandplaydesign-co-uk"
date: 2026-11-15
target: "[[overview|www-plugandplaydesign-co-uk]]"
status: analyzed
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#c40806` canvas, `#fff` ink, `#000` accent)"
---

# UI Design System & Master Generation Blueprint: www-plugandplaydesign-co-uk

> **Web Design Agency London & Guildford · Plug & Play** (https://www.plugandplaydesign.co.uk/) — Award-winning web design agency in London and Guildford. High-performance websites and digital retainers that drive measurable growth.

![Desktop Viewport Capture (1440x17101)](file:///root/projects/fleet/wiki/targets/www-plugandplaydesign-co-uk/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Web Design Agency London & Guildford · Plug & Play** (`https://www.plugandplaydesign.co.uk/`). Award-winning web design agency in London and Guildford. High-performance websites and digital retainers that drive measurable growth.
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#c40806` canvas, `#fff` ink, `#000` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#c40806` (`var(--color-red-600)` in `:root`) paired with `#fff` primary typography and `#000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Geist` for display copy (`Web Design Agency in London and Surr`) with `Geist Mono` and `Geist Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: .25rem`, padding `1rem`) with `cubic-bezier(0,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/www-plugandplaydesign-co-uk/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×17101px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `40rem` extracted from `www-plugandplaydesign-co-uk` stylesheet.
- **Canvas Lateral Padding & Spacing**: `1rem` lateral canvas padding with `.25rem` grid gap.
- **Border Radius Scale**: `.25rem`, `var(--radius-cursor-tooltip)`, `var(--radius-full)`, `var(--radius-lg)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: .25rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `1rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:67.5rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#c40806` | `var(--color-red-600)` in `:root` |
| **Primary Typography Ink** | `#5f58ff` | `var(--color-purple-600)` in `:root` |
| **Elevated Surface / Card Substrate** | `#4b23cd` | `var(--color-purple-700)` in `:root` |
| **Interactive Accent / Highlight** | `#000` | `var(--color-black)` in `:root` |
| **Secondary / Muted Copy** | `#fff` | `var(--color-white)` in `:root` |
| **Structural Hairline Border** | `#fafafa` | `var(--color-grey-50)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `"Geist","Helvetica Neue",Arial,sans-serif` | Typography / Scale Token |
| `--font-mono` | `"Geist Mono",ui-monospace,"SF Mono",Menlo,monospace` | Typography / Scale Token |
| `--color-red-600` | `#c40806` | Brand / Palette Token |
| `--color-purple-600` | `#5f58ff` | Brand / Palette Token |
| `--color-purple-700` | `#4b23cd` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-sm` | `24rem` | Layout / Spatial Grid Token |
| `--container-md` | `28rem` | Layout / Spatial Grid Token |
| `--font-weight-light` | `300` | Canvas / Surface Token |
| `--font-weight-normal` | `400` | Typography / Scale Token |
| `--font-weight-medium` | `500` | Typography / Scale Token |
| `--radius-xs` | `.125rem` | Elevation / Border Token |
| `--radius-sm` | `.25rem` | Elevation / Border Token |
| `--radius-md` | `.5rem` | Elevation / Border Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Geist`.
- **Primary Body Stack**: `Geist Mono`.
- **Technical / Metadata Stack**: `Geist Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`font-size: var(--text-body-sm)`, `line-height: var(--tw-leading,var(...`, `letter-spacing: var(--tw-tracking,var...`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: var(--text-body-sm)`, `line-height: var(--tw-leading,var(...`, `letter-spacing: var(--tw-tracking,var...`).
- **Body Copy**: CSS variables `--text-body-sm: .875rem`, `--text-body-sm--line-height: 1.4`, `--text-body-sm--letter-spacing: -.02em`.
- **Metadata & Navigation Labels**: CSS variables `--font-mono: "Geist Mono",ui-monospace,"SF Mono",Menlo,monospace`, `--default-mono-font-family: var(--font-mono)`, `--color-media-caption: #0006`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.7,.2,.18,.85)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `www-plugandplaydesign-co-uk` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-plugandplaydesign-co-uk` stylesheet.
- **Selector `opacity\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-plugandplaydesign-co-uk` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.fixed>` and `<section.bg-background>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Web Design Agency London & Guildford · Plu │
│ ====================================================================== │
│ [ <header.fixed>           | Our Work · Web Design · Branding · Dig ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.px-page>                                    |   │
│ | H1: Web Design Agency in London and Surrey                       |   │
│ | Substrate: #c40806    | Ink: #fff       | Accent: #000           |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.bg-background>   ) max-w: 40rem          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Our process                  |  | What types of websites do we | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .25rem) | │
│ | [<header.fixed>] -> [<section.px-page>] -> [<section.bg-backgr] |    │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.bg-background>) | https://www.plugandplaydesign.co.u │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.fixed> — `www-plugandplaydesign-co-uk`)**:
   - Landmark `<header class="fixed inset-x-0">` hosting `Web Design Agency London & Guildford` navigation (`Our Work · Web Design · Branding · Digital Marketing · UX / UI Design`), DOM attributes (`data-hero-enter`, `data-precedence="next"`, `data-precedence="next"`, `data-domain="plugandplaydesign.co.uk"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.px-page> — `Web Design Agency in London and Su`)**:
   - Landmark `<section class="px-page pt-section">` presenting display lead `Web Design Agency in London and Surrey` and copy excerpt *"Plug and Play is a creative web design agency based in Guildford,"* over `#c40806` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.bg-background> — `Our process`)**:
   - Landmark `<section class="bg-background px-page">` rendering section `Our process` with copy *"digital transformation"*, asset references (`ca4cfa437ae45d18.css`, `dd5d352a082118c1.css`, `webpack-43624c9fe997cbf4.js`, `cf303062-0b72e54636065547.js`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.w-screen> — `What types of websites do we build`)**:
   - Landmark `<section class="w-screen">` framing `What types of websites do we build?` and `What industries do you work with?` (*"(via its enterprise site,"*) with `#4b23cd` surface cards, `#000` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.bg-background> — `https://www.plugandplaydesign.co.uk/`)**:
   - Landmark `<footer class="bg-background px-page">` anchoring `Web Design Agency London & Guild` footer links (`Our Work · Web Design · Branding · Digital Marketing · UX / UI Design`), copy *"digital marketing strategy"*, and `#fafafa` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-plugandplaydesign-co-uk (Web Design Agency London & Guildford · Plug & Play)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-plugandplaydesign-co-uk` (**Web Design Agency London & Guildford · Plug & Play** — `https://www.plugandplaydesign.co.uk/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#c40806` canvas, `#fff` ink, `#000` accent).
- **Identity & Domain Context**: Award-winning web design agency in London and Guildford. High-performance websites and digital retainers that drive measurable growth.
- **Primary Substrate**: `#c40806` (`var(--color-red-600)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#000`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#c40806` (`var(--color-red-600)` in `:root`) paired with `#fff` primary typography and `#000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Geist` for display copy (`Web Design Agency in London and Surr`) with `Geist Mono` and `Geist Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: .25rem`, padding `1rem`) with `cubic-bezier(0,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-plugandplaydesign-co-uk` in your global stylesheet:

:root {
  /* Web Design Agency London & Guildford · Plug & Play (www-plugandplaydesign-co-uk) — Ground-Truth Extracted CSS Variables */
  --font-sans: "Geist","Helvetica Neue",Arial,sans-serif; /* Typography / Scale Token (www-plugandplaydesign-co-uk) */
  --font-mono: "Geist Mono",ui-monospace,"SF Mono",Menlo,monospace; /* Typography / Scale Token (www-plugandplaydesign-co-uk) */
  --color-red-600: #c40806; /* Brand / Palette Token (www-plugandplaydesign-co-uk) */
  --color-purple-600: #5f58ff; /* Brand / Palette Token (www-plugandplaydesign-co-uk) */
  --color-purple-700: #4b23cd; /* Brand / Palette Token (www-plugandplaydesign-co-uk) */
  --color-black: #000; /* Canvas / Surface Token (www-plugandplaydesign-co-uk) */
  --color-white: #fff; /* Canvas / Surface Token (www-plugandplaydesign-co-uk) */
  --spacing: .25rem; /* Layout / Spatial Grid Token (www-plugandplaydesign-co-uk) */
  --container-sm: 24rem; /* Layout / Spatial Grid Token (www-plugandplaydesign-co-uk) */
  --container-md: 28rem; /* Layout / Spatial Grid Token (www-plugandplaydesign-co-uk) */
  --font-weight-light: 300; /* Canvas / Surface Token (www-plugandplaydesign-co-uk) */
  --font-weight-normal: 400; /* Typography / Scale Token (www-plugandplaydesign-co-uk) */
  --font-weight-medium: 500; /* Typography / Scale Token (www-plugandplaydesign-co-uk) */
  --radius-xs: .125rem; /* Elevation / Border Token (www-plugandplaydesign-co-uk) */
  --radius-sm: .25rem; /* Elevation / Border Token (www-plugandplaydesign-co-uk) */
  --radius-md: .5rem; /* Elevation / Border Token (www-plugandplaydesign-co-uk) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#c40806` — grounded in `var(--color-red-600)` in `:root`
- **Primary Typography Ink**: `#5f58ff` — grounded in `var(--color-purple-600)` in `:root`
- **Elevated Surface / Card Substrate**: `#4b23cd` — grounded in `var(--color-purple-700)` in `:root`
- **Interactive Accent / Highlight**: `#000` — grounded in `var(--color-black)` in `:root`
- **Secondary / Muted Copy**: `#fff` — grounded in `var(--color-white)` in `:root`
- **Structural Hairline Border**: `#fafafa` — grounded in `var(--color-grey-50)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×17101px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `40rem` extracted from `www-plugandplaydesign-co-uk` stylesheet
- **Padding & Gutters**: `1rem` lateral canvas padding with `.25rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: .25rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `1rem` horizontal padding
- **Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:67.5rem)`
- **Corner Radii**: `.25rem`, `var(--radius-cursor-tooltip)`, `var(--radius-full)`, `var(--radius-lg)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Geist`
- **Body Font Stack**: `Geist Mono`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **H1 Display Rule**: rule `h1` (`font-size: var(--text-body-sm)`, `line-height: var(--tw-leading,var(...`, `letter-spacing: var(--tw-tracking,var...`)
- **H2 Section Rule**: rule `h2` (`font-size: var(--text-body-sm)`, `line-height: var(--tw-leading,var(...`, `letter-spacing: var(--tw-tracking,var...`)
- **Body Copy Rule**: CSS variables `--text-body-sm: .875rem`, `--text-body-sm--line-height: 1.4`, `--text-body-sm--letter-spacing: -.02em`
- **Metadata & Index Rule**: CSS variables `--font-mono: "Geist Mono",ui-monospace,"SF Mono",Menlo,monospace`, `--default-mono-font-family: var(--font-mono)`, `--color-media-caption: #c40806`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-plugandplaydesign-co-uk` (`Web Design Agency London & Guildford · Plug & Play`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.fixed> — `www-plugandplaydesign-co-uk`)**:
   - DOM & Selectors: Landmark `<header class="fixed inset-x-0">` hosting `Web Design Agency London & Guildford` navigation (`Our Work · Web Design · Branding · Digital Marketing · UX / UI Design`), DOM attributes (`data-hero-enter`, `data-precedence="next"`, `data-precedence="next"`, `data-domain="plugandplaydesign.co.uk"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.fixed> — `www-plugandplaydesign-co-uk`)` (`www-plugandplaydesign-co-uk`) adapts across `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:67.5rem)` with `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.7,.2,.18,.85)` transitions and links `Our Work · Web Design · Branding · Digital Marketing · UX / UI Design`.
2. **Hero Stage & Focal Lead (<section.px-page> — `Web Design Agency in London and Su`)**:
   - DOM & Selectors: Landmark `<section class="px-page pt-section">` presenting display lead `Web Design Agency in London and Surrey` and copy excerpt *"Plug and Play is a creative web design agency based in Guildford,"* over `#c40806` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×17101px` desktop / `390×2400px` mobile) sets `#c40806` background with `#fff` headline `Web Design Agency in London and Surrey`.
3. **Primary Showcase & Content Grid (<section.bg-background> — `Our process`)**:
   - DOM & Selectors: Landmark `<section class="bg-background px-page">` rendering section `Our process` with copy *"digital transformation"*, asset references (`ca4cfa437ae45d18.css`, `dd5d352a082118c1.css`, `webpack-43624c9fe997cbf4.js`, `cf303062-0b72e54636065547.js`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.bg-background> — `Our process`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: .25rem`) on desktop and Single-column vertical stack at `390px` viewport width with `1rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.w-screen> — `What types of websites do we build`)**:
   - DOM & Selectors: Landmark `<section class="w-screen">` framing `What types of websites do we build?` and `What industries do you work with?` (*"(via its enterprise site,"*) with `#4b23cd` surface cards, `#000` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.w-screen> — `What types of websites do we build`)` uses `.25rem`, `var(--radius-cursor-tooltip)`, `var(--radius-full)`, `var(--radius-lg)` radii, `#000` highlights, and assets (ca4cfa437ae45d18.css, dd5d352a082118c1.css, webpack-43624c9fe997cbf4.js).
5. **Colophon & Global Directory Footer (<footer.bg-background> — `https://www.plugandplaydesign.co.uk/`)**:
   - DOM & Selectors: Landmark `<footer class="bg-background px-page">` anchoring `Web Design Agency London & Guild` footer links (`Our Work · Web Design · Branding · Digital Marketing · UX / UI Design`), copy *"digital marketing strategy"*, and `#fafafa` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.bg-background> — `https://www.plugandplaydesign.co.uk/`)` aligns to `40rem` extracted from `www-plugandplaydesign-co-uk` stylesheet with `1rem` lateral canvas padding with `.25rem` grid gap and attributes (data-hero-enter, data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Plug and Play is a creative web design agency based in Guildford, Surrey, serving..."*
- Copy Excerpt 2: *"digital transformation"*
- Copy Excerpt 3: *"(via its enterprise site,"*
- Copy Excerpt 4: *"digital marketing strategy"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.7,.2,.18,.85)`
- **Extracted Stylesheet Rules (`www-plugandplaydesign-co-uk`)**:
- `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- `sup { vertical-align:baseline;font-size:75%;line-height:0;position:relative }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `www-plugandplaydesign-co-uk` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-plugandplaydesign-co-uk` stylesheet.
- **Selector `opacity\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-plugandplaydesign-co-uk` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.fixed>` and `<section.bg-background>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-plugandplaydesign-co-uk`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
