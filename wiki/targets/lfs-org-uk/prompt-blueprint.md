---
title: "UI Prompt Blueprint: lfs-org-uk"
date: 2026-11-15
target: "[[overview|lfs-org-uk]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#000` ink, `#30363c` accent)"
---

# UI Design System & Master Generation Blueprint: lfs-org-uk

> **London Film School** (https://lfs.org.uk/) — The oldest film school in the UK, dedicated to the education of filmmakers.

![Desktop Viewport Capture (1440x6928)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **London Film School** (`https://lfs.org.uk/`). The oldest film school in the UK, dedicated to the education of filmmakers.
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#000` ink, `#30363c` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`var(--cc-bg)` in `:root`) paired with `#000` primary typography and `#30363c` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Waldenburg Condensed Black` for display copy (`Late applications for MA Filmmaking `) with `Segoe UI` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `24rem` container bounds (`gap: .1875rem`, padding `1rem`) with `cubic-bezier(0,.658,.203,1.005)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×6928px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `24rem` extracted from `lfs-org-uk` stylesheet.
- **Canvas Lateral Padding & Spacing**: `1rem` lateral canvas padding with `.1875rem` grid gap.
- **Border Radius Scale**: `.5rem`, `.4rem`, `1rem`, `var(--cc-modal-border-radius)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 24rem`, `gap: .1875rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `1rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (width>=640px)`, `@media (prefers-reduced-motion)`, `@media screen and (width<=640px)`, `@media screen and (width>=56.25em)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--cc-bg)` in `:root` |
| **Primary Typography Ink** | `#2c2f31` | `var(--cc-primary-color)` in `:root` |
| **Elevated Surface / Card Substrate** | `#5e6266` | `var(--cc-secondary-color)` in `:root` |
| **Interactive Accent / Highlight** | `#30363c` | `var(--cc-btn-primary-bg)` in `:root` |
| **Secondary / Muted Copy** | `#000` | `var(--cc-btn-primary-hover-bg)` in `:root` |
| **Structural Hairline Border** | `#eaeff2` | `var(--cc-btn-secondary-bg)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--cc-modal-border-radius` | `.5rem` | Elevation / Border Token |
| `--cc-btn-border-radius` | `.4rem` | Elevation / Border Token |
| `--cc-modal-transition-duration` | `.25s` | Motion / Easing Token |
| `--cc-link-color` | `var(--cc-btn-primary-bg)` | Typography Ink Token |
| `--cc-modal-margin` | `1rem` | Layout / Spatial Grid Token |
| `--cc-z-index` | `2147480000` | Elevation / Border Token |
| `--cc-bg` | `#fff` | Canvas / Surface Token |
| `--cc-primary-color` | `#2c2f31` | Brand / Palette Token |
| `--cc-secondary-color` | `#5e6266` | Brand / Palette Token |
| `--cc-btn-primary-bg` | `#30363c` | Canvas / Surface Token |
| `--cc-btn-primary-color` | `#fff` | Brand / Palette Token |
| `--cc-btn-primary-border-color` | `var(--cc-btn-primary-bg)` | Brand / Palette Token |
| `--cc-btn-primary-hover-bg` | `#000` | Canvas / Surface Token |
| `--cc-btn-primary-hover-color` | `#fff` | Brand / Palette Token |
| `--cc-btn-primary-hover-border-color` | `var(--cc-btn-primary-hover-bg)` | Brand / Palette Token |
| `--cc-btn-secondary-bg` | `#eaeff2` | Canvas / Surface Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Waldenburg Condensed Black`.
- **Primary Body Stack**: `Segoe UI`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 2rem`, `line-height: 1`, `letter-spacing: -.02em`, `font-weight: 400`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 1.375rem`, `line-height: 1`, `letter-spacing: -.01em`, `font-weight: 400`).
- **Body Copy**: rule `p` (`line-height: 1.2!important`).
- **Metadata & Navigation Labels**: CSS variables `--spacing-xsmall: 1rem`, `--spacing-small: 2rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0,.658,.203,1.005)`, `cubic-bezier(.49,.78,.46,1.34)`.

### Per-Element Transition & Choreography Rules
- **Selector `:root`**: `transition: .25s` extracted from `lfs-org-uk` stylesheet.
- **Selector `#cc-main a`**: `transition: background-size .25s,color .25s` extracted from `lfs-org-uk` stylesheet.
- **Selector `media (prefers-reduced-motion)`**: `transition: 0s` extracted from `lfs-org-uk` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,.658,.203,1.005)`)**: Governs interactive state transitions across `<header.header>` and `<section.homepage-hero>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — London Film School                         │
│ ====================================================================== │
│ [ <header.header>          | Full time courses · MA Filmmaking · MA ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.menu>                                       |   │
│ | H1: Late applications for MA Filmmaking January intak...         |   │
│ | Substrate: #fff       | Ink: #000       | Accent: #30363c        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.homepage-hero>   ) max-w: 24rem          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Courses                      |  | Study at LFS                 | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .1875r) | │
│ | [<header.header>] -> [<section.menu>] -> [<section.homepage-] |      │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>       ) | https://lfs.org.uk/                │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.header> — `lfs-org-uk`)**:
   - Landmark `<header class="header js-header">` hosting `London Film School` navigation (`Full time courses · MA Filmmaking · MA Screenwriting · MA Film Marketing · MA Film Producing`), DOM attributes (`data-category="analytics"`, `data-service="Google Analytics"`, `data-category="analytics"`, `data-service="Google Analytics"`), and stylesheet rule `cc-main span { all:unset;box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.menu> — `Late applications for MA Filmmakin`)**:
   - Landmark `<section class="menu js-overlay-menu">` presenting display lead `Late applications for MA Filmmaking January intak...` and copy excerpt *"London Film School"* over `#fff` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.homepage-hero> — `Courses`)**:
   - Landmark `<section class="homepage-hero homepage-hero--announcement">` rendering section `Courses` with copy *"Full time courses MA Filmmaking MA Screenwriting MA Film Marketin"*, asset references (`recaptcha__en.js`, `favicon-96x96.png`, `favicon.svg`, `favicon.ico`), and grid rule `cc-main button { all:initial;box-sizing:border-box;color:unset;visibility:unset }`.
