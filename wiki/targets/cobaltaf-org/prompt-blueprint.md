---
title: "UI Prompt Blueprint: cobaltaf-org"
date: 2026-11-15
target: "cobaltaf-org"
status: analyzed
capture: dom
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#0047ba` canvas, `#f2f2f2` ink, `#e6d2ee` accent)"
---

# UI Design System & Master Generation Blueprint: cobaltaf-org

> **Cobalt Abortion Fund** (https://cobaltaf.org/) — Read privacy and digital security tips here →

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Cobalt Abortion Fund** (`https://cobaltaf.org/`). Read privacy and digital security tips here →
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#0047ba` canvas, `#f2f2f2` ink, `#e6d2ee` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#0047ba` (`var(--color-cobalt-blue)` in `:root`) paired with `#f2f2f2` primary typography and `#e6d2ee` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Poppins` for display copy (`Abortion Seekers`) with `bookmania` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `100rem` container bounds (`gap: var(--space-xs)`, padding `var(--space-m)`) with `cubic-bezier(0.23,1,0.32,1)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×7641px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `100rem` extracted from `cobaltaf-org` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--space-m)` lateral canvas padding with `var(--space-xs)` grid gap.
- **Border Radius Scale**: `4px`, `50%`, `10px`, `.4rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 100rem`, `gap: var(--space-xs)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--space-m)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:768px)`, `@media (min-width:1024px)`, `@media screen and (min-width:1024px)`, `@media (prefers-reduced-motion:reduce)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0047ba` | `var(--color-cobalt-blue)` in `:root` |
| **Primary Typography Ink** | `#132048` | `var(--color-navy-blue)` in `:root` |
| **Elevated Surface / Card Substrate** | `#c79fe5` | `var(--color-lavender)` in `:root` |
| **Interactive Accent / Highlight** | `#e6d2ee` | `var(--color-lavender-light)` in `:root` |
| **Secondary / Muted Copy** | `#f86` | `var(--color-chartreuse)` in `:root` |
| **Structural Hairline Border** | `#f2f2f2` | `var(--color-gray)` in `:root` |
| **Variable Token (`--color-white`)** | `#fff` | `var(--color-white)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-cobalt-blue` | `#0047ba` | Brand / Palette Token |
| `--color-navy-blue` | `#132048` | Brand / Palette Token |
| `--color-lavender` | `#c79fe5` | Brand / Palette Token |
| `--color-lavender-light` | `#e6d2ee` | Canvas / Surface Token |
| `--color-chartreuse` | `#f86` | Brand / Palette Token |
| `--color-gray` | `#f2f2f2` | Brand / Palette Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--anim-time` | `0.3s` | Motion / Easing Token |
| `--anim-time-long` | `0.6s` | Motion / Easing Token |
| `--anim-ease` | `ease-in` | Motion / Easing Token |
| `--container-fluid` | `100rem` | Layout / Spatial Grid Token |
| `--container` | `83rem` | Layout / Spatial Grid Token |
| `--container-small` | `76rem` | Layout / Spatial Grid Token |
| `--container-padding` | `var(--space-m)` | Layout / Spatial Grid Token |
| `--header-spacing` | `9rem` | Layout / Spatial Grid Token |
| `--font-bookmania` | `"bookmania",serif` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Poppins`.
- **Primary Body Stack**: `bookmania`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `,h1` (`font-size: clamp(2.5658rem,1.4795rem + 5...`, `font-weight: 400`).
- **Section Heading (`H2`)**: rule `,h2` (`font-size: clamp(2.0273rem,1.4553rem + 2...`, `font-weight: 500`).
- **Body Copy**: rule `p` (`line-height: inherit`).
- **Metadata & Navigation Labels**: CSS variables `--container-small: 76rem`, `--label-color: #344054`, `--label-padding: 0px 0px 5px 0px`; rule `,small` (`font-size: clamp(.8rem,.9173rem + -.1422...`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.23,1,0.32,1)`, `cubic-bezier(0.77,0,0.175,1)`, `cubic-bezier(.28,.84,.42,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.swiper-wrapper`**: `transition: ease` extracted from `cobaltaf-org` stylesheet.
- **Selector `.swiper-pagination`**: `transition: opacity .3s` extracted from `cobaltaf-org` stylesheet.
- **Selector `n-bullets-dynamic .swiper-paginat...`**: `transition: transform .2s,top .2s` extracted from `cobaltaf-org` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.23,1,0.32,1)`)**: Governs interactive state transitions across `<header.header>` and `<section.section>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Cobalt Abortion Fund                       │
│ ====================================================================== │
│ [ <header.header>          | Support · Services · Find A Clinic · R ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.section>                                    |   │
│ | H1: Abortion Seekers                                             |   │
│ | Substrate: #0047ba    | Ink: #f2f2f2    | Accent: #e6d2ee        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.section>         ) max-w: 100rem         |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Cobalt Abortion Fund provide |  | Whatever your reason is for  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<header.header>] -> [<section.section>] -> [<section.section>] |    │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>       ) | https://cobaltaf.org/              │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.header> — `cobaltaf-org`)**:
   - Landmark `<header class="header js-header">` hosting `Cobalt Abortion Fund` navigation (`Support · Services · Find A Clinic · Resources · Necesito Apoyo`), DOM attributes (`data-acsb-sr-alert="true"`, `data-acsb-sr-only="true"`, `data-acsb-force-visible="true"`, `data-acsb`), and stylesheet rule `.addtoany_content { clear:both;margin:16px auto }`.
2. **Hero Stage & Focal Lead (<section.section> — `Abortion Seekers`)**:
   - Landmark `<section class="section section-1">` presenting display lead `Abortion Seekers` and copy excerpt *"Press Option+1 for screen-reader mode, Option+0 to cancel"* over `#0047ba` canvas and `#f2f2f2` ink.
3. **Primary Showcase & Content Grid (<section.section> — `Cobalt Abortion Fund provides dire`)**:
   - Landmark `<section class="section section-2">` rendering section `Cobalt Abortion Fund provides direct financial as...` with copy *"Accessibility Screen-Reader Guide, Feedback, and Issue Reporting "*, asset references (`analytics.js`, `gtm.js`, `static.addtoany.com`, `maps.googleapis.com`), and grid rule `.addtoany_header { margin:0 0 16px }`.
4. **Interactive Detail & Feature Matrix (<section.section> — `Whatever your reason is for gettin`)**:
   - Landmark `<section class="section section-3">` framing `Whatever your reason is for getting an abortion,...` and `Our Services` (*"Read privacy and digital security tips here →"*) with `#c79fe5` surface cards, `#e6d2ee` accents, and `.addtoany_list { display:inline;line-height:16px }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://cobaltaf.org/`)**:
   - Landmark `<footer class="footer">` anchoring `Cobalt Abortion Fund` footer links (`Support · Services · Find A Clinic · Resources · Necesito Apoyo`), copy *"Lea consejos de privacidad y seguridad digital aquí →"*, and `#f2f2f2` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: cobaltaf-org (Cobalt Abortion Fund)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `cobaltaf-org` (**Cobalt Abortion Fund** — `https://cobaltaf.org/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#0047ba` canvas, `#f2f2f2` ink, `#e6d2ee` accent).
