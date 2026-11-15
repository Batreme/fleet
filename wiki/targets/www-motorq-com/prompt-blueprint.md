---
title: "UI Prompt Blueprint: www-motorq-com"
date: 2026-11-15
target: "[[overview|www-motorq-com]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#c1b2a2` canvas, `#31273f` ink, `#ff6f6f` accent)"
---

# UI Design System & Master Generation Blueprint: www-motorq-com

> **Motorq · Turn Connected Vehicle Data Into Decisions** (https://www.motorq.com/) — More than telematics. Motorq turns data from 25+ automaker brands into decisions, with no hardware to install. Run safer, leaner, more pr...

![Desktop Viewport Capture (1440x12694)](file:///root/projects/fleet/wiki/targets/www-motorq-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Motorq · Turn Connected Vehicle Data Into Decisions** (`https://www.motorq.com/`). More than telematics. Motorq turns data from 25+ automaker brands into decisions, with no hardware to install. Run safer, leaner, more pr...
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#c1b2a2` canvas, `#31273f` ink, `#ff6f6f` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#c1b2a2` (`var(--_color-palette---beige)` in `:root`) paired with `#31273f` primary typography and `#ff6f6f` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Manrope` for display copy (`Turn vehicle intelligence into actio`) with `Arial` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `940px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(0.32,0.72,0,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/www-motorq-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×12694px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `940px` extracted from `www-motorq-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `9px` lateral canvas padding with `16px` grid gap.
- **Border Radius Scale**: `3px`, `100%`, `50%`, `2px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#c1b2a2` | `var(--_color-palette---beige)` in `:root` |
| **Primary Typography Ink** | `#31273f` | `var(--_themes---form--checkbox-border)` in `:root` |
| **Elevated Surface / Card Substrate** | `#686868` | `var(--_themes---form--input-placeholder)` in `:root` |
| **Interactive Accent / Highlight** | `#ff6f6f` | `var(--_themes---form--error-msg-color)` in `:root` |
| **Secondary / Muted Copy** | `#fff0` | `var(--_color-palette---transparent)` in `:root` |
| **Structural Hairline Border** | `#d5ccc4` | `var(--_color-palette---light-beige)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--_themes---background--primary` | `var(--_color-palette---cream)` | Canvas / Surface Token |
| `--_typography---base--font` | `var(--_typography---primary-font)` | Typography / Scale Token |
| `--_themes---typography--paragraph` | `var(--_color-palette---black)` | Brand / Palette Token |
| `--_typography---base--size` | `1rem` | Layout / Spatial Grid Token |
| `--_typography---base--line-height` | `1.4` | Typography / Scale Token |
| `--_typography---base--weight` | `var(--_typography---weights--400-normal)` | Design System Custom Token |
| `--_typography---base--letter-spacing` | `0rem` | Typography / Scale Token |
| `--_typography---primary-font` | `Manrope,Arial,sans-serif` | Brand / Palette Token |
| `--_themes---typography--heading` | `var(--_color-palette---black)` | Typography Ink Token |
| `--_typography---h1--size` | `3.5rem` | Typography / Scale Token |
| `--_typography---h1--line-height` | `1.1` | Typography / Scale Token |
| `--_typography---h1--weight` | `var(--_typography---weights--400-normal)` | Typography / Scale Token |
| `--_typography---h1--letter-spacing` | `0rem` | Typography / Scale Token |
| `--_typography---h2--size` | `3rem` | Typography / Scale Token |
| `--_typography---h2--line-height` | `1.1` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Manrope`.
- **Primary Body Stack**: `Arial`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--_typography---h1--size: 3.5rem`, `--_typography---h1--line-height: 1.1`, `--_typography---h1--weight: var(--_typography---weights--400-normal)`; rule `h1` (`font-size: 2.125rem`).
- **Section Heading (`H2`)**: CSS variables `--_typography---h2--size: 3rem`, `--_typography---h2--line-height: 1.1`, `--_typography---h2--weight: var(--_typography---weights--400-normal)`; rule `h2` (`font-size: 1.125rem`, `font-weight: var(--_typogr...`).
- **Body Copy**: CSS variables `--_themes---typography--paragraph: var(--_color-palette---black)`; rule `p` (`font-size: var(--_typography---text-md--...`, `line-height: 1.5`).
- **Metadata & Navigation Labels**: CSS variables `--_typography---base--letter-spacing: 0rem`, `--_typography---h1--letter-spacing: 0rem`, `--_typography---h2--letter-spacing: 0rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.32,0.72,0,1)`, `cubic-bezier(.19,1,.22,1)`, `cubic-bezier(0.215,0.61,0.355,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.w-webflow-badge>img`**: `transition: unset` extracted from `www-motorq-com` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s,color .1s` extracted from `www-motorq-com` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `www-motorq-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.32,0.72,0,1)`)**: Governs interactive state transitions across `<nav.nav_menu>` and `<section.section>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Motorq · Turn Connected Vehicle Data Into  │
│ ====================================================================== │
│ [ <nav.nav_menu>           | Commercial Fleets · Rental Fleets · De ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero>                                       |   │
│ | H1: Turn vehicle intelligence into action into action            |   │
│ | Substrate: #c1b2a2    | Ink: #31273f    | Accent: #ff6f6f        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.section>         ) max-w: 940px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Live Webinar: Scaling Connec |  | Skip telematics devices. Con | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px  ) | │
│ | [<nav.nav_menu>] -> [<section.hero>] -> [<section.section>] |        │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>       ) | https://www.motorq.com/            │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.nav_menu> — `www-motorq-com`)**:
   - Landmark `<nav class="nav_menu w-nav-menu">` hosting `Motorq · Turn Connected Vehicle Data` navigation (`Commercial Fleets · Rental Fleets · Dealerships · Lenders · OEMs`), DOM attributes (`data-wf-domain="www.motorq.com"`, `data-wf-page="6a61fa87ccdad47899c19eb0"`, `data-wf-site="6a61fa87ccdad47899c19edd"`, `data-cky-tag="revisit-consent"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Turn vehicle intelligence into act`)**:
   - Landmark `<section class="hero u-overflow-hidden">` presenting display lead `Turn vehicle intelligence into action into action` and copy excerpt *"We value your privacy"* over `#c1b2a2` canvas and `#31273f` ink.
3. **Primary Showcase & Content Grid (<section.section> — `Live Webinar: Scaling Connected Fl`)**:
   - Landmark `<section class="section u-bg-transparent">` rendering section `Live Webinar: Scaling Connected Fleets Without Ha...` with copy *"We use cookies to enhance your browsing experience, serve persona"*, asset references (`cdn.prod.website-files.com`, `motorq123.webflow.shared.f3e1ce02...`, `script.js`, `gtm.js`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.section> — `Skip telematics devices. Connect d`)**:
   - Landmark `<section class="section u-bg-transparent">` framing `Skip telematics devices. Connect directly to OEM-...` and `Automotive brands` (*"Customize Consent Preferences"*) with `#686868` surface cards, `#ff6f6f` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://www.motorq.com/`)**:
   - Landmark `<footer class="footer">` anchoring `Motorq · Turn Connected Vehicle ` footer links (`Commercial Fleets · Rental Fleets · Dealerships · Lenders · OEMs`), copy *"We use cookies to help you navigate efficiently and perform "*, and `#d5ccc4` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-motorq-com (Motorq · Turn Connected Vehicle Data Into Decisions)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-motorq-com` (**Motorq · Turn Connected Vehicle Data Into Decisions** — `https://www.motorq.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#c1b2a2` canvas, `#31273f` ink, `#ff6f6f` accent).
- **Identity & Domain Context**: More than telematics. Motorq turns data from 25+ automaker brands into decisions, with no hardware to install. Run safer, leaner, more pr...
- **Primary Substrate**: `#c1b2a2` (`var(--_color-palette---beige)` in `:root`), **Primary Ink**: `#31273f`, **Accent / Highlight**: `#ff6f6f`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#c1b2a2` (`var(--_color-palette---beige)` in `:root`) paired with `#31273f` primary typography and `#ff6f6f` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Manrope` for display copy (`Turn vehicle intelligence into actio`) with `Arial` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `940px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(0.32,0.72,0,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-motorq-com` in your global stylesheet:

:root {
  /* Motorq · Turn Connected Vehicle Data Into Decisions (www-motorq-com) — Ground-Truth Extracted CSS Variables */
  --w-backdrop-animation: initial; /* Motion / Easing Token (www-motorq-com) */
  --_themes---background--primary: var(--_color-palette---cream); /* Canvas / Surface Token (www-motorq-com) */
  --_typography---base--font: var(--_typography---primary-font); /* Typography / Scale Token (www-motorq-com) */
  --_themes---typography--paragraph: var(--_color-palette---black); /* Brand / Palette Token (www-motorq-com) */
  --_typography---base--size: 1rem; /* Layout / Spatial Grid Token (www-motorq-com) */
  --_typography---base--line-height: 1.4; /* Typography / Scale Token (www-motorq-com) */
  --_typography---base--weight: var(--_typography---weights--400-normal); /* Design System Custom Token (www-motorq-com) */
  --_typography---base--letter-spacing: 0rem; /* Typography / Scale Token (www-motorq-com) */
  --_typography---primary-font: Manrope,Arial,sans-serif; /* Brand / Palette Token (www-motorq-com) */
  --_themes---typography--heading: var(--_color-palette---black); /* Typography Ink Token (www-motorq-com) */
  --_typography---h1--size: 3.5rem; /* Typography / Scale Token (www-motorq-com) */
  --_typography---h1--line-height: 1.1; /* Typography / Scale Token (www-motorq-com) */
  --_typography---h1--weight: var(--_typography---weights--400-normal); /* Typography / Scale Token (www-motorq-com) */
  --_typography---h1--letter-spacing: 0rem; /* Typography / Scale Token (www-motorq-com) */
  --_typography---h2--size: 3rem; /* Typography / Scale Token (www-motorq-com) */
  --_typography---h2--line-height: 1.1; /* Typography / Scale Token (www-motorq-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#c1b2a2` — grounded in `var(--_color-palette---beige)` in `:root`
- **Primary Typography Ink**: `#31273f` — grounded in `var(--_themes---form--checkbox-border)` in `:root`
- **Elevated Surface / Card Substrate**: `#686868` — grounded in `var(--_themes---form--input-placeholder)` in `:root`
- **Interactive Accent / Highlight**: `#ff6f6f` — grounded in `var(--_themes---form--error-msg-color)` in `:root`
- **Secondary / Muted Copy**: `#fff0` — grounded in `var(--_color-palette---transparent)` in `:root`
- **Structural Hairline Border**: `#d5ccc4` — grounded in `var(--_color-palette---light-beige)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×12694px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `940px` extracted from `www-motorq-com` stylesheet
- **Padding & Gutters**: `9px` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding
- **Media Queries**: `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)`
- **Corner Radii**: `3px`, `100%`, `50%`, `2px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Manrope`
- **Body Font Stack**: `Arial`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--_typography---h1--size: 3.5rem`, `--_typography---h1--line-height: 1.1`, `--_typography---h1--weight: var(--_typography---weights--400-normal)`; rule `h1` (`font-size: 2.125rem`)
- **H2 Section Rule**: CSS variables `--_typography---h2--size: 3rem`, `--_typography---h2--line-height: 1.1`, `--_typography---h2--weight: var(--_typography---weights--400-normal)`; rule `h2` (`font-size: 1.125rem`, `font-weight: var(--_typogr...`)
- **Body Copy Rule**: CSS variables `--_themes---typography--paragraph: var(--_color-palette---black)`; rule `p` (`font-size: var(--_typography---text-md--...`, `line-height: 1.5`)
- **Metadata & Index Rule**: CSS variables `--_typography---base--letter-spacing: 0rem`, `--_typography---h1--letter-spacing: 0rem`, `--_typography---h2--letter-spacing: 0rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-motorq-com` (`Motorq · Turn Connected Vehicle Data Into Decisions`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.nav_menu> — `www-motorq-com`)**:
   - DOM & Selectors: Landmark `<nav class="nav_menu w-nav-menu">` hosting `Motorq · Turn Connected Vehicle Data` navigation (`Commercial Fleets · Rental Fleets · Dealerships · Lenders · OEMs`), DOM attributes (`data-wf-domain="www.motorq.com"`, `data-wf-page="6a61fa87ccdad47899c19eb0"`, `data-wf-site="6a61fa87ccdad47899c19edd"`, `data-cky-tag="revisit-consent"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.nav_menu> — `www-motorq-com`)` (`www-motorq-com`) adapts across `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)` with `cubic-bezier(0.32,0.72,0,1)`, `cubic-bezier(.19,1,.22,1)`, `cubic-bezier(0.215,0.61,0.355,1)` transitions and links `Commercial Fleets · Rental Fleets · Dealerships · Lenders · OEMs`.
2. **Hero Stage & Focal Lead (<section.hero> — `Turn vehicle intelligence into act`)**:
   - DOM & Selectors: Landmark `<section class="hero u-overflow-hidden">` presenting display lead `Turn vehicle intelligence into action into action` and copy excerpt *"We value your privacy"* over `#c1b2a2` canvas and `#31273f` ink.
   - Responsive Contract: Hero stage (`1440×12694px` desktop / `390×2400px` mobile) sets `#c1b2a2` background with `#31273f` headline `Turn vehicle intelligence into action into action`.
3. **Primary Showcase & Content Grid (<section.section> — `Live Webinar: Scaling Connected Fl`)**:
   - DOM & Selectors: Landmark `<section class="section u-bg-transparent">` rendering section `Live Webinar: Scaling Connected Fleets Without Ha...` with copy *"We use cookies to enhance your browsing experience, serve persona"*, asset references (`cdn.prod.website-files.com`, `motorq123.webflow.shared.f3e1ce02...`, `script.js`, `gtm.js`), and grid rule `summary { display:block }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.section> — `Live Webinar: Scaling Connected Fl`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `9px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.section> — `Skip telematics devices. Connect d`)**:
   - DOM & Selectors: Landmark `<section class="section u-bg-transparent">` framing `Skip telematics devices. Connect directly to OEM-...` and `Automotive brands` (*"Customize Consent Preferences"*) with `#686868` surface cards, `#ff6f6f` accents, and `video { vertical-align:baseline;display:inline-block }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.section> — `Skip telematics devices. Connect d`)` uses `3px`, `100%`, `50%`, `2px` radii, `#ff6f6f` highlights, and assets (cdn.prod.website-files.com, motorq123.webflow.shared.f3e1ce02..., script.js).
5. **Colophon & Global Directory Footer (<footer.footer> — `https://www.motorq.com/`)**:
   - DOM & Selectors: Landmark `<footer class="footer">` anchoring `Motorq · Turn Connected Vehicle ` footer links (`Commercial Fleets · Rental Fleets · Dealerships · Lenders · OEMs`), copy *"We use cookies to help you navigate efficiently and perform "*, and `#d5ccc4` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer> — `https://www.motorq.com/`)` aligns to `940px` extracted from `www-motorq-com` stylesheet with `9px` lateral canvas padding with `16px` grid gap and attributes (data-wf-domain="www.motorq.com", data-wf-page="6a61fa87ccdad47899c19eb0", data-wf-site="6a61fa87ccdad47899c19edd").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"We value your privacy"*
- Copy Excerpt 2: *"We use cookies to enhance your browsing experience, serve personalized ads or cont..."*
- Copy Excerpt 3: *"Customize Consent Preferences"*
- Copy Excerpt 4: *"We use cookies to help you navigate efficiently and perform certain functions. You..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.32,0.72,0,1)`, `cubic-bezier(.19,1,.22,1)`, `cubic-bezier(0.215,0.61,0.355,1)`
- **Extracted Stylesheet Rules (`www-motorq-com`)**:
- `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`
- `summary { display:block }`
- `video { vertical-align:baseline;display:inline-block }`
- `template { display:none }`
- `strong { font-weight:700 }`
- **Per-Selector Transition Rules**:
- **Selector `.w-webflow-badge>img`**: `transition: unset` extracted from `www-motorq-com` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s,color .1s` extracted from `www-motorq-com` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `www-motorq-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.32,0.72,0,1)`)**: Governs interactive state transitions across `<nav.nav_menu>` and `<section.section>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-motorq-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
