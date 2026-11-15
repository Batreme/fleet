---
title: "UI Prompt Blueprint: plastic-ocean-com"
date: 2026-11-15
target: "plastic-ocean-com"
status: analyzed
capture: specimen
capture_desktop: specimen
capture_mobile: specimen
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#4f4f4f` accent)"
---

# UI Design System & Master Generation Blueprint: plastic-ocean-com

> **Plastic Ocean** (http://plastic-ocean.com/) — Plastic Ocean

![Desktop Design Specimen (Offline WebGL/JS Fallback — not live site capture)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Plastic Ocean** (`http://plastic-ocean.com/`). Plastic Ocean
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#4f4f4f` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--pswp-bg)` in `:root`) paired with `#fff` primary typography and `#4f4f4f` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Inter Tight` for display copy (`Plastic Ocean`) with `Host Grotesk Regular` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `991px` container bounds (`gap: 20px`, padding `20px`) with `cubic-bezier(0.4,0,0.22,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Design Specimen (Offline WebGL/JS Fallback — not live site capture)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `991px` extracted from `plastic-ocean-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `20px` lateral canvas padding with `20px` grid gap.
- **Border Radius Scale**: `5px`, `3px`, `50%`, `6px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 991px`, `gap: 20px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `20px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width: 991px)`, `@media screen and (not (max-width: 991px))`, `@media screen and (not (max-width: 479px))`, `@media (max-width: 479px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--pswp-bg)` in `:root` |
| **Primary Typography Ink** | `#222` | `var(--pswp-placeholder-bg)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff` | `var(--pswp-icon-color)` in `:root` |
| **Interactive Accent / Highlight** | `#4f4f4f` | `var(--pswp-icon-color-secondary)` in `:root` |
| **Secondary / Muted Copy** | `#ffffff` | `body { background: white }` (`#ffffff`) |
| **Structural Hairline Border** | `#000000` | `.mosaic-wrap { color: #000000 }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--default-cell-min-width` | `35px` | Layout / Spatial Grid Token |
| `--pswp-bg` | `#000` | Canvas / Surface Token |
| `--pswp-placeholder-bg` | `#222` | Canvas / Surface Token |
| `--pswp-root-z-index` | `100000` | Elevation / Border Token |
| `--pswp-preloader-color` | `rgba(79, 79, 79, 0.4)` | Brand / Palette Token |
| `--pswp-preloader-color-secondary` | `rgba(255, 255, 255, 0.9)` | Brand / Palette Token |
| `--pswp-icon-color` | `#fff` | Brand / Palette Token |
| `--pswp-icon-color-secondary` | `#4f4f4f` | Brand / Palette Token |
| `--pswp-icon-stroke-color` | `#4f4f4f` | Brand / Palette Token |
| `--pswp-icon-stroke-width` | `2px` | Layout / Spatial Grid Token |
| `--pswp-error-text-color` | `var(--pswp-icon-color)` | Typography Ink Token |
| `--custom-fade` | `1` | Design System Custom Token |
| `--webp-bottle-opacity` | `0` | Design System Custom Token |
| `--white-bg-opacity` | `1` | Canvas / Surface Token |
| `--plastic-ocean-co-bg` | `#000` | Canvas Substrate (from `var(--pswp-bg)` in `:root`) |
| `--plastic-ocean-co-ink` | `#fff` | Primary Typography Ink (stylesheet-derived) |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Inter Tight`.
- **Primary Body Stack**: `Host Grotesk Regular`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1rem`, `20px`, `1.04vw`, `3.33vw`, `1.67vw`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1rem`, `20px`, `1.04vw`, `3.33vw`, `1.67vw`).
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1rem`, `20px`, `1.04vw`, `3.33vw`, `1.67vw`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1rem`, `20px`, `1.04vw`, `3.33vw`, `1.67vw`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.4,0,0.22,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.pop-up__inside-close-button--u-i...`**: `transition: 300ms` extracted from `plastic-ocean-com` stylesheet.
- **Selector `.button--u-i04d40wq6`**: `transition: 300ms` extracted from `plastic-ocean-com` stylesheet.
- **Selector `.list--u-ioy7dxvwt`**: `transition: 300ms` extracted from `plastic-ocean-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.4,0,0.22,1)`)**: Governs interactive state transitions across `<header.wf-displayswap-n4-inactive>` and `<section.section>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Plastic Ocean                              │
│ ====================================================================== │
│ [ <header.wf-displayswap-n | get in touch · Case · Nikolai Kudriavt ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.section>                                    |   │
│ | H1: Plastic Ocean                                                |   │
│ | Substrate: #000       | Ink: #fff       | Accent: #4f4f4f        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.section>         ) max-w: 991px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Featured Work & Interactive  |  | Technical Architecture & Nar | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 20px  ) | │
│ | [<header.wf-display] -> [<section.section>] -> [<section.section>] | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.lenis-smooth> ) | http://plastic-ocean.com/          │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.wf-displayswap-n4-inactive> — `plastic-ocean-com`)**:
   - Landmark `<header class="wf-displayswap-n4-inactive">` hosting `Plastic Ocean` navigation (`get in touch · Case · Nikolai Kudriavtsev · Natalia Pugacheva · Evgeny Kuzmin`), DOM attributes (`data-size="1920x1080"`, `data-origin-src="/thumb/2/evC8fvcePJXD..."`, `data-lenis-prevent="true"`, `data-url="https://t.me/nick_kudrya"`), and stylesheet rule `.div--u-iww1jyf2k { width: 78.13vw; height: 100%; transform: translate3D(0px, 0vh, 0px); }`.
2. **Hero Stage & Focal Lead (<section.section> — `Plastic Ocean`)**:
   - Landmark `<section class="section section--u-iqub3glf6">` presenting display lead `Plastic Ocean` and copy excerpt *"This website is a non-commercial demonstration project. We do not"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.section> — `Featured Work & Interactive Showca`)**:
   - Landmark `<section class="section section--u-i8upocq6y">` rendering section `Featured Work & Interactive Showcase` with copy *"If you’re interested in this format of storytelling — get in touc"*, asset references (`tt_default_styles.css`, `design-i8z5xo3zc-1649318570_style...`, `shared-design-styles.css`, `animation-design-styles.css`), and grid rule `.text--u-ise53ezbe { opacity: 0; transform: translate3D(0px, 0px, 0px); }`.
4. **Interactive Detail & Feature Matrix (<section.section> — `Technical Architecture & Narrative`)**:
   - Landmark `<section class="section section--u-ir9wd7wkv">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Plastic pollution is often communicated through overwhelming stat"*) with `#fff` surface cards, `#4f4f4f` accents, and `.image--u-it5s3ovyb { transform: rotateX(0deg) rotateY(0deg) rotateZ(0deg) translate3D(0px, 0p... }`.
