---
title: "UI Prompt Blueprint: productionportugal-com"
date: 2026-11-15
target: "[[overview|productionportugal-com]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#6b6d79` / `#ff0080`)"
---

# UI Design System & Master Generation Blueprint: productionportugal-com

> **Production Portugal: Your trusted film production company in Portugal an...** (https://productionportugal.com/) — Dive into cinematic excellence with expert location scouting. Explore possibilities with Production Portugal - Your Trusted film producti...

![Desktop Viewport Capture (1440x7800)](file:///root/projects/fleet/wiki/targets/productionportugal-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Production Portugal: Your trusted film production company in Portugal an...** (`https://productionportugal.com/`). Dive into cinematic excellence with expert location scouting. Explore possibilities with Production Portugal - Your Trusted film producti...
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#6b6d79` / `#ff0080`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#6b6d79` (`var(--_colours---color--grey--grey-100)` in `:root`) paired with `#a3003f` primary typography and `#ff0080` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Neue Haas Grotesk Display Pro` for display copy (`We believe happiness—ours and yours—`) with `PP Eiko Italic` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `940px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(0.4,0,0.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/productionportugal-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×7800px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `940px` extracted from `productionportugal-com` stylesheet.
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
| **Primary Canvas Substrate** | `#6b6d79` | `var(--_colours---color--grey--grey-100)` in `:root` |
| **Primary Typography Ink** | `#ff1972` | `var(--home__about__links-edge)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ff0063` | `var(--_colours---brand)` in `:root` |
| **Interactive Accent / Highlight** | `#ff0080` | `var(--base-bg)` in `:root` |
| **Secondary / Muted Copy** | `#ff126f` | `var(--blob-1)` in `:root` |
| **Structural Hairline Border** | `#a3003f` | `var(--blob-2)` in `:root` |
| **Variable Token (`--vignette`)** | `#590224d9` | `var(--vignette)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--_colours---color--grey--grey-100` | `#6b6d79` | Brand / Palette Token |
| `--home__about__links-edge` | `#ff1972` | Typography Ink Token |
| `--_colours---brand` | `#ff0063` | Brand / Palette Token |
| `--psp-stage-height` | `var(--psp-viewport-height, 100dvh) !important` | Layout / Spatial Grid Token |
| `--psp-stage-bottom-inset` | `0px !important` | Dimension / Scale Token |
| `--psp-intro-height` | `100vh` | Layout / Spatial Grid Token |
| `--base-bg` | `#ff0080` | Canvas / Surface Token |
| `--blob-1` | `#ff126f` | Color / Atmospheric Token |
| `--blob-2` | `#a3003f` | Color / Atmospheric Token |
| `--vignette` | `#590224d9` | Color / Atmospheric Token |
| `--psp-viewport-height` | `100vh` | Layout / Spatial Grid Token |
| `--home-hero-project-progress` | `0%` | Dimension / Scale Token |
| `--home-brands-project-progress` | `0%` | Brand / Palette Token |
| `--psp-hover-x` | `0px` | Dimension / Scale Token |
| `--psp-hover-y` | `0px` | Dimension / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Neue Haas Grotesk Display Pro`.
- **Primary Body Stack**: `PP Eiko Italic`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 2em`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 32px`, `line-height: 36px`).
- **Body Copy**: rule `body` (`font-size: 14px`, `line-height: 20px`).
- **Metadata & Navigation Labels**: rule `small` (`font-size: 80%`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.4,0,0.2,1)`, `cubic-bezier(0.22,1,0.36,1)`, `cubic-bezier(0.16,1,0.3,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.w-webflow-badge > img`**: `transition: unset` extracted from `productionportugal-com` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s, color .1s` extracted from `productionportugal-com` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `productionportugal-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.4,0,0.2,1)`)**: Governs interactive state transitions across `<header.header>` and `<section.home__about>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Production Portugal: Your trusted film pro │
│ ====================================================================== │
│ [ <header.header>          | [ WORK ] · [ Commercials ] · [ Long Fo ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.home__hero>                                 |   │
│ | H1: We believe happiness—ours and yours—comes from cl...         |   │
│ | Substrate: #6b6d79    | Ink: #a3003f    | Accent: #ff0080        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.home__about>     ) max-w: 940px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | ® we’re a leading Premium fu |  | Skip the Hesitation. Come Sa | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px  ) | │
│ | [<header.header>] -> [<section.home__her] -> [<section.home__abo] |  │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>       ) | https://productionportugal.com/    │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.header> — `productionportugal-com`)**:
   - Landmark `<header class="header">` hosting `Production Portugal: Your trusted fi` navigation (`[ WORK ] · [ Commercials ] · [ Long Format ] · [ DIRECTORS ] · [ CLIENTS ]`), DOM attributes (`data-wf-domain="productionportugal.com"`, `data-wf-page="69f205b2a0439779a1d74754"`, `data-wf-site="69f205b0a0439779a1d746f7"`, `data-home-intro-title="Minute Maid"`), and stylesheet rule `html.lenis body { height:auto }`.
2. **Hero Stage & Focal Lead (<section.home__hero> — `We believe happiness—ours and your`)**:
   - Landmark `<section class="home__hero">` presenting display lead `We believe happiness—ours and yours—comes from cl...` and copy excerpt *"Hinge Can't Believe We Met on Hinge"* over `#6b6d79` canvas and `#a3003f` ink.
3. **Primary Showcase & Content Grid (<section.home__about> — `® we’re a leading Premium full-sca`)**:
   - Landmark `<section class="home__about">` rendering section `® we’re a leading Premium full-scale production s...` with copy *"Xfinity - We Love To Update"*, asset references (`cdn.prod.website-files.com`, `psp-6eb01f.webflow.shared.c80d7d9...`, `6a68884496439a79375f31d1_PSP-Logo...`, `6a688844292fe50b266154c7_PSP-Logo...`), and grid rule `.lenis.lenis-stopped { overflow:clip }`.
4. **Interactive Detail & Feature Matrix (<section.home__brands> — `Skip the Hesitation. Come Say Hi`)**:
   - Landmark `<section class="home__brands">` framing `Skip the Hesitation. Come Say Hi` and `Volkswagen Abt E-Line` (*"Volkswagen Abt E-Line"*) with `#ff0063` surface cards, `#ff0080` accents, and `.lenis.lenis-smooth iframe { pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://productionportugal.com/`)**:
   - Landmark `<footer class="footer">` anchoring `Production Portugal: Your truste` footer links (`[ WORK ] · [ Commercials ] · [ Long Format ] · [ DIRECTORS ] · [ CLIENTS ]`), copy *"Uber - First Rides"*, and `#a3003f` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: productionportugal-com (Production Portugal: Your trusted film production company in Portugal an...)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `productionportugal-com` (**Production Portugal: Your trusted film production company in Portugal an...** — `https://productionportugal.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#6b6d79` / `#ff0080`).
- **Identity & Domain Context**: Dive into cinematic excellence with expert location scouting. Explore possibilities with Production Portugal - Your Trusted film producti...
- **Primary Substrate**: `#6b6d79` (`var(--_colours---color--grey--grey-100)` in `:root`), **Primary Ink**: `#a3003f`, **Accent / Highlight**: `#ff0080`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#6b6d79` (`var(--_colours---color--grey--grey-100)` in `:root`) paired with `#a3003f` primary typography and `#ff0080` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Neue Haas Grotesk Display Pro` for display copy (`We believe happiness—ours and yours—`) with `PP Eiko Italic` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `940px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(0.4,0,0.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `productionportugal-com` in your global stylesheet:

:root {
  /* Production Portugal: Your trusted film production company in Portugal an... (productionportugal-com) — Ground-Truth Extracted CSS Variables */
  --w-backdrop-animation: initial; /* Motion / Easing Token (productionportugal-com) */
  --_colours---color--grey--grey-100: #6b6d79; /* Brand / Palette Token (productionportugal-com) */
  --home__about__links-edge: #ff1972; /* Typography Ink Token (productionportugal-com) */
  --_colours---brand: #ff0063; /* Brand / Palette Token (productionportugal-com) */
  --psp-stage-height: var(--psp-viewport-height, 100dvh) !important; /* Layout / Spatial Grid Token (productionportugal-com) */
  --psp-stage-bottom-inset: 0px !important; /* Dimension / Scale Token (productionportugal-com) */
  --psp-intro-height: 100vh; /* Layout / Spatial Grid Token (productionportugal-com) */
  --base-bg: #ff0080; /* Canvas / Surface Token (productionportugal-com) */
  --blob-1: #ff126f; /* Color / Atmospheric Token (productionportugal-com) */
  --blob-2: #a3003f; /* Color / Atmospheric Token (productionportugal-com) */
  --vignette: #590224d9; /* Color / Atmospheric Token (productionportugal-com) */
  --psp-viewport-height: 100vh; /* Layout / Spatial Grid Token (productionportugal-com) */
  --home-hero-project-progress: 0%; /* Dimension / Scale Token (productionportugal-com) */
  --home-brands-project-progress: 0%; /* Brand / Palette Token (productionportugal-com) */
  --psp-hover-x: 0px; /* Dimension / Scale Token (productionportugal-com) */
  --psp-hover-y: 0px; /* Dimension / Scale Token (productionportugal-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#6b6d79` — grounded in `var(--_colours---color--grey--grey-100)` in `:root`
- **Primary Typography Ink**: `#ff1972` — grounded in `var(--home__about__links-edge)` in `:root`
- **Elevated Surface / Card Substrate**: `#ff0063` — grounded in `var(--_colours---brand)` in `:root`
- **Interactive Accent / Highlight**: `#ff0080` — grounded in `var(--base-bg)` in `:root`
- **Secondary / Muted Copy**: `#ff126f` — grounded in `var(--blob-1)` in `:root`
- **Structural Hairline Border**: `#a3003f` — grounded in `var(--blob-2)` in `:root`
- **Variable Token (`--vignette`)**: `#590224d9` — grounded in `var(--vignette)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×7800px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `940px` extracted from `productionportugal-com` stylesheet
- **Padding & Gutters**: `9px` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding
- **Media Queries**: `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)`
- **Corner Radii**: `3px`, `100%`, `50%`, `2px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Neue Haas Grotesk Display Pro`
- **Body Font Stack**: `PP Eiko Italic`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: rule `h1` (`font-size: 2em`)
- **H2 Section Rule**: rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy Rule**: rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Index Rule**: rule `small` (`font-size: 80%`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `productionportugal-com` (`Production Portugal: Your trusted film production company in Portugal an...`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.header> — `productionportugal-com`)**:
   - DOM & Selectors: Landmark `<header class="header">` hosting `Production Portugal: Your trusted fi` navigation (`[ WORK ] · [ Commercials ] · [ Long Format ] · [ DIRECTORS ] · [ CLIENTS ]`), DOM attributes (`data-wf-domain="productionportugal.com"`, `data-wf-page="69f205b2a0439779a1d74754"`, `data-wf-site="69f205b0a0439779a1d746f7"`, `data-home-intro-title="Minute Maid"`), and stylesheet rule `html.lenis body { height:auto }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.header> — `productionportugal-com`)` (`productionportugal-com`) adapts across `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)` with `cubic-bezier(0.4,0,0.2,1)`, `cubic-bezier(0.22,1,0.36,1)`, `cubic-bezier(0.16,1,0.3,1)` transitions and links `[ WORK ] · [ Commercials ] · [ Long Format ] · [ DIRECTORS ] · [ CLIENTS ]`.
2. **Hero Stage & Focal Lead (<section.home__hero> — `We believe happiness—ours and your`)**:
   - DOM & Selectors: Landmark `<section class="home__hero">` presenting display lead `We believe happiness—ours and yours—comes from cl...` and copy excerpt *"Hinge Can't Believe We Met on Hinge"* over `#6b6d79` canvas and `#a3003f` ink.
   - Responsive Contract: Hero stage (`1440×7800px` desktop / `390×2400px` mobile) sets `#6b6d79` background with `#a3003f` headline `We believe happiness—ours and yours—comes from cl...`.
3. **Primary Showcase & Content Grid (<section.home__about> — `® we’re a leading Premium full-sca`)**:
   - DOM & Selectors: Landmark `<section class="home__about">` rendering section `® we’re a leading Premium full-scale production s...` with copy *"Xfinity - We Love To Update"*, asset references (`cdn.prod.website-files.com`, `psp-6eb01f.webflow.shared.c80d7d9...`, `6a68884496439a79375f31d1_PSP-Logo...`, `6a688844292fe50b266154c7_PSP-Logo...`), and grid rule `.lenis.lenis-stopped { overflow:clip }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.home__about> — `® we’re a leading Premium full-sca`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `9px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.home__brands> — `Skip the Hesitation. Come Say Hi`)**:
   - DOM & Selectors: Landmark `<section class="home__brands">` framing `Skip the Hesitation. Come Say Hi` and `Volkswagen Abt E-Line` (*"Volkswagen Abt E-Line"*) with `#ff0063` surface cards, `#ff0080` accents, and `.lenis.lenis-smooth iframe { pointer-events:none }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.home__brands> — `Skip the Hesitation. Come Say Hi`)` uses `3px`, `100%`, `50%`, `2px` radii, `#ff0080` highlights, and assets (cdn.prod.website-files.com, psp-6eb01f.webflow.shared.c80d7d9..., 6a68884496439a79375f31d1_PSP-Logo...).
5. **Colophon & Global Directory Footer (<footer.footer> — `https://productionportugal.com/`)**:
   - DOM & Selectors: Landmark `<footer class="footer">` anchoring `Production Portugal: Your truste` footer links (`[ WORK ] · [ Commercials ] · [ Long Format ] · [ DIRECTORS ] · [ CLIENTS ]`), copy *"Uber - First Rides"*, and `#a3003f` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer> — `https://productionportugal.com/`)` aligns to `940px` extracted from `productionportugal-com` stylesheet with `9px` lateral canvas padding with `16px` grid gap and attributes (data-wf-domain="productionportugal.com", data-wf-page="69f205b2a0439779a1d74754", data-wf-site="69f205b0a0439779a1d746f7").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Hinge Can't Believe We Met on Hinge"*
- Copy Excerpt 2: *"Xfinity - We Love To Update"*
- Copy Excerpt 3: *"Volkswagen Abt E-Line"*
- Copy Excerpt 4: *"Uber - First Rides"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.4,0,0.2,1)`, `cubic-bezier(0.22,1,0.36,1)`, `cubic-bezier(0.16,1,0.3,1)`
- **Extracted Stylesheet Rules (`productionportugal-com`)**:
- `html.lenis body { height:auto }`
- `.lenis.lenis-stopped { overflow:clip }`
- `.lenis.lenis-smooth iframe { pointer-events:none }`
- `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`
- `body { margin: 0; }`
- **Per-Selector Transition Rules**:
- **Selector `.w-webflow-badge > img`**: `transition: unset` extracted from `productionportugal-com` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s, color .1s` extracted from `productionportugal-com` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `productionportugal-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.4,0,0.2,1)`)**: Governs interactive state transitions across `<header.header>` and `<section.home__about>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `productionportugal-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
