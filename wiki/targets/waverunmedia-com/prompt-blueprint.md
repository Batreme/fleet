---
title: "UI Prompt Blueprint: waverunmedia-com"
date: 2026-11-15
target: "[[overview|waverunmedia-com]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#6c6c89` canvas, `#f7f7f8` ink, `#e5e5e9` accent)"
---

# UI Design System & Master Generation Blueprint: waverunmedia-com

> **WaveRun Media** (https://waverunmedia.com/) — WaveRun Media captures the pulse of real stories that move markets and shape culture.

![Desktop Viewport Capture (1440x6506)](file:///root/projects/fleet/wiki/targets/waverunmedia-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **WaveRun Media** (`https://waverunmedia.com/`). WaveRun Media captures the pulse of real stories that move markets and shape culture.
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#6c6c89` canvas, `#f7f7f8` ink, `#e5e5e9` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#6c6c89` (`var(--wndb-gray)` in `:root`) paired with `#f7f7f8` primary typography and `#e5e5e9` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Satoshi` for display copy (`the flow of culture`) with `Satoshi` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1114px` container bounds (`gap: 1rem`, padding `32px`) with `cubic-bezier(.04,.05,.12,1.52)` easing and Lenis Smooth Scroll (`data-lenis`), Swiper Touch Carousel Engine.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/waverunmedia-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×6506px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `1114px` extracted from `waverunmedia-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `32px` lateral canvas padding with `1rem` grid gap.
- **Border Radius Scale**: `16px`, `10rem`, `50%`, `2px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1114px`, `gap: 1rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `32px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width:480px)`, `@media screen and (min-width:1024px)`, `@media screen and (min-width:1921px)`, `@media screen and (min-width:768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#6c6c89` | `var(--wndb-gray)` in `:root` |
| **Primary Typography Ink** | `#f7f7f8` | `var(--wndb-gray-50)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ebebef` | `var(--wndb-gray-100)` in `:root` |
| **Interactive Accent / Highlight** | `#e5e5e9` | `var(--wndb-gray-150)` in `:root` |
| **Secondary / Muted Copy** | `#d1d1db` | `var(--wndb-gray-200)` in `:root` |
| **Structural Hairline Border** | `#a9a9bc` | `var(--wndb-gray-300)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--slide-media-height` | `98.8vw` | Layout / Spatial Grid Token |
| `--wndb-mask-color` | `rgba(0,0,0,.15)` | Brand / Palette Token |
| `--wndb-mask-position` | `50% 50% at 50% 20%` | Dimension / Scale Token |
| `--wndb-mask-opacity` | `0.35` | Design System Custom Token |
| `--wndb--max-w--prose` | `min(65ch,1100px)` | Layout / Spatial Grid Token |
| `--wndb--text-scale-factor` | `1` | Typography Ink Token |
| `--wndb--text--xs` | `0.75rem` | Typography Ink Token |
| `--wndb--text--sm` | `0.875rem` | Typography Ink Token |
| `--wndb--text--base` | `1rem` | Typography Ink Token |
| `--wndb--text--md` | `1.125rem` | Typography Ink Token |
| `--wndb--text--lg` | `1.5rem` | Typography Ink Token |
| `--wndb--text--xl` | `2.375rem` | Typography Ink Token |
| `--wndb--text--huge` | `clamp(2.75rem,1.4688rem + 2.5vw,3.5rem)` | Typography Ink Token |
| `--wndb--text-giga` | `clamp(3.25rem,2.546875rem + 2.25vw,4.375rem)` | Typography Ink Token |
| `--nfd-wb-anim-transition-duration` | `1400ms` | Motion / Easing Token |
| `--nfd-wb-anim-transition-delay` | `50ms` | Motion / Easing Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Satoshi`.
- **Primary Body Stack**: `Satoshi`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `100%`, `62.5%`, `1.6rem`, `4.6rem`, `1em`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `100%`, `62.5%`, `1.6rem`, `4.6rem`, `1em`).
- **Body Copy**: CSS variables `--wndb--color--body: var(--wndb--color--surface)`.
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `100%`, `62.5%`, `1.6rem`, `4.6rem`, `1em`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.04,.05,.12,1.52)`, `cubic-bezier(.2,1,.8,1)`, `cubic-bezier(.68,.85,.17,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.btn`**: `transition: background-color .1s ease,color .1s ease` extracted from `waverunmedia-com` stylesheet.
- **Selector `.btn__arrow`**: `transition: .3s cubic-bezier(.04,.05,.12,1.52)` extracted from `waverunmedia-com` stylesheet.
- **Selector `.btn__arrow:after`**: `transition: -webkit-transform .3s cubic-bezier(.04,.05,.12,1.52),-webkit-f...` extracted from `waverunmedia-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.04,.05,.12,1.52)`)**: Governs interactive state transitions across `<header.header>` and `<section.hero>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — WaveRun Media                              │
│ ====================================================================== │
│ [ <header.header>          | Home · About · Partners · KWILL Adviso ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <article.universal>                                  |   │
│ | H1: the flow of culture                                          |   │
│ | Substrate: #6c6c89    | Ink: #f7f7f8    | Accent: #e5e5e9        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.hero>            ) max-w: 1114px         |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Stories in Motion            |  | Flippin’ in Heels            | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 1rem  ) | │
│ | [<header.header>] -> [<article.universal] -> [<section.hero>] |      │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>       ) | https://waverunmedia.com/          │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.header> — `waverunmedia-com`)**:
   - Landmark `<header class="header js-header">` hosting `WaveRun Media` navigation (`Home · About · Partners · KWILL Advisors · ADTV`), DOM attributes (`data-globals="("ajax_url":"https://..."`, `data-video-ready="true"`, `data-video-ready="true"`, `data-from="center"`), and stylesheet rule `html { font-size:100%;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100% }`.
2. **Hero Stage & Focal Lead (<article.universal> — `the flow of culture`)**:
   - Landmark `<article class="universal">` presenting display lead `the flow of culture` and copy excerpt *"Partners KWILL Advisors ADTV PopArt Studio Dr. Lilly Approved NBA"* over `#6c6c89` canvas and `#f7f7f8` ink.
3. **Primary Showcase & Content Grid (<section.hero> — `Stories in Motion`)**:
   - Landmark `<section class="hero hero--bottom">` rendering section `Stories in Motion` with copy *"Dr. Lilly Approved"*, asset references (`apple-icon-57x57.png`, `apple-icon-60x60.png`, `apple-icon-72x72.png`, `apple-icon-76x76.png`), and grid rule `a:active { outline:none }`.
4. **Interactive Detail & Feature Matrix (<section.slider-block> — `Flippin’ in Heels`)**:
   - Landmark `<section class="slider-block">` framing `Flippin’ in Heels` and `The Elevator Pitch` (*"WaveRun Media captures the pulse of real stories that move market"*) with `#ebebef` surface cards, `#e5e5e9` accents, and `strong { font-weight:700 }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://waverunmedia.com/`)**:
   - Landmark `<footer class="footer">` anchoring `WaveRun Media` footer links (`Home · About · Partners · KWILL Advisors · ADTV`), copy *"Flippin’ in Heels Featuring Rashauna Scott"*, and `#a9a9bc` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: waverunmedia-com (WaveRun Media)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `waverunmedia-com` (**WaveRun Media** — `https://waverunmedia.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#6c6c89` canvas, `#f7f7f8` ink, `#e5e5e9` accent).
