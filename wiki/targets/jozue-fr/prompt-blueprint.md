---
title: "UI Prompt Blueprint: jozue-fr"
date: 2026-11-15
target: "[[overview|jozue-fr]]"
status: analyzed
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#111319` canvas, `#fff` ink, `#dcdbdb` accent)"
---

# UI Design System & Master Generation Blueprint: jozue-fr

> **Josué Pichot, freelance art director and photographer in Paris** (https://jozue.fr) — Paris-based freelance art director, photographer, director and product designer. 15+ years in advertising and digital. Available in-house...

![Desktop Viewport Capture (1440x10664)](file:///root/projects/fleet/wiki/targets/jozue-fr/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Josué Pichot, freelance art director and photographer in Paris** (`https://jozue.fr`). Paris-based freelance art director, photographer, director and product designer. 15+ years in advertising and digital. Available in-house...
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#111319` canvas, `#fff` ink, `#dcdbdb` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#111319` (`var(--pill-bg)` in `:root`) paired with `#fff` primary typography and `#dcdbdb` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Neue Haas Grotesk Display` for display copy (`a r t d i r e c t o r + p h o t o g `) with `Helvetica Neue` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: 5rem`, padding `.4rem`) with `cubic-bezier(.4,0,1,1)` easing.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/jozue-fr/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×10664px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `40rem` extracted from `jozue-fr` stylesheet.
- **Canvas Lateral Padding & Spacing**: `.4rem` lateral canvas padding with `5rem` grid gap.
- **Border Radius Scale**: `3rem`, `1.9rem`, `2rem`, `1.1rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: 5rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `.4rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:767px)`, `@media (min-width:1024px)`, `@media (min-width:420px)`, `@media (min-width:1100px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#111319` | `var(--pill-bg)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--roll-from)` in `:root` |
| **Elevated Surface / Card Substrate** | `#050507` | `var(--intro-signature-color)` in `:root` |
| **Interactive Accent / Highlight** | `#dcdbdb` | `var(--home-j-color)` in `:root` |
| **Secondary / Muted Copy** | `#f73326` | `var(--hint-color)` in `:root` |
| **Structural Hairline Border** | `#0000` | `button { background-color: #0000 }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--paletteCount` | `5` | Brand / Palette Token |
| `--title-delay` | `var(--home-title-delay)` | Motion / Easing Token |
| `--island-side` | `1.6rem` | Dimension / Scale Token |
| `--island-bottom` | `calc(1.6rem + env(safe-area-inset-bottom,0px))` | Dimension / Scale Token |
| `--island-bar` | `5.2rem` | Dimension / Scale Token |
| `--island-r` | `2.6rem` | Dimension / Scale Token |
| `--island-fs` | `1.5rem` | Dimension / Scale Token |
| `--island-count` | `3.6rem` | Dimension / Scale Token |
| `--signature-word-y` | `-35.8%` | Dimension / Scale Token |
| `--pill-bg` | `#111319` | Canvas / Surface Token |
| `--roll-from` | `#fff` | Color / Atmospheric Token |
| `--roll-to` | `#fff` | Color / Atmospheric Token |
| `--roll-ink` | `var(--pill-bg,#111319)` | Typography Ink Token |
| `--pagination-off` | `.25` | Design System Custom Token |
| `--pagination-dot` | `.4` | Design System Custom Token |
| `--pagination-bar` | `2.8` | Design System Custom Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Neue Haas Grotesk Display`.
- **Primary Body Stack**: `Helvetica Neue`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `3.5rem`, `4.2rem`, `62.5%`, `1.6rem`, `1.5rem`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `3.5rem`, `4.2rem`, `62.5%`, `1.6rem`, `1.5rem`).
- **Body Copy**: rule `p` (`font-size: 2.3rem`, `line-height: 1.22`, `letter-spacing: .03em`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `3.5rem`, `4.2rem`, `62.5%`, `1.6rem`, `1.5rem`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0.22,0.61,0.36,1)`, `cubic-bezier(0.4,0,1,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.button-selected`**: `transition: all .3s` extracted from `jozue-fr` stylesheet.
- **Selector `.menu-toggle-bar`**: `transition: all .3s` extracted from `jozue-fr` stylesheet.
- **Selector `.menu`**: `transition: all .3s ease-in` extracted from `jozue-fr` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<nav.menu>` and `<section.js-infos>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<article.homepage>` and `<section.js-infos>` interactive targets.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Josué Pichot, freelance art director and p │
│ ====================================================================== │
│ [ <nav.menu>               | About. · Works. · Contact. · Français. ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <article.homepage>                                   |   │
│ | H1: a r t d i r e c t o r + p h o t o g r a p h e r c...         |   │
│ | Substrate: #111319    | Ink: #fff       | Accent: #dcdbdb        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.js-infos>        ) max-w: 40rem          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | selected works 18            |  | let's talk                   | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 5rem  ) | │
│ | [<nav.menu>] -> [<article.homepage>] -> [<section.js-infos>] |       │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.transi>       ) | https://jozue.fr                   │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.menu> — `jozue-fr`)**:
   - Landmark `<nav class="menu menu--site">` hosting `Josué Pichot, freelance art director` navigation (`About. · Works. · Contact. · Français.`), DOM attributes (`data-intro="done"`, `data-color="111319"`, `data-color="F73326"`, `data-title="About"`), and stylesheet rule `root { --paletteCount:5 }`.
2. **Hero Stage & Focal Lead (<article.homepage> — `a r t d i r e c t o r + p h o t o `)**:
   - Landmark `<article class="homepage">` presenting display lead `a r t d i r e c t o r + p h o t o g r a p h e r c...` and copy excerpt *"English. Français."* over `#111319` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.js-infos> — `selected works 18`)**:
   - Landmark `<section class="js-infos homepage__infos">` rendering section `selected works 18` with copy *"a r t d i r e c t o r + p h o t o g r a p h e r"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `jozue-logo-full.DpMZCk-F.svg`), and grid rule `.stop { overflow:hidden }`.
4. **Interactive Detail & Feature Matrix (<section.wrapper> — `let's talk`)**:
   - Landmark `<section class="wrapper wrapper--infos">` framing `let's talk` and `Awards & Archives` (*"a r t d i r e c t o r"*) with `#050507` surface cards, `#dcdbdb` accents, and `.transi { opacity:0;z-index:-1;width:100vw;height:100vh;display:flex;position:fixe... }`.
5. **Colophon & Global Directory Footer (<footer.transi> — `https://jozue.fr`)**:
   - Landmark `<footer class="transi">` anchoring `Josué Pichot, freelance art dire` footer links (`About. · Works. · Contact. · Français.`), copy *"+ p h o t o g r a p h e r"*, and `#0000` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: jozue-fr (Josué Pichot, freelance art director and photographer in Paris)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `jozue-fr` (**Josué Pichot, freelance art director and photographer in Paris** — `https://jozue.fr`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#111319` canvas, `#fff` ink, `#dcdbdb` accent).
- **Identity & Domain Context**: Paris-based freelance art director, photographer, director and product designer. 15+ years in advertising and digital. Available in-house...
- **Primary Substrate**: `#111319` (`var(--pill-bg)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#dcdbdb`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#111319` (`var(--pill-bg)` in `:root`) paired with `#fff` primary typography and `#dcdbdb` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Neue Haas Grotesk Display` for display copy (`a r t d i r e c t o r + p h o t o g `) with `Helvetica Neue` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: 5rem`, padding `.4rem`) with `cubic-bezier(.4,0,1,1)` easing.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `jozue-fr` in your global stylesheet:

:root {
  /* Josué Pichot, freelance art director and photographer in Paris (jozue-fr) — Ground-Truth Extracted CSS Variables */
  --paletteCount: 5; /* Brand / Palette Token (jozue-fr) */
  --title-delay: var(--home-title-delay); /* Motion / Easing Token (jozue-fr) */
  --island-side: 1.6rem; /* Dimension / Scale Token (jozue-fr) */
  --island-bottom: calc(1.6rem + env(safe-area-inset-bottom,0px)); /* Dimension / Scale Token (jozue-fr) */
  --island-bar: 5.2rem; /* Dimension / Scale Token (jozue-fr) */
  --island-r: 2.6rem; /* Dimension / Scale Token (jozue-fr) */
  --island-fs: 1.5rem; /* Dimension / Scale Token (jozue-fr) */
  --island-count: 3.6rem; /* Dimension / Scale Token (jozue-fr) */
  --signature-word-y: -35.8%; /* Dimension / Scale Token (jozue-fr) */
  --pill-bg: #111319; /* Canvas / Surface Token (jozue-fr) */
  --roll-from: #fff; /* Color / Atmospheric Token (jozue-fr) */
  --roll-to: #fff; /* Color / Atmospheric Token (jozue-fr) */
  --roll-ink: var(--pill-bg,#111319); /* Typography Ink Token (jozue-fr) */
  --pagination-off: .25; /* Design System Custom Token (jozue-fr) */
  --pagination-dot: .4; /* Design System Custom Token (jozue-fr) */
  --pagination-bar: 2.8; /* Design System Custom Token (jozue-fr) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#111319` — grounded in `var(--pill-bg)` in `:root`
- **Primary Typography Ink**: `#fff` — grounded in `var(--roll-from)` in `:root`
- **Elevated Surface / Card Substrate**: `#050507` — grounded in `var(--intro-signature-color)` in `:root`
- **Interactive Accent / Highlight**: `#dcdbdb` — grounded in `var(--home-j-color)` in `:root`
- **Secondary / Muted Copy**: `#f73326` — grounded in `var(--hint-color)` in `:root`
- **Structural Hairline Border**: `#0000` — grounded in `button { background-color: #0000 }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×10664px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `40rem` extracted from `jozue-fr` stylesheet
- **Padding & Gutters**: `.4rem` lateral canvas padding with `5rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: 5rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `.4rem` horizontal padding
- **Media Queries**: `@media (min-width:767px)`, `@media (min-width:1024px)`, `@media (min-width:420px)`, `@media (min-width:1100px)`
- **Corner Radii**: `3rem`, `1.9rem`, `2rem`, `1.1rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Neue Haas Grotesk Display`
- **Body Font Stack**: `Helvetica Neue`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `3.5rem`, `4.2rem`, `62.5%`, `1.6rem`, `1.5rem`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `3.5rem`, `4.2rem`, `62.5%`, `1.6rem`, `1.5rem`)
- **Body Copy Rule**: rule `p` (`font-size: 2.3rem`, `line-height: 1.22`, `letter-spacing: .03em`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `3.5rem`, `4.2rem`, `62.5%`, `1.6rem`, `1.5rem`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `jozue-fr` (`Josué Pichot, freelance art director and photographer in Paris`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.menu> — `jozue-fr`)**:
   - DOM & Selectors: Landmark `<nav class="menu menu--site">` hosting `Josué Pichot, freelance art director` navigation (`About. · Works. · Contact. · Français.`), DOM attributes (`data-intro="done"`, `data-color="111319"`, `data-color="F73326"`, `data-title="About"`), and stylesheet rule `root { --paletteCount:5 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.menu> — `jozue-fr`)` (`jozue-fr`) adapts across `@media (min-width:767px)`, `@media (min-width:1024px)`, `@media (min-width:420px)`, `@media (min-width:1100px)` with `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0.22,0.61,0.36,1)`, `cubic-bezier(0.4,0,1,1)` transitions and links `About. · Works. · Contact. · Français.`.
2. **Hero Stage & Focal Lead (<article.homepage> — `a r t d i r e c t o r + p h o t o `)**:
   - DOM & Selectors: Landmark `<article class="homepage">` presenting display lead `a r t d i r e c t o r + p h o t o g r a p h e r c...` and copy excerpt *"English. Français."* over `#111319` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×10664px` desktop / `390×2400px` mobile) sets `#111319` background with `#fff` headline `a r t d i r e c t o r + p h o t o g r a p h e r c...`.
3. **Primary Showcase & Content Grid (<section.js-infos> — `selected works 18`)**:
   - DOM & Selectors: Landmark `<section class="js-infos homepage__infos">` rendering section `selected works 18` with copy *"a r t d i r e c t o r + p h o t o g r a p h e r"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `jozue-logo-full.DpMZCk-F.svg`), and grid rule `.stop { overflow:hidden }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.js-infos> — `selected works 18`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: 5rem`) on desktop and Single-column vertical stack at `390px` viewport width with `.4rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.wrapper> — `let's talk`)**:
   - DOM & Selectors: Landmark `<section class="wrapper wrapper--infos">` framing `let's talk` and `Awards & Archives` (*"a r t d i r e c t o r"*) with `#050507` surface cards, `#dcdbdb` accents, and `.transi { opacity:0;z-index:-1;width:100vw;height:100vh;display:flex;position:fixe... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.wrapper> — `let's talk`)` uses `3rem`, `1.9rem`, `2rem`, `1.1rem` radii, `#dcdbdb` highlights, and assets (favicon.ico, favicon.svg, apple-touch-icon.png).
5. **Colophon & Global Directory Footer (<footer.transi> — `https://jozue.fr`)**:
   - DOM & Selectors: Landmark `<footer class="transi">` anchoring `Josué Pichot, freelance art dire` footer links (`About. · Works. · Contact. · Français.`), copy *"+ p h o t o g r a p h e r"*, and `#0000` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.transi> — `https://jozue.fr`)` aligns to `40rem` extracted from `jozue-fr` stylesheet with `.4rem` lateral canvas padding with `5rem` grid gap and attributes (data-intro="done", data-color="111319", data-color="F73326").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"English. Français."*
- Copy Excerpt 2: *"a r t d i r e c t o r + p h o t o g r a p h e r"*
- Copy Excerpt 3: *"a r t d i r e c t o r"*
- Copy Excerpt 4: *"+ p h o t o g r a p h e r"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0.22,0.61,0.36,1)`, `cubic-bezier(0.4,0,1,1)`
- **Extracted Stylesheet Rules (`jozue-fr`)**:
- `root { --paletteCount:5 }`
- `.stop { overflow:hidden }`
- `.transi { opacity:0;z-index:-1;width:100vw;height:100vh;display:flex;position:fixe... }`
- `.transi--on { z-index:100;opacity:1 }`
- `.transi-title { letter-spacing:-.03em;font-size:4.2rem }`
- **Per-Selector Transition Rules**:
- **Selector `.button-selected`**: `transition: all .3s` extracted from `jozue-fr` stylesheet.
- **Selector `.menu-toggle-bar`**: `transition: all .3s` extracted from `jozue-fr` stylesheet.
- **Selector `.menu`**: `transition: all .3s ease-in` extracted from `jozue-fr` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<nav.menu>` and `<section.js-infos>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<article.homepage>` and `<section.js-infos>` interactive targets.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `jozue-fr`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
