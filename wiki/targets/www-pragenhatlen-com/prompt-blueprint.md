---
title: "UI Prompt Blueprint: www-pragenhatlen-com"
date: 2026-11-15
target: "[[overview|www-pragenhatlen-com]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#52667e` / `#000`)"
---

# UI Design System & Master Generation Blueprint: www-pragenhatlen-com

> **Prägen Hätlen · Swiss watchmaking for the crypto community.** (https://www.pragenhatlen.com/) — Trust, precision, resilience and uncompromising attention to detail.

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Prägen Hätlen · Swiss watchmaking for the crypto community.** (`https://www.pragenhatlen.com/`). Trust, precision, resilience and uncompromising attention to detail.
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#52667e` / `#000`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#52667e` (`var(--watch-color-mid)` in `:root`) paired with `#fff` primary typography and `#000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Manrope` for display copy (`Trust, precision, resilience and unc`) with `RedHatMono` and `RedHatMono`.
  - **Calibrated Spatial Grid & Motion**: Combines `28vw` container bounds (`gap: 20rem`, padding `16rem`) with `cubic-bezier(.215,.61,.355,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `28vw` extracted from `www-pragenhatlen-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `16rem` lateral canvas padding with `20rem` grid gap.
- **Border Radius Scale**: `var(--border-radius)`, `100%`, `1rem`, `4px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 28vw`, `gap: 20rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `16rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width: 768px) and (min-height: 500px) and (orientati...`, `@media (max-width: 768px)`, `@media (max-width: 768px) and (min-width: 768px) and (min-height...`, `@media (min-width: 768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#52667e` | `var(--watch-color-mid)` in `:root` |
| **Primary Typography Ink** | `#0c1114` | `var(--watch-color-dark)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff` | `var(--color-white)` in `:root` |
| **Interactive Accent / Highlight** | `#000` | `var(--color-black)` in `:root` |
| **Secondary / Muted Copy** | `#ecebea` | `var(--color-light)` in `:root` |
| **Structural Hairline Border** | `#bdc4d4` | `var(--color-blue-sky)` in `:root` |
| **Variable Token (`--color-white--40`)** | `#ffffff66` | `var(--color-white--40)` in `:root` |
| **Variable Token (`--color-white--16`)** | `#ffffff29` | `var(--color-white--16)` in `:root` |
| **Variable Token (`--color-white--4`)** | `#ffffff0a` | `var(--color-white--4)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--base-background-color` | `var(--color-blue-sky)` | Canvas / Surface Token |
| `--base-text-color` | `var(--color-onyx-blue)` | Typography Ink Token |
| `--watch-color-mid` | `#52667e` | Brand / Palette Token |
| `--watch-color-dark` | `#0c1114` | Canvas / Surface Token |
| `--breakpoint-mobile` | `320px` | Dimension / Scale Token |
| `--breakpoint-mobile-horizontal` | `500px` | Dimension / Scale Token |
| `--breakpoint-tablet` | `768px` | Dimension / Scale Token |
| `--breakpoint-tablet-height` | `950px` | Layout / Spatial Grid Token |
| `--breakpoint-laptop` | `1024px` | Dimension / Scale Token |
| `--breakpoint-bigLaptop-min` | `1366px` | Dimension / Scale Token |
| `--breakpoint-bigLaptop` | `1440px` | Dimension / Scale Token |
| `--breakpoint-desktop` | `1680px` | Dimension / Scale Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--color-white--40` | `#ffffff66` | Canvas / Surface Token |
| `--color-white--16` | `#ffffff29` | Canvas / Surface Token |
| `--color-white--4` | `#ffffff0a` | Canvas / Surface Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Manrope`.
- **Primary Body Stack**: `RedHatMono`.
- **Technical / Metadata Stack**: `RedHatMono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `11rem`, `12rem`, `20rem`, `24rem`, `32rem`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `11rem`, `12rem`, `20rem`, `24rem`, `32rem`).
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `11rem`, `12rem`, `20rem`, `24rem`, `32rem`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `11rem`, `12rem`, `20rem`, `24rem`, `32rem`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.215,.61,.355,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.Header-module__top__mJsjm`**: `transition: .5s ease color` extracted from `www-pragenhatlen-com` stylesheet.
- **Selector `.Header-module__top_open__BgPji`**: `transition: unset` extracted from `www-pragenhatlen-com` stylesheet.
- **Selector `media (hover: hover)`**: `transition: .25s cubic-bezier(.215,.61,.355,1) opacity` extracted from `www-pragenhatlen-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.215,.61,.355,1)`)**: Governs interactive state transitions across `<header.Header-module__top__mJsjm>` and `<section.BlockEdito-module__root__-Hj6g>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Prägen Hätlen · Swiss watchmaking for the  │
│ ====================================================================== │
│ [ <header.Header-module__t | [02] A b o u t · [04] F A Q            ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.BlockEdito-module__root__-Hj6g>             |   │
│ | H1: Trust, precision, resilience and uncompromising a...         |   │
│ | Substrate: #52667e    | Ink: #fff       | Accent: #000           |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.BlockEdito-module) max-w: 28vw           |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | These principles guide every |  | The founder                  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 20rem ) | │
│ | [<header.Header-mod] -> [<section.BlockEdit] -> [<section.BlockEdit] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.Footer-module_) | https://www.pragenhatlen.com/      │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.Header-module__top__mJsjm> — `www-pragenhatlen-com`)**:
   - Landmark `<header class="Header-module__top__mJsjm">` hosting `Prägen Hätlen · Swiss watchmaking fo` navigation (`[02] A b o u t · [04] F A Q`), DOM attributes (`data-modal-id="cart"`, `data-lenis-prevent="true"`, `data-lenis-prevent="true"`, `data-lenis-prevent="true"`), and stylesheet rule `.App-module__root__JTuhI { background-color:var(--color-bg) }`.
2. **Hero Stage & Focal Lead (<section.BlockEdito-module__root__-Hj6g> — `Trust, precision, resilience and u`)**:
   - Landmark `<section class="BlockEdito-module__root__-Hj6g">` presenting display lead `Trust, precision, resilience and uncompromising a...` and copy excerpt *"label_rotate_phone*"* over `#52667e` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.BlockEdito-module__root__-Hj6g> — `These principles guide everything `)**:
   - Landmark `<section class="BlockEdito-module__root__-Hj6g">` rendering section `These principles guide everything we build.` with copy *"This website uses cookies to analyze traffic and improve your exp"*, asset references (`watch-background-drawing-D_cIL0zr...`, `cart-DdlU5Vpi.png`, `engrave_blue-Bx6rooYN.jpg`, `www.pragenhatlen.com`), and grid rule `.App-module__link__jsQ7Z { color:var(--color-black) }`.
