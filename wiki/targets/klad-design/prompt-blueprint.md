---
title: "UI Prompt Blueprint: klad-design"
date: 2026-11-15
target: "[[overview|klad-design]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#010101` / `#0000`)"
---

# UI Design System & Master Generation Blueprint: klad-design

> **Multidisciplinary Design Syndicate – KLAD** (https://klad.design/) — Klad Syndicate is a multidisciplinary design studio offering comprehensive solutions for ambitious brands. Every design we deliver is ori...

![Desktop Viewport Capture (1440x6793)](file:///root/projects/fleet/wiki/targets/klad-design/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Multidisciplinary Design Syndicate – KLAD** (`https://klad.design/`). Klad Syndicate is a multidisciplinary design studio offering comprehensive solutions for ambitious brands. Every design we deliver is ori...
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#010101` / `#0000`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#010101` (`var(--color-black)` in `:root`) paired with `#fff` primary typography and `#0000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Helvetica Now Display` for display copy (`Klad Syndicate Klad Syndicate Klad S`) with `Segoe UI` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: var(--spacing)`, padding `80px`) with `cubic-bezier(.4,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/klad-design/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×6793px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `40rem` extracted from `klad-design` stylesheet.
- **Canvas Lateral Padding & Spacing**: `80px` lateral canvas padding with `var(--spacing)` grid gap.
- **Border Radius Scale**: `0px` (sharp unrounded corners).

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--spacing)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `80px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:768px)`, `@media (min-width:48rem)`, `@media (min-width:96rem)`, `@media (min-width:64rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#010101` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#e6e6e6` | `var(--color-gray)` in `:root` |
| **Interactive Accent / Highlight** | `#0000` | `textarea { background-color: #0000 }` |
| **Secondary / Muted Copy** | `#000000` | `video { background-color: black }` (`#000000`) |
| **Structural Hairline Border** | `#808080` | `.case-close { color: gray }` (`#808080`) |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-black` | `#010101` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--font-weight-normal` | `400` | Typography / Scale Token |
| `--tracking-normal` | `0em` | Typography / Scale Token |
| `--blur-xs` | `4px` | Elevation / Border Token |
| `--default-transition-duration` | `.15s` | Motion / Easing Token |
| `--default-transition-timing-function` | `cubic-bezier(.4, 0, .2, 1)` | Motion / Easing Token |
| `--default-font-family` | `var(--font-sans)` | Typography / Scale Token |
| `--default-mono-font-family` | `var(--font-mono)` | Typography / Scale Token |
| `--color-gray` | `#e6e6e6` | Brand / Palette Token |
| `--font-helvetica` | `"Helvetica Now Display"` | Typography / Scale Token |
| `--text-normal` | `inherit` | Typography Ink Token |
| `--text-h1` | `74px` | Typography Ink Token |
| `--text-h1--line-height` | `114%` | Typography Ink Token |
| `--text-h1--letter-spacing` | `-.74px` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Helvetica Now Display`.
- **Primary Body Stack**: `Segoe UI`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--text-h1: 74px`, `--text-h1--line-height: 114%`, `--text-h1--letter-spacing: -.74px`.
- **Section Heading (`H2`)**: CSS variables `--text-h2-md: 64px`, `--text-h2-md--line-height: 114%`, `--text-h2-md--letter-spacing: -.64px`; rule `h2` (`font-size: var(--text-p1)`, `line-height: var(--tw-leading,var(...`, `letter-spacing: var(--tw-tracking,var...`).
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--text-h1)`, `var(--text-h1-md)`).
- **Metadata & Navigation Labels**: CSS variables `--default-mono-font-family: var(--font-mono)`, `--text-h1--letter-spacing: -.74px`, `--text-h1-md--letter-spacing: -1.52px`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.16,1,.3,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `klad-design` stylesheet.
- **Selector `button`**: `transition: opacity .15s linear` extracted from `klad-design` stylesheet.
- **Selector `.button:after`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `klad-design` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.site-header>` and `<section.duration-200>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Multidisciplinary Design Syndicate – KLAD  │
│ ====================================================================== │
│ [ <header.site-header>     | About · Work · Process · Expectations  ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.transition-colors>                          |   │
│ | H1: Klad Syndicate Klad Syndicate Klad Syndicate Klad...         |   │
│ | Substrate: #010101    | Ink: #fff       | Accent: #0000          |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.duration-200>    ) max-w: 40rem          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Team 专责小组 Team 专责小组 Team 专责小 |  | Ksusha Ksusha Ksusha Ksusha  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<header.site-heade] -> [<section.transitio] -> [<section.duration-] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.absolute>     ) | https://klad.design/               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.site-header> — `klad-design`)**:
   - Landmark `<header class="site-header fixed">` hosting `Multidisciplinary Design Syndicate –` navigation (`About · Work · Process · Expectations · Pricing`), DOM attributes (`data-theme="light"`, `data-precedence="next"`, `data-page-noise="true"`, `data-active`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.transition-colors> — `Klad Syndicate Klad Syndicate Klad`)**:
   - Landmark `<section class="transition-colors">` presenting display lead `Klad Syndicate Klad Syndicate Klad Syndicate Klad...` and copy excerpt *"All Rights Reserved."* over `#010101` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.duration-200> — `Team 专责小组 Team 专责小组 Team 专责小组 Team`)**:
   - Landmark `<section class="duration-200">` rendering section `Team 专责小组 Team 专责小组 Team 专责小组 Team 专责小组 Team 专责小组...` with copy *"We are a multidisciplinary design syndicate offering comprehensiv"*, asset references (`logo-still.31i0fmdt_igcj.svg`, `world.39sfmav5iqip_.svg`, `1myj9p5-zqliw.css`, `0yigbjg0ha9p3.js`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.pt-20> — `Ksusha Ksusha Ksusha Ksusha Ksusha`)**:
   - Landmark `<section class="pt-20 z-1">` framing `Ksusha Ksusha Ksusha Ksusha Ksusha Ksusha` and `Lena S. Lena S. Lena S. Lena S. Lena S. Lena S.` (*"We actively avoid repeating ourselves. Our process may seem chaot"*) with `#e6e6e6` surface cards, `#0000` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.absolute> — `https://klad.design/`)**:
   - Landmark `<footer class="absolute">` anchoring `Multidisciplinary Design Syndica` footer links (`About · Work · Process · Expectations · Pricing`), copy *"As a small team, we deliberately limit the number of project"*, and `#808080` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: klad-design (Multidisciplinary Design Syndicate – KLAD)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `klad-design` (**Multidisciplinary Design Syndicate – KLAD** — `https://klad.design/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#010101` / `#0000`).
