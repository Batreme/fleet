---
title: "UI Prompt Blueprint: bcgbuildingdesign-com-au"
date: 2026-11-15
target: "bcgbuildingdesign-com-au"
status: analyzed
capture: specimen
capture_desktop: dom
capture_mobile: specimen
archetype: "Light-Substrate Editorial & Modular Grid System (`#f3efe8` canvas, `#1b1a18` ink, `#fffdf8` accent)"
---

# UI Design System & Master Generation Blueprint: bcgbuildingdesign-com-au

> **Building Designer Gold Coast · BCG Building Design** (https://bcgbuildingdesign.com.au/) — Boutique building design studio in Gold Coast crafting high-end custom homes and major renovations, personally led from concept to constr...

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Building Designer Gold Coast · BCG Building Design** (`https://bcgbuildingdesign.com.au/`). Boutique building design studio in Gold Coast crafting high-end custom homes and major renovations, personally led from concept to constr...
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#f3efe8` canvas, `#1b1a18` ink, `#fffdf8` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#f3efe8` (`var(--brand--beige)` in `:root`) paired with `#1b1a18` primary typography and `#fffdf8` accents.
  - **Extracted Typographic Hierarchy**: Pairs `NeueHaasDisplay Pro` for display copy (`Building Designer Gold Coast`) with `Neuehaasgrottext 65 Trial` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `940px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(0.25,0.46,0.45,0.94)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Design Specimen (Offline WebGL/JS Fallback — not live site capture)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×7439px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `940px` extracted from `bcgbuildingdesign-com-au` stylesheet.
- **Canvas Lateral Padding & Spacing**: `9px` lateral canvas padding with `16px` grid gap.
- **Border Radius Scale**: `3px`, `100%`, `50%`, `.125rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f3efe8` | `var(--brand--beige)` in `:root` |
| **Primary Typography Ink** | `#114e0b` | `var(--brand--green-darker)` in `:root` |
| **Elevated Surface / Card Substrate** | `#3a3028` | `var(--brand--brown)` in `:root` |
| **Interactive Accent / Highlight** | `#fffdf8` | `var(--neutral--white)` in `:root` |
| **Secondary / Muted Copy** | `#a9645b` | `var(--terracota)` in `:root` |
| **Structural Hairline Border** | `#1b1a18` | `var(--neutral--black)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--brand--beige` | `#f3efe8` | Brand / Palette Token |
| `--font-family--body` | `"NeueHaasDisplay Pro",Arial,sans-serif` | Typography / Scale Token |
| `--_theme---text-color--primary` | `var(--neutral--black)` | Typography Ink Token |
| `--_typography---body--body-line-height` | `var(--_typography---font-height--medium)` | Typography / Scale Token |
| `--font-weight--semi-bold` | `600` | Typography / Scale Token |
| `--_typography---body--body-letter-spacing` | `var(--_typography---letter-spacing--default)` | Typography / Scale Token |
| `--font-family--heading` | `"NeueHaasDisplay Pro",Arial,sans-serif` | Typography Ink Token |
| `--_typography---h1--h1-font-size` | `3.5rem` | Typography / Scale Token |
| `--_typography---h1--h1-line-height` | `var(--_typography---font-height--tiny)` | Typography / Scale Token |
| `--_typography---h1--h1-font-weight` | `var(--font-weight--semi-bold)` | Typography / Scale Token |
| `--_typography---h1--h1-letter-spacing` | `var(--_typography---letter-spacing--default)` | Typography / Scale Token |
| `--_typography---h2--h2-font-size` | `3em` | Typography / Scale Token |
| `--_typography---h2--h2-line-height` | `var(--_typography---font-height--medium)` | Typography / Scale Token |
| `--_typography---h2--h2-font-weight` | `var(--font-weight--bold)` | Typography / Scale Token |
| `--_typography---h2--h2-letter-spacing` | `var(--_typography---letter-spacing--default)` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `NeueHaasDisplay Pro`.
- **Primary Body Stack**: `Neuehaasgrottext 65 Trial`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--_typography---h1--h1-font-size: 3.5rem`, `--_typography---h1--h1-line-height: var(--_typography---font-height--tiny)`, `--_typography---h1--h1-font-weight: var(--font-weight--semi-bold)`.
- **Section Heading (`H2`)**: CSS variables `--_typography---h2--h2-font-size: 3em`, `--_typography---h2--h2-line-height: var(--_typography---font-height--medium)`, `--_typography---h2--h2-font-weight: var(--font-weight--bold)`.
- **Body Copy**: CSS variables `--font-family--body: "NeueHaasDisplay Pro",Arial,sans-serif`, `--_typography---body--body-line-height: var(--_typography---font-height--medium)`, `--_typography---body--body-letter-spacing: var(--_typography---letter-spacing--default)`.
- **Metadata & Navigation Labels**: CSS variables `--_typography---body--body-letter-spacing: var(--_typography---letter-spacing--default)`, `--_typography---h1--h1-letter-spacing: var(--_typography---letter-spacing--default)`, `--_typography---h2--h2-letter-spacing: var(--_typography---letter-spacing--default)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.25,0.46,0.45,0.94)`.

### Per-Element Transition & Choreography Rules
- **Selector `.w-webflow-badge>img`**: `transition: unset` extracted from `bcgbuildingdesign-com-au` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s,color .1s` extracted from `bcgbuildingdesign-com-au` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `bcgbuildingdesign-com-au` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.25,0.46,0.45,0.94)`)**: Governs interactive state transitions across `<nav.navbar>` and `<section.section>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Building Designer Gold Coast · BCG Buildin │
│ ====================================================================== │
│ [ <nav.navbar>             | Home · Studio · Process · Projects · P ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.section>                                    |   │
│ | H1: Building Designer Gold Coast                                 |   │
│ | Substrate: #f3efe8    | Ink: #1b1a18    | Accent: #fffdf8        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.section>         ) max-w: 940px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Designing beautiful homes th |  | Our Studio                   | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px  ) | │
│ | [<nav.navbar>] -> [<section.section>] -> [<section.section>] |       │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.section_footer) | https://bcgbuildingdesign.com.au/  │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.navbar> — `bcgbuildingdesign-com-au`)**:
   - Landmark `<nav class="navbar">` hosting `Building Designer Gold Coast · BCG B` navigation (`Home · Studio · Process · Projects · Project Enquiry`), DOM attributes (`data-wf-domain="www.bcgbuildingdesign..."`, `data-wf-page="6a794e5aeebba97e3ac774a5"`, `data-wf-site="6a794e5aeebba97e3ac774ae"`, `data-barba="wrapper"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.section> — `Building Designer Gold Coast`)**:
   - Landmark `<section class="section is-relative">` presenting display lead `Building Designer Gold Coast` and copy excerpt *"BCG is a boutique building design studio based on the Gold Coast,"* over `#f3efe8` canvas and `#1b1a18` ink.
3. **Primary Showcase & Content Grid (<section.section> — `Designing beautiful homes that wor`)**:
   - Landmark `<section class="section is-sticky">` rendering section `Designing beautiful homes that work as well as th...` with copy *"Learn More Learn More"*, asset references (`cdn.prod.website-files.com`, `bcg-staging.webflow.shared.4c5b11...`, `gtm.js`, `recaptcha__en.js`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.section-brown> — `Our Studio`)**:
   - Landmark `<section class="section-brown">` framing `Our Studio` and `Every considered home begins with a considered ap...` (*"Designing an enduring home is only half the job. The other half i"*) with `#3a3028` surface cards, `#fffdf8` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.section_footer> — `https://bcgbuildingdesign.com.au/`)**:
   - Landmark `<footer class="section_footer">` anchoring `Building Designer Gold Coast · B` footer links (`Home · Studio · Process · Projects · Project Enquiry`), copy *"We’ve had a great experience with BCG designs. We approached"*, and `#1b1a18` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: bcgbuildingdesign-com-au (Building Designer Gold Coast · BCG Building Design)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `bcgbuildingdesign-com-au` (**Building Designer Gold Coast · BCG Building Design** — `https://bcgbuildingdesign.com.au/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#f3efe8` canvas, `#1b1a18` ink, `#fffdf8` accent).
