---
title: "UI Prompt Blueprint: bar-topas-ch"
date: 2026-11-15
target: "[[overview|bar-topas-ch]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#B21236` / `#FEB914`)"
---

# UI Design System & Master Generation Blueprint: bar-topas-ch

> **Tòpas - bar-topas.ch** (https://bar-topas.ch/) — Tòpas by Topaze — Tapas & Bar. Découvrez la nouvelle cuisine hispano-suisse du Topaze.

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/bar-topas-ch/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Tòpas - bar-topas.ch** (`https://bar-topas.ch/`). Tòpas by Topaze — Tapas & Bar. Découvrez la nouvelle cuisine hispano-suisse du Topaze.
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#B21236` / `#FEB914`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#B21236` (`var(--rouge)` in `:root`) paired with `#EFEFE3` primary typography and `#FEB914` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Archivo` for display copy (`Tòpas by Topaze — Tapas & Bar à Vicq`) with `Barlow Condensed` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `52vw` container bounds (`gap: 26px`, padding `10px`) with `cubic-bezier(.2,.8,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/bar-topas-ch/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `52vw` extracted from `bar-topas-ch` stylesheet.
- **Canvas Lateral Padding & Spacing**: `10px` lateral canvas padding with `26px` grid gap.
- **Border Radius Scale**: `6px`, `999px`, `50%`, `var(--radius)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 52vw`, `gap: 26px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `10px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width: 760px)`, `@media (max-width: 960px)`, `@media (prefers-reduced-motion: reduce)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#B21236` | `var(--rouge)` in `:root` |
| **Primary Typography Ink** | `#EFEFE3` | `var(--creme)` in `:root` |
| **Elevated Surface / Card Substrate** | `#EDEAE0` | `var(--creme-fond)` in `:root` |
| **Interactive Accent / Highlight** | `#FEB914` | `var(--jaune)` in `:root` |
| **Secondary / Muted Copy** | `#FE8826` | `var(--orange)` in `:root` |
| **Structural Hairline Border** | `#F03812` | `var(--orange-rouge)` in `:root` |
| **Variable Token (`--bleu`)** | `#2C9FA2` | `var(--bleu)` in `:root` |
| **Variable Token (`--bordeaux`)** | `#7C1820` | `var(--bordeaux)` in `:root` |
| **Variable Token (`--brun`)** | `#60150D` | `var(--brun)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--rouge` | `#B21236` | Color / Atmospheric Token |
| `--creme` | `#EFEFE3` | Color / Atmospheric Token |
| `--creme-fond` | `#EDEAE0` | Color / Atmospheric Token |
| `--jaune` | `#FEB914` | Color / Atmospheric Token |
| `--orange` | `#FE8826` | Color / Atmospheric Token |
| `--orange-rouge` | `#F03812` | Color / Atmospheric Token |
| `--bleu` | `#2C9FA2` | Color / Atmospheric Token |
| `--bordeaux` | `#7C1820` | Color / Atmospheric Token |
| `--brun` | `#60150D` | Color / Atmospheric Token |
| `--f-title` | `"Archivo", "Arial Black", system-ui, sans-serif` | Dimension / Scale Token |
| `--f-cond` | `"Barlow Condensed", "Arial Narrow", system-ui, sans-serif` | Dimension / Scale Token |
| `--f-text` | `"Source Sans 3", Arial, system-ui, sans-serif` | Typography Ink Token |
| `--gutter` | `clamp(16px, 4vw, 56px)` | Layout / Spatial Grid Token |
| `--radius` | `22px` | Elevation / Border Token |
| `--ease` | `cubic-bezier(.2, .8, .2, 1)` | Motion / Easing Token |
| `--topbar-h` | `76px` | Dimension / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Archivo`.
- **Primary Body Stack**: `Barlow Condensed`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(17px, 1.05vw + 10px, 21px)`, `clamp(11px, .55vw + 8px, 15px)`, `1.25em`, `clamp(44px, 8vw, 130px)`, `clamp(24px, 3.4vw, 54px)`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(17px, 1.05vw + 10px, 21px)`, `clamp(11px, .55vw + 8px, 15px)`, `1.25em`, `clamp(44px, 8vw, 130px)`, `clamp(24px, 3.4vw, 54px)`).
- **Body Copy**: rule `body` (`font-size: clamp(17px, 1.05vw + 10px, 21px)`, `line-height: 1.45`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(17px, 1.05vw + 10px, 21px)`, `clamp(11px, .55vw + 8px, 15px)`, `1.25em`, `clamp(44px, 8vw, 130px)`, `clamp(24px, 3.4vw, 54px)`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.2,.8,.2,1)`, `cubic-bezier(.3,.0,.3,1)`, `cubic-bezier(.3,.7,.3,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.skip`**: `transition: transform .3s var(--ease)` extracted from `bar-topas-ch` stylesheet.
- **Selector `.btn`**: `transition: color .4s var(--ease)` extracted from `bar-topas-ch` stylesheet.
- **Selector `.btn::before`**: `transition: transform .5s var(--ease)` extracted from `bar-topas-ch` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.2,.8,.2,1)`)**: Governs interactive state transitions across `<header.topbar>` and `<section.s-marquee>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Tòpas - bar-topas.ch                       │
│ ====================================================================== │
│ [ <header.topbar>          | Bar Le Topaze                          ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.s-hero>                                     |   │
│ | H1: Tòpas by Topaze — Tapas & Bar à Vicques                      |   │
│ | Substrate: #B21236    | Ink: #EFEFE3    | Accent: #FEB914        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.s-marquee>       ) max-w: 52vw           |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Tòpas                        |  | Un pincho, c’est simple.     | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 26px  ) | │
│ | [<header.topbar>] -> [<section.s-hero>] -> [<section.s-marquee] |    │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.s-end>        ) | https://bar-topas.ch/              │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.topbar> — `bar-topas-ch`)**:
   - Landmark `<header class="topbar">` hosting `Tòpas - bar-topas.ch` navigation (`Bar Le Topaze`), DOM attributes (`data-intro`, `data-intro-bar`, `data-intro-done`, `data-cursor`), and stylesheet rule `after { box-sizing: border-box; }`.
2. **Hero Stage & Focal Lead (<section.s-hero> — `Tòpas by Topaze — Tapas & Bar à Vi`)**:
   - Landmark `<section class="s-hero">` presenting display lead `Tòpas by Topaze — Tapas & Bar à Vicques` and copy excerpt *"On allume la plancha…"* over `#B21236` canvas and `#EFEFE3` ink.
