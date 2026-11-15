---
title: "UI Prompt Blueprint: giordanobetti-com"
date: 2026-11-15
target: "[[overview|giordanobetti-com]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#0000`)"
---

# UI Design System & Master Generation Blueprint: giordanobetti-com

> **Giordano Betti - Independent Cinematographer** (https://giordanobetti.com/) — Giordano Betti is an independent cinematographer and Director of Photography based in Tuscany, Italy.

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/giordanobetti-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Giordano Betti - Independent Cinematographer** (`https://giordanobetti.com/`). Giordano Betti is an independent cinematographer and Director of Photography based in Tuscany, Italy.
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#0000`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--color-black)` in `:root`) paired with `#fff` primary typography and `#0000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Instrument Serif` for display copy (`Something in mind?`) with `Host Grotesk` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: var(--gap)`, padding `var(--gap)`) with `cubic-bezier(.4,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/giordanobetti-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `40rem` extracted from `giordanobetti-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--gap)` lateral canvas padding with `var(--gap)` grid gap.
- **Border Radius Scale**: `0px` (sharp unrounded corners).

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--gap)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--gap)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (width>=40rem)`, `@media (width>=48rem)`, `@media (width>=64rem)`, `@media (width>=80rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#171717` | `var(--color-background)` in `:root` |
| **Interactive Accent / Highlight** | `#0000` | `textarea { background-color: #0000 }` |
| **Secondary / Muted Copy** | `#000000` | `50 { background-color: black }` (`#000000`) |
| **Structural Hairline Border** | `#ffffff` | `.debug .f-cell { background-color: white }` (`#ffffff`) |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `"Host Grotesk", ui-sans-serif, system-ui, sans-serif` | Typography / Scale Token |
| `--font-serif` | `"Instrument Serif", ui-serif, serif` | Typography / Scale Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-3xl` | `48rem` | Layout / Spatial Grid Token |
| `--font-weight-normal` | `400` | Typography / Scale Token |
| `--blur-lg` | `16px` | Elevation / Border Token |
| `--aspect-video` | `16 / 9` | Design System Custom Token |
| `--default-transition-duration` | `.15s` | Motion / Easing Token |
| `--default-transition-timing-function` | `cubic-bezier(.4, 0, .2, 1)` | Motion / Easing Token |
| `--default-font-family` | `var(--font-sans)` | Typography / Scale Token |
| `--default-mono-font-family` | `var(--font-mono)` | Typography / Scale Token |
| `--color-foreground` | `#fff` | Typography Ink Token |
| `--color-background` | `#171717` | Canvas / Surface Token |
| `--gap` | `clamp(14px, 1.5vw, 32px)` | Layout / Spatial Grid Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Instrument Serif`.
- **Primary Body Stack**: `Host Grotesk`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `clamp(40px,2.07vw + 32.24px,72px)`, `clamp(16px,.26vw + 15.03px,20px)`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `clamp(40px,2.07vw + 32.24px,72px)`, `clamp(16px,.26vw + 15.03px,20px)`).
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `clamp(40px,2.07vw + 32.24px,72px)`, `clamp(16px,.26vw + 15.03px,20px)`).
- **Metadata & Navigation Labels**: CSS variables `--default-mono-font-family: var(--font-mono)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `giordanobetti-com` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `giordanobetti-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.header>` and `<section.home-content>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Giordano Betti - Independent Cinematograph │
│ ====================================================================== │
│ [ <header.header>          | instagram instagram · youtube youtube  ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.contact-modal>                              |   │
│ | H1: Something in mind?                                           |   │
│ | Substrate: #000       | Ink: #fff       | Accent: #0000          |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.home-content>    ) max-w: 40rem          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Giordano Betti - Independent |  | Jupiter                      | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<header.header>] -> [<section.contact-m] -> [<section.home-cont] |  │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.header__sectio) | https://giordanobetti.com/         │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.header> — `giordanobetti-com`)**:
   - Landmark `<header class="header js-header">` hosting `Giordano Betti - Independent Cinemat` navigation (`instagram instagram · youtube youtube · linkedin linkedin`), DOM attributes (`data-v-ad171e27`, `data-v-67aeeb6a`, `data-v-6d80a5f8`, `data-v-794a89b8`), and stylesheet rule `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.contact-modal> — `Something in mind?`)**:
   - Landmark `<section class="contact-modal f-grid">` presenting display lead `Something in mind?` and copy excerpt *"Giordano Betti Independent Cinematographer"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.home-content> — `Giordano Betti - Independent Cinem`)**:
   - Landmark `<section class="home-content f-grid">` rendering section `Giordano Betti - Independent Cinematographer` with copy *"Independent Cinematographer"*, asset references (`entry.B8GcDMgn.css`, `Footer.BHv6vXkB.css`, `Action.C2i8mHMB.css`, `MoZuWBAS.js`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.home-content__footer> — `Jupiter`)**:
   - Landmark `<section class="home-content__footer f-grid">` framing `Jupiter` and `AVAVAV X ADIDAS SS25` (*"Something in mind?"*) with `#171717` surface cards, `#0000` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.header__section> — `https://giordanobetti.com/`)**:
   - Landmark `<footer class="header__section">` anchoring `Giordano Betti - Independent Cin` footer links (`instagram instagram · youtube youtube · linkedin linkedin`), copy *"Let's create something meaningful together."*, and `#ffffff` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: giordanobetti-com (Giordano Betti - Independent Cinematographer)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `giordanobetti-com` (**Giordano Betti - Independent Cinematographer** — `https://giordanobetti.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#0000`).
