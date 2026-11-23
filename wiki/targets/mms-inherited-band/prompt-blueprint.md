---
title: "UI Prompt Blueprint: mms-inherited-band"
date: 2026-11-23
captured_at: 2026-11-23
target: "mms-inherited-band"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier2_webgl
http_status: 200
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#262424` / `#fffdf6`)"
---

# UI Design System & Master Generation Blueprint: mms-inherited-band

> **INHERITED – ME, MYSELF & SAM (EP DEBUT)** (https://mms.inherited.band/) — A cinematic deathcore EP built around three stories, three characters, and a world of evidence. Me, Myself and Sam turns music into an in...

![Desktop Viewport Capture (1440x900)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **INHERITED – ME, MYSELF & SAM (EP DEBUT)** (`https://mms.inherited.band/`). A cinematic deathcore EP built around three stories, three characters, and a world of evidence. Me, Myself and Sam turns music into an in...
- **Capture Provenance**: Live browser capture (`tier2_webgl`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#262424` / `#fffdf6`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#262424` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#fffdf6` primary typography and `#fffdf6` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Segoe UI` for display copy (`INHERITED – ME, MYSELF & SAM (EP DEB`) with `Segoe UI` and `Founder Grotesk Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `96rem` container bounds (`gap: 1.5rem`, padding `2rem`) with `cubic-bezier(.25,.46,.45,.94)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x844)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×900px` (`assets/desktop.png`, single-viewport 100vh live capture (900px)), Mobile `390×844px` (`assets/mobile.png`, single-viewport 100vh live capture (844px)).
- **Master Container Bounds**: `96rem` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `2rem` lateral canvas padding with `1.5rem` grid gap.
- **Border Radius Scale**: `0px` (sharp unrounded corners).

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: 1.5rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `2rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (width>=64em)`, `@media (width>=40rem)`, `@media (width>=48rem)`, `@media (width>=64rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#262424` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#fffdf6` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#0a0909` | `.loader__background.svelte-1ojmd8e { background: #0a0909 }` |
| **Interactive Accent / Highlight** | `#fffdf6` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#b4b4b4` | `.tc--light-grey { color: #b4b4b4 }` |
| **Structural Hairline Border** | `#464443` | `.grid-helper__col-inner.svelte-... { border: #464443 }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bw` | `100vw` | Dimension / Scale Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--default-transition-duration` | `.15s` | Motion / Easing Token |
| `--default-transition-timing-function` | `cubic-bezier(.4, 0, .2, 1)` | Motion / Easing Token |
| `--default-font-family` | `var(--font-sans)` | Typography / Scale Token |
| `--default-mono-font-family` | `var(--font-mono)` | Typography / Scale Token |
| `--max-container` | `100vw` | Layout / Spatial Grid Token |
| `--outer-margin` | `24px` | Layout / Spatial Grid Token |
| `--grid-gap` | `0px` | Layout / Spatial Grid Token |
| `--grid-size` | `calc(var(--bw) - (var(--outer-margin) * 2))` | Layout / Spatial Grid Token |
| `--grid-max-size` | `calc(var(--max-container) - (var(--outer-margin) * 2))` | Layout / Spatial Grid Token |
| `--image-height` | `min(80vw / var(--image-ratio), 60lvh)` | Layout / Spatial Grid Token |
| `--progress` | `50%` | Dimension / Scale Token |
| `--tw-rotate-x` | `initial` | Design System Custom Token |
| `--mms-inherited-ba-bg` | `#262424` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--mms-inherited-ba-ink` | `#fffdf6` | Primary Typography Ink (computed-derived) |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Segoe UI`.
- **Primary Body Stack**: `Segoe UI`.
- **Technical / Metadata Stack**: `Founder Grotesk Mono`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 12px`, `line-height: 18px`, `font-weight: 400`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 12px`, `line-height: 18px`, `font-weight: 400`).
- **Body Copy**: live computed `body` (`font-size: 12px`, `line-height: 18px`, `font-weight: 400`); rule `,body` (`font-size: 16px`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: 18px`, `font-weight: 400`); CSS variables `--default-mono-font-family: var(--font-mono)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.25,.46,.45,.94)`, `cubic-bezier(.215,.61,.355,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `oader.svelte-1ojmd8e .loader__evi...`**: `transition: opacity .5s cubic-bezier(.25,.46,.45,.94) .75s` extracted from `mms-inherited-band` stylesheet.
- **Selector `.loader-layer--loading.svelte-1oj...`**: `transition: all .3s cubic-bezier(.25,.46,.45,.94)` extracted from `mms-inherited-band` stylesheet.
- **Selector `media (width>=64em)`**: `transition: opacity .3s cubic-bezier(.25,.46,.45,.94)` extracted from `mms-inherited-band` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.25,.46,.45,.94)`)**: Governs interactive state transitions across `<header.app>` and `<section.sr-only:nth(2)>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — INHERITED – ME, MYSELF & SAM (EP DEBUT)    │
│ ====================================================================== │
│ [ <header.app> (1440px)               | IG · TIKTOK · inherited.band ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.sr-only> (w=1440px)                           | │
│ | H1: INHERITED – ME, MYSELF & SAM (EP DEBUT)                        | │
│ | Substrate: #262424 | Ink: #fffdf6 | Accent: #fffdf6                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.sr-only:nth(2)>) max-w: 96rem              | │
│ | +------------------------------+  +------------------------------+ | │
│ | | THE UNIDENTIFIED SUBJECT     |  | THE MODEL CITIZEN            | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.sr-only:nth(3)>) — Diego Castro            | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.svelte-hy959) | https://mms.inherited.band/          │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 1.5rem)     │
│ ====================================================================== │
│ [ HEADER BAR (<header.app>            ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.sr-only>) — 390px Vertical Lead               | │
│ | H1: INHERITED – ME, MYSELF & SAM (EP DEBUT)                        | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.sr-only:nth(2) — 1-Col Stack              | │
│ | [ Item 1: THE UNIDENTIFIED SUBJECT                               ] | │
│ | [ Item 2: THE MODEL CITIZEN                                      ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.sr-only:nth(3)>) — 1-Col (Diego Castro)     | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.svelte-hy959) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.app> — `mms-inherited-band`)**:
   - Landmark `<header class="app">` (`1440px`) hosting `INHERITED – ME, MYSELF & SAM (EP DEB` navigation (`IG · TIKTOK · inherited.band · INHERITED.BAND`), DOM attributes (`data-sveltekit-preload-data="hover"`, `data-engine="three.js r180"`, `data-cta-audio`), and stylesheet rule `.webgl-container.svelte-hy9597 { z-index:1;width:100vw;height:100lvh;position:fixed;top:0;left:0 }`.