4. **Interactive Detail & Feature Matrix (<section.homepage-courses> — `Study at LFS`)**:
   - Landmark `<section class="homepage-courses background-grey">` framing `Study at LFS` and `About` (*"MA International Film Business"*) with `#5e6266` surface cards, `#30363c` accents, and `cc-main tr { all:revert;color:inherit;font-family:inherit;font-size:inherit;font-weig... }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://lfs.org.uk/`)**:
   - Landmark `<footer class="footer grid-container">` anchoring `London Film School` footer links (`Full time courses · MA Filmmaking · MA Screenwriting · MA Film Marketing · MA Film Producing`), copy *"Study at LFS How to apply Facilities Life in London Funding "*, and `#eaeff2` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: lfs-org-uk (London Film School)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `lfs-org-uk` (**London Film School** — `https://lfs.org.uk/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#000` ink, `#30363c` accent).
- **Identity & Domain Context**: The oldest film school in the UK, dedicated to the education of filmmakers.
- **Primary Substrate**: `#fff` (`var(--cc-bg)` in `:root`), **Primary Ink**: `#000`, **Accent / Highlight**: `#30363c`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`var(--cc-bg)` in `:root`) paired with `#000` primary typography and `#30363c` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Waldenburg Condensed Black` for display copy (`Late applications for MA Filmmaking `) with `Segoe UI` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `24rem` container bounds (`gap: .1875rem`, padding `1rem`) with `cubic-bezier(0,.658,.203,1.005)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `lfs-org-uk` in your global stylesheet:

:root {
  /* London Film School (lfs-org-uk) — Ground-Truth Extracted CSS Variables */
  --cc-modal-border-radius: .5rem; /* Elevation / Border Token (lfs-org-uk) */
  --cc-btn-border-radius: .4rem; /* Elevation / Border Token (lfs-org-uk) */
  --cc-modal-transition-duration: .25s; /* Motion / Easing Token (lfs-org-uk) */
  --cc-link-color: var(--cc-btn-primary-bg); /* Typography Ink Token (lfs-org-uk) */
  --cc-modal-margin: 1rem; /* Layout / Spatial Grid Token (lfs-org-uk) */
  --cc-z-index: 2147480000; /* Elevation / Border Token (lfs-org-uk) */
  --cc-bg: #fff; /* Canvas / Surface Token (lfs-org-uk) */
  --cc-primary-color: #2c2f31; /* Brand / Palette Token (lfs-org-uk) */
  --cc-secondary-color: #5e6266; /* Brand / Palette Token (lfs-org-uk) */
  --cc-btn-primary-bg: #30363c; /* Canvas / Surface Token (lfs-org-uk) */
  --cc-btn-primary-color: #fff; /* Brand / Palette Token (lfs-org-uk) */
  --cc-btn-primary-border-color: var(--cc-btn-primary-bg); /* Brand / Palette Token (lfs-org-uk) */
  --cc-btn-primary-hover-bg: #000; /* Canvas / Surface Token (lfs-org-uk) */
  --cc-btn-primary-hover-color: #fff; /* Brand / Palette Token (lfs-org-uk) */
  --cc-btn-primary-hover-border-color: var(--cc-btn-primary-hover-bg); /* Brand / Palette Token (lfs-org-uk) */
  --cc-btn-secondary-bg: #eaeff2; /* Canvas / Surface Token (lfs-org-uk) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fff` — grounded in `var(--cc-bg)` in `:root`
- **Primary Typography Ink**: `#2c2f31` — grounded in `var(--cc-primary-color)` in `:root`
- **Elevated Surface / Card Substrate**: `#5e6266` — grounded in `var(--cc-secondary-color)` in `:root`
- **Interactive Accent / Highlight**: `#30363c` — grounded in `var(--cc-btn-primary-bg)` in `:root`
- **Secondary / Muted Copy**: `#000` — grounded in `var(--cc-btn-primary-hover-bg)` in `:root`
- **Structural Hairline Border**: `#eaeff2` — grounded in `var(--cc-btn-secondary-bg)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×6928px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `24rem` extracted from `lfs-org-uk` stylesheet
- **Padding & Gutters**: `1rem` lateral canvas padding with `.1875rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 24rem`, `gap: .1875rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `1rem` horizontal padding
- **Media Queries**: `@media screen and (width>=640px)`, `@media (prefers-reduced-motion)`, `@media screen and (width<=640px)`, `@media screen and (width>=56.25em)`
- **Corner Radii**: `.5rem`, `.4rem`, `1rem`, `var(--cc-modal-border-radius)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Waldenburg Condensed Black`
- **Body Font Stack**: `Segoe UI`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: rule `h1` (`font-size: 2rem`, `line-height: 1`, `letter-spacing: -.02em`, `font-weight: 400`)
- **H2 Section Rule**: rule `h2` (`font-size: 1.375rem`, `line-height: 1`, `letter-spacing: -.01em`, `font-weight: 400`)
- **Body Copy Rule**: rule `p` (`line-height: 1.2!important`)
- **Metadata & Index Rule**: CSS variables `--spacing-xsmall: 1rem`, `--spacing-small: 2rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `lfs-org-uk` (`London Film School`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.header> — `lfs-org-uk`)**:
   - DOM & Selectors: Landmark `<header class="header js-header">` hosting `London Film School` navigation (`Full time courses · MA Filmmaking · MA Screenwriting · MA Film Marketing · MA Film Producing`), DOM attributes (`data-category="analytics"`, `data-service="Google Analytics"`, `data-category="analytics"`, `data-service="Google Analytics"`), and stylesheet rule `cc-main span { all:unset;box-sizing:border-box }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.header> — `lfs-org-uk`)` (`lfs-org-uk`) adapts across `@media screen and (width>=640px)`, `@media (prefers-reduced-motion)`, `@media screen and (width<=640px)`, `@media screen and (width>=56.25em)` with `cubic-bezier(0,.658,.203,1.005)`, `cubic-bezier(.49,.78,.46,1.34)` transitions and links `Full time courses · MA Filmmaking · MA Screenwriting · MA Film Marketing · MA Film Producing`.
2. **Hero Stage & Focal Lead (<section.menu> — `Late applications for MA Filmmakin`)**:
   - DOM & Selectors: Landmark `<section class="menu js-overlay-menu">` presenting display lead `Late applications for MA Filmmaking January intak...` and copy excerpt *"London Film School"* over `#fff` canvas and `#000` ink.
   - Responsive Contract: Hero stage (`1440×6928px` desktop / `390×2400px` mobile) sets `#fff` background with `#000` headline `Late applications for MA Filmmaking January intak...`.