- **Identity & Domain Context**: Boutique building design studio in Gold Coast crafting high-end custom homes and major renovations, personally led from concept to constr...
- **Primary Substrate**: `#f3efe8` (`var(--brand--beige)` in `:root`), **Primary Ink**: `#1b1a18`, **Accent / Highlight**: `#fffdf8`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#f3efe8` (`var(--brand--beige)` in `:root`) paired with `#1b1a18` primary typography and `#fffdf8` accents.
  - **Extracted Typographic Hierarchy**: Pairs `NeueHaasDisplay Pro` for display copy (`Building Designer Gold Coast`) with `Neuehaasgrottext 65 Trial` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `940px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(0.25,0.46,0.45,0.94)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `bcgbuildingdesign-com-au` in your global stylesheet:

:root {
  /* Building Designer Gold Coast · BCG Building Design (bcgbuildingdesign-com-au) — Ground-Truth Extracted CSS Variables */
  --w-backdrop-animation: initial; /* Motion / Easing Token (bcgbuildingdesign-com-au) */
  --brand--beige: #f3efe8; /* Brand / Palette Token (bcgbuildingdesign-com-au) */
  --font-family--body: "NeueHaasDisplay Pro",Arial,sans-serif; /* Typography / Scale Token (bcgbuildingdesign-com-au) */
  --_theme---text-color--primary: var(--neutral--black); /* Typography Ink Token (bcgbuildingdesign-com-au) */
  --_typography---body--body-line-height: var(--_typography---font-height--medium); /* Typography / Scale Token (bcgbuildingdesign-com-au) */
  --font-weight--semi-bold: 600; /* Typography / Scale Token (bcgbuildingdesign-com-au) */
  --_typography---body--body-letter-spacing: var(--_typography---letter-spacing--default); /* Typography / Scale Token (bcgbuildingdesign-com-au) */
  --font-family--heading: "NeueHaasDisplay Pro",Arial,sans-serif; /* Typography Ink Token (bcgbuildingdesign-com-au) */
  --_typography---h1--h1-font-size: 3.5rem; /* Typography / Scale Token (bcgbuildingdesign-com-au) */
  --_typography---h1--h1-line-height: var(--_typography---font-height--tiny); /* Typography / Scale Token (bcgbuildingdesign-com-au) */
  --_typography---h1--h1-font-weight: var(--font-weight--semi-bold); /* Typography / Scale Token (bcgbuildingdesign-com-au) */
  --_typography---h1--h1-letter-spacing: var(--_typography---letter-spacing--default); /* Typography / Scale Token (bcgbuildingdesign-com-au) */
  --_typography---h2--h2-font-size: 3em; /* Typography / Scale Token (bcgbuildingdesign-com-au) */
  --_typography---h2--h2-line-height: var(--_typography---font-height--medium); /* Typography / Scale Token (bcgbuildingdesign-com-au) */
  --_typography---h2--h2-font-weight: var(--font-weight--bold); /* Typography / Scale Token (bcgbuildingdesign-com-au) */
  --_typography---h2--h2-letter-spacing: var(--_typography---letter-spacing--default); /* Typography / Scale Token (bcgbuildingdesign-com-au) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f3efe8` — grounded in `var(--brand--beige)` in `:root`
