---
title: "UI Prompt Blueprint: bettr-academy"
date: 2026-11-15
target: "[[overview|bettr-academy]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#0c0c0c` ink, `#fcbf27` accent)"
---

# UI Design System & Master Generation Blueprint: bettr-academy

> **Bettr Academy · World-Class Barista & Coffee Training** (https://bettr.academy/) — Bettr Academy offers SCA-certified and WSQ-accredited coffee courses in Singapore — real, hands-on training with up to 70% SkillsFuture f...

![Desktop Viewport Capture (1440x8103)](file:///root/projects/fleet/wiki/targets/bettr-academy/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Bettr Academy · World-Class Barista & Coffee Training** (`https://bettr.academy/`). Bettr Academy offers SCA-certified and WSQ-accredited coffee courses in Singapore — real, hands-on training with up to 70% SkillsFuture f...
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#0c0c0c` ink, `#fcbf27` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`var(--_primitives---colors--white)` in `:root`) paired with `#0c0c0c` primary typography and `#fcbf27` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Jobclarendon` for display copy (`B e t t r C o f f e e . B e t t r W `) with `Agipo Condensed` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `64rem` container bounds (`gap: .5rem`, padding `1.25rem`) with `cubic-bezier(.34,1.56,.64,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/bettr-academy/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×8103px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `64rem` extracted from `bettr-academy` stylesheet.
- **Canvas Lateral Padding & Spacing**: `1.25rem` lateral canvas padding with `.5rem` grid gap.
- **Border Radius Scale**: `2px`, `.2rem`, `9rem`, `var(--_ui-styles---radius--small)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 64rem`, `gap: .5rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `1.25rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (min-width: 1440px)`, `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--_primitives---colors--white)` in `:root` |
| **Primary Typography Ink** | `#0c0c0c` | `var(--_primitives---colors--neutral-darkest)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff3` | `var(--_primitives---opacity--white-20)` in `:root` |
| **Interactive Accent / Highlight** | `#fcbf27` | `var(--_primitives---colors--sunshine)` in `:root` |
| **Secondary / Muted Copy** | `#2c1c0f` | `var(--_primitives---colors--coffee)` in `:root` |
| **Structural Hairline Border** | `#f7f4ed` | `var(--_primitives---colors--cream)` in `:root` |
| **Variable Token (`--_primitives---opacity--neutral-darkest-5`)** | `#0c0c0c0d` | `var(--_primitives---opacity--neutral-darkest-5)` in `:root` |
| **Variable Token (`--_primitives---opacity--neutral-darkest-15`)** | `#0c0c0c26` | `var(--_primitives---opacity--neutral-darkest-15)` in `:root` |
| **Variable Token (`--_primitives---opacity--white-10`)** | `#ffffff1a` | `var(--_primitives---opacity--white-10)` in `:root` |
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
- **Primary Body Stack**: `Agipo Condensed`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 5.25rem`, `line-height: 1`, `font-weight: 600`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 3.75rem`, `line-height: 1.1`, `font-weight: 600`).
- **Body Copy**: CSS variables `--_typography---font-styles--body: Roboto, sans-serif`; rule `body` (`font-size: 1rem`, `line-height: 1.5`).
- **Metadata & Navigation Labels**: CSS variables `--_ui-styles---radius--small: .25rem`; rule `small` (`font-size: 80%`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.34,1.56,.64,1)`, `cubic-bezier(0.625,0.05,0,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.button`**: `transition: color .2s, border-color .2s, background-color .2s` extracted from `bettr-academy` stylesheet.
- **Selector `.form_input`**: `transition: border-color .2s, background-color .2s` extracted from `bettr-academy` stylesheet.
- **Selector `.notice-banner_component`**: `transition: height .4s` extracted from `bettr-academy` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.34,1.56,.64,1)`)**: Governs interactive state transitions across `<header.section_header>` and `<section.section_journey>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Bettr Academy · World-Class Barista & Coff │
│ ====================================================================== │
│ [ <header.section_header>  | Coffee Automation · Barista · Brewing  ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.notice-banner_component>                    |   │
│ | H1: B e t t r C o f f e e . B e t t r W o r l d .                |   │
│ | Substrate: #fff       | Ink: #0c0c0c    | Accent: #fcbf27        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.section_journey> ) max-w: 64rem          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Where Does Your Bettr Journe |  | Yourself                     | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .5rem ) | │
│ | [<header.section_he] -> [<section.notice-ba] -> [<section.section_j] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer_compone) | https://bettr.academy/             │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.section_header> — `bettr-academy`)**:
   - Landmark `<header class="section_header">` hosting `Bettr Academy · World-Class Barista ` navigation (`Coffee Automation · Barista · Brewing · Sensory · Roasting`), DOM attributes (`data-wf-domain="bettr.academy"`, `data-wf-page="69f15930f71b5763616e2c5d"`, `data-wf-site="69f15930f71b5763616e2c5c"`, `data-barba="wrapper"`), and stylesheet rule `ul { margin-top: 1rem; margin-bottom: 1rem; padding-left: 1.25rem; }`.
2. **Hero Stage & Focal Lead (<section.notice-banner_component> — `B e t t r C o f f e e . B e t t r `)**:
   - Landmark `<section class="notice-banner_component">` presenting display lead `B e t t r C o f f e e . B e t t r W o r l d .` and copy excerpt *"Hospitality Skills"* over `#fff` canvas and `#0c0c0c` ink.
