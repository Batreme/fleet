---
title: "UI Prompt Blueprint: yaas-energy-com"
date: 2026-11-23
captured_at: 2026-11-23
target: "yaas-energy-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#0b0a09` canvas, `#ffffff` ink, `#e53a6b` accent)"
---

# UI Design System & Master Generation Blueprint: yaas-energy-com

> **YAAS Energy — Zero-Sugar Energy Drink in 5 Bold Flavors** (https://yaas-energy.com/) — YAAS — zero-sugar, 5-calorie energy drink in 5 bold flavors: Citrus Lemon, Blueberry Rush, Wild Strawberry, Solar Orange, Green Apple. No...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **YAAS Energy — Zero-Sugar Energy Drink in 5 Bold Flavors** (`https://yaas-energy.com/`). YAAS — zero-sugar, 5-calorie energy drink in 5 bold flavors: Citrus Lemon, Blueberry Rush, Wild Strawberry, Solar Orange, Green Apple. No...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#0b0a09` canvas, `#ffffff` ink, `#e53a6b` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#0b0a09` (live computed `html` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#e53a6b` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Helvetica Neue` for display copy (`YAAS. That feeling when everything j`) with `Helvetica Neue` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 8px`, padding `var(--detail-pad)`) with `cubic-bezier(.22,1,.36,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport).
- **Canvas Lateral Padding & Spacing**: `var(--detail-pad)` lateral canvas padding with `8px` grid gap.
- **Border Radius Scale**: `100px`, `50%`, `18px`, `20px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 8px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--detail-pad)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width: 1199px)`, `@media (min-width: 960px) and (max-width: 1199px)`, `@media (min-width: 1200px)`, `@media (min-width: 640px) and (max-width: 959px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0b0a09` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#212121` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#e53a6b` | `.screen2-h2-accent { color: #e53a6b }` |
| **Secondary / Muted Copy** | `#212121` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#212121` | live computed `button` `border-color` (`computed_styles.json`) |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--asset-bg-texture` | `url('/textures/bg-texture.webp')` | Canvas / Surface Token |
| `--font-display` | `"Soledago", "Arial Narrow", system-ui, -apple-system, sans-serif` | Typography / Scale Token |
| `--font-body` | `"Helvetica Neue", Arial, system-ui, -apple-system, sans-serif` | Typography / Scale Token |
| `--font-beiruti` | `"Bounded", "Helvetica Neue", Arial, system-ui, -apple-system, sans-serif` | Typography / Scale Token |
| `--ui-scale` | `1` | Design System Custom Token |
| `--ink` | `#ffffff` | Typography Ink Token |
| `--ink-soft` | `rgba(255, 255, 255, .85)` | Typography Ink Token |
| `--ink-on-light` | `#212121` | Canvas / Surface Token |
| `--ink-on-light-soft` | `rgba(33, 33, 33, .72)` | Canvas / Surface Token |
| `--block-gap` | `calc(120px * var(--ui-scale))` | Layout / Spatial Grid Token |
| `--heading-gap` | `50px` | Typography Ink Token |
| `--block-heading` | `clamp(30px, 4.17vw, calc(80px * var(--ui-scale)))` | Typography Ink Token |
| `--text-body` | `calc(16px * var(--ui-scale))` | Typography Ink Token |
| `--text-body-sm` | `calc(14px * var(--ui-scale))` | Typography Ink Token |
| `--content-gutter` | `30px` | Layout / Spatial Grid Token |
| `--content-inline` | `var(--content-gutter)` | Design System Custom Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Helvetica Neue`.
- **Primary Body Stack**: `Helvetica Neue`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 32px`, `line-height: normal`, `font-weight: 700`); CSS variables `--font-display: "Soledago", "Arial Narrow", system-ui, -apple-system, sans-serif`.
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 81.9574px`, `line-height: 81.9574px`, `font-weight: 400`); CSS variables `--h2g: 0`.
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--font-body: "Helvetica Neue", Arial, system-ui, -apple-system, sans-serif`, `--text-body: calc(16px * var(--ui-scale))`, `--text-body-sm: calc(14px * var(--ui-scale))`.
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--caption-top: 625px`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.22,1,.36,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.background-layer`**: `transition: background-color .9s ease` extracted from `yaas-energy-com` stylesheet.
- **Selector `.center-glow`**: `transition: opacity .6s ease` extracted from `yaas-energy-com` stylesheet.
- **Selector `.slider-screen`**: `transition: opacity .5s ease` extracted from `yaas-energy-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,1,.36,1)`)**: Governs interactive state transitions across `<nav.hero-nav>` and `<section.screen2>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — YAAS Energy — Zero-Sugar Energy Drink in 5 │
│ ====================================================================== │
│ [ <nav.hero-nav> (1240x34px)          | Flavors · About us · FAQ · C ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.intro-wrap> (w=1440px)                        | │
│ | H1: YAAS. That feeling when everything just hits diff...           | │
│ | Substrate: #0b0a09 | Ink: #ffffff | Accent: #e53a6b                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.screen2>) max-w: 1440px                    | │
│ | +------------------------------+  +------------------------------+ | │
│ | | 5 Flavors. 1 Energy.         |  | Zero-sugar energy for people | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.screen2-arc>) — This isn't about hypi      | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer>) | https://yaas-energy.com/             │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 8px)        │
│ ====================================================================== │
│ [ HEADER BAR (<nav.hero-nav>          ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.intro-wrap>) — 390px Vertical Lead            | │
│ | H1: YAAS. That feeling when everything just hits diff...           | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.screen2>) — 1-Col Stack                   | │
│ | [ Item 1: 5 Flavors. 1 Energy.                                   ] | │
│ | [ Item 2: Zero-sugar energy for people who move at their o       ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.screen2-arc>) — 1-Col (This isn't about h)  | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer>) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.hero-nav> — `yaas-energy-com`)**:
   - Landmark `<nav class="hero-nav">` (`1240x34px`) hosting `YAAS Energy — Zero-Sugar Energy Drin` navigation (`Flavors · About us · FAQ · Contacts`), DOM attributes (`data-seo="1"`, `data-seo="1"`, `data-seo="1"`, `data-seo="1"`), and stylesheet rule `root { --block-heading: clamp(30px, 4.17vw, calc(80px * var(--ui-scale))) }`.
2. **Hero Stage & Focal Lead (<section.intro-wrap> — `YAAS. That feeling when everything`)**:
   - Landmark `<section class="intro-wrap">` presenting display lead `YAAS. That feeling when everything just hits diff...` and copy excerpt *"Yes, we use cookies. Sugar-free."* over `#0b0a09` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.screen2> — `5 Flavors. 1 Energy.`)**:
   - Landmark `<section class="screen2 is-arc-running">` rendering section `5 Flavors. 1 Energy.` with copy *"Zero-sugar energy for people who move at their own speed. Flavor "*, asset references (`favicon.svg`, `favicon-32.png`, `favicon-16.png`, `apple-touch-icon.png`), and grid rule `html { background:0b0a09 }`.
