---
title: "UI Prompt Blueprint: www-casamomo-at"
date: 2026-11-23
captured_at: 2026-11-23
target: "www-casamomo-at"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#0e1201` canvas, `#fff0ca` ink, `#ffffff` accent)"
---

# UI Design System & Master Generation Blueprint: www-casamomo-at

> **Casa Momo • Boutique Apartments in Graz** (https://www.casamomo.at/) — Personally designed apartments for short and longer stays, between quiet minimalism and warm coziness. Discover boutique, garden, loft an...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Casa Momo • Boutique Apartments in Graz** (`https://www.casamomo.at/`). Personally designed apartments for short and longer stays, between quiet minimalism and warm coziness. Discover boutique, garden, loft an...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#0e1201` canvas, `#fff0ca` ink, `#ffffff` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#0e1201` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#fff0ca` primary typography and `#ffffff` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Inter` for display copy (`Casa Momo – Designer Apartments in G`) with `Lay Grotesk Regular` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1344px` container bounds (`gap: 12px`, padding `256px`) with `cubic-bezier(0.66,0,0,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1344px` (measured widest bounded `<section>` landmark width on `1440px` desktop).
- **Canvas Lateral Padding & Spacing**: `256px` lateral canvas padding with `12px` grid gap.
- **Border Radius Scale**: `2px`, `64px`, `8px`, `15px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1344px`, `gap: 12px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `256px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:809px) and (min-width:0)`, `@media (max-width:809.98px)`, `@media (min-width:810px) and (max-width:1599.98px)`, `@media (max-width: 809.98px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0e1201` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#fff0ca` | live computed `p` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#964317` | live computed `footer` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ffffff` | `#__framer-editorbar-button { color: #ffffff }` |
| **Secondary / Muted Copy** | `#000000` | live computed `nav` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#000000` | hairline divider derived from live computed `nav` `color` (`computed_styles.json`) |
| **Variable Token (`--token-11878163-64ae-441d-8311-9e9d670023d9`)** | `#ffe3d4` | `var(--token-11878163-64ae-441d-8311-9e9d670023d9)` in `:root` |
| **Variable Token (`--token-419394a1-565d-4952-8ba3-b4f1eb92339c`)** | `#050505` | `var(--token-419394a1-565d-4952-8ba3-b4f1eb92339c)` in `:root` |
| **Variable Token (`--token-bf966309-2582-4df8-98f4-f091ce81e703`)** | `#131415` | `var(--token-bf966309-2582-4df8-98f4-f091ce81e703)` in `:root` |
| **Variable Token (`--token-86299043-b8f8-4618-9585-4835ac76e9b7`)** | `#bc6f45` | `var(--token-86299043-b8f8-4618-9585-4835ac76e9b7)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--casa-p1-size` | `calc(var(--casa-page-w, 100vw) * 0.020000)` | Layout / Spatial Grid Token |
| `--casa-p1-lh` | `1.2em` | Dimension / Scale Token |
| `--casa-p1-ls` | `-0.2px` | Dimension / Scale Token |
| `--token-8ecd7124-9686-4bd8-bf72-4f81314652d2` | `#fff0ca` | Color / Atmospheric Token |
| `--token-a0f3f7f0-2bee-4607-a7b2-647fda358cb3` | `#0e1201` | Color / Atmospheric Token |
| `--token-11878163-64ae-441d-8311-9e9d670023d9` | `#ffe3d4` | Color / Atmospheric Token |
| `--token-419394a1-565d-4952-8ba3-b4f1eb92339c` | `#050505` | Color / Atmospheric Token |
| `--token-bf966309-2582-4df8-98f4-f091ce81e703` | `#131415` | Color / Atmospheric Token |
| `--token-86299043-b8f8-4618-9585-4835ac76e9b7` | `#bc6f45` | Color / Atmospheric Token |
| `--token-0da0c5a6-8028-40b0-8315-7bce946c6731` | `#131415` | Color / Atmospheric Token |
| `--token-20608b9f-0145-4a1e-b971-ee948ebbb015` | `#fff` | Color / Atmospheric Token |
| `--token-e00ea664-9c78-44de-bf9c-6839d671d9c2` | `#050505` | Color / Atmospheric Token |
| `--token-31f69385-9489-4b68-a801-60367d4b1ac3` | `#0e1201` | Color / Atmospheric Token |
| `--text-decoration-skip-ink` | `var(--framer-text-decoration-skip-ink)` | Typography Ink Token |
| `--text-underline-offset` | `var(--framer-text-decoration-offset)` | Typography Ink Token |
| `--font-family` | `var(--framer-font-family)` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Inter`.
- **Primary Body Stack**: `Lay Grotesk Regular`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 16px`, `line-height: 19.2px`, `font-weight: 400`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 72px`, `line-height: 72px`, `font-weight: 400`, `letter-spacing: -0.9px`).
- **Body Copy**: live computed `body` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 13px`, `line-height: 100%`, `letter-spacing: 0px`, `font-weight: 400`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); CSS variables `--letter-spacing: var(--framer-letter-spacing)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.66,0,0,1)`, `cubic-bezier(0.45,0,0.55,1)`, `cubic-bezier(0.52,0,0,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `media (prefers-reduced-motion: re...`**: `transition: .01ms!important` extracted from `www-casamomo-at` stylesheet.
- **Selector `#__framer-editorbar-label`**: `transition: opacity 0.4s ease-out` extracted from `www-casamomo-at` stylesheet.
- **Selector `data-framer-name="Menu Overlay"]`**: `transition: visibility 0s linear 0.6s,display 0s linear 0.6s` extracted from `www-casamomo-at` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.66,0,0,1)`)**: Governs interactive state transitions across `<header.framer-bg7hsc>` and `<section.framer-chahzh>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline, Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Casa Momo • Boutique Apartments in Graz    │
│ ====================================================================== │
│ [ <header.framer-bg7hsc> (1440x110px) | Overview · Index · Archive · ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.framer-1xtxml1> (w=1440px)                    | │
│ | H1: Casa Momo – Designer Apartments in Graz                        | │
│ | Substrate: #0e1201 | Ink: #fff0ca | Accent: #ffffff                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.framer-chahzh>) max-w: 1344px              | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Boutique N°1                 |  | Boutique N°2                 | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.framer-mefgjz>) — Boutique N°3             | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.framer-18na9) | https://www.casamomo.at/             │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 12px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.framer-bg7hsc>  ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.framer-1xtxml1>) — 390px Vertical Lead        | │
│ | H1: Casa Momo – Designer Apartments in Graz                        | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.framer-chahzh) — 1-Col Stack              | │
│ | [ Item 1: Boutique N°1                                           ] | │
│ | [ Item 2: Boutique N°2                                           ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.framer-mefgjz>) — 1-Col (Boutique N°3)      | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.framer-18na9) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.framer-bg7hsc> — `www-casamomo-at`)**:
   - Landmark `<header class="framer-bg7hsc">` (`1440x110px`) hosting `Casa Momo • Boutique Apartments in G` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-redirect-timezone="1"`, `data-framer-font-css`, `data-framer-css-ssr-minified`, `data-framer-components="framer-lib-cursors-ho..."`), and stylesheet rule `main { box-sizing:border-box;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.framer-1xtxml1> — `Casa Momo – Designer Apartments in`)**:
   - Landmark `<section class="framer-1xtxml1">` presenting display lead `Casa Momo – Designer Apartments in Graz` and copy excerpt *"Book Your Stay B B B o o o o o o k k k Y Y Y o o o u u u r r r S "* over `#0e1201` canvas and `#fff0ca` ink.