5. **Colophon & Global Directory Footer (<footer.lenis-smooth> — `http://plastic-ocean.com/`)**:
   - Landmark `<footer class="lenis-smooth">` anchoring `Plastic Ocean` footer links (`get in touch · Case · Nikolai Kudriavtsev · Natalia Pugacheva · Evgeny Kuzmin`), copy *"The vertical scroll acts as a timeline. As the user scrolls "*, and `#000000` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: plastic-ocean-com (Plastic Ocean)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `plastic-ocean-com` (**Plastic Ocean** — `http://plastic-ocean.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#4f4f4f` accent).
- **Identity & Domain Context**: Plastic Ocean
- **Primary Substrate**: `#000` (`var(--pswp-bg)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#4f4f4f`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--pswp-bg)` in `:root`) paired with `#fff` primary typography and `#4f4f4f` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Inter Tight` for display copy (`Plastic Ocean`) with `Host Grotesk Regular` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `991px` container bounds (`gap: 20px`, padding `20px`) with `cubic-bezier(0.4,0,0.22,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `plastic-ocean-com` in your global stylesheet:

:root {
  /* Plastic Ocean (plastic-ocean-com) — Ground-Truth Extracted CSS Variables */
  --default-cell-min-width: 35px; /* Layout / Spatial Grid Token (plastic-ocean-com) */
  --pswp-bg: #000; /* Canvas / Surface Token (plastic-ocean-com) */
  --pswp-placeholder-bg: #222; /* Canvas / Surface Token (plastic-ocean-com) */
  --pswp-root-z-index: 100000; /* Elevation / Border Token (plastic-ocean-com) */
  --pswp-preloader-color: rgba(79, 79, 79, 0.4); /* Brand / Palette Token (plastic-ocean-com) */
  --pswp-preloader-color-secondary: rgba(255, 255, 255, 0.9); /* Brand / Palette Token (plastic-ocean-com) */
  --pswp-icon-color: #fff; /* Brand / Palette Token (plastic-ocean-com) */
  --pswp-icon-color-secondary: #4f4f4f; /* Brand / Palette Token (plastic-ocean-com) */
  --pswp-icon-stroke-color: #4f4f4f; /* Brand / Palette Token (plastic-ocean-com) */
  --pswp-icon-stroke-width: 2px; /* Layout / Spatial Grid Token (plastic-ocean-com) */
  --pswp-error-text-color: var(--pswp-icon-color); /* Typography Ink Token (plastic-ocean-com) */
  --custom-fade: 1; /* Design System Custom Token (plastic-ocean-com) */
  --webp-bottle-opacity: 0; /* Design System Custom Token (plastic-ocean-com) */
  --white-bg-opacity: 1; /* Canvas / Surface Token (plastic-ocean-com) */
  --plastic-ocean-co-bg: #000; /* Canvas Substrate (from `var(--pswp-bg)` in `:root`) (plastic-ocean-com) */
  --plastic-ocean-co-ink: #fff; /* Primary Typography Ink (stylesheet-derived) (plastic-ocean-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000` — grounded in `var(--pswp-bg)` in `:root`
- **Primary Typography Ink**: `#222` — grounded in `var(--pswp-placeholder-bg)` in `:root`
- **Elevated Surface / Card Substrate**: `#fff` — grounded in `var(--pswp-icon-color)` in `:root`
- **Interactive Accent / Highlight**: `#4f4f4f` — grounded in `var(--pswp-icon-color-secondary)` in `:root`
- **Secondary / Muted Copy**: `#ffffff` — grounded in `body { background: white }` (`#ffffff`)
- **Structural Hairline Border**: `#000000` — grounded in `.mosaic-wrap { color: #000000 }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `991px` extracted from `plastic-ocean-com` stylesheet
- **Padding & Gutters**: `20px` lateral canvas padding with `20px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 991px`, `gap: 20px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `20px` horizontal padding
- **Media Queries**: `@media (max-width: 991px)`, `@media screen and (not (max-width: 991px))`, `@media screen and (not (max-width: 479px))`, `@media (max-width: 479px)`
- **Corner Radii**: `5px`, `3px`, `50%`, `6px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Inter Tight`
- **Body Font Stack**: `Host Grotesk Regular`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1rem`, `20px`, `1.04vw`, `3.33vw`, `1.67vw`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1rem`, `20px`, `1.04vw`, `3.33vw`, `1.67vw`)
- **Body Copy Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1rem`, `20px`, `1.04vw`, `3.33vw`, `1.67vw`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1rem`, `20px`, `1.04vw`, `3.33vw`, `1.67vw`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `plastic-ocean-com` (`Plastic Ocean`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.wf-displayswap-n4-inactive> — `plastic-ocean-com`)**:
   - DOM & Selectors: Landmark `<header class="wf-displayswap-n4-inactive">` hosting `Plastic Ocean` navigation (`get in touch · Case · Nikolai Kudriavtsev · Natalia Pugacheva · Evgeny Kuzmin`), DOM attributes (`data-size="1920x1080"`, `data-origin-src="/thumb/2/evC8fvcePJXD..."`, `data-lenis-prevent="true"`, `data-url="https://t.me/nick_kudrya"`), and stylesheet rule `.div--u-iww1jyf2k { width: 78.13vw; height: 100%; transform: translate3D(0px, 0vh, 0px); }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.wf-displayswap-n4-inactive> — `plastic-ocean-com`)` (`plastic-ocean-com`) adapts across `@media (max-width: 991px)`, `@media screen and (not (max-width: 991px))`, `@media screen and (not (max-width: 479px))`, `@media (max-width: 479px)` with `cubic-bezier(0.4,0,0.22,1)` transitions and links `get in touch · Case · Nikolai Kudriavtsev · Natalia Pugacheva · Evgeny Kuzmin`.
