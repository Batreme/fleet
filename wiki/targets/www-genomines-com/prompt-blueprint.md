---
title: "UI Prompt Blueprint: www-genomines-com"
date: 2026-11-15
target: "www-genomines-com"
status: analyzed
capture: specimen
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#efebe1` / `#fff`)"
---

# UI Design System & Master Generation Blueprint: www-genomines-com

> **Home** (https://www.genomines.com/) — Genomines pioneers sustainable mineral extraction using hyperaccumulator plants, harnessing genomics to mine critical metals from soil, a...

![Desktop Design Specimen (Offline WebGL/JS Fallback — not live site capture)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Home** (`https://www.genomines.com/`). Genomines pioneers sustainable mineral extraction using hyperaccumulator plants, harnessing genomics to mine critical metals from soil, a...
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#efebe1` / `#fff`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#efebe1` (`body { background: #efebe1 }`) paired with `#000` primary typography and `#fff` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Causten` for display copy (`Let's grow together.`) with `Geist Mono` and `Geist Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1000px` container bounds (`gap: 12px`, padding `18px`) with `cubic-bezier(.4,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Design Specimen (Offline WebGL/JS Fallback — not live site capture)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `1000px` extracted from `www-genomines-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `18px` lateral canvas padding with `12px` grid gap.
- **Border Radius Scale**: `3px`, `1px`, `8px`, `6px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1000px`, `gap: 12px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `18px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:1000px)`, `@media (max-width:600px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#efebe1` | `body { background: #efebe1 }` |
| **Primary Typography Ink** | `#373735` | `body { color: #373735 }` |
| **Elevated Surface / Card Substrate** | `#000` | `.grid__visualizer-toggle { background: #000 }` |
| **Interactive Accent / Highlight** | `#fff` | `.grid__visualizer-toggle { color: #fff }` |
| **Secondary / Muted Copy** | `#d4ff8f` | `header__nav>ul .nav__item .nav_... { background: #d4ff8f }` |
| **Structural Hairline Border** | `#b3261e` | `al__form .contact-modal__feedba... { color: #b3261e }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--gridCell` | `0px` | Layout / Spatial Grid Token |
| `--gridGap` | `0px` | Layout / Spatial Grid Token |
| `--gridMargin` | `0px` | Layout / Spatial Grid Token |
| `--wrapper-margin` | `max(18px, 2.0833vw)` | Layout / Spatial Grid Token |
| `--margin-xl` | `72px` | Layout / Spatial Grid Token |
| `--margin-l` | `48px` | Layout / Spatial Grid Token |
| `--margin-m` | `24px` | Layout / Spatial Grid Token |
| `--margin-s` | `12px` | Layout / Spatial Grid Token |
| `--controls-backdrop-color` | `rgba(0, 0, 0, .4)` | Brand / Palette Token |
| `--media-range-track-background` | `rgba(239, 235, 225, .25)` | Canvas / Surface Token |
| `--media-time-range-buffered-color` | `rgba(239, 235, 225, .45)` | Brand / Palette Token |
| `--gradient-steps` | `transparent 0%, transparent 100%` | Dimension / Scale Token |
| `--media-control-hover-background` | `rgba(239, 235, 225, .1)` | Canvas / Surface Token |
| `--media-menu-background` | `rgba(55, 55, 53, .5)` | Canvas / Surface Token |
| `--media-menu-item-hover-background` | `rgba(239, 235, 225, .1)` | Canvas / Surface Token |
| `--quotes-extra-height` | `111px` | Layout / Spatial Grid Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Causten`.
- **Primary Body Stack**: `Geist Mono`.
- **Technical / Metadata Stack**: `Geist Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(1.19rem,.9722222222vw,1.61rem)`, `clamp(3.6rem,4.1666666667vw,7.8rem)`, `62.5%`, `10px`, `1.2rem`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(1.19rem,.9722222222vw,1.61rem)`, `clamp(3.6rem,4.1666666667vw,7.8rem)`, `62.5%`, `10px`, `1.2rem`).
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(1.19rem,.9722222222vw,1.61rem)`, `clamp(3.6rem,4.1666666667vw,7.8rem)`, `62.5%`, `10px`, `1.2rem`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(1.19rem,.9722222222vw,1.61rem)`, `clamp(3.6rem,4.1666666667vw,7.8rem)`, `62.5%`, `10px`, `1.2rem`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.header__nav>ul .nav__item .nav__...`**: `transition: transform .3s ease-out` extracted from `www-genomines-com` stylesheet.
- **Selector `er .header__nav>ul .nav__item .na...`**: `transition: opacity .25s ease-out,transform .25s ease-out,visibility .25s` extracted from `www-genomines-com` stylesheet.
- **Selector `submenu .submenu__item .submenu__...`**: `transition: transform .3s ease-out` extracted from `www-genomines-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.global__header>` and `<section.section__paradigm-shift>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Home                                       │
│ ====================================================================== │
│ [ <header.global__header>  | Homepage · Technology · Systemic Retur ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.section__hero>                              |   │
│ | H1: Let's grow together.                                         |   │
│ | Substrate: #efebe1    | Ink: #000       | Accent: #fff           |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.section__paradigm) max-w: 1000px         |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | We Grow Metal                |  | At scale.                    | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 12px  ) | │
│ | [<header.global__he] -> [<section.section__] -> [<section.section__] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.global__footer) | https://www.genomines.com/         │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.global__header> — `www-genomines-com`)**:
   - Landmark `<header class="global__header">` hosting `Home` navigation (`Homepage · Technology · Systemic Return · About us · Work with us`), DOM attributes (`data-taxi-ignore="true"`, `data-action="contact"`, `data-taxi-ignore="true"`, `data-action="contact"`), and stylesheet rule `after { margin:0;padding:0;box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.section__hero> — `Let's grow together.`)**:
   - Landmark `<section class="section__hero">` presenting display lead `Let's grow together.` and copy excerpt *"Company About us Work with us"* over `#efebe1` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.section__paradigm-shift> — `We Grow Metal`)**:
   - Landmark `<section class="section__paradigm-shift">` rendering section `We Grow Metal` with copy *"Biological infrastructure for critical metal extraction."*, asset references (`favicon-96x96.png`, `favicon.svg`, `favicon.ico`, `apple-touch-icon.png`), and grid rule `video { max-width:100%;display:block }`.