3. **Primary Showcase & Content Grid (<section.section_journey> — `Where Does Your Bettr Journey Begi`)**:
   - Landmark `<section class="section_journey color-scheme-4">` rendering section `Where Does Your Bettr Journey Begin?` with copy *"SkillsFuture Career Transition Programme"*, asset references (`cdn.prod.website-files.com`, `bettr-academy.webflow.shared.25d4...`, `bettr-academy.webflow.69f15930f71...`, `fonts.googleapis.com`), and grid rule `ol { margin-top: 1rem; margin-bottom: 1rem; padding-left: 1.5rem; }`.
4. **Interactive Detail & Feature Matrix (<section.section_rotating-words-banner> — `Yourself`)**:
   - Landmark `<section class="section_rotating-words-banner color-scheme-2">` framing `Yourself` and `Your Team` (*"Workshops & Experiences"*) with `#fff3` surface cards, `#fcbf27` accents, and `li { margin-top: .25rem; margin-bottom: .25rem; padding-left: .5rem; }`.
5. **Colophon & Global Directory Footer (<footer.footer_component> — `https://bettr.academy/`)**:
   - Landmark `<footer class="footer_component color-scheme-3">` anchoring `Bettr Academy · World-Class Bari` footer links (`Coffee Automation · Barista · Brewing · Sensory · Roasting`), copy *"Corporate Training"*, and `#f7f4ed` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: bettr-academy (Bettr Academy · World-Class Barista & Coffee Training)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `bettr-academy` (**Bettr Academy · World-Class Barista & Coffee Training** — `https://bettr.academy/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#0c0c0c` ink, `#fcbf27` accent).
