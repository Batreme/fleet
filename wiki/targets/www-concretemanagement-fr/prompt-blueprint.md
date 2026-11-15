---
title: "UI Prompt Blueprint: www-concretemanagement-fr"
date: 2026-11-15
target: "[[overview|www-concretemanagement-fr]]"
status: analyzed
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#141416` canvas, `#fffdf1` ink, `#fffdf1` accent)"
---

# UI Design System & Master Generation Blueprint: www-concretemanagement-fr

> **Concrete.** (https://www.concretemanagement.fr/) — L’immobilier, pensé pour vous

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/www-concretemanagement-fr/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Concrete.** (`https://www.concretemanagement.fr/`). L’immobilier, pensé pour vous
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#141416` canvas, `#fffdf1` ink, `#fffdf1` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#141416` (`var(--_colors---dark--base)` in `:root`) paired with `#fffdf1` primary typography and `#fffdf1` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Otto` for display copy (`L’immobilier, pensé pour vous`) with `Elios` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `940px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(.36,.33,0,1)` easing and Lenis Smooth Scroll (`data-lenis`), Swiper Touch Carousel Engine.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/www-concretemanagement-fr/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `940px` extracted from `www-concretemanagement-fr` stylesheet.
- **Canvas Lateral Padding & Spacing**: `9px` lateral canvas padding with `16px` grid gap.
- **Border Radius Scale**: `3px`, `100%`, `50%`, `4px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#141416` | `var(--_colors---dark--base)` in `:root` |
| **Primary Typography Ink** | `#dcd9c8` | `var(--_colors---kaki--base)` in `:root` |
| **Elevated Surface / Card Substrate** | `#5f4242` | `var(--_colors---brown--base)` in `:root` |
| **Interactive Accent / Highlight** | `#fffdf1` | `var(--_colors---cream--base)` in `:root` |
| **Secondary / Muted Copy** | `#97968d` | `var(--_colors---kaki--dark)` in `:root` |
| **Structural Hairline Border** | `#2c2b2f` | `var(--_colors---dark--light)` in `:root` |
| **Variable Token (`--_colors---dark--20`)** | `#14141633` | `var(--_colors---dark--20)` in `:root` |
| **Variable Token (`--_colors---white--20`)** | `#fff3` | `var(--_colors---white--20)` in `:root` |
| **Variable Token (`--_colors---white--50`)** | `#ffffff80` | `var(--_colors---white--50)` in `:root` |
| **Variable Token (`--_colors---dark--50`)** | `#14141680` | `var(--_colors---dark--50)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--_colors---dark--base` | `#141416` | Canvas / Surface Token |
| `--_colors---white--base` | `white` | Canvas / Surface Token |
| `--_colors---kaki--base` | `#dcd9c8` | Brand / Palette Token |
| `--xl` | `12.5em` | Dimension / Scale Token |
| `--_sizes---space--md` | `2.5em` | Layout / Spatial Grid Token |
| `--_sizes---space--sm` | `1.5em` | Layout / Spatial Grid Token |
| `--_colors---dark--20` | `#14141633` | Canvas / Surface Token |
| `--_sizes---space--lg` | `5em` | Layout / Spatial Grid Token |
| `--_colors---brown--base` | `#5f4242` | Brand / Palette Token |
| `--_colors---cream--base` | `#fffdf1` | Brand / Palette Token |
| `--_colors---kaki--dark` | `#97968d` | Canvas / Surface Token |
| `--_colors---dark--light` | `#2c2b2f` | Canvas / Surface Token |
| `--_colors---white--20` | `#fff3` | Canvas / Surface Token |
| `--_colors---white--50` | `#ffffff80` | Canvas / Surface Token |
| `--_colors---dark--50` | `#14141680` | Canvas / Surface Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Otto`.
- **Primary Body Stack**: `Elios`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 2em`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 32px`, `line-height: 36px`).
- **Body Copy**: rule `body` (`font-size: 14px`, `line-height: 20px`).
- **Metadata & Navigation Labels**: rule `small` (`font-size: 80%`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.36,.33,0,1)`, `cubic-bezier(.22,.61,.36,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.w-webflow-badge > img`**: `transition: unset` extracted from `www-concretemanagement-fr` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s, color .1s` extracted from `www-concretemanagement-fr` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `www-concretemanagement-fr` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.36,.33,0,1)`)**: Governs interactive state transitions across `<header.w-mod-js>` and `<section.presentation>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Concrete.                                  │
│ ====================================================================== │
│ [ <header.w-mod-js>        | Paris · Lausanne · Propriétaires + · L ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero>                                       |   │
│ | H1: L’immobilier, pensé pour vous                                |   │
│ | Substrate: #141416    | Ink: #fffdf1    | Accent: #fffdf1        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.presentation>    ) max-w: 940px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Concrete est une structure d |  | Votre patrimoine, notre expe | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px  ) | │
│ | [<header.w-mod-js>] -> [<section.hero>] -> [<section.presentat] |    │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.portail-btn>  ) | https://www.concretemanagement.fr/ │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.w-mod-js> — `www-concretemanagement-fr`)**:
   - Landmark `<header class="w-mod-js">` hosting `Concrete.` navigation (`Paris · Lausanne · Propriétaires + · Locataires + · À propos`), DOM attributes (`data-wf-domain="www.concretemanagemen..."`, `data-wf-page="6966a64d3505e01c9d776d27"`, `data-wf-site="6966a64c3505e01c9d776d0f"`, `data-wf--buttonsimple--variant="cream"`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `L’immobilier, pensé pour vous`)**:
   - Landmark `<section class="hero">` presenting display lead `L’immobilier, pensé pour vous` and copy excerpt *"Demander une estimation"* over `#141416` canvas and `#fffdf1` ink.
