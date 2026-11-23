---
title: "UI Prompt Blueprint: www-norddeutscher-figuralchor-de"
date: 2026-11-23
captured_at: 2026-11-23
target: "www-norddeutscher-figuralchor-de"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#c9a85e` accent)"
---

# UI Design System & Master Generation Blueprint: www-norddeutscher-figuralchor-de

> **Norddeutscher Figuralchor Hannover — Kammerchor seit 1981** (https://www.norddeutscher-figuralchor.de) — Norddeutscher Figuralchor Hannover — semiprofessioneller Kammerchor seit 1981 unter Jörg Straube. Konzerte, CD-Einspielungen und Mitsinge...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Norddeutscher Figuralchor Hannover — Kammerchor seit 1981** (`https://www.norddeutscher-figuralchor.de`). Norddeutscher Figuralchor Hannover — semiprofessioneller Kammerchor seit 1981 unter Jörg Straube. Konzerte, CD-Einspielungen und Mitsinge...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#c9a85e` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#c9a85e` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Syne` for display copy (`Norddeutscher Figuralchor — Kammerch`) with `Syne` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 3.6px`, padding `2vw`) with `cubic-bezier(0.4,0,0.2,1)` easing and GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport).
- **Canvas Lateral Padding & Spacing**: `2vw` lateral canvas padding with `3.6px` grid gap.
- **Border Radius Scale**: `50%`, `0.25rem`, `16px`, `8px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 3.6px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `2vw` horizontal padding.
- **Extracted CSS Media Queries**: `@media (width >= 40rem)`, `@media (width >= 48rem)`, `@media (width >= 64rem)`, `@media (width >= 80rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#e6cac7` | live computed `header` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#c9a85e` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#c9a85e` | live computed `a` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e3e3e3` | `#navi-top { border: #e3e3e3 }` |
| **Variable Token (`--color-gold`)** | `#bd7716` | `var(--color-gold)` in `:root` |
| **Variable Token (`--color-charcoal`)** | `#404040` | `var(--color-charcoal)` in `:root` |
| **Variable Token (`--color-conductor`)** | `#d3d1de` | `var(--color-conductor)` in `:root` |
| **Variable Token (`--color-silver`)** | `#d6d6d6` | `var(--color-silver)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `ui-sans-serif, system-ui, sans-serif, "Apple Color Emoji",` | Typography / Scale Token |
| `--font-mono` | `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono",` | Typography / Scale Token |
| `--color-white` | `#ffffff` | Canvas / Surface Token |
| `--font-weight-medium` | `500` | Typography / Scale Token |
| `--font-weight-bold` | `700` | Typography / Scale Token |
| `--ease-in-out` | `cubic-bezier(0.4, 0, 0.2, 1)` | Motion / Easing Token |
| `--default-transition-duration` | `150ms` | Motion / Easing Token |
| `--default-transition-timing-function` | `cubic-bezier(0.4, 0, 0.2, 1)` | Motion / Easing Token |
| `--default-font-family` | `var(--font-sans)` | Typography / Scale Token |
| `--default-mono-font-family` | `var(--font-mono)` | Typography / Scale Token |
| `--color-rose` | `#e6cac7` | Brand / Palette Token |
| `--color-gold` | `#bd7716` | Brand / Palette Token |
| `--color-ink` | `#000000` | Typography Ink Token |
| `--color-charcoal` | `#404040` | Brand / Palette Token |
| `--color-conductor` | `#d3d1de` | Brand / Palette Token |
| `--color-silver` | `#d6d6d6` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Syne`.
- **Primary Body Stack**: `Syne`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 0px`, `line-height: 0px`, `font-weight: 400`); CSS variables `--font-display: "Playfair Display", Georgia, serif`.
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 123.84px`, `line-height: 185.76px`, `font-weight: 400`); rule `h2` (`font-size: 8.6vw`, `letter-spacing: 0`, `font-weight: 400`).
- **Body Copy**: live computed `body` (`font-size: 0px`, `line-height: 0px`, `font-weight: 400`); CSS variables `--font-body: "Syne", system-ui, sans-serif`; rule `body` (`font-size: 0`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 43.2px`, `line-height: 64.8px`, `font-weight: 400`); CSS variables `--font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono",`, `--default-mono-font-family: var(--font-mono)`; rule `small` (`font-size: 80%`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.4,0,0.2,1)`, `cubic-bezier(0.25,0.46,0.45,0.94)`, `cubic-bezier(0.65,0,0.35,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: 150ms` extracted from `www-norddeutscher-figuralchor-de` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease, var(--default-transition-timing-function))` extracted from `www-norddeutscher-figuralchor-de` stylesheet.
- **Selector `.transition-colors`**: `transition: var(--tw-ease, var(--default-transition-timing-function))` extracted from `www-norddeutscher-figuralchor-de` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.4,0,0.2,1)`)**: Governs interactive state transitions across `<header.bg-rose>` and `<section.bg-white:nth(2)>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Norddeutscher Figuralchor Hannover — Kamme │
│ ====================================================================== │
│ [ <header.bg-rose> (1425x679px)       | Home · Der Chor · Der Dirige ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.bg-white> (w=1440px)                          | │
│ | H1: Norddeutscher Figuralchor — Kammerchor aus Hannover            | │
│ | Substrate: #ffffff | Ink: #000000 | Accent: #c9a85e                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.bg-white:nth(2)>) max-w: 1440px            | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Der Maßstab seit 1981        |  | wird Teil von einem.         | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.bg-charcoal>) — Der Norddeutsche Figu      | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.bg-ink>     ) | https://www.norddeutscher-figuralch  │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 3.6px)      │
│ ====================================================================== │
│ [ HEADER BAR (<header.bg-rose>        ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.bg-white>) — 390px Vertical Lead              | │
│ | H1: Norddeutscher Figuralchor — Kammerchor aus Hannover            | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.bg-white:nth() — 1-Col Stack              | │
│ | [ Item 1: Der Maßstab seit 1981                                  ] | │
│ | [ Item 2: wird Teil von einem.                                   ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.bg-charcoal>) — 1-Col (Der Norddeutsche F)  | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.bg-ink>     ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.bg-rose> — `www-norddeutscher-figuralchor-de`)**:
   - Landmark `<header class="bg-rose relative">` (`1425x679px`) hosting `Norddeutscher Figuralchor Hannover —` navigation (`Home · Der Chor · Der Dirigent · Konzerte · CDs`), DOM attributes (`data-infos="konzerte.html"`, `data-email="a29udGFrdEBub3JkZGV1d..."`, `data-email="a29udGFrdEBub3JkZGV1d..."`, `data-email="a29udGFrdEBub3JkZGV1d..."`), and stylesheet rule `file-selector-button { box-sizing: border-box; margin: 0; padding: 0; border: 0 solid; }`.
2. **Hero Stage & Focal Lead (<section.bg-white> — `Norddeutscher Figuralchor — Kammer`)**:
   - Landmark `<section class="bg-white overflow-hidden">` presenting display lead `Norddeutscher Figuralchor — Kammerchor aus Hannover` and copy excerpt *"Der Maßstab seit 1981"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.bg-white:nth(2)> — `Der Maßstab seit 1981`)**:
   - Landmark `<section class="bg-white">` rendering section `Der Maßstab seit 1981` with copy *"wird Teil von einem."*, asset references (`favicon-home.svg`, `favicon.ico`, `apple-touch-icon.png`, `PlayfairDisplay-Regular.woff2`), and grid rule `hr { height: 0; color: inherit; border-top-width: 1px; }`.