2. **Hero Stage & Focal Lead (<section.sr-only> — `INHERITED – ME, MYSELF & SAM (EP D`)**:
   - Landmark `<section class="sr-only">` presenting display lead `INHERITED – ME, MYSELF & SAM (EP DEBUT)` and copy excerpt *"THE INDIVIDUAL MAY APPEAR CALM AND APPROACHABLE, OFTEN USING A VE"* over `#262424` canvas and `#fffdf6` ink.
3. **Primary Showcase & Content Grid (<section.sr-only:nth(2)> — `THE UNIDENTIFIED SUBJECT`)**:
   - Landmark `<section class="sr-only">` rendering section `THE UNIDENTIFIED SUBJECT` with copy *"The individual may appear calm and approachable, often using a ve"*, asset references (`FoundersGrotesk-Medium.woff2`, `FoundersGroteskMono-Regular.woff2`, `favicon.ico`, `favicon.svg`), and grid rule `.webgl-container__canvas.svelte-h... { width:100%;height:100% }`.
4. **Interactive Detail & Feature Matrix (<section.sr-only:nth(3)> — `THE MODEL CITIZEN`)**:
   - Landmark `<section class="sr-only">` framing `THE MODEL CITIZEN` and `Diego Castro` (*"Do not approach. If you recognize this individual, contact inheri"*) with `#0a0909` surface cards, `#fffdf6` accents, and `.audio-ctas.svelte-186a61h { align-items:center;gap:1.5rem;margin-top:2rem;display:flex }`.
5. **Colophon & Global Directory Footer (<footer.svelte-hy9597> — `https://mms.inherited.band/`)**:
   - Landmark `<footer class="svelte-hy9597">` anchoring `INHERITED – ME, MYSELF & SAM (EP` footer links (`IG · TIKTOK · inherited.band · INHERITED.BAND`), copy *"The individual may not appear to be the primary threat. He i"*, and `#464443` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: mms-inherited-band (INHERITED – ME, MYSELF & SAM (EP DEBUT))

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `mms-inherited-band` (**INHERITED – ME, MYSELF & SAM (EP DEBUT)** — `https://mms.inherited.band/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#262424` / `#fffdf6`).
- **Identity & Domain Context**: A cinematic deathcore EP built around three stories, three characters, and a world of evidence. Me, Myself and Sam turns music into an in...
- **Primary Substrate**: `#262424` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#fffdf6`, **Accent / Highlight**: `#fffdf6`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#262424` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#fffdf6` primary typography and `#fffdf6` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Segoe UI` for display copy (`INHERITED – ME, MYSELF & SAM (EP DEB`) with `Segoe UI` and `Founder Grotesk Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `96rem` container bounds (`gap: 1.5rem`, padding `2rem`) with `cubic-bezier(.25,.46,.45,.94)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `mms-inherited-band` in your global stylesheet:

