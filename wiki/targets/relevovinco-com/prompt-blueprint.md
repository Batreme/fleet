---
title: "UI Prompt Blueprint: relevovinco-com"
date: 2026-11-15
target: "relevovinco-com"
status: analyzed
capture: dom
capture_desktop: dom
capture_mobile: dom
archetype: "Light-Substrate Editorial & Modular Grid System (`#d4b08f` canvas, `#1f140b` ink, `#6b4c34` accent)"
---

# UI Design System & Master Generation Blueprint: relevovinco-com

> **Relevo & Vinco — inkless packaging, pressed into the board** (https://relevovinco.com/) — Relevo & Vinco is an inkless packaging workshop in Porto. We emboss, deboss, die-cut and fold raw board so a brand is something people fe...

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Relevo & Vinco — inkless packaging, pressed into the board** (`https://relevovinco.com/`). Relevo & Vinco is an inkless packaging workshop in Porto. We emboss, deboss, die-cut and fold raw board so a brand is something people fe...
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#d4b08f` canvas, `#1f140b` ink, `#6b4c34` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#d4b08f` (`var(--color-1)` in `:root`) paired with `#1f140b` primary typography and `#6b4c34` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Gabarito` for display copy (`Stand out. Press in.`) with `Instrument Sans` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `900px` container bounds (`gap: 8px`, padding `4px`) with `cubic-bezier(.3,.7,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `900px` extracted from `relevovinco-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `4px` lateral canvas padding with `8px` grid gap.
- **Border Radius Scale**: `var(--radius-1)`, `var(--radius-2)`, `var(--radius-3)`, `999px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 900px`, `gap: 8px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `4px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:900px)`, `@media (prefers-reduced-motion:no-preference)`, `@media (max-width:767px)`, `@media (prefers-reduced-motion:no-preference)and (max-width:767px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#d4b08f` | `var(--color-1)` in `:root` |
| **Primary Typography Ink** | `#36261a` | `var(--color-2)` in `:root` |
| **Elevated Surface / Card Substrate** | `#f7e8d2` | `var(--color-3)` in `:root` |
| **Interactive Accent / Highlight** | `#6b4c34` | `var(--color-4)` in `:root` |
| **Secondary / Muted Copy** | `#47331f` | `var(--color-5)` in `:root` |
| **Structural Hairline Border** | `#1f140b` | `var(--color-6)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-1` | `#d4b08f` | Brand / Palette Token |
| `--color-2` | `#36261a` | Brand / Palette Token |
| `--color-3` | `#f7e8d2` | Brand / Palette Token |
| `--color-4` | `#6b4c34` | Brand / Palette Token |
| `--color-5` | `#47331f` | Brand / Palette Token |
| `--color-6` | `#1f140b` | Brand / Palette Token |
| `--font-1` | `"Gabarito", "Gabarito Fallback", "Arial", sans-serif` | Typography / Scale Token |
| `--font-2` | `"Instrument Sans", "Instrument Sans Fallback", "Arial", sans-serif` | Typography / Scale Token |
| `--radius-1` | `6px` | Elevation / Border Token |
| `--radius-2` | `50%` | Elevation / Border Token |
| `--radius-3` | `clamp(18px, 2.4vw, 34px)` | Elevation / Border Token |
| `--shadow-7` | `1px 1px 0 color-mix(in srgb, var(--color-3) 75%, transparent)` | Elevation / Border Token |
| `--shadow-14` | `10px 16px 18px color-mix(in srgb, var(--color-6) 32%, transparent)` | Elevation / Border Token |
| `--space-1` | `clamp(20px, 6.5vw, 96px)` | Layout / Spatial Grid Token |
| `--space-2` | `clamp(96px, 15vh, 180px)` | Layout / Spatial Grid Token |
| `--hero-cap` | `min(16vh, 11.2vw)` | Dimension / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Gabarito`.
- **Primary Body Stack**: `Instrument Sans`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `17px`, `clamp(18px,1.45vw,21px)`, `13px`, `clamp(22px,1.9vw,27px)`, `clamp(44px,6vw,92px)`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `17px`, `clamp(18px,1.45vw,21px)`, `13px`, `clamp(22px,1.9vw,27px)`, `clamp(44px,6vw,92px)`).
- **Body Copy**: rule `p` (`font-size: clamp(26px,2.8vw,42px)`, `line-height: 1.12`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `17px`, `clamp(18px,1.45vw,21px)`, `13px`, `clamp(22px,1.9vw,27px)`, `clamp(44px,6vw,92px)`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.3,.7,.2,1)`, `cubic-bezier(.2,.7,.2,1)`, `cubic-bezier(.2,.75,.15,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.lenis.lenis-autoToggle`**: `transition: 1ms` extracted from `relevovinco-com` stylesheet.
- **Selector `.m-btn`**: `transition: box-shadow .22s cubic-bezier(.3,.7,.2,1),transform .22s cubic-...` extracted from `relevovinco-com` stylesheet.
- **Selector `.m-btn::after`**: `transition: opacity .22s` extracted from `relevovinco-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.3,.7,.2,1)`)**: Governs interactive state transitions across `<header.lenis>` and `<section.relief-defs__shade>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Relevo & Vinco — inkless packaging, presse │
│ ====================================================================== │
│ [ <header.lenis>           | Finishes · Process · Work · Boards · C ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.relief-defs>                                |   │
│ | H1: Stand out. Press in.                                         |   │
│ | Substrate: #d4b08f    | Ink: #1f140b    | Accent: #6b4c34        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.relief-defs__shad) max-w: 900px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Ink fades. Foil peels. Press |  | Six ways to say it without i | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 8px   ) | │
│ | [<header.lenis>] -> [<section.relief-de] -> [<section.relief-de] |   │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.m-text-3>     ) | https://relevovinco.com/           │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.lenis> — `relevovinco-com`)**:
   - Landmark `<header class="lenis">` hosting `Relevo & Vinco — inkless packaging, ` navigation (`Finishes · Process · Work · Boards · Contact`), DOM attributes (`data-fonts`, `data-part="layers"`, `data-part="tokens"`, `data-part="base"`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.relief-defs> — `Stand out. Press in.`)**:
   - Landmark `<section class="relief-defs">` presenting display lead `Stand out. Press in.` and copy excerpt *"Relevo & Vinco is an inkless packaging workshop in Porto. We embo"* over `#d4b08f` canvas and `#1f140b` ink.
