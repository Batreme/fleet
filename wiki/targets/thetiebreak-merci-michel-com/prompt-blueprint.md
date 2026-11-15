---
title: "UI Prompt Blueprint: thetiebreak-merci-michel-com"
date: 2026-11-15
target: "thetiebreak-merci-michel-com"
status: analyzed
capture: specimen
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#fff302`)"
---

# UI Design System & Master Generation Blueprint: thetiebreak-merci-michel-com

> **The Tie-break!** (https://thetiebreak.merci-michel.com/) — Play the game and discover the latest New Balance X Miu Miu collection with Coco Gauff.

![Desktop Design Specimen (Offline WebGL/JS Fallback — not live site capture)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **The Tie-break!** (`https://thetiebreak.merci-michel.com/`). Play the game and discover the latest New Balance X Miu Miu collection with Coco Gauff.
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#fff302`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--ui-color-bg-primary)` in `:root`) paired with `#fff` primary typography and `#fff302` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Instrument` for display copy (`The Tie-break!`) with `WorkSans` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1080px` container bounds (`gap: 0px (flush layout)`, padding `0px`) with `cubic-bezier(.19,1,.22,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Design Specimen (Offline WebGL/JS Fallback — not live site capture)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `1080px` extracted from `thetiebreak-merci-michel-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `0px` lateral canvas padding with `0px (flush layout)` grid gap.
- **Border Radius Scale**: `50%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1080px`, `gap: 0px (flush layout)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `0px` horizontal padding.
- **Extracted CSS Media Queries**: `@media only screen and (max-width:1080px)and (orientation:portrait)`, `@media (prefers-reduced-motion:reduce)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--ui-color-bg-primary)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--ui-color-primary)` in `:root` |
| **Elevated Surface / Card Substrate** | `#142a48` | `var(--ui-color-blue)` in `:root` |
| **Interactive Accent / Highlight** | `#fff302` | `var(--ui-color-primary-hover)` in `:root` |
| **Secondary / Muted Copy** | `#05152d` | `#preloader .preloader-background { background: #05152d }` |
| **Structural Hairline Border** | `#fffc` | `::-moz-selection { background: #fffc }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ball-size` | `max(35px, 1.8vw)` | Layout / Spatial Grid Token |
| `--bounce-height` | `90px` | Layout / Spatial Grid Token |
| `--floor-height` | `0px` | Layout / Spatial Grid Token |
| `--duration` | `.8s` | Motion / Easing Token |
| `--exit-duration` | `.3s` | Motion / Easing Token |
| `--base-text` | `10px` | Typography Ink Token |
| `--padding` | `max(6px, calc(var(--base-text) * .15))` | Layout / Spatial Grid Token |
| `--ui-colors` | `bg-primary:#000 / primary:#fff / blue:#142a48 / primary-hover:#fff302` | Brand / Palette Token |
| `--ui-color-bg-primary` | `#000` | Canvas / Surface Token |
| `--ui-color-primary` | `#fff` | Brand / Palette Token |
| `--ui-color-blue` | `#142a48` | Brand / Palette Token |
| `--ui-color-primary-hover` | `#fff302` | Brand / Palette Token |
| `--miumiu-header` | `1.5em` | Layout / Spatial Grid Token |
| `--scrollbar-width` | `0px` | Layout / Spatial Grid Token |
| `--inner-height` | `900px` | Layout / Spatial Grid Token |
| `--vp-height` | `900px` | Layout / Spatial Grid Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Instrument`.
- **Primary Body Stack**: `WorkSans`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1.4em`, `2.4em`, `15em`, `8.4em`, `1.6em`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1.4em`, `2.4em`, `15em`, `8.4em`, `1.6em`).
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1.4em`, `2.4em`, `15em`, `8.4em`, `1.6em`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1.4em`, `2.4em`, `15em`, `8.4em`, `1.6em`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.19,1,.22,1)`, `cubic-bezier(.25,.46,.45,.94)`, `cubic-bezier(.55,.085,.68,.53)`.

### Per-Element Transition & Choreography Rules
- **Selector `.button[data-v-7fa37a60]`**: `transition: .3s border-color cubic-bezier(.19,1,.22,1)` extracted from `thetiebreak-merci-michel-com` stylesheet.
- **Selector `.button__wrapper[data-v-7fa37a60]...`**: `transition: .3s transform cubic-bezier(.19,1,.22,1)` extracted from `thetiebreak-merci-michel-com` stylesheet.
- **Selector `e.enter-active .home__logo[data-v...`**: `transition: opacity 2s` extracted from `thetiebreak-merci-michel-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.19,1,.22,1)`)**: Governs interactive state transitions across `<header.desktop>` and `<main.ui>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — The Tie-break!                             │
│ ====================================================================== │
│ [ <header.desktop>         | Overview · Index · Archive · About · C ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <main.ui>                                            |   │
│ | H1: The Tie-break!                                               |   │
│ | Substrate: #000       | Ink: #fff       | Accent: #fff302        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<main.ui>                 ) max-w: 1080px         |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Featured Work & Interactive  |  | Technical Architecture & Nar | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 0px (f) | │
│ | [<header.desktop>] -> [<main.ui>] -> [<main.ui>] |                   │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.is-exiting>   ) | https://thetiebreak.merci-michel.c │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.desktop> — `thetiebreak-merci-michel-com`)**:
   - Landmark `<header class="desktop">` hosting `The Tie-break!` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-v-app`, `data-can-control`, `data-engine="three.js r184"`), and stylesheet rule `.webgl-canvas { outline:none }`.
