---
title: "UI Prompt Blueprint: stillform-homes"
date: 2026-11-15
target: "[[overview|stillform-homes]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#fffbeb` / `#1c398e`)"
---

# UI Design System & Master Generation Blueprint: stillform-homes

> **STILL / FORM — Contemporary Architecture & Residences** (https://stillform.homes/) — Discover STILL / FORM, a study in contemporary residential architecture, considered spaces, material, and light. Explore the residences t...

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/stillform-homes/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **STILL / FORM — Contemporary Architecture & Residences** (`https://stillform.homes/`). Discover STILL / FORM, a study in contemporary residential architecture, considered spaces, material, and light. Explore the residences t...
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#fffbeb` / `#1c398e`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fffbeb` (`var(--color-amber-50)` in `:root`) paired with `#1c398e` primary typography and `#1c398e` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Familjen Grotesk` for display copy (`S p a c e , C o n s i d e r e d .`) with `Familjen Grotesk Fallback` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: var(--spacing)`, padding `var(--spacing)`) with `cubic-bezier(0,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/stillform-homes/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `40rem` extracted from `stillform-homes` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--spacing)` lateral canvas padding with `var(--spacing)` grid gap.
- **Border Radius Scale**: `.25rem`, `var(--radius-2xl)`, `20px`, `28px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--spacing)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--spacing)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fffbeb` | `var(--color-amber-50)` in `:root` |
| **Primary Typography Ink** | `#fcbb00` | `var(--color-amber-400)` in `:root` |
| **Elevated Surface / Card Substrate** | `#b75000` | `var(--color-amber-700)` in `:root` |
| **Interactive Accent / Highlight** | `#1c398e` | `var(--color-blue-900)` in `:root` |
| **Secondary / Muted Copy** | `#f9fafb` | `var(--color-gray-50)` in `:root` |
| **Structural Hairline Border** | `#f3f4f6` | `var(--color-gray-100)` in `:root` |
| **Variable Token (`--color-gray-200`)** | `#e5e7eb` | `var(--color-gray-200)` in `:root` |
| **Variable Token (`--color-gray-300`)** | `#d1d5dc` | `var(--color-gray-300)` in `:root` |
| **Variable Token (`--color-gray-400`)** | `#99a1af` | `var(--color-gray-400)` in `:root` |
| **Variable Token (`--color-gray-500`)** | `#6a7282` | `var(--color-gray-500)` in `:root` |
| **Variable Token (`--color-gray-700`)** | `#364153` | `var(--color-gray-700)` in `:root` |
| **Variable Token (`--color-gray-800`)** | `#1e2939` | `var(--color-gray-800)` in `:root` |
| **Variable Token (`--color-gray-900`)** | `#101828` | `var(--color-gray-900)` in `:root` |
| **Variable Token (`--color-black`)** | `#000` | `var(--color-black)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-familjen-grotesk` | `"Familjen Grotesk", "Familjen Grotesk Fallback"` | Typography / Scale Token |
| `--font-instrument-serif` | `"Instrument Serif", "Instrument Serif Fallback"` | Typography / Scale Token |
| `--color-amber-50` | `#fffbeb` | Brand / Palette Token |
| `--color-amber-400` | `#fcbb00` | Brand / Palette Token |
| `--color-amber-700` | `#b75000` | Brand / Palette Token |
| `--color-blue-900` | `#1c398e` | Brand / Palette Token |
| `--color-gray-50` | `#f9fafb` | Brand / Palette Token |
| `--color-gray-100` | `#f3f4f6` | Brand / Palette Token |
| `--color-gray-200` | `#e5e7eb` | Brand / Palette Token |
| `--color-gray-300` | `#d1d5dc` | Brand / Palette Token |
| `--color-gray-400` | `#99a1af` | Brand / Palette Token |
| `--color-gray-500` | `#6a7282` | Brand / Palette Token |
| `--color-gray-700` | `#364153` | Brand / Palette Token |
| `--color-gray-800` | `#1e2939` | Brand / Palette Token |
| `--color-gray-900` | `#101828` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Familjen Grotesk`.
- **Primary Body Stack**: `Familjen Grotesk Fallback`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`.
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`.
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`.
- **Metadata & Navigation Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `stillform-homes` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `stillform-homes` stylesheet.
- **Selector `.transition-all`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `stillform-homes` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<nav.fixed>` and `<section.relative>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — STILL / FORM — Contemporary Architecture & │
│ ====================================================================== │
│ [ <nav.fixed>              | STILL / FORM · S t a y s S t a y s · T ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.sticky>                                     |   │
│ | H1: S p a c e , C o n s i d e r e d .                            |   │
│ | Substrate: #fffbeb    | Ink: #1c398e    | Accent: #1c398e        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.relative>        ) max-w: 40rem          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Full View                    |  | A study in form, light and p | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<nav.fixed>] -> [<section.sticky>] -> [<section.relative>] |        │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.relative>     ) | https://stillform.homes/           │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.fixed> — `stillform-homes`)**:
   - Landmark `<nav class="fixed left-0">` hosting `STILL / FORM — Contemporary Architec` navigation (`STILL / FORM · S t a y s S t a y s · T o u r T o u r`), DOM attributes (`data-precedence="next"`, `data-boot-loader-complete="true"`, `data-hover-reveal="true"`, `data-hover-reveal-initialized="true"`), and stylesheet rule `tesk_f0527726-module__vHdTJa__cla... { font-family:Familjen Grotesk,Familjen Grotesk Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.sticky> — `S p a c e , C o n s i d e r e d .`)**:
   - Landmark `<section class="sticky top-0">` presenting display lead `S p a c e , C o n s i d e r e d .` and copy excerpt *"R e s i d e n c e R e s i d e n c e"* over `#fffbeb` canvas and `#1c398e` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `Full View`)**:
   - Landmark `<section class="relative z-20">` rendering section `Full View` with copy *"S t a y s S t a y s"*, asset references (`7ebf22b5a21034f8-s.p.3j3877k49yy0...`, `e41d5df559864f9e-s.p.1g73gv09-xcb...`, `f5edcc6a132fb1ad-s.p.3ii__yurxaf4...`, `hero3.webp`), and grid rule `otesk_f0527726-module__vHdTJa__va... { --font-familjen-grotesk:"Familjen Grotesk", "Familjen Grotesk Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.relative> — `A study in form, light and proport`)**:
   - Landmark `<section class="relative">` framing `A study in form, light and proportion.` and `Rooms that hold the evening light.` (*"C o n t a c t C o n t a c t"*) with `#b75000` surface cards, `#1c398e` accents, and `erif_72bbfbb4-module__cRt5FG__cla... { font-family:Instrument Serif,Instrument Serif Fallback;font-weight:400 }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://stillform.homes/`)**:
   - Landmark `<footer class="relative z-30">` anchoring `STILL / FORM — Contemporary Arch` footer links (`STILL / FORM · S t a y s S t a y s · T o u r T o u r`), copy *"E x p l o r e R e s i d e n c e E x p l o r e R e s i d e n "*, and `#f3f4f6` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: stillform-homes (STILL / FORM — Contemporary Architecture & Residences)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `stillform-homes` (**STILL / FORM — Contemporary Architecture & Residences** — `https://stillform.homes/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fffbeb` / `#1c398e`).
- **Identity & Domain Context**: Discover STILL / FORM, a study in contemporary residential architecture, considered spaces, material, and light. Explore the residences t...
- **Primary Substrate**: `#fffbeb` (`var(--color-amber-50)` in `:root`), **Primary Ink**: `#1c398e`, **Accent / Highlight**: `#1c398e`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fffbeb` (`var(--color-amber-50)` in `:root`) paired with `#1c398e` primary typography and `#1c398e` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Familjen Grotesk` for display copy (`S p a c e , C o n s i d e r e d .`) with `Familjen Grotesk Fallback` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: var(--spacing)`, padding `var(--spacing)`) with `cubic-bezier(0,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `stillform-homes` in your global stylesheet:

:root {
  /* STILL / FORM — Contemporary Architecture & Residences (stillform-homes) — Ground-Truth Extracted CSS Variables */
  --font-familjen-grotesk: "Familjen Grotesk", "Familjen Grotesk Fallback"; /* Typography / Scale Token (stillform-homes) */
  --font-instrument-serif: "Instrument Serif", "Instrument Serif Fallback"; /* Typography / Scale Token (stillform-homes) */
  --color-amber-50: #fffbeb; /* Brand / Palette Token (stillform-homes) */
  --color-amber-400: #fcbb00; /* Brand / Palette Token (stillform-homes) */
  --color-amber-700: #b75000; /* Brand / Palette Token (stillform-homes) */
  --color-blue-900: #1c398e; /* Brand / Palette Token (stillform-homes) */
  --color-gray-50: #f9fafb; /* Brand / Palette Token (stillform-homes) */
  --color-gray-100: #f3f4f6; /* Brand / Palette Token (stillform-homes) */
  --color-gray-200: #e5e7eb; /* Brand / Palette Token (stillform-homes) */
  --color-gray-300: #d1d5dc; /* Brand / Palette Token (stillform-homes) */
  --color-gray-400: #99a1af; /* Brand / Palette Token (stillform-homes) */
  --color-gray-500: #6a7282; /* Brand / Palette Token (stillform-homes) */
  --color-gray-700: #364153; /* Brand / Palette Token (stillform-homes) */
  --color-gray-800: #1e2939; /* Brand / Palette Token (stillform-homes) */
  --color-gray-900: #101828; /* Brand / Palette Token (stillform-homes) */
  --color-black: #000; /* Canvas / Surface Token (stillform-homes) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fffbeb` — grounded in `var(--color-amber-50)` in `:root`
- **Primary Typography Ink**: `#fcbb00` — grounded in `var(--color-amber-400)` in `:root`
- **Elevated Surface / Card Substrate**: `#b75000` — grounded in `var(--color-amber-700)` in `:root`
- **Interactive Accent / Highlight**: `#1c398e` — grounded in `var(--color-blue-900)` in `:root`
- **Secondary / Muted Copy**: `#f9fafb` — grounded in `var(--color-gray-50)` in `:root`
- **Structural Hairline Border**: `#f3f4f6` — grounded in `var(--color-gray-100)` in `:root`
- **Variable Token (`--color-gray-200`)**: `#e5e7eb` — grounded in `var(--color-gray-200)` in `:root`
- **Variable Token (`--color-gray-300`)**: `#d1d5dc` — grounded in `var(--color-gray-300)` in `:root`
- **Variable Token (`--color-gray-400`)**: `#99a1af` — grounded in `var(--color-gray-400)` in `:root`
- **Variable Token (`--color-gray-500`)**: `#6a7282` — grounded in `var(--color-gray-500)` in `:root`
- **Variable Token (`--color-gray-700`)**: `#364153` — grounded in `var(--color-gray-700)` in `:root`
- **Variable Token (`--color-gray-800`)**: `#1e2939` — grounded in `var(--color-gray-800)` in `:root`
- **Variable Token (`--color-gray-900`)**: `#101828` — grounded in `var(--color-gray-900)` in `:root`
- **Variable Token (`--color-black`)**: `#000` — grounded in `var(--color-black)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `40rem` extracted from `stillform-homes` stylesheet
- **Padding & Gutters**: `var(--spacing)` lateral canvas padding with `var(--spacing)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--spacing)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--spacing)` horizontal padding
- **Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`
- **Corner Radii**: `.25rem`, `var(--radius-2xl)`, `20px`, `28px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Familjen Grotesk`
- **Body Font Stack**: `Familjen Grotesk Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **H2 Section Rule**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`
- **Body Copy Rule**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Index Rule**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `stillform-homes` (`STILL / FORM — Contemporary Architecture & Residences`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.fixed> — `stillform-homes`)**:
   - DOM & Selectors: Landmark `<nav class="fixed left-0">` hosting `STILL / FORM — Contemporary Architec` navigation (`STILL / FORM · S t a y s S t a y s · T o u r T o u r`), DOM attributes (`data-precedence="next"`, `data-boot-loader-complete="true"`, `data-hover-reveal="true"`, `data-hover-reveal-initialized="true"`), and stylesheet rule `tesk_f0527726-module__vHdTJa__cla... { font-family:Familjen Grotesk,Familjen Grotesk Fallback;font-style:normal }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.fixed> — `stillform-homes`)` (`stillform-homes`) adapts across `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)` with `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `STILL / FORM · S t a y s S t a y s · T o u r T o u r`.
2. **Hero Stage & Focal Lead (<section.sticky> — `S p a c e , C o n s i d e r e d .`)**:
   - DOM & Selectors: Landmark `<section class="sticky top-0">` presenting display lead `S p a c e , C o n s i d e r e d .` and copy excerpt *"R e s i d e n c e R e s i d e n c e"* over `#fffbeb` canvas and `#1c398e` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#fffbeb` background with `#1c398e` headline `S p a c e , C o n s i d e r e d .`.
3. **Primary Showcase & Content Grid (<section.relative> — `Full View`)**:
   - DOM & Selectors: Landmark `<section class="relative z-20">` rendering section `Full View` with copy *"S t a y s S t a y s"*, asset references (`7ebf22b5a21034f8-s.p.3j3877k49yy0...`, `e41d5df559864f9e-s.p.1g73gv09-xcb...`, `f5edcc6a132fb1ad-s.p.3ii__yurxaf4...`, `hero3.webp`), and grid rule `otesk_f0527726-module__vHdTJa__va... { --font-familjen-grotesk:"Familjen Grotesk", "Familjen Grotesk Fallback" }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.relative> — `Full View`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--spacing)`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--spacing)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.relative> — `A study in form, light and proport`)**:
   - DOM & Selectors: Landmark `<section class="relative">` framing `A study in form, light and proportion.` and `Rooms that hold the evening light.` (*"C o n t a c t C o n t a c t"*) with `#b75000` surface cards, `#1c398e` accents, and `erif_72bbfbb4-module__cRt5FG__cla... { font-family:Instrument Serif,Instrument Serif Fallback;font-weight:400 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.relative> — `A study in form, light and proport`)` uses `.25rem`, `var(--radius-2xl)`, `20px`, `28px` radii, `#1c398e` highlights, and assets (7ebf22b5a21034f8-s.p.3j3877k49yy0..., e41d5df559864f9e-s.p.1g73gv09-xcb..., f5edcc6a132fb1ad-s.p.3ii__yurxaf4...).
