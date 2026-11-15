---
title: "UI Prompt Blueprint: www-barebonescollective-com"
date: 2026-11-15
target: "[[overview|www-barebonescollective-com]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#0000` canvas, `#000` ink, `#333` accent)"
---

# UI Design System & Master Generation Blueprint: www-barebonescollective-com

> **Bare Bones Collective** (https://www.barebonescollective.com/) — We are a creative agency that believes great brands are built through audacious work

![Desktop Viewport Capture (1440x10637)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Bare Bones Collective** (`https://www.barebonescollective.com/`). We are a creative agency that believes great brands are built through audacious work
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#0000` canvas, `#000` ink, `#333` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#0000` (`a { background-color: #0000 }`) paired with `#000` primary typography and `#333` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Oswald` for display copy (`Bare`) with `PT Sans` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `940px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(.165,.84,.44,1)` easing and Three.js / WebGL Canvas Pipeline, Lottie Vector Animation Player.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×10637px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `940px` extracted from `www-barebonescollective-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `9px` lateral canvas padding with `16px` grid gap.
- **Border Radius Scale**: `3px`, `100%`, `50%`, `1.8rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0000` | `a { background-color: #0000 }` |
| **Primary Typography Ink** | `#000` | `mark { color: #000 }` |
| **Elevated Surface / Card Substrate** | `#ff0` | `mark { background: #ff0 }` |
| **Interactive Accent / Highlight** | `#333` | `body { color: #333 }` |
| **Secondary / Muted Copy** | `#fff` | `body { background-color: #fff }` |
| **Structural Hairline Border** | `#3898ec` | `.w-button { background-color: #3898ec }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--www-barebonescol-bg` | `#0000` | Canvas Substrate (from `a { background-color: #0000 }`) |
| `--www-barebonescol-ink` | `#000` | Primary Typography Ink (stylesheet-derived) |
| `--www-barebonescol-surface` | `#ff0` | Surface Substrate (stylesheet-derived) |
| `--www-barebonescol-accent` | `#333` | Interactive Accent (stylesheet-derived) |
| `--www-barebonescol-muted` | `#fff` | Secondary Ink (stylesheet-derived) |
| `--www-barebonescol-border` | `#3898ec` | Structural Border (stylesheet-derived) |
| `--www-barebonescol-container` | `940px` | Container Bound (stylesheet-derived) |
| `--www-barebonescol-gap` | `16px` | Grid Gutter (stylesheet-derived) |
| `--www-barebonescol-pad` | `9px` | Lateral Padding (stylesheet-derived) |
| `--www-barebonescol-ease` | `cubic-bezier(.165,.84,.44,1)` | Primary Easing Function |
| `--www-barebonescol-radius` | `3px` | Corner Radius (stylesheet-derived) |
| `--www-barebonescol-fs-base` | `2em` | Observed Font Size Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Oswald`.
- **Primary Body Stack**: `PT Sans`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 2em`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 32px`, `line-height: 36px`).
- **Body Copy**: rule `body` (`font-size: 14px`, `line-height: 20px`).
- **Metadata & Navigation Labels**: rule `small` (`font-size: 80%`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.165,.84,.44,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.w-webflow-badge > img`**: `transition: unset` extracted from `www-barebonescollective-com` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s, color .1s` extracted from `www-barebonescollective-com` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `www-barebonescollective-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.165,.84,.44,1)`)**: Governs interactive state transitions across `<header.w-mod-js>` and `<section.logo_element>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Bare Bones Collective                      │
│ ====================================================================== │
│ [ <header.w-mod-js>        | Menu · Work · Services · 360° Campaign ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.menu_element>                               |   │
│ | H1: Bare                                                         |   │
│ | Substrate: #0000      | Ink: #000       | Accent: #333           |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.logo_element>    ) max-w: 940px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Bones                        |  | COLLECTIVE                   | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px  ) | │
│ | [<header.w-mod-js>] -> [<section.menu_elem] -> [<section.logo_elem]  │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.wf-ptserif-n7-) | https://www.barebonescollective.co │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.w-mod-js> — `www-barebonescollective-com`)**:
   - Landmark `<header class="w-mod-js">` hosting `Bare Bones Collective` navigation (`Menu · Work · Services · 360° Campaigns · films`), DOM attributes (`data-wf-domain="www.barebonescollecti..."`, `data-wf-page="68358a988d15891f5e5e5ab6"`, `data-wf-site="68358a988d15891f5e5e5aad"`, `data-w-id="21dd915e-a730-31e5-d8..."`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<section.menu_element> — `Bare`)**:
   - Landmark `<section class="menu_element">` presenting display lead `Bare` and copy excerpt *"influencer campaigns"* over `#0000` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.logo_element> — `Bones`)**:
   - Landmark `<section class="logo_element">` rendering section `Bones` with copy *"hello@barebonescollective.com"*, asset references (`cdn.prod.website-files.com`, `bare-bones-collective.webflow.sha...`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.section-hero> — `COLLECTIVE`)**:
   - Landmark `<section class="section-hero">` framing `COLLECTIVE` and `CREATIVE AGENCY THAT BELIEVES GREAT BRANDS ARE BU...` (*"Bones"*) with `#ff0` surface cards, `#333` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.wf-ptserif-n7-active> — `https://www.barebonescollective.com/`)**:
   - Landmark `<footer class="wf-ptserif-n7-active">` anchoring `Bare Bones Collective` footer links (`Menu · Work · Services · 360° Campaigns · films`), copy *"COLLECTIVE"*, and `#3898ec` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-barebonescollective-com (Bare Bones Collective)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-barebonescollective-com` (**Bare Bones Collective** — `https://www.barebonescollective.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#0000` canvas, `#000` ink, `#333` accent).
