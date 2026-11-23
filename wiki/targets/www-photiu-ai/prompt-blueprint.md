---
title: "UI Prompt Blueprint: www-photiu-ai"
date: 2026-11-23
captured_at: 2026-11-23
target: "www-photiu-ai"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#9ca3af` accent)"
---

# UI Design System & Master Generation Blueprint: www-photiu-ai

> **Remove Background, Upscale & Erase Objects – Photiu.ai** (https://www.photiu.ai) — Discover Photiu.ai's AI tools: remove backgrounds, upscale images, and erase unwanted objects. Achieve stunning photo edits online quickl...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Remove Background, Upscale & Erase Objects – Photiu.ai** (`https://www.photiu.ai`). Discover Photiu.ai's AI tools: remove backgrounds, upscale images, and erase unwanted objects. Achieve stunning photo edits online quickl...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#9ca3af` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `browser-default` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#9ca3af` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Segoe UI` for display copy (`Remove background`) with `Segoe UI` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1200px` container bounds (`gap: 1rem`, padding `.25rem`) with `cubic-bezier(.4,0,.2,1)` easing.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1200px` (measured widest bounded `<section>` landmark width on `1440px` desktop).
- **Canvas Lateral Padding & Spacing**: `.25rem` lateral canvas padding with `1rem` grid gap.
- **Border Radius Scale**: `.5rem`, `8px`, `.25rem`, `1rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1200px`, `gap: 1rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `.25rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:640px)`, `@media (min-width:768px)`, `@media (min-width:1024px)`, `@media (min-width:1280px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `browser-default` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#eeeeff` | `.homebg { background: #eeeeff }` |
| **Interactive Accent / Highlight** | `#9ca3af` | `textarea::-moz-placeholder { color: #9ca3af }` |
| **Secondary / Muted Copy** | `#626262` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#c9c9fc` | `30 { border-color: #c9c9fc }` |
| **Variable Token (`--board-black-color`)** | `#f8f9f9` | `var(--board-black-color)` in `:root` |
| **Variable Token (`--termly-theme-button-background-color`)** | `#003afa` | `var(--termly-theme-button-background-color)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--container-width` | `1200px` | Layout / Spatial Grid Token |
| `--header-h` | `80px` | Layout / Spatial Grid Token |
| `--header-h-sm` | `60px` | Layout / Spatial Grid Token |
| `--footer-h` | `200px` | Dimension / Scale Token |
| `--board-black-color` | `#f8f9f9` | Canvas / Surface Token |
| `--board-white-color` | `transparent` | Canvas / Surface Token |
| `--termly-prompt-padding` | `2.5em` | Layout / Spatial Grid Token |
| `--termly-theme-background-color` | `#ffffff` | Canvas / Surface Token |
| `--termly-theme-button-background-color` | `var(--termly-override-button-background-color, #003afa)` | Canvas / Surface Token |
| `--termly-theme-button-text-color` | `var(--termly-override-button-text-color, #ffffff)` | Typography Ink Token |
| `--termly-theme-color` | `#000000` | Brand / Palette Token |
| `--termly-theme-font-family` | `Roboto, "Open Sans", Arial, Helvetica` | Brand / Palette Token |
| `--termly-theme-font-size` | `12px` | Brand / Palette Token |
| `--termly-z-index` | `var(--termly-override-z-index, 999999)` | Elevation / Border Token |
| `--www-photiu-ai-bg` | `#ffffff` | Canvas Substrate (from live computed `browser-default` `background-color` (`computed_styles.json`)) |
| `--www-photiu-ai-ink` | `#000000` | Primary Typography Ink (computed-derived) |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Segoe UI`.
- **Primary Body Stack**: `Segoe UI`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 48px`, `line-height: 48px`, `font-weight: 700`); rule `h1` (`font-size: 2.25rem`, `line-height: 2.5rem`, `font-weight: 700`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 30px`, `line-height: 50px`, `font-weight: 700`); rule `h2` (`font-size: 1.875rem`, `line-height: 2.25rem`, `font-weight: 700`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 600`); rule `p` (`line-height: 1.625`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 600`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(0,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.main-button`**: `transition: cubic-bezier(.4,0,.2,1)` extracted from `www-photiu-ai` stylesheet.
- **Selector `.transition`**: `transition: cubic-bezier(.4,0,.2,1)` extracted from `www-photiu-ai` stylesheet.
- **Selector `.transition-\[color\2c background...`**: `transition: cubic-bezier(.4,0,.2,1)` extracted from `www-photiu-ai` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<nav.flex-1>` and `<section.w-full:nth(2)>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.w-full>` and `<section.w-full:nth(2)>` interactive targets.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Remove Background, Upscale & Erase Objects │
│ ====================================================================== │
│ [ <nav.flex-1> (1024x36px)            | AI Photo Editor · Image Gene ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.w-full> (w=1440px)                            | │
│ | H1: Remove background                                              | │
│ | Substrate: #ffffff | Ink: #000000 | Accent: #9ca3af                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.w-full:nth(2)>) max-w: 1200px              | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Remove backgrounds instantly |  | HD Background Removal        | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.w-full:nth(3)>) — Erase Freely, Cut Per    | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.flex>       ) | https://www.photiu.ai                │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 1rem)       │
│ ====================================================================== │
│ [ HEADER BAR (<nav.flex-1>            ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.w-full>) — 390px Vertical Lead                | │
│ | H1: Remove background                                              | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.w-full:nth(2)) — 1-Col Stack              | │
│ | [ Item 1: Remove backgrounds instantly with just one click!      ] | │
│ | [ Item 2: HD Background Removal                                  ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.w-full:nth(3)>) — 1-Col (Erase Freely, Cut )  │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.flex>       ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.flex-1> — `www-photiu-ai`)**:
   - Landmark `<nav class="flex-1 hidden">` (`1024x36px`) hosting `Remove Background, Upscale & Erase O` navigation (`AI Photo Editor · Image Generator · Image Upscale · Remove Background · Magic Eraser`), DOM attributes (`data-categories="essential"`, `data-has-derived-categories="1"`, `data-precedence="next"`, `data-termly-part="consent-banner"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid e5e7eb }`.
2. **Hero Stage & Focal Lead (<section.w-full> — `Remove background`)**:
   - Landmark `<section class="w-full">` presenting display lead `Remove background` and copy excerpt *"Photiu.ai's advanced AI technology ensures precise background rem"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.w-full:nth(2)> — `Remove backgrounds instantly with `)**:
   - Landmark `<section class="w-full">` rendering section `Remove backgrounds instantly with just one click!` with copy *"AI Photo Editor Image Generator Image Upscale Remove Background M"*, asset references (`gtm.js`, `eTI4g9fAtUixpHto8YooHCfeUPdUHEz0P...`, `3b524ee0-b2d0-46e4-acf0-3df4c2d8edb5`, `www.googletagmanager.com`), and grid rule `body { margin:0;line-height:inherit }`.
4. **Interactive Detail & Feature Matrix (<section.w-full:nth(3)> — `HD Background Removal`)**:
   - Landmark `<section class="w-full">` framing `HD Background Removal` and `Erase Freely, Cut Perfectly` (*"Resize images to ideal dimensions"*) with `#eeeeff` surface cards, `#9ca3af` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.flex> — `https://www.photiu.ai`)**:
   - Landmark `<footer class="flex w-full">` anchoring `Remove Background, Upscale & Era` footer links (`AI Photo Editor · Image Generator · Image Upscale · Remove Background · Magic Eraser`), copy *"Make your images smaller"*, and `#c9c9fc` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-photiu-ai (Remove Background, Upscale & Erase Objects – Photiu.ai)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-photiu-ai` (**Remove Background, Upscale & Erase Objects – Photiu.ai** — `https://www.photiu.ai`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#9ca3af` accent).