3. **Primary Showcase & Content Grid (<section.framer-chahzh> — `Boutique N°1`)**:
   - Landmark `<section class="framer-chahzh">` rendering section `Boutique N°1` with copy *"Boutique Apartments in the Historic Center of Graz"*, asset references (`1i2kLqAOiU4EMx2iRruplpXhvgs.png`, `SaAMBRSDzmk41xPyN78AdKzfnM.png`, `NVhSQp5HYf1e4Zkg5QjllUhdYXM.png`, `eegZ1ZoVjnHyJtxDMTEhJ2Bhf4.woff2`), and grid rule `root { -webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale }`.
4. **Interactive Detail & Feature Matrix (<section.framer-mefgjz> — `Boutique N°2`)**:
   - Landmark `<section class="framer-mefgjz">` framing `Boutique N°2` and `Boutique N°3` (*"I am the head and heart behind Casa Momo and hosting is what I lo"*) with `#964317` surface cards, `#ffffff` accents, and `button { font-family:sans-serif;font-size:12px }`.
5. **Colophon & Global Directory Footer (<footer.framer-18na9ah> — `https://www.casamomo.at/`)**:
   - Landmark `<footer class="framer-18na9ah">` anchoring `Casa Momo • Boutique Apartments ` footer links (`Overview · Index · Archive · About · Contact`), copy *"5.00 / 5 “Moritz is such a gentle and wonderful host! The ap"*, and `#000000` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-casamomo-at (Casa Momo • Boutique Apartments in Graz)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-casamomo-at` (**Casa Momo • Boutique Apartments in Graz** — `https://www.casamomo.at/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#0e1201` canvas, `#fff0ca` ink, `#ffffff` accent).
