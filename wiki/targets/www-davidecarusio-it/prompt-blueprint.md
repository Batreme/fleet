---
title: "UI Prompt Blueprint: www-davidecarusio-it"
date: 2026-11-15
target: "[[overview|www-davidecarusio-it]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#f9efe7`)"
---

# UI Design System & Master Generation Blueprint: www-davidecarusio-it

> **Davide Carusio - Web Designer / Webflow Dev** (https://www.davidecarusio.it/) — Freelance web designer and Webflow expert in Italy. Fast, custom-built websites from design to development for agencies and international...

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/www-davidecarusio-it/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Davide Carusio - Web Designer / Webflow Dev** (`https://www.davidecarusio.it/`). Freelance web designer and Webflow expert in Italy. Fast, custom-built websites from design to development for agencies and international...
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#f9efe7`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`var(--button-043-color)` in `:root`) paired with `#000` primary typography and `#f9efe7` accents.
  - **Extracted Typographic Hierarchy**: Pairs `system-ui, -apple-system, sans-serif` (no custom `@font-face` extracted) for display copy (`Privacy Policy`) with `system-ui, -apple-system, sans-serif` (no custom `@font-face` extracted) and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `991px` container bounds (`gap: 0px (flush layout)`, padding `0px`) with `cubic-bezier(0.625,0.05,0,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/www-davidecarusio-it/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `991px` extracted from `www-davidecarusio-it` stylesheet.
- **Canvas Lateral Padding & Spacing**: `0px` lateral canvas padding with `0px (flush layout)` grid gap.
- **Border Radius Scale**: `var(--button-043-border-radius)`, `50%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 991px`, `gap: 0px (flush layout)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `0px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media screen and (orientation: landscape) and (max-height: 500px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--button-043-color)` in `:root` |
| **Primary Typography Ink** | `#000` | `var(--button-043-color-focus)` in `:root` |
| **Elevated Surface / Card Substrate** | `#1c1c1b` | `.underlay-nav__container { color: #1c1c1b }` |
| **Interactive Accent / Highlight** | `#f9efe7` | `.underlay-nav__container { color: #f9efe7 }` |
| **Secondary / Muted Copy** | `#000000` | `::selection { background-color: black }` (`#000000`) |
| **Structural Hairline Border** | `#f5ede4` | `.cursor-bubble { background-color: #f5ede4 }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--size-unit` | `16` | Layout / Spatial Grid Token |
| `--size-container-ideal` | `1440` | Layout / Spatial Grid Token |
| `--size-container-min` | `1280px` | Layout / Spatial Grid Token |
| `--size-container-max` | `1920px` | Layout / Spatial Grid Token |
| `--size-container` | `clamp(var(--size-container-min), 100vw, var(--size-container-max))` | Layout / Spatial Grid Token |
| `--button-043-color` | `#fff` | Brand / Palette Token |
| `--button-043-color-background` | `currentColor` | Canvas / Surface Token |
| `--button-043-hover-color-background` | `currentColor` | Canvas / Surface Token |
| `--button-043-icon-color` | `currentColor` | Brand / Palette Token |
| `--button-043-icon-color-background` | `transparent` | Canvas / Surface Token |
| `--button-043-color-focus` | `#000` | Brand / Palette Token |
| `--button-043-padding` | `0.3em 0.5em` | Layout / Spatial Grid Token |
| `--button-043-border-radius` | `0.125em` | Elevation / Border Token |
| `--button-043-icon-border-radius` | `0.125em` | Elevation / Border Token |
| `--button-043-text-duplicate-distance` | `1.5em` | Typography Ink Token |
| `--button-043-focus-inset` | `-0.125em` | Dimension / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `system-ui, -apple-system, sans-serif` (no custom `@font-face` extracted).
- **Primary Body Stack**: `system-ui, -apple-system, sans-serif` (no custom `@font-face` extracted).
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `var(--size-font)`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `var(--size-font)`).
- **Body Copy**: rule `body` (`font-size: var(--size-font)`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `var(--size-font)`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.625,0.05,0,1)`, `cubic-bezier(0.4,0,0.2,1)`, `cubic-bezier(0.32,0.72,0,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.lenis.lenis-autoToggle`**: `transition: 1ms` extracted from `www-davidecarusio-it` stylesheet.
- **Selector `.button-043__bg .button-043__text`**: `transition: color 0.4s ease, background-color 0.4s ease` extracted from `www-davidecarusio-it` stylesheet.
- **Selector `media (hover: hover) and (pointer...`**: `transition: transform 0.4s cubic-bezier(0.625,0.05,0,1), opacity 0.4s c...` extracted from `www-davidecarusio-it` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.625,0.05,0,1)`)**: Governs interactive state transitions across `<nav.underlay-nav__header>` and `<section.sticky-title-wrapper>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Davide Carusio - Web Designer / Webflow De │
│ ====================================================================== │
│ [ <nav.underlay-nav__heade | davide carusio · Projects · Services · ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero_wrap>                                  |   │
│ | H1: Privacy Policy                                               |   │
│ | Substrate: #fff       | Ink: #000       | Accent: #f9efe7        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.sticky-title-wrap) max-w: 991px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Data Controller              |  | Data Collected               | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 0px (f) | │
│ | [<nav.underlay-nav_] -> [<section.hero_wrap] -> [<section.sticky-ti] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer-wrap>  ) | https://www.davidecarusio.it/      │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.underlay-nav__header> — `www-davidecarusio-it`)**:
   - Landmark `<nav class="underlay-nav__header">` hosting `Davide Carusio - Web Designer / Webf` navigation (`davide carusio · Projects · Services · IT · G e t i n t o u c h`), DOM attributes (`data-wf-page="6aabacfa3017369152d1f8b2"`, `data-wf-site="6a3a84272e4493d30711d604"`, `data-theme-nav="light"`, `data-bg-nav="light"`), and stylesheet rule `focus { outline:none; }`.
2. **Hero Stage & Focal Lead (<section.hero_wrap> — `Privacy Policy`)**:
   - Landmark `<section class="hero_wrap">` presenting display lead `Privacy Policy` and copy excerpt *"t h e b e s t p i z z a i s t h e m a r g h e r i t a"* over `#fff` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.sticky-title-wrapper> — `Data Controller`)**:
   - Landmark `<section class="sticky-title-wrapper">` rendering section `Data Controller` with copy *"P r o j e c t s P r o j e c t s"*, asset references (`normalize.css`, `webflow.css`, `davidecarusio-it-v3.webflow.css`, `favicon.png`), and grid rule `html.lenis body { height: auto; }`.
4. **Interactive Detail & Feature Matrix (<section.work_wrap> — `Data Collected`)**:
   - Landmark `<section class="work_wrap">` framing `Data Collected` and `Purpose of Processing` (*"S e r v i c e s S e r v i c e s"*) with `#1c1c1b` surface cards, `#f9efe7` accents, and `.lenis-stopped { overflow: clip; }`.
5. **Colophon & Global Directory Footer (<footer.footer-wrap> — `https://www.davidecarusio.it/`)**:
   - Landmark `<footer class="footer-wrap">` anchoring `Davide Carusio - Web Designer / ` footer links (`davide carusio · Projects · Services · IT · G e t i n t o u c h`), copy *"G e t i n t o u c h"*, and `#f5ede4` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-davidecarusio-it (Davide Carusio - Web Designer / Webflow Dev)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-davidecarusio-it` (**Davide Carusio - Web Designer / Webflow Dev** — `https://www.davidecarusio.it/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#f9efe7`).
- **Identity & Domain Context**: Freelance web designer and Webflow expert in Italy. Fast, custom-built websites from design to development for agencies and international...
- **Primary Substrate**: `#fff` (`var(--button-043-color)` in `:root`), **Primary Ink**: `#000`, **Accent / Highlight**: `#f9efe7`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`var(--button-043-color)` in `:root`) paired with `#000` primary typography and `#f9efe7` accents.
  - **Extracted Typographic Hierarchy**: Pairs `system-ui, -apple-system, sans-serif` (no custom `@font-face` extracted) for display copy (`Privacy Policy`) with `system-ui, -apple-system, sans-serif` (no custom `@font-face` extracted) and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `991px` container bounds (`gap: 0px (flush layout)`, padding `0px`) with `cubic-bezier(0.625,0.05,0,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-davidecarusio-it` in your global stylesheet:

:root {
  /* Davide Carusio - Web Designer / Webflow Dev (www-davidecarusio-it) — Ground-Truth Extracted CSS Variables */
  --size-unit: 16; /* Layout / Spatial Grid Token (www-davidecarusio-it) */
  --size-container-ideal: 1440; /* Layout / Spatial Grid Token (www-davidecarusio-it) */
  --size-container-min: 1280px; /* Layout / Spatial Grid Token (www-davidecarusio-it) */
  --size-container-max: 1920px; /* Layout / Spatial Grid Token (www-davidecarusio-it) */
  --size-container: clamp(var(--size-container-min), 100vw, var(--size-container-max)); /* Layout / Spatial Grid Token (www-davidecarusio-it) */
  --button-043-color: #fff; /* Brand / Palette Token (www-davidecarusio-it) */
  --button-043-color-background: currentColor; /* Canvas / Surface Token (www-davidecarusio-it) */
  --button-043-hover-color-background: currentColor; /* Canvas / Surface Token (www-davidecarusio-it) */
  --button-043-icon-color: currentColor; /* Brand / Palette Token (www-davidecarusio-it) */
  --button-043-icon-color-background: transparent; /* Canvas / Surface Token (www-davidecarusio-it) */
  --button-043-color-focus: #000; /* Brand / Palette Token (www-davidecarusio-it) */
  --button-043-padding: 0.3em 0.5em; /* Layout / Spatial Grid Token (www-davidecarusio-it) */
  --button-043-border-radius: 0.125em; /* Elevation / Border Token (www-davidecarusio-it) */
  --button-043-icon-border-radius: 0.125em; /* Elevation / Border Token (www-davidecarusio-it) */
  --button-043-text-duplicate-distance: 1.5em; /* Typography Ink Token (www-davidecarusio-it) */
  --button-043-focus-inset: -0.125em; /* Dimension / Scale Token (www-davidecarusio-it) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fff` — grounded in `var(--button-043-color)` in `:root`
- **Primary Typography Ink**: `#000` — grounded in `var(--button-043-color-focus)` in `:root`
- **Elevated Surface / Card Substrate**: `#1c1c1b` — grounded in `.underlay-nav__container { color: #1c1c1b }`
- **Interactive Accent / Highlight**: `#f9efe7` — grounded in `.underlay-nav__container { color: #f9efe7 }`
- **Secondary / Muted Copy**: `#000000` — grounded in `::selection { background-color: black }` (`#000000`)
- **Structural Hairline Border**: `#f5ede4` — grounded in `.cursor-bubble { background-color: #f5ede4 }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `991px` extracted from `www-davidecarusio-it` stylesheet
- **Padding & Gutters**: `0px` lateral canvas padding with `0px (flush layout)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 991px`, `gap: 0px (flush layout)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `0px` horizontal padding
- **Media Queries**: `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media screen and (orientation: landscape) and (max-height: 500px)`
- **Corner Radii**: `var(--button-043-border-radius)`, `50%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `system-ui, -apple-system, sans-serif` (no custom `@font-face` extracted)
- **Body Font Stack**: `system-ui, -apple-system, sans-serif` (no custom `@font-face` extracted)
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `var(--size-font)`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `var(--size-font)`)
- **Body Copy Rule**: rule `body` (`font-size: var(--size-font)`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `var(--size-font)`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-davidecarusio-it` (`Davide Carusio - Web Designer / Webflow Dev`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.underlay-nav__header> — `www-davidecarusio-it`)**:
   - DOM & Selectors: Landmark `<nav class="underlay-nav__header">` hosting `Davide Carusio - Web Designer / Webf` navigation (`davide carusio · Projects · Services · IT · G e t i n t o u c h`), DOM attributes (`data-wf-page="6aabacfa3017369152d1f8b2"`, `data-wf-site="6a3a84272e4493d30711d604"`, `data-theme-nav="light"`, `data-bg-nav="light"`), and stylesheet rule `focus { outline:none; }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.underlay-nav__header> — `www-davidecarusio-it`)` (`www-davidecarusio-it`) adapts across `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media screen and (orientation: landscape) and (max-height: 500px)` with `cubic-bezier(0.625,0.05,0,1)`, `cubic-bezier(0.4,0,0.2,1)`, `cubic-bezier(0.32,0.72,0,1)` transitions and links `davide carusio · Projects · Services · IT · G e t i n t o u c h`.
2. **Hero Stage & Focal Lead (<section.hero_wrap> — `Privacy Policy`)**:
   - DOM & Selectors: Landmark `<section class="hero_wrap">` presenting display lead `Privacy Policy` and copy excerpt *"t h e b e s t p i z z a i s t h e m a r g h e r i t a"* over `#fff` canvas and `#000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#fff` background with `#000` headline `Privacy Policy`.
3. **Primary Showcase & Content Grid (<section.sticky-title-wrapper> — `Data Controller`)**:
   - DOM & Selectors: Landmark `<section class="sticky-title-wrapper">` rendering section `Data Controller` with copy *"P r o j e c t s P r o j e c t s"*, asset references (`normalize.css`, `webflow.css`, `davidecarusio-it-v3.webflow.css`, `favicon.png`), and grid rule `html.lenis body { height: auto; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.sticky-title-wrapper> — `Data Controller`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 991px`, `gap: 0px (flush layout)`) on desktop and Single-column vertical stack at `390px` viewport width with `0px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.work_wrap> — `Data Collected`)**:
   - DOM & Selectors: Landmark `<section class="work_wrap">` framing `Data Collected` and `Purpose of Processing` (*"S e r v i c e s S e r v i c e s"*) with `#1c1c1b` surface cards, `#f9efe7` accents, and `.lenis-stopped { overflow: clip; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.work_wrap> — `Data Collected`)` uses `var(--button-043-border-radius)`, `50%` radii, `#f9efe7` highlights, and assets (normalize.css, webflow.css, davidecarusio-it-v3.webflow.css).
5. **Colophon & Global Directory Footer (<footer.footer-wrap> — `https://www.davidecarusio.it/`)**:
   - DOM & Selectors: Landmark `<footer class="footer-wrap">` anchoring `Davide Carusio - Web Designer / ` footer links (`davide carusio · Projects · Services · IT · G e t i n t o u c h`), copy *"G e t i n t o u c h"*, and `#f5ede4` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer-wrap> — `https://www.davidecarusio.it/`)` aligns to `991px` extracted from `www-davidecarusio-it` stylesheet with `0px` lateral canvas padding with `0px (flush layout)` grid gap and attributes (data-wf-page="6aabacfa3017369152d1f8b2", data-wf-site="6a3a84272e4493d30711d604", data-theme-nav="light").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"t h e b e s t p i z z a i s t h e m a r g h e r i t a"*
- Copy Excerpt 2: *"P r o j e c t s P r o j e c t s"*
- Copy Excerpt 3: *"S e r v i c e s S e r v i c e s"*
- Copy Excerpt 4: *"G e t i n t o u c h"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.625,0.05,0,1)`, `cubic-bezier(0.4,0,0.2,1)`, `cubic-bezier(0.32,0.72,0,1)`
- **Extracted Stylesheet Rules (`www-davidecarusio-it`)**:
- `focus { outline:none; }`
- `html.lenis body { height: auto; }`
- `.lenis-stopped { overflow: clip; }`
- `.lenis.lenis-smooth iframe { pointer-events: none; }`
- `.lenis.lenis-autoToggle { transition-property: overflow; transition-duration: 1ms; transition-beha... }`
- **Per-Selector Transition Rules**:
- **Selector `.lenis.lenis-autoToggle`**: `transition: 1ms` extracted from `www-davidecarusio-it` stylesheet.
- **Selector `.button-043__bg .button-043__text`**: `transition: color 0.4s ease, background-color 0.4s ease` extracted from `www-davidecarusio-it` stylesheet.
- **Selector `media (hover: hover) and (pointer...`**: `transition: transform 0.4s cubic-bezier(0.625,0.05,0,1), opacity 0.4s c...` extracted from `www-davidecarusio-it` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.625,0.05,0,1)`)**: Governs interactive state transitions across `<nav.underlay-nav__header>` and `<section.sticky-title-wrapper>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-davidecarusio-it`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