4. **Interactive Detail & Feature Matrix (<section.bg-charcoal> — `wird Teil von einem.`)**:
   - Landmark `<section class="bg-charcoal">` framing `wird Teil von einem.` and `Der Norddeutsche Figuralchor gestaltet seit 1981` (*"Der Norddeutsche Figuralchor gestaltet seit 1981 Konzerte, die Me"*) with `#e6cac7` surface cards, `#c9a85e` accents, and `h6 { font-size: inherit; font-weight: inherit; }`.
5. **Colophon & Global Directory Footer (<footer.bg-ink> — `https://www.norddeutscher-figuralchor.de`)**:
   - Landmark `<footer class="bg-ink">` anchoring `Norddeutscher Figuralchor Hannov` footer links (`Home · Der Chor · Der Dirigent · Konzerte · CDs`), copy *"// 5 x Echo Klassik // Deutscher Chorwettbewerb // Brahms-We"*, and `#e3e3e3` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-norddeutscher-figuralchor-de (Norddeutscher Figuralchor Hannover — Kammerchor seit 1981)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-norddeutscher-figuralchor-de` (**Norddeutscher Figuralchor Hannover — Kammerchor seit 1981** — `https://www.norddeutscher-figuralchor.de`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#c9a85e` accent).
- **Identity & Domain Context**: Norddeutscher Figuralchor Hannover — semiprofessioneller Kammerchor seit 1981 unter Jörg Straube. Konzerte, CD-Einspielungen und Mitsinge...
- **Primary Substrate**: `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#000000`, **Accent / Highlight**: `#c9a85e`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#c9a85e` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Syne` for display copy (`Norddeutscher Figuralchor — Kammerch`) with `Syne` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 3.6px`, padding `2vw`) with `cubic-bezier(0.4,0,0.2,1)` easing and GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-norddeutscher-figuralchor-de` in your global stylesheet:

:root {
  /* Norddeutscher Figuralchor Hannover — Kammerchor seit 1981 (www-norddeutscher-figuralchor-de) — Live-Grounded CSS Variables */
  --font-sans: ui-sans-serif, system-ui, sans-serif, "Apple Color Emoji",; /* Typography / Scale Token (www-norddeutscher-figuralchor-de) */
  --font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono",; /* Typography / Scale Token (www-norddeutscher-figuralchor-de) */
  --color-white: #ffffff; /* Canvas / Surface Token (www-norddeutscher-figuralchor-de) */
  --font-weight-medium: 500; /* Typography / Scale Token (www-norddeutscher-figuralchor-de) */
  --font-weight-bold: 700; /* Typography / Scale Token (www-norddeutscher-figuralchor-de) */
  --ease-in-out: cubic-bezier(0.4, 0, 0.2, 1); /* Motion / Easing Token (www-norddeutscher-figuralchor-de) */
  --default-transition-duration: 150ms; /* Motion / Easing Token (www-norddeutscher-figuralchor-de) */
  --default-transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1); /* Motion / Easing Token (www-norddeutscher-figuralchor-de) */
  --default-font-family: var(--font-sans); /* Typography / Scale Token (www-norddeutscher-figuralchor-de) */
  --default-mono-font-family: var(--font-mono); /* Typography / Scale Token (www-norddeutscher-figuralchor-de) */
  --color-rose: #e6cac7; /* Brand / Palette Token (www-norddeutscher-figuralchor-de) */
  --color-gold: #bd7716; /* Brand / Palette Token (www-norddeutscher-figuralchor-de) */
  --color-ink: #000000; /* Typography Ink Token (www-norddeutscher-figuralchor-de) */
  --color-charcoal: #404040; /* Brand / Palette Token (www-norddeutscher-figuralchor-de) */
  --color-conductor: #d3d1de; /* Brand / Palette Token (www-norddeutscher-figuralchor-de) */
  --color-silver: #d6d6d6; /* Brand / Palette Token (www-norddeutscher-figuralchor-de) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#000000` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#e6cac7` — grounded in live computed `header` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#c9a85e` — grounded in live computed `a` `color` (`computed_styles.json`)
- **Secondary / Muted Copy**: `#c9a85e` — grounded in live computed `a` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#e3e3e3` — grounded in `#navi-top { border: #e3e3e3 }`
- **Variable Token (`--color-gold`)**: `#bd7716` — grounded in `var(--color-gold)` in `:root`
- **Variable Token (`--color-charcoal`)**: `#404040` — grounded in `var(--color-charcoal)` in `:root`
- **Variable Token (`--color-conductor`)**: `#d3d1de` — grounded in `var(--color-conductor)` in `:root`
- **Variable Token (`--color-silver`)**: `#d6d6d6` — grounded in `var(--color-silver)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport)
- **Padding & Gutters**: `2vw` lateral canvas padding with `3.6px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 3.6px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `2vw` horizontal padding
- **Media Queries**: `@media (width >= 40rem)`, `@media (width >= 48rem)`, `@media (width >= 64rem)`, `@media (width >= 80rem)`
- **Corner Radii**: `50%`, `0.25rem`, `16px`, `8px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Syne`
- **Body Font Stack**: `Syne`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: live computed `h1` (`font-size: 0px`, `line-height: 0px`, `font-weight: 400`); CSS variables `--font-display: "Playfair Display", Georgia, serif`
- **H2 Section Rule**: live computed `h2` (`font-size: 123.84px`, `line-height: 185.76px`, `font-weight: 400`); rule `h2` (`font-size: 8.6vw`, `letter-spacing: 0`, `font-weight: 400`)
- **Body Copy Rule**: live computed `body` (`font-size: 0px`, `line-height: 0px`, `font-weight: 400`); CSS variables `--font-body: "Syne", system-ui, sans-serif`; rule `body` (`font-size: 0`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 43.2px`, `line-height: 64.8px`, `font-weight: 400`); CSS variables `--font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono",`, `--default-mono-font-family: var(--font-mono)`; rule `small` (`font-size: 80%`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-norddeutscher-figuralchor-de` (`Norddeutscher Figuralchor Hannover — Kammerchor seit 1981`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.bg-rose> — `www-norddeutscher-figuralchor-de`)**:
   - DOM & Selectors: Landmark `<header class="bg-rose relative">` (`1425x679px`) hosting `Norddeutscher Figuralchor Hannover —` navigation (`Home · Der Chor · Der Dirigent · Konzerte · CDs`), DOM attributes (`data-infos="konzerte.html"`, `data-email="a29udGFrdEBub3JkZGV1d..."`, `data-email="a29udGFrdEBub3JkZGV1d..."`, `data-email="a29udGFrdEBub3JkZGV1d..."`), and stylesheet rule `file-selector-button { box-sizing: border-box; margin: 0; padding: 0; border: 0 solid; }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.bg-rose> — `www-norddeutscher-figuralchor-de`)` (`www-norddeutscher-figuralchor-de`) adapts across `@media (width >= 40rem)`, `@media (width >= 48rem)`, `@media (width >= 64rem)`, `@media (width >= 80rem)` with `cubic-bezier(0.4,0,0.2,1)`, `cubic-bezier(0.25,0.46,0.45,0.94)`, `cubic-bezier(0.65,0,0.35,1)` transitions and links `Home · Der Chor · Der Dirigent · Konzerte · CDs`.
2. **Hero Stage & Focal Lead (<section.bg-white> — `Norddeutscher Figuralchor — Kammer`)**:
   - DOM & Selectors: Landmark `<section class="bg-white overflow-hidden">` presenting display lead `Norddeutscher Figuralchor — Kammerchor aus Hannover` and copy excerpt *"Der Maßstab seit 1981"* over `#ffffff` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#ffffff` background with `#000000` headline `Norddeutscher Figuralchor — Kammerchor aus Hannover`.
3. **Primary Showcase & Content Grid (<section.bg-white:nth(2)> — `Der Maßstab seit 1981`)**:
   - DOM & Selectors: Landmark `<section class="bg-white">` rendering section `Der Maßstab seit 1981` with copy *"wird Teil von einem."*, asset references (`favicon-home.svg`, `favicon.ico`, `apple-touch-icon.png`, `PlayfairDisplay-Regular.woff2`), and grid rule `hr { height: 0; color: inherit; border-top-width: 1px; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.bg-white:nth(2)> — `Der Maßstab seit 1981`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 3.6px`) on desktop and Single-column vertical stack at `390px` viewport width with `2vw` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.bg-charcoal> — `wird Teil von einem.`)**:
   - DOM & Selectors: Landmark `<section class="bg-charcoal">` framing `wird Teil von einem.` and `Der Norddeutsche Figuralchor gestaltet seit 1981` (*"Der Norddeutsche Figuralchor gestaltet seit 1981 Konzerte, die Me"*) with `#e6cac7` surface cards, `#c9a85e` accents, and `h6 { font-size: inherit; font-weight: inherit; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.bg-charcoal> — `wird Teil von einem.`)` uses `50%`, `0.25rem`, `16px`, `8px` radii, `#c9a85e` highlights, and assets (favicon-home.svg, favicon.ico, apple-touch-icon.png).