- **Identity & Domain Context**: Personally designed apartments for short and longer stays, between quiet minimalism and warm coziness. Discover boutique, garden, loft an...
- **Primary Substrate**: `#0e1201` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#fff0ca`, **Accent / Highlight**: `#ffffff`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#0e1201` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#fff0ca` primary typography and `#ffffff` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Inter` for display copy (`Casa Momo – Designer Apartments in G`) with `Lay Grotesk Regular` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1344px` container bounds (`gap: 12px`, padding `256px`) with `cubic-bezier(0.66,0,0,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-casamomo-at` in your global stylesheet:

:root {
  /* Casa Momo • Boutique Apartments in Graz (www-casamomo-at) — Live-Grounded CSS Variables */
  --casa-p1-size: calc(var(--casa-page-w, 100vw) * 0.020000); /* Layout / Spatial Grid Token (www-casamomo-at) */
  --casa-p1-lh: 1.2em; /* Dimension / Scale Token (www-casamomo-at) */
  --casa-p1-ls: -0.2px; /* Dimension / Scale Token (www-casamomo-at) */
  --token-8ecd7124-9686-4bd8-bf72-4f81314652d2: #fff0ca; /* Color / Atmospheric Token (www-casamomo-at) */
  --token-a0f3f7f0-2bee-4607-a7b2-647fda358cb3: #0e1201; /* Color / Atmospheric Token (www-casamomo-at) */
  --token-11878163-64ae-441d-8311-9e9d670023d9: #ffe3d4; /* Color / Atmospheric Token (www-casamomo-at) */
  --token-419394a1-565d-4952-8ba3-b4f1eb92339c: #050505; /* Color / Atmospheric Token (www-casamomo-at) */
  --token-bf966309-2582-4df8-98f4-f091ce81e703: #131415; /* Color / Atmospheric Token (www-casamomo-at) */
  --token-86299043-b8f8-4618-9585-4835ac76e9b7: #bc6f45; /* Color / Atmospheric Token (www-casamomo-at) */
  --token-0da0c5a6-8028-40b0-8315-7bce946c6731: #131415; /* Color / Atmospheric Token (www-casamomo-at) */
  --token-20608b9f-0145-4a1e-b971-ee948ebbb015: #fff; /* Color / Atmospheric Token (www-casamomo-at) */
  --token-e00ea664-9c78-44de-bf9c-6839d671d9c2: #050505; /* Color / Atmospheric Token (www-casamomo-at) */
  --token-31f69385-9489-4b68-a801-60367d4b1ac3: #0e1201; /* Color / Atmospheric Token (www-casamomo-at) */
  --text-decoration-skip-ink: var(--framer-text-decoration-skip-ink); /* Typography Ink Token (www-casamomo-at) */
  --text-underline-offset: var(--framer-text-decoration-offset); /* Typography Ink Token (www-casamomo-at) */
  --font-family: var(--framer-font-family); /* Typography / Scale Token (www-casamomo-at) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#0e1201` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#fff0ca` — grounded in live computed `p` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#964317` — grounded in live computed `footer` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#ffffff` — grounded in `#__framer-editorbar-button { color: #ffffff }`
- **Secondary / Muted Copy**: `#000000` — grounded in live computed `nav` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#000000` — grounded in hairline divider derived from live computed `nav` `color` (`computed_styles.json`)
- **Variable Token (`--token-11878163-64ae-441d-8311-9e9d670023d9`)**: `#ffe3d4` — grounded in `var(--token-11878163-64ae-441d-8311-9e9d670023d9)` in `:root`
- **Variable Token (`--token-419394a1-565d-4952-8ba3-b4f1eb92339c`)**: `#050505` — grounded in `var(--token-419394a1-565d-4952-8ba3-b4f1eb92339c)` in `:root`
- **Variable Token (`--token-bf966309-2582-4df8-98f4-f091ce81e703`)**: `#131415` — grounded in `var(--token-bf966309-2582-4df8-98f4-f091ce81e703)` in `:root`
- **Variable Token (`--token-86299043-b8f8-4618-9585-4835ac76e9b7`)**: `#bc6f45` — grounded in `var(--token-86299043-b8f8-4618-9585-4835ac76e9b7)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1344px` (measured widest bounded `<section>` landmark width on `1440px` desktop)
- **Padding & Gutters**: `256px` lateral canvas padding with `12px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1344px`, `gap: 12px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `256px` horizontal padding
- **Media Queries**: `@media (max-width:809px) and (min-width:0)`, `@media (max-width:809.98px)`, `@media (min-width:810px) and (max-width:1599.98px)`, `@media (max-width: 809.98px)`
- **Corner Radii**: `2px`, `64px`, `8px`, `15px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Lay Grotesk Regular`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 16px`, `line-height: 19.2px`, `font-weight: 400`)
- **H2 Section Rule**: live computed `h2` (`font-size: 72px`, `line-height: 72px`, `font-weight: 400`, `letter-spacing: -0.9px`)
- **Body Copy Rule**: live computed `body` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 13px`, `line-height: 100%`, `letter-spacing: 0px`, `font-weight: 400`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); CSS variables `--letter-spacing: var(--framer-letter-spacing)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-casamomo-at` (`Casa Momo • Boutique Apartments in Graz`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.framer-bg7hsc> — `www-casamomo-at`)**:
   - DOM & Selectors: Landmark `<header class="framer-bg7hsc">` (`1440x110px`) hosting `Casa Momo • Boutique Apartments in G` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-redirect-timezone="1"`, `data-framer-font-css`, `data-framer-css-ssr-minified`, `data-framer-components="framer-lib-cursors-ho..."`), and stylesheet rule `main { box-sizing:border-box;margin:0;padding:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.framer-bg7hsc> — `www-casamomo-at`)` (`www-casamomo-at`) adapts across `@media (max-width:809px) and (min-width:0)`, `@media (max-width:809.98px)`, `@media (min-width:810px) and (max-width:1599.98px)`, `@media (max-width: 809.98px)` with `cubic-bezier(0.66,0,0,1)`, `cubic-bezier(0.45,0,0.55,1)`, `cubic-bezier(0.52,0,0,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<section.framer-1xtxml1> — `Casa Momo – Designer Apartments in`)**:
   - DOM & Selectors: Landmark `<section class="framer-1xtxml1">` presenting display lead `Casa Momo – Designer Apartments in Graz` and copy excerpt *"Book Your Stay B B B o o o o o o k k k Y Y Y o o o u u u r r r S "* over `#0e1201` canvas and `#fff0ca` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#0e1201` background with `#fff0ca` headline `Casa Momo – Designer Apartments in Graz`.
3. **Primary Showcase & Content Grid (<section.framer-chahzh> — `Boutique N°1`)**:
   - DOM & Selectors: Landmark `<section class="framer-chahzh">` rendering section `Boutique N°1` with copy *"Boutique Apartments in the Historic Center of Graz"*, asset references (`1i2kLqAOiU4EMx2iRruplpXhvgs.png`, `SaAMBRSDzmk41xPyN78AdKzfnM.png`, `NVhSQp5HYf1e4Zkg5QjllUhdYXM.png`, `eegZ1ZoVjnHyJtxDMTEhJ2Bhf4.woff2`), and grid rule `root { -webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.framer-chahzh> — `Boutique N°1`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1344px`, `gap: 12px`) on desktop and Single-column vertical stack at `390px` viewport width with `256px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.framer-mefgjz> — `Boutique N°2`)**:
   - DOM & Selectors: Landmark `<section class="framer-mefgjz">` framing `Boutique N°2` and `Boutique N°3` (*"I am the head and heart behind Casa Momo and hosting is what I lo"*) with `#964317` surface cards, `#ffffff` accents, and `button { font-family:sans-serif;font-size:12px }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.framer-mefgjz> — `Boutique N°2`)` uses `2px`, `64px`, `8px`, `15px` radii, `#ffffff` highlights, and assets (1i2kLqAOiU4EMx2iRruplpXhvgs.png, SaAMBRSDzmk41xPyN78AdKzfnM.png, NVhSQp5HYf1e4Zkg5QjllUhdYXM.png).
5. **Colophon & Global Directory Footer (<footer.framer-18na9ah> — `https://www.casamomo.at/`)**:
   - DOM & Selectors: Landmark `<footer class="framer-18na9ah">` anchoring `Casa Momo • Boutique Apartments ` footer links (`Overview · Index · Archive · About · Contact`), copy *"5.00 / 5 “Moritz is such a gentle and wonderful host! The ap"*, and `#000000` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.framer-18na9ah> — `https://www.casamomo.at/`)` aligns to `1344px` (measured widest bounded `<section>` landmark width on `1440px` desktop) with `256px` lateral canvas padding with `12px` grid gap and attributes (data-redirect-timezone="1", data-framer-font-css, data-framer-css-ssr-minified).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Book Your Stay B B B o o o o o o k k k Y Y Y o o o u u u r r r S S S t t t a a a y..."*
- Copy Excerpt 2: *"Boutique Apartments in the Historic Center of Graz"*
- Copy Excerpt 3: *"I am the head and heart behind Casa Momo and hosting is what I love most. I've enj..."*
- Copy Excerpt 4: *"5.00 / 5 “Moritz is such a gentle and wonderful host! The apartment is absolutely..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.66,0,0,1)`, `cubic-bezier(0.45,0,0.55,1)`, `cubic-bezier(0.52,0,0,1)`
- **Extracted Stylesheet Rules (`www-casamomo-at`)**:
- `main { box-sizing:border-box;margin:0;padding:0 }`
- `root { -webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale }`
- `button { font-family:sans-serif;font-size:12px }`
- `body { --framer-will-change-override:transform }`
- `h6 span { display:block }`
- **Per-Selector Transition Rules**:
- **Selector `media (prefers-reduced-motion: re...`**: `transition: .01ms!important` extracted from `www-casamomo-at` stylesheet.
- **Selector `#__framer-editorbar-label`**: `transition: opacity 0.4s ease-out` extracted from `www-casamomo-at` stylesheet.
- **Selector `data-framer-name="Menu Overlay"]`**: `transition: visibility 0s linear 0.6s,display 0s linear 0.6s` extracted from `www-casamomo-at` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.66,0,0,1)`)**: Governs interactive state transitions across `<header.framer-bg7hsc>` and `<section.framer-chahzh>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline, Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-casamomo-at`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
