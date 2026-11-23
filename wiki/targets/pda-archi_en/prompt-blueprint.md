---
title: "UI Prompt Blueprint: pda-archi_en"
date: 2026-11-23
captured_at: 2026-11-23
target: "pda-archi_en"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#eceae5` canvas, `#161616` ink, `#2c2f31` accent)"
---

# UI Design System & Master Generation Blueprint: pda-archi_en

> **Architecture firm in Paris: renovation, refurbishment — PDA** (https://pda.archi/en) — PDA, Partners & Dalous Architecture, transforms office, hospitality and residential buildings in Paris: renovation, refurbishment, vertic...

![Desktop Viewport Capture (1440x900)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Architecture firm in Paris: renovation, refurbishment — PDA** (`https://pda.archi/en`). PDA, Partners & Dalous Architecture, transforms office, hospitality and residential buildings in Paris: renovation, refurbishment, vertic...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#eceae5` canvas, `#161616` ink, `#2c2f31` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#eceae5` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#161616` primary typography and `#2c2f31` accents.
  - **Grounded Typographic Hierarchy**: Pairs `SequelSans` for display copy (`PDA, Partners & Dalous Architecture,`) with `SequelSans` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `120rem` container bounds (`gap: 52px normal`, padding `1rem`) with `cubic-bezier(.23,1,.32,1)` easing and Lenis Smooth Scroll (`data-lenis`).

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x844)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×900px` (`assets/desktop.png`, single-viewport 100vh live capture (900px)), Mobile `390×844px` (`assets/mobile.png`, single-viewport 100vh live capture (844px)).
- **Master Container Bounds**: `120rem` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `1rem` lateral canvas padding with `52px normal` grid gap.
- **Border Radius Scale**: `100px`, `.5rem`, `.4rem`, `1rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 120rem`, `gap: 52px normal`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `1rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (min-width:640px)`, `@media (prefers-reduced-motion)`, `@media screen and (max-width:640px)`, `@media (min-width:40rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#eceae5` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#161616` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `var(--cc-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#2c2f31` | `var(--cc-primary-color)` in `:root` |
| **Secondary / Muted Copy** | `#5e6266` | `var(--cc-secondary-color)` in `:root` |
| **Structural Hairline Border** | `#d4dae0` | `var(--cc-btn-secondary-hover-border-color)` in `:root` |
| **Variable Token (`--cc-btn-primary-bg`)** | `#30363c` | `var(--cc-btn-primary-bg)` in `:root` |
| **Variable Token (`--cc-btn-primary-hover-bg`)** | `#000000` | `var(--cc-btn-primary-hover-bg)` in `:root` |
| **Variable Token (`--cc-btn-secondary-bg`)** | `#eaeff2` | `var(--cc-btn-secondary-bg)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--cc-modal-border-radius` | `.5rem` | Elevation / Border Token |
| `--cc-btn-border-radius` | `.4rem` | Elevation / Border Token |
| `--cc-modal-transition-duration` | `.25s` | Motion / Easing Token |
| `--cc-link-color` | `var(--cc-btn-primary-bg)` | Typography Ink Token |
| `--cc-modal-margin` | `1rem` | Layout / Spatial Grid Token |
| `--cc-z-index` | `2147483647` | Elevation / Border Token |
| `--cc-bg` | `#fff` | Canvas / Surface Token |
| `--cc-primary-color` | `#2c2f31` | Brand / Palette Token |
| `--cc-secondary-color` | `#5e6266` | Brand / Palette Token |
| `--cc-btn-primary-bg` | `#30363c` | Canvas / Surface Token |
| `--cc-btn-primary-color` | `#fff` | Brand / Palette Token |
| `--cc-btn-primary-border-color` | `var(--cc-btn-primary-bg)` | Brand / Palette Token |
| `--cc-btn-primary-hover-bg` | `#000` | Canvas / Surface Token |
| `--cc-btn-primary-hover-color` | `#fff` | Brand / Palette Token |
| `--cc-btn-primary-hover-border-color` | `var(--cc-btn-primary-hover-bg)` | Brand / Palette Token |
| `--cc-btn-secondary-bg` | `#eaeff2` | Canvas / Surface Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `SequelSans`.
- **Primary Body Stack**: `SequelSans`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 60px`, `line-height: 60px`, `font-weight: 600`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 48px`, `line-height: 48px`, `font-weight: 600`); rule `h2` (`font-size: var(--text-24)`, `line-height: var(--spacing-full)`, `font-weight: var(--font-we...`).
- **Body Copy**: live computed `body` (`font-size: 15px`, `line-height: 16.5px`, `font-weight: 500`); CSS variables `--font-body: "SequelSans",sans-serif`; rule `p` (`font-size: var(--text-17)`, `line-height: 110%`, `font-weight: var(--font-we...`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 15px`, `line-height: 16.5px`, `font-weight: 500`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: 1.33333`, `--text-sm: .875rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.23,1,.32,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.25,.46,.45,.9)`.

### Per-Element Transition & Choreography Rules
- **Selector `:root`**: `transition: .25s` extracted from `pda-archi_en` stylesheet.
- **Selector `#cc-main a`**: `transition: background-size .25s,color .25s ease` extracted from `pda-archi_en` stylesheet.
- **Selector `media(prefers-reduced-motion)`**: `transition: 0s` extracted from `pda-archi_en` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.23,1,.32,1)`)**: Governs interactive state transitions across `<header.header>` and `<section.grid-w>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`) with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Architecture firm in Paris: renovation, re │
│ ====================================================================== │
│ [ <header.header> (1440x900px)        | Projects · Expertise · Studi ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.h-screen-mobile> (w=1440px)                   | │
│ | H1: PDA, Partners & Dalous Architecture, an architect...           | │
│ | Substrate: #eceae5 | Ink: #161616 | Accent: #2c2f31                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.grid-w>) max-w: 120rem                     | │
│ | +------------------------------+  +------------------------------+ | │
│ | | 49 Champs-Élysées            |  | 68 Faubourg Saint-Honoré     | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.mt-68>) — 118 Champs-Élysées               | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>     ) | https://pda.archi/en                 │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 52px nor)   │
│ ====================================================================== │
│ [ HEADER BAR (<header.header>         ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.h-screen-mobile) — 390px Vertical Lead        | │
│ | H1: PDA, Partners & Dalous Architecture, an architect...           | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.grid-w>) — 1-Col Stack                    | │
│ | [ Item 1: 49 Champs-Élysées                                      ] | │
│ | [ Item 2: 68 Faubourg Saint-Honoré                               ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.mt-68>) — 1-Col (118 Champs-Élysées)        | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>     ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.header> — `pda-archi_en`)**:
   - Landmark `<header class="header top-0">` (`1440x900px`) hosting `Architecture firm in Paris: renovati` navigation (`Projects · Expertise · Studio · Team · Digital Lab`), DOM attributes (`data-hid="ld-agency"`, `data-dark`, `data-block="aboutBlock"`, `data-src="https://pub-4eb76b4c2..."`), and stylesheet rule `cc-main span { all:unset;box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.h-screen-mobile> — `PDA, Partners & Dalous Architectur`)**:
   - Landmark `<section class="h-screen-mobile relative">` presenting display lead `PDA, Partners & Dalous Architecture, an architect...` and copy excerpt *"Transform uses, keep the"* over `#eceae5` canvas and `#161616` ink.
3. **Primary Showcase & Content Grid (<section.grid-w> — `49 Champs-Élysées`)**:
   - Landmark `<section class="grid-w pt-margin">` rendering section `49 Champs-Élysées` with copy *"Refurbish rather than"*, asset references (`BPdaeD0G.js`, `uCyaXeDn.js`, `D_MfmCAi.js`, `CO_3Dqrm.js`), and grid rule `cc-main button { all:initial;box-sizing:border-box;color:unset;visibility:unset }`.
4. **Interactive Detail & Feature Matrix (<section.mt-68> — `68 Faubourg Saint-Honoré`)**:
   - Landmark `<section class="mt-68 relative">` framing `68 Faubourg Saint-Honoré` and `118 Champs-Élysées` (*"Build where the city is"*) with `#ffffff` surface cards, `#2c2f31` accents, and `cc-main tr { all:revert;color:inherit;font-family:inherit;font-size:inherit;font-weig... }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://pda.archi/en`)**:
   - Landmark `<footer class="footer bg-black">` anchoring `Architecture firm in Paris: reno` footer links (`Projects · Expertise · Studio · Team · Digital Lab`), copy *"5 avenue de l'Opéra 75001 Paris"*, and `#d4dae0` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: pda-archi_en (Architecture firm in Paris: renovation, refurbishment — PDA)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `pda-archi_en` (**Architecture firm in Paris: renovation, refurbishment — PDA** — `https://pda.archi/en`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#eceae5` canvas, `#161616` ink, `#2c2f31` accent).
- **Identity & Domain Context**: PDA, Partners & Dalous Architecture, transforms office, hospitality and residential buildings in Paris: renovation, refurbishment, vertic...
- **Primary Substrate**: `#eceae5` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#161616`, **Accent / Highlight**: `#2c2f31`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#eceae5` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#161616` primary typography and `#2c2f31` accents.
  - **Grounded Typographic Hierarchy**: Pairs `SequelSans` for display copy (`PDA, Partners & Dalous Architecture,`) with `SequelSans` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `120rem` container bounds (`gap: 52px normal`, padding `1rem`) with `cubic-bezier(.23,1,.32,1)` easing and Lenis Smooth Scroll (`data-lenis`).

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `pda-archi_en` in your global stylesheet:

:root {
  /* Architecture firm in Paris: renovation, refurbishment — PDA (pda-archi_en) — Live-Grounded CSS Variables */
  --cc-modal-border-radius: .5rem; /* Elevation / Border Token (pda-archi_en) */
  --cc-btn-border-radius: .4rem; /* Elevation / Border Token (pda-archi_en) */
  --cc-modal-transition-duration: .25s; /* Motion / Easing Token (pda-archi_en) */
  --cc-link-color: var(--cc-btn-primary-bg); /* Typography Ink Token (pda-archi_en) */
  --cc-modal-margin: 1rem; /* Layout / Spatial Grid Token (pda-archi_en) */
  --cc-z-index: 2147483647; /* Elevation / Border Token (pda-archi_en) */
  --cc-bg: #fff; /* Canvas / Surface Token (pda-archi_en) */
  --cc-primary-color: #2c2f31; /* Brand / Palette Token (pda-archi_en) */
  --cc-secondary-color: #5e6266; /* Brand / Palette Token (pda-archi_en) */
  --cc-btn-primary-bg: #30363c; /* Canvas / Surface Token (pda-archi_en) */
  --cc-btn-primary-color: #fff; /* Brand / Palette Token (pda-archi_en) */
  --cc-btn-primary-border-color: var(--cc-btn-primary-bg); /* Brand / Palette Token (pda-archi_en) */
  --cc-btn-primary-hover-bg: #000; /* Canvas / Surface Token (pda-archi_en) */
  --cc-btn-primary-hover-color: #fff; /* Brand / Palette Token (pda-archi_en) */
  --cc-btn-primary-hover-border-color: var(--cc-btn-primary-hover-bg); /* Brand / Palette Token (pda-archi_en) */
  --cc-btn-secondary-bg: #eaeff2; /* Canvas / Surface Token (pda-archi_en) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#eceae5` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#161616` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#ffffff` — grounded in `var(--cc-bg)` in `:root`
- **Interactive Accent / Highlight**: `#2c2f31` — grounded in `var(--cc-primary-color)` in `:root`
- **Secondary / Muted Copy**: `#5e6266` — grounded in `var(--cc-secondary-color)` in `:root`
- **Structural Hairline Border**: `#d4dae0` — grounded in `var(--cc-btn-secondary-hover-border-color)` in `:root`
- **Variable Token (`--cc-btn-primary-bg`)**: `#30363c` — grounded in `var(--cc-btn-primary-bg)` in `:root`
- **Variable Token (`--cc-btn-primary-hover-bg`)**: `#000000` — grounded in `var(--cc-btn-primary-hover-bg)` in `:root`
- **Variable Token (`--cc-btn-secondary-bg`)**: `#eaeff2` — grounded in `var(--cc-btn-secondary-bg)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×900px` (single-viewport 100vh live capture (900px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×844px` (single-viewport 100vh live capture (844px), `390px` standard mobile width).
- **Container Max-Width**: `120rem` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `1rem` lateral canvas padding with `52px normal` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 120rem`, `gap: 52px normal`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `1rem` horizontal padding
- **Media Queries**: `@media screen and (min-width:640px)`, `@media (prefers-reduced-motion)`, `@media screen and (max-width:640px)`, `@media (min-width:40rem)`
- **Corner Radii**: `100px`, `.5rem`, `.4rem`, `1rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `SequelSans`
- **Body Font Stack**: `SequelSans`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: live computed `h1` (`font-size: 60px`, `line-height: 60px`, `font-weight: 600`)
- **H2 Section Rule**: live computed `h2` (`font-size: 48px`, `line-height: 48px`, `font-weight: 600`); rule `h2` (`font-size: var(--text-24)`, `line-height: var(--spacing-full)`, `font-weight: var(--font-we...`)
- **Body Copy Rule**: live computed `body` (`font-size: 15px`, `line-height: 16.5px`, `font-weight: 500`); CSS variables `--font-body: "SequelSans",sans-serif`; rule `p` (`font-size: var(--text-17)`, `line-height: 110%`, `font-weight: var(--font-we...`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 15px`, `line-height: 16.5px`, `font-weight: 500`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: 1.33333`, `--text-sm: .875rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `pda-archi_en` (`Architecture firm in Paris: renovation, refurbishment — PDA`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.header> — `pda-archi_en`)**:
   - DOM & Selectors: Landmark `<header class="header top-0">` (`1440x900px`) hosting `Architecture firm in Paris: renovati` navigation (`Projects · Expertise · Studio · Team · Digital Lab`), DOM attributes (`data-hid="ld-agency"`, `data-dark`, `data-block="aboutBlock"`, `data-src="https://pub-4eb76b4c2..."`), and stylesheet rule `cc-main span { all:unset;box-sizing:border-box }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.header> — `pda-archi_en`)` (`pda-archi_en`) adapts across `@media screen and (min-width:640px)`, `@media (prefers-reduced-motion)`, `@media screen and (max-width:640px)`, `@media (min-width:40rem)` with `cubic-bezier(.23,1,.32,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.25,.46,.45,.9)` transitions and links `Projects · Expertise · Studio · Team · Digital Lab`.
2. **Hero Stage & Focal Lead (<section.h-screen-mobile> — `PDA, Partners & Dalous Architectur`)**:
   - DOM & Selectors: Landmark `<section class="h-screen-mobile relative">` presenting display lead `PDA, Partners & Dalous Architecture, an architect...` and copy excerpt *"Transform uses, keep the"* over `#eceae5` canvas and `#161616` ink.
   - Responsive Contract: Hero stage (`1440×900px` desktop / `390×844px` mobile) sets `#eceae5` background with `#161616` headline `PDA, Partners & Dalous Architecture, an architect...`.
3. **Primary Showcase & Content Grid (<section.grid-w> — `49 Champs-Élysées`)**:
   - DOM & Selectors: Landmark `<section class="grid-w pt-margin">` rendering section `49 Champs-Élysées` with copy *"Refurbish rather than"*, asset references (`BPdaeD0G.js`, `uCyaXeDn.js`, `D_MfmCAi.js`, `CO_3Dqrm.js`), and grid rule `cc-main button { all:initial;box-sizing:border-box;color:unset;visibility:unset }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.grid-w> — `49 Champs-Élysées`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 120rem`, `gap: 52px normal`) on desktop and Single-column vertical stack at `390px` viewport width with `1rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.mt-68> — `68 Faubourg Saint-Honoré`)**:
   - DOM & Selectors: Landmark `<section class="mt-68 relative">` framing `68 Faubourg Saint-Honoré` and `118 Champs-Élysées` (*"Build where the city is"*) with `#ffffff` surface cards, `#2c2f31` accents, and `cc-main tr { all:revert;color:inherit;font-family:inherit;font-size:inherit;font-weig... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.mt-68> — `68 Faubourg Saint-Honoré`)` uses `100px`, `.5rem`, `.4rem`, `1rem` radii, `#2c2f31` highlights, and assets (BPdaeD0G.js, uCyaXeDn.js, D_MfmCAi.js).
5. **Colophon & Global Directory Footer (<footer.footer> — `https://pda.archi/en`)**:
   - DOM & Selectors: Landmark `<footer class="footer bg-black">` anchoring `Architecture firm in Paris: reno` footer links (`Projects · Expertise · Studio · Team · Digital Lab`), copy *"5 avenue de l'Opéra 75001 Paris"*, and `#d4dae0` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer> — `https://pda.archi/en`)` aligns to `120rem` (non-`@media` desktop container stylesheet rule) with `1rem` lateral canvas padding with `52px normal` grid gap and attributes (data-hid="ld-agency", data-dark, data-block="aboutBlock").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Transform uses, keep the"*
- Copy Excerpt 2: *"Refurbish rather than"*
- Copy Excerpt 3: *"Build where the city is"*
- Copy Excerpt 4: *"5 avenue de l'Opéra 75001 Paris"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.23,1,.32,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.25,.46,.45,.9)`
- **Extracted Stylesheet Rules (`pda-archi_en`)**:
- `cc-main span { all:unset;box-sizing:border-box }`
- `cc-main button { all:initial;box-sizing:border-box;color:unset;visibility:unset }`
- `cc-main tr { all:revert;color:inherit;font-family:inherit;font-size:inherit;font-weig... }`
- `cc-main.cc--rtl { direction:rtl }`
- `cc-main strong { font-weight:600 }`
- **Per-Selector Transition Rules**:
- **Selector `:root`**: `transition: .25s` extracted from `pda-archi_en` stylesheet.
- **Selector `#cc-main a`**: `transition: background-size .25s,color .25s ease` extracted from `pda-archi_en` stylesheet.
- **Selector `media(prefers-reduced-motion)`**: `transition: 0s` extracted from `pda-archi_en` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.23,1,.32,1)`)**: Governs interactive state transitions across `<header.header>` and `<section.grid-w>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`) with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `pda-archi_en`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