5. **Colophon & Global Directory Footer (<footer.bg-ink> — `https://www.norddeutscher-figuralchor.de`)**:
   - DOM & Selectors: Landmark `<footer class="bg-ink">` anchoring `Norddeutscher Figuralchor Hannov` footer links (`Home · Der Chor · Der Dirigent · Konzerte · CDs`), copy *"// 5 x Echo Klassik // Deutscher Chorwettbewerb // Brahms-We"*, and `#e3e3e3` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.bg-ink> — `https://www.norddeutscher-figuralchor.de`)` aligns to `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport) with `2vw` lateral canvas padding with `3.6px` grid gap and attributes (data-infos="konzerte.html", data-email="a29udGFrdEBub3JkZGV1d...", data-email="a29udGFrdEBub3JkZGV1d...").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Der Maßstab seit 1981"*
- Copy Excerpt 2: *"wird Teil von einem."*
- Copy Excerpt 3: *"Der Norddeutsche Figuralchor gestaltet seit 1981 Konzerte, die Menschen bewegen —..."*
- Copy Excerpt 4: *"// 5 x Echo Klassik // Deutscher Chorwettbewerb // Brahms-Wettbewerb Hamburg // 2..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.4,0,0.2,1)`, `cubic-bezier(0.25,0.46,0.45,0.94)`, `cubic-bezier(0.65,0,0.35,1)`
- **Extracted Stylesheet Rules (`www-norddeutscher-figuralchor-de`)**:
- `file-selector-button { box-sizing: border-box; margin: 0; padding: 0; border: 0 solid; }`
- `hr { height: 0; color: inherit; border-top-width: 1px; }`
- `h6 { font-size: inherit; font-weight: inherit; }`
- `strong { font-weight: bolder; }`
- `small { font-size: 80%; }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: 150ms` extracted from `www-norddeutscher-figuralchor-de` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease, var(--default-transition-timing-function))` extracted from `www-norddeutscher-figuralchor-de` stylesheet.
- **Selector `.transition-colors`**: `transition: var(--tw-ease, var(--default-transition-timing-function))` extracted from `www-norddeutscher-figuralchor-de` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.4,0,0.2,1)`)**: Governs interactive state transitions across `<header.bg-rose>` and `<section.bg-white:nth(2)>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-norddeutscher-figuralchor-de`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