- **Identity & Domain Context**: Bettr Academy offers SCA-certified and WSQ-accredited coffee courses in Singapore — real, hands-on training with up to 70% SkillsFuture f...
- **Primary Substrate**: `#fff` (`var(--_primitives---colors--white)` in `:root`), **Primary Ink**: `#0c0c0c`, **Accent / Highlight**: `#fcbf27`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`var(--_primitives---colors--white)` in `:root`) paired with `#0c0c0c` primary typography and `#fcbf27` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Jobclarendon` for display copy (`B e t t r C o f f e e . B e t t r W `) with `Agipo Condensed` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `64rem` container bounds (`gap: .5rem`, padding `1.25rem`) with `cubic-bezier(.34,1.56,.64,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `bettr-academy` in your global stylesheet:

:root {
  /* Bettr Academy · World-Class Barista & Coffee Training (bettr-academy) — Ground-Truth Extracted CSS Variables */
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
- **Primary Canvas Substrate**: `#fff` — grounded in `var(--_primitives---colors--white)` in `:root`
- **Primary Typography Ink**: `#0c0c0c` — grounded in `var(--_primitives---colors--neutral-darkest)` in `:root`
- **Elevated Surface / Card Substrate**: `#fff3` — grounded in `var(--_primitives---opacity--white-20)` in `:root`
- **Interactive Accent / Highlight**: `#fcbf27` — grounded in `var(--_primitives---colors--sunshine)` in `:root`
- **Secondary / Muted Copy**: `#2c1c0f` — grounded in `var(--_primitives---colors--coffee)` in `:root`
- **Structural Hairline Border**: `#f7f4ed` — grounded in `var(--_primitives---colors--cream)` in `:root`
- **Variable Token (`--_primitives---opacity--neutral-darkest-5`)**: `#0c0c0c0d` — grounded in `var(--_primitives---opacity--neutral-darkest-5)` in `:root`
- **Variable Token (`--_primitives---opacity--neutral-darkest-15`)**: `#0c0c0c26` — grounded in `var(--_primitives---opacity--neutral-darkest-15)` in `:root`
- **Variable Token (`--_primitives---opacity--white-10`)**: `#ffffff1a` — grounded in `var(--_primitives---opacity--white-10)` in `:root`
- **Variable Token (`--_primitives---colors--earth`)**: `#ed612f` — grounded in `var(--_primitives---colors--earth)` in `:root`
- **Variable Token (`--_primitives---colors--latte`)**: `#edd5b7` — grounded in `var(--_primitives---colors--latte)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×8103px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `64rem` extracted from `bettr-academy` stylesheet
- **Padding & Gutters**: `1.25rem` lateral canvas padding with `.5rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 64rem`, `gap: .5rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `1.25rem` horizontal padding
- **Media Queries**: `@media screen and (min-width: 1440px)`, `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`
- **Corner Radii**: `2px`, `.2rem`, `9rem`, `var(--_ui-styles---radius--small)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Jobclarendon`
- **Body Font Stack**: `Agipo Condensed`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: rule `h1` (`font-size: 5.25rem`, `line-height: 1`, `font-weight: 600`)
- **H2 Section Rule**: rule `h2` (`font-size: 3.75rem`, `line-height: 1.1`, `font-weight: 600`)
- **Body Copy Rule**: CSS variables `--_typography---font-styles--body: Roboto, sans-serif`; rule `body` (`font-size: 1rem`, `line-height: 1.5`)
- **Metadata & Index Rule**: CSS variables `--_ui-styles---radius--small: .25rem`; rule `small` (`font-size: 80%`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `bettr-academy` (`Bettr Academy · World-Class Barista & Coffee Training`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.section_header> — `bettr-academy`)**:
   - DOM & Selectors: Landmark `<header class="section_header">` hosting `Bettr Academy · World-Class Barista ` navigation (`Coffee Automation · Barista · Brewing · Sensory · Roasting`), DOM attributes (`data-wf-domain="bettr.academy"`, `data-wf-page="69f15930f71b5763616e2c5d"`, `data-wf-site="69f15930f71b5763616e2c5c"`, `data-barba="wrapper"`), and stylesheet rule `ul { margin-top: 1rem; margin-bottom: 1rem; padding-left: 1.25rem; }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.section_header> — `bettr-academy`)` (`bettr-academy`) adapts across `@media screen and (min-width: 1440px)`, `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)` with `cubic-bezier(.34,1.56,.64,1)`, `cubic-bezier(0.625,0.05,0,1)` transitions and links `Coffee Automation · Barista · Brewing · Sensory · Roasting`.
2. **Hero Stage & Focal Lead (<section.notice-banner_component> — `B e t t r C o f f e e . B e t t r `)**:
   - DOM & Selectors: Landmark `<section class="notice-banner_component">` presenting display lead `B e t t r C o f f e e . B e t t r W o r l d .` and copy excerpt *"Hospitality Skills"* over `#fff` canvas and `#0c0c0c` ink.
   - Responsive Contract: Hero stage (`1440×8103px` desktop / `390×2400px` mobile) sets `#fff` background with `#0c0c0c` headline `B e t t r C o f f e e . B e t t r W o r l d .`.
3. **Primary Showcase & Content Grid (<section.section_journey> — `Where Does Your Bettr Journey Begi`)**:
   - DOM & Selectors: Landmark `<section class="section_journey color-scheme-4">` rendering section `Where Does Your Bettr Journey Begin?` with copy *"SkillsFuture Career Transition Programme"*, asset references (`cdn.prod.website-files.com`, `bettr-academy.webflow.shared.25d4...`, `bettr-academy.webflow.69f15930f71...`, `fonts.googleapis.com`), and grid rule `ol { margin-top: 1rem; margin-bottom: 1rem; padding-left: 1.5rem; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.section_journey> — `Where Does Your Bettr Journey Begi`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 64rem`, `gap: .5rem`) on desktop and Single-column vertical stack at `390px` viewport width with `1.25rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.section_rotating-words-banner> — `Yourself`)**:
   - DOM & Selectors: Landmark `<section class="section_rotating-words-banner color-scheme-2">` framing `Yourself` and `Your Team` (*"Workshops & Experiences"*) with `#fff3` surface cards, `#fcbf27` accents, and `li { margin-top: .25rem; margin-bottom: .25rem; padding-left: .5rem; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.section_rotating-words-banner> — `Yourself`)` uses `2px`, `.2rem`, `9rem`, `var(--_ui-styles---radius--small)` radii, `#fcbf27` highlights, and assets (cdn.prod.website-files.com, bettr-academy.webflow.shared.25d4..., bettr-academy.webflow.69f15930f71...).
5. **Colophon & Global Directory Footer (<footer.footer_component> — `https://bettr.academy/`)**:
   - DOM & Selectors: Landmark `<footer class="footer_component color-scheme-3">` anchoring `Bettr Academy · World-Class Bari` footer links (`Coffee Automation · Barista · Brewing · Sensory · Roasting`), copy *"Corporate Training"*, and `#f7f4ed` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer_component> — `https://bettr.academy/`)` aligns to `64rem` extracted from `bettr-academy` stylesheet with `1.25rem` lateral canvas padding with `.5rem` grid gap and attributes (data-wf-domain="bettr.academy", data-wf-page="69f15930f71b5763616e2c5d", data-wf-site="69f15930f71b5763616e2c5c").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Hospitality Skills"*
- Copy Excerpt 2: *"SkillsFuture Career Transition Programme"*
- Copy Excerpt 3: *"Workshops & Experiences"*
- Copy Excerpt 4: *"Corporate Training"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.34,1.56,.64,1)`, `cubic-bezier(0.625,0.05,0,1)`
- **Extracted Stylesheet Rules (`bettr-academy`)**:
- `ul { margin-top: 1rem; margin-bottom: 1rem; padding-left: 1.25rem; }`
- `ol { margin-top: 1rem; margin-bottom: 1rem; padding-left: 1.5rem; }`
- `li { margin-top: .25rem; margin-bottom: .25rem; padding-left: .5rem; }`
- `img { max-width: 100%; display: inline-block; }`
- `label { margin-bottom: .25rem; font-weight: 500; }`
- **Per-Selector Transition Rules**:
- **Selector `.button`**: `transition: color .2s, border-color .2s, background-color .2s` extracted from `bettr-academy` stylesheet.
- **Selector `.form_input`**: `transition: border-color .2s, background-color .2s` extracted from `bettr-academy` stylesheet.
- **Selector `.notice-banner_component`**: `transition: height .4s` extracted from `bettr-academy` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.34,1.56,.64,1)`)**: Governs interactive state transitions across `<header.section_header>` and `<section.section_journey>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `bettr-academy`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