- **Primary Typography Ink**: `#114e0b` — grounded in `var(--brand--green-darker)` in `:root`
- **Elevated Surface / Card Substrate**: `#3a3028` — grounded in `var(--brand--brown)` in `:root`
- **Interactive Accent / Highlight**: `#fffdf8` — grounded in `var(--neutral--white)` in `:root`
- **Secondary / Muted Copy**: `#a9645b` — grounded in `var(--terracota)` in `:root`
- **Structural Hairline Border**: `#1b1a18` — grounded in `var(--neutral--black)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×7439px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `940px` extracted from `bcgbuildingdesign-com-au` stylesheet
- **Padding & Gutters**: `9px` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding
- **Media Queries**: `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)`
- **Corner Radii**: `3px`, `100%`, `50%`, `.125rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `NeueHaasDisplay Pro`
- **Body Font Stack**: `Neuehaasgrottext 65 Trial`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--_typography---h1--h1-font-size: 3.5rem`, `--_typography---h1--h1-line-height: var(--_typography---font-height--tiny)`, `--_typography---h1--h1-font-weight: var(--font-weight--semi-bold)`
- **H2 Section Rule**: CSS variables `--_typography---h2--h2-font-size: 3em`, `--_typography---h2--h2-line-height: var(--_typography---font-height--medium)`, `--_typography---h2--h2-font-weight: var(--font-weight--bold)`
- **Body Copy Rule**: CSS variables `--font-family--body: "NeueHaasDisplay Pro",Arial,sans-serif`, `--_typography---body--body-line-height: var(--_typography---font-height--medium)`, `--_typography---body--body-letter-spacing: var(--_typography---letter-spacing--default)`
- **Metadata & Index Rule**: CSS variables `--_typography---body--body-letter-spacing: var(--_typography---letter-spacing--default)`, `--_typography---h1--h1-letter-spacing: var(--_typography---letter-spacing--default)`, `--_typography---h2--h2-letter-spacing: var(--_typography---letter-spacing--default)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `bcgbuildingdesign-com-au` (`Building Designer Gold Coast · BCG Building Design`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.navbar> — `bcgbuildingdesign-com-au`)**:
   - DOM & Selectors: Landmark `<nav class="navbar">` hosting `Building Designer Gold Coast · BCG B` navigation (`Home · Studio · Process · Projects · Project Enquiry`), DOM attributes (`data-wf-domain="www.bcgbuildingdesign..."`, `data-wf-page="6a794e5aeebba97e3ac774a5"`, `data-wf-site="6a794e5aeebba97e3ac774ae"`, `data-barba="wrapper"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.navbar> — `bcgbuildingdesign-com-au`)` (`bcgbuildingdesign-com-au`) adapts across `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)` with `cubic-bezier(0.25,0.46,0.45,0.94)` transitions and links `Home · Studio · Process · Projects · Project Enquiry`.
2. **Hero Stage & Focal Lead (<section.section> — `Building Designer Gold Coast`)**:
   - DOM & Selectors: Landmark `<section class="section is-relative">` presenting display lead `Building Designer Gold Coast` and copy excerpt *"BCG is a boutique building design studio based on the Gold Coast,"* over `#f3efe8` canvas and `#1b1a18` ink.
   - Responsive Contract: Hero stage (`1440×7439px` desktop / `390×2400px` mobile) sets `#f3efe8` background with `#1b1a18` headline `Building Designer Gold Coast`.
3. **Primary Showcase & Content Grid (<section.section> — `Designing beautiful homes that wor`)**:
   - DOM & Selectors: Landmark `<section class="section is-sticky">` rendering section `Designing beautiful homes that work as well as th...` with copy *"Learn More Learn More"*, asset references (`cdn.prod.website-files.com`, `bcg-staging.webflow.shared.4c5b11...`, `gtm.js`, `recaptcha__en.js`), and grid rule `summary { display:block }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.section> — `Designing beautiful homes that wor`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `9px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.section-brown> — `Our Studio`)**:
   - DOM & Selectors: Landmark `<section class="section-brown">` framing `Our Studio` and `Every considered home begins with a considered ap...` (*"Designing an enduring home is only half the job. The other half i"*) with `#3a3028` surface cards, `#fffdf8` accents, and `video { vertical-align:baseline;display:inline-block }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.section-brown> — `Our Studio`)` uses `3px`, `100%`, `50%`, `.125rem` radii, `#fffdf8` highlights, and assets (cdn.prod.website-files.com, bcg-staging.webflow.shared.4c5b11..., gtm.js).
