---
title: "UI Prompt Blueprint: re-cycle-org"
date: 2026-11-15
target: "[[overview|re-cycle-org]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#c8df0a` canvas, `#193838` ink, `#f8f8f8` accent)"
---

# UI Design System & Master Generation Blueprint: re-cycle-org

> **Re-Cycle · Changing Lives Through Bicycle Reuse** (https://re-cycle.org/) — We are Re-Cycle. We collect unwanted bikes from across the UK and ship them to trusted partners in Africa. Donate a bike, change a life.

![Desktop Viewport Capture (1440x5863)](file:///root/projects/fleet/wiki/targets/re-cycle-org/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Re-Cycle · Changing Lives Through Bicycle Reuse** (`https://re-cycle.org/`). We are Re-Cycle. We collect unwanted bikes from across the UK and ship them to trusted partners in Africa. Donate a bike, change a life.
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#c8df0a` canvas, `#193838` ink, `#f8f8f8` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#c8df0a` (`var(--primary)` in `:root`) paired with `#193838` primary typography and `#f8f8f8` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Rubik` for display copy (`Donate a bike. Change a life.`) with `DM Sans` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: var(--spacing)`, padding `var(--spacing)`) with `cubic-bezier(.4,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/re-cycle-org/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×5863px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `40rem` extracted from `re-cycle-org` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--spacing)` lateral canvas padding with `var(--spacing)` grid gap.
- **Border Radius Scale**: `.25rem`, `var(--radius-lg)`, `var(--radius-md)`, `var(--radius-sm)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--spacing)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--spacing)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:96rem)`, `@media (min-width:40rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#c8df0a` | `var(--primary)` in `:root` |
| **Primary Typography Ink** | `#96cdcf` | `var(--secondary)` in `:root` |
| **Elevated Surface / Card Substrate** | `#e4f2f3` | `var(--secondary-light)` in `:root` |
| **Interactive Accent / Highlight** | `#f8f8f8` | `var(--light)` in `:root` |
| **Secondary / Muted Copy** | `#193838` | `var(--dark)` in `:root` |
| **Structural Hairline Border** | `#fff` | `var(--white)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-red-50` | `oklch(97.1% .013 17.38)` | Brand / Palette Token |
| `--color-red-100` | `oklch(93.6% .032 17.717)` | Brand / Palette Token |
| `--color-red-400` | `oklch(70.4% .191 22.216)` | Brand / Palette Token |
| `--color-red-500` | `oklch(63.7% .237 25.331)` | Brand / Palette Token |
| `--color-red-600` | `oklch(57.7% .245 27.325)` | Brand / Palette Token |
| `--color-red-900` | `oklch(39.6% .141 25.723)` | Brand / Palette Token |
| `--color-red-950` | `oklch(25.8% .092 26.042)` | Brand / Palette Token |
| `--color-yellow-400` | `oklch(85.2% .199 91.936)` | Brand / Palette Token |
| `--color-green-500` | `oklch(72.3% .219 149.579)` | Brand / Palette Token |
| `--color-green-600` | `oklch(62.7% .194 149.214)` | Brand / Palette Token |
| `--color-green-900` | `oklch(39.3% .095 152.535)` | Brand / Palette Token |
| `--color-gray-100` | `oklch(96.7% .003 264.542)` | Brand / Palette Token |
| `--color-gray-200` | `oklch(92.8% .006 264.531)` | Brand / Palette Token |
| `--color-gray-300` | `oklch(87.2% .01 258.338)` | Brand / Palette Token |
| `--color-gray-500` | `oklch(55.1% .027 264.364)` | Brand / Palette Token |
| `--color-black` | `var(--black)` | Canvas / Surface Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Rubik`.
- **Primary Body Stack**: `DM Sans`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`.
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`.
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: 1.5`, `--color-body: var(--body)`; rule `p` (`font-size: var(--text-xl)`, `line-height: var(--leading-relaxed)`).
- **Metadata & Navigation Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`; rule `small` (`font-size: 15px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.795,-.035,0,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `re-cycle-org` stylesheet.
- **Selector `.swiper-button`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `re-cycle-org` stylesheet.
- **Selector `.odin-menu-dropdowns .arrow`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `re-cycle-org` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.inset-x-0>` and `<section.footer-main>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Re-Cycle · Changing Lives Through Bicycle  │
│ ====================================================================== │
│ [ <header.inset-x-0>       | What We Do · How We Do It · Bikes to A ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.footer-main>                                |   │
│ | H1: Donate a bike. Change a life.                                |   │
│ | Substrate: #c8df0a    | Ink: #193838    | Accent: #f8f8f8        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.footer-main>     ) max-w: 40rem          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | 377                          |  | 171,227                      | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<header.inset-x-0>] -> [<section.footer-ma] -> [<section.footer-ma] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.relative>     ) | https://re-cycle.org/              │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.inset-x-0> — `re-cycle-org`)**:
   - Landmark `<header class="inset-x-0 w-full">` hosting `Re-Cycle · Changing Lives Through Bi` navigation (`What We Do · How We Do It · Bikes to Africa · UK Community · Our Impact`), DOM attributes (`data-cfasync="false"`, `data-cookieconsent="ignore"`, `data-ezscrex="false"`, `data-no-defer="1"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.footer-main> — `Donate a bike. Change a life.`)**:
   - Landmark `<section class="footer-main relative">` presenting display lead `Donate a bike. Change a life.` and copy excerpt *"What We Do How We Do It Bikes to Africa UK Community"* over `#c8df0a` canvas and `#193838` ink.
3. **Primary Showcase & Content Grid (<section.footer-main> — `377`)**:
   - Landmark `<section class="footer-main relative">` rendering section `377` with copy *"Our Impact Projects Sustainability"*, asset references (`analytics.js`, `ct-bot-detector.min.js`, `gtm.js`, `543115586334417`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.footer-main> — `171,227`)**:
   - Landmark `<section class="footer-main relative">` framing `171,227` and `HOW IT WORKS` (*"Support Us Donate Fundraise Partner Volunteer Shop"*) with `#e4f2f3` surface cards, `#f8f8f8` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://re-cycle.org/`)**:
   - Landmark `<footer class="relative z-20">` anchoring `Re-Cycle · Changing Lives Throug` footer links (`What We Do · How We Do It · Bikes to Africa · UK Community · Our Impact`), copy *"We collect unwanted bikes across the UK and send them to Afr"*, and `#fff` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: re-cycle-org (Re-Cycle · Changing Lives Through Bicycle Reuse)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `re-cycle-org` (**Re-Cycle · Changing Lives Through Bicycle Reuse** — `https://re-cycle.org/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#c8df0a` canvas, `#193838` ink, `#f8f8f8` accent).
- **Identity & Domain Context**: We are Re-Cycle. We collect unwanted bikes from across the UK and ship them to trusted partners in Africa. Donate a bike, change a life.
- **Primary Substrate**: `#c8df0a` (`var(--primary)` in `:root`), **Primary Ink**: `#193838`, **Accent / Highlight**: `#f8f8f8`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#c8df0a` (`var(--primary)` in `:root`) paired with `#193838` primary typography and `#f8f8f8` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Rubik` for display copy (`Donate a bike. Change a life.`) with `DM Sans` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: var(--spacing)`, padding `var(--spacing)`) with `cubic-bezier(.4,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `re-cycle-org` in your global stylesheet:

:root {
  /* Re-Cycle · Changing Lives Through Bicycle Reuse (re-cycle-org) — Ground-Truth Extracted CSS Variables */
  --color-red-50: oklch(97.1% .013 17.38); /* Brand / Palette Token (re-cycle-org) */
  --color-red-100: oklch(93.6% .032 17.717); /* Brand / Palette Token (re-cycle-org) */
  --color-red-400: oklch(70.4% .191 22.216); /* Brand / Palette Token (re-cycle-org) */
  --color-red-500: oklch(63.7% .237 25.331); /* Brand / Palette Token (re-cycle-org) */
  --color-red-600: oklch(57.7% .245 27.325); /* Brand / Palette Token (re-cycle-org) */
  --color-red-900: oklch(39.6% .141 25.723); /* Brand / Palette Token (re-cycle-org) */
  --color-red-950: oklch(25.8% .092 26.042); /* Brand / Palette Token (re-cycle-org) */
  --color-yellow-400: oklch(85.2% .199 91.936); /* Brand / Palette Token (re-cycle-org) */
  --color-green-500: oklch(72.3% .219 149.579); /* Brand / Palette Token (re-cycle-org) */
  --color-green-600: oklch(62.7% .194 149.214); /* Brand / Palette Token (re-cycle-org) */
  --color-green-900: oklch(39.3% .095 152.535); /* Brand / Palette Token (re-cycle-org) */
  --color-gray-100: oklch(96.7% .003 264.542); /* Brand / Palette Token (re-cycle-org) */
  --color-gray-200: oklch(92.8% .006 264.531); /* Brand / Palette Token (re-cycle-org) */
  --color-gray-300: oklch(87.2% .01 258.338); /* Brand / Palette Token (re-cycle-org) */
  --color-gray-500: oklch(55.1% .027 264.364); /* Brand / Palette Token (re-cycle-org) */
  --color-black: var(--black); /* Canvas / Surface Token (re-cycle-org) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#c8df0a` — grounded in `var(--primary)` in `:root`
- **Primary Typography Ink**: `#96cdcf` — grounded in `var(--secondary)` in `:root`
- **Elevated Surface / Card Substrate**: `#e4f2f3` — grounded in `var(--secondary-light)` in `:root`
- **Interactive Accent / Highlight**: `#f8f8f8` — grounded in `var(--light)` in `:root`
- **Secondary / Muted Copy**: `#193838` — grounded in `var(--dark)` in `:root`
- **Structural Hairline Border**: `#fff` — grounded in `var(--white)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×5863px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `40rem` extracted from `re-cycle-org` stylesheet
- **Padding & Gutters**: `var(--spacing)` lateral canvas padding with `var(--spacing)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--spacing)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--spacing)` horizontal padding
- **Media Queries**: `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:96rem)`, `@media (min-width:40rem)`
- **Corner Radii**: `.25rem`, `var(--radius-lg)`, `var(--radius-md)`, `var(--radius-sm)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Rubik`
- **Body Font Stack**: `DM Sans`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **H2 Section Rule**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`
- **Body Copy Rule**: CSS variables `--text-base: 1rem`, `--text-base--line-height: 1.5`, `--color-body: var(--body)`; rule `p` (`font-size: var(--text-xl)`, `line-height: var(--leading-relaxed)`)
- **Metadata & Index Rule**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`; rule `small` (`font-size: 15px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `re-cycle-org` (`Re-Cycle · Changing Lives Through Bicycle Reuse`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.inset-x-0> — `re-cycle-org`)**:
   - DOM & Selectors: Landmark `<header class="inset-x-0 w-full">` hosting `Re-Cycle · Changing Lives Through Bi` navigation (`What We Do · How We Do It · Bikes to Africa · UK Community · Our Impact`), DOM attributes (`data-cfasync="false"`, `data-cookieconsent="ignore"`, `data-ezscrex="false"`, `data-no-defer="1"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.inset-x-0> — `re-cycle-org`)` (`re-cycle-org`) adapts across `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:96rem)`, `@media (min-width:40rem)` with `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.795,-.035,0,1)` transitions and links `What We Do · How We Do It · Bikes to Africa · UK Community · Our Impact`.
2. **Hero Stage & Focal Lead (<section.footer-main> — `Donate a bike. Change a life.`)**:
   - DOM & Selectors: Landmark `<section class="footer-main relative">` presenting display lead `Donate a bike. Change a life.` and copy excerpt *"What We Do How We Do It Bikes to Africa UK Community"* over `#c8df0a` canvas and `#193838` ink.
   - Responsive Contract: Hero stage (`1440×5863px` desktop / `390×2400px` mobile) sets `#c8df0a` background with `#193838` headline `Donate a bike. Change a life.`.
3. **Primary Showcase & Content Grid (<section.footer-main> — `377`)**:
   - DOM & Selectors: Landmark `<section class="footer-main relative">` rendering section `377` with copy *"Our Impact Projects Sustainability"*, asset references (`analytics.js`, `ct-bot-detector.min.js`, `gtm.js`, `543115586334417`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.footer-main> — `377`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--spacing)`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--spacing)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.footer-main> — `171,227`)**:
   - DOM & Selectors: Landmark `<section class="footer-main relative">` framing `171,227` and `HOW IT WORKS` (*"Support Us Donate Fundraise Partner Volunteer Shop"*) with `#e4f2f3` surface cards, `#f8f8f8` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.footer-main> — `171,227`)` uses `.25rem`, `var(--radius-lg)`, `var(--radius-md)`, `var(--radius-sm)` radii, `#f8f8f8` highlights, and assets (analytics.js, ct-bot-detector.min.js, gtm.js).
5. **Colophon & Global Directory Footer (<footer.relative> — `https://re-cycle.org/`)**:
   - DOM & Selectors: Landmark `<footer class="relative z-20">` anchoring `Re-Cycle · Changing Lives Throug` footer links (`What We Do · How We Do It · Bikes to Africa · UK Community · Our Impact`), copy *"We collect unwanted bikes across the UK and send them to Afr"*, and `#fff` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.relative> — `https://re-cycle.org/`)` aligns to `40rem` extracted from `re-cycle-org` stylesheet with `var(--spacing)` lateral canvas padding with `var(--spacing)` grid gap and attributes (data-cfasync="false", data-cookieconsent="ignore", data-ezscrex="false").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"What We Do How We Do It Bikes to Africa UK Community"*
- Copy Excerpt 2: *"Our Impact Projects Sustainability"*
- Copy Excerpt 3: *"Support Us Donate Fundraise Partner Volunteer Shop"*
- Copy Excerpt 4: *"We collect unwanted bikes across the UK and send them to Africa, where they help p..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.795,-.035,0,1)`
- **Extracted Stylesheet Rules (`re-cycle-org`)**:
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- `sup { vertical-align:baseline;font-size:75%;line-height:0;position:relative }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `re-cycle-org` stylesheet.
- **Selector `.swiper-button`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `re-cycle-org` stylesheet.
- **Selector `.odin-menu-dropdowns .arrow`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `re-cycle-org` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.inset-x-0>` and `<section.footer-main>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `re-cycle-org`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
