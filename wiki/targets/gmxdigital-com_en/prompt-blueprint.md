---
title: "UI Prompt Blueprint: gmxdigital-com_en"
date: 2026-11-15
target: "[[overview|gmxdigital-com_en]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#07090c` / `#bcb4c7`)"
---

# UI Design System & Master Generation Blueprint: gmxdigital-com_en

> **GMX Digital — Visual Engineering for Real Estate Launches** (https://gmxdigital.com/en/) — Launch films, 3D visualization and immersive digital experiences for real estate. GMX turns unbuilt architecture into desire before const...

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/gmxdigital-com_en/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **GMX Digital — Visual Engineering for Real Estate Launches** (`https://gmxdigital.com/en/`). Launch films, 3D visualization and immersive digital experiences for real estate. GMX turns unbuilt architecture into desire before const...
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#07090c` / `#bcb4c7`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#07090c` (`var(--ink)` in `:root`) paired with `#f2f0eb` primary typography and `#bcb4c7` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Inter` for display copy (`We engineer reality.`) with `IBM Plex Mono` and `IBM Plex Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `39rem` container bounds (`gap: 2rem`, padding `.5rem`) with `cubic-bezier(.2,.8,.2,1)` easing and HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/gmxdigital-com_en/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `39rem` extracted from `gmxdigital-com_en` stylesheet.
- **Canvas Lateral Padding & Spacing**: `.5rem` lateral canvas padding with `2rem` grid gap.
- **Border Radius Scale**: `50%`, `100px`, `4rem`, `2px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 39rem`, `gap: 2rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `.5rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:2000px)`, `@media (max-width:760px)`, `@media (min-width:1100px) and (max-height:760px)`, `@media (max-width:1100px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#07090c` | `var(--ink)` in `:root` |
| **Primary Typography Ink** | `#f2f0eb` | `var(--paper)` in `:root` |
| **Elevated Surface / Card Substrate** | `#b7bec5` | `var(--muted)` in `:root` |
| **Interactive Accent / Highlight** | `#bcb4c7` | `var(--violet)` in `:root` |
| **Secondary / Muted Copy** | `#ee99cd` | `var(--rose)` in `:root` |
| **Structural Hairline Border** | `#c6a5fa` | `var(--accent)` in `:root` |
| **Variable Token (`--hairline`)** | `#ffffff24` | `var(--hairline)` in `:root` |
| **Variable Token (`--violet-deep`)** | `#75647f` | `var(--violet-deep)` in `:root` |
| **Variable Token (`--magenta`)** | `#b86b9f` | `var(--magenta)` in `:root` |
| **Variable Token (`--mist`)** | `#9fb5b7` | `var(--mist)` in `:root` |
| **Variable Token (`--accent-gradient`)** | `#bba2cf` | `var(--accent-gradient)` in `:root` |
| **Variable Token (`--accent-gradient`)** | `#8277a9` | `var(--accent-gradient)` in `:root` |
| **Variable Token (`--accent-gradient`)** | `#68899d` | `var(--accent-gradient)` in `:root` |
| **Variable Token (`--petrol`)** | `#07171b` | `var(--petrol)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#07090c` | Typography Ink Token |
| `--paper` | `#f2f0eb` | Canvas / Surface Token |
| `--muted` | `#b7bec5` | Color / Atmospheric Token |
| `--hairline` | `#ffffff24` | Color / Atmospheric Token |
| `--violet` | `#bcb4c7` | Color / Atmospheric Token |
| `--page-pad` | `clamp(1.25rem,4.5vw,6.25rem)` | Layout / Spatial Grid Token |
| `--ui` | `'Inter',Arial,sans-serif` | Design System Custom Token |
| `--display` | `'Inter',Arial,sans-serif` | Design System Custom Token |
| `--rose` | `#ee99cd` | Color / Atmospheric Token |
| `--accent` | `#c6a5fa` | Brand / Palette Token |
| `--violet-deep` | `#75647f` | Color / Atmospheric Token |
| `--magenta` | `#b86b9f` | Color / Atmospheric Token |
| `--mist` | `#9fb5b7` | Color / Atmospheric Token |
| `--accent-gradient` | `linear-gradient(90deg, #bba2cf 0%, #8277a9 48%, #68899d 100%)` | Brand / Palette Token |
| `--petrol` | `#07171b` | Color / Atmospheric Token |
| `--ease-out` | `cubic-bezier(.16, 1, .3, 1)` | Motion / Easing Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Inter`.
- **Primary Body Stack**: `IBM Plex Mono`.
- **Technical / Metadata Stack**: `IBM Plex Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--display: 'Inter',Arial,sans-serif`; rule `h1` (`font-size: clamp(3.2rem, 8.8vw, 9.3rem)`, `line-height: .84`, `letter-spacing: -.065em`, `font-weight: 470`).
- **Section Heading (`H2`)**: rule `h2` (`font-weight: 450`).
- **Body Copy**: rule `p` (`font-size: .96rem`, `line-height: 1.65`).
- **Metadata & Navigation Labels**: rule `small` (`font-size: .875rem`, `letter-spacing: .04em`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.2,.8,.2,1)`, `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.76,0,.24,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.gmx-edition .nav-cta i`**: `transition: background .3s,color .3s,transform .4s` extracted from `gmxdigital-com_en` stylesheet.
- **Selector `.gmx-edition .button`**: `transition: box-shadow .35s, border-color .35s` extracted from `gmxdigital-com_en` stylesheet.
- **Selector `.gmx-edition .button::before`**: `transition: transform .7s cubic-bezier(.2,.8,.2,1)` extracted from `gmxdigital-com_en` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.2,.8,.2,1)`)**: Governs interactive state transitions across `<header.site-header>` and `<section.selected-films>`.
- **Runtime Interaction Engine**: Integrates HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — GMX Digital — Visual Engineering for Real  │
│ ====================================================================== │
│ [ <header.site-header>     | Films · Process · Digital · Studio · P ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.genesis>                                    |   │
│ | H1: We engineer reality.                                         |   │
│ | Substrate: #07090c    | Ink: #f2f0eb    | Accent: #bcb4c7        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.selected-films>  ) max-w: 39rem          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Direction you can see. And f |  | What makes a film a GMX film | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 2rem  ) | │
│ | [<header.site-heade] -> [<section.genesis>] -> [<section.selected-]  │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>       ) | https://gmxdigital.com/en/         │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.site-header> — `gmxdigital-com_en`)**:
   - Landmark `<header class="site-header">` hosting `GMX Digital — Visual Engineering for` navigation (`Films · Process · Digital · Studio · PT`), DOM attributes (`data-matter-scene="genesis"`, `data-matter-canvas`, `data-matter-intro`, `data-intro-state="closed"`), and stylesheet rule `.gmx-edition h2 { font-weight:450; }`.
2. **Hero Stage & Focal Lead (<section.genesis> — `We engineer reality.`)**:
   - Landmark `<section class="genesis">` presenting display lead `We engineer reality.` and copy excerpt *"GMX // MATTER ENGINE PRIME MATTER"* over `#07090c` canvas and `#f2f0eb` ink.