2. **Hero Stage & Focal Lead (<section.section> — `Plastic Ocean`)**:
   - DOM & Selectors: Landmark `<section class="section section--u-iqub3glf6">` presenting display lead `Plastic Ocean` and copy excerpt *"This website is a non-commercial demonstration project. We do not"* over `#000` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#000` background with `#fff` headline `Plastic Ocean`.
3. **Primary Showcase & Content Grid (<section.section> — `Featured Work & Interactive Showca`)**:
   - DOM & Selectors: Landmark `<section class="section section--u-i8upocq6y">` rendering section `Featured Work & Interactive Showcase` with copy *"If you’re interested in this format of storytelling — get in touc"*, asset references (`tt_default_styles.css`, `design-i8z5xo3zc-1649318570_style...`, `shared-design-styles.css`, `animation-design-styles.css`), and grid rule `.text--u-ise53ezbe { opacity: 0; transform: translate3D(0px, 0px, 0px); }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.section> — `Featured Work & Interactive Showca`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 991px`, `gap: 20px`) on desktop and Single-column vertical stack at `390px` viewport width with `20px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.section> — `Technical Architecture & Narrative`)**:
   - DOM & Selectors: Landmark `<section class="section section--u-ir9wd7wkv">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Plastic pollution is often communicated through overwhelming stat"*) with `#fff` surface cards, `#4f4f4f` accents, and `.image--u-it5s3ovyb { transform: rotateX(0deg) rotateY(0deg) rotateZ(0deg) translate3D(0px, 0p... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.section> — `Technical Architecture & Narrative`)` uses `5px`, `3px`, `50%`, `6px` radii, `#4f4f4f` highlights, and assets (tt_default_styles.css, design-i8z5xo3zc-1649318570_style..., shared-design-styles.css).
