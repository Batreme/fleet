---
title: "UI Prompt Blueprint: revelatio-studio"
date: 2026-11-15
target: "[[overview|revelatio-studio]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#ff0`)"
---

# UI Design System & Master Generation Blueprint: revelatio-studio

> **Revelatio · Branding, Product Design & Code** (https://revelatio.studio/) — Revelatio is an integrated studio for branding, product design, and code, building digital experiences and brand systems for ambitious co...

![Desktop Viewport Capture (1440x13959)](file:///root/projects/fleet/wiki/targets/revelatio-studio/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Revelatio · Branding, Product Design & Code** (`https://revelatio.studio/`). Revelatio is an integrated studio for branding, product design, and code, building digital experiences and brand systems for ambitious co...
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#ff0`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`var(--tbg)` in `:root`) paired with `#000` primary typography and `#ff0` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Neue Haas Grotesk Text Pro 55 Roman` for display copy (`Branding, Product Design & Code. One`) with `Arial` and `monospace!important`.
  - **Calibrated Spatial Grid & Motion**: Combines `940px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(0.17,0,0.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/revelatio-studio/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×13959px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `940px` extracted from `revelatio-studio` stylesheet.
- **Canvas Lateral Padding & Spacing**: `9px` lateral canvas padding with `16px` grid gap.
- **Border Radius Scale**: `3px`, `100%`, `50%`, `2px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--tbg)` in `:root` |
| **Primary Typography Ink** | `#000` | `var(--tfg)` in `:root` |
| **Elevated Surface / Card Substrate** | `#0000` | `a { background-color: #0000 }` |
| **Interactive Accent / Highlight** | `#ff0` | `mark { background: #ff0 }` |
| **Secondary / Muted Copy** | `#333` | `body { color: #333 }` |
| **Structural Hairline Border** | `#3898ec` | `.w-button { background-color: #3898ec }` |
| **Variable Token (`--color--neutral--900`)** | `#ffffff52` | `var(--color--neutral--900)` in `:root` |
| **Variable Token (`--color--neutral--200`)** | `#00000014` | `var(--color--neutral--200)` in `:root` |
| **Variable Token (`--color--neutral--800`)** | `#ffffff29` | `var(--color--neutral--800)` in `:root` |
| **Variable Token (`--color--neutral--300`)** | `#00000029` | `var(--color--neutral--300)` in `:root` |
| **Variable Token (`--color--neutral--400`)** | `#00000052` | `var(--color--neutral--400)` in `:root` |
| **Variable Token (`--color--neutral--500`)** | `#000000a3` | `var(--color--neutral--500)` in `:root` |
| **Variable Token (`--color--neutral--600`)** | `#ffffff0a` | `var(--color--neutral--600)` in `:root` |
| **Variable Token (`--color--neutral--700`)** | `#ffffff14` | `var(--color--neutral--700)` in `:root` |
| **Variable Token (`--color--neutral--1000`)** | `#ffffffa3` | `var(--color--neutral--1000)` in `:root` |
| **Variable Token (`--color--neutral--100`)** | `#0000000a` | `var(--color--neutral--100)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color--neutral--light` | `white` | Canvas / Surface Token |
| `--color--neutral--dark` | `black` | Canvas / Surface Token |
| `--color--neutral--900` | `#ffffff52` | Brand / Palette Token |
| `--color--neutral--200` | `#00000014` | Brand / Palette Token |
| `--color--neutral--800` | `#ffffff29` | Brand / Palette Token |
| `--color--neutral--300` | `#00000029` | Brand / Palette Token |
| `--color--neutral--400` | `#00000052` | Brand / Palette Token |
| `--color--neutral--500` | `#000000a3` | Brand / Palette Token |
| `--color--neutral--600` | `#ffffff0a` | Brand / Palette Token |
| `--color--neutral--700` | `#ffffff14` | Brand / Palette Token |
| `--color--neutral--1000` | `#ffffffa3` | Brand / Palette Token |
| `--color--neutral--100` | `#0000000a` | Brand / Palette Token |
| `--connected-color` | `var(--color-two)` | Brand / Palette Token |
| `--menu-width` | `16em` | Layout / Spatial Grid Token |
| `--menu-transition-settings` | `height 200ms ease,max-height 200ms ease` | Motion / Easing Token |
| `--clock-rotate-direction` | `1` | Design System Custom Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Neue Haas Grotesk Text Pro 55 Roman`.
- **Primary Body Stack**: `Arial`.
- **Technical / Metadata Stack**: `monospace!important`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 2em`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 32px`, `line-height: 36px`).
- **Body Copy**: rule `body` (`font-size: 14px`, `line-height: 20px`).
- **Metadata & Navigation Labels**: rule `small` (`font-size: 80%`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.17,0,0.2,1)`, `cubic-bezier(0.5,0,0.83,1)`, `cubic-bezier(0.18,0.89,0.32,1.2)`.

### Per-Element Transition & Choreography Rules
- **Selector `.w-webflow-badge > img`**: `transition: unset` extracted from `revelatio-studio` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s, color .1s` extracted from `revelatio-studio` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `revelatio-studio` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.17,0,0.2,1)`)**: Governs interactive state transitions across `<nav.navbar>` and `<div.lenis>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Revelatio · Branding, Product Design & Cod │
│ ====================================================================== │
│ [ <nav.navbar>             | Work · Approach · About · Careers · EN ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <div.w-mod-ix>                                       |   │
│ | H1: Branding, Product Design & Code. One integrated v...         |   │
│ | Substrate: #fff       | Ink: #000       | Accent: #ff0           |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<div.lenis>               ) max-w: 940px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | We partner with companies of |  | Waterloo, New York, Boca Rat | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px  ) | │
│ | [<nav.navbar>] -> [<div.w-mod-ix>] -> [<div.lenis>] |                │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>       ) | https://revelatio.studio/          │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.navbar> — `revelatio-studio`)**:
   - Landmark `<nav class="navbar">` hosting `Revelatio · Branding, Product Design` navigation (`Work · Approach · About · Careers · EN`), DOM attributes (`data-wf-domain="revelatio.studio"`, `data-wf-page="6a1dba8694fc8f455cf55833"`, `data-wf-site="6a1dba8694fc8f455cf5585d"`, `data-scale-hover-bound="1"`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<div.w-mod-ix> — `Branding, Product Design & Code. O`)**:
   - Landmark `<div class="w-mod-ix">` presenting display lead `Branding, Product Design & Code. One integrated v...` and copy excerpt *"G e t i n t o u c h"* over `#fff` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<div.lenis> — `We partner with companies of all s`)**:
   - Landmark `<div class="lenis">` rendering section `We partner with companies of all sizes, across in...` with copy *"S e e a l l p r o j e c t s"*, asset references (`cdn.prod.website-files.com`, `pt-br`, `revelatio-studio.webflow.shared.6...`, `6a1adb7b38c8bf5b0bcefe1c_revelati...`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<div.lenis-smooth> — `Waterloo, New York, Boca Raton, At`)**:
   - Landmark `<div class="lenis-smooth">` framing `Waterloo, New York, Boca Raton, Atlanta, Los Ange...` and `Nothing here happened overnight. Each number repr...` (*"Fractional Brand Leadership Innovation Advisory Dedicated Brand S"*) with `#0000` surface cards, `#ff0` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://revelatio.studio/`)**:
   - Landmark `<footer class="footer">` anchoring `Revelatio · Branding, Product De` footer links (`Work · Approach · About · Careers · EN`), copy *"Fractional Brand Leadership"*, and `#3898ec` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: revelatio-studio (Revelatio · Branding, Product Design & Code)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `revelatio-studio` (**Revelatio · Branding, Product Design & Code** — `https://revelatio.studio/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#ff0`).