3. **Primary Showcase & Content Grid (<section.selected-films> — `Direction you can see. And feel.`)**:
   - Landmark `<section class="selected-films">` rendering section `Direction you can see. And feel.` with copy *"GMX // MATTER ENGINE"*, asset references (`favicon.svg`, `inter-latin-wght-normal.woff2`, `gmx-smoke.webp`, `smoke-volumetric.webp`), and grid rule `.gmx-edition h2 em { color:b7becb; font-style:normal; }`.
4. **Interactive Detail & Feature Matrix (<section.studio> — `What makes a film a GMX film.`)**:
   - Landmark `<section class="studio">` framing `What makes a film a GMX film.` and `Architecture, understood` (*"The invisible becomes matter."*) with `#b7bec5` surface cards, `#bcb4c7` accents, and `.gmx-edition p { text-wrap:pretty; }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://gmxdigital.com/en/`)**:
   - Landmark `<footer class="footer footer--signature">` anchoring `GMX Digital — Visual Engineering` footer links (`Films · Process · Digital · Studio · PT`), copy *"Preparing opening…"*, and `#c6a5fa` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: gmxdigital-com_en (GMX Digital — Visual Engineering for Real Estate Launches)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `gmxdigital-com_en` (**GMX Digital — Visual Engineering for Real Estate Launches** — `https://gmxdigital.com/en/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#07090c` / `#bcb4c7`).
- **Identity & Domain Context**: Launch films, 3D visualization and immersive digital experiences for real estate. GMX turns unbuilt architecture into desire before const...
- **Primary Substrate**: `#07090c` (`var(--ink)` in `:root`), **Primary Ink**: `#f2f0eb`, **Accent / Highlight**: `#bcb4c7`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#07090c` (`var(--ink)` in `:root`) paired with `#f2f0eb` primary typography and `#bcb4c7` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Inter` for display copy (`We engineer reality.`) with `IBM Plex Mono` and `IBM Plex Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `39rem` container bounds (`gap: 2rem`, padding `.5rem`) with `cubic-bezier(.2,.8,.2,1)` easing and HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `gmxdigital-com_en` in your global stylesheet:

:root {
  /* GMX Digital — Visual Engineering for Real Estate Launches (gmxdigital-com_en) — Ground-Truth Extracted CSS Variables */
  --ink: #07090c; /* Typography Ink Token (gmxdigital-com_en) */
  --paper: #f2f0eb; /* Canvas / Surface Token (gmxdigital-com_en) */
  --muted: #b7bec5; /* Color / Atmospheric Token (gmxdigital-com_en) */
  --hairline: #ffffff24; /* Color / Atmospheric Token (gmxdigital-com_en) */
  --violet: #bcb4c7; /* Color / Atmospheric Token (gmxdigital-com_en) */
  --page-pad: clamp(1.25rem,4.5vw,6.25rem); /* Layout / Spatial Grid Token (gmxdigital-com_en) */
  --ui: 'Inter',Arial,sans-serif; /* Design System Custom Token (gmxdigital-com_en) */
  --display: 'Inter',Arial,sans-serif; /* Design System Custom Token (gmxdigital-com_en) */
  --rose: #ee99cd; /* Color / Atmospheric Token (gmxdigital-com_en) */
  --accent: #c6a5fa; /* Brand / Palette Token (gmxdigital-com_en) */
  --violet-deep: #75647f; /* Color / Atmospheric Token (gmxdigital-com_en) */
  --magenta: #b86b9f; /* Color / Atmospheric Token (gmxdigital-com_en) */
  --mist: #9fb5b7; /* Color / Atmospheric Token (gmxdigital-com_en) */
  --accent-gradient: linear-gradient(90deg, #bba2cf 0%, #8277a9 48%, #68899d 100%); /* Brand / Palette Token (gmxdigital-com_en) */
  --petrol: #07171b; /* Color / Atmospheric Token (gmxdigital-com_en) */
  --ease-out: cubic-bezier(.16, 1, .3, 1); /* Motion / Easing Token (gmxdigital-com_en) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#07090c` — grounded in `var(--ink)` in `:root`
- **Primary Typography Ink**: `#f2f0eb` — grounded in `var(--paper)` in `:root`
- **Elevated Surface / Card Substrate**: `#b7bec5` — grounded in `var(--muted)` in `:root`
- **Interactive Accent / Highlight**: `#bcb4c7` — grounded in `var(--violet)` in `:root`
- **Secondary / Muted Copy**: `#ee99cd` — grounded in `var(--rose)` in `:root`
- **Structural Hairline Border**: `#c6a5fa` — grounded in `var(--accent)` in `:root`
- **Variable Token (`--hairline`)**: `#ffffff24` — grounded in `var(--hairline)` in `:root`
- **Variable Token (`--violet-deep`)**: `#75647f` — grounded in `var(--violet-deep)` in `:root`
- **Variable Token (`--magenta`)**: `#b86b9f` — grounded in `var(--magenta)` in `:root`
- **Variable Token (`--mist`)**: `#9fb5b7` — grounded in `var(--mist)` in `:root`
- **Variable Token (`--accent-gradient`)**: `#bba2cf` — grounded in `var(--accent-gradient)` in `:root`
- **Variable Token (`--accent-gradient`)**: `#8277a9` — grounded in `var(--accent-gradient)` in `:root`
- **Variable Token (`--accent-gradient`)**: `#68899d` — grounded in `var(--accent-gradient)` in `:root`
- **Variable Token (`--petrol`)**: `#07171b` — grounded in `var(--petrol)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `39rem` extracted from `gmxdigital-com_en` stylesheet
- **Padding & Gutters**: `.5rem` lateral canvas padding with `2rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 39rem`, `gap: 2rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `.5rem` horizontal padding
- **Media Queries**: `@media (min-width:2000px)`, `@media (max-width:760px)`, `@media (min-width:1100px) and (max-height:760px)`, `@media (max-width:1100px)`
- **Corner Radii**: `50%`, `100px`, `4rem`, `2px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `IBM Plex Mono`
- **Monospace / Technical Font Stack**: `IBM Plex Mono`
- **H1 Display Rule**: CSS variables `--display: 'Inter',Arial,sans-serif`; rule `h1` (`font-size: clamp(3.2rem, 8.8vw, 9.3rem)`, `line-height: .84`, `letter-spacing: -.065em`, `font-weight: 470`)
- **H2 Section Rule**: rule `h2` (`font-weight: 450`)
- **Body Copy Rule**: rule `p` (`font-size: .96rem`, `line-height: 1.65`)
- **Metadata & Index Rule**: rule `small` (`font-size: .875rem`, `letter-spacing: .04em`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `gmxdigital-com_en` (`GMX Digital — Visual Engineering for Real Estate Launches`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.site-header> — `gmxdigital-com_en`)**:
   - DOM & Selectors: Landmark `<header class="site-header">` hosting `GMX Digital — Visual Engineering for` navigation (`Films · Process · Digital · Studio · PT`), DOM attributes (`data-matter-scene="genesis"`, `data-matter-canvas`, `data-matter-intro`, `data-intro-state="closed"`), and stylesheet rule `.gmx-edition h2 { font-weight:450; }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.site-header> — `gmxdigital-com_en`)` (`gmxdigital-com_en`) adapts across `@media (min-width:2000px)`, `@media (max-width:760px)`, `@media (min-width:1100px) and (max-height:760px)`, `@media (max-width:1100px)` with `cubic-bezier(.2,.8,.2,1)`, `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.76,0,.24,1)` transitions and links `Films · Process · Digital · Studio · PT`.
2. **Hero Stage & Focal Lead (<section.genesis> — `We engineer reality.`)**:
   - DOM & Selectors: Landmark `<section class="genesis">` presenting display lead `We engineer reality.` and copy excerpt *"GMX // MATTER ENGINE PRIME MATTER"* over `#07090c` canvas and `#f2f0eb` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#07090c` background with `#f2f0eb` headline `We engineer reality.`.
3. **Primary Showcase & Content Grid (<section.selected-films> — `Direction you can see. And feel.`)**:
   - DOM & Selectors: Landmark `<section class="selected-films">` rendering section `Direction you can see. And feel.` with copy *"GMX // MATTER ENGINE"*, asset references (`favicon.svg`, `inter-latin-wght-normal.woff2`, `gmx-smoke.webp`, `smoke-volumetric.webp`), and grid rule `.gmx-edition h2 em { color:b7becb; font-style:normal; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.selected-films> — `Direction you can see. And feel.`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 39rem`, `gap: 2rem`) on desktop and Single-column vertical stack at `390px` viewport width with `.5rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.studio> — `What makes a film a GMX film.`)**:
   - DOM & Selectors: Landmark `<section class="studio">` framing `What makes a film a GMX film.` and `Architecture, understood` (*"The invisible becomes matter."*) with `#b7bec5` surface cards, `#bcb4c7` accents, and `.gmx-edition p { text-wrap:pretty; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.studio> — `What makes a film a GMX film.`)` uses `50%`, `100px`, `4rem`, `2px` radii, `#bcb4c7` highlights, and assets (favicon.svg, inter-latin-wght-normal.woff2, gmx-smoke.webp).
5. **Colophon & Global Directory Footer (<footer.footer> — `https://gmxdigital.com/en/`)**:
   - DOM & Selectors: Landmark `<footer class="footer footer--signature">` anchoring `GMX Digital — Visual Engineering` footer links (`Films · Process · Digital · Studio · PT`), copy *"Preparing opening…"*, and `#c6a5fa` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer> — `https://gmxdigital.com/en/`)` aligns to `39rem` extracted from `gmxdigital-com_en` stylesheet with `.5rem` lateral canvas padding with `2rem` grid gap and attributes (data-matter-scene="genesis", data-matter-canvas, data-matter-intro).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"GMX // MATTER ENGINE PRIME MATTER"*
- Copy Excerpt 2: *"GMX // MATTER ENGINE"*
- Copy Excerpt 3: *"The invisible becomes matter."*
- Copy Excerpt 4: *"Preparing opening…"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.2,.8,.2,1)`, `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.76,0,.24,1)`
- **Extracted Stylesheet Rules (`gmxdigital-com_en`)**:
- `.gmx-edition h2 { font-weight:450; }`
- `.gmx-edition h2 em { color:b7becb; font-style:normal; }`
- `.gmx-edition p { text-wrap:pretty; }`
- `focus-visible { outline:2px solid d8d8ec; outline-offset:6px; }`
- `.gmx-edition main > section { scroll-margin-top:5.25rem; }`
- **Per-Selector Transition Rules**:
- **Selector `.gmx-edition .nav-cta i`**: `transition: background .3s,color .3s,transform .4s` extracted from `gmxdigital-com_en` stylesheet.
- **Selector `.gmx-edition .button`**: `transition: box-shadow .35s, border-color .35s` extracted from `gmxdigital-com_en` stylesheet.
- **Selector `.gmx-edition .button::before`**: `transition: transform .7s cubic-bezier(.2,.8,.2,1)` extracted from `gmxdigital-com_en` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.2,.8,.2,1)`)**: Governs interactive state transitions across `<header.site-header>` and `<section.selected-films>`.
- **Runtime Interaction Engine**: Integrates HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `gmxdigital-com_en`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