4. **Interactive Detail & Feature Matrix (<section.section__scenes> — `At scale.`)**:
   - Landmark `<section class="section__scenes">` framing `At scale.` and `The payload.` (*"Battery-grade nickel, harvested at best-in-class costs."*) with `#000` surface cards, `#fff` accents, and `button { background:none;border:none;cursor:pointer;font:inherit;color:inherit }`.
5. **Colophon & Global Directory Footer (<footer.global__footer> — `https://www.genomines.com/`)**:
   - Landmark `<footer class="global__footer">` anchoring `Home` footer links (`Homepage · Technology · Systemic Return · About us · Work with us`), copy *"Inside the team replacing the"*, and `#b3261e` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-genomines-com (Home)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-genomines-com` (**Home** — `https://www.genomines.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#efebe1` / `#fff`).
- **Identity & Domain Context**: Genomines pioneers sustainable mineral extraction using hyperaccumulator plants, harnessing genomics to mine critical metals from soil, a...
- **Primary Substrate**: `#efebe1` (`body { background: #efebe1 }`), **Primary Ink**: `#000`, **Accent / Highlight**: `#fff`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#efebe1` (`body { background: #efebe1 }`) paired with `#000` primary typography and `#fff` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Causten` for display copy (`Let's grow together.`) with `Geist Mono` and `Geist Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1000px` container bounds (`gap: 12px`, padding `18px`) with `cubic-bezier(.4,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-genomines-com` in your global stylesheet:

