---
title: "UI Prompt Blueprint: www-codeofsagar-in"
date: 2026-11-15
target: "[[overview|www-codeofsagar-in]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#171717` / `#0f0f0f`)"
---

# UI Design System & Master Generation Blueprint: www-codeofsagar-in

> **Sagar K. Ghosh — Full-stack Developer & Designer** (https://www.codeofsagar.in/) — Websites and stores that sell, 3D people remember and automation that gives your team its time back, designed and built by Sagar K. Ghosh.

![Desktop Viewport Capture (1440x17965)](file:///root/projects/fleet/wiki/targets/www-codeofsagar-in/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Sagar K. Ghosh — Full-stack Developer & Designer** (`https://www.codeofsagar.in/`). Websites and stores that sell, 3D people remember and automation that gives your team its time back, designed and built by Sagar K. Ghosh.
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#171717` / `#0f0f0f`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#171717` (`var(--color-neutral-900)` in `:root`) paired with `#fff` primary typography and `#0f0f0f` accents.
  - **Extracted Typographic Hierarchy**: Pairs `spaceGrotesk` for display copy (`Websites that sell. AI that never sl`) with `spaceGrotesk Fallback` and `spaceMono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1700px` container bounds (`gap: var(--spacing)`, padding `var(--spacing)`) with `cubic-bezier(.4,0,1,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/www-codeofsagar-in/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×17965px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `1700px` extracted from `www-codeofsagar-in` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--spacing)` lateral canvas padding with `var(--spacing)` grid gap.
- **Border Radius Scale**: `.25rem`, `2rem`, `var(--radius-md)`, `var(--radius-sm)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1700px`, `gap: var(--spacing)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--spacing)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:1700px)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#171717` | `var(--color-neutral-900)` in `:root` |
| **Primary Typography Ink** | `#000` | `var(--color-black)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff` | `var(--color-white)` in `:root` |
| **Interactive Accent / Highlight** | `#0f0f0f` | `var(--theme-black-olive)` in `:root` |
| **Secondary / Muted Copy** | `#eb5e28` | `var(--theme-burnt-orange)` in `:root` |
| **Structural Hairline Border** | `#262626` | `var(--ink-soft)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-neutral-900` | `#171717` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |
| `--text-xs--line-height` | `calc(1 / .75)` | Typography Ink Token |
| `--text-lg` | `1.125rem` | Typography Ink Token |
| `--text-lg--line-height` | `calc(1.75 / 1.125)` | Typography Ink Token |
| `--text-7xl` | `4.5rem` | Typography Ink Token |
| `--text-7xl--line-height` | `1` | Typography Ink Token |
| `--font-weight-light` | `300` | Canvas / Surface Token |
| `--font-weight-medium` | `500` | Typography / Scale Token |
| `--font-weight-semibold` | `600` | Typography / Scale Token |
| `--font-weight-bold` | `700` | Typography / Scale Token |
| `--tracking-tight` | `-.025em` | Typography / Scale Token |
| `--tracking-wide` | `.025em` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `spaceGrotesk`.
- **Primary Body Stack**: `spaceGrotesk Fallback`.
- **Technical / Metadata Stack**: `spaceMono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--font-display: var(--font-space-grotesk), ui-sans-serif, system-ui, sans-serif`.
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--text-lg)`, `var(--text-xs)`).
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--text-lg)`, `var(--text-xs)`).
- **Metadata & Navigation Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--default-mono-font-family: var(--font-mono)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `www-codeofsagar-in` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-codeofsagar-in` stylesheet.
- **Selector `.transition\!`**: `transition: var(--tw-ease,var(--default-transition-timing-function))!impor...` extracted from `www-codeofsagar-in` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.NavBar-module__aMivtW__bar>` and `<section.grain-surface>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Sagar K. Ghosh — Full-stack Developer & De │
│ ====================================================================== │
│ [ <header.NavBar-module__a | H H o o m m e e · W W o o r r k k · A  ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.relative>                                   |   │
│ | H1: Websites that sell. AI that never sleeps.                    |   │
│ | Substrate: #171717    | Ink: #fff       | Accent: #0f0f0f        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.grain-surface>   ) max-w: 1700px         |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | S A G A R K . G H O S H      |  | Get Found. Get Chosen. Get B | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<header.NavBar-mod] -> [<section.relative>] -> [<section.grain-sur] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.relative>     ) | https://www.codeofsagar.in/        │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.NavBar-module__aMivtW__bar> — `www-codeofsagar-in`)**:
   - Landmark `<header class="NavBar-module__aMivtW__bar">` hosting `Sagar K. Ghosh — Full-stack Develope` navigation (`H H o o m m e e · W W o o r r k k · A A b b o o u u t t · F F A A Q Q`), DOM attributes (`data-nav-solid`, `data-lines-anim`, `data-sky="day"`, `data-dot="small"`), and stylesheet rule `host { --color-neutral-900:lab(7.78201% -.0000149012 0) }`.
2. **Hero Stage & Focal Lead (<section.relative> — `Websites that sell. AI that never `)**:
   - Landmark `<section class="relative z-10">` presenting display lead `Websites that sell. AI that never sleeps.` and copy excerpt *"S S e e r r v v i i c c e e s s"* over `#171717` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.grain-surface> — `S A G A R K . G H O S H`)**:
   - Landmark `<section class="grain-surface home-titles">` rendering section `S A G A R K . G H O S H` with copy *"A A b b o o u u t t"*, asset references (`space_grotesk_latin_wght_normal-s...`, `space_mono_latin_400_normal-s.p.1...`, `space_mono_latin_700_normal-s.p.0...`, `36s0t0o8ux5as.js`), and grid rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.font-grotesk> — `Get Found. Get Chosen. Get Bought.`)**:
   - Landmark `<section class="font-grotesk">` framing `Get Found. Get Chosen. Get Bought.` and `What clients say` (*"P P l l a a y y g g r r o o u u n n d d"*) with `#fff` surface cards, `#0f0f0f` accents, and `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://www.codeofsagar.in/`)**:
   - Landmark `<footer class="relative flex">` anchoring `Sagar K. Ghosh — Full-stack Deve` footer links (`H H o o m m e e · W W o o r r k k · A A b b o o u u t t · F F A A Q Q`), copy *"C C o o n n t t a a c c t t"*, and `#262626` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-codeofsagar-in (Sagar K. Ghosh — Full-stack Developer & Designer)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-codeofsagar-in` (**Sagar K. Ghosh — Full-stack Developer & Designer** — `https://www.codeofsagar.in/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#171717` / `#0f0f0f`).
