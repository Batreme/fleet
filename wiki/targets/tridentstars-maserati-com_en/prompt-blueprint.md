---
title: "UI Prompt Blueprint: tridentstars-maserati-com_en"
date: 2026-11-23
captured_at: 2026-11-23
target: "tridentstars-maserati-com_en"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#2285f7`)"
---

# UI Design System & Master Generation Blueprint: tridentstars-maserati-com_en

> **Discover Maserati’s Trident Constellation in the Sky** (https://tridentstars.maserati.com/en/) — A real constellation of stars created to celebrate 100 years of vision, performance and iconic design.

![Desktop Viewport Capture (1440x900)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Discover Maserati’s Trident Constellation in the Sky** (`https://tridentstars.maserati.com/en/`). A real constellation of stars created to celebrate 100 years of vision, performance and iconic design.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#2285f7`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#000000` (live computed `html` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#2285f7` accents.
  - **Grounded Typographic Hierarchy**: Pairs `TWK Everett` for display copy (`100 YEARS OF THE TRIDENT LOGO 1 0 0 `) with `TWK Everett` and `Roboto Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `96rem` container bounds (`gap: 1rem`, padding `24px`) with `cubic-bezier(.4,0,1,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x844)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×900px` (`assets/desktop.png`, single-viewport 100vh live capture (900px)), Mobile `390×844px` (`assets/mobile.png`, single-viewport 100vh live capture (844px)).
- **Master Container Bounds**: `96rem` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `24px` lateral canvas padding with `1rem` grid gap.
- **Border Radius Scale**: `var(--radius-2xl)`, `var(--radius-xl)`, `64px`, `9999px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: 1rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `24px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:27.5rem)`, `@media (min-width:40rem)`, `@media (min-width:51.25rem)`, `@media (min-width:64rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#2d2d2d` | `var(--tl-thumb-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#2285f7` | `etrust-pc-sdk #clear-filters-ha... { color: #2285f7 }` |
| **Secondary / Muted Copy** | `#78808e` | `.ot-leg-btn-container .ot-inact... { color: #78808e }` |
| **Structural Hairline Border** | `#2d2d2d` | `var(--tl-border-color)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--easing` | `cubic-brazier(.19,.39,0,1.04)` | Motion / Easing Token |
| `--tl-border-color` | `#2d2d2d` | Brand / Palette Token |
| `--tl-thumb-bg` | `#2d2d2d` | Canvas / Surface Token |
| `--spin` | `0deg` | Design System Custom Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-xl` | `36rem` | Layout / Spatial Grid Token |
| `--container-3xl` | `48rem` | Layout / Spatial Grid Token |
| `--text-sm` | `.875rem` | Typography Ink Token |
| `--text-sm--line-height` | `1.42857` | Typography Ink Token |
| `--text-xl` | `1.25rem` | Typography Ink Token |
| `--text-xl--line-height` | `1.4` | Typography Ink Token |
| `--text-2xl` | `1.5rem` | Typography Ink Token |
| `--text-2xl--line-height` | `1.33333` | Typography Ink Token |
| `--font-weight-medium` | `500` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `TWK Everett`.
- **Primary Body Stack**: `TWK Everett`.
- **Technical / Metadata Stack**: `Roboto Mono`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 64px`, `line-height: 64px`, `font-weight: 200`); rule `h1` (`font-size: 1.5rem`, `line-height: 1.2`).
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: 1.33333`; rule `h2` (`font-size: 1.5rem`, `line-height: 1.25`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 300`); rule `p` (`font-size: .75em`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 11px`, `line-height: 15px`, `font-weight: 500`, `letter-spacing: 1px`); CSS variables `--text-sm: .875rem`, `--text-sm--line-height: 1.42857`, `--default-mono-font-family: var(--font-mono)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `tridentstars-maserati-com_en` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-duration,var(--default-transition-duration))` extracted from `tridentstars-maserati-com_en` stylesheet.
- **Selector `.transition-\[color\]`**: `transition: var(--tw-duration,var(--default-transition-duration))` extracted from `tridentstars-maserati-com_en` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.top-0>` and `<section.ot-hide>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Discover Maserati’s Trident Constellation  │
│ ====================================================================== │
│ [ <header.top-0> (1440x90px)          | the manifesto · discover mor ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.ot-sdk-row> (w=1440px)                        | │
│ | H1: 100 YEARS OF THE TRIDENT LOGO 1 0 0 Y E A R S O F...           | │
│ | Substrate: #000000 | Ink: #ffffff | Accent: #2285f7                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.ot-hide>) max-w: 96rem                     | │
│ | +------------------------------+  +------------------------------+ | │
│ | | SCROLL TO EXPLORE THE TRIDEN |  | 100 YEARS OF THE TRIDENT LOG | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.left-0>) — 100 YEARS OF THE TRID           | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.z-header>   ) | https://tridentstars.maserati.com/e  │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 1rem)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.top-0>          ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.ot-sdk-row>) — 390px Vertical Lead            | │
│ | H1: 100 YEARS OF THE TRIDENT LOGO 1 0 0 Y E A R S O F...           | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.ot-hide>) — 1-Col Stack                   | │
│ | [ Item 1: SCROLL TO EXPLORE THE TRIDENT CONSTELLATION            ] | │
│ | [ Item 2: 100 YEARS OF THE TRIDENT LOGO 1 0 0 Y E A R S O        ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.left-0>) — 1-Col (100 YEARS OF THE T)       | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.z-header>   ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.top-0> — `tridentstars-maserati-com_en`)**:
   - Landmark `<header class="top-0 right-0">` (`1440x90px`) hosting `Discover Maserati’s Trident Constell` navigation (`the manifesto · discover more`), DOM attributes (`data-domain-script="81be852f-f22f-496a-87..."`, `data-document-language="true"`, `data-hid="adobe-launch"`, `data-hid="adobe-data-layer"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.ot-sdk-row> — `100 YEARS OF THE TRIDENT LOGO 1 0 `)**:
   - Landmark `<section class="ot-sdk-row ot-cat-grp">` presenting display lead `100 YEARS OF THE TRIDENT LOGO 1 0 0 Y E A R S O F...` and copy excerpt *"SCROLL TO EXPLORE THE TRIDENT CONSTELLATION"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.ot-hide> — `SCROLL TO EXPLORE THE TRIDENT CONS`)**:
   - Landmark `<section class="ot-hide ot-hosts-ui">` rendering section `SCROLL TO EXPLORE THE TRIDENT CONSTELLATION` with copy *"100 YEARS OF THE TRIDENT LOGO 1 0 0 Y E A R S O F T H E T R I D E"*, asset references (`entry.Btz3ffrH.css`, `default.CffeYOeI.css`, `MoleculesExternalLink.BgGEM1Uz.css`, `MoleculesPopup.CyDrrBxz.css`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.left-0> — `100 YEARS OF THE TRIDENT LOGO 1 0 `)**:
   - Landmark `<section class="left-0">` framing `100 YEARS OF THE TRIDENT LOGO 1 0 0 Y E A R S O ` and `100 YEARS OF THE TRIDENT LOGO` (*"100 YEARS OF THE TRIDENT LOGO"*) with `#2d2d2d` surface cards, `#2285f7` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.z-header> — `https://tridentstars.maserati.com/en/`)**:
   - Landmark `<footer class="z-header">` anchoring `Discover Maserati’s Trident Cons` footer links (`the manifesto · discover more`), copy *"1 0 0 Y E A R S O F T H E T R I D E N T L O G O"*, and `#2d2d2d` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: tridentstars-maserati-com_en (Discover Maserati’s Trident Constellation in the Sky)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `tridentstars-maserati-com_en` (**Discover Maserati’s Trident Constellation in the Sky** — `https://tridentstars.maserati.com/en/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#2285f7`).
