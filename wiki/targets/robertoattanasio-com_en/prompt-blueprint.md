---
title: "UI Prompt Blueprint: robertoattanasio-com_en"
date: 2026-11-15
target: "[[overview|robertoattanasio-com_en]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#222`)"
---

# UI Design System & Master Generation Blueprint: robertoattanasio-com_en

> **Roberto Attanasio** (https://robertoattanasio.com/en) — I write code by day and words by night. Projects, music and poems, all hidden in my digital world: drag the field and find them.

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/robertoattanasio-com_en/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Roberto Attanasio** (`https://robertoattanasio.com/en`). I write code by day and words by night. Projects, music and poems, all hidden in my digital world: drag the field and find them.
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#222`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`var(--margo-color-neutral)` in `:root`) paired with `#000` primary typography and `#222` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Mononoki` for display copy (`Roberto Attanasio`) with `Segoe UI` and `Mononoki`.
  - **Calibrated Spatial Grid & Motion**: Combines `80rem` container bounds (`gap: var(--margo-button-gap)`, padding `1rem`) with `cubic-bezier(0,0,.2,1)` easing and HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/robertoattanasio-com_en/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `80rem` extracted from `robertoattanasio-com_en` stylesheet.
- **Canvas Lateral Padding & Spacing**: `1rem` lateral canvas padding with `var(--margo-button-gap)` grid gap.
- **Border Radius Scale**: `var(--margo-radius)`, `var(--margo-radius-sm)`, `var(--margo-radius-xs)`, `9999px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 80rem`, `gap: var(--margo-button-gap)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `1rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:reduce)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--margo-color-neutral)` in `:root` |
| **Primary Typography Ink** | `#000` | `var(--margo-color-on-neutral)` in `:root` |
| **Elevated Surface / Card Substrate** | `#eceaea` | `var(--margo-color-main)` in `:root` |
| **Interactive Accent / Highlight** | `#222` | `var(--margo-color-on-main)` in `:root` |
| **Secondary / Muted Copy** | `#9c0ea3` | `var(--margo-color-primary)` in `:root` |
| **Structural Hairline Border** | `#7d0b82` | `var(--margo-color-primary-darken)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-md` | `28rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |
| `--text-sm` | `.875rem` | Typography Ink Token |
| `--text-base` | `1rem` | Typography Ink Token |
| `--text-xl` | `1.75rem` | Typography Ink Token |
| `--font-weight-medium` | `500` | Typography / Scale Token |
| `--tracking-widest` | `.1em` | Typography / Scale Token |
| `--leading-relaxed` | `1.625` | Typography / Scale Token |
| `--ease-out` | `cubic-bezier(0, 0, .2, 1)` | Motion / Easing Token |
| `--blur-sm` | `8px` | Elevation / Border Token |
| `--default-transition-duration` | `.15s` | Motion / Easing Token |
| `--default-transition-timing-function` | `cubic-bezier(.4, 0, .2, 1)` | Motion / Easing Token |
| `--default-font-family` | `var(--font-sans)` | Typography / Scale Token |
| `--default-mono-font-family` | `var(--font-mono)` | Typography / Scale Token |
| `--font-primary` | `var(--margo-font-family-primary)` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Mononoki`.
- **Primary Body Stack**: `Segoe UI`.
- **Technical / Metadata Stack**: `Mononoki`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `.875rem`, `.75rem`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `.875rem`, `.75rem`).
- **Body Copy**: CSS variables `--text-base: 1rem`; rule `,body` (`line-height: 1.5`).
- **Metadata & Navigation Labels**: CSS variables `--text-xs: .75rem`, `--text-sm: .875rem`, `--default-mono-font-family: var(--font-mono)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.4,0,1,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `robertoattanasio-com_en` stylesheet.
- **Selector `:where(.margo-button)`**: `transition: .16s` extracted from `robertoattanasio-com_en` stylesheet.
- **Selector `:where(.margo-button-icon-label)`**: `transition: .18s` extracted from `robertoattanasio-com_en` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.fixed>` and `<article.flex>`.
- **Runtime Interaction Engine**: Integrates HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Roberto Attanasio                          │
│ ====================================================================== │
│ [ <header.fixed>           | Overview · Index · Archive · About · C ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.sr-only>                                    |   │
│ | H1: Roberto Attanasio                                            |   │
│ | Substrate: #fff       | Ink: #000       | Accent: #222           |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<article.flex>            ) max-w: 80rem          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Hi, I'm a Frontend Web Devel |  | I write code by day and word | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<header.fixed>] -> [<section.sr-only>] -> [<article.flex>] |        │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.flex>         ) | https://robertoattanasio.com/en    │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.fixed> — `robertoattanasio-com_en`)**:
   - Landmark `<header class="fixed top-6">` hosting `Roberto Attanasio` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="default"`, `data-root="true"`, `data-cursor="idle"`, `data-scrim-anchor="true"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.sr-only> — `Roberto Attanasio`)**:
   - Landmark `<section class="sr-only">` presenting display lead `Roberto Attanasio` and copy excerpt *"Hi, I'm a Frontend Web Developer with five years of experience."* over `#fff` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<article.flex> — `Hi, I'm a Frontend Web Developer w`)**:
   - Landmark `<article class="flex flex-col">` rendering section `Hi, I'm a Frontend Web Developer with five years` with copy *"I write code by day and words by night. In between there's the pi"*, asset references (`index-D4Xf2DBZ.css`, `index-D8wnR5rE.js`, `route-C0O9SbwD.js`, `use-cursor-hint-Yyqb97NY.js`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<article.flex> — `I write code by day and words by n`)**:
   - Landmark `<article class="flex flex-col">` framing `I write code by day and words by night. In betwe` and `r.attanasio90@gmail.com r.attanasio90@gmail.com ` (*"r.attanasio90@gmail.com r.attanasio90@gmail.com *86V6+--·2V-7:X8R"*) with `#eceaea` surface cards, `#222` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.flex> — `https://robertoattanasio.com/en`)**:
   - Landmark `<footer class="flex">` anchoring `Roberto Attanasio` footer links (`Overview · Index · Archive · About · Contact`), copy *"r.attanasio90@gmail.com"*, and `#7d0b82` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: robertoattanasio-com_en (Roberto Attanasio)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `robertoattanasio-com_en` (**Roberto Attanasio** — `https://robertoattanasio.com/en`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#222`).
- **Identity & Domain Context**: I write code by day and words by night. Projects, music and poems, all hidden in my digital world: drag the field and find them.
- **Primary Substrate**: `#fff` (`var(--margo-color-neutral)` in `:root`), **Primary Ink**: `#000`, **Accent / Highlight**: `#222`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`var(--margo-color-neutral)` in `:root`) paired with `#000` primary typography and `#222` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Mononoki` for display copy (`Roberto Attanasio`) with `Segoe UI` and `Mononoki`.
  - **Calibrated Spatial Grid & Motion**: Combines `80rem` container bounds (`gap: var(--margo-button-gap)`, padding `1rem`) with `cubic-bezier(0,0,.2,1)` easing and HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `robertoattanasio-com_en` in your global stylesheet:

:root {
  /* Roberto Attanasio (robertoattanasio-com_en) — Ground-Truth Extracted CSS Variables */
  --spacing: .25rem; /* Layout / Spatial Grid Token (robertoattanasio-com_en) */
  --container-md: 28rem; /* Layout / Spatial Grid Token (robertoattanasio-com_en) */
  --text-xs: .75rem; /* Typography Ink Token (robertoattanasio-com_en) */
  --text-sm: .875rem; /* Typography Ink Token (robertoattanasio-com_en) */
  --text-base: 1rem; /* Typography Ink Token (robertoattanasio-com_en) */
  --text-xl: 1.75rem; /* Typography Ink Token (robertoattanasio-com_en) */
  --font-weight-medium: 500; /* Typography / Scale Token (robertoattanasio-com_en) */
  --tracking-widest: .1em; /* Typography / Scale Token (robertoattanasio-com_en) */
  --leading-relaxed: 1.625; /* Typography / Scale Token (robertoattanasio-com_en) */
  --ease-out: cubic-bezier(0, 0, .2, 1); /* Motion / Easing Token (robertoattanasio-com_en) */
  --blur-sm: 8px; /* Elevation / Border Token (robertoattanasio-com_en) */
  --default-transition-duration: .15s; /* Motion / Easing Token (robertoattanasio-com_en) */
  --default-transition-timing-function: cubic-bezier(.4, 0, .2, 1); /* Motion / Easing Token (robertoattanasio-com_en) */
  --default-font-family: var(--font-sans); /* Typography / Scale Token (robertoattanasio-com_en) */
  --default-mono-font-family: var(--font-mono); /* Typography / Scale Token (robertoattanasio-com_en) */
  --font-primary: var(--margo-font-family-primary); /* Brand / Palette Token (robertoattanasio-com_en) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fff` — grounded in `var(--margo-color-neutral)` in `:root`