4. **Interactive Detail & Feature Matrix (<section.screen2-arc> — `Zero-sugar energy for people who m`)**:
   - Landmark `<section class="screen2-arc">` framing `Zero-sugar energy for people who move at their o` and `This isn't about hyping you up. It's about stayi` (*"This isn't about hyping you up. It's about staying locked in to y"*) with `#212121` surface cards, `#e53a6b` accents, and `button { font-family:inherit;color:inherit;background:none;border:none;cursor:poi... }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://yaas-energy.com/`)**:
   - Landmark `<footer class="site-footer is-reveal">` anchoring `YAAS Energy — Zero-Sugar Energy ` footer links (`Flavors · About us · FAQ · Contacts`), copy *"When the night's just getting started and your battery isn't"*, and `#212121` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: yaas-energy-com (YAAS Energy — Zero-Sugar Energy Drink in 5 Bold Flavors)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `yaas-energy-com` (**YAAS Energy — Zero-Sugar Energy Drink in 5 Bold Flavors** — `https://yaas-energy.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#0b0a09` canvas, `#ffffff` ink, `#e53a6b` accent).
- **Identity & Domain Context**: YAAS — zero-sugar, 5-calorie energy drink in 5 bold flavors: Citrus Lemon, Blueberry Rush, Wild Strawberry, Solar Orange, Green Apple. No...
- **Primary Substrate**: `#0b0a09` (live computed `html` `background-color` (`computed_styles.json`)), **Primary Ink**: `#ffffff`, **Accent / Highlight**: `#e53a6b`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#0b0a09` (live computed `html` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#e53a6b` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Helvetica Neue` for display copy (`YAAS. That feeling when everything j`) with `Helvetica Neue` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 8px`, padding `var(--detail-pad)`) with `cubic-bezier(.22,1,.36,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `yaas-energy-com` in your global stylesheet:

:root {
  /* YAAS Energy — Zero-Sugar Energy Drink in 5 Bold Flavors (yaas-energy-com) — Live-Grounded CSS Variables */
  --asset-bg-texture: url('/textures/bg-texture.webp'); /* Canvas / Surface Token (yaas-energy-com) */
  --font-display: "Soledago", "Arial Narrow", system-ui, -apple-system, sans-serif; /* Typography / Scale Token (yaas-energy-com) */
  --font-body: "Helvetica Neue", Arial, system-ui, -apple-system, sans-serif; /* Typography / Scale Token (yaas-energy-com) */
  --font-beiruti: "Bounded", "Helvetica Neue", Arial, system-ui, -apple-system, sans-serif; /* Typography / Scale Token (yaas-energy-com) */
  --ui-scale: 1; /* Design System Custom Token (yaas-energy-com) */
  --ink: #ffffff; /* Typography Ink Token (yaas-energy-com) */
  --ink-soft: rgba(255, 255, 255, .85); /* Typography Ink Token (yaas-energy-com) */
  --ink-on-light: #212121; /* Canvas / Surface Token (yaas-energy-com) */
  --ink-on-light-soft: rgba(33, 33, 33, .72); /* Canvas / Surface Token (yaas-energy-com) */
  --block-gap: calc(120px * var(--ui-scale)); /* Layout / Spatial Grid Token (yaas-energy-com) */
  --heading-gap: 50px; /* Typography Ink Token (yaas-energy-com) */
  --block-heading: clamp(30px, 4.17vw, calc(80px * var(--ui-scale))); /* Typography Ink Token (yaas-energy-com) */
  --text-body: calc(16px * var(--ui-scale)); /* Typography Ink Token (yaas-energy-com) */
  --text-body-sm: calc(14px * var(--ui-scale)); /* Typography Ink Token (yaas-energy-com) */
  --content-gutter: 30px; /* Layout / Spatial Grid Token (yaas-energy-com) */
  --content-inline: var(--content-gutter); /* Design System Custom Token (yaas-energy-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#0b0a09` — grounded in live computed `html` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#ffffff` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#212121` — grounded in live computed `button` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#e53a6b` — grounded in `.screen2-h2-accent { color: #e53a6b }`
- **Secondary / Muted Copy**: `#212121` — grounded in live computed `p` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#212121` — grounded in live computed `button` `border-color` (`computed_styles.json`)

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport)
- **Padding & Gutters**: `var(--detail-pad)` lateral canvas padding with `8px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 8px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--detail-pad)` horizontal padding
- **Media Queries**: `@media (max-width: 1199px)`, `@media (min-width: 960px) and (max-width: 1199px)`, `@media (min-width: 1200px)`, `@media (min-width: 640px) and (max-width: 959px)`
- **Corner Radii**: `100px`, `50%`, `18px`, `20px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Helvetica Neue`
- **Body Font Stack**: `Helvetica Neue`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: live computed `h1` (`font-size: 32px`, `line-height: normal`, `font-weight: 700`); CSS variables `--font-display: "Soledago", "Arial Narrow", system-ui, -apple-system, sans-serif`
- **H2 Section Rule**: live computed `h2` (`font-size: 81.9574px`, `line-height: 81.9574px`, `font-weight: 400`); CSS variables `--h2g: 0`
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--font-body: "Helvetica Neue", Arial, system-ui, -apple-system, sans-serif`, `--text-body: calc(16px * var(--ui-scale))`, `--text-body-sm: calc(14px * var(--ui-scale))`
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--caption-top: 625px`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `yaas-energy-com` (`YAAS Energy — Zero-Sugar Energy Drink in 5 Bold Flavors`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.hero-nav> — `yaas-energy-com`)**:
   - DOM & Selectors: Landmark `<nav class="hero-nav">` (`1240x34px`) hosting `YAAS Energy — Zero-Sugar Energy Drin` navigation (`Flavors · About us · FAQ · Contacts`), DOM attributes (`data-seo="1"`, `data-seo="1"`, `data-seo="1"`, `data-seo="1"`), and stylesheet rule `root { --block-heading: clamp(30px, 4.17vw, calc(80px * var(--ui-scale))) }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.hero-nav> — `yaas-energy-com`)` (`yaas-energy-com`) adapts across `@media (max-width: 1199px)`, `@media (min-width: 960px) and (max-width: 1199px)`, `@media (min-width: 1200px)`, `@media (min-width: 640px) and (max-width: 959px)` with `cubic-bezier(.22,1,.36,1)` transitions and links `Flavors · About us · FAQ · Contacts`.
2. **Hero Stage & Focal Lead (<section.intro-wrap> — `YAAS. That feeling when everything`)**:
   - DOM & Selectors: Landmark `<section class="intro-wrap">` presenting display lead `YAAS. That feeling when everything just hits diff...` and copy excerpt *"Yes, we use cookies. Sugar-free."* over `#0b0a09` canvas and `#ffffff` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#0b0a09` background with `#ffffff` headline `YAAS. That feeling when everything just hits diff...`.
3. **Primary Showcase & Content Grid (<section.screen2> — `5 Flavors. 1 Energy.`)**:
   - DOM & Selectors: Landmark `<section class="screen2 is-arc-running">` rendering section `5 Flavors. 1 Energy.` with copy *"Zero-sugar energy for people who move at their own speed. Flavor "*, asset references (`favicon.svg`, `favicon-32.png`, `favicon-16.png`, `apple-touch-icon.png`), and grid rule `html { background:0b0a09 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.screen2> — `5 Flavors. 1 Energy.`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 8px`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--detail-pad)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.screen2-arc> — `Zero-sugar energy for people who m`)**:
   - DOM & Selectors: Landmark `<section class="screen2-arc">` framing `Zero-sugar energy for people who move at their o` and `This isn't about hyping you up. It's about stayi` (*"This isn't about hyping you up. It's about staying locked in to y"*) with `#212121` surface cards, `#e53a6b` accents, and `button { font-family:inherit;color:inherit;background:none;border:none;cursor:poi... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.screen2-arc> — `Zero-sugar energy for people who m`)` uses `100px`, `50%`, `18px`, `20px` radii, `#e53a6b` highlights, and assets (favicon.svg, favicon-32.png, favicon-16.png).
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://yaas-energy.com/`)**:
   - DOM & Selectors: Landmark `<footer class="site-footer is-reveal">` anchoring `YAAS Energy — Zero-Sugar Energy ` footer links (`Flavors · About us · FAQ · Contacts`), copy *"When the night's just getting started and your battery isn't"*, and `#212121` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.site-footer> — `https://yaas-energy.com/`)` aligns to `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport) with `var(--detail-pad)` lateral canvas padding with `8px` grid gap and attributes (data-seo="1", data-seo="1", data-seo="1").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Yes, we use cookies. Sugar-free."*
- Copy Excerpt 2: *"Zero-sugar energy for people who move at their own speed. Flavor maxed out, sugar..."*
- Copy Excerpt 3: *"This isn't about hyping you up. It's about staying locked in to your own thing."*
- Copy Excerpt 4: *"When the night's just getting started and your battery isn't"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.22,1,.36,1)`
- **Extracted Stylesheet Rules (`yaas-energy-com`)**:
- `root { --block-heading: clamp(30px, 4.17vw, calc(80px * var(--ui-scale))) }`
- `html { background:0b0a09 }`
- `button { font-family:inherit;color:inherit;background:none;border:none;cursor:poi... }`
- `.intro-wrap { position:relative;height:300vh }`
- `.intro-pin { position:sticky;top:0;height:100vh;overflow:hidden;--h2g: 0 }`
- **Per-Selector Transition Rules**:
- **Selector `.background-layer`**: `transition: background-color .9s ease` extracted from `yaas-energy-com` stylesheet.
- **Selector `.center-glow`**: `transition: opacity .6s ease` extracted from `yaas-energy-com` stylesheet.
- **Selector `.slider-screen`**: `transition: opacity .5s ease` extracted from `yaas-energy-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,1,.36,1)`)**: Governs interactive state transitions across `<nav.hero-nav>` and `<section.screen2>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `yaas-energy-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