:root {
  /* Home (www-genomines-com) — Ground-Truth Extracted CSS Variables */
  --gridCell: 0px; /* Layout / Spatial Grid Token (www-genomines-com) */
  --gridGap: 0px; /* Layout / Spatial Grid Token (www-genomines-com) */
  --gridMargin: 0px; /* Layout / Spatial Grid Token (www-genomines-com) */
  --wrapper-margin: max(18px, 2.0833vw); /* Layout / Spatial Grid Token (www-genomines-com) */
  --margin-xl: 72px; /* Layout / Spatial Grid Token (www-genomines-com) */
  --margin-l: 48px; /* Layout / Spatial Grid Token (www-genomines-com) */
  --margin-m: 24px; /* Layout / Spatial Grid Token (www-genomines-com) */
  --margin-s: 12px; /* Layout / Spatial Grid Token (www-genomines-com) */
  --controls-backdrop-color: rgba(0, 0, 0, .4); /* Brand / Palette Token (www-genomines-com) */
  --media-range-track-background: rgba(239, 235, 225, .25); /* Canvas / Surface Token (www-genomines-com) */
  --media-time-range-buffered-color: rgba(239, 235, 225, .45); /* Brand / Palette Token (www-genomines-com) */
  --gradient-steps: transparent 0%, transparent 100%; /* Dimension / Scale Token (www-genomines-com) */
  --media-control-hover-background: rgba(239, 235, 225, .1); /* Canvas / Surface Token (www-genomines-com) */
  --media-menu-background: rgba(55, 55, 53, .5); /* Canvas / Surface Token (www-genomines-com) */
  --media-menu-item-hover-background: rgba(239, 235, 225, .1); /* Canvas / Surface Token (www-genomines-com) */
  --quotes-extra-height: 111px; /* Layout / Spatial Grid Token (www-genomines-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#efebe1` — grounded in `body { background: #efebe1 }`
- **Primary Typography Ink**: `#373735` — grounded in `body { color: #373735 }`
- **Elevated Surface / Card Substrate**: `#000` — grounded in `.grid__visualizer-toggle { background: #000 }`
- **Interactive Accent / Highlight**: `#fff` — grounded in `.grid__visualizer-toggle { color: #fff }`
- **Secondary / Muted Copy**: `#d4ff8f` — grounded in `header__nav>ul .nav__item .nav_... { background: #d4ff8f }`
- **Structural Hairline Border**: `#b3261e` — grounded in `al__form .contact-modal__feedba... { color: #b3261e }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1000px` extracted from `www-genomines-com` stylesheet
- **Padding & Gutters**: `18px` lateral canvas padding with `12px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1000px`, `gap: 12px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `18px` horizontal padding
- **Media Queries**: `@media (max-width:1000px)`, `@media (max-width:600px)`
- **Corner Radii**: `3px`, `1px`, `8px`, `6px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Causten`
- **Body Font Stack**: `Geist Mono`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(1.19rem,.9722222222vw,1.61rem)`, `clamp(3.6rem,4.1666666667vw,7.8rem)`, `62.5%`, `10px`, `1.2rem`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(1.19rem,.9722222222vw,1.61rem)`, `clamp(3.6rem,4.1666666667vw,7.8rem)`, `62.5%`, `10px`, `1.2rem`)
- **Body Copy Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(1.19rem,.9722222222vw,1.61rem)`, `clamp(3.6rem,4.1666666667vw,7.8rem)`, `62.5%`, `10px`, `1.2rem`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(1.19rem,.9722222222vw,1.61rem)`, `clamp(3.6rem,4.1666666667vw,7.8rem)`, `62.5%`, `10px`, `1.2rem`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-genomines-com` (`Home`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.global__header> — `www-genomines-com`)**:
   - DOM & Selectors: Landmark `<header class="global__header">` hosting `Home` navigation (`Homepage · Technology · Systemic Return · About us · Work with us`), DOM attributes (`data-taxi-ignore="true"`, `data-action="contact"`, `data-taxi-ignore="true"`, `data-action="contact"`), and stylesheet rule `after { margin:0;padding:0;box-sizing:border-box }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.global__header> — `www-genomines-com`)` (`www-genomines-com`) adapts across `@media (max-width:1000px)`, `@media (max-width:600px)` with `cubic-bezier(.4,0,.2,1)` transitions and links `Homepage · Technology · Systemic Return · About us · Work with us`.
2. **Hero Stage & Focal Lead (<section.section__hero> — `Let's grow together.`)**:
   - DOM & Selectors: Landmark `<section class="section__hero">` presenting display lead `Let's grow together.` and copy excerpt *"Company About us Work with us"* over `#efebe1` canvas and `#000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#efebe1` background with `#000` headline `Let's grow together.`.
3. **Primary Showcase & Content Grid (<section.section__paradigm-shift> — `We Grow Metal`)**:
   - DOM & Selectors: Landmark `<section class="section__paradigm-shift">` rendering section `We Grow Metal` with copy *"Biological infrastructure for critical metal extraction."*, asset references (`favicon-96x96.png`, `favicon.svg`, `favicon.ico`, `apple-touch-icon.png`), and grid rule `video { max-width:100%;display:block }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.section__paradigm-shift> — `We Grow Metal`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1000px`, `gap: 12px`) on desktop and Single-column vertical stack at `390px` viewport width with `18px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.section__scenes> — `At scale.`)**:
   - DOM & Selectors: Landmark `<section class="section__scenes">` framing `At scale.` and `The payload.` (*"Battery-grade nickel, harvested at best-in-class costs."*) with `#000` surface cards, `#fff` accents, and `button { background:none;border:none;cursor:pointer;font:inherit;color:inherit }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.section__scenes> — `At scale.`)` uses `3px`, `1px`, `8px`, `6px` radii, `#fff` highlights, and assets (favicon-96x96.png, favicon.svg, favicon.ico).
5. **Colophon & Global Directory Footer (<footer.global__footer> — `https://www.genomines.com/`)**:
   - DOM & Selectors: Landmark `<footer class="global__footer">` anchoring `Home` footer links (`Homepage · Technology · Systemic Return · About us · Work with us`), copy *"Inside the team replacing the"*, and `#b3261e` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.global__footer> — `https://www.genomines.com/`)` aligns to `1000px` extracted from `www-genomines-com` stylesheet with `18px` lateral canvas padding with `12px` grid gap and attributes (data-taxi-ignore="true", data-action="contact", data-taxi-ignore="true").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Company About us Work with us"*
- Copy Excerpt 2: *"Biological infrastructure for critical metal extraction."*
- Copy Excerpt 3: *"Battery-grade nickel, harvested at best-in-class costs."*
- Copy Excerpt 4: *"Inside the team replacing the"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`www-genomines-com`)**:
- `after { margin:0;padding:0;box-sizing:border-box }`
- `video { max-width:100%;display:block }`
- `button { background:none;border:none;cursor:pointer;font:inherit;color:inherit }`
- `textarea { font:inherit }`
- `.type__body { font-family:Causten,sans-serif;font-size:clamp(1.19rem,.9722222222vw,1.6... }`
- **Per-Selector Transition Rules**:
- **Selector `.header__nav>ul .nav__item .nav__...`**: `transition: transform .3s ease-out` extracted from `www-genomines-com` stylesheet.
- **Selector `er .header__nav>ul .nav__item .na...`**: `transition: opacity .25s ease-out,transform .25s ease-out,visibility .25s` extracted from `www-genomines-com` stylesheet.
- **Selector `submenu .submenu__item .submenu__...`**: `transition: transform .3s ease-out` extracted from `www-genomines-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.global__header>` and `<section.section__paradigm-shift>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-genomines-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