- **Primary Typography Ink**: `#000` — grounded in `var(--margo-color-on-neutral)` in `:root`
- **Elevated Surface / Card Substrate**: `#eceaea` — grounded in `var(--margo-color-main)` in `:root`
- **Interactive Accent / Highlight**: `#222` — grounded in `var(--margo-color-on-main)` in `:root`
- **Secondary / Muted Copy**: `#9c0ea3` — grounded in `var(--margo-color-primary)` in `:root`
- **Structural Hairline Border**: `#7d0b82` — grounded in `var(--margo-color-primary-darken)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `80rem` extracted from `robertoattanasio-com_en` stylesheet
- **Padding & Gutters**: `1rem` lateral canvas padding with `var(--margo-button-gap)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 80rem`, `gap: var(--margo-button-gap)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `1rem` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:reduce)`
- **Corner Radii**: `var(--margo-radius)`, `var(--margo-radius-sm)`, `var(--margo-radius-xs)`, `9999px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Mononoki`
- **Body Font Stack**: `Segoe UI`
- **Monospace / Technical Font Stack**: `Mononoki`
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `.875rem`, `.75rem`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `.875rem`, `.75rem`)
- **Body Copy Rule**: CSS variables `--text-base: 1rem`; rule `,body` (`line-height: 1.5`)
- **Metadata & Index Rule**: CSS variables `--text-xs: .75rem`, `--text-sm: .875rem`, `--default-mono-font-family: var(--font-mono)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `robertoattanasio-com_en` (`Roberto Attanasio`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.fixed> — `robertoattanasio-com_en`)**:
   - DOM & Selectors: Landmark `<header class="fixed top-6">` hosting `Roberto Attanasio` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="default"`, `data-root="true"`, `data-cursor="idle"`, `data-scrim-anchor="true"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.fixed> — `robertoattanasio-com_en`)` (`robertoattanasio-com_en`) adapts across `@media (prefers-reduced-motion:reduce)` with `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.4,0,1,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<section.sr-only> — `Roberto Attanasio`)**:
   - DOM & Selectors: Landmark `<section class="sr-only">` presenting display lead `Roberto Attanasio` and copy excerpt *"Hi, I'm a Frontend Web Developer with five years of experience."* over `#fff` canvas and `#000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#fff` background with `#000` headline `Roberto Attanasio`.
