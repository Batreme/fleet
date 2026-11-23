---
title: "UI Prompt Blueprint: www-sigma-imaging-se"
date: 2026-11-23
captured_at: 2026-11-23
target: "www-sigma-imaging-se"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#fefefd` canvas, `#000000` ink, `#0077cb` accent)"
---

# UI Design System & Master Generation Blueprint: www-sigma-imaging-se

> **SIGMA Imaging Nordics & Baltics · Lenses, Cameras & Cine-lenses - Sigma** (https://www.sigma-imaging.se/) — Official SIGMA subsidiary for the Nordics and Baltics. Lenses and cameras Made in Aizu, Japan, with 5-year warranty, local support and fi...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **SIGMA Imaging Nordics & Baltics · Lenses, Cameras & Cine-lenses - Sigma** (`https://www.sigma-imaging.se/`). Official SIGMA subsidiary for the Nordics and Baltics. Lenses and cameras Made in Aizu, Japan, with 5-year warranty, local support and fi...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#fefefd` canvas, `#000000` ink, `#0077cb` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#fefefd` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#0077cb` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Sigma Serif Headline` for display copy (`SMALL, POWERFUL,`) with `Sigma Serif` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1456px` container bounds (`gap: 1rem`, padding `.5rem`) with `cubic-bezier(.4,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1456px` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `.5rem` lateral canvas padding with `1rem` grid gap.
- **Border Radius Scale**: `100%`, `.3125rem`, `.375rem`, `.125rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1456px`, `gap: 1rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `.5rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:768px)`, `@media (min-width:640px)`, `@media (min-width:1024px)`, `@media (min-width:1201px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#fefefd` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `p` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `var(--amscroll-background-color)` in `:root` |
| **Interactive Accent / Highlight** | `#0077cb` | `.mollie-buttons .button:hover { background-color: #0077cb }` |
| **Secondary / Muted Copy** | `#9c9c9c` | `var(--adp-color-secondary)` in `:root` |
| **Structural Hairline Border** | `#cccfd6` | `var(--amscroll-border-color)` in `:root` |
| **Variable Token (`--amscroll--text--color`)** | `#252525` | `var(--amscroll--text--color)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--amscroll-module--path` | `"../Amasty_Scroll"` | Design System Custom Token |
| `--amscroll--transition-duration` | `.2s` | Motion / Easing Token |
| `--amscroll--hover-filter` | `brightness(.8)` | Design System Custom Token |
| `--amscroll-loader--size` | `25px` | Layout / Spatial Grid Token |
| `--amscroll--text--color` | `#252525` | Typography Ink Token |
| `--amscroll-border-color` | `#cccfd6` | Brand / Palette Token |
| `--amscroll-background-color` | `#fff` | Canvas / Surface Token |
| `--amscroll--indent` | `10px` | Dimension / Scale Token |
| `--amscroll--indent--m` | `@amscroll--indent + @amscroll--indent/2` | Design System Custom Token |
| `--amscroll--indent--l` | `@amscroll--indent * 2` | Design System Custom Token |
| `--amscroll--indent--xl` | `@amscroll--indent--l + @amscroll--indent/2` | Design System Custom Token |
| `--amcart-background` | `#FFFFFF` | Canvas / Surface Token |
| `--amcart-product-name` | `#000000` | Color / Atmospheric Token |
| `--amcart-dialog-text` | `#000000` | Typography Ink Token |
| `--amcart-btn-text` | `#000000` | Typography Ink Token |
| `--amcart-continue-btn` | `#000000` | Color / Atmospheric Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Sigma Serif Headline`.
- **Primary Body Stack**: `Sigma Serif`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 48px`, `line-height: 52.8px`, `font-weight: 400`, `letter-spacing: 0.08px`); rule `h1` (`font-size: 2.25rem`, `line-height: 2.5rem`, `font-weight: 300`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 16px`, `line-height: 20px`, `font-weight: 400`, `letter-spacing: 0.08px`); rule `h2` (`font-size: 2.25rem`, `line-height: 2.5rem`, `font-weight: 300`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 20px`, `font-weight: 400`, `letter-spacing: 0.08px`); CSS variables `--ps-font-body: "Sigma Serif", serif`; rule `p` (`font-size: .8125rem`, `line-height: 125%`, `letter-spacing: .02em`, `font-weight: 400`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 20px`, `font-weight: 400`, `letter-spacing: 0.08px`); CSS variables `--amlabel-margin-between: 7px`, `--gap-amlabel-margin: var(--amlabel-margin-between)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,1,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.ambar-btn-accept`**: `transition: cubic-bezier(.4,0,.2,1)` extracted from `www-sigma-imaging-se` stylesheet.
- **Selector `.ambar-btn-allow`**: `transition: cubic-bezier(.4,0,.2,1)` extracted from `www-sigma-imaging-se` stylesheet.
- **Selector `.ambar-btn-decline`**: `transition: cubic-bezier(.4,0,.2,1)` extracted from `www-sigma-imaging-se` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.ammenu-header-container>` and `<section.cms-index-index>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — SIGMA Imaging Nordics & Baltics · Lenses,  │
│ ====================================================================== │
│ [ <header.ammenu-header- (1425x0px)   | Products · Made in Aizu · In ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.message> (w=1425px)                           | │
│ | H1: SMALL, POWERFUL,                                               | │
│ | Substrate: #fefefd | Ink: #000000 | Accent: #0077cb                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.cms-index-index>) max-w: 1456px            | │
│ | +------------------------------+  +------------------------------+ | │
│ | | ADAPTABLE                    |  | NEW PRODUCTS                 | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.page-layout-1colu) — FEATURED PRODUCTS     | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.page-footer>) | https://www.sigma-imaging.se/        │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 1rem)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.ammenu-header-co) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.message>) — 390px Vertical Lead               | │
│ | H1: SMALL, POWERFUL,                                               | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.cms-index-ind) — 1-Col Stack              | │
│ | [ Item 1: ADAPTABLE                                              ] | │
│ | [ Item 2: NEW PRODUCTS                                           ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.page-layout-1co) — 1-Col (FEATURED PRODUCTS)  │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.page-footer>) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.ammenu-header-container> — `www-sigma-imaging-se`)**:
   - Landmark `<header class="ammenu-header-container page-header">` (`1425x0px`) hosting `SIGMA Imaging Nordics & Baltics · Le` navigation (`Products · Made in Aizu · Inspiration · Support · News`), DOM attributes (`data-src="//www.googletagmanage..."`, `data-cfasync="false"`, `data-dialog-ref-name="am-cookie-bar"`, `data-dispatch-action="cookiebar-action-allow"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid ccc }`.
2. **Hero Stage & Focal Lead (<section.message> — `SMALL, POWERFUL,`)**:
   - Landmark `<section class="message global">` presenting display lead `SMALL, POWERFUL,` and copy excerpt *"We use cookies to help improve our services, make personal offers"* over `#fefefd` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.cms-index-index> — `ADAPTABLE`)**:
   - Landmark `<section class="cms-index-index">` rendering section `ADAPTABLE` with copy *"The Sigma FP2 is a camera fully designed around human creativity."*, asset references (`recaptcha__en.js`, `gtm.js`, `styles.css`, `eu-guarantee.css`), and grid rule `body { margin:0;line-height:inherit }`.