5. **Colophon & Global Directory Footer (<footer.relative> — `https://stillform.homes/`)**:
   - DOM & Selectors: Landmark `<footer class="relative z-30">` anchoring `STILL / FORM — Contemporary Arch` footer links (`STILL / FORM · S t a y s S t a y s · T o u r T o u r`), copy *"E x p l o r e R e s i d e n c e E x p l o r e R e s i d e n "*, and `#f3f4f6` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.relative> — `https://stillform.homes/`)` aligns to `40rem` extracted from `stillform-homes` stylesheet with `var(--spacing)` lateral canvas padding with `var(--spacing)` grid gap and attributes (data-precedence="next", data-boot-loader-complete="true", data-hover-reveal="true").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"R e s i d e n c e R e s i d e n c e"*
- Copy Excerpt 2: *"S t a y s S t a y s"*
- Copy Excerpt 3: *"C o n t a c t C o n t a c t"*
- Copy Excerpt 4: *"E x p l o r e R e s i d e n c e E x p l o r e R e s i d e n c e →"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`stillform-homes`)**:
- `tesk_f0527726-module__vHdTJa__cla... { font-family:Familjen Grotesk,Familjen Grotesk Fallback;font-style:normal }`
- `otesk_f0527726-module__vHdTJa__va... { --font-familjen-grotesk:"Familjen Grotesk", "Familjen Grotesk Fallback" }`
- `erif_72bbfbb4-module__cRt5FG__cla... { font-family:Instrument Serif,Instrument Serif Fallback;font-weight:400 }`
- `serif_72bbfbb4-module__cRt5FG__va... { --font-instrument-serif:"Instrument Serif", "Instrument Serif Fallback" }`
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `stillform-homes` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `stillform-homes` stylesheet.
- **Selector `.transition-all`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `stillform-homes` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<nav.fixed>` and `<section.relative>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `stillform-homes`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