5. **Colophon & Global Directory Footer (<footer.lenis-smooth> — `http://plastic-ocean.com/`)**:
   - DOM & Selectors: Landmark `<footer class="lenis-smooth">` anchoring `Plastic Ocean` footer links (`get in touch · Case · Nikolai Kudriavtsev · Natalia Pugacheva · Evgeny Kuzmin`), copy *"The vertical scroll acts as a timeline. As the user scrolls "*, and `#000000` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.lenis-smooth> — `http://plastic-ocean.com/`)` aligns to `991px` extracted from `plastic-ocean-com` stylesheet with `20px` lateral canvas padding with `20px` grid gap and attributes (data-size="1920x1080", data-origin-src="/thumb/2/evC8fvcePJXD...", data-lenis-prevent="true").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"This website is a non-commercial demonstration project. We do not use contact form..."*
- Copy Excerpt 2: *"If you’re interested in this format of storytelling — get in touch"*
- Copy Excerpt 3: *"Plastic pollution is often communicated through overwhelming statistics. Our goal..."*
- Copy Excerpt 4: *"The vertical scroll acts as a timeline. As the user scrolls down, the bottle sinks..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.4,0,0.22,1)`
- **Extracted Stylesheet Rules (`plastic-ocean-com`)**:
- `.div--u-iww1jyf2k { width: 78.13vw; height: 100%; transform: translate3D(0px, 0vh, 0px); }`
- `.text--u-ise53ezbe { opacity: 0; transform: translate3D(0px, 0px, 0px); }`
- `.image--u-it5s3ovyb { transform: rotateX(0deg) rotateY(0deg) rotateZ(0deg) translate3D(0px, 0p... }`
- `.div--u-ia1mnlrch { width: 100vw; height: 100vh; transform: translate3D(0px, 0px, 0px); }`
- `.div--u-i6z6x9gef { width: 100vw; height: 100vh; transform: translate3D(0px, 0px, 0px); }`
- **Per-Selector Transition Rules**:
- **Selector `.pop-up__inside-close-button--u-i...`**: `transition: 300ms` extracted from `plastic-ocean-com` stylesheet.
- **Selector `.button--u-i04d40wq6`**: `transition: 300ms` extracted from `plastic-ocean-com` stylesheet.
- **Selector `.list--u-ioy7dxvwt`**: `transition: 300ms` extracted from `plastic-ocean-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.4,0,0.22,1)`)**: Governs interactive state transitions across `<header.wf-displayswap-n4-inactive>` and `<section.section>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `plastic-ocean-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
