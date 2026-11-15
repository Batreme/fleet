---
title: "UI Prompt Blueprint: noho-ink"
date: 2026-11-15
target: "noho-ink"
status: analyzed
capture: dom
capture_desktop: dom
capture_mobile: dom
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#f1eee9` / `#0000`)"
---

# UI Design System & Master Generation Blueprint: noho-ink

> **Noho** (https://noho.ink) — E n e r g y u s a g e E n e r g y u s a g e

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Noho** (`https://noho.ink`). E n e r g y u s a g e E n e r g y u s a g e
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#f1eee9` / `#0000`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#f1eee9` (`var(--bg-page)` in `:root`) paired with `#3c3c3c` primary typography and `#0000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Switzer` for display copy (`“He ain’t heavy”`) with `Switzer Variable` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1279px` container bounds (`gap: 1.042vw`, padding `2.083vw`) with `cubic-bezier(0.25,0.1,0.25,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `1279px` extracted from `noho-ink` stylesheet.
- **Canvas Lateral Padding & Spacing**: `2.083vw` lateral canvas padding with `1.042vw` grid gap.
- **Border Radius Scale**: `100%`, `3px`, `50%`, `50px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1279px`, `gap: 1.042vw`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `2.083vw` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (min-width:1280px),screen and (min-width:992px...`, `@media screen and (min-width:992px)and (max-width:1279px)and (ho...`, `@media screen and (max-width:991px),screen and (min-width:992px)...`, `@media (max-width:479px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f1eee9` | `var(--bg-page)` in `:root` |
| **Primary Typography Ink** | `#3c3c3c` | `var(--txt-main)` in `:root` |
| **Elevated Surface / Card Substrate** | `#d7d1c7` | `var(--bg-switch)` in `:root` |
| **Interactive Accent / Highlight** | `#0000` | `var(--transperent)` in `:root` |
| **Secondary / Muted Copy** | `#e7e2da` | `var(--bg-element)` in `:root` |
| **Structural Hairline Border** | `#cdc0b0` | `var(--bg-element-third)` in `:root` |
| **Variable Token (`--raven-black-40`)** | `#3c3c3c66` | `var(--raven-black-40)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--noho-slogan-lift` | `0px` | Dimension / Scale Token |
| `--bg-page` | `#f1eee9` | Canvas / Surface Token |
| `--txt-main` | `#3c3c3c` | Color / Atmospheric Token |
| `--bg-form-element` | `white` | Canvas / Surface Token |
| `--raven-black-100` | `#3c3c3c` | Canvas / Surface Token |
| `--bg-switch` | `#d7d1c7` | Canvas / Surface Token |
| `--bg-inner-switch` | `white` | Canvas / Surface Token |
| `--bg-btn-pm` | `#3c3c3c` | Canvas / Surface Token |
| `--txt-btn-pm` | `white` | Design System Custom Token |
| `--bg-btn-sc` | `white` | Canvas / Surface Token |
| `--txt-btn-sc` | `#3c3c3c` | Color / Atmospheric Token |
| `--bg-btn-big` | `#3c3c3c` | Canvas / Surface Token |
| `--txt-btn-big` | `white` | Design System Custom Token |
| `--transperent` | `#0000` | Color / Atmospheric Token |
| `--raven-black-40` | `#3c3c3c66` | Canvas / Surface Token |
| `--offbeat` | `#d7d1c7` | Color / Atmospheric Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Switzer`.
- **Primary Body Stack**: `Switzer Variable`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `.h1` (`font-size: 7.292vw!important`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 32px`, `line-height: 36px`).
- **Body Copy**: rule `body` (`font-size: 14px`, `line-height: 20px`).
- **Metadata & Navigation Labels**: rule `small` (`font-size: 80%`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `#noho-screensaver`**: `transition: opacity .32s ease,visibility .32s ease,background-color .32s ease` extracted from `noho-ink` stylesheet.
- **Selector `.w-webflow-badge > img`**: `transition: unset` extracted from `noho-ink` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s, color .1s` extracted from `noho-ink` stylesheet.
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in static CSS).
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Noho                                       │
│ ====================================================================== │
│ [ <header.header>          | A b o u t A b o u t · P r i c e P r i  ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.switch>                                     |   │
│ | H1: “He ain’t heavy”                                             |   │
│ | Substrate: #f1eee9    | Ink: #3c3c3c    | Accent: #0000          |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.switch>          ) max-w: 1279px         |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | “Not only do they look great |  | Josh L                       | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 1.042v) | │
│ | [<header.header>] -> [<section.switch>] -> [<section.switch>] |      │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer-parent>) | https://noho.ink                   │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.header> — `noho-ink`)**:
   - Landmark `<header class="header section">` hosting `Noho` navigation (`A b o u t A b o u t · P r i c e P r i c e · B l o g B l o g · F A Q F A Q · About`), DOM attributes (`data-wf-domain="noho-a7a5a8.webflow.io"`, `data-wf-page="667aaef1d0489a9d5183ef5d"`, `data-wf-site="667aaef1d0489a9d5183ef56"`, `data-wf-status="1"`), and stylesheet rule `html { height:auto;overflow-x:hidden;overflow-y:auto }`.
2. **Hero Stage & Focal Lead (<section.switch> — `“He ain’t heavy”`)**:
   - Landmark `<section class="switch">` presenting display lead `“He ain’t heavy”` and copy excerpt *"A b o u t A b o u t"* over `#f1eee9` canvas and `#3c3c3c` ink.
3. **Primary Showcase & Content Grid (<section.switch> — `“Not only do they look great, but `)**:
   - Landmark `<section class="switch">` rendering section `“Not only do they look great, but they are very c...` with copy *"P r i c e P r i c e"*, asset references (`webflow.shared.min.css`, `6a4e44ce6ee465198645089f_favicon-...`, `6a4e444d307c1e077753f979_favicon-...`, `6a4e44ceccf875bb9d22c7cd_favicon-...`), and grid rule `html ::selection { background-color:var(--bg-form-element);color:var(--text-form-element) }`.
4. **Interactive Detail & Feature Matrix (<section.hero-section-parent> — `Josh L`)**:
   - Landmark `<section class="hero-section-parent">` framing `Josh L` and `Why Lighty` (*"E n e r g y u s a g e E n e r g y u s a g e"*) with `#d7d1c7` surface cards, `#0000` accents, and `html ::-moz-selection { background-color:var(--bg-form-element);color:var(--text-form-element) }`.
5. **Colophon & Global Directory Footer (<footer.footer-parent> — `https://noho.ink`)**:
   - Landmark `<footer class="footer-parent">` anchoring `Noho` footer links (`A b o u t A b o u t · P r i c e P r i c e · B l o g B l o g · F A Q F A Q · About`), copy *"Dark mode and reduce animation options allow you to save abo"*, and `#cdc0b0` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: noho-ink (Noho)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `noho-ink` (**Noho** — `https://noho.ink`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f1eee9` / `#0000`).
- **Identity & Domain Context**: E n e r g y u s a g e E n e r g y u s a g e
- **Primary Substrate**: `#f1eee9` (`var(--bg-page)` in `:root`), **Primary Ink**: `#3c3c3c`, **Accent / Highlight**: `#0000`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#f1eee9` (`var(--bg-page)` in `:root`) paired with `#3c3c3c` primary typography and `#0000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Switzer` for display copy (`“He ain’t heavy”`) with `Switzer Variable` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1279px` container bounds (`gap: 1.042vw`, padding `2.083vw`) with `cubic-bezier(0.25,0.1,0.25,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `noho-ink` in your global stylesheet:

:root {
  /* Noho (noho-ink) — Ground-Truth Extracted CSS Variables */
  --noho-slogan-lift: 0px; /* Dimension / Scale Token (noho-ink) */
  --bg-page: #f1eee9; /* Canvas / Surface Token (noho-ink) */
  --txt-main: #3c3c3c; /* Color / Atmospheric Token (noho-ink) */
  --bg-form-element: white; /* Canvas / Surface Token (noho-ink) */
  --raven-black-100: #3c3c3c; /* Canvas / Surface Token (noho-ink) */
  --bg-switch: #d7d1c7; /* Canvas / Surface Token (noho-ink) */
  --bg-inner-switch: white; /* Canvas / Surface Token (noho-ink) */
  --bg-btn-pm: #3c3c3c; /* Canvas / Surface Token (noho-ink) */
  --txt-btn-pm: white; /* Design System Custom Token (noho-ink) */
  --bg-btn-sc: white; /* Canvas / Surface Token (noho-ink) */
  --txt-btn-sc: #3c3c3c; /* Color / Atmospheric Token (noho-ink) */
  --bg-btn-big: #3c3c3c; /* Canvas / Surface Token (noho-ink) */
  --txt-btn-big: white; /* Design System Custom Token (noho-ink) */
  --transperent: #0000; /* Color / Atmospheric Token (noho-ink) */
  --raven-black-40: #3c3c3c66; /* Canvas / Surface Token (noho-ink) */
  --offbeat: #d7d1c7; /* Color / Atmospheric Token (noho-ink) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f1eee9` — grounded in `var(--bg-page)` in `:root`
- **Primary Typography Ink**: `#3c3c3c` — grounded in `var(--txt-main)` in `:root`
- **Elevated Surface / Card Substrate**: `#d7d1c7` — grounded in `var(--bg-switch)` in `:root`
- **Interactive Accent / Highlight**: `#0000` — grounded in `var(--transperent)` in `:root`
- **Secondary / Muted Copy**: `#e7e2da` — grounded in `var(--bg-element)` in `:root`
- **Structural Hairline Border**: `#cdc0b0` — grounded in `var(--bg-element-third)` in `:root`
- **Variable Token (`--raven-black-40`)**: `#3c3c3c66` — grounded in `var(--raven-black-40)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1279px` extracted from `noho-ink` stylesheet
- **Padding & Gutters**: `2.083vw` lateral canvas padding with `1.042vw` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1279px`, `gap: 1.042vw`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `2.083vw` horizontal padding
- **Media Queries**: `@media screen and (min-width:1280px),screen and (min-width:992px...`, `@media screen and (min-width:992px)and (max-width:1279px)and (ho...`, `@media screen and (max-width:991px),screen and (min-width:992px)...`, `@media (max-width:479px)`
- **Corner Radii**: `100%`, `3px`, `50%`, `50px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Switzer`
- **Body Font Stack**: `Switzer Variable`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: rule `.h1` (`font-size: 7.292vw!important`)
- **H2 Section Rule**: rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy Rule**: rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Index Rule**: rule `small` (`font-size: 80%`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `noho-ink` (`Noho`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.header> — `noho-ink`)**:
   - DOM & Selectors: Landmark `<header class="header section">` hosting `Noho` navigation (`A b o u t A b o u t · P r i c e P r i c e · B l o g B l o g · F A Q F A Q · About`), DOM attributes (`data-wf-domain="noho-a7a5a8.webflow.io"`, `data-wf-page="667aaef1d0489a9d5183ef5d"`, `data-wf-site="667aaef1d0489a9d5183ef56"`, `data-wf-status="1"`), and stylesheet rule `html { height:auto;overflow-x:hidden;overflow-y:auto }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.header> — `noho-ink`)` (`noho-ink`) adapts across `@media screen and (min-width:1280px),screen and (min-width:992px...`, `@media screen and (min-width:992px)and (max-width:1279px)and (ho...`, `@media screen and (max-width:991px),screen and (min-width:992px)...`, `@media (max-width:479px)` with `cubic-bezier(0.25,0.1,0.25,1)` transitions and links `A b o u t A b o u t · P r i c e P r i c e · B l o g B l o g · F A Q F A Q · About`.
2. **Hero Stage & Focal Lead (<section.switch> — `“He ain’t heavy”`)**:
   - DOM & Selectors: Landmark `<section class="switch">` presenting display lead `“He ain’t heavy”` and copy excerpt *"A b o u t A b o u t"* over `#f1eee9` canvas and `#3c3c3c` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#f1eee9` background with `#3c3c3c` headline `“He ain’t heavy”`.
3. **Primary Showcase & Content Grid (<section.switch> — `“Not only do they look great, but `)**:
   - DOM & Selectors: Landmark `<section class="switch">` rendering section `“Not only do they look great, but they are very c...` with copy *"P r i c e P r i c e"*, asset references (`webflow.shared.min.css`, `6a4e44ce6ee465198645089f_favicon-...`, `6a4e444d307c1e077753f979_favicon-...`, `6a4e44ceccf875bb9d22c7cd_favicon-...`), and grid rule `html ::selection { background-color:var(--bg-form-element);color:var(--text-form-element) }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.switch> — `“Not only do they look great, but `)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1279px`, `gap: 1.042vw`) on desktop and Single-column vertical stack at `390px` viewport width with `2.083vw` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.hero-section-parent> — `Josh L`)**:
   - DOM & Selectors: Landmark `<section class="hero-section-parent">` framing `Josh L` and `Why Lighty` (*"E n e r g y u s a g e E n e r g y u s a g e"*) with `#d7d1c7` surface cards, `#0000` accents, and `html ::-moz-selection { background-color:var(--bg-form-element);color:var(--text-form-element) }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.hero-section-parent> — `Josh L`)` uses `100%`, `3px`, `50%`, `50px` radii, `#0000` highlights, and assets (webflow.shared.min.css, 6a4e44ce6ee465198645089f_favicon-..., 6a4e444d307c1e077753f979_favicon-...).
5. **Colophon & Global Directory Footer (<footer.footer-parent> — `https://noho.ink`)**:
   - DOM & Selectors: Landmark `<footer class="footer-parent">` anchoring `Noho` footer links (`A b o u t A b o u t · P r i c e P r i c e · B l o g B l o g · F A Q F A Q · About`), copy *"Dark mode and reduce animation options allow you to save abo"*, and `#cdc0b0` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer-parent> — `https://noho.ink`)` aligns to `1279px` extracted from `noho-ink` stylesheet with `2.083vw` lateral canvas padding with `1.042vw` grid gap and attributes (data-wf-domain="noho-a7a5a8.webflow.io", data-wf-page="667aaef1d0489a9d5183ef5d", data-wf-site="667aaef1d0489a9d5183ef56").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"A b o u t A b o u t"*
- Copy Excerpt 2: *"P r i c e P r i c e"*
- Copy Excerpt 3: *"E n e r g y u s a g e E n e r g y u s a g e"*
- Copy Excerpt 4: *"Dark mode and reduce animation options allow you to save about 35% of your device..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`
- **Extracted Stylesheet Rules (`noho-ink`)**:
- `html { height:auto;overflow-x:hidden;overflow-y:auto }`
- `html ::selection { background-color:var(--bg-form-element);color:var(--text-form-element) }`
- `html ::-moz-selection { background-color:var(--bg-form-element);color:var(--text-form-element) }`
- `body { overflow-x:hidden;overflow-y:auto }`
- `html.noho-intro-active model-viewer { content-visibility:hidden;contain:strict;pointer-events:none }`
- **Per-Selector Transition Rules**:
- **Selector `#noho-screensaver`**: `transition: opacity .32s ease,visibility .32s ease,background-color .32s ease` extracted from `noho-ink` stylesheet.
- **Selector `.w-webflow-badge > img`**: `transition: unset` extracted from `noho-ink` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s, color .1s` extracted from `noho-ink` stylesheet.
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in static CSS).
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `noho-ink`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
