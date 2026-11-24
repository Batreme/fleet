---
title: "UI Prompt Blueprint: lenvalproperties-com"
date: 2026-11-24
captured_at: 2026-11-24
target: "lenvalproperties-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
capture_mode: behavioral_journey_v2
asset_format: webp
scroll_driver: native
desktop_keyframes: 8
subpages_crawled: 3
http_status: 200
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#211a19` / `#0082f3`)"
---

# UI Design System & Master Generation Blueprint: lenvalproperties-com

> **Lenval Properties — Creators of Refined Living & Iconic Spaces** (https://lenvalproperties.com) — Boutique residential developments in Abu Dhabi, built with intention and designed to endure.

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x1744)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Lenval Properties — Creators of Refined Living & Iconic Spaces** (`https://lenvalproperties.com`). Boutique residential developments in Abu Dhabi, built with intention and designed to endure.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#211a19` / `#0082f3`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#211a19` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#0082f3` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Financier Display` for display copy (`Creators of Refined Living & Iconic `) with `Helvetica Now Display`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 43.2px`, padding `9px`) with `cubic-bezier(0.76,0,0.24,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=12337px` / doc `13237px`), Mobile `390×1744px` (`assets/mobile-journey.webp`, `2` keyframes).
- **Master Container Bounds**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport).
- **Canvas Lateral Padding & Spacing**: `9px` lateral canvas padding with `43.2px` grid gap.
- **Border Radius Scale**: `3px`, `100%`, `50%`, `2px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 43.2px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#211a19` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#222222` | `.w-slider-nav-invert>div.w-active { background-color: #222222 }` |
| **Interactive Accent / Highlight** | `#0082f3` | `.w-dropdown-link.w--current { color: #0082f3 }` |
| **Secondary / Muted Copy** | `#f9f4ee` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#3898ec` | `.w-select:focus { border-color: #3898ec }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--_fonts---font-body` | `"Helvetica Now Display",Arial,sans-serif` | Typography / Scale Token |
| `--_colors---base-1000--primary` | `var(--_global-colors---base-1000--100)` | Brand / Palette Token |
| `--_fonts---font-display` | `"Financier Display","Times New Roman",sans-serif` | Typography / Scale Token |
| `--_fonts---h1--size` | `calc(64rem/var(--_special-units---scale-ratio))` | Typography / Scale Token |
| `--_fonts---h1--line-height` | `75%` | Typography / Scale Token |
| `--_fonts---h1--letter-spacing` | `-.032em` | Typography / Scale Token |
| `--_fonts---h2--size` | `calc(40rem/var(--_special-units---scale-ratio))` | Typography / Scale Token |
| `--_fonts---h2--line-height` | `100%` | Typography / Scale Token |
| `--_fonts---h2--letter-spacing` | `-.024em` | Typography / Scale Token |
| `--_fonts---h3--size` | `calc(16rem/var(--_special-units---scale-ratio))` | Typography / Scale Token |
| `--_fonts---h3--line-height` | `100%` | Typography / Scale Token |
| `--_fonts---h3--letter-spacing` | `0em` | Typography / Scale Token |
| `--_fonts---h4--size` | `0rem` | Typography / Scale Token |
| `--_fonts---h4--line-height` | `100%` | Typography / Scale Token |
| `--_fonts---h4--letter-spacing` | `-.048em` | Typography / Scale Token |
| `--_fonts---h5--size` | `0rem` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Financier Display`.
- **Primary Body Stack**: `Helvetica Now Display`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 57.6px`, `line-height: 43.2px`, `font-weight: 400`, `letter-spacing: -1.8432px`); CSS variables `--_fonts---font-display: "Financier Display","Times New Roman",sans-serif`, `--_fonts---h1--size: calc(64rem/var(--_special-units---scale-ratio))`, `--_fonts---h1--line-height: 75%`.
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 57.6px`, `line-height: 43.2px`, `font-weight: 400`, `letter-spacing: -1.8432px`); CSS variables `--_fonts---h2--size: calc(40rem/var(--_special-units---scale-ratio))`, `--_fonts---h2--line-height: 100%`, `--_fonts---h2--letter-spacing: -.024em`.
- **Body Copy**: live computed `body` (`font-size: 14.4px`, `line-height: 14.4px`, `font-weight: 400`); CSS variables `--_fonts---font-body: "Helvetica Now Display",Arial,sans-serif`.
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 14.4px`, `line-height: 14.4px`, `font-weight: 400`); CSS variables `--_fonts---h1--letter-spacing: -.032em`, `--_fonts---h2--letter-spacing: -.024em`, `--_fonts---h3--letter-spacing: 0em`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.76,0,0.24,1)`, `cubic-bezier(0.25,1,0.5,1)`, `cubic-bezier(0.5,0,0.75,0)`.

### Per-Element Transition & Choreography Rules
- **Selector `.w-webflow-badge>img`**: `transition: unset` extracted from `lenvalproperties-com` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s,color .1s` extracted from `lenvalproperties-com` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `lenvalproperties-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.76,0,0.24,1)`)**: Governs interactive state transitions across `<header.header>` and `<section.theme_on-dark>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Lottie Vector Animation Player, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `13237px`, deepest scrollY reached `12337px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: `Lenis`, `GSAP/ScrollTrigger`, `WebGL/Canvas`.
- **Route Transition Architecture**: First internal navigation (`/projects`) measured as `MPA` in `1093ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Lenval Properties — Creators of Refined Li │
│ ====================================================================== │
│ [ <header.header> (1440x43px)         | Overview · Index · Archive · ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.section> (w=1440px)                           | │
│ | H1: Creators of Refined Living & Iconic Spaces                     | │
│ | Substrate: #211a19 | Ink: #ffffff | Accent: #0082f3                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.theme_on-dark>) max-w: 1440px              | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Lenval develops timeless lan |  | Exceptional Exceptional Spac | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.section:nth(2)>) — Architecture for a Be   | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.section>    ) | https://lenvalproperties.com         │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 43.2px)     │
│ ====================================================================== │
│ [ HEADER BAR (<header.header>         ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.section>) — 390px Vertical Lead               | │
│ | H1: Creators of Refined Living & Iconic Spaces                     | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.theme_on-dark) — 1-Col Stack              | │
│ | [ Item 1: Lenval develops timeless landmarks shaped by arch...   ] | │
│ | [ Item 2: Exceptional Exceptional Spaces for Refined Living      ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.section:nth(2)>) — 1-Col (Architecture for a) │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.section>    ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.header> — `lenvalproperties-com`)**:
   - Landmark `<header class="header theme_on-color">` (`1440x43px`) hosting `Lenval Properties — Creators of Refi` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-wf-domain="lenvalproperties.com"`, `data-wf-page="69e0bb41d2ab22009f0e60bb"`, `data-wf-site="69e0bb41d2ab22009f0e60c1"`, `data-barba="wrapper"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.section> — `Creators of Refined Living & Iconi`)**:
   - Landmark `<section class="section theme_on-color">` presenting display lead `Creators of Refined Living & Iconic Spaces` and copy excerpt *"TO CRAFT EXCEPTIONAL PROPERTIES AND REFINED EXPERIENCES."* over `#211a19` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.theme_on-dark> — `Lenval develops timeless landmarks`)**:
   - Landmark `<section class="section theme_on-dark">` rendering section `Lenval develops timeless landmarks shaped by arch...` with copy *"Creators of Refined"*, asset references (`cdn.prod.website-files.com`, `lenvalproperties.webflow.shared.2...`, `6a8c839c1d892f3111d574bd_landscap... (This experience is designed for portr...)`, `6a8c839c1d892f3111d574bc_landscap...`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.section:nth(2)> — `Exceptional Exceptional Spaces for`)**:
   - Landmark `<section class="section theme_on-dark">` framing `Exceptional Exceptional Spaces for Refined Living` and `Architecture for a Bespoke Life` (*"s c r o l l t o e x p l o r e s c r o l l t o e x p l o r e"*) with `#222222` surface cards, `#0082f3` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.section> — `https://lenvalproperties.com`)**:
   - Landmark `<footer class="section clip">` anchoring `Lenval Properties — Creators of ` footer links (`Overview · Index · Archive · About · Contact`), copy *"Jubail Island, Abu Dhabi"*, and `#3898ec` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `Creators of Refined Living & Iconic Spaces` · sticky/fixed elements: `1`