- **Identity & Domain Context**: Websites and stores that sell, 3D people remember and automation that gives your team its time back, designed and built by Sagar K. Ghosh.
- **Primary Substrate**: `#171717` (`var(--color-neutral-900)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#0f0f0f`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#171717` (`var(--color-neutral-900)` in `:root`) paired with `#fff` primary typography and `#0f0f0f` accents.
  - **Extracted Typographic Hierarchy**: Pairs `spaceGrotesk` for display copy (`Websites that sell. AI that never sl`) with `spaceGrotesk Fallback` and `spaceMono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1700px` container bounds (`gap: var(--spacing)`, padding `var(--spacing)`) with `cubic-bezier(.4,0,1,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-codeofsagar-in` in your global stylesheet:

:root {
  /* Sagar K. Ghosh — Full-stack Developer & Designer (www-codeofsagar-in) — Ground-Truth Extracted CSS Variables */
  --color-neutral-900: #171717; /* Brand / Palette Token (www-codeofsagar-in) */
  --color-black: #000; /* Canvas / Surface Token (www-codeofsagar-in) */
  --color-white: #fff; /* Canvas / Surface Token (www-codeofsagar-in) */
  --spacing: .25rem; /* Layout / Spatial Grid Token (www-codeofsagar-in) */
  --text-xs: .75rem; /* Typography Ink Token (www-codeofsagar-in) */
  --text-xs--line-height: calc(1 / .75); /* Typography Ink Token (www-codeofsagar-in) */
  --text-lg: 1.125rem; /* Typography Ink Token (www-codeofsagar-in) */
  --text-lg--line-height: calc(1.75 / 1.125); /* Typography Ink Token (www-codeofsagar-in) */
  --text-7xl: 4.5rem; /* Typography Ink Token (www-codeofsagar-in) */
  --text-7xl--line-height: 1; /* Typography Ink Token (www-codeofsagar-in) */
  --font-weight-light: 300; /* Canvas / Surface Token (www-codeofsagar-in) */
  --font-weight-medium: 500; /* Typography / Scale Token (www-codeofsagar-in) */
  --font-weight-semibold: 600; /* Typography / Scale Token (www-codeofsagar-in) */
  --font-weight-bold: 700; /* Typography / Scale Token (www-codeofsagar-in) */
  --tracking-tight: -.025em; /* Typography / Scale Token (www-codeofsagar-in) */
  --tracking-wide: .025em; /* Typography / Scale Token (www-codeofsagar-in) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#171717` — grounded in `var(--color-neutral-900)` in `:root`
- **Primary Typography Ink**: `#000` — grounded in `var(--color-black)` in `:root`
- **Elevated Surface / Card Substrate**: `#fff` — grounded in `var(--color-white)` in `:root`
- **Interactive Accent / Highlight**: `#0f0f0f` — grounded in `var(--theme-black-olive)` in `:root`
- **Secondary / Muted Copy**: `#eb5e28` — grounded in `var(--theme-burnt-orange)` in `:root`
- **Structural Hairline Border**: `#262626` — grounded in `var(--ink-soft)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×17965px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1700px` extracted from `www-codeofsagar-in` stylesheet
- **Padding & Gutters**: `var(--spacing)` lateral canvas padding with `var(--spacing)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1700px`, `gap: var(--spacing)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--spacing)` horizontal padding
- **Media Queries**: `@media (min-width:1700px)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`
- **Corner Radii**: `.25rem`, `2rem`, `var(--radius-md)`, `var(--radius-sm)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `spaceGrotesk`
- **Body Font Stack**: `spaceGrotesk Fallback`
- **Monospace / Technical Font Stack**: `spaceMono`
- **H1 Display Rule**: CSS variables `--font-display: var(--font-space-grotesk), ui-sans-serif, system-ui, sans-serif`
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--text-lg)`, `var(--text-xs)`)
- **Body Copy Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--text-lg)`, `var(--text-xs)`)
- **Metadata & Index Rule**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--default-mono-font-family: var(--font-mono)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-codeofsagar-in` (`Sagar K. Ghosh — Full-stack Developer & Designer`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.NavBar-module__aMivtW__bar> — `www-codeofsagar-in`)**:
   - DOM & Selectors: Landmark `<header class="NavBar-module__aMivtW__bar">` hosting `Sagar K. Ghosh — Full-stack Develope` navigation (`H H o o m m e e · W W o o r r k k · A A b b o o u u t t · F F A A Q Q`), DOM attributes (`data-nav-solid`, `data-lines-anim`, `data-sky="day"`, `data-dot="small"`), and stylesheet rule `host { --color-neutral-900:lab(7.78201% -.0000149012 0) }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.NavBar-module__aMivtW__bar> — `www-codeofsagar-in`)` (`www-codeofsagar-in`) adapts across `@media (min-width:1700px)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)` with `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `H H o o m m e e · W W o o r r k k · A A b b o o u u t t · F F A A Q Q`.
2. **Hero Stage & Focal Lead (<section.relative> — `Websites that sell. AI that never `)**:
   - DOM & Selectors: Landmark `<section class="relative z-10">` presenting display lead `Websites that sell. AI that never sleeps.` and copy excerpt *"S S e e r r v v i i c c e e s s"* over `#171717` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×17965px` desktop / `390×2400px` mobile) sets `#171717` background with `#fff` headline `Websites that sell. AI that never sleeps.`.
3. **Primary Showcase & Content Grid (<section.grain-surface> — `S A G A R K . G H O S H`)**:
   - DOM & Selectors: Landmark `<section class="grain-surface home-titles">` rendering section `S A G A R K . G H O S H` with copy *"A A b b o o u u t t"*, asset references (`space_grotesk_latin_wght_normal-s...`, `space_mono_latin_400_normal-s.p.1...`, `space_mono_latin_700_normal-s.p.0...`, `36s0t0o8ux5as.js`), and grid rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.grain-surface> — `S A G A R K . G H O S H`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1700px`, `gap: var(--spacing)`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--spacing)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.font-grotesk> — `Get Found. Get Chosen. Get Bought.`)**:
   - DOM & Selectors: Landmark `<section class="font-grotesk">` framing `Get Found. Get Chosen. Get Bought.` and `What clients say` (*"P P l l a a y y g g r r o o u u n n d d"*) with `#fff` surface cards, `#0f0f0f` accents, and `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.font-grotesk> — `Get Found. Get Chosen. Get Bought.`)` uses `.25rem`, `2rem`, `var(--radius-md)`, `var(--radius-sm)` radii, `#0f0f0f` highlights, and assets (space_grotesk_latin_wght_normal-s..., space_mono_latin_400_normal-s.p.1..., space_mono_latin_700_normal-s.p.0...).
5. **Colophon & Global Directory Footer (<footer.relative> — `https://www.codeofsagar.in/`)**:
   - DOM & Selectors: Landmark `<footer class="relative flex">` anchoring `Sagar K. Ghosh — Full-stack Deve` footer links (`H H o o m m e e · W W o o r r k k · A A b b o o u u t t · F F A A Q Q`), copy *"C C o o n n t t a a c c t t"*, and `#262626` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.relative> — `https://www.codeofsagar.in/`)` aligns to `1700px` extracted from `www-codeofsagar-in` stylesheet with `var(--spacing)` lateral canvas padding with `var(--spacing)` grid gap and attributes (data-nav-solid, data-lines-anim, data-sky="day").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"S S e e r r v v i i c c e e s s"*
- Copy Excerpt 2: *"A A b b o o u u t t"*
- Copy Excerpt 3: *"P P l l a a y y g g r r o o u u n n d d"*
- Copy Excerpt 4: *"C C o o n n t t a a c c t t"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`www-codeofsagar-in`)**:
- `host { --color-neutral-900:lab(7.78201% -.0000149012 0) }`
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `www-codeofsagar-in` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-codeofsagar-in` stylesheet.
- **Selector `.transition\!`**: `transition: var(--tw-ease,var(--default-transition-timing-function))!impor...` extracted from `www-codeofsagar-in` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.NavBar-module__aMivtW__bar>` and `<section.grain-surface>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-codeofsagar-in`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