- **Identity & Domain Context**: Giordano Betti is an independent cinematographer and Director of Photography based in Tuscany, Italy.
- **Primary Substrate**: `#000` (`var(--color-black)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#0000`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--color-black)` in `:root`) paired with `#fff` primary typography and `#0000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Instrument Serif` for display copy (`Something in mind?`) with `Host Grotesk` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: var(--gap)`, padding `var(--gap)`) with `cubic-bezier(.4,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `giordanobetti-com` in your global stylesheet:

:root {
  /* Giordano Betti - Independent Cinematographer (giordanobetti-com) — Ground-Truth Extracted CSS Variables */
  --font-sans: "Host Grotesk", ui-sans-serif, system-ui, sans-serif; /* Typography / Scale Token (giordanobetti-com) */
  --font-serif: "Instrument Serif", ui-serif, serif; /* Typography / Scale Token (giordanobetti-com) */
  --color-black: #000; /* Canvas / Surface Token (giordanobetti-com) */
  --color-white: #fff; /* Canvas / Surface Token (giordanobetti-com) */
  --spacing: .25rem; /* Layout / Spatial Grid Token (giordanobetti-com) */
  --container-3xl: 48rem; /* Layout / Spatial Grid Token (giordanobetti-com) */
  --font-weight-normal: 400; /* Typography / Scale Token (giordanobetti-com) */
  --blur-lg: 16px; /* Elevation / Border Token (giordanobetti-com) */
  --aspect-video: 16 / 9; /* Design System Custom Token (giordanobetti-com) */
  --default-transition-duration: .15s; /* Motion / Easing Token (giordanobetti-com) */
  --default-transition-timing-function: cubic-bezier(.4, 0, .2, 1); /* Motion / Easing Token (giordanobetti-com) */
  --default-font-family: var(--font-sans); /* Typography / Scale Token (giordanobetti-com) */
  --default-mono-font-family: var(--font-mono); /* Typography / Scale Token (giordanobetti-com) */
  --color-foreground: #fff; /* Typography Ink Token (giordanobetti-com) */
  --color-background: #171717; /* Canvas / Surface Token (giordanobetti-com) */
  --gap: clamp(14px, 1.5vw, 32px); /* Layout / Spatial Grid Token (giordanobetti-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000` — grounded in `var(--color-black)` in `:root`
- **Primary Typography Ink**: `#fff` — grounded in `var(--color-white)` in `:root`
- **Elevated Surface / Card Substrate**: `#171717` — grounded in `var(--color-background)` in `:root`
- **Interactive Accent / Highlight**: `#0000` — grounded in `textarea { background-color: #0000 }`
- **Secondary / Muted Copy**: `#000000` — grounded in `50 { background-color: black }` (`#000000`)
- **Structural Hairline Border**: `#ffffff` — grounded in `.debug .f-cell { background-color: white }` (`#ffffff`)

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `40rem` extracted from `giordanobetti-com` stylesheet
- **Padding & Gutters**: `var(--gap)` lateral canvas padding with `var(--gap)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--gap)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--gap)` horizontal padding
- **Media Queries**: `@media (width>=40rem)`, `@media (width>=48rem)`, `@media (width>=64rem)`, `@media (width>=80rem)`
- **Corner Radii**: `0px` (sharp unrounded corners)

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Instrument Serif`
- **Body Font Stack**: `Host Grotesk`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `clamp(40px,2.07vw + 32.24px,72px)`, `clamp(16px,.26vw + 15.03px,20px)`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `clamp(40px,2.07vw + 32.24px,72px)`, `clamp(16px,.26vw + 15.03px,20px)`)
- **Body Copy Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `clamp(40px,2.07vw + 32.24px,72px)`, `clamp(16px,.26vw + 15.03px,20px)`)
- **Metadata & Index Rule**: CSS variables `--default-mono-font-family: var(--font-mono)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `giordanobetti-com` (`Giordano Betti - Independent Cinematographer`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.header> — `giordanobetti-com`)**:
   - DOM & Selectors: Landmark `<header class="header js-header">` hosting `Giordano Betti - Independent Cinemat` navigation (`instagram instagram · youtube youtube · linkedin linkedin`), DOM attributes (`data-v-ad171e27`, `data-v-67aeeb6a`, `data-v-6d80a5f8`, `data-v-794a89b8`), and stylesheet rule `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.header> — `giordanobetti-com`)` (`giordanobetti-com`) adapts across `@media (width>=40rem)`, `@media (width>=48rem)`, `@media (width>=64rem)`, `@media (width>=80rem)` with `cubic-bezier(.4,0,.2,1)` transitions and links `instagram instagram · youtube youtube · linkedin linkedin`.
2. **Hero Stage & Focal Lead (<section.contact-modal> — `Something in mind?`)**:
   - DOM & Selectors: Landmark `<section class="contact-modal f-grid">` presenting display lead `Something in mind?` and copy excerpt *"Giordano Betti Independent Cinematographer"* over `#000` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#000` background with `#fff` headline `Something in mind?`.
3. **Primary Showcase & Content Grid (<section.home-content> — `Giordano Betti - Independent Cinem`)**:
   - DOM & Selectors: Landmark `<section class="home-content f-grid">` rendering section `Giordano Betti - Independent Cinematographer` with copy *"Independent Cinematographer"*, asset references (`entry.B8GcDMgn.css`, `Footer.BHv6vXkB.css`, `Action.C2i8mHMB.css`, `MoZuWBAS.js`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.home-content> — `Giordano Betti - Independent Cinem`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--gap)`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--gap)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.home-content__footer> — `Jupiter`)**:
   - DOM & Selectors: Landmark `<section class="home-content__footer f-grid">` framing `Jupiter` and `AVAVAV X ADIDAS SS25` (*"Something in mind?"*) with `#171717` surface cards, `#0000` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.home-content__footer> — `Jupiter`)` uses `0px` (sharp unrounded corners) radii, `#0000` highlights, and assets (entry.B8GcDMgn.css, Footer.BHv6vXkB.css, Action.C2i8mHMB.css).
5. **Colophon & Global Directory Footer (<footer.header__section> — `https://giordanobetti.com/`)**:
   - DOM & Selectors: Landmark `<footer class="header__section">` anchoring `Giordano Betti - Independent Cin` footer links (`instagram instagram · youtube youtube · linkedin linkedin`), copy *"Let's create something meaningful together."*, and `#ffffff` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.header__section> — `https://giordanobetti.com/`)` aligns to `40rem` extracted from `giordanobetti-com` stylesheet with `var(--gap)` lateral canvas padding with `var(--gap)` grid gap and attributes (data-v-ad171e27, data-v-67aeeb6a, data-v-6d80a5f8).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Giordano Betti Independent Cinematographer"*
- Copy Excerpt 2: *"Independent Cinematographer"*
- Copy Excerpt 3: *"Something in mind?"*
- Copy Excerpt 4: *"Let's create something meaningful together."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`giordanobetti-com`)**:
- `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- `sup { vertical-align:baseline;font-size:75%;line-height:0;position:relative }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `giordanobetti-com` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `giordanobetti-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.header>` and `<section.home-content>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `giordanobetti-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