:root {
  /* INHERITED – ME, MYSELF & SAM (EP DEBUT) (mms-inherited-band) — Live-Grounded CSS Variables */
  --bw: 100vw; /* Dimension / Scale Token (mms-inherited-band) */
  --spacing: .25rem; /* Layout / Spatial Grid Token (mms-inherited-band) */
  --default-transition-duration: .15s; /* Motion / Easing Token (mms-inherited-band) */
  --default-transition-timing-function: cubic-bezier(.4, 0, .2, 1); /* Motion / Easing Token (mms-inherited-band) */
  --default-font-family: var(--font-sans); /* Typography / Scale Token (mms-inherited-band) */
  --default-mono-font-family: var(--font-mono); /* Typography / Scale Token (mms-inherited-band) */
  --max-container: 100vw; /* Layout / Spatial Grid Token (mms-inherited-band) */
  --outer-margin: 24px; /* Layout / Spatial Grid Token (mms-inherited-band) */
  --grid-gap: 0px; /* Layout / Spatial Grid Token (mms-inherited-band) */
  --grid-size: calc(var(--bw) - (var(--outer-margin) * 2)); /* Layout / Spatial Grid Token (mms-inherited-band) */
  --grid-max-size: calc(var(--max-container) - (var(--outer-margin) * 2)); /* Layout / Spatial Grid Token (mms-inherited-band) */
  --image-height: min(80vw / var(--image-ratio), 60lvh); /* Layout / Spatial Grid Token (mms-inherited-band) */
  --progress: 50%; /* Dimension / Scale Token (mms-inherited-band) */
  --tw-rotate-x: initial; /* Design System Custom Token (mms-inherited-band) */
  --mms-inherited-ba-bg: #262424; /* Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) (mms-inherited-band) */
  --mms-inherited-ba-ink: #fffdf6; /* Primary Typography Ink (computed-derived) (mms-inherited-band) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#262424` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#fffdf6` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#0a0909` — grounded in `.loader__background.svelte-1ojmd8e { background: #0a0909 }`
- **Interactive Accent / Highlight**: `#fffdf6` — grounded in live computed `a` `color` (`computed_styles.json`)
- **Secondary / Muted Copy**: `#b4b4b4` — grounded in `.tc--light-grey { color: #b4b4b4 }`
- **Structural Hairline Border**: `#464443` — grounded in `.grid-helper__col-inner.svelte-... { border: #464443 }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×900px` (single-viewport 100vh live capture (900px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×844px` (single-viewport 100vh live capture (844px), `390px` standard mobile width).
- **Container Max-Width**: `96rem` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `2rem` lateral canvas padding with `1.5rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: 1.5rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `2rem` horizontal padding
- **Media Queries**: `@media (width>=64em)`, `@media (width>=40rem)`, `@media (width>=48rem)`, `@media (width>=64rem)`
- **Corner Radii**: `0px` (sharp unrounded corners)

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Segoe UI`
- **Body Font Stack**: `Segoe UI`
- **Monospace / Technical Font Stack**: `Founder Grotesk Mono`
- **H1 Display Rule**: live computed `h1` (`font-size: 12px`, `line-height: 18px`, `font-weight: 400`)
- **H2 Section Rule**: live computed `h2` (`font-size: 12px`, `line-height: 18px`, `font-weight: 400`)
- **Body Copy Rule**: live computed `body` (`font-size: 12px`, `line-height: 18px`, `font-weight: 400`); rule `,body` (`font-size: 16px`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 12px`, `line-height: 18px`, `font-weight: 400`); CSS variables `--default-mono-font-family: var(--font-mono)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `mms-inherited-band` (`INHERITED – ME, MYSELF & SAM (EP DEBUT)`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.app> — `mms-inherited-band`)**:
   - DOM & Selectors: Landmark `<header class="app">` (`1440px`) hosting `INHERITED – ME, MYSELF & SAM (EP DEB` navigation (`IG · TIKTOK · inherited.band · INHERITED.BAND`), DOM attributes (`data-sveltekit-preload-data="hover"`, `data-engine="three.js r180"`, `data-cta-audio`), and stylesheet rule `.webgl-container.svelte-hy9597 { z-index:1;width:100vw;height:100lvh;position:fixed;top:0;left:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.app> — `mms-inherited-band`)` (`mms-inherited-band`) adapts across `@media (width>=64em)`, `@media (width>=40rem)`, `@media (width>=48rem)`, `@media (width>=64rem)` with `cubic-bezier(.25,.46,.45,.94)`, `cubic-bezier(.215,.61,.355,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `IG · TIKTOK · inherited.band · INHERITED.BAND`.
2. **Hero Stage & Focal Lead (<section.sr-only> — `INHERITED – ME, MYSELF & SAM (EP D`)**:
   - DOM & Selectors: Landmark `<section class="sr-only">` presenting display lead `INHERITED – ME, MYSELF & SAM (EP DEBUT)` and copy excerpt *"THE INDIVIDUAL MAY APPEAR CALM AND APPROACHABLE, OFTEN USING A VE"* over `#262424` canvas and `#fffdf6` ink.
   - Responsive Contract: Hero stage (`1440×900px` desktop / `390×844px` mobile) sets `#262424` background with `#fffdf6` headline `INHERITED – ME, MYSELF & SAM (EP DEBUT)`.
3. **Primary Showcase & Content Grid (<section.sr-only:nth(2)> — `THE UNIDENTIFIED SUBJECT`)**:
   - DOM & Selectors: Landmark `<section class="sr-only">` rendering section `THE UNIDENTIFIED SUBJECT` with copy *"The individual may appear calm and approachable, often using a ve"*, asset references (`FoundersGrotesk-Medium.woff2`, `FoundersGroteskMono-Regular.woff2`, `favicon.ico`, `favicon.svg`), and grid rule `.webgl-container__canvas.svelte-h... { width:100%;height:100% }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.sr-only:nth(2)> — `THE UNIDENTIFIED SUBJECT`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: 1.5rem`) on desktop and Single-column vertical stack at `390px` viewport width with `2rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.sr-only:nth(3)> — `THE MODEL CITIZEN`)**:
   - DOM & Selectors: Landmark `<section class="sr-only">` framing `THE MODEL CITIZEN` and `Diego Castro` (*"Do not approach. If you recognize this individual, contact inheri"*) with `#0a0909` surface cards, `#fffdf6` accents, and `.audio-ctas.svelte-186a61h { align-items:center;gap:1.5rem;margin-top:2rem;display:flex }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.sr-only:nth(3)> — `THE MODEL CITIZEN`)` uses `0px` (sharp unrounded corners) radii, `#fffdf6` highlights, and assets (FoundersGrotesk-Medium.woff2, FoundersGroteskMono-Regular.woff2, favicon.ico).
5. **Colophon & Global Directory Footer (<footer.svelte-hy9597> — `https://mms.inherited.band/`)**:
   - DOM & Selectors: Landmark `<footer class="svelte-hy9597">` anchoring `INHERITED – ME, MYSELF & SAM (EP` footer links (`IG · TIKTOK · inherited.band · INHERITED.BAND`), copy *"The individual may not appear to be the primary threat. He i"*, and `#464443` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.svelte-hy9597> — `https://mms.inherited.band/`)` aligns to `96rem` (non-`@media` desktop container stylesheet rule) with `2rem` lateral canvas padding with `1.5rem` grid gap and attributes (data-sveltekit-preload-data="hover", data-engine="three.js r180", data-cta-audio).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"THE INDIVIDUAL MAY APPEAR CALM AND APPROACHABLE, OFTEN USING A VEHICLE TO ISOLATE..."*
- Copy Excerpt 2: *"The individual may appear calm and approachable, often using a vehicle to isolate..."*
- Copy Excerpt 3: *"Do not approach. If you recognize this individual, contact inherited.band ."*
- Copy Excerpt 4: *"The individual may not appear to be the primary threat. He is believed to operate..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.25,.46,.45,.94)`, `cubic-bezier(.215,.61,.355,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`mms-inherited-band`)**:
- `.webgl-container.svelte-hy9597 { z-index:1;width:100vw;height:100lvh;position:fixed;top:0;left:0 }`
- `.webgl-container__canvas.svelte-h... { width:100%;height:100% }`
- `.audio-ctas.svelte-186a61h { align-items:center;gap:1.5rem;margin-top:2rem;display:flex }`
- `.loader.is-visible.svelte-1ojmd8e { pointer-events:auto }`
- `.loader__background.svelte-1ojmd8e { opacity:.5;background:0a0909;width:100%;height:100%;position:absolute;to... }`
- **Per-Selector Transition Rules**:
- **Selector `oader.svelte-1ojmd8e .loader__evi...`**: `transition: opacity .5s cubic-bezier(.25,.46,.45,.94) .75s` extracted from `mms-inherited-band` stylesheet.
- **Selector `.loader-layer--loading.svelte-1oj...`**: `transition: all .3s cubic-bezier(.25,.46,.45,.94)` extracted from `mms-inherited-band` stylesheet.
- **Selector `media (width>=64em)`**: `transition: opacity .3s cubic-bezier(.25,.46,.45,.94)` extracted from `mms-inherited-band` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.25,.46,.45,.94)`)**: Governs interactive state transitions across `<header.app>` and `<section.sr-only:nth(2)>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `mms-inherited-band`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