- **Identity & Domain Context**: WaveRun Media captures the pulse of real stories that move markets and shape culture.
- **Primary Substrate**: `#6c6c89` (`var(--wndb-gray)` in `:root`), **Primary Ink**: `#f7f7f8`, **Accent / Highlight**: `#e5e5e9`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#6c6c89` (`var(--wndb-gray)` in `:root`) paired with `#f7f7f8` primary typography and `#e5e5e9` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Satoshi` for display copy (`the flow of culture`) with `Satoshi` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1114px` container bounds (`gap: 1rem`, padding `32px`) with `cubic-bezier(.04,.05,.12,1.52)` easing and Lenis Smooth Scroll (`data-lenis`), Swiper Touch Carousel Engine.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `waverunmedia-com` in your global stylesheet:

:root {
  /* WaveRun Media (waverunmedia-com) — Ground-Truth Extracted CSS Variables */
  --slide-media-height: 98.8vw; /* Layout / Spatial Grid Token (waverunmedia-com) */
  --wndb-mask-color: rgba(0,0,0,.15); /* Brand / Palette Token (waverunmedia-com) */
  --wndb-mask-position: 50% 50% at 50% 20%; /* Dimension / Scale Token (waverunmedia-com) */
  --wndb-mask-opacity: 0.35; /* Design System Custom Token (waverunmedia-com) */
  --wndb--max-w--prose: min(65ch,1100px); /* Layout / Spatial Grid Token (waverunmedia-com) */
  --wndb--text-scale-factor: 1; /* Typography Ink Token (waverunmedia-com) */
  --wndb--text--xs: 0.75rem; /* Typography Ink Token (waverunmedia-com) */
  --wndb--text--sm: 0.875rem; /* Typography Ink Token (waverunmedia-com) */
  --wndb--text--base: 1rem; /* Typography Ink Token (waverunmedia-com) */
  --wndb--text--md: 1.125rem; /* Typography Ink Token (waverunmedia-com) */
  --wndb--text--lg: 1.5rem; /* Typography Ink Token (waverunmedia-com) */
  --wndb--text--xl: 2.375rem; /* Typography Ink Token (waverunmedia-com) */
  --wndb--text--huge: clamp(2.75rem,1.4688rem + 2.5vw,3.5rem); /* Typography Ink Token (waverunmedia-com) */
  --wndb--text-giga: clamp(3.25rem,2.546875rem + 2.25vw,4.375rem); /* Typography Ink Token (waverunmedia-com) */
  --nfd-wb-anim-transition-duration: 1400ms; /* Motion / Easing Token (waverunmedia-com) */
  --nfd-wb-anim-transition-delay: 50ms; /* Motion / Easing Token (waverunmedia-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#6c6c89` — grounded in `var(--wndb-gray)` in `:root`
- **Primary Typography Ink**: `#f7f7f8` — grounded in `var(--wndb-gray-50)` in `:root`
- **Elevated Surface / Card Substrate**: `#ebebef` — grounded in `var(--wndb-gray-100)` in `:root`
- **Interactive Accent / Highlight**: `#e5e5e9` — grounded in `var(--wndb-gray-150)` in `:root`
- **Secondary / Muted Copy**: `#d1d1db` — grounded in `var(--wndb-gray-200)` in `:root`
- **Structural Hairline Border**: `#a9a9bc` — grounded in `var(--wndb-gray-300)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×6506px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1114px` extracted from `waverunmedia-com` stylesheet
- **Padding & Gutters**: `32px` lateral canvas padding with `1rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1114px`, `gap: 1rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `32px` horizontal padding
- **Media Queries**: `@media screen and (max-width:480px)`, `@media screen and (min-width:1024px)`, `@media screen and (min-width:1921px)`, `@media screen and (min-width:768px)`
- **Corner Radii**: `16px`, `10rem`, `50%`, `2px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Satoshi`
- **Body Font Stack**: `Satoshi`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `100%`, `62.5%`, `1.6rem`, `4.6rem`, `1em`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `100%`, `62.5%`, `1.6rem`, `4.6rem`, `1em`)
- **Body Copy Rule**: CSS variables `--wndb--color--body: var(--wndb--color--surface)`
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `100%`, `62.5%`, `1.6rem`, `4.6rem`, `1em`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `waverunmedia-com` (`WaveRun Media`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.header> — `waverunmedia-com`)**:
   - DOM & Selectors: Landmark `<header class="header js-header">` hosting `WaveRun Media` navigation (`Home · About · Partners · KWILL Advisors · ADTV`), DOM attributes (`data-globals="("ajax_url":"https://..."`, `data-video-ready="true"`, `data-video-ready="true"`, `data-from="center"`), and stylesheet rule `html { font-size:100%;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100% }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.header> — `waverunmedia-com`)` (`waverunmedia-com`) adapts across `@media screen and (max-width:480px)`, `@media screen and (min-width:1024px)`, `@media screen and (min-width:1921px)`, `@media screen and (min-width:768px)` with `cubic-bezier(.04,.05,.12,1.52)`, `cubic-bezier(.2,1,.8,1)`, `cubic-bezier(.68,.85,.17,1)` transitions and links `Home · About · Partners · KWILL Advisors · ADTV`.
2. **Hero Stage & Focal Lead (<article.universal> — `the flow of culture`)**:
   - DOM & Selectors: Landmark `<article class="universal">` presenting display lead `the flow of culture` and copy excerpt *"Partners KWILL Advisors ADTV PopArt Studio Dr. Lilly Approved NBA"* over `#6c6c89` canvas and `#f7f7f8` ink.
   - Responsive Contract: Hero stage (`1440×6506px` desktop / `390×2400px` mobile) sets `#6c6c89` background with `#f7f7f8` headline `the flow of culture`.
3. **Primary Showcase & Content Grid (<section.hero> — `Stories in Motion`)**:
   - DOM & Selectors: Landmark `<section class="hero hero--bottom">` rendering section `Stories in Motion` with copy *"Dr. Lilly Approved"*, asset references (`apple-icon-57x57.png`, `apple-icon-60x60.png`, `apple-icon-72x72.png`, `apple-icon-76x76.png`), and grid rule `a:active { outline:none }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.hero> — `Stories in Motion`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1114px`, `gap: 1rem`) on desktop and Single-column vertical stack at `390px` viewport width with `32px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.slider-block> — `Flippin’ in Heels`)**:
   - DOM & Selectors: Landmark `<section class="slider-block">` framing `Flippin’ in Heels` and `The Elevator Pitch` (*"WaveRun Media captures the pulse of real stories that move market"*) with `#ebebef` surface cards, `#e5e5e9` accents, and `strong { font-weight:700 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.slider-block> — `Flippin’ in Heels`)` uses `16px`, `10rem`, `50%`, `2px` radii, `#e5e5e9` highlights, and assets (apple-icon-57x57.png, apple-icon-60x60.png, apple-icon-72x72.png).
5. **Colophon & Global Directory Footer (<footer.footer> — `https://waverunmedia.com/`)**:
   - DOM & Selectors: Landmark `<footer class="footer">` anchoring `WaveRun Media` footer links (`Home · About · Partners · KWILL Advisors · ADTV`), copy *"Flippin’ in Heels Featuring Rashauna Scott"*, and `#a9a9bc` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer> — `https://waverunmedia.com/`)` aligns to `1114px` extracted from `waverunmedia-com` stylesheet with `32px` lateral canvas padding with `1rem` grid gap and attributes (data-globals="("ajax_url":"https://...", data-video-ready="true", data-video-ready="true").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Partners KWILL Advisors ADTV PopArt Studio Dr. Lilly Approved NBA"*
- Copy Excerpt 2: *"Dr. Lilly Approved"*
- Copy Excerpt 3: *"WaveRun Media captures the pulse of real stories that move markets and shape culture."*
- Copy Excerpt 4: *"Flippin’ in Heels Featuring Rashauna Scott"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.04,.05,.12,1.52)`, `cubic-bezier(.2,1,.8,1)`, `cubic-bezier(.68,.85,.17,1)`
- **Extracted Stylesheet Rules (`waverunmedia-com`)**:
- `html { font-size:100%;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100% }`
- `a:active { outline:none }`
- `strong { font-weight:700 }`
- `img { border:0;-ms-interpolation-mode:bicubic;vertical-align:middle }`
- `textarea { vertical-align:middle }`
- **Per-Selector Transition Rules**:
- **Selector `.btn`**: `transition: background-color .1s ease,color .1s ease` extracted from `waverunmedia-com` stylesheet.
- **Selector `.btn__arrow`**: `transition: .3s cubic-bezier(.04,.05,.12,1.52)` extracted from `waverunmedia-com` stylesheet.
- **Selector `.btn__arrow:after`**: `transition: -webkit-transform .3s cubic-bezier(.04,.05,.12,1.52),-webkit-f...` extracted from `waverunmedia-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.04,.05,.12,1.52)`)**: Governs interactive state transitions across `<header.header>` and `<section.hero>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `waverunmedia-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
