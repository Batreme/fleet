---
title: "UI Prompt Blueprint: belgradearbor-rs_en"
date: 2026-11-15
target: "belgradearbor-rs_en"
status: analyzed
capture: specimen
capture_desktop: specimen
capture_mobile: specimen
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#fb2c36` / `#2e3a26`)"
---

# UI Design System & Master Generation Blueprint: belgradearbor-rs_en

> **Belgrade Arbor · Residential & Business Complex in New Belgrade** (https://belgradearbor.rs/en) — Discover Belgrade Arbor - premium apartments and business spaces in New Belgrade. Explore residences, amenities, location, and availability.

![Desktop Design Specimen (Offline WebGL/JS Fallback — not live site capture)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Belgrade Arbor · Residential & Business Complex in New Belgrade** (`https://belgradearbor.rs/en`). Discover Belgrade Arbor - premium apartments and business spaces in New Belgrade. Explore residences, amenities, location, and availability.
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#fb2c36` / `#2e3a26`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fb2c36` (`var(--color-red-500)` in `:root`) paired with `#fff` primary typography and `#2e3a26` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Work Sans` for display copy (`Belgrade Arbor`) with `Work Sans Fallback` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `481px` container bounds (`gap: 0px (flush layout)`, padding `0px`) with `cubic-bezier(.4,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Design Specimen (Offline WebGL/JS Fallback — not live site capture)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `481px` extracted from `belgradearbor-rs_en` stylesheet.
- **Canvas Lateral Padding & Spacing**: `0px` lateral canvas padding with `0px (flush layout)` grid gap.
- **Border Radius Scale**: `.25rem`, `1.25rem`, `1.75rem`, `var(--radius)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 481px`, `gap: 0px (flush layout)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `0px` horizontal padding.
- **Extracted CSS Media Queries**: `@media not all and (min-width:1121px)`, `@media not all and (min-width:601px)`, `@media (min-width:481px)`, `@media (min-width:601px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fb2c36` | `var(--color-red-500)` in `:root` |
| **Primary Typography Ink** | `#000` | `var(--color-black)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fdfbef` | `var(--color-vanilla)` in `:root` |
| **Interactive Accent / Highlight** | `#2e3a26` | `var(--color-pine-green)` in `:root` |
| **Secondary / Muted Copy** | `#fff` | `var(--card)` in `:root` |
| **Structural Hairline Border** | `#0a0a0a` | `var(--card-foreground)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-workSans` | `"Work Sans", "Work Sans Fallback"` | Typography / Scale Token |
| `--font-editorialOld` | `"editorialOld", "editorialOld Fallback"` | Typography / Scale Token |
| `--font-sans` | `var(--font-workSans)` | Typography / Scale Token |
| `--color-red-500` | `#fb2c36` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-lg` | `32rem` | Layout / Spatial Grid Token |
| `--container-xl` | `36rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |
| `--text-xs--line-height` | `calc(1 / .75)` | Typography Ink Token |
| `--text-sm` | `.875rem` | Typography Ink Token |
| `--text-sm--line-height` | `calc(1.25 / .875)` | Typography Ink Token |
| `--text-base` | `1rem` | Typography Ink Token |
| `--text-base--line-height` | `calc(1.5 / 1)` | Typography Ink Token |
| `--font-weight-light` | `300` | Canvas / Surface Token |
| `--font-weight-normal` | `400` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Work Sans`.
- **Primary Body Stack**: `Work Sans Fallback`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `20rem`, `10rem`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `20rem`, `10rem`).
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`.
- **Metadata & Navigation Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: cubic-bezier(.4,0,.2,1)` extracted from `belgradearbor-rs_en` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `belgradearbor-rs_en` stylesheet.
- **Selector `box-shadow\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `belgradearbor-rs_en` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<nav.mt-12>` and `<section.introduction-mobile>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Belgrade Arbor · Residential & Business Co │
│ ====================================================================== │
│ [ <nav.mt-12>              | Home Home · Business Business · Locati ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.relative>                                   |   │
│ | H1: Belgrade Arbor                                               |   │
│ | Substrate: #fb2c36    | Ink: #fff       | Accent: #2e3a26        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.introduction-mobi) max-w: 481px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | The visual identity of Belgr |  | Belgrade Arbor isn't just an | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 0px (f) | │
│ | [<nav.mt-12>] -> [<section.relative>] -> [<section.introduct] |      │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.to-vanilla>   ) | https://belgradearbor.rs/en        │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.mt-12> — `belgradearbor-rs_en`)**:
   - Landmark `<nav class="mt-12 flex">` hosting `Belgrade Arbor · Residential & Busin` navigation (`Home Home · Business Business · Location Location · Amenities Amenities · Contact Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-cookieconsent="ignore"`), and stylesheet rule `sans_5fdc899b-module__sptEXa__cla... { font-family:Work Sans,Work Sans Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.relative> — `Belgrade Arbor`)**:
   - Landmark `<section class="relative">` presenting display lead `Belgrade Arbor` and copy excerpt *"3D Experience 3D Experience"* over `#fb2c36` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.introduction-mobile> — `The visual identity of Belgrade Ar`)**:
   - Landmark `<section class="introduction-mobile relative">` rendering section `The visual identity of Belgrade Arbor is defined...` with copy *"Residences Residences"*, asset references (`0p5o.wdb6s0x3.css`, `13l3zbj81552..css`, `0eqspdm2dt5_-.css`, `00u~npbo7.a04.js`), and grid rule `sans_5fdc899b-module__sptEXa__var... { --font-workSans:"Work Sans", "Work Sans Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.relative> — `Belgrade Arbor isn't just another `)**:
   - Landmark `<section class="relative z-1">` framing `Belgrade Arbor isn't just another addition to the...` and `A N e w C h a p t e r i n P r e s t i g i o u s L...` (*"Retail Spaces Retail Spaces"*) with `#fdfbef` surface cards, `#2e3a26` accents, and `lold_a81ffa36-module__Y0KS7a__cla... { font-family:editorialOld,editorialOld Fallback }`.
5. **Colophon & Global Directory Footer (<footer.to-vanilla> — `https://belgradearbor.rs/en`)**:
   - Landmark `<footer class="to-vanilla relative">` anchoring `Belgrade Arbor · Residential & B` footer links (`Home Home · Business Business · Location Location · Amenities Amenities · Contact Contact`), copy *"Amenities Amenities"*, and `#0a0a0a` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: belgradearbor-rs_en (Belgrade Arbor · Residential & Business Complex in New Belgrade)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `belgradearbor-rs_en` (**Belgrade Arbor · Residential & Business Complex in New Belgrade** — `https://belgradearbor.rs/en`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#fb2c36` / `#2e3a26`).
- **Identity & Domain Context**: Discover Belgrade Arbor - premium apartments and business spaces in New Belgrade. Explore residences, amenities, location, and availability.
- **Primary Substrate**: `#fb2c36` (`var(--color-red-500)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#2e3a26`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fb2c36` (`var(--color-red-500)` in `:root`) paired with `#fff` primary typography and `#2e3a26` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Work Sans` for display copy (`Belgrade Arbor`) with `Work Sans Fallback` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `481px` container bounds (`gap: 0px (flush layout)`, padding `0px`) with `cubic-bezier(.4,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `belgradearbor-rs_en` in your global stylesheet:

:root {
  /* Belgrade Arbor · Residential & Business Complex in New Belgrade (belgradearbor-rs_en) — Ground-Truth Extracted CSS Variables */
  --font-workSans: "Work Sans", "Work Sans Fallback"; /* Typography / Scale Token (belgradearbor-rs_en) */
  --font-editorialOld: "editorialOld", "editorialOld Fallback"; /* Typography / Scale Token (belgradearbor-rs_en) */
  --font-sans: var(--font-workSans); /* Typography / Scale Token (belgradearbor-rs_en) */
  --color-red-500: #fb2c36; /* Brand / Palette Token (belgradearbor-rs_en) */
  --color-black: #000; /* Canvas / Surface Token (belgradearbor-rs_en) */
  --spacing: .25rem; /* Layout / Spatial Grid Token (belgradearbor-rs_en) */
  --container-lg: 32rem; /* Layout / Spatial Grid Token (belgradearbor-rs_en) */
  --container-xl: 36rem; /* Layout / Spatial Grid Token (belgradearbor-rs_en) */
  --text-xs: .75rem; /* Typography Ink Token (belgradearbor-rs_en) */
  --text-xs--line-height: calc(1 / .75); /* Typography Ink Token (belgradearbor-rs_en) */
  --text-sm: .875rem; /* Typography Ink Token (belgradearbor-rs_en) */
  --text-sm--line-height: calc(1.25 / .875); /* Typography Ink Token (belgradearbor-rs_en) */
  --text-base: 1rem; /* Typography Ink Token (belgradearbor-rs_en) */
  --text-base--line-height: calc(1.5 / 1); /* Typography Ink Token (belgradearbor-rs_en) */
  --font-weight-light: 300; /* Canvas / Surface Token (belgradearbor-rs_en) */
  --font-weight-normal: 400; /* Typography / Scale Token (belgradearbor-rs_en) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fb2c36` — grounded in `var(--color-red-500)` in `:root`
- **Primary Typography Ink**: `#000` — grounded in `var(--color-black)` in `:root`
- **Elevated Surface / Card Substrate**: `#fdfbef` — grounded in `var(--color-vanilla)` in `:root`
- **Interactive Accent / Highlight**: `#2e3a26` — grounded in `var(--color-pine-green)` in `:root`
- **Secondary / Muted Copy**: `#fff` — grounded in `var(--card)` in `:root`
- **Structural Hairline Border**: `#0a0a0a` — grounded in `var(--card-foreground)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `481px` extracted from `belgradearbor-rs_en` stylesheet
- **Padding & Gutters**: `0px` lateral canvas padding with `0px (flush layout)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 481px`, `gap: 0px (flush layout)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `0px` horizontal padding
- **Media Queries**: `@media not all and (min-width:1121px)`, `@media not all and (min-width:601px)`, `@media (min-width:481px)`, `@media (min-width:601px)`
- **Corner Radii**: `.25rem`, `1.25rem`, `1.75rem`, `var(--radius)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Work Sans`
- **Body Font Stack**: `Work Sans Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `20rem`, `10rem`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `20rem`, `10rem`)
- **Body Copy Rule**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Index Rule**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `belgradearbor-rs_en` (`Belgrade Arbor · Residential & Business Complex in New Belgrade`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.mt-12> — `belgradearbor-rs_en`)**:
   - DOM & Selectors: Landmark `<nav class="mt-12 flex">` hosting `Belgrade Arbor · Residential & Busin` navigation (`Home Home · Business Business · Location Location · Amenities Amenities · Contact Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-cookieconsent="ignore"`), and stylesheet rule `sans_5fdc899b-module__sptEXa__cla... { font-family:Work Sans,Work Sans Fallback;font-style:normal }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.mt-12> — `belgradearbor-rs_en`)` (`belgradearbor-rs_en`) adapts across `@media not all and (min-width:1121px)`, `@media not all and (min-width:601px)`, `@media (min-width:481px)`, `@media (min-width:601px)` with `cubic-bezier(.4,0,.2,1)` transitions and links `Home Home · Business Business · Location Location · Amenities Amenities · Contact Contact`.
2. **Hero Stage & Focal Lead (<section.relative> — `Belgrade Arbor`)**:
   - DOM & Selectors: Landmark `<section class="relative">` presenting display lead `Belgrade Arbor` and copy excerpt *"3D Experience 3D Experience"* over `#fb2c36` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#fb2c36` background with `#fff` headline `Belgrade Arbor`.
3. **Primary Showcase & Content Grid (<section.introduction-mobile> — `The visual identity of Belgrade Ar`)**:
   - DOM & Selectors: Landmark `<section class="introduction-mobile relative">` rendering section `The visual identity of Belgrade Arbor is defined...` with copy *"Residences Residences"*, asset references (`0p5o.wdb6s0x3.css`, `13l3zbj81552..css`, `0eqspdm2dt5_-.css`, `00u~npbo7.a04.js`), and grid rule `sans_5fdc899b-module__sptEXa__var... { --font-workSans:"Work Sans", "Work Sans Fallback" }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.introduction-mobile> — `The visual identity of Belgrade Ar`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 481px`, `gap: 0px (flush layout)`) on desktop and Single-column vertical stack at `390px` viewport width with `0px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.relative> — `Belgrade Arbor isn't just another `)**:
   - DOM & Selectors: Landmark `<section class="relative z-1">` framing `Belgrade Arbor isn't just another addition to the...` and `A N e w C h a p t e r i n P r e s t i g i o u s L...` (*"Retail Spaces Retail Spaces"*) with `#fdfbef` surface cards, `#2e3a26` accents, and `lold_a81ffa36-module__Y0KS7a__cla... { font-family:editorialOld,editorialOld Fallback }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.relative> — `Belgrade Arbor isn't just another `)` uses `.25rem`, `1.25rem`, `1.75rem`, `var(--radius)` radii, `#2e3a26` highlights, and assets (0p5o.wdb6s0x3.css, 13l3zbj81552..css, 0eqspdm2dt5_-.css).
5. **Colophon & Global Directory Footer (<footer.to-vanilla> — `https://belgradearbor.rs/en`)**:
   - DOM & Selectors: Landmark `<footer class="to-vanilla relative">` anchoring `Belgrade Arbor · Residential & B` footer links (`Home Home · Business Business · Location Location · Amenities Amenities · Contact Contact`), copy *"Amenities Amenities"*, and `#0a0a0a` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.to-vanilla> — `https://belgradearbor.rs/en`)` aligns to `481px` extracted from `belgradearbor-rs_en` stylesheet with `0px` lateral canvas padding with `0px (flush layout)` grid gap and attributes (data-precedence="next", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"3D Experience 3D Experience"*
- Copy Excerpt 2: *"Residences Residences"*
- Copy Excerpt 3: *"Retail Spaces Retail Spaces"*
- Copy Excerpt 4: *"Amenities Amenities"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`belgradearbor-rs_en`)**:
- `sans_5fdc899b-module__sptEXa__cla... { font-family:Work Sans,Work Sans Fallback;font-style:normal }`
- `sans_5fdc899b-module__sptEXa__var... { --font-workSans:"Work Sans", "Work Sans Fallback" }`
- `lold_a81ffa36-module__Y0KS7a__cla... { font-family:editorialOld,editorialOld Fallback }`
- `alold_a81ffa36-module__Y0KS7a__va... { --font-editorialOld:"editorialOld", "editorialOld Fallback" }`
- `sans_85248dc3-module__gzDsyq__cla... { font-family:Work Sans,Work Sans Fallback;font-style:normal }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: cubic-bezier(.4,0,.2,1)` extracted from `belgradearbor-rs_en` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `belgradearbor-rs_en` stylesheet.
- **Selector `box-shadow\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `belgradearbor-rs_en` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<nav.mt-12>` and `<section.introduction-mobile>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `belgradearbor-rs_en`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