5. **Colophon & Global Directory Footer (<footer.section_footer> — `https://bcgbuildingdesign.com.au/`)**:
   - DOM & Selectors: Landmark `<footer class="section_footer">` anchoring `Building Designer Gold Coast · B` footer links (`Home · Studio · Process · Projects · Project Enquiry`), copy *"We’ve had a great experience with BCG designs. We approached"*, and `#1b1a18` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.section_footer> — `https://bcgbuildingdesign.com.au/`)` aligns to `940px` extracted from `bcgbuildingdesign-com-au` stylesheet with `9px` lateral canvas padding with `16px` grid gap and attributes (data-wf-domain="www.bcgbuildingdesign...", data-wf-page="6a794e5aeebba97e3ac774a5", data-wf-site="6a794e5aeebba97e3ac774ae").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"BCG is a boutique building design studio based on the Gold Coast, specialising in..."*
- Copy Excerpt 2: *"Learn More Learn More"*
- Copy Excerpt 3: *"Designing an enduring home is only half the job. The other half is making sure eve..."*
- Copy Excerpt 4: *"We’ve had a great experience with BCG designs. We approached Bianca because we wer..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.25,0.46,0.45,0.94)`
- **Extracted Stylesheet Rules (`bcgbuildingdesign-com-au`)**:
- `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`
- `summary { display:block }`
- `video { vertical-align:baseline;display:inline-block }`
- `template { display:none }`
- `strong { font-weight:700 }`
- **Per-Selector Transition Rules**:
- **Selector `.w-webflow-badge>img`**: `transition: unset` extracted from `bcgbuildingdesign-com-au` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s,color .1s` extracted from `bcgbuildingdesign-com-au` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `bcgbuildingdesign-com-au` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.25,0.46,0.45,0.94)`)**: Governs interactive state transitions across `<nav.navbar>` and `<section.section>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `bcgbuildingdesign-com-au`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
