---
title: "UI Prompt Blueprint: ladolfinajumping-com"
date: 2026-11-15
target: "[[overview|ladolfinajumping-com]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#fbe0b6` canvas, `#0d1620` ink, `#c7bcac` accent)"
---

# UI Design System & Master Generation Blueprint: ladolfinajumping-com

> **La Dolfina Jumping. World class genetics, breed in Argentina** (https://ladolfinajumping.com/) — We are dedicated to create the finest show jumping horses through our cutting-edge breeding program in Argentina by sourcing and importin...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **La Dolfina Jumping. World class genetics, breed in Argentina** (`https://ladolfinajumping.com/`). We are dedicated to create the finest show jumping horses through our cutting-edge breeding program in Argentina by sourcing and importin...
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#fbe0b6` canvas, `#0d1620` ink, `#c7bcac` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fbe0b6` (`var(--color-primary)` in `:root`) paired with `#0d1620` primary typography and `#c7bcac` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Marcellus` for display copy (`D e l i v e r i n g A c c e s s t o `) with `Alpine Script` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `600px` container bounds (`gap: 10px`, padding `45vw`) with `cubic-bezier(.4,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `600px` extracted from `ladolfinajumping-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `45vw` lateral canvas padding with `10px` grid gap.
- **Border Radius Scale**: `100px`, `99px`, `50px`, `100%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 600px`, `gap: 10px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `45vw` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width: 600px)`, `@media (min-width: 600px)`, `@media (min-width: 1024px)`, `@media (min-width: 1256px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fbe0b6` | `var(--color-primary)` in `:root` |
| **Primary Typography Ink** | `#0a1b2e` | `var(--color-secondary)` in `:root` |
| **Elevated Surface / Card Substrate** | `#be7e21` | `var(--color-tertiary)` in `:root` |
| **Interactive Accent / Highlight** | `#c7bcac` | `var(--color-quaternary)` in `:root` |
| **Secondary / Muted Copy** | `#475768` | `var(--color-p)` in `:root` |
| **Structural Hairline Border** | `#0d1620` | `var(--color-dark-strong)` in `:root` |
| **Variable Token (`--color-footer`)** | `#162638` | `var(--color-footer)` in `:root` |
| **Variable Token (`--form-brdr`)** | `#efe7dc` | `var(--form-brdr)` in `:root` |
| **Variable Token (`--swiper-theme-color`)** | `#007aff` | `var(--swiper-theme-color)` in stylesheet |
| **Variable Token (`--swiper-preloader-color`)** | `#fff` | `var(--swiper-preloader-color)` in stylesheet |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-primary` | `"Noto Sans Display", sans-serif` | Brand / Palette Token |
| `--font-secondary` | `"Alpine Script" !important` | Brand / Palette Token |
| `--font-tertiary` | `"Marcellus", "Dualis Lite", "Noto Sans Display", sans-serif` | Typography / Scale Token |
| `--color-primary` | `#fbe0b6` | Brand / Palette Token |
| `--color-secondary` | `#0a1b2e` | Brand / Palette Token |
| `--color-tertiary` | `#be7e21` | Brand / Palette Token |
| `--color-quaternary` | `#c7bcac` | Brand / Palette Token |
| `--color-form` | `rgb(175, 145, 95)` | Brand / Palette Token |
| `--color-p` | `#475768` | Brand / Palette Token |
| `--color-dark-strong` | `#0d1620` | Canvas / Surface Token |
| `--color-footer` | `#162638` | Brand / Palette Token |
| `--form-brdr` | `2px solid #efe7dc` | Color / Atmospheric Token |
| `--swiper-theme-color` | `#007aff` | Brand / Palette Token |
| `--swiper-preloader-color` | `#fff` | Brand / Palette Token |
| `--ladolfinajumping-bg` | `#fbe0b6` | Canvas Substrate (from `var(--color-primary)` in `:root`) |
| `--ladolfinajumping-ink` | `#0d1620` | Primary Typography Ink (stylesheet-derived) |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Marcellus`.
- **Primary Body Stack**: `Alpine Script`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`letter-spacing: .25em`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`, `12px`, `clamp(32px,8vw,36px)`, `clamp(32px,8vw,48px)`, `clamp(32px,8vw,60px)`).
- **Body Copy**: rule `p` (`font-weight: 500`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`, `12px`, `clamp(32px,8vw,36px)`, `clamp(32px,8vw,48px)`, `clamp(32px,8vw,60px)`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.o-btn`**: `transition: .35s` extracted from `ladolfinajumping-com` stylesheet.
- **Selector `.o-btn:before`**: `transition: .35s` extracted from `ladolfinajumping-com` stylesheet.
- **Selector `.o-close`**: `transition: .5s` extracted from `ladolfinajumping-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.header>` and `<section.o-section>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — La Dolfina Jumping. World class genetics,  │
│ ====================================================================== │
│ [ <header.header>          | Breeding Cría · Saddles · Bridles · Mo ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <article.loader>                                     |   │
│ | H1: D e l i v e r i n g A c c e s s t o e x c e p t i...         |   │
│ | Substrate: #fbe0b6    | Ink: #0d1620    | Accent: #c7bcac        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.o-section>       ) max-w: 600px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | A n e x c l u s i v e b r a  |  | A d o l f o C a m b i a s o  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 10px  ) | │
│ | [<header.header>] -> [<article.loader>] -> [<section.o-section] |    │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>       ) | https://ladolfinajumping.com/      │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.header> — `ladolfinajumping-com`)**:
   - Landmark `<header class="header has--bg-darken">` hosting `La Dolfina Jumping. World class gene` navigation (`Breeding Cría · Saddles · Bridles · Monturas · Cabezadas`), DOM attributes (`data-speed="0.5"`, `data-transition="opacity-in"`, `data-speed="0.25"`, `data-transition="opacity-scale-in-group"`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<article.loader> — `D e l i v e r i n g A c c e s s t `)**:
   - Landmark `<article class="loader">` presenting display lead `D e l i v e r i n g A c c e s s t o e x c e p t i...` and copy excerpt *"Tour & Championship Tour y Campeonatos"* over `#fbe0b6` canvas and `#0d1620` ink.
3. **Primary Showcase & Content Grid (<section.o-section> — `A n e x c l u s i v e b r a n d`)**:
   - Landmark `<section class="o-section c-brand">` rendering section `A n e x c l u s i v e b r a n d` with copy *"Tour & Championship"*, asset references (`289546863693632`, `fbevents.js`, `gtm.js`, `favicon.png`), and grid rule `html { height:auto;font-size:16px }`.
4. **Interactive Detail & Feature Matrix (<section.o-section> — `A d o l f o C a m b i a s o`)**:
   - Landmark `<section class="o-section c-breeding">` framing `A d o l f o C a m b i a s o` and `B r e e d i n g` (*"Tour y Campeonatos"*) with `#be7e21` surface cards, `#c7bcac` accents, and `html.lenis { height:auto;scroll-behavior:initial }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://ladolfinajumping.com/`)**:
   - Landmark `<footer class="footer bg-white">` anchoring `La Dolfina Jumping. World class ` footer links (`Breeding Cría · Saddles · Bridles · Monturas · Cabezadas`), copy *"Equipment Equipamiento Saddles Bridles Monturas Cabezadas"*, and `#0d1620` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: ladolfinajumping-com (La Dolfina Jumping. World class genetics, breed in Argentina)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `ladolfinajumping-com` (**La Dolfina Jumping. World class genetics, breed in Argentina** — `https://ladolfinajumping.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#fbe0b6` canvas, `#0d1620` ink, `#c7bcac` accent).
