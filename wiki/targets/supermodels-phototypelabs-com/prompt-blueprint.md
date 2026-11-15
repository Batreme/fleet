---
title: "UI Prompt Blueprint: supermodels-phototypelabs-com"
date: 2026-11-15
target: "[[overview|supermodels-phototypelabs-com]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#f7f6f2` / `#000`)"
---

# UI Design System & Master Generation Blueprint: supermodels-phototypelabs-com

> **SUPERMODELS — Image, Video, Voice & Music, Pay Per Use** (https://supermodels.phototypelabs.com) — SUPERMODELS is a creative platform for images, video, voice, music, and text with leading models. Pay per use, with no subscription.

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/supermodels-phototypelabs-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **SUPERMODELS — Image, Video, Voice & Music, Pay Per Use** (`https://supermodels.phototypelabs.com`). SUPERMODELS is a creative platform for images, video, voice, music, and text with leading models. Pay per use, with no subscription.
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#f7f6f2` / `#000`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#f7f6f2` (`var(--studio-category-color)` in `:root`) paired with `#000` primary typography and `#000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Onest` for display copy (`Your ideas. One creative platform.`) with `DM Sans` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `10ch` container bounds (`gap: .65rem`, padding `.27rem`) with `cubic-bezier(.2,.8,.2,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/supermodels-phototypelabs-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `10ch` extracted from `supermodels-phototypelabs-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `.27rem` lateral canvas padding with `.65rem` grid gap.
- **Border Radius Scale**: `999px`, `50%`, `var(--radius-sm)`, `.7rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 10ch`, `gap: .65rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `.27rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (width<=1000px)`, `@media (width<=550px)`, `@media (width<=900px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f7f6f2` | `var(--studio-category-color)` in `:root` |
| **Primary Typography Ink** | `#283a2d` | `var(--category-tag-bg)` in `:root` |
| **Elevated Surface / Card Substrate** | `#57d778` | `var(--category-tag-ink)` in `:root` |
| **Interactive Accent / Highlight** | `#000` | `var(--site-frame)` in `:root` |
| **Secondary / Muted Copy** | `#ecebe7` | `var(--editorial-ground)` in `:root` |
| **Structural Hairline Border** | `#171715` | `var(--editorial-ink)` in `:root` |
| **Variable Token (`--landing-on-dark-muted`)** | `#f7f6f2bf` | `var(--landing-on-dark-muted)` in `:root` |
| **Variable Token (`--landing-dark-line`)** | `#f7f6f247` | `var(--landing-dark-line)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--category-dot` | `var(--editorial-paper)` | Design System Custom Token |
| `--landing-content-inset` | `clamp(24px, 4.2vw, 68px)` | Dimension / Scale Token |
| `--paper` | `var(--editorial-paper)` | Canvas / Surface Token |
| `--ink` | `var(--editorial-ink)` | Typography Ink Token |
| `--muted` | `var(--editorial-muted)` | Design System Custom Token |
| `--line` | `var(--editorial-rule)` | Design System Custom Token |
| `--serif` | `var(--font-editorial)` | Typography / Scale Token |
| `--sans` | `var(--font-sans)` | Typography / Scale Token |
| `--headline` | `var(--font-display)` | Design System Custom Token |
| `--font-mono` | `var(--font-sans)` | Typography / Scale Token |
| `--landing-dark` | `var(--editorial-ink)` | Canvas / Surface Token |
| `--landing-on-dark` | `var(--editorial-paper)` | Canvas / Surface Token |
| `--landing-on-dark-muted` | `#f7f6f2bf` | Canvas / Surface Token |
| `--landing-dark-line` | `#f7f6f247` | Canvas / Surface Token |
| `--landing-quiet` | `var(--editorial-paper-quiet)` | Design System Custom Token |
| `--landing-heading-size` | `clamp(2.35rem, 5.2vw, 5.25rem)` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Onest`.
- **Primary Body Stack**: `DM Sans`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--font-display: "Manrope", var(--font-sans)`.
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.75rem`, `.65rem`, `2rem`, `1.4rem`, `clamp(7rem,14vw,14rem)`).
- **Body Copy**: CSS variables `--landing-body-size: .9375rem`.
- **Metadata & Navigation Labels**: CSS variables `--font-mono: var(--font-sans)`, `--landing-label-size: .75rem`, `--hero-brand-letter-spacing: 0.02em`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.2,.8,.2,1)`, `cubic-bezier(.22,.61,.36,1)`, `cubic-bezier(.2,.75,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.app-slider-fill[data-v-c750e325]`**: `transition: width .16s cubic-bezier(.2,.8,.2,1)` extracted from `supermodels-phototypelabs-com` stylesheet.
- **Selector `nput[data-v-c750e325]::-webkit-sl...`**: `transition: transform .18s cubic-bezier(.2,.8,.2,1)` extracted from `supermodels-phototypelabs-com` stylesheet.
- **Selector `er-input[data-v-c750e325]::-moz-r...`**: `transition: transform .18s cubic-bezier(.2,.8,.2,1)` extracted from `supermodels-phototypelabs-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.2,.8,.2,1)`)**: Governs interactive state transitions across `<header.editorial-header>` and `<section.principles-section>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — SUPERMODELS — Image, Video, Voice & Music, │
│ ====================================================================== │
│ [ <header.editorial-header | Models · Providers · Pricing · Example ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.editorial-hero>                             |   │
│ | H1: Your ideas. One creative platform.                           |   │
│ | Substrate: #f7f6f2    | Ink: #000       | Accent: #000           |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.principles-sectio) max-w: 10ch           |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Pay per use                  |  | Model choice                 | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .65rem) | │
│ | [<header.editorial-] -> [<section.editorial] -> [<section.principle] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.creative-foote) | https://supermodels.phototypelabs. │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.editorial-header> — `supermodels-phototypelabs-com`)**:
   - Landmark `<header class="editorial-header">` hosting `SUPERMODELS — Image, Video, Voice & ` navigation (`Models · Providers · Pricing · Examples · News`), DOM attributes (`data-landing-brand="SUPERMODELS"`, `data-landing-brand-weight="700"`, `data-landing-brand-spacing="0.02"`, `data-landing-font="Onest"`), and stylesheet rule `webkit-slider-runnable-track { background:0 0;height:.32rem }`.
2. **Hero Stage & Focal Lead (<section.editorial-hero> — `Your ideas. One creative platform.`)**:
   - Landmark `<section class="editorial-hero">` presenting display lead `Your ideas. One creative platform.` and copy excerpt *"Explore leading models for images, video, voice, music, and text."* over `#f7f6f2` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.principles-section> — `Pay per use`)**:
   - Landmark `<section class="principles-section platform-overview">` rendering section `Pay per use` with copy *"Pick a model. Type a prompt. Get a result."*, asset references (`favicon.svg`, `favicon.png`, `favicon.ico`, `apple-touch-icon.png`), and grid rule `moz-range-track { background:0 0;height:.32rem }`.
4. **Interactive Detail & Feature Matrix (<article.editorial-landing> — `Model choice`)**:
   - Landmark `<article class="editorial-landing">` framing `Model choice` and `Batch comparisons` (*"No subscription. Add wallet credit from $10 and see the estimated"*) with `#57d778` surface cards, `#000` accents, and `active::-webkit-slider-thumb { transform:scale(1.24) }`.
5. **Colophon & Global Directory Footer (<footer.creative-footer> — `https://supermodels.phototypelabs.com`)**:
   - Landmark `<footer class="creative-footer">` anchoring `SUPERMODELS — Image, Video, Voic` footer links (`Models · Providers · Pricing · Examples · News`), copy *"Explore about 47 published models from OpenAI, Google, Anthr"*, and `#171715` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: supermodels-phototypelabs-com (SUPERMODELS — Image, Video, Voice & Music, Pay Per Use)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `supermodels-phototypelabs-com` (**SUPERMODELS — Image, Video, Voice & Music, Pay Per Use** — `https://supermodels.phototypelabs.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f7f6f2` / `#000`).
- **Identity & Domain Context**: SUPERMODELS is a creative platform for images, video, voice, music, and text with leading models. Pay per use, with no subscription.
- **Primary Substrate**: `#f7f6f2` (`var(--studio-category-color)` in `:root`), **Primary Ink**: `#000`, **Accent / Highlight**: `#000`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#f7f6f2` (`var(--studio-category-color)` in `:root`) paired with `#000` primary typography and `#000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Onest` for display copy (`Your ideas. One creative platform.`) with `DM Sans` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `10ch` container bounds (`gap: .65rem`, padding `.27rem`) with `cubic-bezier(.2,.8,.2,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `supermodels-phototypelabs-com` in your global stylesheet:

:root {
  /* SUPERMODELS — Image, Video, Voice & Music, Pay Per Use (supermodels-phototypelabs-com) — Ground-Truth Extracted CSS Variables */
  --category-dot: var(--editorial-paper); /* Design System Custom Token (supermodels-phototypelabs-com) */
  --landing-content-inset: clamp(24px, 4.2vw, 68px); /* Dimension / Scale Token (supermodels-phototypelabs-com) */
  --paper: var(--editorial-paper); /* Canvas / Surface Token (supermodels-phototypelabs-com) */
  --ink: var(--editorial-ink); /* Typography Ink Token (supermodels-phototypelabs-com) */
  --muted: var(--editorial-muted); /* Design System Custom Token (supermodels-phototypelabs-com) */
  --line: var(--editorial-rule); /* Design System Custom Token (supermodels-phototypelabs-com) */
  --serif: var(--font-editorial); /* Typography / Scale Token (supermodels-phototypelabs-com) */
  --sans: var(--font-sans); /* Typography / Scale Token (supermodels-phototypelabs-com) */
  --headline: var(--font-display); /* Design System Custom Token (supermodels-phototypelabs-com) */
  --font-mono: var(--font-sans); /* Typography / Scale Token (supermodels-phototypelabs-com) */
  --landing-dark: var(--editorial-ink); /* Canvas / Surface Token (supermodels-phototypelabs-com) */
  --landing-on-dark: var(--editorial-paper); /* Canvas / Surface Token (supermodels-phototypelabs-com) */
  --landing-on-dark-muted: #f7f6f2bf; /* Canvas / Surface Token (supermodels-phototypelabs-com) */
  --landing-dark-line: #f7f6f247; /* Canvas / Surface Token (supermodels-phototypelabs-com) */
  --landing-quiet: var(--editorial-paper-quiet); /* Design System Custom Token (supermodels-phototypelabs-com) */
  --landing-heading-size: clamp(2.35rem, 5.2vw, 5.25rem); /* Typography Ink Token (supermodels-phototypelabs-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f7f6f2` — grounded in `var(--studio-category-color)` in `:root`
- **Primary Typography Ink**: `#283a2d` — grounded in `var(--category-tag-bg)` in `:root`
- **Elevated Surface / Card Substrate**: `#57d778` — grounded in `var(--category-tag-ink)` in `:root`
- **Interactive Accent / Highlight**: `#000` — grounded in `var(--site-frame)` in `:root`
- **Secondary / Muted Copy**: `#ecebe7` — grounded in `var(--editorial-ground)` in `:root`
- **Structural Hairline Border**: `#171715` — grounded in `var(--editorial-ink)` in `:root`
- **Variable Token (`--landing-on-dark-muted`)**: `#f7f6f2bf` — grounded in `var(--landing-on-dark-muted)` in `:root`
- **Variable Token (`--landing-dark-line`)**: `#f7f6f247` — grounded in `var(--landing-dark-line)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `10ch` extracted from `supermodels-phototypelabs-com` stylesheet
- **Padding & Gutters**: `.27rem` lateral canvas padding with `.65rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 10ch`, `gap: .65rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `.27rem` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (width<=1000px)`, `@media (width<=550px)`, `@media (width<=900px)`
- **Corner Radii**: `999px`, `50%`, `var(--radius-sm)`, `.7rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Onest`
- **Body Font Stack**: `DM Sans`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--font-display: "Manrope", var(--font-sans)`
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.75rem`, `.65rem`, `2rem`, `1.4rem`, `clamp(7rem,14vw,14rem)`)
- **Body Copy Rule**: CSS variables `--landing-body-size: .9375rem`
- **Metadata & Index Rule**: CSS variables `--font-mono: var(--font-sans)`, `--landing-label-size: .75rem`, `--hero-brand-letter-spacing: 0.02em`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `supermodels-phototypelabs-com` (`SUPERMODELS — Image, Video, Voice & Music, Pay Per Use`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.editorial-header> — `supermodels-phototypelabs-com`)**:
   - DOM & Selectors: Landmark `<header class="editorial-header">` hosting `SUPERMODELS — Image, Video, Voice & ` navigation (`Models · Providers · Pricing · Examples · News`), DOM attributes (`data-landing-brand="SUPERMODELS"`, `data-landing-brand-weight="700"`, `data-landing-brand-spacing="0.02"`, `data-landing-font="Onest"`), and stylesheet rule `webkit-slider-runnable-track { background:0 0;height:.32rem }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.editorial-header> — `supermodels-phototypelabs-com`)` (`supermodels-phototypelabs-com`) adapts across `@media (prefers-reduced-motion:reduce)`, `@media (width<=1000px)`, `@media (width<=550px)`, `@media (width<=900px)` with `cubic-bezier(.2,.8,.2,1)`, `cubic-bezier(.22,.61,.36,1)`, `cubic-bezier(.2,.75,.2,1)` transitions and links `Models · Providers · Pricing · Examples · News`.
2. **Hero Stage & Focal Lead (<section.editorial-hero> — `Your ideas. One creative platform.`)**:
   - DOM & Selectors: Landmark `<section class="editorial-hero">` presenting display lead `Your ideas. One creative platform.` and copy excerpt *"Explore leading models for images, video, voice, music, and text."* over `#f7f6f2` canvas and `#000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#f7f6f2` background with `#000` headline `Your ideas. One creative platform.`.
3. **Primary Showcase & Content Grid (<section.principles-section> — `Pay per use`)**:
   - DOM & Selectors: Landmark `<section class="principles-section platform-overview">` rendering section `Pay per use` with copy *"Pick a model. Type a prompt. Get a result."*, asset references (`favicon.svg`, `favicon.png`, `favicon.ico`, `apple-touch-icon.png`), and grid rule `moz-range-track { background:0 0;height:.32rem }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.principles-section> — `Pay per use`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 10ch`, `gap: .65rem`) on desktop and Single-column vertical stack at `390px` viewport width with `.27rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.editorial-landing> — `Model choice`)**:
   - DOM & Selectors: Landmark `<article class="editorial-landing">` framing `Model choice` and `Batch comparisons` (*"No subscription. Add wallet credit from $10 and see the estimated"*) with `#57d778` surface cards, `#000` accents, and `active::-webkit-slider-thumb { transform:scale(1.24) }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.editorial-landing> — `Model choice`)` uses `999px`, `50%`, `var(--radius-sm)`, `.7rem` radii, `#000` highlights, and assets (favicon.svg, favicon.png, favicon.ico).
5. **Colophon & Global Directory Footer (<footer.creative-footer> — `https://supermodels.phototypelabs.com`)**:
   - DOM & Selectors: Landmark `<footer class="creative-footer">` anchoring `SUPERMODELS — Image, Video, Voic` footer links (`Models · Providers · Pricing · Examples · News`), copy *"Explore about 47 published models from OpenAI, Google, Anthr"*, and `#171715` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.creative-footer> — `https://supermodels.phototypelabs.com`)` aligns to `10ch` extracted from `supermodels-phototypelabs-com` stylesheet with `.27rem` lateral canvas padding with `.65rem` grid gap and attributes (data-landing-brand="SUPERMODELS", data-landing-brand-weight="700", data-landing-brand-spacing="0.02").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Explore leading models for images, video, voice, music, and text. Shape a prompt,..."*
- Copy Excerpt 2: *"Pick a model. Type a prompt. Get a result."*
- Copy Excerpt 3: *"No subscription. Add wallet credit from $10 and see the estimated price before eac..."*
- Copy Excerpt 4: *"Explore about 47 published models from OpenAI, Google, Anthropic, Alibaba, ByteDan..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.2,.8,.2,1)`, `cubic-bezier(.22,.61,.36,1)`, `cubic-bezier(.2,.75,.2,1)`
- **Extracted Stylesheet Rules (`supermodels-phototypelabs-com`)**:
- `webkit-slider-runnable-track { background:0 0;height:.32rem }`
- `moz-range-track { background:0 0;height:.32rem }`
- `active::-webkit-slider-thumb { transform:scale(1.24) }`
- `active::-moz-range-thumb { transform:scale(1.24) }`
- `webkit-slider-thumb { transition:none }`
- **Per-Selector Transition Rules**:
- **Selector `.app-slider-fill[data-v-c750e325]`**: `transition: width .16s cubic-bezier(.2,.8,.2,1)` extracted from `supermodels-phototypelabs-com` stylesheet.
- **Selector `nput[data-v-c750e325]::-webkit-sl...`**: `transition: transform .18s cubic-bezier(.2,.8,.2,1)` extracted from `supermodels-phototypelabs-com` stylesheet.
- **Selector `er-input[data-v-c750e325]::-moz-r...`**: `transition: transform .18s cubic-bezier(.2,.8,.2,1)` extracted from `supermodels-phototypelabs-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.2,.8,.2,1)`)**: Governs interactive state transitions across `<header.editorial-header>` and `<section.principles-section>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `supermodels-phototypelabs-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