- **Identity & Domain Context**: Discover Photiu.ai's AI tools: remove backgrounds, upscale images, and erase unwanted objects. Achieve stunning photo edits online quickl...
- **Primary Substrate**: `#ffffff` (live computed `browser-default` `background-color` (`computed_styles.json`)), **Primary Ink**: `#000000`, **Accent / Highlight**: `#9ca3af`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `browser-default` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#9ca3af` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Segoe UI` for display copy (`Remove background`) with `Segoe UI` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1200px` container bounds (`gap: 1rem`, padding `.25rem`) with `cubic-bezier(.4,0,.2,1)` easing.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-photiu-ai` in your global stylesheet:

:root {
  /* Remove Background, Upscale & Erase Objects – Photiu.ai (www-photiu-ai) — Live-Grounded CSS Variables */
  --container-width: 1200px; /* Layout / Spatial Grid Token (www-photiu-ai) */
  --header-h: 80px; /* Layout / Spatial Grid Token (www-photiu-ai) */
  --header-h-sm: 60px; /* Layout / Spatial Grid Token (www-photiu-ai) */
  --footer-h: 200px; /* Dimension / Scale Token (www-photiu-ai) */
  --board-black-color: #f8f9f9; /* Canvas / Surface Token (www-photiu-ai) */
  --board-white-color: transparent; /* Canvas / Surface Token (www-photiu-ai) */
  --termly-prompt-padding: 2.5em; /* Layout / Spatial Grid Token (www-photiu-ai) */
  --termly-theme-background-color: #ffffff; /* Canvas / Surface Token (www-photiu-ai) */
  --termly-theme-button-background-color: var(--termly-override-button-background-color, #003afa); /* Canvas / Surface Token (www-photiu-ai) */
  --termly-theme-button-text-color: var(--termly-override-button-text-color, #ffffff); /* Typography Ink Token (www-photiu-ai) */
  --termly-theme-color: #000000; /* Brand / Palette Token (www-photiu-ai) */
  --termly-theme-font-family: Roboto, "Open Sans", Arial, Helvetica; /* Brand / Palette Token (www-photiu-ai) */
  --termly-theme-font-size: 12px; /* Brand / Palette Token (www-photiu-ai) */
  --termly-z-index: var(--termly-override-z-index, 999999); /* Elevation / Border Token (www-photiu-ai) */
  --www-photiu-ai-bg: #ffffff; /* Canvas Substrate (from live computed `browser-default` `background-color` (`computed_styles.json`)) (www-photiu-ai) */
  --www-photiu-ai-ink: #000000; /* Primary Typography Ink (computed-derived) (www-photiu-ai) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `browser-default` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#000000` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#eeeeff` — grounded in `.homebg { background: #eeeeff }`
- **Interactive Accent / Highlight**: `#9ca3af` — grounded in `textarea::-moz-placeholder { color: #9ca3af }`
- **Secondary / Muted Copy**: `#626262` — grounded in live computed `p` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#c9c9fc` — grounded in `30 { border-color: #c9c9fc }`
- **Variable Token (`--board-black-color`)**: `#f8f9f9` — grounded in `var(--board-black-color)` in `:root`
- **Variable Token (`--termly-theme-button-background-color`)**: `#003afa` — grounded in `var(--termly-theme-button-background-color)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1200px` (measured widest bounded `<section>` landmark width on `1440px` desktop)
- **Padding & Gutters**: `.25rem` lateral canvas padding with `1rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1200px`, `gap: 1rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `.25rem` horizontal padding
- **Media Queries**: `@media (min-width:640px)`, `@media (min-width:768px)`, `@media (min-width:1024px)`, `@media (min-width:1280px)`
- **Corner Radii**: `.5rem`, `8px`, `.25rem`, `1rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Segoe UI`
- **Body Font Stack**: `Segoe UI`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: live computed `h1` (`font-size: 48px`, `line-height: 48px`, `font-weight: 700`); rule `h1` (`font-size: 2.25rem`, `line-height: 2.5rem`, `font-weight: 700`)
- **H2 Section Rule**: live computed `h2` (`font-size: 30px`, `line-height: 50px`, `font-weight: 700`); rule `h2` (`font-size: 1.875rem`, `line-height: 2.25rem`, `font-weight: 700`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 600`); rule `p` (`line-height: 1.625`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 600`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-photiu-ai` (`Remove Background, Upscale & Erase Objects – Photiu.ai`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.flex-1> — `www-photiu-ai`)**:
   - DOM & Selectors: Landmark `<nav class="flex-1 hidden">` (`1024x36px`) hosting `Remove Background, Upscale & Erase O` navigation (`AI Photo Editor · Image Generator · Image Upscale · Remove Background · Magic Eraser`), DOM attributes (`data-categories="essential"`, `data-has-derived-categories="1"`, `data-precedence="next"`, `data-termly-part="consent-banner"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid e5e7eb }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.flex-1> — `www-photiu-ai`)` (`www-photiu-ai`) adapts across `@media (min-width:640px)`, `@media (min-width:768px)`, `@media (min-width:1024px)`, `@media (min-width:1280px)` with `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(0,0,.2,1)` transitions and links `AI Photo Editor · Image Generator · Image Upscale · Remove Background · Magic Eraser`.
2. **Hero Stage & Focal Lead (<section.w-full> — `Remove background`)**:
   - DOM & Selectors: Landmark `<section class="w-full">` presenting display lead `Remove background` and copy excerpt *"Photiu.ai's advanced AI technology ensures precise background rem"* over `#ffffff` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#ffffff` background with `#000000` headline `Remove background`.
3. **Primary Showcase & Content Grid (<section.w-full:nth(2)> — `Remove backgrounds instantly with `)**:
   - DOM & Selectors: Landmark `<section class="w-full">` rendering section `Remove backgrounds instantly with just one click!` with copy *"AI Photo Editor Image Generator Image Upscale Remove Background M"*, asset references (`gtm.js`, `eTI4g9fAtUixpHto8YooHCfeUPdUHEz0P...`, `3b524ee0-b2d0-46e4-acf0-3df4c2d8edb5`, `www.googletagmanager.com`), and grid rule `body { margin:0;line-height:inherit }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.w-full:nth(2)> — `Remove backgrounds instantly with `)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1200px`, `gap: 1rem`) on desktop and Single-column vertical stack at `390px` viewport width with `.25rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.w-full:nth(3)> — `HD Background Removal`)**:
   - DOM & Selectors: Landmark `<section class="w-full">` framing `HD Background Removal` and `Erase Freely, Cut Perfectly` (*"Resize images to ideal dimensions"*) with `#eeeeff` surface cards, `#9ca3af` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.w-full:nth(3)> — `HD Background Removal`)` uses `.5rem`, `8px`, `.25rem`, `1rem` radii, `#9ca3af` highlights, and assets (gtm.js, eTI4g9fAtUixpHto8YooHCfeUPdUHEz0P..., 3b524ee0-b2d0-46e4-acf0-3df4c2d8edb5).
5. **Colophon & Global Directory Footer (<footer.flex> — `https://www.photiu.ai`)**:
   - DOM & Selectors: Landmark `<footer class="flex w-full">` anchoring `Remove Background, Upscale & Era` footer links (`AI Photo Editor · Image Generator · Image Upscale · Remove Background · Magic Eraser`), copy *"Make your images smaller"*, and `#c9c9fc` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.flex> — `https://www.photiu.ai`)` aligns to `1200px` (measured widest bounded `<section>` landmark width on `1440px` desktop) with `.25rem` lateral canvas padding with `1rem` grid gap and attributes (data-categories="essential", data-has-derived-categories="1", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Photiu.ai's advanced AI technology ensures precise background removal in seconds,..."*
- Copy Excerpt 2: *"AI Photo Editor Image Generator Image Upscale Remove Background Magic Eraser Quick..."*
- Copy Excerpt 3: *"Resize images to ideal dimensions"*
- Copy Excerpt 4: *"Make your images smaller"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(0,0,.2,1)`
- **Extracted Stylesheet Rules (`www-photiu-ai`)**:
- `before { box-sizing:border-box;border:0 solid e5e7eb }`
- `body { margin:0;line-height:inherit }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- `sup { font-size:75%;line-height:0;position:relative;vertical-align:baseline }`
- **Per-Selector Transition Rules**:
- **Selector `.main-button`**: `transition: cubic-bezier(.4,0,.2,1)` extracted from `www-photiu-ai` stylesheet.
- **Selector `.transition`**: `transition: cubic-bezier(.4,0,.2,1)` extracted from `www-photiu-ai` stylesheet.
- **Selector `.transition-\[color\2c background...`**: `transition: cubic-bezier(.4,0,.2,1)` extracted from `www-photiu-ai` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<nav.flex-1>` and `<section.w-full:nth(2)>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.w-full>` and `<section.w-full:nth(2)>` interactive targets.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-photiu-ai`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
