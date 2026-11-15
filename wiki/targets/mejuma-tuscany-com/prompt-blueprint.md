---
title: "UI Prompt Blueprint: mejuma-tuscany-com"
date: 2026-11-15
target: "[[overview|mejuma-tuscany-com]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#f1f1f1` canvas, `#38352c` ink, `#c5beb4` accent)"
---

# UI Design System & Master Generation Blueprint: mejuma-tuscany-com

> **Mejuma Tuscany** (https://mejuma-tuscany.com/) — Find your dream home in Tuscany with expert guidance. We handle property search, purchase, renovation & local coordination. Trusted turnk...

![Desktop Viewport Capture (1440x9010)](file:///root/projects/fleet/wiki/targets/mejuma-tuscany-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Mejuma Tuscany** (`https://mejuma-tuscany.com/`). Find your dream home in Tuscany with expert guidance. We handle property search, purchase, renovation & local coordination. Trusted turnk...
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#f1f1f1` canvas, `#38352c` ink, `#c5beb4` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#f1f1f1` (`var(--sand--50)` in `:root`) paired with `#38352c` primary typography and `#c5beb4` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Made Mirage` for display copy (`m e j u m a`) with `Roxale Story 400` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `940px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(.77,0,.175,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/mejuma-tuscany-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×9010px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `940px` extracted from `mejuma-tuscany-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `9px` lateral canvas padding with `16px` grid gap.
- **Border Radius Scale**: `3px`, `100%`, `50%`, `.125rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f1f1f1` | `var(--sand--50)` in `:root` |
| **Primary Typography Ink** | `#38352c` | `var(--green--950)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ffca4f` | `var(--yellow)` in `:root` |
| **Interactive Accent / Highlight** | `#c5beb4` | `var(--sand--300)` in `:root` |
| **Secondary / Muted Copy** | `#e8e4e1` | `var(--sand--100)` in `:root` |
| **Structural Hairline Border** | `#82886e` | `var(--green--600)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--sand--50` | `#f1f1f1` | Color / Atmospheric Token |
| `--green--950` | `#38352c` | Color / Atmospheric Token |
| `--yellow` | `#ffca4f` | Color / Atmospheric Token |
| `--sand--300` | `#c5beb4` | Color / Atmospheric Token |
| `--sand--100` | `#e8e4e1` | Color / Atmospheric Token |
| `--green--600` | `#82886e` | Color / Atmospheric Token |
| `--cs-color-header-action-text` | `var(--cs-color-header-action-text-hover)` | Typography Ink Token |
| `--cs-base` | `max(1rem,15px)` | Dimension / Scale Token |
| `--cs-space-1` | `calc(var(--cs-base) * .25)` | Layout / Spatial Grid Token |
| `--cs-space-2` | `calc(var(--cs-base) * .5)` | Layout / Spatial Grid Token |
| `--cs-space-3` | `calc(var(--cs-base) * .75)` | Layout / Spatial Grid Token |
| `--cs-space-4` | `calc(var(--cs-base) * 1)` | Layout / Spatial Grid Token |
| `--cs-space-5` | `calc(var(--cs-base) * 1.25)` | Layout / Spatial Grid Token |
| `--cs-space-6` | `calc(var(--cs-base) * 1.5)` | Layout / Spatial Grid Token |
| `--cs-space-7` | `calc(var(--cs-base) * 1.75)` | Layout / Spatial Grid Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Made Mirage`.
- **Primary Body Stack**: `Roxale Story 400`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 2em`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 32px`, `line-height: 36px`).
- **Body Copy**: CSS variables `--cs-font-size-body: calc(var(--cs-base) * .875)`, `--cs-font-size-body-min: 0px`, `--cs-font-weight-body: 400`; rule `body` (`font-size: 14px`, `line-height: 20px`).
- **Metadata & Navigation Labels**: CSS variables `--cs-font-weight-toggle-label: var(--cs-font-weight-medium)`; rule `small` (`font-size: 80%`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.77,0,.175,1)`, `cubic-bezier(0.65,0.05,0,1)`, `cubic-bezier(0.65,0.1,0,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.lenis.lenis-autoToggle`**: `transition: 1ms` extracted from `mejuma-tuscany-com` stylesheet.
- **Selector `.w-webflow-badge > img`**: `transition: unset` extracted from `mejuma-tuscany-com` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s, color .1s` extracted from `mejuma-tuscany-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.77,0,.175,1)`)**: Governs interactive state transitions across `<header.cs-banner__header>` and `<section.wf-golostext-n4-active>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Swiper Touch Carousel Engine, Lottie Vector Animation Player, Barba.js Page Transition Router, Locomotive Scroll Parallax with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Mejuma Tuscany                             │
│ ====================================================================== │
│ [ <header.cs-banner__heade | Overview · Index · Archive · About · C ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.js>                                         |   │
│ | H1: m e j u m a                                                  |   │
│ | Substrate: #f1f1f1    | Ink: #38352c    | Accent: #c5beb4        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.wf-golostext-n4-a) max-w: 940px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | We guide the search, purchas |  | La Valle di Semifonte        | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px  ) | │
│ | [<header.cs-banner_] -> [<section.js>] -> [<section.wf-golost] |     │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.wf-active>    ) | https://mejuma-tuscany.com/        │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.cs-banner__header> — `mejuma-tuscany-com`)**:
   - Landmark `<header class="cs-banner__header">` hosting `Mejuma Tuscany` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-wf-domain="www.mejuma-tuscany.com"`, `data-wf-page="6a71d6d6aa3293dbfd19a3b3"`, `data-wf-site="6a71d6d6aa3293dbfd19a3b7"`, `data-scroll-orientation="vertical"`), and stylesheet rule `html.lenis body { height:auto }`.
2. **Hero Stage & Focal Lead (<section.js> — `m e j u m a`)**:
   - Landmark `<section class="js">` presenting display lead `m e j u m a` and copy excerpt *"info@mejuma-tuscany.com"* over `#f1f1f1` canvas and `#38352c` ink.
3. **Primary Showcase & Content Grid (<section.wf-golostext-n4-active> — `We guide the search, purchase, ren`)**:
   - Landmark `<section class="wf-golostext-n4-active">` rendering section `We guide the search, purchase, renovation and loc...` with copy *"Discover a carefully curated selection of Tuscan homes, with pers"*, asset references (`cdn.prod.website-files.com`, `mejuma-staging.webflow.shared.777...`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `.lenis-stopped { overflow:clip }`.
4. **Interactive Detail & Feature Matrix (<section.wf-golostext-n7-active> — `La Valle di Semifonte`)**:
   - Landmark `<section class="wf-golostext-n7-active">` framing `La Valle di Semifonte` and `Dimora Montecchio` (*"Explore our properties"*) with `#ffca4f` surface cards, `#c5beb4` accents, and `.lenis.lenis-smooth iframe { pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.wf-active> — `https://mejuma-tuscany.com/`)**:
   - Landmark `<footer class="wf-active">` anchoring `Mejuma Tuscany` footer links (`Overview · Index · Archive · About · Contact`), copy *"Our mission is simple: to make buying and owning a home in T"*, and `#82886e` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: mejuma-tuscany-com (Mejuma Tuscany)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `mejuma-tuscany-com` (**Mejuma Tuscany** — `https://mejuma-tuscany.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#f1f1f1` canvas, `#38352c` ink, `#c5beb4` accent).
- **Identity & Domain Context**: Find your dream home in Tuscany with expert guidance. We handle property search, purchase, renovation & local coordination. Trusted turnk...
- **Primary Substrate**: `#f1f1f1` (`var(--sand--50)` in `:root`), **Primary Ink**: `#38352c`, **Accent / Highlight**: `#c5beb4`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#f1f1f1` (`var(--sand--50)` in `:root`) paired with `#38352c` primary typography and `#c5beb4` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Made Mirage` for display copy (`m e j u m a`) with `Roxale Story 400` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `940px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(.77,0,.175,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `mejuma-tuscany-com` in your global stylesheet:

:root {
  /* Mejuma Tuscany (mejuma-tuscany-com) — Ground-Truth Extracted CSS Variables */
  --w-backdrop-animation: initial; /* Motion / Easing Token (mejuma-tuscany-com) */
  --sand--50: #f1f1f1; /* Color / Atmospheric Token (mejuma-tuscany-com) */
  --green--950: #38352c; /* Color / Atmospheric Token (mejuma-tuscany-com) */
  --yellow: #ffca4f; /* Color / Atmospheric Token (mejuma-tuscany-com) */
  --sand--300: #c5beb4; /* Color / Atmospheric Token (mejuma-tuscany-com) */
  --sand--100: #e8e4e1; /* Color / Atmospheric Token (mejuma-tuscany-com) */
  --green--600: #82886e; /* Color / Atmospheric Token (mejuma-tuscany-com) */
  --cs-color-header-action-text: var(--cs-color-header-action-text-hover); /* Typography Ink Token (mejuma-tuscany-com) */
  --cs-base: max(1rem,15px); /* Dimension / Scale Token (mejuma-tuscany-com) */
  --cs-space-1: calc(var(--cs-base) * .25); /* Layout / Spatial Grid Token (mejuma-tuscany-com) */
  --cs-space-2: calc(var(--cs-base) * .5); /* Layout / Spatial Grid Token (mejuma-tuscany-com) */
  --cs-space-3: calc(var(--cs-base) * .75); /* Layout / Spatial Grid Token (mejuma-tuscany-com) */
  --cs-space-4: calc(var(--cs-base) * 1); /* Layout / Spatial Grid Token (mejuma-tuscany-com) */
  --cs-space-5: calc(var(--cs-base) * 1.25); /* Layout / Spatial Grid Token (mejuma-tuscany-com) */
  --cs-space-6: calc(var(--cs-base) * 1.5); /* Layout / Spatial Grid Token (mejuma-tuscany-com) */
  --cs-space-7: calc(var(--cs-base) * 1.75); /* Layout / Spatial Grid Token (mejuma-tuscany-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f1f1f1` — grounded in `var(--sand--50)` in `:root`
- **Primary Typography Ink**: `#38352c` — grounded in `var(--green--950)` in `:root`
- **Elevated Surface / Card Substrate**: `#ffca4f` — grounded in `var(--yellow)` in `:root`
- **Interactive Accent / Highlight**: `#c5beb4` — grounded in `var(--sand--300)` in `:root`
- **Secondary / Muted Copy**: `#e8e4e1` — grounded in `var(--sand--100)` in `:root`
- **Structural Hairline Border**: `#82886e` — grounded in `var(--green--600)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×9010px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `940px` extracted from `mejuma-tuscany-com` stylesheet
- **Padding & Gutters**: `9px` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding
- **Media Queries**: `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)`
- **Corner Radii**: `3px`, `100%`, `50%`, `.125rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Made Mirage`
- **Body Font Stack**: `Roxale Story 400`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: rule `h1` (`font-size: 2em`)
- **H2 Section Rule**: rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy Rule**: CSS variables `--cs-font-size-body: calc(var(--cs-base) * .875)`, `--cs-font-size-body-min: 0px`, `--cs-font-weight-body: 400`; rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Index Rule**: CSS variables `--cs-font-weight-toggle-label: var(--cs-font-weight-medium)`; rule `small` (`font-size: 80%`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `mejuma-tuscany-com` (`Mejuma Tuscany`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.cs-banner__header> — `mejuma-tuscany-com`)**:
   - DOM & Selectors: Landmark `<header class="cs-banner__header">` hosting `Mejuma Tuscany` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-wf-domain="www.mejuma-tuscany.com"`, `data-wf-page="6a71d6d6aa3293dbfd19a3b3"`, `data-wf-site="6a71d6d6aa3293dbfd19a3b7"`, `data-scroll-orientation="vertical"`), and stylesheet rule `html.lenis body { height:auto }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.cs-banner__header> — `mejuma-tuscany-com`)` (`mejuma-tuscany-com`) adapts across `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)` with `cubic-bezier(.77,0,.175,1)`, `cubic-bezier(0.65,0.05,0,1)`, `cubic-bezier(0.65,0.1,0,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<section.js> — `m e j u m a`)**:
   - DOM & Selectors: Landmark `<section class="js">` presenting display lead `m e j u m a` and copy excerpt *"info@mejuma-tuscany.com"* over `#f1f1f1` canvas and `#38352c` ink.
   - Responsive Contract: Hero stage (`1440×9010px` desktop / `390×2400px` mobile) sets `#f1f1f1` background with `#38352c` headline `m e j u m a`.
3. **Primary Showcase & Content Grid (<section.wf-golostext-n4-active> — `We guide the search, purchase, ren`)**:
   - DOM & Selectors: Landmark `<section class="wf-golostext-n4-active">` rendering section `We guide the search, purchase, renovation and loc...` with copy *"Discover a carefully curated selection of Tuscan homes, with pers"*, asset references (`cdn.prod.website-files.com`, `mejuma-staging.webflow.shared.777...`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `.lenis-stopped { overflow:clip }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.wf-golostext-n4-active> — `We guide the search, purchase, ren`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `9px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.wf-golostext-n7-active> — `La Valle di Semifonte`)**:
   - DOM & Selectors: Landmark `<section class="wf-golostext-n7-active">` framing `La Valle di Semifonte` and `Dimora Montecchio` (*"Explore our properties"*) with `#ffca4f` surface cards, `#c5beb4` accents, and `.lenis.lenis-smooth iframe { pointer-events:none }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.wf-golostext-n7-active> — `La Valle di Semifonte`)` uses `3px`, `100%`, `50%`, `.125rem` radii, `#c5beb4` highlights, and assets (cdn.prod.website-files.com, mejuma-staging.webflow.shared.777..., fonts.googleapis.com).
5. **Colophon & Global Directory Footer (<footer.wf-active> — `https://mejuma-tuscany.com/`)**:
   - DOM & Selectors: Landmark `<footer class="wf-active">` anchoring `Mejuma Tuscany` footer links (`Overview · Index · Archive · About · Contact`), copy *"Our mission is simple: to make buying and owning a home in T"*, and `#82886e` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.wf-active> — `https://mejuma-tuscany.com/`)` aligns to `940px` extracted from `mejuma-tuscany-com` stylesheet with `9px` lateral canvas padding with `16px` grid gap and attributes (data-wf-domain="www.mejuma-tuscany.com", data-wf-page="6a71d6d6aa3293dbfd19a3b3", data-wf-site="6a71d6d6aa3293dbfd19a3b7").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"info@mejuma-tuscany.com"*
- Copy Excerpt 2: *"Discover a carefully curated selection of Tuscan homes, with personal guidance eve..."*
- Copy Excerpt 3: *"Explore our properties"*
- Copy Excerpt 4: *"Our mission is simple: to make buying and owning a home in Tuscany as enjoyable as..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.77,0,.175,1)`, `cubic-bezier(0.65,0.05,0,1)`, `cubic-bezier(0.65,0.1,0,1)`
- **Extracted Stylesheet Rules (`mejuma-tuscany-com`)**:
- `html.lenis body { height:auto }`
- `.lenis-stopped { overflow:clip }`
- `.lenis.lenis-smooth iframe { pointer-events:none }`
- `.lenis.lenis-autoToggle { transition-behavior:allow-discrete;transition-duration:1ms;transition-pr... }`
- `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`
- **Per-Selector Transition Rules**:
- **Selector `.lenis.lenis-autoToggle`**: `transition: 1ms` extracted from `mejuma-tuscany-com` stylesheet.
- **Selector `.w-webflow-badge > img`**: `transition: unset` extracted from `mejuma-tuscany-com` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s, color .1s` extracted from `mejuma-tuscany-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.77,0,.175,1)`)**: Governs interactive state transitions across `<header.cs-banner__header>` and `<section.wf-golostext-n4-active>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Swiper Touch Carousel Engine, Lottie Vector Animation Player, Barba.js Page Transition Router, Locomotive Scroll Parallax with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `mejuma-tuscany-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
