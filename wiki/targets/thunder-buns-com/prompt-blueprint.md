---
title: "UI Prompt Blueprint: thunder-buns-com"
date: 2026-11-15
target: "[[overview|thunder-buns-com]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#30363c`)"
---

# UI Design System & Master Generation Blueprint: thunder-buns-com

> **Thunderbuns · Smashburgers Delivered** (https://thunder-buns.com/) — The best smash burgers, 100% halal. Delivered across the Netherlands, Belgium and Germany. Order through your usual delivery app.

![Desktop Viewport Capture (1440x5983)](file:///root/projects/fleet/wiki/targets/thunder-buns-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Thunderbuns · Smashburgers Delivered** (`https://thunder-buns.com/`). The best smash burgers, 100% halal. Delivered across the Netherlands, Belgium and Germany. Order through your usual delivery app.
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#30363c`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`var(--cc-bg)` in `:root`) paired with `#000` primary typography and `#30363c` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Bowlby One` for display copy (`Burgers that hit like lightning.`) with `Anton` and `Haffer Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `24rem` container bounds (`gap: var(--grid-gap)`, padding `2px`) with `cubic-bezier(.625,.05,0,1)` easing and Lenis Smooth Scroll (`data-lenis`), Barba.js Page Transition Router.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/thunder-buns-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×5983px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `24rem` extracted from `thunder-buns-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `2px` lateral canvas padding with `var(--grid-gap)` grid gap.
- **Border Radius Scale**: `4px`, `12px`, `3px`, `50%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 24rem`, `gap: var(--grid-gap)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `2px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen`, `@media screen and (-ms-high-contrast:active)`, `@media screen and (-ms-high-contrast:black-on-white)`, `@media screen and (min-width:640px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--cc-bg)` in `:root` |
| **Primary Typography Ink** | `#2c2f31` | `var(--cc-primary-color)` in `:root` |
| **Elevated Surface / Card Substrate** | `#5e6266` | `var(--cc-secondary-color)` in `:root` |
| **Interactive Accent / Highlight** | `#30363c` | `var(--cc-btn-primary-bg)` in `:root` |
| **Secondary / Muted Copy** | `#000` | `var(--cc-btn-primary-hover-bg)` in `:root` |
| **Structural Hairline Border** | `#eaeff2` | `var(--cc-btn-secondary-bg)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--cc-modal-border-radius` | `.5rem` | Elevation / Border Token |
| `--cc-btn-border-radius` | `.4rem` | Elevation / Border Token |
| `--cc-modal-transition-duration` | `.25s` | Motion / Easing Token |
| `--cc-link-color` | `var(--cc-btn-primary-bg)` | Typography Ink Token |
| `--cc-modal-margin` | `1rem` | Layout / Spatial Grid Token |
| `--cc-z-index` | `2147483647` | Elevation / Border Token |
| `--cc-bg` | `#fff` | Canvas / Surface Token |
| `--cc-primary-color` | `#2c2f31` | Brand / Palette Token |
| `--cc-secondary-color` | `#5e6266` | Brand / Palette Token |
| `--cc-btn-primary-bg` | `#30363c` | Canvas / Surface Token |
| `--cc-btn-primary-color` | `#fff` | Brand / Palette Token |
| `--cc-btn-primary-border-color` | `var(--cc-btn-primary-bg)` | Brand / Palette Token |
| `--cc-btn-primary-hover-bg` | `#000` | Canvas / Surface Token |
| `--cc-btn-primary-hover-color` | `#fff` | Brand / Palette Token |
| `--cc-btn-primary-hover-border-color` | `var(--cc-btn-primary-hover-bg)` | Brand / Palette Token |
| `--cc-btn-secondary-bg` | `#eaeff2` | Canvas / Surface Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Bowlby One`.
- **Primary Body Stack**: `Anton`.
- **Technical / Metadata Stack**: `Haffer Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`font-size: min(14.5em,130px)`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 3.3em`, `line-height: .88`).
- **Body Copy**: rule `p` (`font-size: 1.4em`, `line-height: 1.2`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `10px`, `14px`, `16px`, `100%`, `1.05em`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.625,.05,0,1)`, `cubic-bezier(.33,1,.68,1)`, `cubic-bezier(.22,1,.36,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.mapboxgl-marker`**: `transition: opacity .2s` extracted from `thunder-buns-com` stylesheet.
- **Selector `.mapboxgl-touch-pan-blocker`**: `transition: opacity .75s ease-in-out` extracted from `thunder-buns-com` stylesheet.
- **Selector `.mapboxgl-touch-pan-blocker-show`**: `transition: opacity .1s ease-in-out` extracted from `thunder-buns-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.625,.05,0,1)`)**: Governs interactive state transitions across `<header.lenis>` and `<section.award>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Barba.js Page Transition Router, HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Thunderbuns · Smashburgers Delivered       │
│ ====================================================================== │
│ [ <header.lenis>           | English · Nederlands · Deutsch · Franç ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.award>                                      |   │
│ | H1: Burgers that hit like lightning.                             |   │
│ | Substrate: #fff       | Ink: #000       | Accent: #30363c        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.award>           ) max-w: 24rem          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Who are we? What do we do? W |  | Winner Thuisbezorgd.nl Award | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<header.lenis>] -> [<section.award>] -> [<section.award>] |         │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.shape>        ) | https://thunder-buns.com/          │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.lenis> — `thunder-buns-com`)**:
   - Landmark `<header class="lenis">` hosting `Thunderbuns · Smashburgers Delivered` navigation (`English · Nederlands · Deutsch · Français · Order`), DOM attributes (`data-ga-id="G-DKWN4TYM2V"`, `data-barba="wrapper"`, `data-scrolling-started="false"`, `data-scrolling-direction="up"`), and stylesheet rule `.mapboxgl-canvas { position:absolute;left:0;top:0 }`.
2. **Hero Stage & Focal Lead (<section.award> — `Burgers that hit like lightning.`)**:
   - Landmark `<section class="award">` presenting display lead `Burgers that hit like lightning.` and copy excerpt *"Order Thunderbuns Online - Order Thunderbuns Online - Order Thund"* over `#fff` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.award> — `Who are we? What do we do? Where a`)**:
   - Landmark `<section class="award">` rendering section `Who are we? What do we do? Where are we?` with copy *"Order Thunderbuns Online -"*, asset references (`tb-favicon2.png`, `BowlbyOne-Regular.woff2`, `Satoshi-Regular.woff2`, `image.mux.com`), and grid rule `.mapboxgl-map:-webkit-full-screen { width:100%;height:100% }`.
4. **Interactive Detail & Feature Matrix (<section.award> — `Winner Thuisbezorgd.nl Award 2025 `)**:
   - Landmark `<section class="award">` framing `Winner Thuisbezorgd.nl Award 2025 “Best National...` and `Best National Chain` (*"We make smashburgers. Two patties, smashed onto a screaming hot p"*) with `#5e6266` surface cards, `#30363c` accents, and `.mapboxgl-canary { background-color:salmon }`.
5. **Colophon & Global Directory Footer (<footer.shape> — `https://thunder-buns.com/`)**:
   - Landmark `<footer class="shape">` anchoring `Thunderbuns · Smashburgers Deliv` footer links (`English · Nederlands · Deutsch · Français · Order`), copy *"You'll now find us in 130+ locations across the Netherlands,"*, and `#eaeff2` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: thunder-buns-com (Thunderbuns · Smashburgers Delivered)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `thunder-buns-com` (**Thunderbuns · Smashburgers Delivered** — `https://thunder-buns.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#30363c`).
- **Identity & Domain Context**: The best smash burgers, 100% halal. Delivered across the Netherlands, Belgium and Germany. Order through your usual delivery app.
- **Primary Substrate**: `#fff` (`var(--cc-bg)` in `:root`), **Primary Ink**: `#000`, **Accent / Highlight**: `#30363c`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`var(--cc-bg)` in `:root`) paired with `#000` primary typography and `#30363c` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Bowlby One` for display copy (`Burgers that hit like lightning.`) with `Anton` and `Haffer Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `24rem` container bounds (`gap: var(--grid-gap)`, padding `2px`) with `cubic-bezier(.625,.05,0,1)` easing and Lenis Smooth Scroll (`data-lenis`), Barba.js Page Transition Router.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `thunder-buns-com` in your global stylesheet:

:root {
  /* Thunderbuns · Smashburgers Delivered (thunder-buns-com) — Ground-Truth Extracted CSS Variables */
  --cc-modal-border-radius: .5rem; /* Elevation / Border Token (thunder-buns-com) */
  --cc-btn-border-radius: .4rem; /* Elevation / Border Token (thunder-buns-com) */
  --cc-modal-transition-duration: .25s; /* Motion / Easing Token (thunder-buns-com) */
  --cc-link-color: var(--cc-btn-primary-bg); /* Typography Ink Token (thunder-buns-com) */
  --cc-modal-margin: 1rem; /* Layout / Spatial Grid Token (thunder-buns-com) */
  --cc-z-index: 2147483647; /* Elevation / Border Token (thunder-buns-com) */
  --cc-bg: #fff; /* Canvas / Surface Token (thunder-buns-com) */
  --cc-primary-color: #2c2f31; /* Brand / Palette Token (thunder-buns-com) */
  --cc-secondary-color: #5e6266; /* Brand / Palette Token (thunder-buns-com) */
  --cc-btn-primary-bg: #30363c; /* Canvas / Surface Token (thunder-buns-com) */
  --cc-btn-primary-color: #fff; /* Brand / Palette Token (thunder-buns-com) */
  --cc-btn-primary-border-color: var(--cc-btn-primary-bg); /* Brand / Palette Token (thunder-buns-com) */
  --cc-btn-primary-hover-bg: #000; /* Canvas / Surface Token (thunder-buns-com) */
  --cc-btn-primary-hover-color: #fff; /* Brand / Palette Token (thunder-buns-com) */
  --cc-btn-primary-hover-border-color: var(--cc-btn-primary-hover-bg); /* Brand / Palette Token (thunder-buns-com) */
  --cc-btn-secondary-bg: #eaeff2; /* Canvas / Surface Token (thunder-buns-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fff` — grounded in `var(--cc-bg)` in `:root`
- **Primary Typography Ink**: `#2c2f31` — grounded in `var(--cc-primary-color)` in `:root`
- **Elevated Surface / Card Substrate**: `#5e6266` — grounded in `var(--cc-secondary-color)` in `:root`
- **Interactive Accent / Highlight**: `#30363c` — grounded in `var(--cc-btn-primary-bg)` in `:root`
- **Secondary / Muted Copy**: `#000` — grounded in `var(--cc-btn-primary-hover-bg)` in `:root`
- **Structural Hairline Border**: `#eaeff2` — grounded in `var(--cc-btn-secondary-bg)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×5983px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `24rem` extracted from `thunder-buns-com` stylesheet
- **Padding & Gutters**: `2px` lateral canvas padding with `var(--grid-gap)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 24rem`, `gap: var(--grid-gap)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `2px` horizontal padding
- **Media Queries**: `@media screen`, `@media screen and (-ms-high-contrast:active)`, `@media screen and (-ms-high-contrast:black-on-white)`, `@media screen and (min-width:640px)`
- **Corner Radii**: `4px`, `12px`, `3px`, `50%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Bowlby One`
- **Body Font Stack**: `Anton`
- **Monospace / Technical Font Stack**: `Haffer Mono`
- **H1 Display Rule**: rule `h1` (`font-size: min(14.5em,130px)`)
- **H2 Section Rule**: rule `h2` (`font-size: 3.3em`, `line-height: .88`)
- **Body Copy Rule**: rule `p` (`font-size: 1.4em`, `line-height: 1.2`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `10px`, `14px`, `16px`, `100%`, `1.05em`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `thunder-buns-com` (`Thunderbuns · Smashburgers Delivered`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.lenis> — `thunder-buns-com`)**:
   - DOM & Selectors: Landmark `<header class="lenis">` hosting `Thunderbuns · Smashburgers Delivered` navigation (`English · Nederlands · Deutsch · Français · Order`), DOM attributes (`data-ga-id="G-DKWN4TYM2V"`, `data-barba="wrapper"`, `data-scrolling-started="false"`, `data-scrolling-direction="up"`), and stylesheet rule `.mapboxgl-canvas { position:absolute;left:0;top:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.lenis> — `thunder-buns-com`)` (`thunder-buns-com`) adapts across `@media screen`, `@media screen and (-ms-high-contrast:active)`, `@media screen and (-ms-high-contrast:black-on-white)`, `@media screen and (min-width:640px)` with `cubic-bezier(.625,.05,0,1)`, `cubic-bezier(.33,1,.68,1)`, `cubic-bezier(.22,1,.36,1)` transitions and links `English · Nederlands · Deutsch · Français · Order`.
2. **Hero Stage & Focal Lead (<section.award> — `Burgers that hit like lightning.`)**:
   - DOM & Selectors: Landmark `<section class="award">` presenting display lead `Burgers that hit like lightning.` and copy excerpt *"Order Thunderbuns Online - Order Thunderbuns Online - Order Thund"* over `#fff` canvas and `#000` ink.
   - Responsive Contract: Hero stage (`1440×5983px` desktop / `390×2400px` mobile) sets `#fff` background with `#000` headline `Burgers that hit like lightning.`.
3. **Primary Showcase & Content Grid (<section.award> — `Who are we? What do we do? Where a`)**:
   - DOM & Selectors: Landmark `<section class="award">` rendering section `Who are we? What do we do? Where are we?` with copy *"Order Thunderbuns Online -"*, asset references (`tb-favicon2.png`, `BowlbyOne-Regular.woff2`, `Satoshi-Regular.woff2`, `image.mux.com`), and grid rule `.mapboxgl-map:-webkit-full-screen { width:100%;height:100% }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.award> — `Who are we? What do we do? Where a`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 24rem`, `gap: var(--grid-gap)`) on desktop and Single-column vertical stack at `390px` viewport width with `2px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.award> — `Winner Thuisbezorgd.nl Award 2025 `)**:
   - DOM & Selectors: Landmark `<section class="award">` framing `Winner Thuisbezorgd.nl Award 2025 “Best National...` and `Best National Chain` (*"We make smashburgers. Two patties, smashed onto a screaming hot p"*) with `#5e6266` surface cards, `#30363c` accents, and `.mapboxgl-canary { background-color:salmon }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.award> — `Winner Thuisbezorgd.nl Award 2025 `)` uses `4px`, `12px`, `3px`, `50%` radii, `#30363c` highlights, and assets (tb-favicon2.png, BowlbyOne-Regular.woff2, Satoshi-Regular.woff2).
5. **Colophon & Global Directory Footer (<footer.shape> — `https://thunder-buns.com/`)**:
   - DOM & Selectors: Landmark `<footer class="shape">` anchoring `Thunderbuns · Smashburgers Deliv` footer links (`English · Nederlands · Deutsch · Français · Order`), copy *"You'll now find us in 130+ locations across the Netherlands,"*, and `#eaeff2` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.shape> — `https://thunder-buns.com/`)` aligns to `24rem` extracted from `thunder-buns-com` stylesheet with `2px` lateral canvas padding with `var(--grid-gap)` grid gap and attributes (data-ga-id="G-DKWN4TYM2V", data-barba="wrapper", data-scrolling-started="false").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Order Thunderbuns Online - Order Thunderbuns Online - Order Thunderbuns Online - O..."*
- Copy Excerpt 2: *"Order Thunderbuns Online -"*
- Copy Excerpt 3: *"We make smashburgers. Two patties, smashed onto a screaming hot plate until the ed..."*
- Copy Excerpt 4: *"You'll now find us in 130+ locations across the Netherlands, Belgium and Germany,..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.625,.05,0,1)`, `cubic-bezier(.33,1,.68,1)`, `cubic-bezier(.22,1,.36,1)`
- **Extracted Stylesheet Rules (`thunder-buns-com`)**:
- `.mapboxgl-canvas { position:absolute;left:0;top:0 }`
- `.mapboxgl-map:-webkit-full-screen { width:100%;height:100% }`
- `.mapboxgl-canary { background-color:salmon }`
- `ctrl-group button.mapboxgl-ctrl-c... { cursor:grab;-webkit-user-select:none;user-select:none }`
- `oxgl-interactive.mapboxgl-track-p... { cursor:pointer }`
- **Per-Selector Transition Rules**:
- **Selector `.mapboxgl-marker`**: `transition: opacity .2s` extracted from `thunder-buns-com` stylesheet.
- **Selector `.mapboxgl-touch-pan-blocker`**: `transition: opacity .75s ease-in-out` extracted from `thunder-buns-com` stylesheet.
- **Selector `.mapboxgl-touch-pan-blocker-show`**: `transition: opacity .1s ease-in-out` extracted from `thunder-buns-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.625,.05,0,1)`)**: Governs interactive state transitions across `<header.lenis>` and `<section.award>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Barba.js Page Transition Router, HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `thunder-buns-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