- **Identity & Domain Context**: A real constellation of stars created to celebrate 100 years of vision, performance and iconic design.
- **Primary Substrate**: `#000000` (live computed `html` `background-color` (`computed_styles.json`)), **Primary Ink**: `#ffffff`, **Accent / Highlight**: `#2285f7`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#000000` (live computed `html` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#2285f7` accents.
  - **Grounded Typographic Hierarchy**: Pairs `TWK Everett` for display copy (`100 YEARS OF THE TRIDENT LOGO 1 0 0 `) with `TWK Everett` and `Roboto Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `96rem` container bounds (`gap: 1rem`, padding `24px`) with `cubic-bezier(.4,0,1,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `tridentstars-maserati-com_en` in your global stylesheet:

:root {
  /* Discover Maserati’s Trident Constellation in the Sky (tridentstars-maserati-com_en) — Live-Grounded CSS Variables */
  --easing: cubic-brazier(.19,.39,0,1.04); /* Motion / Easing Token (tridentstars-maserati-com_en) */
  --tl-border-color: #2d2d2d; /* Brand / Palette Token (tridentstars-maserati-com_en) */
  --tl-thumb-bg: #2d2d2d; /* Canvas / Surface Token (tridentstars-maserati-com_en) */
  --spin: 0deg; /* Design System Custom Token (tridentstars-maserati-com_en) */
  --color-black: #000; /* Canvas / Surface Token (tridentstars-maserati-com_en) */
  --color-white: #fff; /* Canvas / Surface Token (tridentstars-maserati-com_en) */
  --spacing: .25rem; /* Layout / Spatial Grid Token (tridentstars-maserati-com_en) */
  --container-xl: 36rem; /* Layout / Spatial Grid Token (tridentstars-maserati-com_en) */
  --container-3xl: 48rem; /* Layout / Spatial Grid Token (tridentstars-maserati-com_en) */
  --text-sm: .875rem; /* Typography Ink Token (tridentstars-maserati-com_en) */
  --text-sm--line-height: 1.42857; /* Typography Ink Token (tridentstars-maserati-com_en) */
  --text-xl: 1.25rem; /* Typography Ink Token (tridentstars-maserati-com_en) */
  --text-xl--line-height: 1.4; /* Typography Ink Token (tridentstars-maserati-com_en) */
  --text-2xl: 1.5rem; /* Typography Ink Token (tridentstars-maserati-com_en) */
  --text-2xl--line-height: 1.33333; /* Typography Ink Token (tridentstars-maserati-com_en) */
  --font-weight-medium: 500; /* Typography / Scale Token (tridentstars-maserati-com_en) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000000` — grounded in live computed `html` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#ffffff` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#2d2d2d` — grounded in `var(--tl-thumb-bg)` in `:root`
- **Interactive Accent / Highlight**: `#2285f7` — grounded in `etrust-pc-sdk #clear-filters-ha... { color: #2285f7 }`
- **Secondary / Muted Copy**: `#78808e` — grounded in `.ot-leg-btn-container .ot-inact... { color: #78808e }`
- **Structural Hairline Border**: `#2d2d2d` — grounded in `var(--tl-border-color)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×900px` (single-viewport 100vh live capture (900px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×844px` (single-viewport 100vh live capture (844px), `390px` standard mobile width).
- **Container Max-Width**: `96rem` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `24px` lateral canvas padding with `1rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: 1rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `24px` horizontal padding
- **Media Queries**: `@media (min-width:27.5rem)`, `@media (min-width:40rem)`, `@media (min-width:51.25rem)`, `@media (min-width:64rem)`
- **Corner Radii**: `var(--radius-2xl)`, `var(--radius-xl)`, `64px`, `9999px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `TWK Everett`
- **Body Font Stack**: `TWK Everett`
- **Monospace / Technical Font Stack**: `Roboto Mono`
- **H1 Display Rule**: live computed `h1` (`font-size: 64px`, `line-height: 64px`, `font-weight: 200`); rule `h1` (`font-size: 1.5rem`, `line-height: 1.2`)
- **H2 Section Rule**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: 1.33333`; rule `h2` (`font-size: 1.5rem`, `line-height: 1.25`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 300`); rule `p` (`font-size: .75em`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 11px`, `line-height: 15px`, `font-weight: 500`, `letter-spacing: 1px`); CSS variables `--text-sm: .875rem`, `--text-sm--line-height: 1.42857`, `--default-mono-font-family: var(--font-mono)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `tridentstars-maserati-com_en` (`Discover Maserati’s Trident Constellation in the Sky`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.top-0> — `tridentstars-maserati-com_en`)**:
   - DOM & Selectors: Landmark `<header class="top-0 right-0">` (`1440x90px`) hosting `Discover Maserati’s Trident Constell` navigation (`the manifesto · discover more`), DOM attributes (`data-domain-script="81be852f-f22f-496a-87..."`, `data-document-language="true"`, `data-hid="adobe-launch"`, `data-hid="adobe-data-layer"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.top-0> — `tridentstars-maserati-com_en`)` (`tridentstars-maserati-com_en`) adapts across `@media (min-width:27.5rem)`, `@media (min-width:40rem)`, `@media (min-width:51.25rem)`, `@media (min-width:64rem)` with `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `the manifesto · discover more`.
2. **Hero Stage & Focal Lead (<section.ot-sdk-row> — `100 YEARS OF THE TRIDENT LOGO 1 0 `)**:
   - DOM & Selectors: Landmark `<section class="ot-sdk-row ot-cat-grp">` presenting display lead `100 YEARS OF THE TRIDENT LOGO 1 0 0 Y E A R S O F...` and copy excerpt *"SCROLL TO EXPLORE THE TRIDENT CONSTELLATION"* over `#000000` canvas and `#ffffff` ink.
   - Responsive Contract: Hero stage (`1440×900px` desktop / `390×844px` mobile) sets `#000000` background with `#ffffff` headline `100 YEARS OF THE TRIDENT LOGO 1 0 0 Y E A R S O F...`.
3. **Primary Showcase & Content Grid (<section.ot-hide> — `SCROLL TO EXPLORE THE TRIDENT CONS`)**:
   - DOM & Selectors: Landmark `<section class="ot-hide ot-hosts-ui">` rendering section `SCROLL TO EXPLORE THE TRIDENT CONSTELLATION` with copy *"100 YEARS OF THE TRIDENT LOGO 1 0 0 Y E A R S O F T H E T R I D E"*, asset references (`entry.Btz3ffrH.css`, `default.CffeYOeI.css`, `MoleculesExternalLink.BgGEM1Uz.css`, `MoleculesPopup.CyDrrBxz.css`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.ot-hide> — `SCROLL TO EXPLORE THE TRIDENT CONS`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: 1rem`) on desktop and Single-column vertical stack at `390px` viewport width with `24px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.left-0> — `100 YEARS OF THE TRIDENT LOGO 1 0 `)**:
   - DOM & Selectors: Landmark `<section class="left-0">` framing `100 YEARS OF THE TRIDENT LOGO 1 0 0 Y E A R S O ` and `100 YEARS OF THE TRIDENT LOGO` (*"100 YEARS OF THE TRIDENT LOGO"*) with `#2d2d2d` surface cards, `#2285f7` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.left-0> — `100 YEARS OF THE TRIDENT LOGO 1 0 `)` uses `var(--radius-2xl)`, `var(--radius-xl)`, `64px`, `9999px` radii, `#2285f7` highlights, and assets (entry.Btz3ffrH.css, default.CffeYOeI.css, MoleculesExternalLink.BgGEM1Uz.css).
5. **Colophon & Global Directory Footer (<footer.z-header> — `https://tridentstars.maserati.com/en/`)**:
   - DOM & Selectors: Landmark `<footer class="z-header">` anchoring `Discover Maserati’s Trident Cons` footer links (`the manifesto · discover more`), copy *"1 0 0 Y E A R S O F T H E T R I D E N T L O G O"*, and `#2d2d2d` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.z-header> — `https://tridentstars.maserati.com/en/`)` aligns to `96rem` (non-`@media` desktop container stylesheet rule) with `24px` lateral canvas padding with `1rem` grid gap and attributes (data-domain-script="81be852f-f22f-496a-87...", data-document-language="true", data-hid="adobe-launch").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"SCROLL TO EXPLORE THE TRIDENT CONSTELLATION"*
- Copy Excerpt 2: *"100 YEARS OF THE TRIDENT LOGO 1 0 0 Y E A R S O F T H E T R I D E N T L O G O"*
- Copy Excerpt 3: *"100 YEARS OF THE TRIDENT LOGO"*
- Copy Excerpt 4: *"1 0 0 Y E A R S O F T H E T R I D E N T L O G O"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`tridentstars-maserati-com_en`)**:
- `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- `sup { vertical-align:baseline;font-size:75%;line-height:0;position:relative }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `tridentstars-maserati-com_en` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-duration,var(--default-transition-duration))` extracted from `tridentstars-maserati-com_en` stylesheet.
- **Selector `.transition-\[color\]`**: `transition: var(--tw-duration,var(--default-transition-duration))` extracted from `tridentstars-maserati-com_en` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.top-0>` and `<section.ot-hide>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `tridentstars-maserati-com_en`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
