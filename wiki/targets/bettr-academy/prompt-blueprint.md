---
title: "UI Prompt Blueprint: bettr-academy"
date: 2026-11-24
captured_at: 2026-11-24
target: "bettr-academy"
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
archetype: "Light-Substrate Editorial & Modular Grid System (`#f7f4ed` canvas, `#2c1c0f` ink, `#0082f3` accent)"
---

# UI Design System & Master Generation Blueprint: bettr-academy

> **Bettr Academy · World-Class Barista & Coffee Training** (https://bettr.academy/) — Bettr Academy offers SCA-certified and WSQ-accredited coffee courses in Singapore — real, hands-on training with up to 70% SkillsFuture f...

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Bettr Academy · World-Class Barista & Coffee Training** (`https://bettr.academy/`). Bettr Academy offers SCA-certified and WSQ-accredited coffee courses in Singapore — real, hands-on training with up to 70% SkillsFuture f...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#f7f4ed` canvas, `#2c1c0f` ink, `#0082f3` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f7f4ed` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#2c1c0f` primary typography and `#0082f3` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Jobclarendon` for display copy (`Bettr Coffee. Bettr World.`) with `Roboto`.
  - **Calibrated Spatial Grid & Motion**: Combines `96rem` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(.34,1.56,.64,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=7214px` / doc `8261px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `96rem` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `9px` lateral canvas padding with `16px` grid gap.
- **Border Radius Scale**: `100%`, `3px`, `50%`, `2px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: 16px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f7f4ed` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#2c1c0f` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#fcbf27` | live computed `footer` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#0082f3` | `.w-dropdown-link.w--current { color: #0082f3 }` |
| **Secondary / Muted Copy** | `#fcbf27` | live computed `h1` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e2e2e2` | `blockquote { border-left: #e2e2e2 }` |
| **Variable Token (`--_primitives---colors--white`)** | `#ffffff` | `var(--_primitives---colors--white)` in `:root` |
| **Variable Token (`--_primitives---opacity--neutral-darkest-5`)** | `#0c0c0c` | `var(--_primitives---opacity--neutral-darkest-5)` in `:root` |
| **Variable Token (`--_primitives---opacity--white-20`)** | `#fff3` | `var(--_primitives---opacity--white-20)` in `:root` |
| **Variable Token (`--_primitives---colors--earth`)** | `#ed612f` | `var(--_primitives---colors--earth)` in `:root` |
| **Variable Token (`--_primitives---colors--latte`)** | `#edd5b7` | `var(--_primitives---colors--latte)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-scheme-1--background` | `var(--_primitives---colors--cream)` | Canvas / Surface Token |
| `--_typography---font-styles--body` | `Roboto, sans-serif` | Typography / Scale Token |
| `--color-scheme-1--text` | `var(--_primitives---colors--coffee)` | Typography Ink Token |
| `--_typography---font-styles--heading` | `Jobclarendon, Arial, sans-serif` | Typography Ink Token |
| `--_primitives---colors--white` | `#fff` | Canvas / Surface Token |
| `--_primitives---opacity--transparent` | `transparent` | Design System Custom Token |
| `--_primitives---opacity--neutral-darkest-5` | `#0c0c0c0d` | Canvas / Surface Token |
| `--_primitives---opacity--neutral-darkest-15` | `#0c0c0c26` | Canvas / Surface Token |
| `--_primitives---colors--neutral-darkest` | `#0c0c0c` | Canvas / Surface Token |
| `--_primitives---opacity--white-10` | `#ffffff1a` | Canvas / Surface Token |
| `--_primitives---opacity--white-20` | `#fff3` | Canvas / Surface Token |
| `--_primitives---colors--sunshine` | `#fcbf27` | Brand / Palette Token |
| `--_primitives---colors--coffee` | `#2c1c0f` | Brand / Palette Token |
| `--_primitives---colors--cream` | `#f7f4ed` | Brand / Palette Token |
| `--_primitives---colors--earth` | `#ed612f` | Brand / Palette Token |
| `--_primitives---colors--latte` | `#edd5b7` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Jobclarendon`.
- **Primary Body Stack**: `Roboto`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 154.977px`, `line-height: 185.972px`, `font-weight: 600`); rule `h1` (`font-size: 2em`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 84px`, `line-height: 84px`, `font-weight: 600`); rule `h2` (`font-size: 32px`, `line-height: 36px`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--_typography---font-styles--body: Roboto, sans-serif`; rule `body` (`font-size: 14px`, `line-height: 20px`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--_ui-styles---radius--small: .25rem`; rule `small` (`font-size: 80%`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.34,1.56,.64,1)`, `cubic-bezier(0.625,0.05,0,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.w-webflow-badge > img`**: `transition: unset` extracted from `bettr-academy` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s, color .1s` extracted from `bettr-academy` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `bettr-academy` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.34,1.56,.64,1)`)**: Governs interactive state transitions across `<header.section_header>` and `<section.section_journey>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `8261px`, deepest scrollY reached `7214px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: `Lenis`, `GSAP/ScrollTrigger`.
- **Route Transition Architecture**: First internal navigation (`/courses/course-category/coffee-automation`) measured as `direct` in `1444ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Bettr Academy · World-Class Barista & Coff │
│ ====================================================================== │
│ [ <header.section_header (1440x855px) | Coffee Automation · Barista  ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.notice-banner_component> (w=1440px)           | │
│ | H1: Bettr Coffee. Bettr World.                                     | │
│ | Substrate: #f7f4ed | Ink: #2c1c0f | Accent: #0082f3                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.section_journey>) max-w: 96rem             | │
│ | +------------------------------+  +------------------------------+ | │
│ | | B e t t r C o f f e e . B e  |  | Where Does Your Bettr Journe | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.section_rotating-) — Your Coffee Career, C | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer_compo) | https://bettr.academy/               │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.section_header> ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.notice-banner_c) — 390px Vertical Lead        | │
│ | H1: Bettr Coffee. Bettr World.                                     | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.section_journ) — 1-Col Stack              | │
│ | [ Item 1: B e t t r C o f f e e . B e t t r W o r l d .          ] | │
│ | [ Item 2: Where Does Your Bettr Journey Begin?                   ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.section_rotatin) — 1-Col (Your Coffee Career) │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer_compo) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.section_header> — `bettr-academy`)**:
   - Landmark `<header class="section_header">` (`1440x855px`) hosting `Bettr Academy · World-Class Barista ` navigation (`Coffee Automation · Barista · Brewing · Sensory · Roasting`), DOM attributes (`data-wf-domain="bettr.academy"`, `data-wf-page="69f15930f71b5763616e2c5d"`, `data-wf-site="69f15930f71b5763616e2c5c"`, `data-barba="wrapper"`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<section.notice-banner_component> — `Bettr Coffee. Bettr World.`)**:
   - Landmark `<section class="notice-banner_component">` presenting display lead `Bettr Coffee. Bettr World.` and copy excerpt *"WORLD-CLASS COFFEE EDUCATION"* over `#f7f4ed` canvas and `#2c1c0f` ink.
3. **Primary Showcase & Content Grid (<section.section_journey> — `B e t t r C o f f e e . B e t t r `)**:
   - Landmark `<section class="section_journey color-scheme-4">` rendering section `B e t t r C o f f e e . B e t t r W o r l d .` with copy *"WORLD-CLASS COfFEE EDUCATION"*, asset references (`cdn.prod.website-files.com`, `bettr-academy.webflow.shared.25d4...`, `bettr-academy.webflow.69f15930f71...`, `fonts.googleapis.com`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.section_rotating-words-banner> — `Where Does Your Bettr Journey Begi`)**:
   - Landmark `<section class="section_rotating-words-banner color-scheme-2">` framing `Where Does Your Bettr Journey Begin?` and `Your Coffee Career, Curated.` (*"Stop just making coffee, start building a career. Gain the SCA cr"*) with `#fcbf27` surface cards, `#0082f3` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.footer_component> — `https://bettr.academy/`)**:
   - Landmark `<footer class="footer_component color-scheme-3">` anchoring `Bettr Academy · World-Class Bari` footer links (`Coffee Automation · Barista · Brewing · Sensory · Roasting`), copy *"Build team skills and foster professional development. Coffe"*, and `#e2e2e2` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `Bettr Coffee. Bettr World.` · sticky/fixed elements: `2`
- **Step 02** (`y=850px`, `12%`): Active landmark `Yourself` · sticky/fixed elements: `2`
- **Step 03** (`y=1700px`, `24%`): Active landmark `Your Coffee Career, Curated.` · sticky/fixed elements: `2`
- **Step 04** (`y=3400px`, `46%`): Active landmark `A way that’s 100% Better. But why Bettr?` · sticky/fixed elements: `1`
- **Step 05** (`y=4250px`, `58%`): Active landmark `The Gold Standard in Global Certification` · sticky/fixed elements: `2`
- **Step 06** (`y=5950px`, `81%`): Active landmark `100% Reviews Straight from the Community` · sticky/fixed elements: `1`
- **Step 07** (`y=6800px`, `92%`): Active landmark `Footer` · sticky/fixed elements: `2`
- **Step 08** (`y=7214px`, `98%`): Active landmark `Footer` · sticky/fixed elements: `1`

### Multi-Page Internal Route Map
- **Detail Route (`/courses/course-category/coffee-automation`)**: `https://bettr.academy/courses/course-category/coffee-automation` — H1: `Coffee Automation`, scrollHeight `4278px`, transition `direct` (`1444ms`)
- **About Route (`/about-us`)**: `https://bettr.academy/about-us` — H1: `About Bettr`, scrollHeight `6556px`, transition `direct` (`2330ms`)
- **Detail Route (`/courses/course-category/barista-courses`)**: `https://bettr.academy/courses/course-category/barista-courses` — H1: `Barista Courses`, scrollHeight `6523px`, transition `direct` (`2427ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: bettr-academy (Bettr Academy · World-Class Barista & Coffee Training)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `bettr-academy` (**Bettr Academy · World-Class Barista & Coffee Training** — `https://bettr.academy/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#f7f4ed` canvas, `#2c1c0f` ink, `#0082f3` accent).
- **Identity & Domain Context**: Bettr Academy offers SCA-certified and WSQ-accredited coffee courses in Singapore — real, hands-on training with up to 70% SkillsFuture f...
- **Primary Substrate**: `#f7f4ed` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#2c1c0f`, **Accent / Highlight**: `#0082f3`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f7f4ed` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#2c1c0f` primary typography and `#0082f3` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Jobclarendon` for display copy (`Bettr Coffee. Bettr World.`) with `Roboto`.
  - **Calibrated Spatial Grid & Motion**: Combines `96rem` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(.34,1.56,.64,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `bettr-academy` in your global stylesheet:

:root {
  /* Bettr Academy · World-Class Barista & Coffee Training (bettr-academy) — Live-Grounded CSS Variables */
  --color-scheme-1--background: var(--_primitives---colors--cream); /* Canvas / Surface Token (bettr-academy) */
  --_typography---font-styles--body: Roboto, sans-serif; /* Typography / Scale Token (bettr-academy) */
  --color-scheme-1--text: var(--_primitives---colors--coffee); /* Typography Ink Token (bettr-academy) */
  --_typography---font-styles--heading: Jobclarendon, Arial, sans-serif; /* Typography Ink Token (bettr-academy) */
  --_primitives---colors--white: #fff; /* Canvas / Surface Token (bettr-academy) */
  --_primitives---opacity--transparent: transparent; /* Design System Custom Token (bettr-academy) */
  --_primitives---opacity--neutral-darkest-5: #0c0c0c0d; /* Canvas / Surface Token (bettr-academy) */
  --_primitives---opacity--neutral-darkest-15: #0c0c0c26; /* Canvas / Surface Token (bettr-academy) */
  --_primitives---colors--neutral-darkest: #0c0c0c; /* Canvas / Surface Token (bettr-academy) */
  --_primitives---opacity--white-10: #ffffff1a; /* Canvas / Surface Token (bettr-academy) */
  --_primitives---opacity--white-20: #fff3; /* Canvas / Surface Token (bettr-academy) */
  --_primitives---colors--sunshine: #fcbf27; /* Brand / Palette Token (bettr-academy) */
  --_primitives---colors--coffee: #2c1c0f; /* Brand / Palette Token (bettr-academy) */
  --_primitives---colors--cream: #f7f4ed; /* Brand / Palette Token (bettr-academy) */
  --_primitives---colors--earth: #ed612f; /* Brand / Palette Token (bettr-academy) */
  --_primitives---colors--latte: #edd5b7; /* Brand / Palette Token (bettr-academy) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f7f4ed` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#2c1c0f` — grounded in live computed `main` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#fcbf27` — grounded in live computed `footer` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#0082f3` — grounded in `.w-dropdown-link.w--current { color: #0082f3 }`
- **Secondary / Muted Copy**: `#fcbf27` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#e2e2e2` — grounded in `blockquote { border-left: #e2e2e2 }`
- **Variable Token (`--_primitives---colors--white`)**: `#ffffff` — grounded in `var(--_primitives---colors--white)` in `:root`
- **Variable Token (`--_primitives---opacity--neutral-darkest-5`)**: `#0c0c0c` — grounded in `var(--_primitives---opacity--neutral-darkest-5)` in `:root`
- **Variable Token (`--_primitives---opacity--white-20`)**: `#fff3` — grounded in `var(--_primitives---opacity--white-20)` in `:root`
- **Variable Token (`--_primitives---colors--earth`)**: `#ed612f` — grounded in `var(--_primitives---colors--earth)` in `:root`
- **Variable Token (`--_primitives---colors--latte`)**: `#edd5b7` — grounded in `var(--_primitives---colors--latte)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `96rem` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `9px` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding
- **Media Queries**: `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)`
- **Corner Radii**: `100%`, `3px`, `50%`, `2px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Jobclarendon`
- **Body Font Stack**: `Roboto`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 154.977px`, `line-height: 185.972px`, `font-weight: 600`); rule `h1` (`font-size: 2em`)
- **H2 Section Rule**: live computed `h2` (`font-size: 84px`, `line-height: 84px`, `font-weight: 600`); rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--_typography---font-styles--body: Roboto, sans-serif`; rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--_ui-styles---radius--small: .25rem`; rule `small` (`font-size: 80%`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `bettr-academy` (`Bettr Academy · World-Class Barista & Coffee Training`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.section_header> — `bettr-academy`)**:
   - DOM & Selectors: Landmark `<header class="section_header">` (`1440x855px`) hosting `Bettr Academy · World-Class Barista ` navigation (`Coffee Automation · Barista · Brewing · Sensory · Roasting`), DOM attributes (`data-wf-domain="bettr.academy"`, `data-wf-page="69f15930f71b5763616e2c5d"`, `data-wf-site="69f15930f71b5763616e2c5c"`, `data-barba="wrapper"`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.section_header> — `bettr-academy`)` (`bettr-academy`) adapts across `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)` with `cubic-bezier(.34,1.56,.64,1)`, `cubic-bezier(0.625,0.05,0,1)` transitions and links `Coffee Automation · Barista · Brewing · Sensory · Roasting`.
2. **Hero Stage & Focal Lead (<section.notice-banner_component> — `Bettr Coffee. Bettr World.`)**:
   - DOM & Selectors: Landmark `<section class="notice-banner_component">` presenting display lead `Bettr Coffee. Bettr World.` and copy excerpt *"WORLD-CLASS COFFEE EDUCATION"* over `#f7f4ed` canvas and `#2c1c0f` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×2616px` mobile) sets `#f7f4ed` background with `#2c1c0f` headline `Bettr Coffee. Bettr World.`.
3. **Primary Showcase & Content Grid (<section.section_journey> — `B e t t r C o f f e e . B e t t r `)**:
   - DOM & Selectors: Landmark `<section class="section_journey color-scheme-4">` rendering section `B e t t r C o f f e e . B e t t r W o r l d .` with copy *"WORLD-CLASS COfFEE EDUCATION"*, asset references (`cdn.prod.website-files.com`, `bettr-academy.webflow.shared.25d4...`, `bettr-academy.webflow.69f15930f71...`, `fonts.googleapis.com`), and grid rule `body { margin: 0; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.section_journey> — `B e t t r C o f f e e . B e t t r `)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `9px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.section_rotating-words-banner> — `Where Does Your Bettr Journey Begi`)**:
   - DOM & Selectors: Landmark `<section class="section_rotating-words-banner color-scheme-2">` framing `Where Does Your Bettr Journey Begin?` and `Your Coffee Career, Curated.` (*"Stop just making coffee, start building a career. Gain the SCA cr"*) with `#fcbf27` surface cards, `#0082f3` accents, and `summary { display: block; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.section_rotating-words-banner> — `Where Does Your Bettr Journey Begi`)` uses `100%`, `3px`, `50%`, `2px` radii, `#0082f3` highlights, and assets (cdn.prod.website-files.com, bettr-academy.webflow.shared.25d4..., bettr-academy.webflow.69f15930f71...).
5. **Colophon & Global Directory Footer (<footer.footer_component> — `https://bettr.academy/`)**:
   - DOM & Selectors: Landmark `<footer class="footer_component color-scheme-3">` anchoring `Bettr Academy · World-Class Bari` footer links (`Coffee Automation · Barista · Brewing · Sensory · Roasting`), copy *"Build team skills and foster professional development. Coffe"*, and `#e2e2e2` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer_component> — `https://bettr.academy/`)` aligns to `96rem` (non-`@media` desktop container stylesheet rule) with `9px` lateral canvas padding with `16px` grid gap and attributes (data-wf-domain="bettr.academy", data-wf-page="69f15930f71b5763616e2c5d", data-wf-site="69f15930f71b5763616e2c5c").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"WORLD-CLASS COFFEE EDUCATION"*
- Copy Excerpt 2: *"WORLD-CLASS COfFEE EDUCATION"*
- Copy Excerpt 3: *"Stop just making coffee, start building a career. Gain the SCA credentials recogni..."*
- Copy Excerpt 4: *"Build team skills and foster professional development. Coffee Appreciation, Life S..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.34,1.56,.64,1)`, `cubic-bezier(0.625,0.05,0,1)`
- **Extracted Stylesheet Rules (`bettr-academy`)**:
- `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`
- `body { margin: 0; }`
- `summary { display: block; }`
- `video { vertical-align: baseline; display: inline-block; }`
- `template { display: none; }`
- **Per-Selector Transition Rules**:
- **Selector `.w-webflow-badge > img`**: `transition: unset` extracted from `bettr-academy` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s, color .1s` extracted from `bettr-academy` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `bettr-academy` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.34,1.56,.64,1)`)**: Governs interactive state transitions across `<header.section_header>` and `<section.section_journey>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `8261px` across 8 distinct viewport chapters using Lenis, GSAP/ScrollTrigger.
- **Vertical Chapter Sequence**: Bettr Coffee. Bettr World. (0%) -> Yourself (12%) -> Your Coffee Career, Curated. (24%) -> A way that’s 100% Better. B... (46%) -> The Gold Standard in Global... (58%) -> 100% Reviews Straight from... (81%) -> Footer (92%) -> Footer (98%).
- **Multi-Page Routes**: Scaffold internal routes `/courses/course-category/coffee-automation` (detail, direct), `/about-us` (about, direct), `/courses/course-category/barista-courses` (detail, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `bettr-academy`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | Bettr Coffee. Bettr World. | `2` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `12%` | Yourself | `2` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `1700px` | `24%` | Your Coffee Career, Curated. | `2` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `3400px` | `46%` | A way that’s 100% Better. But why Bettr? | `1` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `4250px` | `58%` | The Gold Standard in Global Certification | `2` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `5950px` | `81%` | 100% Reviews Straight from the Community | `1` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `6800px` | `92%` | Footer | `2` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `7214px` | `98%` | Footer | `1` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | Bettr Coffee. Bettr World. | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `4512px` | `50%` | Pursue a career in F&B with SkillsFuture... | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `9025px` | `100%` | Footer | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `detail` | `https://bettr.academy/courses/course-category/coffee-automation` | Coffee Automation | `4278px` | `direct` (`1444ms`) | [subpage-01-courses-course-category-coffee-autom.webp](assets/subpage-01-courses-course-category-coffee-autom.webp) |
| `2` | `about` | `https://bettr.academy/about-us` | About Bettr | `6556px` | `direct` (`2330ms`) | [subpage-02-about-us.webp](assets/subpage-02-about-us.webp) |
| `3` | `detail` | `https://bettr.academy/courses/course-category/barista-courses` | Barista Courses | `6523px` | `direct` (`2427ms`) | [subpage-03-courses-course-category-barista-cour.webp](assets/subpage-03-courses-course-category-barista-cour.webp) |

