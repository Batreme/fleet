---
title: "UI Prompt Blueprint: www-tomdekoning-work"
date: 2026-11-23
captured_at: 2026-11-23
target: "www-tomdekoning-work"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#ffa500`)"
---

# UI Design System & Master Generation Blueprint: www-tomdekoning-work

> **tomdekoning.work — Building brands that turn heads** (https://www.tomdekoning.work/) — Freelance creative director in the Netherlands. Strategy, (web)design & development for brands that want to stand out. 8+ years experienc...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **tomdekoning.work — Building brands that turn heads** (`https://www.tomdekoning.work/`). Freelance creative director in the Netherlands. Strategy, (web)design & development for brands that want to stand out. 8+ years experienc...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#ffa500`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#000000` (live computed `canvas-modal-luma` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#ffa500` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Ppneuemontreal` for display copy (`t o mdek o ning .w o rk`) with `Playfair Display` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `80rem` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(.645,.045,.355,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `80rem` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `9px` lateral canvas padding with `16px` grid gap.
- **Border Radius Scale**: `3px`, `100%`, `50%`, `.125rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 80rem`, `gap: 16px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `canvas-modal-luma` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | `.w-button { color: #ffffff }` |
| **Elevated Surface / Card Substrate** | `#222222` | `.w-slider-nav-invert > div.w-ac... { background-color: #222222 }` |
| **Interactive Accent / Highlight** | `#ffa500` | `.button { background-color: orange }` (`#ffa500`) |
| **Secondary / Muted Copy** | `#808080` | `.text-color-grey { color: gray }` (`#808080`) |
| **Structural Hairline Border** | `#3898ec` | `.w-select:focus { border-color: #3898ec }` |
| **Variable Token (`--black`)** | `#0b0b0b` | `var(--black)` in `:root` |
| **Variable Token (`--sand`)** | `#e7e1d7` | `var(--sand)` in `:root` |
| **Variable Token (`--orange`)** | `#f34213` | `var(--orange)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--black` | `#0b0b0b` | Canvas / Surface Token |
| `--sand` | `#e7e1d7` | Color / Atmospheric Token |
| `--orange` | `#f34213` | Color / Atmospheric Token |
| `--white` | `white` | Canvas / Surface Token |
| `--button-097-color` | `#E7E1D7` | Brand / Palette Token |
| `--button-097-color-background` | `#F34213` | Canvas / Surface Token |
| `--button-097-hover-color` | `#0B0B0B` | Brand / Palette Token |
| `--button-097-hover-color-background` | `#E7E1D7` | Canvas / Surface Token |
| `--button-097-color-focus` | `#E7E1D7` | Brand / Palette Token |
| `--button-097-border-radius` | `0.5em` | Elevation / Border Token |
| `--button-097-dot-border-radius` | `0.25em` | Elevation / Border Token |
| `--button-097-padding-right` | `0.75em` | Layout / Spatial Grid Token |
| `--button-097-padding-left` | `1em` | Layout / Spatial Grid Token |
| `--button-097-gap` | `0.375em` | Layout / Spatial Grid Token |
| `--button-097-dot-size` | `0.5em` | Layout / Spatial Grid Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Ppneuemontreal`.
- **Primary Body Stack**: `Playfair Display`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 2em`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 32px`, `line-height: 36px`).
- **Body Copy**: rule `body` (`font-size: 14px`, `line-height: 20px`).
- **Metadata & Navigation Labels**: rule `small` (`font-size: 80%`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.645,.045,.355,1)`, `cubic-bezier(0.32,0.72,0,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.w-webflow-badge > img`**: `transition: unset` extracted from `www-tomdekoning-work` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s, color .1s` extracted from `www-tomdekoning-work` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `www-tomdekoning-work` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.645,.045,.355,1)`)**: Governs interactive state transitions across `<nav.navbar>` and `<section.wf-playfairdisplay-n6-active>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Locomotive Scroll Parallax with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — tomdekoning.work — Building brands that tu │
│ ====================================================================== │
│ [ <nav.navbar> (1440px)               | MENU                         ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.w-mod-ix> (w=1440px)                          | │
│ | H1: t o mdek o ning .w o rk                                        | │
│ | Substrate: #000000 | Ink: #ffffff | Accent: #ffa500                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.wf-playfairdispla) max-w: 80rem            | │
│ | +------------------------------+  +------------------------------+ | │
│ | | A B O U T A B O U T          |  | C O N T A C T C O N T A C T  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.wf-playfairdispla) — I kill average brands | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.wf-playfaird) | https://www.tomdekoning.work/        │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px)       │
│ ====================================================================== │
│ [ HEADER BAR (<nav.navbar>            ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.w-mod-ix>) — 390px Vertical Lead              | │
│ | H1: t o mdek o ning .w o rk                                        | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.wf-playfairdi) — 1-Col Stack              | │
│ | [ Item 1: A B O U T A B O U T                                    ] | │
│ | [ Item 2: C O N T A C T C O N T A C T                            ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.wf-playfairdisp) — 1-Col (I kill average bra) │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.wf-playfaird) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.navbar> — `www-tomdekoning-work`)**:
   - Landmark `<nav class="navbar">` (`1440px`) hosting `tomdekoning.work — Building brands t` navigation (`MENU`), DOM attributes (`data-wf-domain="www.tomdekoning.work"`, `data-wf-page="6a981ab95ec4bc0363c7f6b9"`, `data-wf-site="6947d4a42871d2972031e9ab"`, `data-scroll-orientation="vertical"`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<section.w-mod-ix> — `t o mdek o ning .w o rk`)**:
   - Landmark `<section class="w-mod-ix">` presenting display lead `t o mdek o ning .w o rk` and copy excerpt *"A B O U T A B O U T"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.wf-playfairdisplay-n6-active> — `A B O U T A B O U T`)**:
   - Landmark `<section class="wf-playfairdisplay-n6-active">` rendering section `A B O U T A B O U T` with copy *"C O N T A C T C O N T A C T"*, asset references (`cdn.prod.website-files.com`, `tdk-work.webflow.shared.09be52ab1...`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.wf-playfairdisplay-n5-active> — `C O N T A C T C O N T A C T`)**:
   - Landmark `<section class="wf-playfairdisplay-n5-active">` framing `C O N T A C T C O N T A C T` and `I kill average brands and rebuild them, stronger` (*"I kill average brands and rebuild them, stronger, sharper, unforg"*) with `#222222` surface cards, `#ffa500` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.wf-playfairdisplay-n3-active> — `https://www.tomdekoning.work/`)**:
   - Landmark `<footer class="wf-playfairdisplay-n3-active">` anchoring `tomdekoning.work — Building bran` footer links (`MENU`), copy *"I’m a freelance creative director based in the Netherlands. "*, and `#3898ec` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-tomdekoning-work (tomdekoning.work — Building brands that turn heads)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-tomdekoning-work` (**tomdekoning.work — Building brands that turn heads** — `https://www.tomdekoning.work/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#ffa500`).
- **Identity & Domain Context**: Freelance creative director in the Netherlands. Strategy, (web)design & development for brands that want to stand out. 8+ years experienc...
- **Primary Substrate**: `#000000` (live computed `canvas-modal-luma` `background-color` (`computed_styles.json`)), **Primary Ink**: `#ffffff`, **Accent / Highlight**: `#ffa500`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#000000` (live computed `canvas-modal-luma` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#ffa500` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Ppneuemontreal` for display copy (`t o mdek o ning .w o rk`) with `Playfair Display` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `80rem` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(.645,.045,.355,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-tomdekoning-work` in your global stylesheet:

:root {
  /* tomdekoning.work — Building brands that turn heads (www-tomdekoning-work) — Live-Grounded CSS Variables */
  --w-backdrop-animation: initial; /* Motion / Easing Token (www-tomdekoning-work) */
  --black: #0b0b0b; /* Canvas / Surface Token (www-tomdekoning-work) */
  --sand: #e7e1d7; /* Color / Atmospheric Token (www-tomdekoning-work) */
  --orange: #f34213; /* Color / Atmospheric Token (www-tomdekoning-work) */
  --white: white; /* Canvas / Surface Token (www-tomdekoning-work) */
  --button-097-color: #E7E1D7; /* Brand / Palette Token (www-tomdekoning-work) */
  --button-097-color-background: #F34213; /* Canvas / Surface Token (www-tomdekoning-work) */
  --button-097-hover-color: #0B0B0B; /* Brand / Palette Token (www-tomdekoning-work) */
  --button-097-hover-color-background: #E7E1D7; /* Canvas / Surface Token (www-tomdekoning-work) */
  --button-097-color-focus: #E7E1D7; /* Brand / Palette Token (www-tomdekoning-work) */
  --button-097-border-radius: 0.5em; /* Elevation / Border Token (www-tomdekoning-work) */
  --button-097-dot-border-radius: 0.25em; /* Elevation / Border Token (www-tomdekoning-work) */
  --button-097-padding-right: 0.75em; /* Layout / Spatial Grid Token (www-tomdekoning-work) */
  --button-097-padding-left: 1em; /* Layout / Spatial Grid Token (www-tomdekoning-work) */
  --button-097-gap: 0.375em; /* Layout / Spatial Grid Token (www-tomdekoning-work) */
  --button-097-dot-size: 0.5em; /* Layout / Spatial Grid Token (www-tomdekoning-work) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000000` — grounded in live computed `canvas-modal-luma` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#ffffff` — grounded in `.w-button { color: #ffffff }`
- **Elevated Surface / Card Substrate**: `#222222` — grounded in `.w-slider-nav-invert > div.w-ac... { background-color: #222222 }`
- **Interactive Accent / Highlight**: `#ffa500` — grounded in `.button { background-color: orange }` (`#ffa500`)
- **Secondary / Muted Copy**: `#808080` — grounded in `.text-color-grey { color: gray }` (`#808080`)
- **Structural Hairline Border**: `#3898ec` — grounded in `.w-select:focus { border-color: #3898ec }`
- **Variable Token (`--black`)**: `#0b0b0b` — grounded in `var(--black)` in `:root`
- **Variable Token (`--sand`)**: `#e7e1d7` — grounded in `var(--sand)` in `:root`
- **Variable Token (`--orange`)**: `#f34213` — grounded in `var(--orange)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `80rem` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `9px` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 80rem`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding
- **Media Queries**: `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)`
- **Corner Radii**: `3px`, `100%`, `50%`, `.125rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Ppneuemontreal`
- **Body Font Stack**: `Playfair Display`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: rule `h1` (`font-size: 2em`)
- **H2 Section Rule**: rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy Rule**: rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Index Rule**: rule `small` (`font-size: 80%`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-tomdekoning-work` (`tomdekoning.work — Building brands that turn heads`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.navbar> — `www-tomdekoning-work`)**:
   - DOM & Selectors: Landmark `<nav class="navbar">` (`1440px`) hosting `tomdekoning.work — Building brands t` navigation (`MENU`), DOM attributes (`data-wf-domain="www.tomdekoning.work"`, `data-wf-page="6a981ab95ec4bc0363c7f6b9"`, `data-wf-site="6947d4a42871d2972031e9ab"`, `data-scroll-orientation="vertical"`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.navbar> — `www-tomdekoning-work`)` (`www-tomdekoning-work`) adapts across `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)` with `cubic-bezier(.645,.045,.355,1)`, `cubic-bezier(0.32,0.72,0,1)` transitions and links `MENU`.
2. **Hero Stage & Focal Lead (<section.w-mod-ix> — `t o mdek o ning .w o rk`)**:
   - DOM & Selectors: Landmark `<section class="w-mod-ix">` presenting display lead `t o mdek o ning .w o rk` and copy excerpt *"A B O U T A B O U T"* over `#000000` canvas and `#ffffff` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#000000` background with `#ffffff` headline `t o mdek o ning .w o rk`.
3. **Primary Showcase & Content Grid (<section.wf-playfairdisplay-n6-active> — `A B O U T A B O U T`)**:
   - DOM & Selectors: Landmark `<section class="wf-playfairdisplay-n6-active">` rendering section `A B O U T A B O U T` with copy *"C O N T A C T C O N T A C T"*, asset references (`cdn.prod.website-files.com`, `tdk-work.webflow.shared.09be52ab1...`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `body { margin: 0; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.wf-playfairdisplay-n6-active> — `A B O U T A B O U T`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 80rem`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `9px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.wf-playfairdisplay-n5-active> — `C O N T A C T C O N T A C T`)**:
   - DOM & Selectors: Landmark `<section class="wf-playfairdisplay-n5-active">` framing `C O N T A C T C O N T A C T` and `I kill average brands and rebuild them, stronger` (*"I kill average brands and rebuild them, stronger, sharper, unforg"*) with `#222222` surface cards, `#ffa500` accents, and `summary { display: block; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.wf-playfairdisplay-n5-active> — `C O N T A C T C O N T A C T`)` uses `3px`, `100%`, `50%`, `.125rem` radii, `#ffa500` highlights, and assets (cdn.prod.website-files.com, tdk-work.webflow.shared.09be52ab1..., fonts.googleapis.com).
5. **Colophon & Global Directory Footer (<footer.wf-playfairdisplay-n3-active> — `https://www.tomdekoning.work/`)**:
   - DOM & Selectors: Landmark `<footer class="wf-playfairdisplay-n3-active">` anchoring `tomdekoning.work — Building bran` footer links (`MENU`), copy *"I’m a freelance creative director based in the Netherlands. "*, and `#3898ec` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.wf-playfairdisplay-n3-active> — `https://www.tomdekoning.work/`)` aligns to `80rem` (non-`@media` desktop container stylesheet rule) with `9px` lateral canvas padding with `16px` grid gap and attributes (data-wf-domain="www.tomdekoning.work", data-wf-page="6a981ab95ec4bc0363c7f6b9", data-wf-site="6947d4a42871d2972031e9ab").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"A B O U T A B O U T"*
- Copy Excerpt 2: *"C O N T A C T C O N T A C T"*
- Copy Excerpt 3: *"I kill average brands and rebuild them, stronger, sharper, unforgettable."*
- Copy Excerpt 4: *"I’m a freelance creative director based in the Netherlands. I bring strategy, desi..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.645,.045,.355,1)`, `cubic-bezier(0.32,0.72,0,1)`
- **Extracted Stylesheet Rules (`www-tomdekoning-work`)**:
- `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`
- `body { margin: 0; }`
- `summary { display: block; }`
- `video { vertical-align: baseline; display: inline-block; }`
- `template { display: none; }`
- **Per-Selector Transition Rules**:
- **Selector `.w-webflow-badge > img`**: `transition: unset` extracted from `www-tomdekoning-work` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s, color .1s` extracted from `www-tomdekoning-work` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `www-tomdekoning-work` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.645,.045,.355,1)`)**: Governs interactive state transitions across `<nav.navbar>` and `<section.wf-playfairdisplay-n6-active>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Locomotive Scroll Parallax with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-tomdekoning-work`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