4. **Interactive Detail & Feature Matrix (<section.page-layout-1column> — `NEW PRODUCTS`)**:
   - Landmark `<section class="page-layout-1column">` framing `NEW PRODUCTS` and `FEATURED PRODUCTS` (*"Even in the digital age, taking a photograph is a deeply physical"*) with `#ffffff` surface cards, `#0077cb` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.page-footer> — `https://www.sigma-imaging.se/`)**:
   - Landmark `<footer class="page-footer">` anchoring `SIGMA Imaging Nordics & Baltics ` footer links (`Products · Made in Aizu · Inspiration · Support · News`), copy *"CONTEMPORARY 50 mm F1.4 CL DG"*, and `#cccfd6` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-sigma-imaging-se (SIGMA Imaging Nordics & Baltics · Lenses, Cameras & Cine-lenses - Sigma)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-sigma-imaging-se` (**SIGMA Imaging Nordics & Baltics · Lenses, Cameras & Cine-lenses - Sigma** — `https://www.sigma-imaging.se/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#fefefd` canvas, `#000000` ink, `#0077cb` accent).
- **Identity & Domain Context**: Official SIGMA subsidiary for the Nordics and Baltics. Lenses and cameras Made in Aizu, Japan, with 5-year warranty, local support and fi...
- **Primary Substrate**: `#fefefd` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#000000`, **Accent / Highlight**: `#0077cb`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#fefefd` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#0077cb` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Sigma Serif Headline` for display copy (`SMALL, POWERFUL,`) with `Sigma Serif` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1456px` container bounds (`gap: 1rem`, padding `.5rem`) with `cubic-bezier(.4,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-sigma-imaging-se` in your global stylesheet:

:root {
  /* SIGMA Imaging Nordics & Baltics · Lenses, Cameras & Cine-lenses - Sigma (www-sigma-imaging-se) — Live-Grounded CSS Variables */
  --amscroll-module--path: "../Amasty_Scroll"; /* Design System Custom Token (www-sigma-imaging-se) */
  --amscroll--transition-duration: .2s; /* Motion / Easing Token (www-sigma-imaging-se) */
  --amscroll--hover-filter: brightness(.8); /* Design System Custom Token (www-sigma-imaging-se) */
  --amscroll-loader--size: 25px; /* Layout / Spatial Grid Token (www-sigma-imaging-se) */
  --amscroll--text--color: #252525; /* Typography Ink Token (www-sigma-imaging-se) */
  --amscroll-border-color: #cccfd6; /* Brand / Palette Token (www-sigma-imaging-se) */
  --amscroll-background-color: #fff; /* Canvas / Surface Token (www-sigma-imaging-se) */
  --amscroll--indent: 10px; /* Dimension / Scale Token (www-sigma-imaging-se) */
  --amscroll--indent--m: @amscroll--indent + @amscroll--indent/2; /* Design System Custom Token (www-sigma-imaging-se) */
  --amscroll--indent--l: @amscroll--indent * 2; /* Design System Custom Token (www-sigma-imaging-se) */
  --amscroll--indent--xl: @amscroll--indent--l + @amscroll--indent/2; /* Design System Custom Token (www-sigma-imaging-se) */
  --amcart-background: #FFFFFF; /* Canvas / Surface Token (www-sigma-imaging-se) */
  --amcart-product-name: #000000; /* Color / Atmospheric Token (www-sigma-imaging-se) */
  --amcart-dialog-text: #000000; /* Typography Ink Token (www-sigma-imaging-se) */
  --amcart-btn-text: #000000; /* Typography Ink Token (www-sigma-imaging-se) */
  --amcart-continue-btn: #000000; /* Color / Atmospheric Token (www-sigma-imaging-se) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fefefd` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#000000` — grounded in live computed `p` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#ffffff` — grounded in `var(--amscroll-background-color)` in `:root`
- **Interactive Accent / Highlight**: `#0077cb` — grounded in `.mollie-buttons .button:hover { background-color: #0077cb }`
- **Secondary / Muted Copy**: `#9c9c9c` — grounded in `var(--adp-color-secondary)` in `:root`
- **Structural Hairline Border**: `#cccfd6` — grounded in `var(--amscroll-border-color)` in `:root`
- **Variable Token (`--amscroll--text--color`)**: `#252525` — grounded in `var(--amscroll--text--color)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1456px` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `.5rem` lateral canvas padding with `1rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1456px`, `gap: 1rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `.5rem` horizontal padding
- **Media Queries**: `@media (min-width:768px)`, `@media (min-width:640px)`, `@media (min-width:1024px)`, `@media (min-width:1201px)`
- **Corner Radii**: `100%`, `.3125rem`, `.375rem`, `.125rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Sigma Serif Headline`
- **Body Font Stack**: `Sigma Serif`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: live computed `h1` (`font-size: 48px`, `line-height: 52.8px`, `font-weight: 400`, `letter-spacing: 0.08px`); rule `h1` (`font-size: 2.25rem`, `line-height: 2.5rem`, `font-weight: 300`)
- **H2 Section Rule**: live computed `h2` (`font-size: 16px`, `line-height: 20px`, `font-weight: 400`, `letter-spacing: 0.08px`); rule `h2` (`font-size: 2.25rem`, `line-height: 2.5rem`, `font-weight: 300`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 20px`, `font-weight: 400`, `letter-spacing: 0.08px`); CSS variables `--ps-font-body: "Sigma Serif", serif`; rule `p` (`font-size: .8125rem`, `line-height: 125%`, `letter-spacing: .02em`, `font-weight: 400`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 20px`, `font-weight: 400`, `letter-spacing: 0.08px`); CSS variables `--amlabel-margin-between: 7px`, `--gap-amlabel-margin: var(--amlabel-margin-between)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-sigma-imaging-se` (`SIGMA Imaging Nordics & Baltics · Lenses, Cameras & Cine-lenses - Sigma`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.ammenu-header-container> — `www-sigma-imaging-se`)**:
   - DOM & Selectors: Landmark `<header class="ammenu-header-container page-header">` (`1425x0px`) hosting `SIGMA Imaging Nordics & Baltics · Le` navigation (`Products · Made in Aizu · Inspiration · Support · News`), DOM attributes (`data-src="//www.googletagmanage..."`, `data-cfasync="false"`, `data-dialog-ref-name="am-cookie-bar"`, `data-dispatch-action="cookiebar-action-allow"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid ccc }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.ammenu-header-container> — `www-sigma-imaging-se`)` (`www-sigma-imaging-se`) adapts across `@media (min-width:768px)`, `@media (min-width:640px)`, `@media (min-width:1024px)`, `@media (min-width:1201px)` with `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,1,1)` transitions and links `Products · Made in Aizu · Inspiration · Support · News`.
2. **Hero Stage & Focal Lead (<section.message> — `SMALL, POWERFUL,`)**:
   - DOM & Selectors: Landmark `<section class="message global">` presenting display lead `SMALL, POWERFUL,` and copy excerpt *"We use cookies to help improve our services, make personal offers"* over `#fefefd` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#fefefd` background with `#000000` headline `SMALL, POWERFUL,`.