3. **Primary Showcase & Content Grid (<section.s-marquee> — `Tòpas`)**:
   - Landmark `<section class="s-marquee">` rendering section `Tòpas` with copy *"Les pinchos arrivent. Paciencia, amigo."*, asset references (`1640559617463684`, `fbevents.js`, `gtm.js`, `archivo-var-latin.woff2`), and grid rule `html.lenis body { height: auto; }`.
4. **Interactive Detail & Feature Matrix (<section.s-def> — `Un pincho, c’est simple.`)**:
   - Landmark `<section class="s-def">` framing `Un pincho, c’est simple.` and `Mucho délicieuse.` (*"On fait fondre la raclette. Lentamente."*) with `#EDEAE0` surface cards, `#FEB914` accents, and `.lenis.lenis-smooth { scroll-behavior: auto !important; }`.
5. **Colophon & Global Directory Footer (<footer.s-end> — `https://bar-topas.ch/`)**:
   - Landmark `<footer class="s-end edge-wave">` anchoring `Tòpas - bar-topas.ch` footer links (`Bar Le Topaze`), copy *"El chef cherche son pic. Il était dans sa poche."*, and `#F03812` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: bar-topas-ch (Tòpas - bar-topas.ch)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `bar-topas-ch` (**Tòpas - bar-topas.ch** — `https://bar-topas.ch/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#B21236` / `#FEB914`).
- **Identity & Domain Context**: Tòpas by Topaze — Tapas & Bar. Découvrez la nouvelle cuisine hispano-suisse du Topaze.
- **Primary Substrate**: `#B21236` (`var(--rouge)` in `:root`), **Primary Ink**: `#EFEFE3`, **Accent / Highlight**: `#FEB914`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#B21236` (`var(--rouge)` in `:root`) paired with `#EFEFE3` primary typography and `#FEB914` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Archivo` for display copy (`Tòpas by Topaze — Tapas & Bar à Vicq`) with `Barlow Condensed` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `52vw` container bounds (`gap: 26px`, padding `10px`) with `cubic-bezier(.2,.8,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `bar-topas-ch` in your global stylesheet:

:root {
  /* Tòpas - bar-topas.ch (bar-topas-ch) — Ground-Truth Extracted CSS Variables */
  --rouge: #B21236; /* Color / Atmospheric Token (bar-topas-ch) */
  --creme: #EFEFE3; /* Color / Atmospheric Token (bar-topas-ch) */
  --creme-fond: #EDEAE0; /* Color / Atmospheric Token (bar-topas-ch) */
  --jaune: #FEB914; /* Color / Atmospheric Token (bar-topas-ch) */
  --orange: #FE8826; /* Color / Atmospheric Token (bar-topas-ch) */
  --orange-rouge: #F03812; /* Color / Atmospheric Token (bar-topas-ch) */
  --bleu: #2C9FA2; /* Color / Atmospheric Token (bar-topas-ch) */
  --bordeaux: #7C1820; /* Color / Atmospheric Token (bar-topas-ch) */
  --brun: #60150D; /* Color / Atmospheric Token (bar-topas-ch) */
  --f-title: "Archivo", "Arial Black", system-ui, sans-serif; /* Dimension / Scale Token (bar-topas-ch) */
  --f-cond: "Barlow Condensed", "Arial Narrow", system-ui, sans-serif; /* Dimension / Scale Token (bar-topas-ch) */
  --f-text: "Source Sans 3", Arial, system-ui, sans-serif; /* Typography Ink Token (bar-topas-ch) */
  --gutter: clamp(16px, 4vw, 56px); /* Layout / Spatial Grid Token (bar-topas-ch) */
  --radius: 22px; /* Elevation / Border Token (bar-topas-ch) */
  --ease: cubic-bezier(.2, .8, .2, 1); /* Motion / Easing Token (bar-topas-ch) */
  --topbar-h: 76px; /* Dimension / Scale Token (bar-topas-ch) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#B21236` — grounded in `var(--rouge)` in `:root`
- **Primary Typography Ink**: `#EFEFE3` — grounded in `var(--creme)` in `:root`
- **Elevated Surface / Card Substrate**: `#EDEAE0` — grounded in `var(--creme-fond)` in `:root`
- **Interactive Accent / Highlight**: `#FEB914` — grounded in `var(--jaune)` in `:root`
- **Secondary / Muted Copy**: `#FE8826` — grounded in `var(--orange)` in `:root`
- **Structural Hairline Border**: `#F03812` — grounded in `var(--orange-rouge)` in `:root`
- **Variable Token (`--bleu`)**: `#2C9FA2` — grounded in `var(--bleu)` in `:root`
- **Variable Token (`--bordeaux`)**: `#7C1820` — grounded in `var(--bordeaux)` in `:root`
- **Variable Token (`--brun`)**: `#60150D` — grounded in `var(--brun)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `52vw` extracted from `bar-topas-ch` stylesheet
- **Padding & Gutters**: `10px` lateral canvas padding with `26px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 52vw`, `gap: 26px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `10px` horizontal padding
- **Media Queries**: `@media (max-width: 760px)`, `@media (max-width: 960px)`, `@media (prefers-reduced-motion: reduce)`
- **Corner Radii**: `6px`, `999px`, `50%`, `var(--radius)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Archivo`
- **Body Font Stack**: `Barlow Condensed`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(17px, 1.05vw + 10px, 21px)`, `clamp(11px, .55vw + 8px, 15px)`, `1.25em`, `clamp(44px, 8vw, 130px)`, `clamp(24px, 3.4vw, 54px)`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(17px, 1.05vw + 10px, 21px)`, `clamp(11px, .55vw + 8px, 15px)`, `1.25em`, `clamp(44px, 8vw, 130px)`, `clamp(24px, 3.4vw, 54px)`)
- **Body Copy Rule**: rule `body` (`font-size: clamp(17px, 1.05vw + 10px, 21px)`, `line-height: 1.45`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(17px, 1.05vw + 10px, 21px)`, `clamp(11px, .55vw + 8px, 15px)`, `1.25em`, `clamp(44px, 8vw, 130px)`, `clamp(24px, 3.4vw, 54px)`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `bar-topas-ch` (`Tòpas - bar-topas.ch`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.topbar> — `bar-topas-ch`)**:
   - DOM & Selectors: Landmark `<header class="topbar">` hosting `Tòpas - bar-topas.ch` navigation (`Bar Le Topaze`), DOM attributes (`data-intro`, `data-intro-bar`, `data-intro-done`, `data-cursor`), and stylesheet rule `after { box-sizing: border-box; }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.topbar> — `bar-topas-ch`)` (`bar-topas-ch`) adapts across `@media (max-width: 760px)`, `@media (max-width: 960px)`, `@media (prefers-reduced-motion: reduce)` with `cubic-bezier(.2,.8,.2,1)`, `cubic-bezier(.3,.0,.3,1)`, `cubic-bezier(.3,.7,.3,1)` transitions and links `Bar Le Topaze`.
2. **Hero Stage & Focal Lead (<section.s-hero> — `Tòpas by Topaze — Tapas & Bar à Vi`)**:
   - DOM & Selectors: Landmark `<section class="s-hero">` presenting display lead `Tòpas by Topaze — Tapas & Bar à Vicques` and copy excerpt *"On allume la plancha…"* over `#B21236` canvas and `#EFEFE3` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#B21236` background with `#EFEFE3` headline `Tòpas by Topaze — Tapas & Bar à Vicques`.
3. **Primary Showcase & Content Grid (<section.s-marquee> — `Tòpas`)**:
   - DOM & Selectors: Landmark `<section class="s-marquee">` rendering section `Tòpas` with copy *"Les pinchos arrivent. Paciencia, amigo."*, asset references (`1640559617463684`, `fbevents.js`, `gtm.js`, `archivo-var-latin.woff2`), and grid rule `html.lenis body { height: auto; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.s-marquee> — `Tòpas`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 52vw`, `gap: 26px`) on desktop and Single-column vertical stack at `390px` viewport width with `10px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.s-def> — `Un pincho, c’est simple.`)**:
   - DOM & Selectors: Landmark `<section class="s-def">` framing `Un pincho, c’est simple.` and `Mucho délicieuse.` (*"On fait fondre la raclette. Lentamente."*) with `#EDEAE0` surface cards, `#FEB914` accents, and `.lenis.lenis-smooth { scroll-behavior: auto !important; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.s-def> — `Un pincho, c’est simple.`)` uses `6px`, `999px`, `50%`, `var(--radius)` radii, `#FEB914` highlights, and assets (1640559617463684, fbevents.js, gtm.js).
5. **Colophon & Global Directory Footer (<footer.s-end> — `https://bar-topas.ch/`)**:
   - DOM & Selectors: Landmark `<footer class="s-end edge-wave">` anchoring `Tòpas - bar-topas.ch` footer links (`Bar Le Topaze`), copy *"El chef cherche son pic. Il était dans sa poche."*, and `#F03812` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.s-end> — `https://bar-topas.ch/`)` aligns to `52vw` extracted from `bar-topas-ch` stylesheet with `10px` lateral canvas padding with `26px` grid gap and attributes (data-intro, data-intro-bar, data-intro-done).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"On allume la plancha…"*
- Copy Excerpt 2: *"Les pinchos arrivent. Paciencia, amigo."*
- Copy Excerpt 3: *"On fait fondre la raclette. Lentamente."*
- Copy Excerpt 4: *"El chef cherche son pic. Il était dans sa poche."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.2,.8,.2,1)`, `cubic-bezier(.3,.0,.3,1)`, `cubic-bezier(.3,.7,.3,1)`
- **Extracted Stylesheet Rules (`bar-topas-ch`)**:
- `after { box-sizing: border-box; }`
- `html.lenis body { height: auto; }`
- `.lenis.lenis-smooth { scroll-behavior: auto !important; }`
- `.lenis.lenis-stopped { overflow: hidden; }`
- `svg { display: block; max-width: 100%; }`
- **Per-Selector Transition Rules**:
- **Selector `.skip`**: `transition: transform .3s var(--ease)` extracted from `bar-topas-ch` stylesheet.
- **Selector `.btn`**: `transition: color .4s var(--ease)` extracted from `bar-topas-ch` stylesheet.
- **Selector `.btn::before`**: `transition: transform .5s var(--ease)` extracted from `bar-topas-ch` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.2,.8,.2,1)`)**: Governs interactive state transitions across `<header.topbar>` and `<section.s-marquee>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `bar-topas-ch`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