3. **Primary Showcase & Content Grid (<section.relief-defs__shade> — `Ink fades. Foil peels. Pressure st`)**:
   - Landmark `<section class="relief-defs__shade">` rendering section `Ink fades. Foil peels. Pressure stays.` with copy *"Order a sample kit"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `gabarito-a94f9001.woff2`), and grid rule `html { -webkit-text-size-adjust:100%;text-size-adjust:100% }`.
4. **Interactive Detail & Feature Matrix (<section.nav__bar> — `Six ways to say it without ink`)**:
   - Landmark `<section class="nav__bar">` framing `Six ways to say it without ink` and `Blind emboss` (*"Every box we make carries its brand in the board itself: raised w"*) with `#f7e8d2` surface cards, `#6b4c34` accents, and `img { display:block;max-width:100%;height:auto }`.
5. **Colophon & Global Directory Footer (<footer.m-text-3> — `https://relevovinco.com/`)**:
   - Landmark `<footer class="m-text-3">` anchoring `Relevo & Vinco — inkless packagi` footer links (`Finishes · Process · Work · Boards · Contact`), copy *"Nothing to scuff off in transit and nothing to separate at t"*, and `#1f140b` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: relevovinco-com (Relevo & Vinco — inkless packaging, pressed into the board)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `relevovinco-com` (**Relevo & Vinco — inkless packaging, pressed into the board** — `https://relevovinco.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#d4b08f` canvas, `#1f140b` ink, `#6b4c34` accent).
- **Identity & Domain Context**: Relevo & Vinco is an inkless packaging workshop in Porto. We emboss, deboss, die-cut and fold raw board so a brand is something people fe...
- **Primary Substrate**: `#d4b08f` (`var(--color-1)` in `:root`), **Primary Ink**: `#1f140b`, **Accent / Highlight**: `#6b4c34`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#d4b08f` (`var(--color-1)` in `:root`) paired with `#1f140b` primary typography and `#6b4c34` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Gabarito` for display copy (`Stand out. Press in.`) with `Instrument Sans` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `900px` container bounds (`gap: 8px`, padding `4px`) with `cubic-bezier(.3,.7,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `relevovinco-com` in your global stylesheet:

:root {
  /* Relevo & Vinco — inkless packaging, pressed into the board (relevovinco-com) — Ground-Truth Extracted CSS Variables */
  --color-1: #d4b08f; /* Brand / Palette Token (relevovinco-com) */
  --color-2: #36261a; /* Brand / Palette Token (relevovinco-com) */
  --color-3: #f7e8d2; /* Brand / Palette Token (relevovinco-com) */
  --color-4: #6b4c34; /* Brand / Palette Token (relevovinco-com) */
  --color-5: #47331f; /* Brand / Palette Token (relevovinco-com) */
  --color-6: #1f140b; /* Brand / Palette Token (relevovinco-com) */
  --font-1: "Gabarito", "Gabarito Fallback", "Arial", sans-serif; /* Typography / Scale Token (relevovinco-com) */
  --font-2: "Instrument Sans", "Instrument Sans Fallback", "Arial", sans-serif; /* Typography / Scale Token (relevovinco-com) */
  --radius-1: 6px; /* Elevation / Border Token (relevovinco-com) */
  --radius-2: 50%; /* Elevation / Border Token (relevovinco-com) */
  --radius-3: clamp(18px, 2.4vw, 34px); /* Elevation / Border Token (relevovinco-com) */
  --shadow-7: 1px 1px 0 color-mix(in srgb, var(--color-3) 75%, transparent); /* Elevation / Border Token (relevovinco-com) */
  --shadow-14: 10px 16px 18px color-mix(in srgb, var(--color-6) 32%, transparent); /* Elevation / Border Token (relevovinco-com) */
  --space-1: clamp(20px, 6.5vw, 96px); /* Layout / Spatial Grid Token (relevovinco-com) */
  --space-2: clamp(96px, 15vh, 180px); /* Layout / Spatial Grid Token (relevovinco-com) */
  --hero-cap: min(16vh, 11.2vw); /* Dimension / Scale Token (relevovinco-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#d4b08f` — grounded in `var(--color-1)` in `:root`
- **Primary Typography Ink**: `#36261a` — grounded in `var(--color-2)` in `:root`
- **Elevated Surface / Card Substrate**: `#f7e8d2` — grounded in `var(--color-3)` in `:root`
- **Interactive Accent / Highlight**: `#6b4c34` — grounded in `var(--color-4)` in `:root`
- **Secondary / Muted Copy**: `#47331f` — grounded in `var(--color-5)` in `:root`
- **Structural Hairline Border**: `#1f140b` — grounded in `var(--color-6)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `900px` extracted from `relevovinco-com` stylesheet
- **Padding & Gutters**: `4px` lateral canvas padding with `8px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 900px`, `gap: 8px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `4px` horizontal padding
- **Media Queries**: `@media (max-width:900px)`, `@media (prefers-reduced-motion:no-preference)`, `@media (max-width:767px)`, `@media (prefers-reduced-motion:no-preference)and (max-width:767px)`
- **Corner Radii**: `var(--radius-1)`, `var(--radius-2)`, `var(--radius-3)`, `999px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Gabarito`
- **Body Font Stack**: `Instrument Sans`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `17px`, `clamp(18px,1.45vw,21px)`, `13px`, `clamp(22px,1.9vw,27px)`, `clamp(44px,6vw,92px)`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `17px`, `clamp(18px,1.45vw,21px)`, `13px`, `clamp(22px,1.9vw,27px)`, `clamp(44px,6vw,92px)`)
- **Body Copy Rule**: rule `p` (`font-size: clamp(26px,2.8vw,42px)`, `line-height: 1.12`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `17px`, `clamp(18px,1.45vw,21px)`, `13px`, `clamp(22px,1.9vw,27px)`, `clamp(44px,6vw,92px)`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `relevovinco-com` (`Relevo & Vinco — inkless packaging, pressed into the board`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.lenis> — `relevovinco-com`)**:
   - DOM & Selectors: Landmark `<header class="lenis">` hosting `Relevo & Vinco — inkless packaging, ` navigation (`Finishes · Process · Work · Boards · Contact`), DOM attributes (`data-fonts`, `data-part="layers"`, `data-part="tokens"`, `data-part="base"`), and stylesheet rule `after { box-sizing:border-box }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.lenis> — `relevovinco-com`)` (`relevovinco-com`) adapts across `@media (max-width:900px)`, `@media (prefers-reduced-motion:no-preference)`, `@media (max-width:767px)`, `@media (prefers-reduced-motion:no-preference)and (max-width:767px)` with `cubic-bezier(.3,.7,.2,1)`, `cubic-bezier(.2,.7,.2,1)`, `cubic-bezier(.2,.75,.15,1)` transitions and links `Finishes · Process · Work · Boards · Contact`.
2. **Hero Stage & Focal Lead (<section.relief-defs> — `Stand out. Press in.`)**:
   - DOM & Selectors: Landmark `<section class="relief-defs">` presenting display lead `Stand out. Press in.` and copy excerpt *"Relevo & Vinco is an inkless packaging workshop in Porto. We embo"* over `#d4b08f` canvas and `#1f140b` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#d4b08f` background with `#1f140b` headline `Stand out. Press in.`.
3. **Primary Showcase & Content Grid (<section.relief-defs__shade> — `Ink fades. Foil peels. Pressure st`)**:
   - DOM & Selectors: Landmark `<section class="relief-defs__shade">` rendering section `Ink fades. Foil peels. Pressure stays.` with copy *"Order a sample kit"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `gabarito-a94f9001.woff2`), and grid rule `html { -webkit-text-size-adjust:100%;text-size-adjust:100% }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.relief-defs__shade> — `Ink fades. Foil peels. Pressure st`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 900px`, `gap: 8px`) on desktop and Single-column vertical stack at `390px` viewport width with `4px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.nav__bar> — `Six ways to say it without ink`)**:
   - DOM & Selectors: Landmark `<section class="nav__bar">` framing `Six ways to say it without ink` and `Blind emboss` (*"Every box we make carries its brand in the board itself: raised w"*) with `#f7e8d2` surface cards, `#6b4c34` accents, and `img { display:block;max-width:100%;height:auto }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.nav__bar> — `Six ways to say it without ink`)` uses `var(--radius-1)`, `var(--radius-2)`, `var(--radius-3)`, `999px` radii, `#6b4c34` highlights, and assets (favicon.ico, favicon.svg, apple-touch-icon.png).
5. **Colophon & Global Directory Footer (<footer.m-text-3> — `https://relevovinco.com/`)**:
   - DOM & Selectors: Landmark `<footer class="m-text-3">` anchoring `Relevo & Vinco — inkless packagi` footer links (`Finishes · Process · Work · Boards · Contact`), copy *"Nothing to scuff off in transit and nothing to separate at t"*, and `#1f140b` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.m-text-3> — `https://relevovinco.com/`)` aligns to `900px` extracted from `relevovinco-com` stylesheet with `4px` lateral canvas padding with `8px` grid gap and attributes (data-fonts, data-part="layers", data-part="tokens").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Relevo & Vinco is an inkless packaging workshop in Porto. We emboss, deboss, cut a..."*
- Copy Excerpt 2: *"Order a sample kit"*
- Copy Excerpt 3: *"Every box we make carries its brand in the board itself: raised where it should ca..."*
- Copy Excerpt 4: *"Nothing to scuff off in transit and nothing to separate at the recycling bin. The..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.3,.7,.2,1)`, `cubic-bezier(.2,.7,.2,1)`, `cubic-bezier(.2,.75,.15,1)`
- **Extracted Stylesheet Rules (`relevovinco-com`)**:
- `after { box-sizing:border-box }`
- `html { -webkit-text-size-adjust:100%;text-size-adjust:100% }`
- `img { display:block;max-width:100%;height:auto }`
- `select { font:inherit;color:inherit }`
- `focus-visible { outline:3px solid var(--color-2);outline-offset:3px }`
- **Per-Selector Transition Rules**:
- **Selector `.lenis.lenis-autoToggle`**: `transition: 1ms` extracted from `relevovinco-com` stylesheet.
- **Selector `.m-btn`**: `transition: box-shadow .22s cubic-bezier(.3,.7,.2,1),transform .22s cubic-...` extracted from `relevovinco-com` stylesheet.
- **Selector `.m-btn::after`**: `transition: opacity .22s` extracted from `relevovinco-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.3,.7,.2,1)`)**: Governs interactive state transitions across `<header.lenis>` and `<section.relief-defs__shade>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `relevovinco-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
