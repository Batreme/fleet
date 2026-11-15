---
title: "UI Prompt Blueprint: tour-kyrgyzstan-com"
date: 2026-11-15
target: "[[overview|tour-kyrgyzstan-com]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#FFFFFF` canvas, `#000000` ink, `#fff` accent)"
---

# UI Design System & Master Generation Blueprint: tour-kyrgyzstan-com

> **Tour Kyrgyzstan — Central Asia, unmapped** (https://tour-kyrgyzstan.com/) — Discover authentic Kyrgyzstan tours. Mountain trekking, nomadic culture, and professional video production services.

![Desktop Viewport Capture (1440x11869)](file:///root/projects/fleet/wiki/targets/tour-kyrgyzstan-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Tour Kyrgyzstan — Central Asia, unmapped** (`https://tour-kyrgyzstan.com/`). Discover authentic Kyrgyzstan tours. Mountain trekking, nomadic culture, and professional video production services.
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#FFFFFF` canvas, `#000000` ink, `#fff` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#FFFFFF` (`var(--paper)` in `:root`) paired with `#000000` primary typography and `#fff` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Archivo` for display copy (`Central Asia like you've never imagi`) with `Fragment Mono` and `Fragment Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1400px` container bounds (`gap: 8px`, padding `24px`) with `cubic-bezier(.16,1,.3,1)` easing and Framer Motion Layout Physics.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/tour-kyrgyzstan-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×11869px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `1400px` extracted from `tour-kyrgyzstan-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `24px` lateral canvas padding with `8px` grid gap.
- **Border Radius Scale**: `0%`, `50%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1400px`, `gap: 8px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `24px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (hover: none), (max-width: 900px)`, `@media (max-width: 900px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#FFFFFF` | `var(--paper)` in `:root` |
| **Primary Typography Ink** | `#000000` | `var(--ink)` in `:root` |
| **Elevated Surface / Card Substrate** | `#dc2f02` | `.nav__links a:hover { color: #dc2f02 }` |
| **Interactive Accent / Highlight** | `#fff` | `.nav__mobile-menu > a { color: #fff }` |
| **Secondary / Muted Copy** | `#b52501` | `.hero__cta:hover { background: #b52501 }` |
| **Structural Hairline Border** | `#0d0d0d` | `.section--dark { background: #0d0d0d }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--paper` | `#FFFFFF` | Canvas / Surface Token |
| `--ink` | `#000000` | Typography Ink Token |
| `--ink-soft` | `rgba(0,0,0,.65)` | Typography Ink Token |
| `--ink-faint` | `rgba(0,0,0,.45)` | Typography Ink Token |
| `--hero-vh` | `900px` | Layout / Spatial Grid Token |
| `--seg-w` | `30px` | Dimension / Scale Token |
| `--tour-kyrgyzstan--bg` | `#FFFFFF` | Canvas Substrate (from `var(--paper)` in `:root`) |
| `--tour-kyrgyzstan--ink` | `#000000` | Primary Typography Ink (stylesheet-derived) |
| `--tour-kyrgyzstan--surface` | `#dc2f02` | Surface Substrate (stylesheet-derived) |
| `--tour-kyrgyzstan--accent` | `#fff` | Interactive Accent (stylesheet-derived) |
| `--tour-kyrgyzstan--muted` | `#b52501` | Secondary Ink (stylesheet-derived) |
| `--tour-kyrgyzstan--border` | `#0d0d0d` | Structural Border (stylesheet-derived) |
| `--tour-kyrgyzstan--container` | `1400px` | Container Bound (stylesheet-derived) |
| `--tour-kyrgyzstan--gap` | `8px` | Grid Gutter (stylesheet-derived) |
| `--tour-kyrgyzstan--pad` | `24px` | Lateral Padding (stylesheet-derived) |
| `--tour-kyrgyzstan--ease` | `cubic-bezier(.16,1,.3,1)` | Primary Easing Function |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Archivo`.
- **Primary Body Stack**: `Fragment Mono`.
- **Technical / Metadata Stack**: `Fragment Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `15px`, `12px`, `14px`, `13px`, `clamp(32px, 3.4vw, 72px)`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `15px`, `12px`, `14px`, `13px`, `clamp(32px, 3.4vw, 72px)`).
- **Body Copy**: rule `body` (`font-weight: 400`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `15px`, `12px`, `14px`, `13px`, `clamp(32px, 3.4vw, 72px)`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.76,0,.24,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.nav`**: `transition: color .35s ease, background .2s ease` extracted from `tour-kyrgyzstan-com` stylesheet.
- **Selector `.nav__burger-line`**: `transition: transform .3s ease, top .3s ease, width .3s ease, left .3s ease` extracted from `tour-kyrgyzstan-com` stylesheet.
- **Selector `.nav__mobile-menu`**: `transition: opacity .2s ease, transform .2s ease` extracted from `tour-kyrgyzstan-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<nav.nav>` and `<section.section>`.
- **Runtime Interaction Engine**: Integrates Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Tour Kyrgyzstan — Central Asia, unmapped   │
│ ====================================================================== │
│ [ <nav.nav>                | Gallery · Expeditions                  ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero>                                       |   │
│ | H1: Central Asia like you've never imagined                      |   │
│ | Substrate: #FFFFFF    | Ink: #000000    | Accent: #fff           |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.section>         ) max-w: 1400px         |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Journeys, which don't exist  |  | Immersive nomadic experience | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 8px   ) | │
│ | [<nav.nav>] -> [<section.hero>] -> [<section.section>] |             │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>       ) | https://tour-kyrgyzstan.com/       │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.nav> — `tour-kyrgyzstan-com`)**:
   - Landmark `<nav class="nav">` hosting `Tour Kyrgyzstan — Central Asia, unma` navigation (`Gallery · Expeditions`), DOM attributes (`data-line="0"`, `data-line="1"`, `data-index="0"`, `data-index="1"`), and stylesheet rule `root { --paper: FFFFFF; --ink: 000000; --ink-soft: rgba(0,0,0,.65); --ink-faint... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Central Asia like you've never ima`)**:
   - Landmark `<section class="hero">` presenting display lead `Central Asia like you've never imagined` and copy excerpt *"K y r g y z s t a n i s h o m e t o u s . W e ' d l o v e t o s h"* over `#FFFFFF` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.section> — `Journeys, which don't exist in gui`)**:
   - Landmark `<section class="section">` rendering section `Journeys, which don't exist in guidebooks` with copy *"K y r g y z s t a n i s h o m e t o u s ."*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `cassette.webp`), and grid rule `html { scroll-behavior: smooth; overflow-x: hidden; -webkit-text-size-adjust: 1... }`.
4. **Interactive Detail & Feature Matrix (<section.section> — `Immersive nomadic experience`)**:
   - Landmark `<section class="section">` framing `Immersive nomadic experience` and `We also provide professional production services` (*"W e ' d l o v e t o s h o w i t t o y o u ."*) with `#dc2f02` surface cards, `#fff` accents, and `img { display: block; max-width: 100%; }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://tour-kyrgyzstan.com/`)**:
   - Landmark `<footer class="footer section--dark">` anchoring `Tour Kyrgyzstan — Central Asia, ` footer links (`Gallery · Expeditions`), copy *"Cycling Expedition"*, and `#0d0d0d` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: tour-kyrgyzstan-com (Tour Kyrgyzstan — Central Asia, unmapped)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `tour-kyrgyzstan-com` (**Tour Kyrgyzstan — Central Asia, unmapped** — `https://tour-kyrgyzstan.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#FFFFFF` canvas, `#000000` ink, `#fff` accent).
- **Identity & Domain Context**: Discover authentic Kyrgyzstan tours. Mountain trekking, nomadic culture, and professional video production services.
- **Primary Substrate**: `#FFFFFF` (`var(--paper)` in `:root`), **Primary Ink**: `#000000`, **Accent / Highlight**: `#fff`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#FFFFFF` (`var(--paper)` in `:root`) paired with `#000000` primary typography and `#fff` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Archivo` for display copy (`Central Asia like you've never imagi`) with `Fragment Mono` and `Fragment Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1400px` container bounds (`gap: 8px`, padding `24px`) with `cubic-bezier(.16,1,.3,1)` easing and Framer Motion Layout Physics.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `tour-kyrgyzstan-com` in your global stylesheet:

:root {
  /* Tour Kyrgyzstan — Central Asia, unmapped (tour-kyrgyzstan-com) — Ground-Truth Extracted CSS Variables */
  --paper: #FFFFFF; /* Canvas / Surface Token (tour-kyrgyzstan-com) */
  --ink: #000000; /* Typography Ink Token (tour-kyrgyzstan-com) */
  --ink-soft: rgba(0,0,0,.65); /* Typography Ink Token (tour-kyrgyzstan-com) */
  --ink-faint: rgba(0,0,0,.45); /* Typography Ink Token (tour-kyrgyzstan-com) */
  --hero-vh: 900px; /* Layout / Spatial Grid Token (tour-kyrgyzstan-com) */
  --seg-w: 30px; /* Dimension / Scale Token (tour-kyrgyzstan-com) */
  --tour-kyrgyzstan--bg: #FFFFFF; /* Canvas Substrate (from `var(--paper)` in `:root`) (tour-kyrgyzstan-com) */
  --tour-kyrgyzstan--ink: #000000; /* Primary Typography Ink (stylesheet-derived) (tour-kyrgyzstan-com) */
  --tour-kyrgyzstan--surface: #dc2f02; /* Surface Substrate (stylesheet-derived) (tour-kyrgyzstan-com) */
  --tour-kyrgyzstan--accent: #fff; /* Interactive Accent (stylesheet-derived) (tour-kyrgyzstan-com) */
  --tour-kyrgyzstan--muted: #b52501; /* Secondary Ink (stylesheet-derived) (tour-kyrgyzstan-com) */
  --tour-kyrgyzstan--border: #0d0d0d; /* Structural Border (stylesheet-derived) (tour-kyrgyzstan-com) */
  --tour-kyrgyzstan--container: 1400px; /* Container Bound (stylesheet-derived) (tour-kyrgyzstan-com) */
  --tour-kyrgyzstan--gap: 8px; /* Grid Gutter (stylesheet-derived) (tour-kyrgyzstan-com) */
  --tour-kyrgyzstan--pad: 24px; /* Lateral Padding (stylesheet-derived) (tour-kyrgyzstan-com) */
  --tour-kyrgyzstan--ease: cubic-bezier(.16,1,.3,1); /* Primary Easing Function (tour-kyrgyzstan-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#FFFFFF` — grounded in `var(--paper)` in `:root`
- **Primary Typography Ink**: `#000000` — grounded in `var(--ink)` in `:root`
- **Elevated Surface / Card Substrate**: `#dc2f02` — grounded in `.nav__links a:hover { color: #dc2f02 }`
- **Interactive Accent / Highlight**: `#fff` — grounded in `.nav__mobile-menu > a { color: #fff }`
- **Secondary / Muted Copy**: `#b52501` — grounded in `.hero__cta:hover { background: #b52501 }`
- **Structural Hairline Border**: `#0d0d0d` — grounded in `.section--dark { background: #0d0d0d }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×11869px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1400px` extracted from `tour-kyrgyzstan-com` stylesheet
- **Padding & Gutters**: `24px` lateral canvas padding with `8px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1400px`, `gap: 8px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `24px` horizontal padding
- **Media Queries**: `@media (hover: none), (max-width: 900px)`, `@media (max-width: 900px)`
- **Corner Radii**: `0%`, `50%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Archivo`
- **Body Font Stack**: `Fragment Mono`
- **Monospace / Technical Font Stack**: `Fragment Mono`
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `15px`, `12px`, `14px`, `13px`, `clamp(32px, 3.4vw, 72px)`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `15px`, `12px`, `14px`, `13px`, `clamp(32px, 3.4vw, 72px)`)
- **Body Copy Rule**: rule `body` (`font-weight: 400`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `15px`, `12px`, `14px`, `13px`, `clamp(32px, 3.4vw, 72px)`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `tour-kyrgyzstan-com` (`Tour Kyrgyzstan — Central Asia, unmapped`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.nav> — `tour-kyrgyzstan-com`)**:
   - DOM & Selectors: Landmark `<nav class="nav">` hosting `Tour Kyrgyzstan — Central Asia, unma` navigation (`Gallery · Expeditions`), DOM attributes (`data-line="0"`, `data-line="1"`, `data-index="0"`, `data-index="1"`), and stylesheet rule `root { --paper: FFFFFF; --ink: 000000; --ink-soft: rgba(0,0,0,.65); --ink-faint... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.nav> — `tour-kyrgyzstan-com`)` (`tour-kyrgyzstan-com`) adapts across `@media (hover: none), (max-width: 900px)`, `@media (max-width: 900px)` with `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.76,0,.24,1)` transitions and links `Gallery · Expeditions`.
2. **Hero Stage & Focal Lead (<section.hero> — `Central Asia like you've never ima`)**:
   - DOM & Selectors: Landmark `<section class="hero">` presenting display lead `Central Asia like you've never imagined` and copy excerpt *"K y r g y z s t a n i s h o m e t o u s . W e ' d l o v e t o s h"* over `#FFFFFF` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1440×11869px` desktop / `390×2400px` mobile) sets `#FFFFFF` background with `#000000` headline `Central Asia like you've never imagined`.
3. **Primary Showcase & Content Grid (<section.section> — `Journeys, which don't exist in gui`)**:
   - DOM & Selectors: Landmark `<section class="section">` rendering section `Journeys, which don't exist in guidebooks` with copy *"K y r g y z s t a n i s h o m e t o u s ."*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `cassette.webp`), and grid rule `html { scroll-behavior: smooth; overflow-x: hidden; -webkit-text-size-adjust: 1... }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.section> — `Journeys, which don't exist in gui`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1400px`, `gap: 8px`) on desktop and Single-column vertical stack at `390px` viewport width with `24px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.section> — `Immersive nomadic experience`)**:
   - DOM & Selectors: Landmark `<section class="section">` framing `Immersive nomadic experience` and `We also provide professional production services` (*"W e ' d l o v e t o s h o w i t t o y o u ."*) with `#dc2f02` surface cards, `#fff` accents, and `img { display: block; max-width: 100%; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.section> — `Immersive nomadic experience`)` uses `0%`, `50%` radii, `#fff` highlights, and assets (favicon.ico, favicon.svg, apple-touch-icon.png).
5. **Colophon & Global Directory Footer (<footer.footer> — `https://tour-kyrgyzstan.com/`)**:
   - DOM & Selectors: Landmark `<footer class="footer section--dark">` anchoring `Tour Kyrgyzstan — Central Asia, ` footer links (`Gallery · Expeditions`), copy *"Cycling Expedition"*, and `#0d0d0d` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer> — `https://tour-kyrgyzstan.com/`)` aligns to `1400px` extracted from `tour-kyrgyzstan-com` stylesheet with `24px` lateral canvas padding with `8px` grid gap and attributes (data-line="0", data-line="1", data-index="0").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"K y r g y z s t a n i s h o m e t o u s . W e ' d l o v e t o s h o w i t t o y o u ."*
- Copy Excerpt 2: *"K y r g y z s t a n i s h o m e t o u s ."*
- Copy Excerpt 3: *"W e ' d l o v e t o s h o w i t t o y o u ."*
- Copy Excerpt 4: *"Cycling Expedition"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.76,0,.24,1)`
- **Extracted Stylesheet Rules (`tour-kyrgyzstan-com`)**:
- `root { --paper: FFFFFF; --ink: 000000; --ink-soft: rgba(0,0,0,.65); --ink-faint... }`
- `html { scroll-behavior: smooth; overflow-x: hidden; -webkit-text-size-adjust: 1... }`
- `img { display: block; max-width: 100%; }`
- `body.intro-active .nav { display: none; }`
- `.nav__mark img { filter: none; }`
- **Per-Selector Transition Rules**:
- **Selector `.nav`**: `transition: color .35s ease, background .2s ease` extracted from `tour-kyrgyzstan-com` stylesheet.
- **Selector `.nav__burger-line`**: `transition: transform .3s ease, top .3s ease, width .3s ease, left .3s ease` extracted from `tour-kyrgyzstan-com` stylesheet.
- **Selector `.nav__mobile-menu`**: `transition: opacity .2s ease, transform .2s ease` extracted from `tour-kyrgyzstan-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<nav.nav>` and `<section.section>`.
- **Runtime Interaction Engine**: Integrates Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `tour-kyrgyzstan-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