3. **Primary Showcase & Content Grid (<article.flex> — `Hi, I'm a Frontend Web Developer w`)**:
   - DOM & Selectors: Landmark `<article class="flex flex-col">` rendering section `Hi, I'm a Frontend Web Developer with five years` with copy *"I write code by day and words by night. In between there's the pi"*, asset references (`index-D4Xf2DBZ.css`, `index-D8wnR5rE.js`, `route-C0O9SbwD.js`, `use-cursor-hint-Yyqb97NY.js`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<article.flex> — `Hi, I'm a Frontend Web Developer w`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 80rem`, `gap: var(--margo-button-gap)`) on desktop and Single-column vertical stack at `390px` viewport width with `1rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.flex> — `I write code by day and words by n`)**:
   - DOM & Selectors: Landmark `<article class="flex flex-col">` framing `I write code by day and words by night. In betwe` and `r.attanasio90@gmail.com r.attanasio90@gmail.com ` (*"r.attanasio90@gmail.com r.attanasio90@gmail.com *86V6+--·2V-7:X8R"*) with `#eceaea` surface cards, `#222` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.flex> — `I write code by day and words by n`)` uses `var(--margo-radius)`, `var(--margo-radius-sm)`, `var(--margo-radius-xs)`, `9999px` radii, `#222` highlights, and assets (index-D4Xf2DBZ.css, index-D8wnR5rE.js, route-C0O9SbwD.js).
5. **Colophon & Global Directory Footer (<footer.flex> — `https://robertoattanasio.com/en`)**:
   - DOM & Selectors: Landmark `<footer class="flex">` anchoring `Roberto Attanasio` footer links (`Overview · Index · Archive · About · Contact`), copy *"r.attanasio90@gmail.com"*, and `#7d0b82` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.flex> — `https://robertoattanasio.com/en`)` aligns to `80rem` extracted from `robertoattanasio-com_en` stylesheet with `1rem` lateral canvas padding with `var(--margo-button-gap)` grid gap and attributes (data-precedence="default", data-root="true", data-cursor="idle").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Hi, I'm a Frontend Web Developer with five years of experience."*
- Copy Excerpt 2: *"I write code by day and words by night. In between there's the piano, design and p..."*
- Copy Excerpt 3: *"r.attanasio90@gmail.com r.attanasio90@gmail.com *86V6+--·2V-7:X8R·<--ZE"*
- Copy Excerpt 4: *"r.attanasio90@gmail.com"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.4,0,1,1)`
- **Extracted Stylesheet Rules (`robertoattanasio-com_en`)**:
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- `sup { vertical-align:baseline;font-size:75%;line-height:0;position:relative }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `robertoattanasio-com_en` stylesheet.
- **Selector `:where(.margo-button)`**: `transition: .16s` extracted from `robertoattanasio-com_en` stylesheet.
- **Selector `:where(.margo-button-icon-label)`**: `transition: .18s` extracted from `robertoattanasio-com_en` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.fixed>` and `<article.flex>`.
- **Runtime Interaction Engine**: Integrates HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `robertoattanasio-com_en`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