- **Identity & Domain Context**: We are dedicated to create the finest show jumping horses through our cutting-edge breeding program in Argentina by sourcing and importin...
- **Primary Substrate**: `#fbe0b6` (`var(--color-primary)` in `:root`), **Primary Ink**: `#0d1620`, **Accent / Highlight**: `#c7bcac`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fbe0b6` (`var(--color-primary)` in `:root`) paired with `#0d1620` primary typography and `#c7bcac` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Marcellus` for display copy (`D e l i v e r i n g A c c e s s t o `) with `Alpine Script` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `600px` container bounds (`gap: 10px`, padding `45vw`) with `cubic-bezier(.4,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `ladolfinajumping-com` in your global stylesheet:

:root {
  /* La Dolfina Jumping. World class genetics, breed in Argentina (ladolfinajumping-com) — Ground-Truth Extracted CSS Variables */
  --font-primary: "Noto Sans Display", sans-serif; /* Brand / Palette Token (ladolfinajumping-com) */
  --font-secondary: "Alpine Script" !important; /* Brand / Palette Token (ladolfinajumping-com) */
  --font-tertiary: "Marcellus", "Dualis Lite", "Noto Sans Display", sans-serif; /* Typography / Scale Token (ladolfinajumping-com) */
  --color-primary: #fbe0b6; /* Brand / Palette Token (ladolfinajumping-com) */
  --color-secondary: #0a1b2e; /* Brand / Palette Token (ladolfinajumping-com) */
  --color-tertiary: #be7e21; /* Brand / Palette Token (ladolfinajumping-com) */
  --color-quaternary: #c7bcac; /* Brand / Palette Token (ladolfinajumping-com) */
  --color-form: rgb(175, 145, 95); /* Brand / Palette Token (ladolfinajumping-com) */
  --color-p: #475768; /* Brand / Palette Token (ladolfinajumping-com) */
  --color-dark-strong: #0d1620; /* Canvas / Surface Token (ladolfinajumping-com) */
  --color-footer: #162638; /* Brand / Palette Token (ladolfinajumping-com) */
  --form-brdr: 2px solid #efe7dc; /* Color / Atmospheric Token (ladolfinajumping-com) */
  --swiper-theme-color: #007aff; /* Brand / Palette Token (ladolfinajumping-com) */
  --swiper-preloader-color: #fff; /* Brand / Palette Token (ladolfinajumping-com) */
  --ladolfinajumping-bg: #fbe0b6; /* Canvas Substrate (from `var(--color-primary)` in `:root`) (ladolfinajumping-com) */
  --ladolfinajumping-ink: #0d1620; /* Primary Typography Ink (stylesheet-derived) (ladolfinajumping-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fbe0b6` — grounded in `var(--color-primary)` in `:root`
- **Primary Typography Ink**: `#0a1b2e` — grounded in `var(--color-secondary)` in `:root`
- **Elevated Surface / Card Substrate**: `#be7e21` — grounded in `var(--color-tertiary)` in `:root`
- **Interactive Accent / Highlight**: `#c7bcac` — grounded in `var(--color-quaternary)` in `:root`
- **Secondary / Muted Copy**: `#475768` — grounded in `var(--color-p)` in `:root`
- **Structural Hairline Border**: `#0d1620` — grounded in `var(--color-dark-strong)` in `:root`
- **Variable Token (`--color-footer`)**: `#162638` — grounded in `var(--color-footer)` in `:root`
- **Variable Token (`--form-brdr`)**: `#efe7dc` — grounded in `var(--form-brdr)` in `:root`
- **Variable Token (`--swiper-theme-color`)**: `#007aff` — grounded in `var(--swiper-theme-color)` in stylesheet
- **Variable Token (`--swiper-preloader-color`)**: `#fff` — grounded in `var(--swiper-preloader-color)` in stylesheet

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `600px` extracted from `ladolfinajumping-com` stylesheet
- **Padding & Gutters**: `45vw` lateral canvas padding with `10px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 600px`, `gap: 10px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `45vw` horizontal padding
- **Media Queries**: `@media (max-width: 600px)`, `@media (min-width: 600px)`, `@media (min-width: 1024px)`, `@media (min-width: 1256px)`
- **Corner Radii**: `100px`, `99px`, `50px`, `100%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Marcellus`
- **Body Font Stack**: `Alpine Script`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: rule `h1` (`letter-spacing: .25em`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`, `12px`, `clamp(32px,8vw,36px)`, `clamp(32px,8vw,48px)`, `clamp(32px,8vw,60px)`)
- **Body Copy Rule**: rule `p` (`font-weight: 500`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`, `12px`, `clamp(32px,8vw,36px)`, `clamp(32px,8vw,48px)`, `clamp(32px,8vw,60px)`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `ladolfinajumping-com` (`La Dolfina Jumping. World class genetics, breed in Argentina`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.header> — `ladolfinajumping-com`)**:
   - DOM & Selectors: Landmark `<header class="header has--bg-darken">` hosting `La Dolfina Jumping. World class gene` navigation (`Breeding Cría · Saddles · Bridles · Monturas · Cabezadas`), DOM attributes (`data-speed="0.5"`, `data-transition="opacity-in"`, `data-speed="0.25"`, `data-transition="opacity-scale-in-group"`), and stylesheet rule `after { box-sizing:border-box }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.header> — `ladolfinajumping-com`)` (`ladolfinajumping-com`) adapts across `@media (max-width: 600px)`, `@media (min-width: 600px)`, `@media (min-width: 1024px)`, `@media (min-width: 1256px)` with `cubic-bezier(.4,0,.2,1)` transitions and links `Breeding Cría · Saddles · Bridles · Monturas · Cabezadas`.
2. **Hero Stage & Focal Lead (<article.loader> — `D e l i v e r i n g A c c e s s t `)**:
   - DOM & Selectors: Landmark `<article class="loader">` presenting display lead `D e l i v e r i n g A c c e s s t o e x c e p t i...` and copy excerpt *"Tour & Championship Tour y Campeonatos"* over `#fbe0b6` canvas and `#0d1620` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#fbe0b6` background with `#0d1620` headline `D e l i v e r i n g A c c e s s t o e x c e p t i...`.