- **Identity & Domain Context**: Read privacy and digital security tips here →
- **Primary Substrate**: `#0047ba` (`var(--color-cobalt-blue)` in `:root`), **Primary Ink**: `#f2f2f2`, **Accent / Highlight**: `#e6d2ee`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#0047ba` (`var(--color-cobalt-blue)` in `:root`) paired with `#f2f2f2` primary typography and `#e6d2ee` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Poppins` for display copy (`Abortion Seekers`) with `bookmania` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `100rem` container bounds (`gap: var(--space-xs)`, padding `var(--space-m)`) with `cubic-bezier(0.23,1,0.32,1)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `cobaltaf-org` in your global stylesheet:

:root {
  /* Cobalt Abortion Fund (cobaltaf-org) — Ground-Truth Extracted CSS Variables */
  --color-cobalt-blue: #0047ba; /* Brand / Palette Token (cobaltaf-org) */
  --color-navy-blue: #132048; /* Brand / Palette Token (cobaltaf-org) */
  --color-lavender: #c79fe5; /* Brand / Palette Token (cobaltaf-org) */
  --color-lavender-light: #e6d2ee; /* Canvas / Surface Token (cobaltaf-org) */
  --color-chartreuse: #f86; /* Brand / Palette Token (cobaltaf-org) */
  --color-gray: #f2f2f2; /* Brand / Palette Token (cobaltaf-org) */
  --color-white: #fff; /* Canvas / Surface Token (cobaltaf-org) */
  --anim-time: 0.3s; /* Motion / Easing Token (cobaltaf-org) */
  --anim-time-long: 0.6s; /* Motion / Easing Token (cobaltaf-org) */
  --anim-ease: ease-in; /* Motion / Easing Token (cobaltaf-org) */
  --container-fluid: 100rem; /* Layout / Spatial Grid Token (cobaltaf-org) */
  --container: 83rem; /* Layout / Spatial Grid Token (cobaltaf-org) */
  --container-small: 76rem; /* Layout / Spatial Grid Token (cobaltaf-org) */
  --container-padding: var(--space-m); /* Layout / Spatial Grid Token (cobaltaf-org) */
  --header-spacing: 9rem; /* Layout / Spatial Grid Token (cobaltaf-org) */
  --font-bookmania: "bookmania",serif; /* Typography / Scale Token (cobaltaf-org) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#0047ba` — grounded in `var(--color-cobalt-blue)` in `:root`
- **Primary Typography Ink**: `#132048` — grounded in `var(--color-navy-blue)` in `:root`
- **Elevated Surface / Card Substrate**: `#c79fe5` — grounded in `var(--color-lavender)` in `:root`
- **Interactive Accent / Highlight**: `#e6d2ee` — grounded in `var(--color-lavender-light)` in `:root`
- **Secondary / Muted Copy**: `#f86` — grounded in `var(--color-chartreuse)` in `:root`
- **Structural Hairline Border**: `#f2f2f2` — grounded in `var(--color-gray)` in `:root`
- **Variable Token (`--color-white`)**: `#fff` — grounded in `var(--color-white)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×7641px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `100rem` extracted from `cobaltaf-org` stylesheet
- **Padding & Gutters**: `var(--space-m)` lateral canvas padding with `var(--space-xs)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 100rem`, `gap: var(--space-xs)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--space-m)` horizontal padding
- **Media Queries**: `@media (min-width:768px)`, `@media (min-width:1024px)`, `@media screen and (min-width:1024px)`, `@media (prefers-reduced-motion:reduce)`
- **Corner Radii**: `4px`, `50%`, `10px`, `.4rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Poppins`
- **Body Font Stack**: `bookmania`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: rule `,h1` (`font-size: clamp(2.5658rem,1.4795rem + 5...`, `font-weight: 400`)
- **H2 Section Rule**: rule `,h2` (`font-size: clamp(2.0273rem,1.4553rem + 2...`, `font-weight: 500`)
- **Body Copy Rule**: rule `p` (`line-height: inherit`)
- **Metadata & Index Rule**: CSS variables `--container-small: 76rem`, `--label-color: #0047ba`, `--label-padding: 0px 0px 5px 0px`; rule `,small` (`font-size: clamp(.8rem,.9173rem + -.1422...`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `cobaltaf-org` (`Cobalt Abortion Fund`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.header> — `cobaltaf-org`)**:
   - DOM & Selectors: Landmark `<header class="header js-header">` hosting `Cobalt Abortion Fund` navigation (`Support · Services · Find A Clinic · Resources · Necesito Apoyo`), DOM attributes (`data-acsb-sr-alert="true"`, `data-acsb-sr-only="true"`, `data-acsb-force-visible="true"`, `data-acsb`), and stylesheet rule `.addtoany_content { clear:both;margin:16px auto }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.header> — `cobaltaf-org`)` (`cobaltaf-org`) adapts across `@media (min-width:768px)`, `@media (min-width:1024px)`, `@media screen and (min-width:1024px)`, `@media (prefers-reduced-motion:reduce)` with `cubic-bezier(0.23,1,0.32,1)`, `cubic-bezier(0.77,0,0.175,1)`, `cubic-bezier(.28,.84,.42,1)` transitions and links `Support · Services · Find A Clinic · Resources · Necesito Apoyo`.
2. **Hero Stage & Focal Lead (<section.section> — `Abortion Seekers`)**:
   - DOM & Selectors: Landmark `<section class="section section-1">` presenting display lead `Abortion Seekers` and copy excerpt *"Press Option+1 for screen-reader mode, Option+0 to cancel"* over `#0047ba` canvas and `#f2f2f2` ink.
   - Responsive Contract: Hero stage (`1440×7641px` desktop / `390×2400px` mobile) sets `#0047ba` background with `#f2f2f2` headline `Abortion Seekers`.
3. **Primary Showcase & Content Grid (<section.section> — `Cobalt Abortion Fund provides dire`)**:
   - DOM & Selectors: Landmark `<section class="section section-2">` rendering section `Cobalt Abortion Fund provides direct financial as...` with copy *"Accessibility Screen-Reader Guide, Feedback, and Issue Reporting "*, asset references (`analytics.js`, `gtm.js`, `static.addtoany.com`, `maps.googleapis.com`), and grid rule `.addtoany_header { margin:0 0 16px }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.section> — `Cobalt Abortion Fund provides dire`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 100rem`, `gap: var(--space-xs)`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--space-m)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.section> — `Whatever your reason is for gettin`)**:
   - DOM & Selectors: Landmark `<section class="section section-3">` framing `Whatever your reason is for getting an abortion,...` and `Our Services` (*"Read privacy and digital security tips here →"*) with `#c79fe5` surface cards, `#e6d2ee` accents, and `.addtoany_list { display:inline;line-height:16px }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.section> — `Whatever your reason is for gettin`)` uses `4px`, `50%`, `10px`, `.4rem` radii, `#e6d2ee` highlights, and assets (analytics.js, gtm.js, static.addtoany.com).
5. **Colophon & Global Directory Footer (<footer.footer> — `https://cobaltaf.org/`)**:
   - DOM & Selectors: Landmark `<footer class="footer">` anchoring `Cobalt Abortion Fund` footer links (`Support · Services · Find A Clinic · Resources · Necesito Apoyo`), copy *"Lea consejos de privacidad y seguridad digital aquí →"*, and `#f2f2f2` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer> — `https://cobaltaf.org/`)` aligns to `100rem` extracted from `cobaltaf-org` stylesheet with `var(--space-m)` lateral canvas padding with `var(--space-xs)` grid gap and attributes (data-acsb-sr-alert="true", data-acsb-sr-only="true", data-acsb-force-visible="true").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Press Option+1 for screen-reader mode, Option+0 to cancel"*
- Copy Excerpt 2: *"Accessibility Screen-Reader Guide, Feedback, and Issue Reporting · New window"*
- Copy Excerpt 3: *"Read privacy and digital security tips here →"*
- Copy Excerpt 4: *"Lea consejos de privacidad y seguridad digital aquí →"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.23,1,0.32,1)`, `cubic-bezier(0.77,0,0.175,1)`, `cubic-bezier(.28,.84,.42,1)`
- **Extracted Stylesheet Rules (`cobaltaf-org`)**:
- `.addtoany_content { clear:both;margin:16px auto }`
- `.addtoany_header { margin:0 0 16px }`
- `.addtoany_list { display:inline;line-height:16px }`
- `.widget .addtoany_list a { border:0;box-shadow:none;display:inline-block;font-size:16px;padding:0 4... }`
- `.addtoany_list a img { border:0;display:inline-block;opacity:1;overflow:hidden;vertical-align:b... }`
- **Per-Selector Transition Rules**:
- **Selector `.swiper-wrapper`**: `transition: ease` extracted from `cobaltaf-org` stylesheet.
- **Selector `.swiper-pagination`**: `transition: opacity .3s` extracted from `cobaltaf-org` stylesheet.
- **Selector `n-bullets-dynamic .swiper-paginat...`**: `transition: transform .2s,top .2s` extracted from `cobaltaf-org` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.23,1,0.32,1)`)**: Governs interactive state transitions across `<header.header>` and `<section.section>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `cobaltaf-org`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