- **Identity & Domain Context**: Revelatio is an integrated studio for branding, product design, and code, building digital experiences and brand systems for ambitious co...
- **Primary Substrate**: `#fff` (`var(--tbg)` in `:root`), **Primary Ink**: `#000`, **Accent / Highlight**: `#ff0`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`var(--tbg)` in `:root`) paired with `#000` primary typography and `#ff0` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Neue Haas Grotesk Text Pro 55 Roman` for display copy (`Branding, Product Design & Code. One`) with `Arial` and `monospace!important`.
  - **Calibrated Spatial Grid & Motion**: Combines `940px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(0.17,0,0.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `revelatio-studio` in your global stylesheet:

:root {
  /* Revelatio · Branding, Product Design & Code (revelatio-studio) — Ground-Truth Extracted CSS Variables */
  --color--neutral--light: white; /* Canvas / Surface Token (revelatio-studio) */
  --color--neutral--dark: black; /* Canvas / Surface Token (revelatio-studio) */
  --color--neutral--900: #ffffff52; /* Brand / Palette Token (revelatio-studio) */
  --color--neutral--200: #00000014; /* Brand / Palette Token (revelatio-studio) */
  --color--neutral--800: #ffffff29; /* Brand / Palette Token (revelatio-studio) */
  --color--neutral--300: #00000029; /* Brand / Palette Token (revelatio-studio) */
  --color--neutral--400: #00000052; /* Brand / Palette Token (revelatio-studio) */
  --color--neutral--500: #000000a3; /* Brand / Palette Token (revelatio-studio) */
  --color--neutral--600: #ffffff0a; /* Brand / Palette Token (revelatio-studio) */
  --color--neutral--700: #ffffff14; /* Brand / Palette Token (revelatio-studio) */
  --color--neutral--1000: #ffffffa3; /* Brand / Palette Token (revelatio-studio) */
  --color--neutral--100: #0000000a; /* Brand / Palette Token (revelatio-studio) */
  --connected-color: var(--color-two); /* Brand / Palette Token (revelatio-studio) */
  --menu-width: 16em; /* Layout / Spatial Grid Token (revelatio-studio) */
  --menu-transition-settings: height 200ms ease,max-height 200ms ease; /* Motion / Easing Token (revelatio-studio) */
  --clock-rotate-direction: 1; /* Design System Custom Token (revelatio-studio) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fff` — grounded in `var(--tbg)` in `:root`
- **Primary Typography Ink**: `#000` — grounded in `var(--tfg)` in `:root`
- **Elevated Surface / Card Substrate**: `#0000` — grounded in `a { background-color: #0000 }`
- **Interactive Accent / Highlight**: `#ff0` — grounded in `mark { background: #ff0 }`
- **Secondary / Muted Copy**: `#333` — grounded in `body { color: #333 }`
- **Structural Hairline Border**: `#3898ec` — grounded in `.w-button { background-color: #3898ec }`
- **Variable Token (`--color--neutral--900`)**: `#ffffff52` — grounded in `var(--color--neutral--900)` in `:root`
- **Variable Token (`--color--neutral--200`)**: `#00000014` — grounded in `var(--color--neutral--200)` in `:root`
- **Variable Token (`--color--neutral--800`)**: `#ffffff29` — grounded in `var(--color--neutral--800)` in `:root`
- **Variable Token (`--color--neutral--300`)**: `#00000029` — grounded in `var(--color--neutral--300)` in `:root`
- **Variable Token (`--color--neutral--400`)**: `#00000052` — grounded in `var(--color--neutral--400)` in `:root`
- **Variable Token (`--color--neutral--500`)**: `#000000a3` — grounded in `var(--color--neutral--500)` in `:root`
- **Variable Token (`--color--neutral--600`)**: `#ffffff0a` — grounded in `var(--color--neutral--600)` in `:root`
- **Variable Token (`--color--neutral--700`)**: `#ffffff14` — grounded in `var(--color--neutral--700)` in `:root`
- **Variable Token (`--color--neutral--1000`)**: `#ffffffa3` — grounded in `var(--color--neutral--1000)` in `:root`
- **Variable Token (`--color--neutral--100`)**: `#0000000a` — grounded in `var(--color--neutral--100)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×13959px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `940px` extracted from `revelatio-studio` stylesheet
- **Padding & Gutters**: `9px` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding
- **Media Queries**: `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)`
- **Corner Radii**: `3px`, `100%`, `50%`, `2px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Neue Haas Grotesk Text Pro 55 Roman`
- **Body Font Stack**: `Arial`
- **Monospace / Technical Font Stack**: `monospace!important`
- **H1 Display Rule**: rule `h1` (`font-size: 2em`)
- **H2 Section Rule**: rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy Rule**: rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Index Rule**: rule `small` (`font-size: 80%`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `revelatio-studio` (`Revelatio · Branding, Product Design & Code`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.navbar> — `revelatio-studio`)**:
   - DOM & Selectors: Landmark `<nav class="navbar">` hosting `Revelatio · Branding, Product Design` navigation (`Work · Approach · About · Careers · EN`), DOM attributes (`data-wf-domain="revelatio.studio"`, `data-wf-page="6a1dba8694fc8f455cf55833"`, `data-wf-site="6a1dba8694fc8f455cf5585d"`, `data-scale-hover-bound="1"`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.navbar> — `revelatio-studio`)` (`revelatio-studio`) adapts across `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)` with `cubic-bezier(0.17,0,0.2,1)`, `cubic-bezier(0.5,0,0.83,1)`, `cubic-bezier(0.18,0.89,0.32,1.2)` transitions and links `Work · Approach · About · Careers · EN`.
2. **Hero Stage & Focal Lead (<div.w-mod-ix> — `Branding, Product Design & Code. O`)**:
   - DOM & Selectors: Landmark `<div class="w-mod-ix">` presenting display lead `Branding, Product Design & Code. One integrated v...` and copy excerpt *"G e t i n t o u c h"* over `#fff` canvas and `#000` ink.
   - Responsive Contract: Hero stage (`1440×13959px` desktop / `390×2400px` mobile) sets `#fff` background with `#000` headline `Branding, Product Design & Code. One integrated v...`.
3. **Primary Showcase & Content Grid (<div.lenis> — `We partner with companies of all s`)**:
   - DOM & Selectors: Landmark `<div class="lenis">` rendering section `We partner with companies of all sizes, across in...` with copy *"S e e a l l p r o j e c t s"*, asset references (`cdn.prod.website-files.com`, `pt-br`, `revelatio-studio.webflow.shared.6...`, `6a1adb7b38c8bf5b0bcefe1c_revelati...`), and grid rule `body { margin: 0; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<div.lenis> — `We partner with companies of all s`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `9px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<div.lenis-smooth> — `Waterloo, New York, Boca Raton, At`)**:
   - DOM & Selectors: Landmark `<div class="lenis-smooth">` framing `Waterloo, New York, Boca Raton, Atlanta, Los Ange...` and `Nothing here happened overnight. Each number repr...` (*"Fractional Brand Leadership Innovation Advisory Dedicated Brand S"*) with `#0000` surface cards, `#ff0` accents, and `summary { display: block; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<div.lenis-smooth> — `Waterloo, New York, Boca Raton, At`)` uses `3px`, `100%`, `50%`, `2px` radii, `#ff0` highlights, and assets (cdn.prod.website-files.com, pt-br, revelatio-studio.webflow.shared.6...).
5. **Colophon & Global Directory Footer (<footer.footer> — `https://revelatio.studio/`)**:
   - DOM & Selectors: Landmark `<footer class="footer">` anchoring `Revelatio · Branding, Product De` footer links (`Work · Approach · About · Careers · EN`), copy *"Fractional Brand Leadership"*, and `#3898ec` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer> — `https://revelatio.studio/`)` aligns to `940px` extracted from `revelatio-studio` stylesheet with `9px` lateral canvas padding with `16px` grid gap and attributes (data-wf-domain="revelatio.studio", data-wf-page="6a1dba8694fc8f455cf55833", data-wf-site="6a1dba8694fc8f455cf5585d").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"G e t i n t o u c h"*
- Copy Excerpt 2: *"S e e a l l p r o j e c t s"*
- Copy Excerpt 3: *"Fractional Brand Leadership Innovation Advisory Dedicated Brand Squads Embedded Pr..."*
- Copy Excerpt 4: *"Fractional Brand Leadership"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.17,0,0.2,1)`, `cubic-bezier(0.5,0,0.83,1)`, `cubic-bezier(0.18,0.89,0.32,1.2)`
- **Extracted Stylesheet Rules (`revelatio-studio`)**:
- `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`
- `body { margin: 0; }`
- `summary { display: block; }`
- `video { vertical-align: baseline; display: inline-block; }`
- `template { display: none; }`
- **Per-Selector Transition Rules**:
- **Selector `.w-webflow-badge > img`**: `transition: unset` extracted from `revelatio-studio` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s, color .1s` extracted from `revelatio-studio` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `revelatio-studio` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.17,0,0.2,1)`)**: Governs interactive state transitions across `<nav.navbar>` and `<div.lenis>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `revelatio-studio`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