3. **Primary Showcase & Content Grid (<section.cms-index-index> — `ADAPTABLE`)**:
   - DOM & Selectors: Landmark `<section class="cms-index-index">` rendering section `ADAPTABLE` with copy *"The Sigma FP2 is a camera fully designed around human creativity."*, asset references (`recaptcha__en.js`, `gtm.js`, `styles.css`, `eu-guarantee.css`), and grid rule `body { margin:0;line-height:inherit }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.cms-index-index> — `ADAPTABLE`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1456px`, `gap: 1rem`) on desktop and Single-column vertical stack at `390px` viewport width with `.5rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.page-layout-1column> — `NEW PRODUCTS`)**:
   - DOM & Selectors: Landmark `<section class="page-layout-1column">` framing `NEW PRODUCTS` and `FEATURED PRODUCTS` (*"Even in the digital age, taking a photograph is a deeply physical"*) with `#ffffff` surface cards, `#0077cb` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.page-layout-1column> — `NEW PRODUCTS`)` uses `100%`, `.3125rem`, `.375rem`, `.125rem` radii, `#0077cb` highlights, and assets (recaptcha__en.js, gtm.js, styles.css).
5. **Colophon & Global Directory Footer (<footer.page-footer> — `https://www.sigma-imaging.se/`)**:
   - DOM & Selectors: Landmark `<footer class="page-footer">` anchoring `SIGMA Imaging Nordics & Baltics ` footer links (`Products · Made in Aizu · Inspiration · Support · News`), copy *"CONTEMPORARY 50 mm F1.4 CL DG"*, and `#cccfd6` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.page-footer> — `https://www.sigma-imaging.se/`)` aligns to `1456px` (non-`@media` desktop container stylesheet rule) with `.5rem` lateral canvas padding with `1rem` grid gap and attributes (data-src="//www.googletagmanage...", data-cfasync="false", data-dialog-ref-name="am-cookie-bar").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"We use cookies to help improve our services, make personal offers, and enhance you..."*
- Copy Excerpt 2: *"The Sigma FP2 is a camera fully designed around human creativity. Purposefully dec..."*
- Copy Excerpt 3: *"Even in the digital age, taking a photograph is a deeply physical process. There i..."*
- Copy Excerpt 4: *"CONTEMPORARY 50 mm F1.4 CL DG"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,1,1)`
- **Extracted Stylesheet Rules (`www-sigma-imaging-se`)**:
- `before { box-sizing:border-box;border:0 solid ccc }`
- `body { margin:0;line-height:inherit }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- `sup { font-size:75%;line-height:0;position:relative;vertical-align:initial }`
- **Per-Selector Transition Rules**:
- **Selector `.ambar-btn-accept`**: `transition: cubic-bezier(.4,0,.2,1)` extracted from `www-sigma-imaging-se` stylesheet.
- **Selector `.ambar-btn-allow`**: `transition: cubic-bezier(.4,0,.2,1)` extracted from `www-sigma-imaging-se` stylesheet.
- **Selector `.ambar-btn-decline`**: `transition: cubic-bezier(.4,0,.2,1)` extracted from `www-sigma-imaging-se` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.ammenu-header-container>` and `<section.cms-index-index>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-sigma-imaging-se`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