3. **Primary Showcase & Content Grid (<section.presentation> — `Concrete est une structure de gest`)**:
   - Landmark `<section class="presentation u-section">` rendering section `Concrete est une structure de gestion patrimonial...` with copy *"Gestion moyenne durée"*, asset references (`cdn.prod.website-files.com`, `concrete-3b73a4.webflow.shared.4d...`, `69809783d135718ad587d127_favicon.png`, `69809785d587f5575f03e822_favicon-...`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.stacking> — `Votre patrimoine, notre expertise`)**:
   - Landmark `<section class="stacking u-section">` framing `Votre patrimoine, notre expertise` and `Gestion moyenne durée` (*"Gestion courte durée"*) with `#5f4242` surface cards, `#fffdf1` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.portail-btn> — `https://www.concretemanagement.fr/`)**:
   - Landmark `<footer class="portail-btn">` anchoring `Concrete.` footer links (`Paris · Lausanne · Propriétaires + · Locataires + · À propos`), copy *"Trouver un appartement"*, and `#2c2b2f` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-concretemanagement-fr (Concrete.)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-concretemanagement-fr` (**Concrete.** — `https://www.concretemanagement.fr/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#141416` canvas, `#fffdf1` ink, `#fffdf1` accent).
- **Identity & Domain Context**: L’immobilier, pensé pour vous
- **Primary Substrate**: `#141416` (`var(--_colors---dark--base)` in `:root`), **Primary Ink**: `#fffdf1`, **Accent / Highlight**: `#fffdf1`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#141416` (`var(--_colors---dark--base)` in `:root`) paired with `#fffdf1` primary typography and `#fffdf1` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Otto` for display copy (`L’immobilier, pensé pour vous`) with `Elios` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `940px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(.36,.33,0,1)` easing and Lenis Smooth Scroll (`data-lenis`), Swiper Touch Carousel Engine.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-concretemanagement-fr` in your global stylesheet:

:root {
  /* Concrete. (www-concretemanagement-fr) — Ground-Truth Extracted CSS Variables */
  --w-backdrop-animation: initial; /* Motion / Easing Token (www-concretemanagement-fr) */
  --_colors---dark--base: #141416; /* Canvas / Surface Token (www-concretemanagement-fr) */
  --_colors---white--base: white; /* Canvas / Surface Token (www-concretemanagement-fr) */
  --_colors---kaki--base: #dcd9c8; /* Brand / Palette Token (www-concretemanagement-fr) */
  --xl: 12.5em; /* Dimension / Scale Token (www-concretemanagement-fr) */
  --_sizes---space--md: 2.5em; /* Layout / Spatial Grid Token (www-concretemanagement-fr) */
  --_sizes---space--sm: 1.5em; /* Layout / Spatial Grid Token (www-concretemanagement-fr) */
  --_colors---dark--20: #14141633; /* Canvas / Surface Token (www-concretemanagement-fr) */
  --_sizes---space--lg: 5em; /* Layout / Spatial Grid Token (www-concretemanagement-fr) */
  --_colors---brown--base: #5f4242; /* Brand / Palette Token (www-concretemanagement-fr) */
  --_colors---cream--base: #fffdf1; /* Brand / Palette Token (www-concretemanagement-fr) */
  --_colors---kaki--dark: #97968d; /* Canvas / Surface Token (www-concretemanagement-fr) */
  --_colors---dark--light: #2c2b2f; /* Canvas / Surface Token (www-concretemanagement-fr) */
  --_colors---white--20: #fff3; /* Canvas / Surface Token (www-concretemanagement-fr) */
  --_colors---white--50: #ffffff80; /* Canvas / Surface Token (www-concretemanagement-fr) */
  --_colors---dark--50: #14141680; /* Canvas / Surface Token (www-concretemanagement-fr) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#141416` — grounded in `var(--_colors---dark--base)` in `:root`
- **Primary Typography Ink**: `#dcd9c8` — grounded in `var(--_colors---kaki--base)` in `:root`
- **Elevated Surface / Card Substrate**: `#5f4242` — grounded in `var(--_colors---brown--base)` in `:root`
- **Interactive Accent / Highlight**: `#fffdf1` — grounded in `var(--_colors---cream--base)` in `:root`
- **Secondary / Muted Copy**: `#97968d` — grounded in `var(--_colors---kaki--dark)` in `:root`
- **Structural Hairline Border**: `#2c2b2f` — grounded in `var(--_colors---dark--light)` in `:root`
- **Variable Token (`--_colors---dark--20`)**: `#14141633` — grounded in `var(--_colors---dark--20)` in `:root`
- **Variable Token (`--_colors---white--20`)**: `#fff3` — grounded in `var(--_colors---white--20)` in `:root`
- **Variable Token (`--_colors---white--50`)**: `#ffffff80` — grounded in `var(--_colors---white--50)` in `:root`
- **Variable Token (`--_colors---dark--50`)**: `#14141680` — grounded in `var(--_colors---dark--50)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `940px` extracted from `www-concretemanagement-fr` stylesheet
- **Padding & Gutters**: `9px` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding
- **Media Queries**: `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)`
- **Corner Radii**: `3px`, `100%`, `50%`, `4px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Otto`
- **Body Font Stack**: `Elios`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: rule `h1` (`font-size: 2em`)
- **H2 Section Rule**: rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy Rule**: rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Index Rule**: rule `small` (`font-size: 80%`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-concretemanagement-fr` (`Concrete.`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.w-mod-js> — `www-concretemanagement-fr`)**:
   - DOM & Selectors: Landmark `<header class="w-mod-js">` hosting `Concrete.` navigation (`Paris · Lausanne · Propriétaires + · Locataires + · À propos`), DOM attributes (`data-wf-domain="www.concretemanagemen..."`, `data-wf-page="6966a64d3505e01c9d776d27"`, `data-wf-site="6966a64c3505e01c9d776d0f"`, `data-wf--buttonsimple--variant="cream"`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.w-mod-js> — `www-concretemanagement-fr`)` (`www-concretemanagement-fr`) adapts across `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)` with `cubic-bezier(.36,.33,0,1)`, `cubic-bezier(.22,.61,.36,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `Paris · Lausanne · Propriétaires + · Locataires + · À propos`.
2. **Hero Stage & Focal Lead (<section.hero> — `L’immobilier, pensé pour vous`)**:
   - DOM & Selectors: Landmark `<section class="hero">` presenting display lead `L’immobilier, pensé pour vous` and copy excerpt *"Demander une estimation"* over `#141416` canvas and `#fffdf1` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#141416` background with `#fffdf1` headline `L’immobilier, pensé pour vous`.
3. **Primary Showcase & Content Grid (<section.presentation> — `Concrete est une structure de gest`)**:
   - DOM & Selectors: Landmark `<section class="presentation u-section">` rendering section `Concrete est une structure de gestion patrimonial...` with copy *"Gestion moyenne durée"*, asset references (`cdn.prod.website-files.com`, `concrete-3b73a4.webflow.shared.4d...`, `69809783d135718ad587d127_favicon.png`, `69809785d587f5575f03e822_favicon-...`), and grid rule `body { margin: 0; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.presentation> — `Concrete est une structure de gest`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `9px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.stacking> — `Votre patrimoine, notre expertise`)**:
   - DOM & Selectors: Landmark `<section class="stacking u-section">` framing `Votre patrimoine, notre expertise` and `Gestion moyenne durée` (*"Gestion courte durée"*) with `#5f4242` surface cards, `#fffdf1` accents, and `summary { display: block; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.stacking> — `Votre patrimoine, notre expertise`)` uses `3px`, `100%`, `50%`, `4px` radii, `#fffdf1` highlights, and assets (cdn.prod.website-files.com, concrete-3b73a4.webflow.shared.4d..., 69809783d135718ad587d127_favicon.png).
5. **Colophon & Global Directory Footer (<footer.portail-btn> — `https://www.concretemanagement.fr/`)**:
   - DOM & Selectors: Landmark `<footer class="portail-btn">` anchoring `Concrete.` footer links (`Paris · Lausanne · Propriétaires + · Locataires + · À propos`), copy *"Trouver un appartement"*, and `#2c2b2f` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.portail-btn> — `https://www.concretemanagement.fr/`)` aligns to `940px` extracted from `www-concretemanagement-fr` stylesheet with `9px` lateral canvas padding with `16px` grid gap and attributes (data-wf-domain="www.concretemanagemen...", data-wf-page="6966a64d3505e01c9d776d27", data-wf-site="6966a64c3505e01c9d776d0f").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Demander une estimation"*
- Copy Excerpt 2: *"Gestion moyenne durée"*
- Copy Excerpt 3: *"Gestion courte durée"*
- Copy Excerpt 4: *"Trouver un appartement"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.36,.33,0,1)`, `cubic-bezier(.22,.61,.36,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`www-concretemanagement-fr`)**:
- `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`
- `body { margin: 0; }`
- `summary { display: block; }`
- `video { vertical-align: baseline; display: inline-block; }`
- `template { display: none; }`
- **Per-Selector Transition Rules**:
- **Selector `.w-webflow-badge > img`**: `transition: unset` extracted from `www-concretemanagement-fr` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s, color .1s` extracted from `www-concretemanagement-fr` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `www-concretemanagement-fr` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.36,.33,0,1)`)**: Governs interactive state transitions across `<header.w-mod-js>` and `<section.presentation>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-concretemanagement-fr`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
