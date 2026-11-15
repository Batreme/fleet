---
title: "UI Prompt Blueprint: www-3d-discovery-fr"
date: 2026-11-15
target: "[[overview|www-3d-discovery-fr]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#1a1a1a` / `#ebebeb`)"
---

# UI Design System & Master Generation Blueprint: www-3d-discovery-fr

> **3D Discovery · Exploring New Dimensions** (https://www.3d-discovery.fr/) — Transformez vos lieux, projets et produits en expériences web immersives : exploration 3D, contenus et interactions réunis pour présenter...

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/www-3d-discovery-fr/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **3D Discovery · Exploring New Dimensions** (`https://www.3d-discovery.fr/`). Transformez vos lieux, projets et produits en expériences web immersives : exploration 3D, contenus et interactions réunis pour présenter...
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#1a1a1a` / `#ebebeb`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#1a1a1a` (`var(--color-primary)` in `:root`) paired with `#ebebeb` primary typography and `#ebebeb` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Inter` for display copy (`Transformez vos lieux en experiences`) with `Inter Fallback` and `JetBrains Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1280px` container bounds (`gap: .5rem`, padding `1.5rem`) with `cubic-bezier(.8,0,1,1)` easing and Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/www-3d-discovery-fr/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `1280px` extracted from `www-3d-discovery-fr` stylesheet.
- **Canvas Lateral Padding & Spacing**: `1.5rem` lateral canvas padding with `.5rem` grid gap.
- **Border Radius Scale**: `50%`, `999px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1280px`, `gap: .5rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `1.5rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (min-width:768px)`, `@media (min-width:1024px)`, `@media (min-width:1280px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#1a1a1a` | `var(--color-primary)` in `:root` |
| **Primary Typography Ink** | `#2e2e2e` | `var(--color-primary-light)` in `:root` |
| **Elevated Surface / Card Substrate** | `#242424` | `var(--bg-elevated)` in `:root` |
| **Interactive Accent / Highlight** | `#ebebeb` | `var(--bg-inverse)` in `:root` |
| **Secondary / Muted Copy** | `#b3b3b3` | `var(--text-secondary)` in `:root` |
| **Structural Hairline Border** | `#999` | `var(--text-muted)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-inter` | `"Inter", "Inter Fallback"` | Typography / Scale Token |
| `--font-sora` | `"Sora", "Sora Fallback"` | Typography / Scale Token |
| `--color-primary` | `#1a1a1a` | Brand / Palette Token |
| `--color-primary-light` | `#2e2e2e` | Canvas / Surface Token |
| `--color-primary-dark` | `#1a1a1a` | Canvas / Surface Token |
| `--color-secondary` | `#1a1a1a` | Brand / Palette Token |
| `--header-height` | `64px` | Layout / Spatial Grid Token |
| `--header-height-mobile` | `56px` | Layout / Spatial Grid Token |
| `--container-padding` | `1.5rem` | Layout / Spatial Grid Token |
| `--transition-fast` | `.15s ease` | Motion / Easing Token |
| `--transition-base` | `.2s ease` | Motion / Easing Token |
| `--transition-slow` | `.3s ease` | Motion / Easing Token |
| `--transition-theme` | `.2s ease` | Brand / Palette Token |
| `--z-header` | `30` | Layout / Spatial Grid Token |
| `--z-modal` | `50` | Elevation / Border Token |
| `--z-tooltip` | `70` | Elevation / Border Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Inter`.
- **Primary Body Stack**: `Inter Fallback`.
- **Technical / Metadata Stack**: `JetBrains Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `,.h1` (`font-size: 2.25rem`, `line-height: 1.1`, `letter-spacing: -.025em`, `font-weight: 700`).
- **Section Heading (`H2`)**: rule `,.h2` (`font-size: 1.875rem`, `line-height: 1.1`, `letter-spacing: -.025em`, `font-weight: 700`).
- **Body Copy**: CSS variables `--bg-body: #1a1a1a`, `--tra-body-h: 16rem`.
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1rem`, `2.25rem`, `3rem`, `3.75rem`, `4.5rem`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.8,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.65,0,.35,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `:after`**: `transition: .01ms!important` extracted from `www-3d-discovery-fr` stylesheet.
- **Selector `body`**: `transition: background-color var(--transition-theme),color var(--transitio...` extracted from `www-3d-discovery-fr` stylesheet.
- **Selector `::-webkit-scrollbar-track`**: `transition: background var(--transition-theme)` extracted from `www-3d-discovery-fr` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.8,0,1,1)`)**: Governs interactive state transitions across `<header.header>` and `<section.sg-section>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — 3D Discovery · Exploring New Dimensions    │
│ ====================================================================== │
│ [ <header.header>          | Solutions · Expériences · Fonctionnali ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.sg-section>                                 |   │
│ | H1: Transformez vos lieux en experiences immersives              |   │
│ | Substrate: #1a1a1a    | Ink: #ebebeb    | Accent: #ebebeb        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.sg-section>      ) max-w: 1280px         |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Choisissez votre terrain     |  | Voir, c’est comprendre       | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .5rem ) | │
│ | [<header.header>] -> [<section.sg-sectio] -> [<section.sg-sectio] |  │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.sg-footer>    ) | https://www.3d-discovery.fr/       │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.header> — `www-3d-discovery-fr`)**:
   - Landmark `<header class="header">` hosting `3D Discovery · Exploring New Dimensi` navigation (`Solutions · Expériences · Fonctionnalités · Blog`), DOM attributes (`data-theme="light"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `nter_2fe1ab3d-module__-T-KAq__cla... { font-family:Inter,Inter Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.sg-section> — `Transformez vos lieux en experienc`)**:
   - Landmark `<section class="sg-section">` presenting display lead `Transformez vos lieux en experiences immersives` and copy excerpt *"Planifier une démo"* over `#1a1a1a` canvas and `#ebebeb` ink.
3. **Primary Showcase & Content Grid (<section.sg-section> — `Choisissez votre terrain`)**:
   - Landmark `<section class="sg-section sg-section--seq">` rendering section `Choisissez votre terrain` with copy *"03 Fonctionnalités"*, asset references (`83afe278b6a6bb3c-s.p.0q-301v4kxxn...`, `c41ca59f1c34ba31-s.p.0xxb547n1hn7...`, `0ghcmdv7avfm..css`, `04vxxuqck~drg.css`), and grid rule `inter_2fe1ab3d-module__-T-KAq__va... { --font-inter:"Inter", "Inter Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.sg-section> — `Voir, c’est comprendre`)**:
   - Landmark `<section class="sg-section sg-solutions">` framing `Voir, c’est comprendre` and `Planifier une démo` (*"3D Discovery · ©2026"*) with `#242424` surface cards, `#ebebeb` accents, and `sora_3fd80e00-module__HLND6q__cla... { font-family:Sora,Sora Fallback;font-style:normal }`.
5. **Colophon & Global Directory Footer (<footer.sg-footer> — `https://www.3d-discovery.fr/`)**:
   - Landmark `<footer class="sg-footer">` anchoring `3D Discovery · Exploring New Dim` footer links (`Solutions · Expériences · Fonctionnalités · Blog`), copy *"Exploring new dimensions"*, and `#999` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-3d-discovery-fr (3D Discovery · Exploring New Dimensions)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-3d-discovery-fr` (**3D Discovery · Exploring New Dimensions** — `https://www.3d-discovery.fr/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#1a1a1a` / `#ebebeb`).
- **Identity & Domain Context**: Transformez vos lieux, projets et produits en expériences web immersives : exploration 3D, contenus et interactions réunis pour présenter...
- **Primary Substrate**: `#1a1a1a` (`var(--color-primary)` in `:root`), **Primary Ink**: `#ebebeb`, **Accent / Highlight**: `#ebebeb`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#1a1a1a` (`var(--color-primary)` in `:root`) paired with `#ebebeb` primary typography and `#ebebeb` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Inter` for display copy (`Transformez vos lieux en experiences`) with `Inter Fallback` and `JetBrains Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1280px` container bounds (`gap: .5rem`, padding `1.5rem`) with `cubic-bezier(.8,0,1,1)` easing and Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-3d-discovery-fr` in your global stylesheet:

:root {
  /* 3D Discovery · Exploring New Dimensions (www-3d-discovery-fr) — Ground-Truth Extracted CSS Variables */
  --font-inter: "Inter", "Inter Fallback"; /* Typography / Scale Token (www-3d-discovery-fr) */
  --font-sora: "Sora", "Sora Fallback"; /* Typography / Scale Token (www-3d-discovery-fr) */
  --color-primary: #1a1a1a; /* Brand / Palette Token (www-3d-discovery-fr) */
  --color-primary-light: #2e2e2e; /* Canvas / Surface Token (www-3d-discovery-fr) */
  --color-primary-dark: #1a1a1a; /* Canvas / Surface Token (www-3d-discovery-fr) */
  --color-secondary: #1a1a1a; /* Brand / Palette Token (www-3d-discovery-fr) */
  --header-height: 64px; /* Layout / Spatial Grid Token (www-3d-discovery-fr) */
  --header-height-mobile: 56px; /* Layout / Spatial Grid Token (www-3d-discovery-fr) */
  --container-padding: 1.5rem; /* Layout / Spatial Grid Token (www-3d-discovery-fr) */
  --transition-fast: .15s ease; /* Motion / Easing Token (www-3d-discovery-fr) */
  --transition-base: .2s ease; /* Motion / Easing Token (www-3d-discovery-fr) */
  --transition-slow: .3s ease; /* Motion / Easing Token (www-3d-discovery-fr) */
  --transition-theme: .2s ease; /* Brand / Palette Token (www-3d-discovery-fr) */
  --z-header: 30; /* Layout / Spatial Grid Token (www-3d-discovery-fr) */
  --z-modal: 50; /* Elevation / Border Token (www-3d-discovery-fr) */
  --z-tooltip: 70; /* Elevation / Border Token (www-3d-discovery-fr) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#1a1a1a` — grounded in `var(--color-primary)` in `:root`
- **Primary Typography Ink**: `#2e2e2e` — grounded in `var(--color-primary-light)` in `:root`
- **Elevated Surface / Card Substrate**: `#242424` — grounded in `var(--bg-elevated)` in `:root`
- **Interactive Accent / Highlight**: `#ebebeb` — grounded in `var(--bg-inverse)` in `:root`
- **Secondary / Muted Copy**: `#b3b3b3` — grounded in `var(--text-secondary)` in `:root`
- **Structural Hairline Border**: `#999` — grounded in `var(--text-muted)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1280px` extracted from `www-3d-discovery-fr` stylesheet
- **Padding & Gutters**: `1.5rem` lateral canvas padding with `.5rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1280px`, `gap: .5rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `1.5rem` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (min-width:768px)`, `@media (min-width:1024px)`, `@media (min-width:1280px)`
- **Corner Radii**: `50%`, `999px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter Fallback`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **H1 Display Rule**: rule `,.h1` (`font-size: 2.25rem`, `line-height: 1.1`, `letter-spacing: -.025em`, `font-weight: 700`)
- **H2 Section Rule**: rule `,.h2` (`font-size: 1.875rem`, `line-height: 1.1`, `letter-spacing: -.025em`, `font-weight: 700`)
- **Body Copy Rule**: CSS variables `--bg-body: #1a1a1a`, `--tra-body-h: 16rem`
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1rem`, `2.25rem`, `3rem`, `3.75rem`, `4.5rem`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-3d-discovery-fr` (`3D Discovery · Exploring New Dimensions`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.header> — `www-3d-discovery-fr`)**:
   - DOM & Selectors: Landmark `<header class="header">` hosting `3D Discovery · Exploring New Dimensi` navigation (`Solutions · Expériences · Fonctionnalités · Blog`), DOM attributes (`data-theme="light"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `nter_2fe1ab3d-module__-T-KAq__cla... { font-family:Inter,Inter Fallback;font-style:normal }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.header> — `www-3d-discovery-fr`)` (`www-3d-discovery-fr`) adapts across `@media (prefers-reduced-motion:reduce)`, `@media (min-width:768px)`, `@media (min-width:1024px)`, `@media (min-width:1280px)` with `cubic-bezier(.8,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.65,0,.35,1)` transitions and links `Solutions · Expériences · Fonctionnalités · Blog`.
2. **Hero Stage & Focal Lead (<section.sg-section> — `Transformez vos lieux en experienc`)**:
   - DOM & Selectors: Landmark `<section class="sg-section">` presenting display lead `Transformez vos lieux en experiences immersives` and copy excerpt *"Planifier une démo"* over `#1a1a1a` canvas and `#ebebeb` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#1a1a1a` background with `#ebebeb` headline `Transformez vos lieux en experiences immersives`.
3. **Primary Showcase & Content Grid (<section.sg-section> — `Choisissez votre terrain`)**:
   - DOM & Selectors: Landmark `<section class="sg-section sg-section--seq">` rendering section `Choisissez votre terrain` with copy *"03 Fonctionnalités"*, asset references (`83afe278b6a6bb3c-s.p.0q-301v4kxxn...`, `c41ca59f1c34ba31-s.p.0xxb547n1hn7...`, `0ghcmdv7avfm..css`, `04vxxuqck~drg.css`), and grid rule `inter_2fe1ab3d-module__-T-KAq__va... { --font-inter:"Inter", "Inter Fallback" }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.sg-section> — `Choisissez votre terrain`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1280px`, `gap: .5rem`) on desktop and Single-column vertical stack at `390px` viewport width with `1.5rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.sg-section> — `Voir, c’est comprendre`)**:
   - DOM & Selectors: Landmark `<section class="sg-section sg-solutions">` framing `Voir, c’est comprendre` and `Planifier une démo` (*"3D Discovery · ©2026"*) with `#242424` surface cards, `#ebebeb` accents, and `sora_3fd80e00-module__HLND6q__cla... { font-family:Sora,Sora Fallback;font-style:normal }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.sg-section> — `Voir, c’est comprendre`)` uses `50%`, `999px` radii, `#ebebeb` highlights, and assets (83afe278b6a6bb3c-s.p.0q-301v4kxxn..., c41ca59f1c34ba31-s.p.0xxb547n1hn7..., 0ghcmdv7avfm..css).
5. **Colophon & Global Directory Footer (<footer.sg-footer> — `https://www.3d-discovery.fr/`)**:
   - DOM & Selectors: Landmark `<footer class="sg-footer">` anchoring `3D Discovery · Exploring New Dim` footer links (`Solutions · Expériences · Fonctionnalités · Blog`), copy *"Exploring new dimensions"*, and `#999` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.sg-footer> — `https://www.3d-discovery.fr/`)` aligns to `1280px` extracted from `www-3d-discovery-fr` stylesheet with `1.5rem` lateral canvas padding with `.5rem` grid gap and attributes (data-theme="light", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Planifier une démo"*
- Copy Excerpt 2: *"03 Fonctionnalités"*
- Copy Excerpt 3: *"3D Discovery · ©2026"*
- Copy Excerpt 4: *"Exploring new dimensions"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.8,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.65,0,.35,1)`
- **Extracted Stylesheet Rules (`www-3d-discovery-fr`)**:
- `nter_2fe1ab3d-module__-T-KAq__cla... { font-family:Inter,Inter Fallback;font-style:normal }`
- `inter_2fe1ab3d-module__-T-KAq__va... { --font-inter:"Inter", "Inter Fallback" }`
- `sora_3fd80e00-module__HLND6q__cla... { font-family:Sora,Sora Fallback;font-style:normal }`
- `.sora_3fd80e00-module__HLND6q__va... { --font-sora:"Sora", "Sora Fallback" }`
- `after { box-sizing:border-box }`
- **Per-Selector Transition Rules**:
- **Selector `:after`**: `transition: .01ms!important` extracted from `www-3d-discovery-fr` stylesheet.
- **Selector `body`**: `transition: background-color var(--transition-theme),color var(--transitio...` extracted from `www-3d-discovery-fr` stylesheet.
- **Selector `::-webkit-scrollbar-track`**: `transition: background var(--transition-theme)` extracted from `www-3d-discovery-fr` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.8,0,1,1)`)**: Governs interactive state transitions across `<header.header>` and `<section.sg-section>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-3d-discovery-fr`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