- **Identity & Domain Context**: We are a creative agency that believes great brands are built through audacious work
- **Primary Substrate**: `#0000` (`a { background-color: #0000 }`), **Primary Ink**: `#000`, **Accent / Highlight**: `#333`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#0000` (`a { background-color: #0000 }`) paired with `#000` primary typography and `#333` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Oswald` for display copy (`Bare`) with `PT Sans` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `940px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(.165,.84,.44,1)` easing and Three.js / WebGL Canvas Pipeline, Lottie Vector Animation Player.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-barebonescollective-com` in your global stylesheet:

:root {
  /* Bare Bones Collective (www-barebonescollective-com) — Ground-Truth Extracted CSS Variables */
  --w-backdrop-animation: initial; /* Motion / Easing Token (www-barebonescollective-com) */
  --www-barebonescol-bg: #0000; /* Canvas Substrate (from `a { background-color: #0000 }`) (www-barebonescollective-com) */
  --www-barebonescol-ink: #000; /* Primary Typography Ink (stylesheet-derived) (www-barebonescollective-com) */
  --www-barebonescol-surface: #ff0; /* Surface Substrate (stylesheet-derived) (www-barebonescollective-com) */
  --www-barebonescol-accent: #333; /* Interactive Accent (stylesheet-derived) (www-barebonescollective-com) */
  --www-barebonescol-muted: #fff; /* Secondary Ink (stylesheet-derived) (www-barebonescollective-com) */
  --www-barebonescol-border: #3898ec; /* Structural Border (stylesheet-derived) (www-barebonescollective-com) */
  --www-barebonescol-container: 940px; /* Container Bound (stylesheet-derived) (www-barebonescollective-com) */
  --www-barebonescol-gap: 16px; /* Grid Gutter (stylesheet-derived) (www-barebonescollective-com) */
  --www-barebonescol-pad: 9px; /* Lateral Padding (stylesheet-derived) (www-barebonescollective-com) */
  --www-barebonescol-ease: cubic-bezier(.165,.84,.44,1); /* Primary Easing Function (www-barebonescollective-com) */
  --www-barebonescol-radius: 3px; /* Corner Radius (stylesheet-derived) (www-barebonescollective-com) */
  --www-barebonescol-fs-base: 2em; /* Observed Font Size Token (www-barebonescollective-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#0000` — grounded in `a { background-color: #0000 }`
- **Primary Typography Ink**: `#000` — grounded in `mark { color: #000 }`
- **Elevated Surface / Card Substrate**: `#ff0` — grounded in `mark { background: #ff0 }`
- **Interactive Accent / Highlight**: `#333` — grounded in `body { color: #333 }`
- **Secondary / Muted Copy**: `#fff` — grounded in `body { background-color: #fff }`
- **Structural Hairline Border**: `#3898ec` — grounded in `.w-button { background-color: #3898ec }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×10637px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `940px` extracted from `www-barebonescollective-com` stylesheet
- **Padding & Gutters**: `9px` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding
- **Media Queries**: `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)`
- **Corner Radii**: `3px`, `100%`, `50%`, `1.8rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Oswald`
- **Body Font Stack**: `PT Sans`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: rule `h1` (`font-size: 2em`)
- **H2 Section Rule**: rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy Rule**: rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Index Rule**: rule `small` (`font-size: 80%`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-barebonescollective-com` (`Bare Bones Collective`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.w-mod-js> — `www-barebonescollective-com`)**:
   - DOM & Selectors: Landmark `<header class="w-mod-js">` hosting `Bare Bones Collective` navigation (`Menu · Work · Services · 360° Campaigns · films`), DOM attributes (`data-wf-domain="www.barebonescollecti..."`, `data-wf-page="68358a988d15891f5e5e5ab6"`, `data-wf-site="68358a988d15891f5e5e5aad"`, `data-w-id="21dd915e-a730-31e5-d8..."`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.w-mod-js> — `www-barebonescollective-com`)` (`www-barebonescollective-com`) adapts across `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)` with `cubic-bezier(.165,.84,.44,1)` transitions and links `Menu · Work · Services · 360° Campaigns · films`.
2. **Hero Stage & Focal Lead (<section.menu_element> — `Bare`)**:
   - DOM & Selectors: Landmark `<section class="menu_element">` presenting display lead `Bare` and copy excerpt *"influencer campaigns"* over `#0000` canvas and `#000` ink.
   - Responsive Contract: Hero stage (`1440×10637px` desktop / `390×2400px` mobile) sets `#0000` background with `#000` headline `Bare`.
3. **Primary Showcase & Content Grid (<section.logo_element> — `Bones`)**:
   - DOM & Selectors: Landmark `<section class="logo_element">` rendering section `Bones` with copy *"hello@barebonescollective.com"*, asset references (`cdn.prod.website-files.com`, `bare-bones-collective.webflow.sha...`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `body { margin: 0; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.logo_element> — `Bones`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `9px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.section-hero> — `COLLECTIVE`)**:
   - DOM & Selectors: Landmark `<section class="section-hero">` framing `COLLECTIVE` and `CREATIVE AGENCY THAT BELIEVES GREAT BRANDS ARE BU...` (*"Bones"*) with `#ff0` surface cards, `#333` accents, and `summary { display: block; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.section-hero> — `COLLECTIVE`)` uses `3px`, `100%`, `50%`, `1.8rem` radii, `#333` highlights, and assets (cdn.prod.website-files.com, bare-bones-collective.webflow.sha..., fonts.googleapis.com).
5. **Colophon & Global Directory Footer (<footer.wf-ptserif-n7-active> — `https://www.barebonescollective.com/`)**:
   - DOM & Selectors: Landmark `<footer class="wf-ptserif-n7-active">` anchoring `Bare Bones Collective` footer links (`Menu · Work · Services · 360° Campaigns · films`), copy *"COLLECTIVE"*, and `#3898ec` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.wf-ptserif-n7-active> — `https://www.barebonescollective.com/`)` aligns to `940px` extracted from `www-barebonescollective-com` stylesheet with `9px` lateral canvas padding with `16px` grid gap and attributes (data-wf-domain="www.barebonescollecti...", data-wf-page="68358a988d15891f5e5e5ab6", data-wf-site="68358a988d15891f5e5e5aad").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"influencer campaigns"*
- Copy Excerpt 2: *"hello@barebonescollective.com"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.165,.84,.44,1)`
- **Extracted Stylesheet Rules (`www-barebonescollective-com`)**:
- `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`
- `body { margin: 0; }`
- `summary { display: block; }`
- `video { vertical-align: baseline; display: inline-block; }`
- `template { display: none; }`
- **Per-Selector Transition Rules**:
- **Selector `.w-webflow-badge > img`**: `transition: unset` extracted from `www-barebonescollective-com` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s, color .1s` extracted from `www-barebonescollective-com` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `www-barebonescollective-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.165,.84,.44,1)`)**: Governs interactive state transitions across `<header.w-mod-js>` and `<section.logo_element>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-barebonescollective-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