- **Step 02** (`y=850px`, `7%`): Active landmark `Creators of Refined Living & Iconic Spaces` · sticky/fixed elements: `0`
- **Step 03** (`y=3400px`, `28%`): Active landmark `Project S` · sticky/fixed elements: `0`
- **Step 04** (`y=5100px`, `41%`): Active landmark `Project J` · sticky/fixed elements: `0`
- **Step 05** (`y=7650px`, `62%`): Active landmark `Project J` · sticky/fixed elements: `0`
- **Step 06** (`y=8955px`, `73%`): Active landmark `Architecture for a Bespoke Life` · sticky/fixed elements: `0`
- **Step 07** (`y=11900px`, `96%`): Active landmark `Footer` · sticky/fixed elements: `0`
- **Step 08** (`y=12337px`, `100%`): Active landmark `Footer` · sticky/fixed elements: `1`

### Multi-Page Internal Route Map
- **Listing Route (`/projects`)**: `https://lenvalproperties.com/projects` — H1: `projects`, scrollHeight `900px`, transition `MPA` (`1093ms`)
- **Detail Route (`/projects/project-j`)**: `https://lenvalproperties.com/projects/project-j` — H1: `Project J`, scrollHeight `13789px`, transition `direct` (`3124ms`)
- **About Route (`/about`)**: `https://lenvalproperties.com/about` — H1: `A Developer Building For Generations`, scrollHeight `6668px`, transition `direct` (`774ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: lenvalproperties-com (Lenval Properties — Creators of Refined Living & Iconic Spaces)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `lenvalproperties-com` (**Lenval Properties — Creators of Refined Living & Iconic Spaces** — `https://lenvalproperties.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#211a19` / `#0082f3`).
- **Identity & Domain Context**: Boutique residential developments in Abu Dhabi, built with intention and designed to endure.
- **Primary Substrate**: `#211a19` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#ffffff`, **Accent / Highlight**: `#0082f3`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#211a19` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#0082f3` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Financier Display` for display copy (`Creators of Refined Living & Iconic `) with `Helvetica Now Display`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 43.2px`, padding `9px`) with `cubic-bezier(0.76,0,0.24,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `lenvalproperties-com` in your global stylesheet:

:root {
  /* Lenval Properties — Creators of Refined Living & Iconic Spaces (lenvalproperties-com) — Live-Grounded CSS Variables */
  --_fonts---font-body: "Helvetica Now Display",Arial,sans-serif; /* Typography / Scale Token (lenvalproperties-com) */
  --_colors---base-1000--primary: var(--_global-colors---base-1000--100); /* Brand / Palette Token (lenvalproperties-com) */
  --_fonts---font-display: "Financier Display","Times New Roman",sans-serif; /* Typography / Scale Token (lenvalproperties-com) */
  --_fonts---h1--size: calc(64rem/var(--_special-units---scale-ratio)); /* Typography / Scale Token (lenvalproperties-com) */
  --_fonts---h1--line-height: 75%; /* Typography / Scale Token (lenvalproperties-com) */
  --_fonts---h1--letter-spacing: -.032em; /* Typography / Scale Token (lenvalproperties-com) */
  --_fonts---h2--size: calc(40rem/var(--_special-units---scale-ratio)); /* Typography / Scale Token (lenvalproperties-com) */
  --_fonts---h2--line-height: 100%; /* Typography / Scale Token (lenvalproperties-com) */
  --_fonts---h2--letter-spacing: -.024em; /* Typography / Scale Token (lenvalproperties-com) */
  --_fonts---h3--size: calc(16rem/var(--_special-units---scale-ratio)); /* Typography / Scale Token (lenvalproperties-com) */
  --_fonts---h3--line-height: 100%; /* Typography / Scale Token (lenvalproperties-com) */
  --_fonts---h3--letter-spacing: 0em; /* Typography / Scale Token (lenvalproperties-com) */
  --_fonts---h4--size: 0rem; /* Typography / Scale Token (lenvalproperties-com) */
  --_fonts---h4--line-height: 100%; /* Typography / Scale Token (lenvalproperties-com) */
  --_fonts---h4--letter-spacing: -.048em; /* Typography / Scale Token (lenvalproperties-com) */
  --_fonts---h5--size: 0rem; /* Typography / Scale Token (lenvalproperties-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#211a19` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#ffffff` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#222222` — grounded in `.w-slider-nav-invert>div.w-active { background-color: #222222 }`
- **Interactive Accent / Highlight**: `#0082f3` — grounded in `.w-dropdown-link.w--current { color: #0082f3 }`
- **Secondary / Muted Copy**: `#f9f4ee` — grounded in live computed `p` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#3898ec` — grounded in `.w-select:focus { border-color: #3898ec }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×1744px` (full-page live capture (1744px), `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport)
- **Padding & Gutters**: `9px` lateral canvas padding with `43.2px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 43.2px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding
- **Media Queries**: `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)`
- **Corner Radii**: `3px`, `100%`, `50%`, `2px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Financier Display`
- **Body Font Stack**: `Helvetica Now Display`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 57.6px`, `line-height: 43.2px`, `font-weight: 400`, `letter-spacing: -1.8432px`); CSS variables `--_fonts---font-display: "Financier Display","Times New Roman",sans-serif`, `--_fonts---h1--size: calc(64rem/var(--_special-units---scale-ratio))`, `--_fonts---h1--line-height: 75%`
- **H2 Section Rule**: live computed `h2` (`font-size: 57.6px`, `line-height: 43.2px`, `font-weight: 400`, `letter-spacing: -1.8432px`); CSS variables `--_fonts---h2--size: calc(40rem/var(--_special-units---scale-ratio))`, `--_fonts---h2--line-height: 100%`, `--_fonts---h2--letter-spacing: -.024em`
- **Body Copy Rule**: live computed `body` (`font-size: 14.4px`, `line-height: 14.4px`, `font-weight: 400`); CSS variables `--_fonts---font-body: "Helvetica Now Display",Arial,sans-serif`
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 14.4px`, `line-height: 14.4px`, `font-weight: 400`); CSS variables `--_fonts---h1--letter-spacing: -.032em`, `--_fonts---h2--letter-spacing: -.024em`, `--_fonts---h3--letter-spacing: 0em`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `lenvalproperties-com` (`Lenval Properties — Creators of Refined Living & Iconic Spaces`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.header> — `lenvalproperties-com`)**:
   - DOM & Selectors: Landmark `<header class="header theme_on-color">` (`1440x43px`) hosting `Lenval Properties — Creators of Refi` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-wf-domain="lenvalproperties.com"`, `data-wf-page="69e0bb41d2ab22009f0e60bb"`, `data-wf-site="69e0bb41d2ab22009f0e60c1"`, `data-barba="wrapper"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.header> — `lenvalproperties-com`)` (`lenvalproperties-com`) adapts across `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)` with `cubic-bezier(0.76,0,0.24,1)`, `cubic-bezier(0.25,1,0.5,1)`, `cubic-bezier(0.5,0,0.75,0)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<section.section> — `Creators of Refined Living & Iconi`)**:
   - DOM & Selectors: Landmark `<section class="section theme_on-color">` presenting display lead `Creators of Refined Living & Iconic Spaces` and copy excerpt *"TO CRAFT EXCEPTIONAL PROPERTIES AND REFINED EXPERIENCES."* over `#211a19` canvas and `#ffffff` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×1744px` mobile) sets `#211a19` background with `#ffffff` headline `Creators of Refined Living & Iconic Spaces`.
3. **Primary Showcase & Content Grid (<section.theme_on-dark> — `Lenval develops timeless landmarks`)**:
   - DOM & Selectors: Landmark `<section class="section theme_on-dark">` rendering section `Lenval develops timeless landmarks shaped by arch...` with copy *"Creators of Refined"*, asset references (`cdn.prod.website-files.com`, `lenvalproperties.webflow.shared.2...`, `6a8c839c1d892f3111d574bd_landscap... (This experience is designed for portr...)`, `6a8c839c1d892f3111d574bc_landscap...`), and grid rule `summary { display:block }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.theme_on-dark> — `Lenval develops timeless landmarks`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 43.2px`) on desktop and Single-column vertical stack at `390px` viewport width with `9px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.section:nth(2)> — `Exceptional Exceptional Spaces for`)**:
   - DOM & Selectors: Landmark `<section class="section theme_on-dark">` framing `Exceptional Exceptional Spaces for Refined Living` and `Architecture for a Bespoke Life` (*"s c r o l l t o e x p l o r e s c r o l l t o e x p l o r e"*) with `#222222` surface cards, `#0082f3` accents, and `video { vertical-align:baseline;display:inline-block }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.section:nth(2)> — `Exceptional Exceptional Spaces for`)` uses `3px`, `100%`, `50%`, `2px` radii, `#0082f3` highlights, and assets (cdn.prod.website-files.com, lenvalproperties.webflow.shared.2..., 6a8c839c1d892f3111d574bd_landscap... (This experience is designed for portr...)).
5. **Colophon & Global Directory Footer (<footer.section> — `https://lenvalproperties.com`)**:
   - DOM & Selectors: Landmark `<footer class="section clip">` anchoring `Lenval Properties — Creators of ` footer links (`Overview · Index · Archive · About · Contact`), copy *"Jubail Island, Abu Dhabi"*, and `#3898ec` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.section> — `https://lenvalproperties.com`)` aligns to `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport) with `9px` lateral canvas padding with `43.2px` grid gap and attributes (data-wf-domain="lenvalproperties.com", data-wf-page="69e0bb41d2ab22009f0e60bb", data-wf-site="69e0bb41d2ab22009f0e60c1").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"TO CRAFT EXCEPTIONAL PROPERTIES AND REFINED EXPERIENCES."*
- Copy Excerpt 2: *"Creators of Refined"*
- Copy Excerpt 3: *"s c r o l l t o e x p l o r e s c r o l l t o e x p l o r e"*
- Copy Excerpt 4: *"Jubail Island, Abu Dhabi"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.76,0,0.24,1)`, `cubic-bezier(0.25,1,0.5,1)`, `cubic-bezier(0.5,0,0.75,0)`
- **Extracted Stylesheet Rules (`lenvalproperties-com`)**:
- `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`
- `summary { display:block }`
- `video { vertical-align:baseline;display:inline-block }`
- `template { display:none }`
- `strong { font-weight:700 }`
- **Per-Selector Transition Rules**:
- **Selector `.w-webflow-badge>img`**: `transition: unset` extracted from `lenvalproperties-com` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s,color .1s` extracted from `lenvalproperties-com` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `lenvalproperties-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.76,0,0.24,1)`)**: Governs interactive state transitions across `<header.header>` and `<section.theme_on-dark>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Lottie Vector Animation Player, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `13237px` across 8 distinct viewport chapters using Lenis, GSAP/ScrollTrigger, WebGL/Canvas.
- **Vertical Chapter Sequence**: Creators of Refined Living... (0%) -> Creators of Refined Living... (7%) -> Project S (28%) -> Project J (41%) -> Project J (62%) -> Architecture for a Bespoke... (73%) -> Footer (96%) -> Footer (100%).
- **Multi-Page Routes**: Scaffold internal routes `/projects` (listing, MPA), `/projects/project-j` (detail, direct), `/about` (about, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `lenvalproperties-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | Creators of Refined Living & Iconic Spaces | `1` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `7%` | Creators of Refined Living & Iconic Spaces | `0` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `3400px` | `28%` | Project S | `0` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `5100px` | `41%` | Project J | `0` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `7650px` | `62%` | Project J | `0` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `8955px` | `73%` | Architecture for a Bespoke Life | `0` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `11900px` | `96%` | Footer | `0` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `12337px` | `100%` | Footer | `1` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | #hero | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `6870px` | `100%` | Footer / Bottom | [mobile-step-02.webp](assets/mobile-step-02.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `listing` | `https://lenvalproperties.com/projects` | projects | `900px` | `MPA` (`1093ms`) | [subpage-01-projects.webp](assets/subpage-01-projects.webp) |
| `2` | `detail` | `https://lenvalproperties.com/projects/project-j` | Project J | `13789px` | `direct` (`3124ms`) | [subpage-02-projects-project-j.webp](assets/subpage-02-projects-project-j.webp) |
| `3` | `about` | `https://lenvalproperties.com/about` | A Developer Building For Generations | `6668px` | `direct` (`774ms`) | [subpage-03-about.webp](assets/subpage-03-about.webp) |

