---
title: "UI Prompt Blueprint: www-paragonproductions-co"
date: 2026-11-15
target: "[[overview|www-paragonproductions-co]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#ff5b4b` canvas, `#f8f8f8` ink, `#ffcdd2` accent)"
---

# UI Design System & Master Generation Blueprint: www-paragonproductions-co

> **PARAGON · Creative Production Studio** (https://www.paragonproductions.co/) — PARAGON is a production partner driven by pursuit. We team up with brands and agencies to craft commercials, branded films, and campaigns...

![Desktop Viewport Capture (1440x13738)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **PARAGON · Creative Production Studio** (`https://www.paragonproductions.co/`). PARAGON is a production partner driven by pursuit. We team up with brands and agencies to craft commercials, branded films, and campaigns...
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#ff5b4b` canvas, `#f8f8f8` ink, `#ffcdd2` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#ff5b4b` (`var(--_color---swatch--red)` in `:root`) paired with `#f8f8f8` primary typography and `#ffcdd2` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Review Condensed` for display copy (`Always In PURSUIT`) with `Proxima Nova` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `940px` container bounds (`gap: var(--site--gutter)`, padding `.5rem`) with `cubic-bezier(.23,1,.32,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×13738px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `940px` extracted from `www-paragonproductions-co` stylesheet.
- **Canvas Lateral Padding & Spacing**: `.5rem` lateral canvas padding with `var(--site--gutter)` grid gap.
- **Border Radius Scale**: `3px`, `100%`, `50%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: var(--site--gutter)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `.5rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ff5b4b` | `var(--_color---swatch--red)` in `:root` |
| **Primary Typography Ink** | `#100f0f` | `var(--_color---swatch--black)` in `:root` |
| **Elevated Surface / Card Substrate** | `#6d6c6c` | `var(--_color---swatch--grey-500)` in `:root` |
| **Interactive Accent / Highlight** | `#ffcdd2` | `var(--_color---system--error-light)` in `:root` |
| **Secondary / Muted Copy** | `#d32f2f` | `var(--_color---system--error)` in `:root` |
| **Structural Hairline Border** | `#f8f8f8` | `var(--_color---swatch--white)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--_theme---background--primary` | `var(--_color---swatch--white)` | Canvas / Surface Token |
| `--_text-style---font-family` | `var(--_typography---font-family--tertiary)` | Typography Ink Token |
| `--_theme---text--primary` | `var(--_color---swatch--black)` | Typography Ink Token |
| `--_text-style---font-size` | `var(--_typography---font-size--text-main)` | Typography Ink Token |
| `--_text-style---line-height` | `var(--_typography---line-height--131-5)` | Typography Ink Token |
| `--_text-style---font-weight` | `var(--_typography---font-weight--normal)` | Typography Ink Token |
| `--_text-style---letter-spacing` | `var(--_typography---letter-spacing--0em)` | Typography Ink Token |
| `--_typography---font-family--secondary` | `"Review Condensed",Arial,sans-serif` | Brand / Palette Token |
| `--_typography---font-weight--medium` | `500` | Typography / Scale Token |
| `--_text-style---margin-top` | `var(--_spacing---space--4)` | Typography Ink Token |
| `--_text-style---margin-bottom` | `var(--_spacing---space--5)` | Typography Ink Token |
| `--_color---swatch--red` | `#ff5b4b` | Brand / Palette Token |
| `--_typography---font-family--primary` | `"Proxima Nova",Arial,sans-serif` | Brand / Palette Token |
| `--_theme---text--secondary` | `var(--_color---swatch--grey-500)` | Typography Ink Token |
| `--_typography---font-weight--thin` | `100` | Typography / Scale Token |
| `--_typography---font-weight--extra-light` | `200` | Canvas / Surface Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Review Condensed`.
- **Primary Body Stack**: `Proxima Nova`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`font-size: var(--_text-style---font-size)`, `line-height: var(--_text-style---l...`, `letter-spacing: var(--_typography---l...`, `font-weight: var(--_text-s...`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: var(--_text-style---font-size)`, `line-height: var(--_text-style---l...`, `letter-spacing: var(--_typography---l...`, `font-weight: var(--_text-s...`).
- **Body Copy**: rule `p` (`font-size: var(--_text-style---font-size)`, `line-height: var(--_text-style---l...`, `letter-spacing: var(--_typography---l...`, `font-weight: var(--_text-s...`).
- **Metadata & Navigation Labels**: CSS variables `--_text-style---letter-spacing: var(--_typography---letter-spacing--0em)`, `--max-width--small: 80rem`, `--max-width--extra-small: 50rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.23,1,.32,1)`, `cubic-bezier(.215,.61,.355,1)`, `cubic-bezier(.165,.84,.44,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.u-button`**: `transition: box-shadow .4s,border-color .4s,color .4s,background-color .4s` extracted from `www-paragonproductions-co` stylesheet.
- **Selector `.nav_logo_wrap`**: `transition: background-color .3s` extracted from `www-paragonproductions-co` stylesheet.
- **Selector `.nav_menu_link`**: `transition: background-color .3s` extracted from `www-paragonproductions-co` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.23,1,.32,1)`)**: Governs interactive state transitions across `<nav.nav_wrap>` and `<section.home-services_wrap>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — PARAGON · Creative Production Studio       │
│ ====================================================================== │
│ [ <nav.nav_wrap>           | Skip to main content · Work · Who We A ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.home-hero_wrap>                             |   │
│ | H1: Always In PURSUIT                                            |   │
│ | Substrate: #ff5b4b    | Ink: #f8f8f8    | Accent: #ffcdd2        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.home-services_wra) max-w: 940px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | What We Do                   |  | PARAGON is a production part | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<nav.nav_wrap>] -> [<section.home-hero] -> [<section.home-serv] |   │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer_wrap>  ) | https://www.paragonproductions.co/ │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.nav_wrap> — `www-paragonproductions-co`)**:
   - Landmark `<nav class="nav_wrap">` hosting `PARAGON · Creative Production Studio` navigation (`Skip to main content · Work · Who We Are · News · Contact Us`), DOM attributes (`data-wf-domain="www.paragonproduction..."`, `data-wf-page="68be24b22b086720602bcd26"`, `data-wf-site="68be24b22b086720602bcd38"`, `data-wf-intellimize-customer-id="117787750"`), and stylesheet rule `html.lenis body { height:auto }`.
2. **Hero Stage & Focal Lead (<section.home-hero_wrap> — `Always In PURSUIT`)**:
   - Landmark `<section class="home-hero_wrap">` presenting display lead `Always In PURSUIT` and copy excerpt *"Skip to main content"* over `#ff5b4b` canvas and `#f8f8f8` ink.
3. **Primary Showcase & Content Grid (<section.home-services_wrap> — `What We Do`)**:
   - Landmark `<section class="home-services_wrap">` rendering section `What We Do` with copy *"Instagram Instagram Instagram"*, asset references (`cdn.prod.website-files.com`, `paragonproductions.webflow.shared...`, `paragonproductions.webflow.68be24...`, `gtm.js`), and grid rule `.lenis.lenis-stopped { overflow:clip }`.
4. **Interactive Detail & Feature Matrix (<section.featured-work_wrap> — `PARAGON is a production partner dr`)**:
   - Landmark `<section class="featured-work_wrap">` framing `PARAGON is a production partner driven by pursuit.` and `BUILT FOR THE CHASE` (*"LinkedIn LinkedIn LinkedIn"*) with `#6d6c6c` surface cards, `#ffcdd2` accents, and `.lenis.lenis-smooth iframe { pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.footer_wrap> — `https://www.paragonproductions.co/`)**:
   - Landmark `<footer class="footer_wrap">` anchoring `PARAGON · Creative Production St` footer links (`Skip to main content · Work · Who We Are · News · Contact Us`), copy *"ALWAYS IN PURSUIT //"*, and `#f8f8f8` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-paragonproductions-co (PARAGON · Creative Production Studio)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-paragonproductions-co` (**PARAGON · Creative Production Studio** — `https://www.paragonproductions.co/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#ff5b4b` canvas, `#f8f8f8` ink, `#ffcdd2` accent).
- **Identity & Domain Context**: PARAGON is a production partner driven by pursuit. We team up with brands and agencies to craft commercials, branded films, and campaigns...
- **Primary Substrate**: `#ff5b4b` (`var(--_color---swatch--red)` in `:root`), **Primary Ink**: `#f8f8f8`, **Accent / Highlight**: `#ffcdd2`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#ff5b4b` (`var(--_color---swatch--red)` in `:root`) paired with `#f8f8f8` primary typography and `#ffcdd2` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Review Condensed` for display copy (`Always In PURSUIT`) with `Proxima Nova` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `940px` container bounds (`gap: var(--site--gutter)`, padding `.5rem`) with `cubic-bezier(.23,1,.32,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-paragonproductions-co` in your global stylesheet:

:root {
  /* PARAGON · Creative Production Studio (www-paragonproductions-co) — Ground-Truth Extracted CSS Variables */
  --_theme---background--primary: var(--_color---swatch--white); /* Canvas / Surface Token (www-paragonproductions-co) */
  --_text-style---font-family: var(--_typography---font-family--tertiary); /* Typography Ink Token (www-paragonproductions-co) */
  --_theme---text--primary: var(--_color---swatch--black); /* Typography Ink Token (www-paragonproductions-co) */
  --_text-style---font-size: var(--_typography---font-size--text-main); /* Typography Ink Token (www-paragonproductions-co) */
  --_text-style---line-height: var(--_typography---line-height--131-5); /* Typography Ink Token (www-paragonproductions-co) */
  --_text-style---font-weight: var(--_typography---font-weight--normal); /* Typography Ink Token (www-paragonproductions-co) */
  --_text-style---letter-spacing: var(--_typography---letter-spacing--0em); /* Typography Ink Token (www-paragonproductions-co) */
  --_typography---font-family--secondary: "Review Condensed",Arial,sans-serif; /* Brand / Palette Token (www-paragonproductions-co) */
  --_typography---font-weight--medium: 500; /* Typography / Scale Token (www-paragonproductions-co) */
  --_text-style---margin-top: var(--_spacing---space--4); /* Typography Ink Token (www-paragonproductions-co) */
  --_text-style---margin-bottom: var(--_spacing---space--5); /* Typography Ink Token (www-paragonproductions-co) */
  --_color---swatch--red: #ff5b4b; /* Brand / Palette Token (www-paragonproductions-co) */
  --_typography---font-family--primary: "Proxima Nova",Arial,sans-serif; /* Brand / Palette Token (www-paragonproductions-co) */
  --_theme---text--secondary: var(--_color---swatch--grey-500); /* Typography Ink Token (www-paragonproductions-co) */
  --_typography---font-weight--thin: 100; /* Typography / Scale Token (www-paragonproductions-co) */
  --_typography---font-weight--extra-light: 200; /* Canvas / Surface Token (www-paragonproductions-co) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ff5b4b` — grounded in `var(--_color---swatch--red)` in `:root`
- **Primary Typography Ink**: `#100f0f` — grounded in `var(--_color---swatch--black)` in `:root`
- **Elevated Surface / Card Substrate**: `#6d6c6c` — grounded in `var(--_color---swatch--grey-500)` in `:root`
- **Interactive Accent / Highlight**: `#ffcdd2` — grounded in `var(--_color---system--error-light)` in `:root`
- **Secondary / Muted Copy**: `#d32f2f` — grounded in `var(--_color---system--error)` in `:root`
- **Structural Hairline Border**: `#f8f8f8` — grounded in `var(--_color---swatch--white)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×13738px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `940px` extracted from `www-paragonproductions-co` stylesheet
- **Padding & Gutters**: `.5rem` lateral canvas padding with `var(--site--gutter)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: var(--site--gutter)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `.5rem` horizontal padding
- **Media Queries**: `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)`
- **Corner Radii**: `3px`, `100%`, `50%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Review Condensed`
- **Body Font Stack**: `Proxima Nova`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: rule `h1` (`font-size: var(--_text-style---font-size)`, `line-height: var(--_text-style---l...`, `letter-spacing: var(--_typography---l...`, `font-weight: var(--_text-s...`)
- **H2 Section Rule**: rule `h2` (`font-size: var(--_text-style---font-size)`, `line-height: var(--_text-style---l...`, `letter-spacing: var(--_typography---l...`, `font-weight: var(--_text-s...`)
- **Body Copy Rule**: rule `p` (`font-size: var(--_text-style---font-size)`, `line-height: var(--_text-style---l...`, `letter-spacing: var(--_typography---l...`, `font-weight: var(--_text-s...`)
- **Metadata & Index Rule**: CSS variables `--_text-style---letter-spacing: var(--_typography---letter-spacing--0em)`, `--max-width--small: 80rem`, `--max-width--extra-small: 50rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-paragonproductions-co` (`PARAGON · Creative Production Studio`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.nav_wrap> — `www-paragonproductions-co`)**:
   - DOM & Selectors: Landmark `<nav class="nav_wrap">` hosting `PARAGON · Creative Production Studio` navigation (`Skip to main content · Work · Who We Are · News · Contact Us`), DOM attributes (`data-wf-domain="www.paragonproduction..."`, `data-wf-page="68be24b22b086720602bcd26"`, `data-wf-site="68be24b22b086720602bcd38"`, `data-wf-intellimize-customer-id="117787750"`), and stylesheet rule `html.lenis body { height:auto }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.nav_wrap> — `www-paragonproductions-co`)` (`www-paragonproductions-co`) adapts across `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)` with `cubic-bezier(.23,1,.32,1)`, `cubic-bezier(.215,.61,.355,1)`, `cubic-bezier(.165,.84,.44,1)` transitions and links `Skip to main content · Work · Who We Are · News · Contact Us`.
2. **Hero Stage & Focal Lead (<section.home-hero_wrap> — `Always In PURSUIT`)**:
   - DOM & Selectors: Landmark `<section class="home-hero_wrap">` presenting display lead `Always In PURSUIT` and copy excerpt *"Skip to main content"* over `#ff5b4b` canvas and `#f8f8f8` ink.
   - Responsive Contract: Hero stage (`1440×13738px` desktop / `390×2400px` mobile) sets `#ff5b4b` background with `#f8f8f8` headline `Always In PURSUIT`.
3. **Primary Showcase & Content Grid (<section.home-services_wrap> — `What We Do`)**:
   - DOM & Selectors: Landmark `<section class="home-services_wrap">` rendering section `What We Do` with copy *"Instagram Instagram Instagram"*, asset references (`cdn.prod.website-files.com`, `paragonproductions.webflow.shared...`, `paragonproductions.webflow.68be24...`, `gtm.js`), and grid rule `.lenis.lenis-stopped { overflow:clip }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.home-services_wrap> — `What We Do`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: var(--site--gutter)`) on desktop and Single-column vertical stack at `390px` viewport width with `.5rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.featured-work_wrap> — `PARAGON is a production partner dr`)**:
   - DOM & Selectors: Landmark `<section class="featured-work_wrap">` framing `PARAGON is a production partner driven by pursuit.` and `BUILT FOR THE CHASE` (*"LinkedIn LinkedIn LinkedIn"*) with `#6d6c6c` surface cards, `#ffcdd2` accents, and `.lenis.lenis-smooth iframe { pointer-events:none }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.featured-work_wrap> — `PARAGON is a production partner dr`)` uses `3px`, `100%`, `50%` radii, `#ffcdd2` highlights, and assets (cdn.prod.website-files.com, paragonproductions.webflow.shared..., paragonproductions.webflow.68be24...).
5. **Colophon & Global Directory Footer (<footer.footer_wrap> — `https://www.paragonproductions.co/`)**:
   - DOM & Selectors: Landmark `<footer class="footer_wrap">` anchoring `PARAGON · Creative Production St` footer links (`Skip to main content · Work · Who We Are · News · Contact Us`), copy *"ALWAYS IN PURSUIT //"*, and `#f8f8f8` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer_wrap> — `https://www.paragonproductions.co/`)` aligns to `940px` extracted from `www-paragonproductions-co` stylesheet with `.5rem` lateral canvas padding with `var(--site--gutter)` grid gap and attributes (data-wf-domain="www.paragonproduction...", data-wf-page="68be24b22b086720602bcd26", data-wf-site="68be24b22b086720602bcd38").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Skip to main content"*
- Copy Excerpt 2: *"Instagram Instagram Instagram"*
- Copy Excerpt 3: *"LinkedIn LinkedIn LinkedIn"*
- Copy Excerpt 4: *"ALWAYS IN PURSUIT //"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.23,1,.32,1)`, `cubic-bezier(.215,.61,.355,1)`, `cubic-bezier(.165,.84,.44,1)`
- **Extracted Stylesheet Rules (`www-paragonproductions-co`)**:
- `html.lenis body { height:auto }`
- `.lenis.lenis-stopped { overflow:clip }`
- `.lenis.lenis-smooth iframe { pointer-events:none }`
- `img { object-fit:cover;width:100%;max-width:100% }`
- `label { position:relative }`
- **Per-Selector Transition Rules**:
- **Selector `.u-button`**: `transition: box-shadow .4s,border-color .4s,color .4s,background-color .4s` extracted from `www-paragonproductions-co` stylesheet.
- **Selector `.nav_logo_wrap`**: `transition: background-color .3s` extracted from `www-paragonproductions-co` stylesheet.
- **Selector `.nav_menu_link`**: `transition: background-color .3s` extracted from `www-paragonproductions-co` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.23,1,.32,1)`)**: Governs interactive state transitions across `<nav.nav_wrap>` and `<section.home-services_wrap>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-paragonproductions-co`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