2. **Hero Stage & Focal Lead (<main.ui> — `The Tie-break!`)**:
   - Landmark `<main class="ui">` presenting display lead `The Tie-break!` and copy excerpt *"Play the game and discover the latest New Balance X Miu Miu colle"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<main.ui> — `Featured Work & Interactive Showca`)**:
   - Landmark `<main class="ui">` rendering section `Featured Work & Interactive Showcase` with copy *"The Tie-break!"*, asset references (`utag.js`, `favicon.ico`, `favicon_dark.svg`, `favicon_light.svg`), and grid rule `hover { border-color:transparent }`.
4. **Interactive Detail & Feature Matrix (<main.ui> — `Technical Architecture & Narrative`)**:
   - Landmark `<main class="ui">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Work & Interactive Showcase"*) with `#142a48` surface cards, `#fff302` accents, and `before { transform:scale(1.1) }`.
5. **Colophon & Global Directory Footer (<footer.is-exiting> — `https://thetiebreak.merci-michel.com/`)**:
   - Landmark `<footer class="is-exiting">` anchoring `The Tie-break!` footer links (`Overview · Index · Archive · About · Contact`), copy *"Technical Architecture & Narrative"*, and `#fffc` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: thetiebreak-merci-michel-com (The Tie-break!)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `thetiebreak-merci-michel-com` (**The Tie-break!** — `https://thetiebreak.merci-michel.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#fff302`).
- **Identity & Domain Context**: Play the game and discover the latest New Balance X Miu Miu collection with Coco Gauff.
- **Primary Substrate**: `#000` (`var(--ui-color-bg-primary)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#fff302`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--ui-color-bg-primary)` in `:root`) paired with `#fff` primary typography and `#fff302` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Instrument` for display copy (`The Tie-break!`) with `WorkSans` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1080px` container bounds (`gap: 0px (flush layout)`, padding `0px`) with `cubic-bezier(.19,1,.22,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `thetiebreak-merci-michel-com` in your global stylesheet:

:root {
  /* The Tie-break! (thetiebreak-merci-michel-com) — Ground-Truth Extracted CSS Variables */
  --ball-size: max(35px, 1.8vw); /* Layout / Spatial Grid Token (thetiebreak-merci-michel-com) */
  --bounce-height: 90px; /* Layout / Spatial Grid Token (thetiebreak-merci-michel-com) */
  --floor-height: 0px; /* Layout / Spatial Grid Token (thetiebreak-merci-michel-com) */
  --duration: .8s; /* Motion / Easing Token (thetiebreak-merci-michel-com) */
  --exit-duration: .3s; /* Motion / Easing Token (thetiebreak-merci-michel-com) */
  --base-text: 10px; /* Typography Ink Token (thetiebreak-merci-michel-com) */
  --padding: max(6px, calc(var(--base-text) * .15)); /* Layout / Spatial Grid Token (thetiebreak-merci-michel-com) */
  --ui-colors: bg-primary:#000 / primary:#fff / blue:#142a48 / primary-hover:#fff302; /* Brand / Palette Token (thetiebreak-merci-michel-com) */
  --ui-color-bg-primary: #000; /* Canvas / Surface Token (thetiebreak-merci-michel-com) */
  --ui-color-primary: #fff; /* Brand / Palette Token (thetiebreak-merci-michel-com) */
  --ui-color-blue: #142a48; /* Brand / Palette Token (thetiebreak-merci-michel-com) */
  --ui-color-primary-hover: #fff302; /* Brand / Palette Token (thetiebreak-merci-michel-com) */
  --miumiu-header: 1.5em; /* Layout / Spatial Grid Token (thetiebreak-merci-michel-com) */
  --scrollbar-width: 0px; /* Layout / Spatial Grid Token (thetiebreak-merci-michel-com) */
  --inner-height: 900px; /* Layout / Spatial Grid Token (thetiebreak-merci-michel-com) */
  --vp-height: 900px; /* Layout / Spatial Grid Token (thetiebreak-merci-michel-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000` — grounded in `var(--ui-color-bg-primary)` in `:root`
- **Primary Typography Ink**: `#fff` — grounded in `var(--ui-color-primary)` in `:root`
- **Elevated Surface / Card Substrate**: `#142a48` — grounded in `var(--ui-color-blue)` in `:root`
- **Interactive Accent / Highlight**: `#fff302` — grounded in `var(--ui-color-primary-hover)` in `:root`
- **Secondary / Muted Copy**: `#05152d` — grounded in `#preloader .preloader-background { background: #05152d }`
- **Structural Hairline Border**: `#fffc` — grounded in `::-moz-selection { background: #fffc }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1080px` extracted from `thetiebreak-merci-michel-com` stylesheet
- **Padding & Gutters**: `0px` lateral canvas padding with `0px (flush layout)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1080px`, `gap: 0px (flush layout)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `0px` horizontal padding
- **Media Queries**: `@media only screen and (max-width:1080px)and (orientation:portrait)`, `@media (prefers-reduced-motion:reduce)`
- **Corner Radii**: `50%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Instrument`
- **Body Font Stack**: `WorkSans`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1.4em`, `2.4em`, `15em`, `8.4em`, `1.6em`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1.4em`, `2.4em`, `15em`, `8.4em`, `1.6em`)
- **Body Copy Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1.4em`, `2.4em`, `15em`, `8.4em`, `1.6em`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1.4em`, `2.4em`, `15em`, `8.4em`, `1.6em`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `thetiebreak-merci-michel-com` (`The Tie-break!`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.desktop> — `thetiebreak-merci-michel-com`)**:
   - DOM & Selectors: Landmark `<header class="desktop">` hosting `The Tie-break!` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-v-app`, `data-can-control`, `data-engine="three.js r184"`), and stylesheet rule `.webgl-canvas { outline:none }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.desktop> — `thetiebreak-merci-michel-com`)` (`thetiebreak-merci-michel-com`) adapts across `@media only screen and (max-width:1080px)and (orientation:portrait)`, `@media (prefers-reduced-motion:reduce)` with `cubic-bezier(.19,1,.22,1)`, `cubic-bezier(.25,.46,.45,.94)`, `cubic-bezier(.55,.085,.68,.53)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<main.ui> — `The Tie-break!`)**:
   - DOM & Selectors: Landmark `<main class="ui">` presenting display lead `The Tie-break!` and copy excerpt *"Play the game and discover the latest New Balance X Miu Miu colle"* over `#000` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#000` background with `#fff` headline `The Tie-break!`.
3. **Primary Showcase & Content Grid (<main.ui> — `Featured Work & Interactive Showca`)**:
   - DOM & Selectors: Landmark `<main class="ui">` rendering section `Featured Work & Interactive Showcase` with copy *"The Tie-break!"*, asset references (`utag.js`, `favicon.ico`, `favicon_dark.svg`, `favicon_light.svg`), and grid rule `hover { border-color:transparent }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<main.ui> — `Featured Work & Interactive Showca`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1080px`, `gap: 0px (flush layout)`) on desktop and Single-column vertical stack at `390px` viewport width with `0px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<main.ui> — `Technical Architecture & Narrative`)**:
   - DOM & Selectors: Landmark `<main class="ui">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Work & Interactive Showcase"*) with `#142a48` surface cards, `#fff302` accents, and `before { transform:scale(1.1) }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<main.ui> — `Technical Architecture & Narrative`)` uses `50%` radii, `#fff302` highlights, and assets (utag.js, favicon.ico, favicon_dark.svg).
5. **Colophon & Global Directory Footer (<footer.is-exiting> — `https://thetiebreak.merci-michel.com/`)**:
   - DOM & Selectors: Landmark `<footer class="is-exiting">` anchoring `The Tie-break!` footer links (`Overview · Index · Archive · About · Contact`), copy *"Technical Architecture & Narrative"*, and `#fffc` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.is-exiting> — `https://thetiebreak.merci-michel.com/`)` aligns to `1080px` extracted from `thetiebreak-merci-michel-com` stylesheet with `0px` lateral canvas padding with `0px (flush layout)` grid gap and attributes (data-v-app, data-can-control, data-engine="three.js r184").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Lead Copy: *"Play the game and discover the latest New Balance X Miu Miu collection with Coco Gauff."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.19,1,.22,1)`, `cubic-bezier(.25,.46,.45,.94)`, `cubic-bezier(.55,.085,.68,.53)`
- **Extracted Stylesheet Rules (`thetiebreak-merci-michel-com`)**:
- `.webgl-canvas { outline:none }`
- `hover { border-color:transparent }`
- `before { transform:scale(1.1) }`
- `img { width:1.35em }`
- `svg { width:1.35em;height:auto }`
- **Per-Selector Transition Rules**:
- **Selector `.button[data-v-7fa37a60]`**: `transition: .3s border-color cubic-bezier(.19,1,.22,1)` extracted from `thetiebreak-merci-michel-com` stylesheet.
- **Selector `.button__wrapper[data-v-7fa37a60]...`**: `transition: .3s transform cubic-bezier(.19,1,.22,1)` extracted from `thetiebreak-merci-michel-com` stylesheet.
- **Selector `e.enter-active .home__logo[data-v...`**: `transition: opacity 2s` extracted from `thetiebreak-merci-michel-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.19,1,.22,1)`)**: Governs interactive state transitions across `<header.desktop>` and `<main.ui>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `thetiebreak-merci-michel-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