4. **Interactive Detail & Feature Matrix (<section.BlockEdito-module__root__-Hj6g> — `The founder`)**:
   - Landmark `<section class="BlockEdito-module__root__-Hj6g">` framing `The founder` and `The Atelier` (*"[01] C o l l e c t i o n"*) with `#fff` surface cards, `#000` accents, and `.App-module__link__jsQ7Z:hover { color:var(--color-blue-cher-ami) }`.
5. **Colophon & Global Directory Footer (<footer.Footer-module__root__oib9b> — `https://www.pragenhatlen.com/`)**:
   - Landmark `<footer class="Footer-module__root__oib9b">` anchoring `Prägen Hätlen · Swiss watchmakin` footer links (`[02] A b o u t · [04] F A Q`), copy *"[03] P l a c e y o u r i n t e r e s t"*, and `#bdc4d4` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-pragenhatlen-com (Prägen Hätlen · Swiss watchmaking for the crypto community.)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-pragenhatlen-com` (**Prägen Hätlen · Swiss watchmaking for the crypto community.** — `https://www.pragenhatlen.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#52667e` / `#000`).
- **Identity & Domain Context**: Trust, precision, resilience and uncompromising attention to detail.
- **Primary Substrate**: `#52667e` (`var(--watch-color-mid)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#000`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#52667e` (`var(--watch-color-mid)` in `:root`) paired with `#fff` primary typography and `#000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Manrope` for display copy (`Trust, precision, resilience and unc`) with `RedHatMono` and `RedHatMono`.
  - **Calibrated Spatial Grid & Motion**: Combines `28vw` container bounds (`gap: 20rem`, padding `16rem`) with `cubic-bezier(.215,.61,.355,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-pragenhatlen-com` in your global stylesheet:

:root {
  /* Prägen Hätlen · Swiss watchmaking for the crypto community. (www-pragenhatlen-com) — Ground-Truth Extracted CSS Variables */
  --base-background-color: var(--color-blue-sky); /* Canvas / Surface Token (www-pragenhatlen-com) */
  --base-text-color: var(--color-onyx-blue); /* Typography Ink Token (www-pragenhatlen-com) */
  --watch-color-mid: #52667e; /* Brand / Palette Token (www-pragenhatlen-com) */
  --watch-color-dark: #0c1114; /* Canvas / Surface Token (www-pragenhatlen-com) */
  --breakpoint-mobile: 320px; /* Dimension / Scale Token (www-pragenhatlen-com) */
  --breakpoint-mobile-horizontal: 500px; /* Dimension / Scale Token (www-pragenhatlen-com) */
  --breakpoint-tablet: 768px; /* Dimension / Scale Token (www-pragenhatlen-com) */
  --breakpoint-tablet-height: 950px; /* Layout / Spatial Grid Token (www-pragenhatlen-com) */
  --breakpoint-laptop: 1024px; /* Dimension / Scale Token (www-pragenhatlen-com) */
  --breakpoint-bigLaptop-min: 1366px; /* Dimension / Scale Token (www-pragenhatlen-com) */
  --breakpoint-bigLaptop: 1440px; /* Dimension / Scale Token (www-pragenhatlen-com) */
  --breakpoint-desktop: 1680px; /* Dimension / Scale Token (www-pragenhatlen-com) */
  --color-white: #fff; /* Canvas / Surface Token (www-pragenhatlen-com) */
  --color-white--40: #ffffff66; /* Canvas / Surface Token (www-pragenhatlen-com) */
  --color-white--16: #ffffff29; /* Canvas / Surface Token (www-pragenhatlen-com) */
  --color-white--4: #ffffff0a; /* Canvas / Surface Token (www-pragenhatlen-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#52667e` — grounded in `var(--watch-color-mid)` in `:root`
- **Primary Typography Ink**: `#0c1114` — grounded in `var(--watch-color-dark)` in `:root`
- **Elevated Surface / Card Substrate**: `#fff` — grounded in `var(--color-white)` in `:root`
- **Interactive Accent / Highlight**: `#000` — grounded in `var(--color-black)` in `:root`
- **Secondary / Muted Copy**: `#ecebea` — grounded in `var(--color-light)` in `:root`
- **Structural Hairline Border**: `#bdc4d4` — grounded in `var(--color-blue-sky)` in `:root`
- **Variable Token (`--color-white--40`)**: `#ffffff66` — grounded in `var(--color-white--40)` in `:root`
- **Variable Token (`--color-white--16`)**: `#ffffff29` — grounded in `var(--color-white--16)` in `:root`
- **Variable Token (`--color-white--4`)**: `#ffffff0a` — grounded in `var(--color-white--4)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `28vw` extracted from `www-pragenhatlen-com` stylesheet
- **Padding & Gutters**: `16rem` lateral canvas padding with `20rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 28vw`, `gap: 20rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `16rem` horizontal padding
- **Media Queries**: `@media (min-width: 768px) and (min-height: 500px) and (orientati...`, `@media (max-width: 768px)`, `@media (max-width: 768px) and (min-width: 768px) and (min-height...`, `@media (min-width: 768px)`
- **Corner Radii**: `var(--border-radius)`, `100%`, `1rem`, `4px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Manrope`
- **Body Font Stack**: `RedHatMono`
- **Monospace / Technical Font Stack**: `RedHatMono`
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `11rem`, `12rem`, `20rem`, `24rem`, `32rem`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `11rem`, `12rem`, `20rem`, `24rem`, `32rem`)
- **Body Copy Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `11rem`, `12rem`, `20rem`, `24rem`, `32rem`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `11rem`, `12rem`, `20rem`, `24rem`, `32rem`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-pragenhatlen-com` (`Prägen Hätlen · Swiss watchmaking for the crypto community.`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.Header-module__top__mJsjm> — `www-pragenhatlen-com`)**:
   - DOM & Selectors: Landmark `<header class="Header-module__top__mJsjm">` hosting `Prägen Hätlen · Swiss watchmaking fo` navigation (`[02] A b o u t · [04] F A Q`), DOM attributes (`data-modal-id="cart"`, `data-lenis-prevent="true"`, `data-lenis-prevent="true"`, `data-lenis-prevent="true"`), and stylesheet rule `.App-module__root__JTuhI { background-color:var(--color-bg) }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.Header-module__top__mJsjm> — `www-pragenhatlen-com`)` (`www-pragenhatlen-com`) adapts across `@media (min-width: 768px) and (min-height: 500px) and (orientati...`, `@media (max-width: 768px)`, `@media (max-width: 768px) and (min-width: 768px) and (min-height...`, `@media (min-width: 768px)` with `cubic-bezier(.215,.61,.355,1)` transitions and links `[02] A b o u t · [04] F A Q`.
2. **Hero Stage & Focal Lead (<section.BlockEdito-module__root__-Hj6g> — `Trust, precision, resilience and u`)**:
   - DOM & Selectors: Landmark `<section class="BlockEdito-module__root__-Hj6g">` presenting display lead `Trust, precision, resilience and uncompromising a...` and copy excerpt *"label_rotate_phone*"* over `#52667e` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#52667e` background with `#fff` headline `Trust, precision, resilience and uncompromising a...`.
3. **Primary Showcase & Content Grid (<section.BlockEdito-module__root__-Hj6g> — `These principles guide everything `)**:
   - DOM & Selectors: Landmark `<section class="BlockEdito-module__root__-Hj6g">` rendering section `These principles guide everything we build.` with copy *"This website uses cookies to analyze traffic and improve your exp"*, asset references (`watch-background-drawing-D_cIL0zr...`, `cart-DdlU5Vpi.png`, `engrave_blue-Bx6rooYN.jpg`, `www.pragenhatlen.com`), and grid rule `.App-module__link__jsQ7Z { color:var(--color-black) }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.BlockEdito-module__root__-Hj6g> — `These principles guide everything `)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 28vw`, `gap: 20rem`) on desktop and Single-column vertical stack at `390px` viewport width with `16rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.BlockEdito-module__root__-Hj6g> — `The founder`)**:
   - DOM & Selectors: Landmark `<section class="BlockEdito-module__root__-Hj6g">` framing `The founder` and `The Atelier` (*"[01] C o l l e c t i o n"*) with `#fff` surface cards, `#000` accents, and `.App-module__link__jsQ7Z:hover { color:var(--color-blue-cher-ami) }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.BlockEdito-module__root__-Hj6g> — `The founder`)` uses `var(--border-radius)`, `100%`, `1rem`, `4px` radii, `#000` highlights, and assets (watch-background-drawing-D_cIL0zr..., cart-DdlU5Vpi.png, engrave_blue-Bx6rooYN.jpg).
5. **Colophon & Global Directory Footer (<footer.Footer-module__root__oib9b> — `https://www.pragenhatlen.com/`)**:
   - DOM & Selectors: Landmark `<footer class="Footer-module__root__oib9b">` anchoring `Prägen Hätlen · Swiss watchmakin` footer links (`[02] A b o u t · [04] F A Q`), copy *"[03] P l a c e y o u r i n t e r e s t"*, and `#bdc4d4` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.Footer-module__root__oib9b> — `https://www.pragenhatlen.com/`)` aligns to `28vw` extracted from `www-pragenhatlen-com` stylesheet with `16rem` lateral canvas padding with `20rem` grid gap and attributes (data-modal-id="cart", data-lenis-prevent="true", data-lenis-prevent="true").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"label_rotate_phone*"*
- Copy Excerpt 2: *"This website uses cookies to analyze traffic and improve your experience"*
- Copy Excerpt 3: *"[01] C o l l e c t i o n"*
- Copy Excerpt 4: *"[03] P l a c e y o u r i n t e r e s t"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.215,.61,.355,1)`
- **Extracted Stylesheet Rules (`www-pragenhatlen-com`)**:
- `.App-module__root__JTuhI { background-color:var(--color-bg) }`
- `.App-module__link__jsQ7Z { color:var(--color-black) }`
- `.App-module__link__jsQ7Z:hover { color:var(--color-blue-cher-ami) }`
- `.Loader-module__background__Nbt4d { position:absolute;top:50%;left:50%;-webkit-transform:translate(-50%,-50%... }`
- `.Loader-module__background__Nbt4d... { width:auto;height:72vh }`
- **Per-Selector Transition Rules**:
- **Selector `.Header-module__top__mJsjm`**: `transition: .5s ease color` extracted from `www-pragenhatlen-com` stylesheet.
- **Selector `.Header-module__top_open__BgPji`**: `transition: unset` extracted from `www-pragenhatlen-com` stylesheet.
- **Selector `media (hover: hover)`**: `transition: .25s cubic-bezier(.215,.61,.355,1) opacity` extracted from `www-pragenhatlen-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.215,.61,.355,1)`)**: Governs interactive state transitions across `<header.Header-module__top__mJsjm>` and `<section.BlockEdito-module__root__-Hj6g>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-pragenhatlen-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