- **Identity & Domain Context**: Klad Syndicate is a multidisciplinary design studio offering comprehensive solutions for ambitious brands. Every design we deliver is ori...
- **Primary Substrate**: `#010101` (`var(--color-black)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#0000`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#010101` (`var(--color-black)` in `:root`) paired with `#fff` primary typography and `#0000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Helvetica Now Display` for display copy (`Klad Syndicate Klad Syndicate Klad S`) with `Segoe UI` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: var(--spacing)`, padding `80px`) with `cubic-bezier(.4,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `klad-design` in your global stylesheet:

:root {
  /* Multidisciplinary Design Syndicate – KLAD (klad-design) — Ground-Truth Extracted CSS Variables */
  --color-black: #010101; /* Canvas / Surface Token (klad-design) */
  --color-white: #fff; /* Canvas / Surface Token (klad-design) */
  --spacing: .25rem; /* Layout / Spatial Grid Token (klad-design) */
  --font-weight-normal: 400; /* Typography / Scale Token (klad-design) */
  --tracking-normal: 0em; /* Typography / Scale Token (klad-design) */
  --blur-xs: 4px; /* Elevation / Border Token (klad-design) */
  --default-transition-duration: .15s; /* Motion / Easing Token (klad-design) */
  --default-transition-timing-function: cubic-bezier(.4, 0, .2, 1); /* Motion / Easing Token (klad-design) */
  --default-font-family: var(--font-sans); /* Typography / Scale Token (klad-design) */
  --default-mono-font-family: var(--font-mono); /* Typography / Scale Token (klad-design) */
  --color-gray: #e6e6e6; /* Brand / Palette Token (klad-design) */
  --font-helvetica: "Helvetica Now Display"; /* Typography / Scale Token (klad-design) */
  --text-normal: inherit; /* Typography Ink Token (klad-design) */
  --text-h1: 74px; /* Typography Ink Token (klad-design) */
  --text-h1--line-height: 114%; /* Typography Ink Token (klad-design) */
  --text-h1--letter-spacing: -.74px; /* Typography Ink Token (klad-design) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#010101` — grounded in `var(--color-black)` in `:root`
- **Primary Typography Ink**: `#fff` — grounded in `var(--color-white)` in `:root`
- **Elevated Surface / Card Substrate**: `#e6e6e6` — grounded in `var(--color-gray)` in `:root`
- **Interactive Accent / Highlight**: `#0000` — grounded in `textarea { background-color: #0000 }`
- **Secondary / Muted Copy**: `#000000` — grounded in `video { background-color: black }` (`#000000`)
- **Structural Hairline Border**: `#808080` — grounded in `.case-close { color: gray }` (`#808080`)

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×6793px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `40rem` extracted from `klad-design` stylesheet
- **Padding & Gutters**: `80px` lateral canvas padding with `var(--spacing)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--spacing)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `80px` horizontal padding
- **Media Queries**: `@media (min-width:768px)`, `@media (min-width:48rem)`, `@media (min-width:96rem)`, `@media (min-width:64rem)`
- **Corner Radii**: `0px` (sharp unrounded corners)

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Helvetica Now Display`
- **Body Font Stack**: `Segoe UI`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: CSS variables `--text-h1: 74px`, `--text-h1--line-height: 114%`, `--text-h1--letter-spacing: -.74px`
- **H2 Section Rule**: CSS variables `--text-h2-md: 64px`, `--text-h2-md--line-height: 114%`, `--text-h2-md--letter-spacing: -.64px`; rule `h2` (`font-size: var(--text-p1)`, `line-height: var(--tw-leading,var(...`, `letter-spacing: var(--tw-tracking,var...`)
- **Body Copy Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--text-h1)`, `var(--text-h1-md)`)
- **Metadata & Index Rule**: CSS variables `--default-mono-font-family: var(--font-mono)`, `--text-h1--letter-spacing: -.74px`, `--text-h1-md--letter-spacing: -1.52px`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `klad-design` (`Multidisciplinary Design Syndicate – KLAD`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.site-header> — `klad-design`)**:
   - DOM & Selectors: Landmark `<header class="site-header fixed">` hosting `Multidisciplinary Design Syndicate –` navigation (`About · Work · Process · Expectations · Pricing`), DOM attributes (`data-theme="light"`, `data-precedence="next"`, `data-page-noise="true"`, `data-active`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.site-header> — `klad-design`)` (`klad-design`) adapts across `@media (min-width:768px)`, `@media (min-width:48rem)`, `@media (min-width:96rem)`, `@media (min-width:64rem)` with `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.16,1,.3,1)` transitions and links `About · Work · Process · Expectations · Pricing`.
2. **Hero Stage & Focal Lead (<section.transition-colors> — `Klad Syndicate Klad Syndicate Klad`)**:
   - DOM & Selectors: Landmark `<section class="transition-colors">` presenting display lead `Klad Syndicate Klad Syndicate Klad Syndicate Klad...` and copy excerpt *"All Rights Reserved."* over `#010101` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×6793px` desktop / `390×2400px` mobile) sets `#010101` background with `#fff` headline `Klad Syndicate Klad Syndicate Klad Syndicate Klad...`.
3. **Primary Showcase & Content Grid (<section.duration-200> — `Team 专责小组 Team 专责小组 Team 专责小组 Team`)**:
   - DOM & Selectors: Landmark `<section class="duration-200">` rendering section `Team 专责小组 Team 专责小组 Team 专责小组 Team 专责小组 Team 专责小组...` with copy *"We are a multidisciplinary design syndicate offering comprehensiv"*, asset references (`logo-still.31i0fmdt_igcj.svg`, `world.39sfmav5iqip_.svg`, `1myj9p5-zqliw.css`, `0yigbjg0ha9p3.js`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.duration-200> — `Team 专责小组 Team 专责小组 Team 专责小组 Team`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--spacing)`) on desktop and Single-column vertical stack at `390px` viewport width with `80px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.pt-20> — `Ksusha Ksusha Ksusha Ksusha Ksusha`)**:
   - DOM & Selectors: Landmark `<section class="pt-20 z-1">` framing `Ksusha Ksusha Ksusha Ksusha Ksusha Ksusha` and `Lena S. Lena S. Lena S. Lena S. Lena S. Lena S.` (*"We actively avoid repeating ourselves. Our process may seem chaot"*) with `#e6e6e6` surface cards, `#0000` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.pt-20> — `Ksusha Ksusha Ksusha Ksusha Ksusha`)` uses `0px` (sharp unrounded corners) radii, `#0000` highlights, and assets (logo-still.31i0fmdt_igcj.svg, world.39sfmav5iqip_.svg, 1myj9p5-zqliw.css).
5. **Colophon & Global Directory Footer (<footer.absolute> — `https://klad.design/`)**:
   - DOM & Selectors: Landmark `<footer class="absolute">` anchoring `Multidisciplinary Design Syndica` footer links (`About · Work · Process · Expectations · Pricing`), copy *"As a small team, we deliberately limit the number of project"*, and `#808080` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.absolute> — `https://klad.design/`)` aligns to `40rem` extracted from `klad-design` stylesheet with `80px` lateral canvas padding with `var(--spacing)` grid gap and attributes (data-theme="light", data-precedence="next", data-page-noise="true").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"All Rights Reserved."*
- Copy Excerpt 2: *"We are a multidisciplinary design syndicate offering comprehensive solutions for a..."*
- Copy Excerpt 3: *"We actively avoid repeating ourselves. Our process may seem chaotic at times, but..."*
- Copy Excerpt 4: *"As a small team, we deliberately limit the number of projects we take on, dedicati..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.16,1,.3,1)`
- **Extracted Stylesheet Rules (`klad-design`)**:
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- `sup { vertical-align:baseline;font-size:75%;line-height:0;position:relative }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `klad-design` stylesheet.
- **Selector `button`**: `transition: opacity .15s linear` extracted from `klad-design` stylesheet.
- **Selector `.button:after`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `klad-design` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.site-header>` and `<section.duration-200>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `klad-design`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
