---
title: "UI Prompt Blueprint: www-anduril-com"
date: 2026-11-15
target: "[[overview|www-anduril-com]]"
archetype: "Mission-Critical Defense Autonomy Platform & Odometer Telemetry Grid (`HelveticaNowDisplay` + `Elios`)"
---

# UI Design System & Master Generation Blueprint: www-anduril-com

> **Anduril Industries · Transforming U.S. Defense Capabilities with Advanced Technology** — An authoritative defense hardware and autonomous systems platform engineered around near-black stealth carbon (`--theme-color-background: #010101`), stark optic white (`--theme-color-text: #fff`), warm bone light-theme chapters (`.theme-light` / `#f1f0ea`), and high-visibility radar volt-yellow (`#dff140`) and alert red (`#ff3535`) indicators.

![Desktop Viewport Capture (1440x5230)](file:///root/projects/fleet/wiki/targets/www-anduril-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Anduril Industries · Transforming U.S. Defense Capabilities with Advanced Technology**. An authoritative defense hardware and autonomous systems platform engineered around near-black stealth carbon (`--theme-color-background: #010101`), stark optic white (`--theme-color-text: #fff`), warm bone light-theme chapters (`.theme-light` / `#f1f0ea`), and high-visibility radar volt-yellow (`#dff140`) and alert red (`#ff3535`) indicators.
- **Visual Archetype**: **Mission-Critical Defense Autonomy Platform & Odometer Telemetry Grid (`HelveticaNowDisplay` + `Elios`)**.
- **Anti-AI-Slop Differentiators**:
  1. **Programmatic Theme Polarity Switching**: Uses root CSS state variables (`--theme-color-background: #010101`, `--theme-color-text: #fff`) that invert dynamically on `.theme-light` chapters (`#f1f0ea` / `#fff` background with `#010101` ink).
  2. **Mechanical Odometer Metric Rollers**: Driven by custom CSS math (`--roller-scale: 1`, `--roller-font-size: calc(3rem*var(--roller-scale))`, `--roller-column-height: calc(2.5rem*var(--roller-scale))`, `--roller-digit-width: calc(1.8rem*var(--roller-scale))`).
  3. **Tactical Hardware Showcase Matrix**: Full-viewport autonomous system modules (`H2: Arsenal-2`, `H2: Steelfin`, `H2: Barracuda`) with aspect-ratio locked containers (`--in-production-h: max(505px,100vw*505/403)`).
  4. **Precision Industrial Typography**: Combines `HelveticaNowDisplay` for authoritative headlines with custom technical display face `Elios` for system designations and telemetry readouts.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x6917)](file:///root/projects/fleet/wiki/targets/www-anduril-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Full-Page Dimensions**: Desktop `1440×5230px` (`assets/desktop.png`), Mobile `390×6917px` (`assets/mobile.png`).
- **Master Container Bounds**: Full-bleed `100vw` tactical viewports with `@media (min-width:1440px)` and `@media (min-width:1920px)` max-bounds.
- **Canvas Lateral Padding & Spacing**: Responsive horizontal padding scaling across `@media (min-width:400px)`, `768px`, `1280px`, `1440px`, `1920px`.
- **Border Radius Scale**: `0px` razor-sharp corners across all cards and plates; circular `.CircleButton` (`border: 1px solid #fff`) for directional triggers.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Full-bleed stacked hardware plates (`Arsenal-2`, `Steelfin`, `Barracuda`) and multi-column telemetry counters.
- **Mobile Layout**: Controlled via `--is-mob: 1` inside `@media (max-width:768px)`, activating `<nav class="HeaderMobile lenis">`.
- **Extracted CSS Media Queries**: `@media (max-width:768px)` (`--is-mob: 1`), `@media (min-width:400px)`, `@media (min-width:768px)`, `@media (min-width:1280px)`, `@media (min-width:1440px)`, `@media (min-width:1920px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| Primary Dark Substrate | `#010101` | `--theme-color-background` (`:root`) |
| Pure Black Base | `#000000` | `--base-color: black` (`:root`) |
| Light-Theme Paper Surface | `#f1f0ea` | Extracted stylesheet surface hex (`#f1f0ea` / `.theme-light`) |
| Elevated Slate Surface | `#2f3234` | Extracted stylesheet dark panel hex (`#2f3234`) |
| Primary White Ink | `#fff` | `--theme-color-text` / `--linkbutton-color` (`:root`) |
| Secondary Muted Ink | `#b0b0a9` | Extracted stylesheet muted neutral (`#b0b0a9`) |
| Dimmed Technical Ink | `#565654` | Extracted stylesheet dim gray (`#565654`) |
| Radar Volt-Yellow Accent | `#dff140` | Extracted stylesheet high-visibility accent (`#dff140`) |
| Alert Warning Red | `#ff3535` | Extracted stylesheet warning indicator (`#ff3535`) |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--is-mob` | `0` | Viewport breakpoint flag (switches to `1` at `max-width: 768px`) |
| `--theme-color-background` | `#010101` | Primary stealth carbon background surface |
| `--theme-color-text` | `#fff` | Primary high-contrast text ink |
| `--base-color` | `black` | Base substrate color keyword |
| `--contrast-color` | `white` | High-contrast foreground keyword |
| `--linkbutton-color` | `#fff` | Default `.LinkButton` & `.CircleButton` foreground |
| `--linkbutton-hover-color` | `#010101` | Inverted button label ink on hover fill |
| `--roller-scale` | `1` | Scale multiplier for mechanical odometer counters |
| `--roller-font-size` | `calc(3rem*var(--roller-scale))` | Odometer digit font size |
| `--roller-column-height` | `calc(2.5rem*var(--roller-scale))` | Odometer vertical slot height |
| `--roller-digit-width` | `calc(1.8rem*var(--roller-scale))` | Odometer fixed monospace digit width |
| `--links-height` | `0px` | Collapsible navigation submenu height state |
| `--frosted` | `0` | Header backdrop frosted glass state toggle |
| `--backgroundOpacity` | `0` | Dynamic scroll overlay opacity value |
| `--in-production-h` | `max(505px,100vw*505/403)` | Responsive aspect-ratio height for production showcase |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `HelveticaNowDisplay, Helvetica, Arial, sans-serif` paired with `Elios, sans-serif`.
- **Primary Body Stack**: `HelveticaNowDisplay, Helvetica, Arial, sans-serif`.
- **Technical / Metadata Stack**: `Elios, monospace` (Odometer telemetry counters, autonomous system designations).

### Typographic Scale & Rules
- **Hero Display (`H1`)**: `clamp(2.75rem, 5.5vw, 5.25rem)`, `font-family: HelveticaNowDisplay, sans-serif`, `font-weight: 500`, `line-height: 0.98`, `letter-spacing: -0.03em`.
- **Section Heading (`H2`)**: `clamp(2rem, 4vw, 3.75rem)`, `font-family: HelveticaNowDisplay, sans-serif` ("Arsenal-2", "Steelfin", "Barracuda").
- **Body Copy**: `1rem (16px)`, `font-family: HelveticaNowDisplay, Helvetica, Arial, sans-serif`, `line-height: 1.55`, `color: #b0b0a9`.
- **Metadata & Navigation Labels**: `0.75rem (12px)`, `font-family: Elios, sans-serif`, `letter-spacing: 0.1em`, `text-transform: uppercase`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.215,.62,.34,1)` (custom tactical ease-out).

### Per-Element Transition & Choreography Rules
- `Button & Link Reveals (.CircleButton, .LinkButton)` -> `transition: all 350ms cubic-bezier(.215,.62,.34,1)` (invert fill from `#010101` to `#fff` with `--linkbutton-hover-color: #010101`)
- `Odometer Digit Columns` -> vertical `translateY` slot rotation scaled by `--roller-column-height: calc(2.5rem*var(--roller-scale))`
- `Lenis Smooth Scroll (<nav class="HeaderMobile lenis">)` -> inertia-damped viewport scrolling synchronized with `--backgroundOpacity`

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ <header class="header"> <nav class="HeaderDesktop"> (Bg: #010101, Text │
│   [ANDURIL]   [Lattice] [Arsenal] [Air] [Maritime] [Subsea] [Mission]  │
├────────────────────────────────────────────────────────────────────────┤
│ <main> Hero Mission Stage (Substrate: --theme-color-background #010101 │
│   Title: Transforming U.S. Defense Capabilities with Advanced Technolo │
│   [ .CircleButton (1px solid #fff) ]  [ Telemetry Odometer (--roller-* │
├────────────────────────────────────────────────────────────────────────┤
│ <section class="hardware-matrix"> (Full-Bleed Autonomous Systems)      │
│   [ H2: Arsenal-2 (Hyperscale Mfg) ] │ [ H2: Steelfin (Autonomous UUV) │
│   [ H2: Barracuda (Autonomous AAV) ] │ [ Height: --in-production-h     │
├────────────────────────────────────────────────────────────────────────┤
│ <footer class="Footer"> [Lattice OS] [Careers] [Newsroom] © Anduril    │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Desktop & Mobile Header (`<header class="header">`, `<nav class="HeaderDesktop">`, and `<nav class="HeaderMobile lenis">`)**:
   - Fixed top bar controlled by `--frosted` and `--links-height`, switching to `HeaderMobile` when `--is-mob: 1` (`@media (max-width:768px)`).
2. **Hero Autonomy Viewport (`<main>`)**:
   - Full-bleed dark stage (`--theme-color-background: #010101`) with `HelveticaNowDisplay` headline and `.CircleButton` (`1px solid #fff`, hover fill `#fff` with `--linkbutton-hover-color: #010101`) triggers.
3. **Autonomous Systems Matrix (`H2: Arsenal-2`, `H2: Steelfin`, `H2: Barracuda`)**:
   - Stacked and split hardware modules sized via `--in-production-h: max(505px,100vw*505/403)` showcasing defense platforms with `Elios` technical indices and `#dff140` radar accents.
4. **Odometer Telemetry Section (`--roller-font-size`, `--roller-column-height`, `--roller-digit-width`)**:
   - Mechanical rolling digit counters sized via `calc(3rem*var(--roller-scale))` on `.theme-light` (`#f1f0ea`) and `#2f3234` slate substrates.
5. **Global Footer (`<footer class="Footer">`)**:
   - Structured defense directory linking Lattice, Force Protection, and Careers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-anduril-com (Anduril Industries · Transforming U.S. Defense Capabilities with Advanced Technology)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-anduril-com` (Anduril Industries · Transforming U.S. Defense Capabilities with Advanced Technology).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Mission-Critical Defense Autonomy Platform & Odometer Telemetry Grid (`HelveticaNowDisplay` + `Elios`).
- **Primary Substrate**: `#010101` (`--theme-color-background` (`:root`)), **Primary Ink**: `#fff`, **Accent / Highlight**: `#ff3535`.
- **Site-Specific Differentiators**:
  1. **Programmatic Theme Polarity Switching**: Uses root CSS state variables (`--theme-color-background: #010101`, `--theme-color-text: #fff`) that invert dynamically on `.theme-light` chapters (`#f1f0ea` / `#fff` background with `#010101` ink).
  2. **Mechanical Odometer Metric Rollers**: Driven by custom CSS math (`--roller-scale: 1`, `--roller-font-size: calc(3rem*var(--roller-scale))`, `--roller-column-height: calc(2.5rem*var(--roller-scale))`, `--roller-digit-width: calc(1.8rem*var(--roller-scale))`).
  3. **Tactical Hardware Showcase Matrix**: Full-viewport autonomous system modules (`H2: Arsenal-2`, `H2: Steelfin`, `H2: Barracuda`) with aspect-ratio locked containers (`--in-production-h: max(505px,100vw*505/403)`).
  4. **Precision Industrial Typography**: Combines `HelveticaNowDisplay` for authoritative headlines with custom technical display face `Elios` for system designations and telemetry readouts.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-anduril-com` in your global stylesheet:

:root {
  /* Anduril Industries · Transforming U.S. Defense Capabilities with Advanced Technology — Ground-Truth Extracted CSS Variables */
  --is-mob: 0; /* Viewport breakpoint flag (switches to `1` at `max-width: 768px`) */
  --theme-color-background: #010101; /* Primary stealth carbon background surface */
  --theme-color-text: #fff; /* Primary high-contrast text ink */
  --base-color: black; /* Base substrate color keyword */
  --contrast-color: white; /* High-contrast foreground keyword */
  --linkbutton-color: #fff; /* Default `.LinkButton` & `.CircleButton` foreground */
  --linkbutton-hover-color: #010101; /* Inverted button label ink on hover fill */
  --roller-scale: 1; /* Scale multiplier for mechanical odometer counters */
  --roller-font-size: calc(3rem*var(--roller-scale)); /* Odometer digit font size */
  --roller-column-height: calc(2.5rem*var(--roller-scale)); /* Odometer vertical slot height */
  --roller-digit-width: calc(1.8rem*var(--roller-scale)); /* Odometer fixed monospace digit width */
  --links-height: 0px; /* Collapsible navigation submenu height state */
  --frosted: 0; /* Header backdrop frosted glass state toggle */
  --backgroundOpacity: 0; /* Dynamic scroll overlay opacity value */
  --in-production-h: max(505px,100vw*505/403); /* Responsive aspect-ratio height for production showcase */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Dark Substrate**: `#010101` — grounded in `--theme-color-background` (`:root`)
- **Pure Black Base**: `#000000` — grounded in `--base-color: black` (`:root`)
- **Light-Theme Paper Surface**: `#f1f0ea` — grounded in Extracted stylesheet surface hex (`#f1f0ea` / `.theme-light`)
- **Elevated Slate Surface**: `#2f3234` — grounded in Extracted stylesheet dark panel hex (`#2f3234`)
- **Primary White Ink**: `#fff` — grounded in `--theme-color-text` / `--linkbutton-color` (`:root`)
- **Secondary Muted Ink**: `#b0b0a9` — grounded in Extracted stylesheet muted neutral (`#b0b0a9`)
- **Dimmed Technical Ink**: `#565654` — grounded in Extracted stylesheet dim gray (`#565654`)
- **Radar Volt-Yellow Accent**: `#dff140` — grounded in Extracted stylesheet high-visibility accent (`#dff140`)
- **Alert Warning Red**: `#ff3535` — grounded in Extracted stylesheet warning indicator (`#ff3535`)

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×5230px` full-page capture (`1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×6917px` full-page capture (`390px` standard mobile width).
- **Container Max-Width**: Full-bleed `100vw` tactical viewports with `@media (min-width:1440px)` and `@media (min-width:1920px)` max-bounds
- **Padding & Gutters**: Responsive horizontal padding scaling across `@media (min-width:400px)`, `768px`, `1280px`, `1440px`, `1920px`
- **Desktop Grid**: Full-bleed stacked hardware plates (`Arsenal-2`, `Steelfin`, `Barracuda`) and multi-column telemetry counters
- **Mobile Adaptation**: Controlled via `--is-mob: 1` inside `@media (max-width:768px)`, activating `<nav class="HeaderMobile lenis">`
- **Media Queries**: `@media (max-width:768px)` (`--is-mob: 1`), `@media (min-width:400px)`, `@media (min-width:768px)`, `@media (min-width:1280px)`, `@media (min-width:1440px)`, `@media (min-width:1920px)`
- **Corner Radii**: `0px` razor-sharp corners across all cards and plates; circular `.CircleButton` (`border: 1px solid #fff`) for directional triggers

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `HelveticaNowDisplay, Helvetica, Arial, sans-serif` paired with `Elios, sans-serif`
- **Body Font Stack**: `HelveticaNowDisplay, Helvetica, Arial, sans-serif`
- **Monospace / Technical Font Stack**: `Elios, monospace` (Odometer telemetry counters, autonomous system designations)
- **H1 Display Rule**: `clamp(2.75rem, 5.5vw, 5.25rem)`, `font-family: HelveticaNowDisplay, sans-serif`, `font-weight: 500`, `line-height: 0.98`, `letter-spacing: -0.03em`
- **H2 Section Rule**: `clamp(2rem, 4vw, 3.75rem)`, `font-family: HelveticaNowDisplay, sans-serif` ("Arsenal-2", "Steelfin", "Barracuda")
- **Body Copy Rule**: `1rem (16px)`, `font-family: HelveticaNowDisplay, Helvetica, Arial, sans-serif`, `line-height: 1.55`, `color: #b0b0a9`
- **Metadata & Index Rule**: `0.75rem (12px)`, `font-family: Elios, sans-serif`, `letter-spacing: 0.1em`, `text-transform: uppercase`

### 6. Component Hierarchy & Real DOM Landmarks
Scaffold the interface with these exact structural regions and class selectors from `www-anduril-com`:
1. **Desktop & Mobile Header (`<header class="header">`, `<nav class="HeaderDesktop">`, and `<nav class="HeaderMobile lenis">`)**:
   - Architecture & Selectors: Fixed top bar controlled by `--frosted` and `--links-height`, switching to `HeaderMobile` when `--is-mob: 1` (`@media (max-width:768px)`).
   - Layout & State Contract: Sticky/fixed top header navigation adapting across `@media (max-width:768px)` (`--is-mob: 1`), `@media (min-width:400px)`, `@media (min-width:768px)`, `@media (min-width:1280px)`, `@media (min-width:1440px)`, `@media (min-width:1920px)` with `cubic-bezier(.215,.62,.34,1)` (custom tactical ease-out) menu transitions.
2. **Hero Autonomy Viewport (`<main>`)**:
   - Architecture & Selectors: Full-bleed dark stage (`--theme-color-background: #010101`) with `HelveticaNowDisplay` headline and `.CircleButton` (`1px solid #fff`, hover fill `#fff` with `--linkbutton-hover-color: #010101`) triggers.
   - Layout & State Contract: Full-viewport hero stage (`1440px` desktop / `390px` mobile) pairing `#010101` substrate with `#fff` display typography (`H1`).
3. **Autonomous Systems Matrix (`H2: Arsenal-2`, `H2: Steelfin`, `H2: Barracuda`)**:
   - Architecture & Selectors: Stacked and split hardware modules sized via `--in-production-h: max(505px,100vw*505/403)` showcasing defense platforms with `Elios` technical indices and `#dff140` radar accents.
   - Layout & State Contract: Primary showcase grid executing Full-bleed stacked hardware plates (`Arsenal-2`, `Steelfin`, `Barracuda`) and multi-column telemetry counters on desktop and Controlled via `--is-mob: 1` inside `@media (max-width:768px)`, activating `<nav class="HeaderMobile lenis">` on mobile.
4. **Odometer Telemetry Section (`--roller-font-size`, `--roller-column-height`, `--roller-digit-width`)**:
   - Architecture & Selectors: Mechanical rolling digit counters sized via `calc(3rem*var(--roller-scale))` on `.theme-light` (`#f1f0ea`) and `#2f3234` slate substrates.
   - Layout & State Contract: Interactive specification & narrative module framed by `0px` razor-sharp corners across all cards and plates; circular `.CircleButton` (`border: 1px solid #fff`) for directional triggers and `#ff3535` highlights.
5. **Global Footer (`<footer class="Footer">`)**:
   - Architecture & Selectors: Structured defense directory linking Lattice, Force Protection, and Careers.
   - Layout & State Contract: Footer directory and utility bar anchored to Full-bleed `100vw` tactical viewports with `@media (min-width:1440px)` and `@media (min-width:1920px)` max-bounds with Responsive horizontal padding scaling across `@media (min-width:400px)`, `768px`, `1280px`, `1440px`, `1920px` lateral gutters.

### 7. Motion & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.215,.62,.34,1)` (custom tactical ease-out)
- **Per-Selector Transition Rules**:
- `Button & Link Reveals (.CircleButton, .LinkButton)` -> `transition: all 350ms cubic-bezier(.215,.62,.34,1)` (invert fill from `#010101` to `#fff` with `--linkbutton-hover-color: #010101`)
- `Odometer Digit Columns` -> vertical `translateY` slot rotation scaled by `--roller-column-height: calc(2.5rem*var(--roller-scale))`
- `Lenis Smooth Scroll (<nav class="HeaderMobile lenis">)` -> inertia-damped viewport scrolling synchronized with `--backgroundOpacity`

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