3. **Primary Showcase & Content Grid (<section.homepage-hero> — `Courses`)**:
   - DOM & Selectors: Landmark `<section class="homepage-hero homepage-hero--announcement">` rendering section `Courses` with copy *"Full time courses MA Filmmaking MA Screenwriting MA Film Marketin"*, asset references (`recaptcha__en.js`, `favicon-96x96.png`, `favicon.svg`, `favicon.ico`), and grid rule `cc-main button { all:initial;box-sizing:border-box;color:unset;visibility:unset }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.homepage-hero> — `Courses`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 24rem`, `gap: .1875rem`) on desktop and Single-column vertical stack at `390px` viewport width with `1rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.homepage-courses> — `Study at LFS`)**:
   - DOM & Selectors: Landmark `<section class="homepage-courses background-grey">` framing `Study at LFS` and `About` (*"MA International Film Business"*) with `#5e6266` surface cards, `#30363c` accents, and `cc-main tr { all:revert;color:inherit;font-family:inherit;font-size:inherit;font-weig... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.homepage-courses> — `Study at LFS`)` uses `.5rem`, `.4rem`, `1rem`, `var(--cc-modal-border-radius)` radii, `#30363c` highlights, and assets (recaptcha__en.js, favicon-96x96.png, favicon.svg).
5. **Colophon & Global Directory Footer (<footer.footer> — `https://lfs.org.uk/`)**:
   - DOM & Selectors: Landmark `<footer class="footer grid-container">` anchoring `London Film School` footer links (`Full time courses · MA Filmmaking · MA Screenwriting · MA Film Marketing · MA Film Producing`), copy *"Study at LFS How to apply Facilities Life in London Funding "*, and `#eaeff2` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer> — `https://lfs.org.uk/`)` aligns to `24rem` extracted from `lfs-org-uk` stylesheet with `1rem` lateral canvas padding with `.1875rem` grid gap and attributes (data-category="analytics", data-service="Google Analytics", data-category="analytics").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"London Film School"*
- Copy Excerpt 2: *"Full time courses MA Filmmaking MA Screenwriting MA Film Marketing MA Film Produci..."*
- Copy Excerpt 3: *"MA International Film Business"*
- Copy Excerpt 4: *"Study at LFS How to apply Facilities Life in London Funding Ask a student"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0,.658,.203,1.005)`, `cubic-bezier(.49,.78,.46,1.34)`
- **Extracted Stylesheet Rules (`lfs-org-uk`)**:
- `cc-main span { all:unset;box-sizing:border-box }`
- `cc-main button { all:initial;box-sizing:border-box;color:unset;visibility:unset }`
- `cc-main tr { all:revert;color:inherit;font-family:inherit;font-size:inherit;font-weig... }`
- `cc-main.cc--rtl { direction:rtl }`
- `cc-main strong { font-weight:600 }`
- **Per-Selector Transition Rules**:
- **Selector `:root`**: `transition: .25s` extracted from `lfs-org-uk` stylesheet.
- **Selector `#cc-main a`**: `transition: background-size .25s,color .25s` extracted from `lfs-org-uk` stylesheet.
- **Selector `media (prefers-reduced-motion)`**: `transition: 0s` extracted from `lfs-org-uk` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,.658,.203,1.005)`)**: Governs interactive state transitions across `<header.header>` and `<section.homepage-hero>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `lfs-org-uk`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