3. **Primary Showcase & Content Grid (<section.o-section> — `A n e x c l u s i v e b r a n d`)**:
   - DOM & Selectors: Landmark `<section class="o-section c-brand">` rendering section `A n e x c l u s i v e b r a n d` with copy *"Tour & Championship"*, asset references (`289546863693632`, `fbevents.js`, `gtm.js`, `favicon.png`), and grid rule `html { height:auto;font-size:16px }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.o-section> — `A n e x c l u s i v e b r a n d`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 600px`, `gap: 10px`) on desktop and Single-column vertical stack at `390px` viewport width with `45vw` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.o-section> — `A d o l f o C a m b i a s o`)**:
   - DOM & Selectors: Landmark `<section class="o-section c-breeding">` framing `A d o l f o C a m b i a s o` and `B r e e d i n g` (*"Tour y Campeonatos"*) with `#be7e21` surface cards, `#c7bcac` accents, and `html.lenis { height:auto;scroll-behavior:initial }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.o-section> — `A d o l f o C a m b i a s o`)` uses `100px`, `99px`, `50px`, `100%` radii, `#c7bcac` highlights, and assets (289546863693632, fbevents.js, gtm.js).
5. **Colophon & Global Directory Footer (<footer.footer> — `https://ladolfinajumping.com/`)**:
   - DOM & Selectors: Landmark `<footer class="footer bg-white">` anchoring `La Dolfina Jumping. World class ` footer links (`Breeding Cría · Saddles · Bridles · Monturas · Cabezadas`), copy *"Equipment Equipamiento Saddles Bridles Monturas Cabezadas"*, and `#0d1620` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer> — `https://ladolfinajumping.com/`)` aligns to `600px` extracted from `ladolfinajumping-com` stylesheet with `45vw` lateral canvas padding with `10px` grid gap and attributes (data-speed="0.5", data-transition="opacity-in", data-speed="0.25").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Tour & Championship Tour y Campeonatos"*
- Copy Excerpt 2: *"Tour & Championship"*
- Copy Excerpt 3: *"Tour y Campeonatos"*
- Copy Excerpt 4: *"Equipment Equipamiento Saddles Bridles Monturas Cabezadas"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`ladolfinajumping-com`)**:
- `after { box-sizing:border-box }`
- `html { height:auto;font-size:16px }`
- `html.lenis { height:auto;scroll-behavior:initial }`
- `.lenis.lenis-smooth { scroll-behavior:auto }`
- `.scroll-container { height:100vh;overflow-y:scroll }`
- **Per-Selector Transition Rules**:
- **Selector `.o-btn`**: `transition: .35s` extracted from `ladolfinajumping-com` stylesheet.
- **Selector `.o-btn:before`**: `transition: .35s` extracted from `ladolfinajumping-com` stylesheet.
- **Selector `.o-close`**: `transition: .5s` extracted from `ladolfinajumping-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.header>` and `<section.o-section>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `ladolfinajumping-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
